# Generative models

Best entry: `prince-udl/16…19`; deepest reference: `murphy-pml2/21…27`; vision angle: `torralba-fcv/33-32-generative-models.md`, `35-34-conditional-generative-models.md`.

## Taxonomy
| Family | Likelihood | Sampling | Key idea |
|---|---|---|---|
| Autoregressive | exact | slow (sequential) | p(x)=∏p(xᵢ|x<ᵢ); PixelCNN, GPT, image tokens |
| VAE | lower bound (ELBO) | fast | amortized variational inference with encoder q(z|x) |
| Normalizing flow | exact | fast | invertible f, change of variables |
| GAN | none (implicit) | fast | adversarial game |
| Energy-based | unnormalized | MCMC | p(x) ∝ exp(−E(x)) |
| Diffusion / score / flow matching | bound / ODE exact | iterative | learn to reverse a noising process |

## VAEs
- ELBO: log p(x) ≥ E_q(z|x)[log p(x|z)] − KL(q(z|x)‖p(z)). Gap = KL(q‖p(z|x)).
- Reparameterization z = μ + σ⊙ε, ε~N(0,I) gives low-variance gradients.
- Issues: blurry samples (Gaussian decoder), posterior collapse; β-VAE (disentanglement), VQ-VAE (discrete codes → used as tokenizers for images/audio; latent diffusion uses KL-regularized autoencoders).
- Read: `prince-udl/18-variational-autoencoders.md`; `murphy-pml2/22-21-variational-autoencoders.md`; `goodfellow-dl/21-20-deep-generative-models.md`.

## GANs
- min_G max_D E[log D(x)] + E[log(1 − D(G(z)))]; optimal D gives JS divergence. Non-saturating generator loss in practice.
- Failure modes: mode collapse, instability. Fixes: Wasserstein GAN + gradient penalty, spectral norm, progressive growing, StyleGAN (mapping network, AdaIN/style modulation). Conditional GANs, pix2pix, CycleGAN (cycle consistency).
- Evaluation: FID, IS, precision/recall for generative models.
- Read: `prince-udl/16-generative-adversarial-networks.md`; `murphy-pml2/27-26-…`; `zhang-d2l/23-generative-adversarial-networks.md`.

## Normalizing flows
- log p(x) = log p_z(f(x)) + log|det ∂f/∂x|. Need cheap Jacobian determinants: coupling layers (RealNVP, Glow), autoregressive flows (MAF/IAF), residual flows; continuous flows (Neural ODE) via trace.
- Read: `prince-udl/17-normalizing-flows.md`; `murphy-pml2/24-23-normalizing-flows.md`.

## Energy-based models
- Train with contrastive divergence / MCMC (Langevin), score matching, noise-contrastive estimation. Partition function Z is the central difficulty.
- Read: `murphy-pml2/25-24-energy-based-models.md`; `goodfellow-dl/19-18-confronting-the-partition.md`.

## Diffusion models
- Forward: q(xₜ|x₀) = N(√ᾱₜ x₀, (1−ᾱₜ)I). Reverse learned: p_θ(xₜ₋₁|xₜ).
- DDPM simple loss: E‖ε − ε_θ(√ᾱₜx₀ + √(1−ᾱₜ)ε, t)‖². Equivalent to denoising score matching: ε_θ ≈ −√(1−ᾱₜ)∇log p(xₜ).
- Score SDE view: forward SDE, reverse SDE, probability-flow ODE (deterministic, DDIM). Fast samplers (DDIM, DPM-Solver), distillation/consistency models.
- Flow matching / rectified flow: regress velocity field along straight paths between noise and data; now common for image/video generators.
- Guidance: classifier guidance; classifier-free guidance ε̃ = (1+w)ε(x,c) − wε(x).
- Latent diffusion: diffuse in an autoencoder's latent space; U-Net or DiT (transformer) denoiser; text conditioning via cross-attention.
- Read: `prince-udl/19-diffusion-models.md`; `murphy-pml2/26-25-diffusion-models.md`; `torralba-fcv/33-32-…`, `35-34-…`.

## Autoregressive image/sequence models
- PixelRNN/PixelCNN (masked convs), image GPT, VQ tokens + transformer, WaveNet for audio; LLMs are the dominant AR models.
- Read: `murphy-pml2/23-22-autoregressive-models.md`.

## Connecting generation and representation
- Good generative models learn useful features (MAE, diffusion features); good representations make generation easier (latent spaces). Read `torralba-fcv/34-33-generative-modeling-meets-representation-learning.md`.
