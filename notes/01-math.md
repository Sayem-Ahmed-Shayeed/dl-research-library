# Mathematical foundations

## Linear algebra
- Vectors/matrices as linear maps; rank, null space, column space; a system Ax=b is solvable iff b ∈ col(A).
- Inner products, norms (L1, L2, L∞, Frobenius), orthogonal projection onto span(B): P = B(BᵀB)⁻¹Bᵀ.
- Eigendecomposition A = QΛQ⁻¹; symmetric A = QΛQᵀ with orthonormal Q, real λ. Positive (semi)definite ⇔ all λ > 0 (≥ 0).
- SVD A = UΣVᵀ exists for every matrix. Best rank-k approximation = truncate SVD (Eckart–Young). Pseudo-inverse A⁺ = VΣ⁺Uᵀ gives least-squares solution.
- Condition number κ = σ_max/σ_min controls numerical sensitivity and gradient-descent speed.
- Trace tricks: tr(AB)=tr(BA), xᵀAx = tr(Axxᵀ); det = ∏λ; log det appears in Gaussians and normalizing flows.
- Read: `deisenroth-mml/03-2-linear-algebra.md`, `05-4-matrix-decompositions.md`; `goodfellow-dl/03-2-linear-algebra.md`; `murphy-pml1/08-7-linear-algebra.md`; `bishop-prml/19-appendix-c-properties-of-matrices.md`.

## Calculus and gradients
- Gradient ∇f points to steepest ascent; Jacobian J (m×n) of f: ℝⁿ→ℝᵐ; Hessian H = second derivatives (curvature).
- Chain rule in vector form: ∂L/∂x = Jᵀ ∂L/∂y — this is backpropagation (reverse-mode autodiff = vector–Jacobian products; cost ≈ a few forward passes).
- Useful identities: ∂(aᵀx)/∂x = a; ∂(xᵀAx)/∂x = (A+Aᵀ)x; ∂ log det X/∂X = X⁻ᵀ; softmax-cross-entropy gradient wrt logits = p − y.
- Taylor expansion f(x+δ) ≈ f(x) + ∇fᵀδ + ½δᵀHδ underlies Newton's method, Laplace approximation, and learning-rate analysis.
- Read: `deisenroth-mml/06-5-vector-calculus.md`; `scardapane-alice/07-automatic-differentiation.md`; `zhang-d2l/28-multivariable-calculus.md`; `prince-udl/08-gradients-and-initialization.md`.

## Probability
- Sum rule p(x)=Σ_y p(x,y); product rule p(x,y)=p(y|x)p(x); Bayes p(θ|D) = p(D|θ)p(θ)/p(D).
- Expectation, variance, covariance; law of total expectation/variance; change of variables p_y(y) = p_x(x)|det ∂x/∂y| (basis of flows).
- Key distributions: Bernoulli/categorical (classification), Gaussian (regression, latent spaces), Beta/Dirichlet (conjugate priors), Laplace (L1), Student-t (robust), exponential family p(x|η)=h(x)exp(ηᵀT(x)−A(η)).
- Multivariate Gaussian: marginals and conditionals are Gaussian; conditional mean μ_a + Σ_abΣ_bb⁻¹(x_b−μ_b). This drives GPs, Kalman filters, linear-Gaussian models.
- Read: `deisenroth-mml/07-6-probability-and-distributions.md`; `bishop-prml/04-2-probability-distributions.md`; `murphy-pml1/03-…`, `04-…`; `prince-udl/25-probability.md`.

## Statistics and estimation
- MLE: θ̂ = argmax Σ log p(xᵢ|θ). Minimizing NLL ⇔ minimizing KL(p_data‖p_θ). Squared loss = Gaussian NLL; cross-entropy = categorical NLL.
- MAP = MLE + log prior; L2 weight decay = Gaussian prior, L1 = Laplace prior.
- Bias–variance decomposition: E[(y−f̂)²] = bias² + variance + noise.
- Bayesian inference: predictive p(y|x,D) = ∫p(y|x,θ)p(θ|D)dθ; conjugacy gives closed forms.
- Bootstrap, confidence intervals, hypothesis tests — needed for honest experimental comparisons.
- Read: `murphy-pml1/05-4-statistics.md`; `bishop-prml/03-1-introduction.md` (§1.2–1.3); `zhang-d2l/31-maximum-likelihood.md`, `34-statistics.md`.

## Information theory
- Entropy H(p) = −Σ p log p; cross-entropy H(p,q) = −Σ p log q = H(p) + KL(p‖q).
- KL(p‖q) ≥ 0, asymmetric: forward KL (mode-covering, used in MLE), reverse KL (mode-seeking, used in VI).
- Mutual information I(X;Y) = KL(p(x,y)‖p(x)p(y)); InfoNCE contrastive loss is a lower bound on MI.
- Perplexity = exp(cross-entropy per token) — the LM metric.
- Read: `murphy-pml1/07-6-information-theory.md`; `murphy-pml2/06-5-information-theory.md`; `goodfellow-dl/04-3-probability-and-information.md`; `bishop-prml/03-1-introduction.md` (§1.6).

## Optimization
- Convexity ⇒ local = global minimum. Deep nets are non-convex but SGD finds good minima; saddle points are more common than bad local minima in high dimension.
- Gradient descent θ ← θ − η∇L; converges for η < 2/L (L = Lipschitz constant of gradient); rate depends on condition number.
- Constrained optimization: Lagrange multipliers, KKT conditions (→ SVM dual).
- Second-order: Newton, quasi-Newton (L-BFGS), natural gradient (Fisher information) — rare in DL at scale but conceptually important (Adam ≈ diagonal preconditioning).
- Read: `deisenroth-mml/08-7-continuous-optimization.md`; `murphy-pml1/09-8-optimization.md`; `goodfellow-dl/05-4-numerical-computation.md`; `bishop-prml/21-appendix-e-lagrange-multipliers.md`.

## Numerical stability (practical)
- Use log-sum-exp: log Σ exp(aᵢ) = m + log Σ exp(aᵢ − m), m = max aᵢ. Compute softmax+cross-entropy jointly from logits.
- Under/overflow in fp16: use bf16 or loss scaling; keep reductions (norms, softmax) in fp32.
- Read: `goodfellow-dl/05-4-numerical-computation.md`; `zhang-d2l/16-computational-performance.md`.
