# suresim_2025 — Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators (Badithela et al., arXiv 2025)

sources: papers/md/suresim_2025.md [1d57125f] ; no code

## One-line contribution
Casts "few real trials + many simulated trials" as prediction-powered inference: paired real/sim outcomes estimate a rectifier that de-biases large-scale simulation, and Waudby-Smith–Ramdas betting intervals give finite-sample-valid confidence intervals on mean real performance; saves 20–25 % of hardware trials when paired correlation is ~0.6–0.7 and nothing when it is ~0 (Abstract, Sec. 5.1).

## Setting
- hand(s): Franka Panda with parallel gripper; single arm (Sec. 5, App. E). Sim gripper replaced by the 3D model of the real one.
- simulator / physics: ManiSkill3; robot base pose and both camera calibrations transferred by manual calibration; scripted table mesh with real texture; 3D-scanned background; default shader with shadows; "tune lighting parameters until policy performance in simulation on randomly selected initial conditions is as high as possible" (Sec. 5 "Experimental Setup"). Timestep/contact model not stated.
- observation: wrist RealSense D405 + Logitech C920 third-person, both 192×192; 8-D state = 7 joint positions + gripper binary (App. E).
- action space: 8-D absolute joint-position targets + gripper; joint-space control at 15 Hz; DP horizon 16 / 8 executed; π0 open-loop chunk of 30 (Sec. 5, App. E, Table 2).
- objects / data: ~120 real toy-kitchen objects (Fig. 2), 3D models from a single image via Meshy, scaled to real size; 2,100 extra sim objects from RoboCASA (Objaverse + Luma AI text-to-3D), filtered to categories with a real counterpart. DP: 200 demos of tomato→plate over 30×40 cm. π0: 7 objects × 40 demos, "put <object> into the box", 10×20 cm pick region (Sec. 5 "Policies").

## Method
- paradigm: evaluation statistics, not a policy. Policies under test: single-task Diffusion Policy (ResNet-18, 50k updates, batch 64, ~1 h on L40) and π0-base finetuned (VLM frozen, action expert trained, 15k steps, batch 64) (App. E.1).
- problem: bounded metric M: X×Π→[0,1]; find CI with P(μ* ∈ CI) ≥ 1−α for finite n with "no assumptions on the distribution of Y_i beyond measurability and the boundedness induced by the metric M" (Sec. 3, Eq. 1).
- SureSim (uniform PPI, Alg. 1/2): sample n+N environments i.i.d. from D_env; real2sim g; sim outcome f(X̃_i) for all n+N; real Y_i for a uniformly random subset of n. Per-sample Δ_i = f(X̃_i) + ((n+N)/n)·(Y_i − f(X̃_i))·ξ_i, ξ_i = 1 iff paired. One WSR call on {Δ_i} with bounds L = −(n+N)/n, U = 1+(n+N)/n. "The first term is referred as the rectifier, since it adjusts the bias in simulation predictions" (Sec. 4).
- SureSim (2-Stage, Alg. 3): WSR CI on D_sim at level δ (L=0, U=1); WSR CI on rectifier {Y_i − f(X̃_i)} at α−δ (L=−1, U=1); CI = (f_l − R_u, f_u − R_l). "using δ ≈ 0.9α is a reliable heuristic" (footnote 1, App. C).
- SureSim-UB: union bound of SureSim at 3α/4 and Classical at α/4.
- WSR (Alg. 4): normalise to [0,1]; grid of candidate means; μ̂_t = (0.5+Σ Z_j)/(t+1), σ̂_t² = (0.25+Σ(Z_j−μ̂_t)²)/(t+1), λ_t = sqrt(2 log(2/α)/(n σ̂_t²)); betting martingale with c = 0.99; drop m when M_t(m) ≥ 1/α; CI clipped to [0,1].
- Theorem 1: "SureSim and its variants return finite-sample valid confidence interval CI that satisfies Equation (1)", following [17,52] given i.i.d. environments.
- Classical baseline: WSR on the n real outcomes alone. Control Variate [50] shown only sim2sim because it "is not provably Type-I error controlling in finite samples" (Chebyshev with a possibly biased variance estimate) (Sec. 4).
- key trick(s) against sim-real gap: same random seed in real and sim; "in simulation, we sample 20 initial conditions from a 2cm-by-2cm box of the real (x, y) initial condition, execute the policy for each, and average the results" (Sec. 5 "Real-Simulation Evaluation Gap").

## Evaluation
- metrics (exact): real partial score "0 for no grasp, 0.25 for a failed grasp (object slips), 0.5 for a successful grasp, 0.75 for successful grasp but unsuccessful release over the place object, and 1 for complete task success". Sim partial score "0 for no grasp, 0.5 for successful grasp, and 1 for complete task success" (Sec. 5 "Evaluation Metrics"). DP experiment: real label per object = mean over 5 initial conditions; paired sim label = mean over 100 sim initial conditions (Sec. 5.1).
- headline numbers: DP, n = 60, N = 700, α = 0.1, 100 redraws of 60 of 120 objects: SureSim mean width 0.16 vs Classical 0.187 (−14.4 %); >25 % hardware trials saved (Fig. 4, 5). π0 moderate correlation (ICs {1,2,3,4}), ρ = 0.59, N = 2100: >20 % savings, SureSim converges by N = 500 (Fig. 5, 6); scaling to N = 50,000 with replacement only approaches the rectifier lower bound (Fig. 7). π0 low correlation (ICs {1,2,3}), ρ ≈ −0.05: "none of our methods beat Classical" (Fig. 8). Sim2sim (two lighting settings), ρ = 0.97, n = 100, N = 2000, 400 held-out envs for coverage: all methods beat Classical at α = 0.1; Control Variate loses its advantage as α shrinks and its empirical coverage "can degrade with additional simulation samples" (Fig. 9, 11).
- Table 1 (App. A), averaged over 100 draws: DP real2sim n=60, N=700, ρ=0.702, real mean 0.246, paired sim mean 0.188, extra sim mean 0.174, σ̂²_Y=0.104, σ̂²_{Y−f}=0.054. π0 moderate: 60, 2100, 0.588, 0.825, 0.820, 0.772, 0.138, 0.090. π0 low: 60, 2100, −0.051, 0.983, 0.932, 0.928, 0.014, 0.029. π0 sim2sim: 100, 2000, 0.974, 0.751, 0.731, 0.732, 0.116, 0.006.
- savings definition: compute each method's CI at n = 60, then search the n Classical needs to be tighter (Sec. 5.1).
- decision rule for when sim helps: "combining real and simulated data is effective only when the rectifier variance is smaller than the variance of real evaluations" (Sec. 5.1; compare the last two Table 1 columns).
- baselines beaten: Classical (real-only WSR); Control Variate at loose α only, and it lacks coverage.
- real robot? Franka Panda, n = 60 paired real trials per experiment; DP real labels each average 5 rollouts, so 300 rollouts per redraw for that experiment.

## Limitations stated by the authors
- "reliably predicting the real evaluation outcome for a specific initial condition is extremely challenging"; "repeated trials from the same initial condition can produce different outcomes" (Sec. 7).
- Needs a real2sim pipeline and paired trials; physics simulators are costly to set up. The i.i.d. assumption between paired objects and extra sim objects is only approximated: "we take these 120 objects are taken to approximate the real-world distribution" (Sec. 5, App. E.2).
- Random, not active, sampling of real environments (Sec. 7). Coverage validated on 400 held-out sims, not synthetic ground truth (footnote 3).

## Quotable claims (verbatim, with section)
- "most research studies report empirical success rates of policies evaluated on a small number (e.g., 20-40) of trials" (Sec. 1)
- "researchers typically compare policy performance using only 20-30 real-world trials. However, such small sample sizes are insufficient to draw statistically significant conclusions in policy comparisons" (Sec. 2)
- "as we scale the number of simulations, the confidence intervals from our methods do not shrink to arbitrarily small widths. This controlled behavior is desirable, as it prevents overconfidence" (Sec. 5.1)
- "the simulation-to-real gap precludes rigorous statistical inferences about real-world outcomes from simulation results alone" (Sec. 1)

## Notes for the survey
- Feeds the evaluation section as the "simulation with a guarantee" entry: sim-only numbers (ours included) carry no real-world claim; the usable content of a simulator for inference is its paired correlation with real outcomes, i.e. the rectifier variance.
- Parallel gripper, pick-and-place only; no dexterous hand. Its 5-level ordinal real score differs from LBM's milestone fraction and from beyond_binary's continuous progress; all three are bounded metrics.
- Same authors as beyond_binary_success_2026 (Snyder, Badithela, Majumdar); that paper cites this one as [7] and says it "does not address policy comparison".
