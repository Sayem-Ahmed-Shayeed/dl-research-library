# Contributing

Thanks for helping. This skill is meant to make Claude a better companion for theory-driven research, learning, and justifying ideas from textbooks, so the most useful contributions make its answers more accurate, better sourced or broader in coverage.

## Ways to contribute

- **Add a book.** It must be legally free to download from its authors or publisher (open PDF, arXiv or an official website).
- **Improve the notes** in `notes/`: fix errors, add missing core concepts, or point to a better chapter for a topic.
- **Improve extraction**: better chapter splitting, equation handling or page markers in `scripts/build_library.py`.
- **Improve search** in `scripts/search.py`.
- **Improve `SKILL.md`** so Claude triggers on the right questions and cites more reliably.
- **Report a problem**: a wrong citation, a book whose download link moved, or a build that fails.

## Ground rules

- **Never commit book text.** `library/<book>/` is gitignored for a reason: only the skill, notes, scripts and `library/INDEX.md` are shared. PRs that add copyrighted text will be closed.
- Link only to official sources (author, publisher, arXiv), never to mirrors.
- Notes should be short, written in your own words, and point to chapters as *Book, section (PDF p. N)*. Don't paste paragraphs from the books.
- Keep `SKILL.md` concise, because Claude loads it every time the skill triggers.

## Adding a book

1. Fork the repo and create a branch.
2. Add an entry to `BOOKS` (PDF) or `WEB` (HTML) in `scripts/books.py`: `"File-Base-Name": ("slug", "Author, Title (Year)")` (web books also take the website URL).
3. Add a row to the book table in `README.md` with the official link and the filename to save it as.
4. Build it locally and check that the chapters split sensibly:
   ```bash
   python3 scripts/build_library.py ~/dl-books .
   ls library/<slug>/
   python3 scripts/search.py 'a topic from the book' -b <slug>
   ```
5. Commit only the book's section of `library/INDEX.md`, plus the script and README changes. Don't commit the regenerated INDEX entries for books you don't have, if they changed.
6. If the book fills a gap, add pointers to it in the relevant `notes/` file and in `notes/00-reading-map.md`.
7. Update the book count and list in the `description` of `SKILL.md`.

## Pull requests

- One topic per PR.
- Describe what changed and how you tested it (which books you built, which queries you tried).
- For notes, cite the chapter and page you checked against.

## Development setup

```bash
git clone https://github.com/<you>/dl-research-library ~/.claude/skills/dl-research-library
pip install pymupdf
```

Then follow the Setup section of the README to build the library from your own copies of the books.
