# Research practice

## Doing research (Torralba, Isola, Freeman ch 52)
- Pick problems that are important and where you have an edge; small concrete starts; build simple systems end to end; iterate quickly; look at data and failures yourself; keep a research log.
- Read: `torralba-fcv/53-52-how-to-do-research.md`.

## Writing papers (ch 53)
- One clear main idea; the paper sells the idea, not the effort. Figure 1 tells the story. Introduction = problem, why it matters, what is missing, your idea, results. Be precise and honest about limitations.
- Read: `torralba-fcv/54-53-how-to-write-papers.md`. (User's own paper conventions live in their global CLAUDE.md: Introduction, Related Work, Methods, Experimental Setup, Results, Discussion, Conclusion.)

## Giving talks (ch 54)
- Read: `torralba-fcv/55-54-how-to-give-talks.md`.

## Experimental methodology checklist
- Strong, tuned baselines with the same budget as your method; report the tuning budget.
- Multiple seeds; mean ± std or confidence intervals; significance tests when gaps are small (`murphy-pml1/05-4-statistics.md`).
- Ablations: remove one component at a time; sensitivity to hyperparameters.
- Clean splits: no test-set tuning, check for train–test leakage and near-duplicates; report data provenance (`hardt-recht-ppa/08-datasets.md`).
- Evaluate under shift and on OOD/robustness benchmarks where relevant (`torralba-fcv/36-35-…`, `37-36-…`).
- Measure what matters (metric choice; calibration; compute/latency/params).
- Read: `goodfellow-dl/12-11-practical-methodology.md`; `prince-udl/09-measuring-performance.md`; `hardt-recht-ppa/06-generalization.md`.

## Ethics and impact
- Bias, fairness criteria (demographic parity, equalized odds, calibration — cannot all hold together), privacy, misuse, environmental cost, dataset consent and licensing.
- Read: `prince-udl/22-deep-learning-and-ethics.md`; `torralba-fcv/05-4-computer-vision-and-society.md`.
