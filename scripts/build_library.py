"""Split the PDF and web books into chapter-sized markdown files and build INDEX.md.
Usage: python3 build_library.py <project_dir> <skill_dir>
"""
import sys, os, re, glob, warnings
warnings.filterwarnings("ignore")
import fitz

PROJ, SKILL = sys.argv[1], sys.argv[2]
LIB = os.path.join(SKILL, "library")
MAX_PAGES = 120
SKIP = re.compile(r"^(cover|contents|list of (figures|tables|algorithms)|bibliography|references|index|acknowledg|"
                  r"about the author|copyright|dedication|praise|half.?title|title page|exercises$|subject index)", re.I)
PART = re.compile(r"^(part\s+[ivx\d]+\b|[IVX]+\s)", re.I)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from books import BOOKS, WEB  # edit books.py to add a book

def slugify(s, n=60):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower().replace("\r", " ")).strip("-")
    return s[:n].strip("-") or "untitled"

def clean(t):
    t = t.replace("\r", " ").replace("­", "")
    t = re.sub(r"-\n(?=[a-z])", "", t)          # de-hyphenate line breaks
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

index = []  # (book display, slug, [(file, title, sections)])

def emit(slug, n, title, sections, body, header_extra):
    os.makedirs(os.path.join(LIB, slug), exist_ok=True)
    fn = f"{n:02d}-{slugify(title)}.md"
    with open(os.path.join(LIB, slug, fn), "w", encoding="utf-8") as fo:
        fo.write(f"# {title}\n\n{header_extra}\n\n")
        if sections:
            fo.write("## Sections\n" + "\n".join(sections) + "\n\n---\n\n")
        fo.write(body + "\n")
    return fn

# ---------- PDFs ----------
for base, (slug, disp) in BOOKS.items():
    path = os.path.join(PROJ, "Books", base + ".pdf")
    if not os.path.exists(path):
        path = os.path.join(PROJ, base + ".pdf")
    if not os.path.exists(path):
        print("skip (not found):", base + ".pdf"); continue
    doc = fitz.open(path)
    toc = [(l, t.replace("\r", " ").strip(), p) for l, t, p in doc.get_toc() if p > 0]
    N = doc.page_count
    nodes = []
    for i, (l, t, p) in enumerate(toc):
        end = N
        for l2, t2, p2 in toc[i + 1:]:
            if l2 <= l:
                end = max(p, p2 - 1) if p2 > p else p
                break
        kids = []
        for j in range(i + 1, len(toc)):
            if toc[j][0] <= l: break
            kids.append(j)
        nodes.append(dict(level=l, title=t, start=p, end=end, kids=kids, idx=i))

    chosen = []
    def pick(i):
        nd = nodes[i]
        if SKIP.match(nd["title"]): return
        direct = [k for k in nd["kids"] if nodes[k]["level"] == nd["level"] + 1]
        if direct and (nd["end"] - nd["start"] + 1 > MAX_PAGES or PART.match(nd["title"])):
            for k in direct: pick(k)
        else:
            chosen.append(nd)
    for i, nd in enumerate(nodes):
        if nd["level"] == 1: pick(i)

    files = []
    for n, nd in enumerate(chosen, 1):
        secs = ["  " * (nodes[k]["level"] - nd["level"] - 1) + f"- {nodes[k]['title']} (p.{nodes[k]['start']})"
                for k in nd["kids"] if nodes[k]["level"] - nd["level"] <= 2]
        body = "\n\n".join(f"<!-- page {p+1} -->\n" + clean(doc[p].get_text()) for p in range(nd["start"] - 1, nd["end"]))
        hdr = f"Source: {disp} — PDF pages {nd['start']}–{nd['end']}"
        fn = emit(slug, n, nd["title"], secs, body, hdr)
        files.append((fn, nd["title"], [nodes[k]["title"] for k in nd["kids"] if nodes[k]["level"] == nd["level"] + 1]))
    index.append((disp, slug, files))
    print(slug, len(files), "chapters")

# ---------- web books ----------
for base, (slug, disp, _url) in WEB.items():
    src = os.path.join(PROJ, "md", base + ".md")
    if not os.path.exists(src):
        print("skip (not found):", src); continue
    text = open(src, encoding="utf-8").read()
    parts = re.split(r"<!-- source: (\S+?)\.html -->", text)
    files, n = [], 0
    for name, body in zip(parts[1::2], parts[2::2]):
        body = clean(body)
        if len(body.split()) < 150 or name.startswith("part_") or name in ("notations", "notation"):
            if name not in ("notation", "notations"): continue
        n += 1
        if slug == "torralba-fcv":
            m = re.search(r"^# (.+)$", body, re.M)
            title = m.group(1).strip() if m else name.replace("_", " ")
            secs = [h for h in re.findall(r"^## (\d+\.\d+ .+)$", body, re.M)]
        else:
            title = name.replace("_", " ").title()
            m = re.search(r"Chapter\s+(\d+)\s*\n+\s*(.+)", body[:3000])
            if m: title = f"{m.group(1)} {m.group(2).strip()}"
            secs = list(dict.fromkeys(re.findall(r"^(\d{1,2}\.\d{1,2} [A-Z][^\n]{3,70})$", body, re.M)))
        hdr = f"Source: {disp} — web chapter `{name}.html`"
        fn = emit(slug, n, title, ["- " + s for s in secs], body, hdr)
        files.append((fn, title, secs))
    index.append((disp, slug, files))
    print(slug, len(files), "chapters")

with open(os.path.join(LIB, "INDEX.md"), "w", encoding="utf-8") as fo:
    fo.write("# Library index\n\nEvery chapter file in `library/`, with its top-level sections. "
             "Grep this file first to find where a topic lives.\n")
    for disp, slug, files in index:
        fo.write(f"\n## {disp} — `{slug}/`\n\n")
        for fn, title, secs in files:
            s = "; ".join(re.sub(r"\s+", " ", x) for x in secs[:25])
            fo.write(f"- `{slug}/{fn}` — **{title}**" + (f": {s}" if s else "") + "\n")
print("done")
