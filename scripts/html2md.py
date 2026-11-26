"""Convert downloaded HTML chapter files to plain markdown-ish text.
Usage: python3 -I html2md.py OUT.md in1.html in2.html ...
"""
import sys, re, html
from html.parser import HTMLParser

SKIP = {"script", "style", "nav", "head", "noscript", "svg"}
BLOCK = {"p", "div", "br", "li", "tr", "section", "article", "figcaption", "pre", "table", "ul", "ol"}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in SKIP: self.skip += 1
        elif re.fullmatch(r"h[1-6]", tag): self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li": self.out.append("\n- ")
        elif tag in BLOCK: self.out.append("\n")
    def handle_endtag(self, tag):
        if tag in SKIP: self.skip = max(0, self.skip - 1)
        elif re.fullmatch(r"h[1-6]", tag) or tag in BLOCK: self.out.append("\n")
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

out, files = sys.argv[1], sys.argv[2:]
with open(out, "w", encoding="utf-8") as fo:
    for f in files:
        p = P(); p.feed(open(f, encoding="utf-8", errors="replace").read())
        t = "".join(p.out)
        t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
        fo.write(f"\n\n<!-- source: {f.rsplit('/',1)[-1]} -->\n" + t.strip() + "\n")
