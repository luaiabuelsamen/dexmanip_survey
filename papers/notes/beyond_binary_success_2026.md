# beyond_binary_success_2026 — Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison (Snyder et al., arXiv 2026)

sources: papers/md/beyond_binary_success_2026.md [9dcf242d] ; no code

## One-line contribution
N-SCORE: a safe-anytime-valid (test-martingale) sequential comparison on paired per-trial score differences for any metric bounded in [0,1], with an online betting fraction tuned by KDE-like density estimates; Type-I error ≤ α*; on LBM 1.0 data with partial-credit rubrics it cuts evaluation burden ~70 % (sim) / ~45 % (hardware) vs batch and up to 50 % vs the binary sequential test STEP (Abstract, Table II).

## Setting
- hand(s): none of its own. Data re-analysed: LBM 1.0 [9] bimanual Franka gripper rollouts (sim N = 200 per task, hardware N = 50 per task); RoboArena [6] on DROID, 4 policies, 641 trials each, continuous progress scores; Mujoco RL (CleanRL PPO/TD3/DDPG/SAC, 10^6 steps, 1000 eval episodes each); synthetic Bernoulli and random-polynomial densities (Sec. VI, App. C).
- "over 4500 hardware evaluation rollouts and 2000 high-fidelity simulation rollouts" re-used (Sec. I).
- simulator / observation / action: n/a.

## Method
- paradigm: statistical test. Definition 1: "A real-valued random variable M(ω) is termed a 'generalized progress metric' if it is bounded; that is, P[M ∈ [0,1]] = 1" (extends to [A,B] by normalisation, footnote 2).
- hypotheses: H0 (S−): mean of policy 1's score distribution ≤ policy 0's; H1 (S+): greater; over all Lebesgue-measurable distributions on [0,1] (Sec. IV-A). Neyman–Pearson: α ≤ α* as hard constraint, minimise E[N] + λβ over decision rules (Eq. 2, Sec. IV-C).
- Algorithm 1 (N-SCORE), structure verbatim: "Initialize: X_0 = 1; X̄ = 1; ξ_0 = 0; F_0 = {∅}; n = 1. while X̄ < 1/α* and n ≤ N_max do: Observe evaluation progress scores r_{0,n}, r_{1,n}; Compute increment a_{n−1} = 1 + ξ_{n−1}(r_{1,n} − r_{0,n}); Update martingale X_n ← a_{n−1}·X_{n−1}; Update test statistic X̄ ← max{X̄, X_n}; Update filtration F_n ← F_{n−1} ∪ (r_{0,n}, r_{1,n}); Update ξ_n ← proj_[0,1] g(F_n); n ← n+1. if X̄ < 1/α* then return Fail to Reject Null else return Reject Null."
- Lemma 1 (null stability): E[X_n] contracts for all h ∈ S− and any ξ_n ∈ [0,1]. Theorem 1: Type-I error of Algorithm 1 ≤ α*, via Ville's inequality. Remark 1: ξ_n can be optimised online for expected growth rate; family N-SCORE_k with k akin to kernel bandwidth (N-SCORE_2 and N-SCORE_∞ used) (Sec. V-B).
- baselines (Sec. VI-A, App. B-A): STEP [68] (binary, SOTA, near-optimal); θ-SAVI [73] (parametric SAVI, discrete partial credit); WSR [80] confidence sequence on Z_n = r_{1,n} − r_{0,n}, stop at the first t with 0 ∉ CI_t, betting constant c = 0.95 (Alg. 2).
- multi-policy: pairwise tests with Bonferroni; α = 0.05 over 6 pairs → 0.0083 each (Fig. 2, App. C-B).

## Evaluation
- metrics (exact): time-to-decision TTD = evaluations per policy before a decision at α = 0.05; empirical power; blank entries counted as N. Total trials = column sum × 2 policies (Table II caption).
- Table I, synthetic. Bernoulli (35 alternatives × 250 redraws, N = 1000; power over the 9 hardest with gap 0.1): STEP TTD 95.1 / power 0.953; θ-SAVI 117.6 / 0.962; N-SCORE_2 117.9 / 0.965; N-SCORE_∞ 122.3 / 0.958; WSR 224.8 / 0.592. Nonparametric (3000 redraws, gap ≥ 0.01): N-SCORE_∞ 206.8 / 0.889; WSR 247.3 / 0.840.
- Table II, LBM 1.0 finetuned-LBM vs single-task, per task TTD (progress N-SCORE_∞ / WSR | binary STEP / N-SCORE_2 / θ-SAVI / WSR): DumpVegetables 38/36 | 154/–/–/–; PutContainer 33/36 | 169/–/–/–; PutFruit 10/10 | 40/46/45/52; SeparateFruit 18/20 | 77/98/98/103; TurnUpsideDown all blank. Sim totals: 598 / 604 | 1280 / 1488 / 1486 / 1510 (nominal batch 2000). Hardware: BikeRotor blank; CutApple 29/29 | blank; CleanLitter 36/23 | blank; ClearCounter 16/15 | 23/25/30/46; SetUpBreakfast 12/13 | 15/19/19/17. Hardware totals 286 / 260 | 376 / 388 / 398 / 426 (nominal 500).
- text summary: binary sequential saves 25–35 % (sim) and 16–25 % (hardware) vs batch; partial credit "yield savings of approximately 70%, corresponding to a nearly 1400-sample reduction" in sim, ">50%" vs STEP; hardware ~45 % vs batch, 24–30 % vs STEP (Sec. VI-B4). LBM rubrics had "between six and eight partial credit outcomes; each subtask was weighted equally".
- RoboArena (Fig. 2, App. Fig. A.3): N-SCORE separates all four policies in 1419 total trials; WSR needs 1881 and cannot separate π0 from PGDiff; STEP on binary scores uses 1979 and fails to separate two policies. p-values reach 0.0083 in 18 trials for the ~30-point gap vs PG-Binning; a 20-point binary gap needs ~80 trials (App. C-B, Fig. A.4).
- Table III / A.I, Mujoco: PPO vs DDPG InvertedPendulum-v4 WSR 677 vs N-SCORE 267; totals PPO vs DDPG 1758 vs 894, SAC vs TD3 2862 vs 2758; whole RL suite ~5600 (N-SCORE) vs ~7100 (WSR) vs 28k batch.
- baselines beaten: WSR everywhere; matches θ-SAVI on parametric data; STEP remains best on pure Bernoulli.
- real robot? none run by the authors; hardware data are LBM 1.0 and RoboArena logs.

## Limitations stated by the authors
- "any procedure using tools from safe, anytime-valid inference (SAVI) tends to achieve tighter Type-1 error control than specified, leaving some 'risk budget' unused" — explains the gap to STEP (Sec. VII).
- "they rely crucially on i.i.d. evaluation data. Moreover, rigorous guarantees are only meaningful if the evaluation paradigm is similarly rigorous and reproducible" (Sec. VII).
- App. C-C on sampling schemes: RoboArena's "one environment, every policy once" scheme (L = N) can inflate the variance of score differences so tests are "overly optimistic, violating Type-1 Error control"; LBM's stratified scheme is exchangeable, not i.i.d., "practically negligible" when L ≪ N; post-hoc fix: per initial condition keep one random policy's score → effective sample N/K.

## Quotable claims (verbatim, with section)
- "a policy that completes 90% of the task is clearly better than a policy that is frozen the whole time, yet their success rates would be identically 0%" (Sec. I)
- "In robot manipulation, evaluation constraints often limit evaluation to 10-60 trials; the statistical validity of such comparisons is often not reported" (Sec. II-A)
- "the evaluation burden of using partial credit measures is essentially identical to success measures, so the added informativity (and reduction in necessary evaluation trials), can be realized for free" (App. C-B)
- "for the same performance gap, the signal-to-noise ratio is relatively higher in continuous progress settings because the empirical variance of continuous scores is no greater than the empirical variance of the corresponding Bernoulli scores" (App. C-B)

## Notes for the survey
- Feeds the evaluation-protocol section: for graded physical-plausibility scores (penetration depth, held fraction, contact ratio) bounded to [0,1], N-SCORE or WSR are the applicable sequential tests; STEP and Lai-1988 apply only to binary success. Direct successor to lbm_careful_examination_2025, whose Welch-t step on TC it replaces with a Type-I-controlled test on the same rollouts.
- Caveat for our own protocol: fixed seeds per environment and stratified evaluation are the "exchangeable, not i.i.d." case discussed in App. C-C; comparing two policies on identical seeds is their first (degenerate-distribution) setting, which they say remains valid.
- ycb_2015 already advised partial-credit scoring in 2015 (Sec. IV-B2 there); this paper supplies the test that makes that advice pay.
