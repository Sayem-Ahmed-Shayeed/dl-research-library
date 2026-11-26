# dl-research-library

A [Claude Code](https://claude.com/claude-code) skill that grounds Claude in 14 standard textbooks on deep learning, computer vision, NLP/LLMs, probabilistic ML and the mathematics behind them.

Use it when you want to:

- **do theory-driven work**: derive a loss, check an assumption, or find the principled version of a trick before building on it;
- **learn** a concept properly (backprop, ELBO, diffusion, attention, epipolar geometry, RLHF ...) with explanations taken from the books rather than from memory;
- **justify your ideas**: back a design choice, a method section or a reviewer reply with the textbook result and a citation (*book, section, PDF page*) you can check.

Claude answers from the book text and cites where it came from. When the books don't cover something (very recent methods, specific papers), it says so instead of guessing.

## What's inside

| Path | Contents |
|---|---|
| `SKILL.md` | Instructions Claude follows when the skill is triggered |
| `notes/` | 10 short curated notes (math, ML foundations, DL core, architectures, CV, NLP/LLMs, generative models, probabilistic inference, research practice), each pointing to the best chapters |
| `library/INDEX.md` | Every chapter of every book with its section titles |
| `library/<book>/` | Full chapter text, **built locally** from the books (not included in this repo; see Setup) |
| `scripts/search.py` | BM25 search over chapters with matching lines |
| `scripts/page.py` | Renders a book's PDF page to an image, so Claude can read equations and figures as printed |
| `scripts/books.py` | The list of books (edit this to add one) |
| `scripts/build_library.py` | Splits the books into chapter files and rebuilds `INDEX.md` |
| `scripts/html2md.py` | Converts the two web-only books from HTML |

## Books

All are freely available from their authors or publishers. Download them from the official links below.

| Folder | Book | Official free source | Save as |
|---|---|---|---|
| `prince-udl` | Prince, *Understanding Deep Learning* (2023) | https://udlbook.github.io/udlbook/ | `Prince-Understanding-Deep-Learning-2023.pdf` |
| `zhang-d2l` | Zhang, Lipton, Li, Smola, *Dive into Deep Learning* | https://d2l.ai/ | `Zhang-et-al-Dive-into-Deep-Learning.pdf` |
| `goodfellow-dl` | Goodfellow, Bengio, Courville, *Deep Learning* (2016) | https://www.deeplearningbook.org/ (HTML) | `md/Goodfellow-Bengio-Courville-Deep-Learning-2016.md` |
| `torralba-fcv` | Torralba, Isola, Freeman, *Foundations of Computer Vision* (2024) | https://visionbook.mit.edu/ (HTML) | `md/Torralba-Isola-Freeman-Foundations-of-Computer-Vision-2024.md` |
| `bishop-prml` | Bishop, *Pattern Recognition and Machine Learning* (2006) | https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ | `Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf` |
| `murphy-pml1` | Murphy, *Probabilistic ML: An Introduction* (2022) | https://probml.github.io/pml-book/ | `Murphy-Probabilistic-ML-Introduction-2022.pdf` |
| `murphy-pml2` | Murphy, *Probabilistic ML: Advanced Topics* (2023) | https://probml.github.io/pml-book/ | `Murphy-Probabilistic-ML-Advanced-2023.pdf` |
| `jurafsky-slp3` | Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft | https://web.stanford.edu/~jurafsky/slp3/ | `Jurafsky-Martin-Speech-and-Language-Processing-3rd-draft.pdf` |
| `xiao-zhu-llm` | Xiao & Zhu, *Foundations of Large Language Models* (2025) | https://arxiv.org/abs/2501.09223 | `Xiao-Zhu-Foundations-of-Large-Language-Models-2025.pdf` |
| `deisenroth-mml` | Deisenroth, Faisal, Ong, *Mathematics for Machine Learning* (2020) | https://mml-book.github.io/ | `Deisenroth-Mathematics-for-Machine-Learning.pdf` |
| `scardapane-alice` | Scardapane, *Alice's Adventures in a Differentiable Wonderland* (2024) | https://arxiv.org/abs/2404.17625 | `Scardapane-Alices-Adventures-Differentiable-Wonderland-2024.pdf` |
| `fleuret-lbdl` | Fleuret, *The Little Book of Deep Learning* (2023) | https://fleuret.org/francois/lbdl.html | `Fleuret-Little-Book-of-Deep-Learning.pdf` |
| `hardt-recht-ppa` | Hardt & Recht, *Patterns, Predictions, and Actions* (2022) | https://mlstory.org/ | `Hardt-Recht-Patterns-Predictions-and-Actions.pdf` |
| `bronstein-gdl` | Bronstein, Bruna, Cohen, Veličković, *Geometric Deep Learning* (2021) | https://arxiv.org/abs/2104.13478 | `Bronstein-et-al-Geometric-Deep-Learning-2021.pdf` |

You don't need all of them: the build skips any book it can't find.

## Setup

```bash
# 1. Install the skill
git clone https://github.com/Sayem-Ahmed-Shayeed/dl-research-library ~/.claude/skills/dl-research-library
pip install pymupdf

# 2. Put the PDFs in a folder, named as in the table above
mkdir -p ~/dl-books/Books ~/dl-books/md
#    -> ~/dl-books/Books/Prince-Understanding-Deep-Learning-2023.pdf, ...

# 3. (Optional) web-only books: save each chapter's HTML page, then convert in reading order
python3 ~/.claude/skills/dl-research-library/scripts/html2md.py \
    ~/dl-books/md/Torralba-Isola-Freeman-Foundations-of-Computer-Vision-2024.md chapter1.html chapter2.html ...

# 4. Build the chapter library
python3 ~/.claude/skills/dl-research-library/scripts/build_library.py ~/dl-books ~/.claude/skills/dl-research-library

# 5. Tell the page viewer where your PDFs are (for reading equations as printed)
echo ~/dl-books > ~/.claude/skills/dl-research-library/books_dir.txt
```

Restart Claude Code. The skill triggers automatically on ML/DL/CV/NLP theory questions, or you can ask for it by name.

## Example prompts

- "Derive the ELBO for a VAE and cite where each step comes from."
- "I want to justify using label smoothing in my method section. What do the textbooks say about it?"
- "Explain the epipolar constraint, then give me a 2-week reading plan for multi-view geometry."
- "Is my proposed loss a proper scoring rule? Check against the books."

Search directly from the shell:

```bash
python3 ~/.claude/skills/dl-research-library/scripts/search.py '"classifier-free guidance" diffusion' -k 5
```

## Contributing

Contributions are welcome: new freely available books, better notes, better extraction or search. See [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue to suggest a book.

## Notes

- Text is extracted from PDFs/HTML, so equations come out flattened. The skill handles this by rendering the cited PDF page from your local copy (`scripts/page.py`) and reading the equation from the image. The PDFs are never uploaded, which keeps this repo small (the 14 books total about 425 MB).
- Copyright of each book remains with its authors and publishers. This repo contains only the skill, notes, scripts and a table-of-contents index, not the books themselves.

## License

MIT for the skill, notes and scripts (see [LICENSE](LICENSE)). The books are not covered.
