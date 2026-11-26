# Deep learning core: networks, losses, training

## Networks
- MLP: h = a(Wx + b) stacked. Nonlinearities: ReLU (default), GELU/SiLU (transformers), tanh/sigmoid (gates).
- Universal approximation: one wide hidden layer suffices in principle; depth gives exponentially more linear regions per parameter (`prince-udl/04-shallow-neural-networks.md`, `05-deep-neural-networks.md`, `scardapane-alice/16-1d-universal-approximation.md`).
- Networks as distribution transformers: layers push the data distribution through a sequence of maps (`torralba-fcv/14-13-…`).
- Read: `goodfellow-dl/07-6-deep-feedforward-networks.md`; `zhang-d2l/08-multilayer-perceptrons.md`; `torralba-fcv/13-12-neural-networks.md`.

## Loss functions = negative log-likelihoods
- Recipe (Prince ch 5): pick a distribution over outputs, have the net predict its parameters, minimize NLL.
  - Gaussian → MSE; Laplace → L1; Bernoulli → binary CE; categorical → softmax CE; mixture → MDN; heteroscedastic regression → predict mean and variance.
- Label smoothing, focal loss (class imbalance / dense detection), contrastive/InfoNCE, triplet loss (metric learning), Dice/IoU losses (segmentation).
- Read: `prince-udl/06-loss-functions.md`; `scardapane-alice/04-datasets-and-losses.md`; `bishop-prml/07-5-neural-networks.md` §5.2, §5.6.

## Backpropagation and autodiff
- Forward pass stores activations; backward pass multiplies vector–Jacobian products in reverse topological order. Memory ∝ depth × activations → gradient checkpointing trades compute for memory.
- Read: `prince-udl/08-gradients-and-initialization.md`; `torralba-fcv/15-14-backpropagation.md`; `scardapane-alice/07-automatic-differentiation.md`; `goodfellow-dl/07-6-…` §6.5.

## Initialization
- Keep activation and gradient variance constant across layers: Xavier/Glorot Var(w) = 2/(n_in+n_out) (tanh); He/Kaiming Var(w) = 2/n_in (ReLU).
- Bad init → vanishing/exploding gradients. Residual nets: init last layer of each block to zero (or small) so blocks start as identity.
- Read: `prince-udl/08-gradients-and-initialization.md`.

## Optimization
- SGD with minibatches: gradient noise acts as regularizer. Momentum: v ← βv + g; θ ← θ − ηv. Nesterov variant.
- Adaptive: AdaGrad, RMSProp, Adam (m, v moving averages + bias correction). AdamW = decoupled weight decay (the default for transformers).
- Learning-rate schedule matters as much as optimizer: linear warmup then cosine/linear decay; step decay for CNNs; LR range test.
- Batch size: linear-scaling rule (η ∝ batch) with warmup; very large batches need LARS/LAMB.
- Gradient clipping (by global norm) for RNNs/transformers.
- Loss landscape: saddles, flat vs sharp minima (SAM), edge of stability.
- Read: `prince-udl/07-fitting-models.md`; `zhang-d2l/15-optimization-algorithms.md`; `goodfellow-dl/09-8-optimization-for-training-deep.md`; `hardt-recht-ppa/05-optimization.md`.

## Normalization and residual connections
- BatchNorm: normalize per-channel over batch; train/eval behavior differs; smooths landscape; problematic with small batches.
- LayerNorm (transformers), RMSNorm (LLMs), GroupNorm/InstanceNorm (small-batch vision, style).
- Pre-norm (x + F(LN(x))) is more stable than post-norm for deep transformers.
- Residual connections y = x + F(x): ease optimization, allow 100+ layers, make the network an ensemble of shallow paths; shattered-gradients explanation.
- Read: `prince-udl/12-residual-networks.md`; `scardapane-alice/10-scaling-up-the-models.md`; `zhang-d2l/11-modern-convolutional-neural-networks.md`.

## Regularization
- Explicit: weight decay (L2), L1, dropout (ensemble of subnetworks), stochastic depth, label smoothing.
- Implicit: SGD noise, early stopping (≈ L2), architecture inductive bias.
- Data: augmentation (flips, crops, color jitter, Mixup, CutMix, RandAugment), more data, synthetic data, adversarial training.
- Ensembles, test-time augmentation.
- Read: `prince-udl/10-regularization.md`; `goodfellow-dl/08-7-regularization-for-deep-learning.md`; `torralba-fcv/37-36-training-for-robustness-and-generality.md`.

## Practical methodology (debugging and tuning)
- Start with a simple baseline, overfit a tiny batch first, check loss at init (≈ log K for K classes), visualize data and predictions.
- Tune LR first, then batch size/weight decay/schedule; use random or Bayesian search (Hyperband, ASHA).
- Monitor: train vs val loss, gradient norms, activation stats, LR.
- Read: `goodfellow-dl/12-11-practical-methodology.md`; `zhang-d2l/22-hyperparameter-optimization.md`, `09-builders-guide.md`; `prince-udl/09-measuring-performance.md`.

## Efficiency and scale
- Mixed precision (bf16/fp16), data/model/pipeline/tensor parallelism, ZeRO/FSDP, activation checkpointing, compiled kernels (FlashAttention).
- Scaling laws: loss falls as a power law in parameters, data, and compute; compute-optimal training balances N and D (~20 tokens/parameter, Chinchilla) — see `xiao-zhu-llm/01-pre-training.md`.
- Read: `zhang-d2l/16-computational-performance.md`.

## Why deep learning works (open questions)
- Overparameterization, implicit bias of SGD toward flat/low-norm solutions, lottery tickets, neural tangent kernel regime vs feature learning, double descent.
- Read: `prince-udl/21-why-does-deep-learning-work.md`; `hardt-recht-ppa/07-deep-learning.md`.
