# Probabilistic modeling and inference

## Graphical models
- Directed (Bayesian networks): p(x) = ∏ p(xᵢ|pa(xᵢ)); d-separation reads conditional independence.
- Undirected (MRFs): p(x) = (1/Z) ∏ ψ_C(x_C); factor graphs unify both.
- Exact inference: variable elimination, sum-product / belief propagation (exact on trees), max-product/Viterbi for MAP, junction tree. Loopy BP approximate.
- Read: `bishop-prml/10-8-graphical-models.md`; `murphy-pml2/05-4-graphical-models.md`, `10-9-message-passing-algorithms.md`; `goodfellow-dl/17-16-structured-probabilistic-models.md`; `torralba-fcv/30-29-probabilistic-graphical-models.md`.

## Latent variable models
- Mixtures (GMM), factor analysis/PPCA, ICA, topic models, HMMs (forward–backward, Viterbi, Baum–Welch), linear dynamical systems (Kalman filter/smoother).
- Read: `bishop-prml/11-9-…`, `14-12-continuous-latent-variables.md`, `15-13-sequential-data.md`; `goodfellow-dl/14-13-linear-factor-models.md`; `murphy-pml2/09-8-gaussian-filtering-and-smoothing.md`, `29-28-latent-factor-models.md`, `30-29-state-space-models.md`.

## Approximate inference
- Laplace approximation: Gaussian at the mode with covariance = inverse Hessian.
- Variational inference: maximize ELBO over a family q; mean-field coordinate ascent (CAVI); stochastic VI; amortized VI (VAEs); reverse-KL is mode-seeking and underestimates variance. Expectation propagation uses forward KL locally.
- Monte Carlo: importance sampling, rejection sampling; MCMC: Metropolis–Hastings, Gibbs, Hamiltonian MC/NUTS, Langevin dynamics, slice sampling; diagnostics (R̂, ESS). Sequential Monte Carlo / particle filters.
- Read: `bishop-prml/12-10-approximate-inference.md`, `13-11-sampling-methods.md`; `murphy-pml2/08-7-…`, `11-10-variational-inference.md`, `12-11-…`, `13-12-…`, `14-13-…`; `goodfellow-dl/18-17-monte-carlo-methods.md`, `20-19-approximate-inference.md`.

## Bayesian deep learning and uncertainty
- Aleatoric (data noise) vs epistemic (model) uncertainty.
- Methods: MC dropout, deep ensembles (strong baseline), SWAG, Laplace on last layer, variational BNNs, function-space priors.
- Calibration: temperature scaling; evaluate with ECE/NLL/Brier; OOD detection; conformal prediction for distribution-free coverage guarantees.
- Read: `murphy-pml2/18-17-bayesian-neural-networks.md`, `20-19-beyond-the-iid-assumption.md`; `bishop-prml/07-5-neural-networks.md` §5.7.

## Gaussian processes
- f ~ GP(m, k); posterior mean k*ᵀ(K+σ²I)⁻¹y; variance k** − k*ᵀ(K+σ²I)⁻¹k*. Cost O(N³) → sparse/inducing-point GPs. Kernel choice = prior on functions; marginal likelihood for hyperparameters. Infinite-width nets → GPs (NNGP) and NTK.
- Read: `bishop-prml/08-6-kernel-methods.md` §6.4; `murphy-pml2/19-18-gaussian-processes.md`; `zhang-d2l/21-gaussian-processes.md`.

## Causality and decision making
- Correlation ≠ causation; DAGs, do-operator, backdoor adjustment, confounding, potential outcomes, randomized experiments, instrumental variables.
- Decision making under uncertainty, bandits, RL (MDPs, Bellman equations, Q-learning, policy gradients, actor–critic).
- Read: `hardt-recht-ppa/09-causality.md`, `10-causal-inference-in-practice.md`, `11-…`, `12-reinforcement-learning.md`; `murphy-pml2/35-34-…`, `36-35-reinforcement-learning.md`, `37-36-causality.md`; `prince-udl/20-reinforcement-learning.md`; `zhang-d2l/20-reinforcement-learning.md`.
