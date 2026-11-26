"""Book list shared by build_library.py and page.py."""

BOOKS = {  # PDF basename -> (slug, display name)
    "Bishop-Pattern-Recognition-and-Machine-Learning-2006": ("bishop-prml", "Bishop, Pattern Recognition and Machine Learning (2006)"),
    "Bronstein-et-al-Geometric-Deep-Learning-2021": ("bronstein-gdl", "Bronstein et al., Geometric Deep Learning (2021)"),
    "Deisenroth-Mathematics-for-Machine-Learning": ("deisenroth-mml", "Deisenroth, Faisal, Ong, Mathematics for Machine Learning (2020)"),
    "Fleuret-Little-Book-of-Deep-Learning": ("fleuret-lbdl", "Fleuret, The Little Book of Deep Learning (2023)"),
    "Hardt-Recht-Patterns-Predictions-and-Actions": ("hardt-recht-ppa", "Hardt & Recht, Patterns, Predictions, and Actions (2022)"),
    "Jurafsky-Martin-Speech-and-Language-Processing-3rd-draft": ("jurafsky-slp3", "Jurafsky & Martin, Speech and Language Processing, 3rd ed. draft (Aug 2026)"),
    "Murphy-Probabilistic-ML-Advanced-2023": ("murphy-pml2", "Murphy, Probabilistic Machine Learning: Advanced Topics (2023)"),
    "Murphy-Probabilistic-ML-Introduction-2022": ("murphy-pml1", "Murphy, Probabilistic Machine Learning: An Introduction (2022)"),
    "Prince-Understanding-Deep-Learning-2023": ("prince-udl", "Prince, Understanding Deep Learning (2023)"),
    "Scardapane-Alices-Adventures-Differentiable-Wonderland-2024": ("scardapane-alice", "Scardapane, Alice's Adventures in a Differentiable Wonderland (2024)"),
    "Xiao-Zhu-Foundations-of-Large-Language-Models-2025": ("xiao-zhu-llm", "Xiao & Zhu, Foundations of Large Language Models (2025)"),
    "Zhang-et-al-Dive-into-Deep-Learning": ("zhang-d2l", "Zhang, Lipton, Li, Smola, Dive into Deep Learning"),
}

WEB = {  # markdown basename (in <books_dir>/md/) -> (slug, display name, website)
    "Torralba-Isola-Freeman-Foundations-of-Computer-Vision-2024": ("torralba-fcv", "Torralba, Isola, Freeman, Foundations of Computer Vision (2024)", "https://visionbook.mit.edu/"),
    "Goodfellow-Bengio-Courville-Deep-Learning-2016": ("goodfellow-dl", "Goodfellow, Bengio, Courville, Deep Learning (2016)", "https://www.deeplearningbook.org/"),
}

# Official online copies, used when the local PDF is missing.
# slug -> (PDF URL that opens in a browser at "#page=N", or None; book website)
ONLINE = {
    "bishop-prml": ("https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf",
                    "https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/"),
    "bronstein-gdl": ("https://arxiv.org/pdf/2104.13478", "https://arxiv.org/abs/2104.13478"),
    "deisenroth-mml": ("https://mml-book.github.io/book/mml-book.pdf", "https://mml-book.github.io/"),
    "fleuret-lbdl": ("https://fleuret.org/public/lbdl.pdf", "https://fleuret.org/francois/lbdl.html"),
    "hardt-recht-ppa": ("https://mlstory.org/pdf/patterns.pdf", "https://mlstory.org/"),
    "jurafsky-slp3": ("https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf", "https://web.stanford.edu/~jurafsky/slp3/"),
    "murphy-pml1": (None, "https://probml.github.io/pml-book/book1.html"),   # PDF is a GitHub release download
    "murphy-pml2": (None, "https://probml.github.io/pml-book/book2.html"),
    "prince-udl": (None, "https://udlbook.github.io/udlbook/"),               # PDF is a GitHub release download
    "scardapane-alice": ("https://arxiv.org/pdf/2404.17625", "https://arxiv.org/abs/2404.17625"),
    "xiao-zhu-llm": ("https://arxiv.org/pdf/2501.09223", "https://arxiv.org/abs/2501.09223"),
    "zhang-d2l": ("https://d2l.ai/d2l-en.pdf", "https://d2l.ai/"),
}
