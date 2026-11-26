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
Prints the path of every PNG written. Web-only books print their website instead.
"""
import argparse, os, sys, tempfile
from books import BOOKS, WEB

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
            sys.exit(f"{disp} is a web book with no PDF. See the chapter on {url}")

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
        sys.exit(f"{base}.pdf not found. Tried:\n  " + "\n  ".join(tried) +
                 "\nSet DL_BOOKS_DIR or write your books folder path into " + os.path.join(SKILL, "books_dir.txt"))

    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
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
