# Machine learning foundations

## The learning problem
- Supervised: learn f: x→y from pairs; minimize empirical risk (1/N)Σ ℓ(f(xᵢ), yᵢ) as proxy for expected risk.
- Unsupervised: model p(x) or structure (clusters, low-dim manifolds). Self-supervised: create targets from data itself (masking, contrast, next-token).
- Reinforcement learning: maximize expected return from interaction (`prince-udl/20-…`, `hardt-recht-ppa/11,12`, `murphy-pml2/36-35-…`).
- Inductive bias: assumptions that let a model generalize (linearity, smoothness, locality, translation equivariance, permutation invariance). The geometric-DL view: architectures = symmetries (`bronstein-gdl/05-3-geometric-priors.md`).
- Read: `prince-udl/02-introduction.md`, `03-supervised-learning.md`; `goodfellow-dl/06-5-machine-learning-basics.md`; `torralba-fcv/10-9-introduction-to-learning.md`.

## Generalization
- Train / validation / test split; test set used once. Cross-validation for small data.
- Underfitting (high bias) vs overfitting (high variance). Capacity, VC dimension, Rademacher complexity (classical bounds; loose for deep nets).
- **Double descent**: test error falls again past the interpolation threshold; overparameterized nets generalize thanks to implicit regularization of SGD, architecture priors, and data. Read `prince-udl/09-measuring-performance.md`, `21-why-does-deep-learning-work.md`.
- Curse of dimensionality: volume grows exponentially, so local methods fail without strong priors (`bishop-prml/03-1-introduction.md` §1.4, `bronstein-gdl/04-2-learning-in-high-dimensions.md`).
- Benchmarks and holdout reuse: adaptive overfitting is smaller than feared, but distribution shift (ImageNet→ImageNetV2) costs accuracy (`hardt-recht-ppa/06-generalization.md`, `08-datasets.md`).
- Read: `torralba-fcv/12-11-the-problem-of-generalization.md`.

## Decision theory and evaluation
- Bayes-optimal classifier: argmax_y p(y|x). Loss matrices / costs shift thresholds.
- Metrics: accuracy, precision/recall/F1, ROC-AUC, PR-AUC (use for imbalance), calibration (ECE, reliability diagrams), top-k, mAP (detection), mIoU (segmentation), BLEU/ROUGE/perplexity (NLP).
- Read: `murphy-pml1/06-5-decision-theory.md`; `bishop-prml/03-1-introduction.md` §1.5.

## Linear models (the base of every network's last layer)
- Linear regression: ŵ = (XᵀX + λI)⁻¹Xᵀy (ridge). Lasso (L1) gives sparsity.
- Logistic regression: p(y=1|x) = σ(wᵀx); softmax regression for K classes; trained by cross-entropy, convex.
- Generative vs discriminative: LDA/naive Bayes model p(x|y) — good with little data; logistic regression models p(y|x) directly.
- Basis functions / kernels: the kernel trick k(x,x') = φ(x)ᵀφ(x'); SVM maximizes margin; GPs put priors on functions.
- Read: `bishop-prml/05-3-…`, `06-4-…`, `08-6-kernel-methods.md`, `09-7-sparse-kernel-machines.md`; `murphy-pml1/10-…`, `11-…`, `12-…`, `18-17-kernel-methods.md`; `jurafsky-slp3/04-logistic-regression.md`; `deisenroth-mml/10-9-…`, `13-12-…`.

## Classic non-deep methods worth knowing
- k-NN, decision trees, random forests, gradient boosting (XGBoost-style) — still state-of-the-art on tabular data (`murphy-pml1/17-16-…`, `19-18-trees-forests-bagging-and-boosting.md`; `bishop-prml/16-14-combining-models.md`).
- Ensembles: bagging reduces variance, boosting reduces bias; deep ensembles give strong uncertainty estimates.
- Clustering: k-means, GMM via EM, spectral clustering (`bishop-prml/11-9-mixture-models-and-em.md`, `murphy-pml1/22-21-clustering.md`).
- Dimensionality reduction: PCA (maximize variance = minimize reconstruction error), probabilistic PCA, kernel PCA, t-SNE/UMAP for visualization (`bishop-prml/14-12-…`, `deisenroth-mml/11-10-…`, `murphy-pml1/21-20-dimensionality-reduction.md`).

## EM algorithm (template for latent-variable learning)
- Maximize log p(x|θ) = log Σ_z p(x,z|θ). E-step: q(z) = p(z|x,θ_old). M-step: θ = argmax E_q[log p(x,z|θ)].
- Monotonically increases likelihood; it is coordinate ascent on the ELBO — same bound used by VAEs.
- Read: `bishop-prml/11-9-mixture-models-and-em.md` (§9.3–9.4), `deisenroth-mml/12-11-…`.

## Learning with fewer labels
- Transfer learning/fine-tuning, data augmentation, semi-supervised (pseudo-labels, consistency), self-supervised pretraining, active learning, few-shot/meta-learning.
- Read: `murphy-pml1/20-19-learning-with-fewer-labeled-examples.md`; `torralba-fcv/38-37-transfer-learning-and-adaptation.md`.
