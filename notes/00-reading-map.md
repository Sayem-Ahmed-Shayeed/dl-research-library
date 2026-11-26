# Reading map: which book for what

All paths are relative to `library/`. Shorthand like `prince-udl/03…10` or `torralba-fcv/25,27` means the chapter files whose names start with those numbers (file numbers, not book chapter numbers). Book folders:

| Folder | Book | Best for |
|---|---|---|
| `prince-udl/` | Prince, *Understanding Deep Learning* (2023) | Clearest modern DL explanations: losses, init, residuals, transformers, GNNs, all generative families, why DL generalizes |
| `zhang-d2l/` | Zhang et al., *Dive into Deep Learning* | Runnable PyTorch for every architecture; CNN history (AlexNet→ResNet→RegNet), attention, BERT, detection/segmentation basics, optimizers, HPO |
| `goodfellow-dl/` | Goodfellow, Bengio, Courville, *Deep Learning* (2016) | Classic theory: regularization, optimization, CNN/RNN theory, practical methodology, autoencoders, partition functions, approximate inference |
| `torralba-fcv/` | Torralba, Isola, Freeman, *Foundations of Computer Vision* (2024) | Vision itself: imaging, filtering, Fourier, pyramids, geometry, stereo, SfM, NeRF, flow, recognition, VLMs, robustness, **how to do research / write papers / give talks** |
| `bishop-prml/` | Bishop, *PRML* (2006) | Probabilistic ML: Bayesian regression/classification, kernels, graphical models, EM, variational inference, sampling, PCA, HMM/LDS |
| `murphy-pml1/` | Murphy, *PML: An Introduction* (2022) | Modern reference for probability, statistics, decision/information theory, linear models, trees/boosting, semi-/self-supervised learning |
| `murphy-pml2/` | Murphy, *PML: Advanced Topics* (2023) | Research-level reference: VI, MCMC, BNNs, GPs, distribution shift, VAEs, flows, EBMs, diffusion, GANs, representation learning, interpretability, RL, causality |
| `jurafsky-slp3/` | Jurafsky & Martin, *SLP* 3rd ed. (Aug 2026 draft) | NLP/LLMs: tokens, n-grams, embeddings, transformers, post-training (RLHF/DPO), MLMs, RAG, agents, MT, speech, parsing, IE |
| `xiao-zhu-llm/` | Xiao & Zhu, *Foundations of LLMs* (2025) | LLM pre-training, scaling, prompting/CoT, alignment (SFT, RLHF, DPO), inference/KV cache/decoding, reasoning |
| `deisenroth-mml/` | Deisenroth et al., *Mathematics for ML* | Linear algebra, geometry, matrix decompositions, vector calculus, probability, optimization; PCA, GMM, SVM worked from first principles |
| `scardapane-alice/` | Scardapane, *Alice's Adventures in a Differentiable Wonderland* (2024) | Compact modern tour: autodiff, convs, scaling tricks (norm, residual, dropout), transformers in practice, GNNs, SSM/recurrent models |
| `fleuret-lbdl/` | Fleuret, *Little Book of Deep Learning* | 150-page dense overview; good quick refresher |
| `hardt-recht-ppa/` | Hardt & Recht, *Patterns, Predictions, and Actions* | Generalization theory, datasets & benchmarks culture, causality, RL — critical/research perspective |
| `bronstein-gdl/` | Bronstein et al., *Geometric Deep Learning* | Symmetry/invariance view unifying CNNs, GNNs, transformers, equivariant nets |

## Learning paths

**Deep learning foundations (in order):** `deisenroth-mml` ch 2,5,6,7 (as needed) → `prince-udl/03…10` → `zhang-d2l/06…09` (code) → `goodfellow-dl/08-7`, `09-8` (regularization & optimization depth) → `prince-udl/21-why-does-deep-learning-work.md`.

**Computer vision:** `torralba-fcv/02…09` (images & imaging) → `16…24` (filtering, Fourier, pyramids) → `prince-udl/11,12` + `zhang-d2l/10,11,17` (CNNs, detection, segmentation) → `torralba-fcv/25,27` (CNNs, transformers) → `39…46` (geometry, stereo, SfM, NeRF) → `47…50` (motion) → `51,52` (recognition, vision–language) → `36…38` (bias, robustness, transfer).

**NLP / LLMs:** `jurafsky-slp3/02…07` → `09,08` (MLMs, post-training) → `11,12` (RAG, agents) → `xiao-zhu-llm/01…06`.

**Generative models:** `prince-udl/16…19` → `murphy-pml2/21…27` → `torralba-fcv/33…35` (vision-centric) → `bishop-prml/12-10` + `murphy-pml2/11-10` (variational inference math).

**Probabilistic / Bayesian ML:** `bishop-prml/03…16` alongside `murphy-pml1/03…07`, then `murphy-pml2/05…20`.

**Research craft:** `torralba-fcv/53-52-how-to-do-research.md`, `54-53-how-to-write-papers.md`, `55-54-how-to-give-talks.md`; `goodfellow-dl/12-11-practical-methodology.md`; `hardt-recht-ppa/08-datasets.md`; `prince-udl/09-measuring-performance.md`.

## Gaps in this library
- No dedicated book on modern object detection/segmentation families (YOLO, DETR, Mask R-CNN, SAM) — D2L ch "Computer Vision" and Torralba ch 50 give basics; go to papers.
- LLM topics after mid-2025 (newest reasoning/RL methods, MoE details) — `jurafsky-slp3` (Aug 2026 draft) and `xiao-zhu-llm` are the most recent; otherwise papers.
- Szeliski, *Computer Vision: Algorithms and Applications* 2nd ed. is not in the library (requires form download at szeliski.org/Book). Bishop & Bishop *Deep Learning: Foundations and Concepts* (2024) is read-online only at bishopbook.com.
