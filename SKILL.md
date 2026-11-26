---
name: dl-research-library
description: Local reference library of 14 full textbooks on deep learning, computer vision, NLP/LLMs, probabilistic ML and the math behind them (Prince UDL, Dive into Deep Learning, Goodfellow DL, Torralba-Isola-Freeman Foundations of CV, Bishop PRML, Murphy PML 1&2, Jurafsky-Martin SLP3, Xiao-Zhu LLMs, Deisenroth MML, Scardapane, Fleuret, Hardt-Recht, Bronstein GDL), split into chapter files with a search tool and curated foundation notes. Use when the user asks to explain, derive, compare or look up a concept in ML/DL/CV/NLP (e.g. backprop, ELBO, diffusion, attention, ViT, stereo, optical flow, RLHF), wants study plans or reading recommendations, needs textbook-grounded background or citations for a research paper, or is designing experiments and wants the methodological basics.
---

# Deep learning / CV / NLP research library

Everything lives next to this file:

- `notes/` — curated foundations, short and dense, each concept with pointers to the best chapters. Start here.
  - `00-reading-map.md` which book is best for what, learning paths, known gaps
  - `01-math.md` linear algebra, calculus, probability, statistics, information theory, optimization
  - `02-ml-foundations.md` generalization, evaluation, linear models, kernels, trees, EM, PCA, few-label learning
  - `03-deep-learning-core.md` MLPs, losses as NLLs, backprop, init, optimizers, normalization, residuals, regularization, practical tuning, scale
  - `04-architectures.md` CNNs, RNNs/SSMs, attention & transformers, ViT, GNNs, autoencoders, symmetry view
  - `05-computer-vision.md` image formation, filtering/Fourier/pyramids, geometry, stereo, SfM, NeRF, motion, detection/segmentation, SSL, VLMs, robustness
  - `06-nlp-llms.md` tokenization, LMs, embeddings, pretraining, RLHF/DPO, prompting/reasoning, inference, RAG, agents, classic NLP tasks
  - `07-generative-models.md` VAE, GAN, flows, EBMs, diffusion/flow matching, autoregressive
  - `08-probabilistic-inference.md` graphical models, latent variables, VI, MCMC, Bayesian DL & uncertainty, GPs, causality, RL
  - `09-research-practice.md` doing research, writing papers, talks, experimental methodology, ethics
- `library/INDEX.md` — every chapter file of every book with its section titles (~80 KB; grep it, don't read it whole).
- `library/<book>/NN-<chapter>.md` — full chapter text extracted from the books (PDF page markers `<!-- page N -->` inside). Each file begins with a `## Sections` list giving section titles and PDF page numbers.
- `scripts/search.py` — BM25 ranking of chapters for a query, with matching lines and line numbers.

## How to answer with this library

1. Read the one relevant `notes/` file (they are small) to orient and get candidate chapters.
2. Find the exact passage:
   ```bash
   python3 ~/.claude/skills/dl-research-library/scripts/search.py '"classifier-free guidance" diffusion' -k 6
   python3 ~/.claude/skills/dl-research-library/scripts/search.py 'epipolar fundamental matrix' -b torralba-fcv,bishop-prml
   grep -n -i 'rotary' ~/.claude/skills/dl-research-library/library/INDEX.md
   ```
   Quote phrases in the query for a phrase bonus; `-b` restricts to book folders; `-n` lines per hit.
3. Open only the needed part of a chapter: use the line numbers from search output with `Read` offset/limit (chapters are 2k–20k lines; never read a whole chapter unless asked). The `## Sections` block at the top of the file maps sections to PDF pages.
4. Answer from the book text, and cite it as *Book, chapter/section (PDF p. N)* so the user can check it. Prefer the clearest source for explanations (Prince, Torralba, D2L) and the most rigorous for derivations (Bishop, Murphy, Goodfellow).
5. If the library does not cover something (post-2025 methods, specific recent papers, YOLO/DETR/SAM details), say so and fall back to web search or papers rather than guessing.

## Notes on text quality
- Text was extracted with PyMuPDF/pdftotext and from HTML; equations are flattened (subscripts on separate lines, symbols sometimes lost). When an equation matters, reconstruct it carefully and cross-check a second book, or point the user to the PDF page.
- Prince files are numbered from the PDF outline, so `prince-udl/18-variational-autoencoders.md` is the book's chapter 17. Use the title, not the number.
- The chapter files are built locally from the source books (see README.md). If `library/<book>/` folders are missing, tell the user to run the setup in README.md, and meanwhile answer from `notes/` and `library/INDEX.md`. The web books (Torralba, Goodfellow) come from visionbook.mit.edu and deeplearningbook.org.

## Rebuilding
`scripts/build_library.py <project_dir> <skill_dir>` re-splits the PDFs and regenerates `library/` and `INDEX.md`; `scripts/html2md.py` converts downloaded web chapters. The web books must first be re-downloaded and converted into `<project_dir>/md/`.
