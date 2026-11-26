#!/usr/bin/env python3
"""Render PDF pages of a library book to PNG, so equations and figures can be read as they are printed.

Usage:
  python3 page.py <book-slug> <page>[-<page>] [--dpi 150] [--out DIR] [--books DIR]

  <page> is the PDF page number, as in the `<!-- page N -->` markers and the
  `(p.N)` entries of each chapter's `## Sections` list.

Examples:
  python3 page.py prince-udl 360
  python3 page.py bishop-prml 480-481 --dpi 200

The PDFs are looked up in the books folder, in this order:
  --books DIR, $DL_BOOKS_DIR, the path written in <skill>/books_dir.txt, ~/dl-books
(each folder is searched directly and in its Books/ subfolder).
Prints the path of every PNG written. If the PDF is not available locally, or the book is
web-only, prints a link to the official online copy at that page instead.
"""
import argparse, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from books import BOOKS, WEB, ONLINE

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def books_dirs(arg):
    dirs = []
    if arg:
        dirs.append(arg)
    if os.environ.get("DL_BOOKS_DIR"):
        dirs.append(os.environ["DL_BOOKS_DIR"])
    cfg = os.path.join(SKILL, "books_dir.txt")
    if os.path.exists(cfg):
        dirs.append(open(cfg, encoding="utf-8").read().strip())
    dirs.append(os.path.expanduser("~/dl-books"))
    return [os.path.expanduser(d) for d in dirs if d]


def online(slug, pages, reason):
    pdf_url, site = ONLINE.get(slug, (None, None))
    page = pages.partition("-")[0]
    print(reason)
    if pdf_url:
        print(f"ONLINE: {pdf_url}#page={page}")
    else:
        print(f"ONLINE: {site}  (download the PDF there and go to PDF page {page})")
    print("Online editions can be newer than the one indexed, so the page may be off by a few; "
          "search for the section title. To render pages locally, set DL_BOOKS_DIR or write your "
          "books folder into " + os.path.join(SKILL, "books_dir.txt"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("pages")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "dl-research-library-pages"))
    ap.add_argument("--books", default="")
    a = ap.parse_args()

    for base, (slug, disp, url) in WEB.items():
        if slug == a.slug:
            print(f"{disp} is a web book with no PDF. ONLINE: {url} (open the chapter named in the file header)")
            return

    base = next((b for b, (s, _) in BOOKS.items() if s == a.slug), None)
    if base is None:
        sys.exit("unknown book slug: " + a.slug + "\nknown: " + ", ".join(s for s, _ in BOOKS.values()))

    tried = []
    for d in books_dirs(a.books):
        for p in (os.path.join(d, "Books", base + ".pdf"), os.path.join(d, base + ".pdf")):
            tried.append(p)
            if os.path.exists(p):
                pdf = p
                break
        else:
            continue
        break
    else:
        online(a.slug, a.pages, "No local PDF for %s (looked in: %s)." % (a.slug, ", ".join(books_dirs(a.books))))
        return

    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            online(a.slug, a.pages, "PyMuPDF is not installed (pip install pymupdf), so pages cannot be rendered.")
            return
    doc = pymupdf.open(pdf)
    lo, _, hi = a.pages.partition("-")
    lo, hi = int(lo), int(hi or lo)
    if not (1 <= lo <= hi <= doc.page_count):
        sys.exit(f"pages must be within 1-{doc.page_count}")
    if hi - lo > 9:
        sys.exit("render at most 10 pages at a time")
    os.makedirs(a.out, exist_ok=True)
    for n in range(lo, hi + 1):
        out = os.path.join(a.out, f"{a.slug}-p{n}.png")
        doc[n - 1].get_pixmap(dpi=a.dpi).save(out)
        print(out)


if __name__ == "__main__":
    main()
