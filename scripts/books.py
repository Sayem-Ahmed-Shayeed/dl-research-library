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
