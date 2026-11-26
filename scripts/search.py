#!/usr/bin/env python3
"""Rank library chapters for a query (BM25 over chapter files) and show matching lines.

Usage:
  python3 search.py "query words" [-k 8] [-b book-slug[,slug2]] [-n 3]
    -k  number of chapters to list (default 8)
    -b  restrict to these book folders (e.g. prince-udl,torralba-fcv)
    -n  matching lines to show per chapter (default 3)
Phrases in double quotes inside the query get a bonus, e.g.  '"positional encoding" vit'
"""
import argparse, math, os, re, collections

LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "library")
TOK = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

ap = argparse.ArgumentParser()
ap.add_argument("query")
ap.add_argument("-k", type=int, default=8)
ap.add_argument("-b", default="")
ap.add_argument("-n", type=int, default=3)
a = ap.parse_args()

phrases = [p.lower() for p in re.findall(r'"([^"]+)"', a.query)]
terms = [t for t in TOK.findall(a.query.lower()) if len(t) > 1]
books = set(filter(None, a.b.split(",")))

docs = []
for d in sorted(os.listdir(LIB)):
    p = os.path.join(LIB, d)
    if not os.path.isdir(p) or (books and d not in books):
        continue
    for f in sorted(os.listdir(p)):
        if f.endswith(".md"):
            docs.append(os.path.join(d, f))

tf, lens, df = {}, {}, collections.Counter()
texts = {}
for rel in docs:
    t = open(os.path.join(LIB, rel), encoding="utf-8", errors="replace").read().lower()
    texts[rel] = t
    c = collections.Counter(TOK.findall(t))
    tf[rel] = {q: c[q] for q in terms}
    lens[rel] = sum(c.values()) or 1
    for q in set(terms):
        if c[q]:
            df[q] += 1

N, avg = len(docs), sum(lens.values()) / max(1, len(docs))
scores = {}
for rel in docs:
    s = 0.0
    for q in terms:
        f = tf[rel][q]
        if f:
            idf = math.log(1 + (N - df[q] + 0.5) / (df[q] + 0.5))
            s += idf * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * lens[rel] / avg))
    for ph in phrases:
        s += 3.0 * math.log1p(texts[rel].count(ph))
    title = rel.lower()
    s += sum(1.5 for q in terms if q in title)
    if s > 0:
        scores[rel] = s

top = sorted(scores, key=scores.get, reverse=True)[: a.k]
if not top:
    print("No matches. Try synonyms or fewer words.")
for rel in top:
    path = os.path.join(LIB, rel)
    print(f"\n[{scores[rel]:.1f}] library/{rel}")
    shown = 0
    keys = phrases or terms
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            low = line.lower()
            hits = sum(k in low for k in keys)
            if hits >= max(1, min(2, len(keys))):
                print(f"   L{i}: {line.strip()[:160]}")
                shown += 1
                if shown >= a.n:
                    break
