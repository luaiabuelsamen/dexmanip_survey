# pang_global_planning_2022 — Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-dynamic Contact Models (Pang, Suh, Yang, Tedrake; IEEE T-RO 2023, arXiv 2022)

sources: papers/md/pang_global_planning_2022.md [01bc9841] ; code/md/pang_global_planning_2022.md [c9177559]

Parse caveat (RESOLVED by OCR): the explicit cost/objective equations of the iMPC problem (Sec. V-A) and the SOCP/log-barrier equations (Sec. III-B/IV-B, Eqs. 23-27, 31, 34) render blank in the flattened markdown, but have been recovered by OCR from papers/md/pang_global_planning_2022.ocr.md (OCR text is noisier than the layout parse, symbols may be imperfect). The structural description below (quadratic tracking + control cost, log-barrier-relaxed friction-cone constraints) is confirmed by them. The iMPC tracking objective, Eq. 43, quoted verbatim from the OCR (its line breaks kept):

```
MPC(¯xj) = u⋆
j, where
(43a)
min
xt,ut
xT −xd
T
2
QT
+
T −1
t=j
∥xt −xd
t ∥2
Qt + ∥ut∥2
Rt
(43b)
s.t. xt+1 = At(xt −¯xt) + Bt(ut −¯ut) + ct,
(43c)
Cx
t xt ≤dx
t , Cu
t ut ≤du
t , ∀t ∈{j · · · T −1},
(43d)
xj = ¯xj.
(43e)
```

(recovered by OCR from papers/md/pang_global_planning_2022.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect). The OCR mangles two things here: the Σ glyph before "T −1 / t=j" in (43b) is dropped entirely, and the terminal term's squared weighted norm is flattened to a bare "xT −xd_T / 2 / QT" — read the summation and the ‖·‖²_QT from the structure, not from these characters. The accompanying prose is clean: "Here, {Qt, Rt} are the quadratic weights for state and input, respectively; QT is the weight on the terminal state; {Cx_t, dx_t} and {Cu_t, du_t} are inequality parameters on the state and input, respectively." No numeric values for Qt/Rt/QT are printed in the OCR either, so the *weights* remain SOURCE THIN even though the cost's form is now recovered.

IMPORTANT SCOPE NOTE: this is a model-based/planning counterpoint paper, not an RL tracker of human hand-object references. There is no learned policy, no human demonstration data, and no hand retargeting anywhere in this work. Many TEMPLATE/HOWTO_METHOD fields below are answered "not applicable" for this reason, as instructed.

## One-line contribution
A convex, differentiable, quasi-dynamic contact model (CQDC) is locally smoothed (proven equivalent whether the smoothing is "randomized," i.e. RL-style sampling and averaging, or "analytic," i.e. a log-barrier relaxation of the friction-cone constraints), and this smoothed local model is used both inside an iLQR-style trajectory optimizer (iMPC) and to bias a sampling-based global planner (an RRT variant with a smoothed Mahalanobis distance metric, single-step dynamically-consistent extension, and contact sampling), letting a CPU-only planner solve dexterous, contact-rich tasks (3D in-hand rotation, extrinsic-dexterity plate pickup, constrained door opening) in about a minute of wall-clock time, without any learning (Abstract; Sec. I "Summary of Contributions").

## Setting
- hand(s): Allegro Hand (full 3D model) for in-hand rotation, pen placement, plate pickup, and door opening tasks; a 2-DoF-per-finger planar hand (2 fingers) for 2D reorientation tasks; 2 Kuka iiwa arms for the hardware "IiwaBimanual" bucket-rotation task (Sec. V-B1, Sec. VIII-A, Sec. IX-A4). Not applicable: no arm attached to the Allegro hand (fixed-base hand); bimanual only in the IiwaBimanual hardware variant.
- simulator / physics: the paper's own CQDC (Convex Quasi-Dynamic Differentiable Contact) model, implemented in the Drake robotics toolbox using MultibodyPlant/SceneGraph for collision detection and mass/Jacobian/signed-distance computation, with a custom SOCP solve (via MathematicalProgram + a third-party conic solver) and a custom in-house Newton's-method solver for the log-barrier-smoothed variant (Sec. III-D, IV-B). Real hardware validation compares against Drake's own high-fidelity second-order simulator with "a sophisticated and accurate contact solver" (Sec. IX-A3). Wall-clock: numerical experiments run on a single desktop, AMD Threadripper 2950 (16 cores/32 threads), 32GB RAM (Sec. V-B3); planning "on the order of a minute" online, all on CPU (Sec. VIII intro); trajectory-optimization case-study running times per Table II (20 iterations, 5 trials): e.g. Analytic smoothing 2.17s (PlanarPushing), 5.20s (PlanarHand), 19.59s (AllegroHand); RRT running times per Table III (1000 iterations): Analytic 3.25s (PlanarPushing) up to 117.16s (AllegroPlate).
- observation: full state x = q = (q^u, q^a) — unactuated object configuration and actuated robot configuration — assumed fully known (no perception/vision pipeline; state comes from the simulator or, on hardware, a motion-capture system tracking the bucket, Sec. IX-A4). Not applicable: no partial observability / vision-based observation.
- action space: u ∈ R^{n_a} = commanded robot joint positions, interpreted as equilibrium positions of a spring/impedance model with diagonal stiffness matrix K^a (robots modeled as impedances reduced to springs under the quasi-dynamic assumption) (Sec. III-B).
- objects / data: NOT APPLICABLE — no human demonstration dataset. Each task is hand-specified by an initial and goal object configuration q_0^u / q_goal^u: Planar Pushing (3,2,2), Planar Hand Reorientation (3,4,13), Allegro In-Hand Rotation (6,16,20) [Sec. V-B1]; Pen Placement (6,19,24), Plate Pickup (6,19,42, exploiting extrinsic dexterity against a wall), Door Opening (2,19,22, requires rotating a handle before pushing) [Sec. VIII-A] — tuples are (n_u unactuated DoF, n_a actuated DoF, n_cg collision geometries).

## Method
- paradigm: trajectory optimization (iLQR-inspired iMPC) for local case studies, plus sampling-based global motion planning (RRT variant) for the harder tasks — NOT RL, NOT IL. No neural network, no training data, no learned policy anywhere (confirmed throughout Secs. III-VIII; the paper's explicit framing is "traditional model-based approaches can be effective," Sec. X).
- algorithm — iMPC (Sec. V-A, Alg. 1): an iLQR-style algorithm from [16, Suh et al.] that computes time-varying locally-linear models {A_t, B_t, c_t} of the dynamics at each step of a nominal trajectory, then solves a QP for the optimal input sequence tracking a desired state trajectory {x_t^d}; when smoothing is used, {A_t,ρ, B_t,ρ, c_t,ρ} (smoothed linearizations) replace the exact first-order Taylor expansions, and the smoothing variance/κ is annealed (reduced/increased) every outer iteration so the surrogate converges to the true dynamics.
- algorithm — RRT-through-contact (Sec. VI-VII, Alg. 2-3): vanilla RRT enhanced with (i) a `Nearest` step using a smoothed local Mahalanobis distance metric on the unactuated object d^u_{ρ,γ} instead of Euclidean distance (because a globally-uniform metric is "a poor measure of reachability" under contact dynamics); (ii) a fast single-timestep `Extend` step that projects the subgoal displacement onto Range(B_ρ) via least-squares, then rolls out the ACTUAL (non-smoothed) CQDC dynamics f — "we use the actual dynamics f as opposed to the smooth surrogate dynamics f_ρ... This ensures that while the search for the next action relies on the smoothed model, the actual path is dynamically consistent under the original non-smooth contact dynamics"; (iii) a `ContactSample` operation that, with some probability, replaces `Extend` by fixing q^u_nearest and solving (via IK for planar systems, or EigenGrasps [65] random-direction hand-closing for Allegro-hand systems) for a q^a that makes contact, since contact-free nodes hinder tree growth. Final RRT paths are refined by segmenting at ContactSample boundaries, short-cutting, and re-running iMPC trajectory optimization on each contact-rich segment with a smaller step size h (Sec. VII-E).
- human dataset / retargeting: NOT APPLICABLE — no human demonstration data of any kind is used anywhere in this paper; tasks are specified purely as goal object configurations.
- reward/objective (block C) — paper: the iMPC cost is described only in prose as tracking a desired state trajectory {x_t^d} (Sec. V-A); the cost itself is Eq. 43b, now recovered by OCR and quoted in full in the Parse caveat above — "min / xt,ut / xT −xd_T / 2 / QT / + / T −1 / t=j / ∥xt −xd_t ∥2 / Qt + ∥ut∥2 / Rt / (43b)" (recovered by OCR from papers/md/pang_global_planning_2022.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect; the Σ glyph is dropped by the OCR); the exact numeric state/control cost weights {Qt, Rt, QT} are still not printed anywhere in the paper. For the RRT stage, "reward" is replaced by two planner-quality metrics rather than a scalar objective (see Evaluation block). The forward dynamics themselves are the solution to a convex Second-Order-Cone Program (27) whose objective (27a) is a quadratic "cost of work" (∝ δq^T Q δq for some configuration-dependent Q built from M^u(q), K^a, and regularization ε) subject to the quasi-dynamic equations of motion and Anitescu's convex-relaxed Coulomb friction constraints (25)-(26); analytic smoothing converts the hard friction/non-penetration constraints into log-barrier penalty terms in this same objective with a barrier weight κ that is annealed (increased) across iMPC iterations (Sec. IV-B, Eq. 34). Both equations are recovered by OCR from papers/md/pang_global_planning_2022.ocr.md (OCR text is noisier than the layout parse, symbols may be imperfect), quoted verbatim with the OCR's line breaks:

```
min.
δq
1
2δq⊺Qδq + b⊺δq, subject to
(27a)
Jiδq + φi
02
∈K⋆
i , ∀i ∈{1 . . . nc}, where (27b)
Q :=
ϵMu/h
0
0
hKa , b := −h
τ u
Ka(u −qa) + τ a ,
(27c)
```

```
min.
δq
1
2δq⊺Qδq + b⊺δq
−1
κ
nc
i=1
log
(Jniδq + φi)2
µ2
i
−(Jtiδq)⊺Jtiδq ,
(34)
```

So Q is block-diagonal, blk-diag(ϵM^u/h, hK^a), and b = −h·(τ^u, K^a(u − q^a) + τ^a) — confirming the prose reading above. The OCR mangles the block-matrix layout of (27c) (the two diagonal blocks and the two stacked entries of b are flattened onto separate lines with the brackets lost) and drops the Σ glyph before "nc / i=1" in (34), as well as the fraction bar in the log argument; the log-barrier term is −(1/κ)Σ_i log[((J_ni δq + φ_i)²/µ_i²) − (J_ti δq)ᵀ J_ti δq] read structurally. The projection-of-penetrating-configurations problem (31) is likewise recovered: "min. / δq / 1 / 2δq⊺Qδq + b⊺δq, subject to / (31a) / φi(q + δq) ≥0, i ∈{1 . . . nc}, / (31b)" — the same quadratic work-cost objective as (27a) under the non-linear non-penetration constraint.
- reward/objective (block C) — code: `qsim/system.py`-family functions `step_log_mp` / `step_log_cvx` take an explicit `log_barrier_weight` argument implementing κ from Eq. 34 (code/md lines 1242-1247); YAML configs (e.g. `models/q_sys/allegro_hand_and_sphere.yml`) set per-task physical/cost-relevant parameters: `Kp` (per-joint impedance/stiffness gains, e.g. [100]×16 for the sim Allegro hand vs. a much softer [2,3,3,2,...] for the hardware variant), `gravity`, `nd_per_contact: 4` (number of extreme rays approximating the friction cone), `contact_detection_tolerance` (see block D), `unactuated_mass_scale: 5.` (a regularization/scaling on the object's effective mass, related to ε in Eq. 23b). No task-specific per-term reward weights (analogous to λ_p/λ_r in the RL papers in this survey) are exposed in the parsed config files — the "reward" here is entirely the physical cost-of-work SOCP objective plus goal-distance metrics used only for reporting, not for optimization directly in the RRT stage.
- key trick(s): proving randomized smoothing (RL's implicit mechanism) and analytic log-barrier smoothing are equivalent ways of computing the same local linear model, then exploiting analytic smoothing's speed advantage (no need for N=100 parallel dynamics samples) inside a global planner; treating a "single time step" dynamically-consistent extension as sufficient for RRT growth under quasi-dynamic (long-sighted) dynamics, avoiding expensive per-node trajectory optimization.

## Evaluation
- metrics (Sec. V-B/VIII-A, quoted): trajectory-optimization case study — minimum cost achieved and wall-clock running time (Table II), averaged over 5 trials, 20 iterations. RRT case study — two planner-quality metrics, NOT a binary success/fail criterion: (1) "Iteration vs. Minimum distance to goal," defined as min_{q∈V} ‖q^u − q_goal^u‖ at every iteration (a successful planner drives this to zero asymptotically); (2) "Iteration vs. Packing Ratio," a Monte-Carlo estimate of the fraction of a workspace volume "reachable" (within some threshold η of the local Mahalanobis metric) by the current tree, averaged over 5 runs, 1000 iterations (Table III gives running times only, not success rates). No stated failure/early-termination rule during a rollout — the planning process runs for a fixed iteration budget (20 for iMPC, 1000 for RRT) and quality is read off the above continuous metrics, not a pass/fail criterion.
- headline numbers: Table II (min cost / time, 5 trials × 20 iters): Analytic smoothing beats exact/no-smoothing on PlanarPushing (11.74 vs. 31.64) and AllegroHand (5.78 vs. 44.68) but not PlanarHand (26.55 vs. 18.49, exact slightly better) — attributed to fewer contact-mode changes in PlanarHand (Sec. V-C1). Table III (RRT wall-clock, 1000 iters): Analytic fastest across all 6 systems (e.g. 3.25s PlanarPushing, 117.16s AllegroPlate) vs. randomized-first/-zero roughly 2-3× slower, consistent with the N=100-samples/32-threads compute-cost argument (Sec. V-C3, VIII-B2). Sim-to-real error (Fig. 12, Sec. IX-B): 2D systems (PlanarPushing, PlanarHand, IiwaBimanual) show low mean position/orientation error and good open-loop transfer; 3D systems (AllegroHand, AllegroPlate, AllegroPen, AllegroDoor) show much larger error, attributed to the quasi-dynamic assumption breaking down (insufficient damping from point contact at the palm) and to "missed contacts" (grasps valid under CQDC failing under Drake's second-order solver, causing dropped plates/missed door handles).
- baselines beaten: "Exact" (no smoothing, exact linearization), "NoContact" (RRT without contact sampling), "Global" (RRT with a globally-uniform weighted Euclidean metric instead of the local Mahalanobis metric) — all three ablations perform worse than the full method on the distance-to-goal and packing-ratio metrics (Sec. VIII-B). The paper positions itself against RL more broadly in prose ("Compared to existing tools in RL which use heavy offline computation in the order of hours or days, our contribution offers... online planning in the order of a minute," Sec. X) but does not re-run or numerically compare against a specific RL baseline in this paper.
- real robot? yes, IiwaBimanual: 2 Kuka iiwa arms rotating a bucket by 180°, evaluated via motion-capture-tracked open-loop plan execution, at least 10 trajectory segments evaluated per system across all 7 systems shown in Fig. 12 (Sec. IX-A2/A4) — this is open-loop trajectory tracking of a planned path, not a repeated-trial task-success rate; no discrete trial count or success percentage is reported, only the continuous position/orientation error metrics.

## Limitations stated by the authors (Sec. IX-B, "Results & Discussion")
- The quasi-dynamic assumption is violated on 3D systems with light point contact (e.g. object resting on an Allegro-hand palm) where damping is insufficient, letting the object "roll quite far from the planned trajectory or even off the palm."
- "Missed Contacts": small trajectory discrepancies from the phase gap between first-order (CQDC) and second-order (Drake) dynamics cause grasps valid under CQDC to fail under the higher-fidelity solver — plates dropped, door handles missed.
- Open-loop execution of CQDC-derived plans is insufficient under real second-order dynamics; the authors state closed-loop, quasi-dynamic-enforcing low-level feedback control is needed (future work), as is incorporating classical grasp-quality robustness objectives into the high-level planner.
- Collision geometry is restricted to sphere-sphere/sphere-box/sphere-cylinder pairs "to avoid discontinuities coming from collision detection" (Sec. III-D) — e.g. box-shaped Allegro fingers are approximated as arrays of inscribing spheres, a geometric approximation the authors flag as alleviable by future smoothing-over-geometry work.
- Contact sampling introduces "non-physical behavior where the robot teleports from one configuration to another," valid only when the object can remain in static equilibrium without the teleporting DoFs (Sec. VII-C).

## Quotable claims (verbatim, with section)
- "we can define the dynamics from an infeasible q as the projection of q to the 'nearest' point in the feasible (non-penetrating) set" (Sec. IV-A)
- "samples within the penetrating regime are projected onto the boundary of the feasible set and then averaged, the expected value of such a distribution creates a stochastic force field that pushes the object away from feasible set's boundary" (Sec. IV-A)
- "we use the actual dynamics f as opposed to the smooth surrogate dynamics f_ρ... This ensures that while the search for the next action relies on the smoothed model, the actual path is dynamically consistent under the original non-smooth contact dynamics" (Sec. VII-B)
- "we curate our system models so that every contact pair is either sphere-sphere, sphere-box, or sphere-cylinder, which means the contact points and normals change smoothly" (Sec. III-D)
- "there exists a persistent phase difference between q_real^u and q_sim^u... This is not surprising, as the CQDC dynamics that generates q_sim^u is inherently a first-order system, whereas q_real^u is generated from second-order dynamics" (Sec. IX-B)

## Notes for the survey
- Feeds: the block-D contact/penetration section as the sharpest contrast to the RL trackers in this batch. Non-penetration here is a HARD CONSTRAINT of the un-smoothed CQDC forward dynamics (φ_i(q) ≥ 0 enforced via the SOCP (27)); penetration only ever appears transiently during smoothing sample generation (finite-support ρ can sample a penetrating q̄+w_i), and is handled by definition, not penalty: a penetrating configuration is defined as the projection to the nearest feasible (non-penetrating) configuration under the same quadratic work-cost metric that defines the dynamics itself (Sec. IV-A, Eq. 31) — averaging these projections is what produces the "stochastic force field" that gives useful gradients near contact. This is a genuinely different mechanism from any of the RL papers' contact-graph/force-threshold rewards: it is a smoothing-time device for gradient computation, not a training signal, and the paper never reports a quantitative penetration measurement on any final executed trajectory (sim or hardware) — interpenetration is analytically eliminated in the final rolled-out dynamics (`f`, not `f_ρ`, Sec. VII-B) rather than measured post hoc.
- Contact-detection tolerance (code, YAML configs): `contact_detection_tolerance` is set per task, e.g. 0.025 m for most Allegro/planar systems, 0.0125 m for `allegro_hand_tilted_and_sphere`, and anomalously 10.0 for the `planar_hand_ball*` family (units/scale not explained in the parsed code — flag as unusual and worth checking against the repo directly before citing). `nd_per_contact: 4` (friction-cone polyhedral approximation rays) and `unactuated_mass_scale: 5.` are set uniformly across the Allegro configs read.
- Object tracking: position AND orientation — every task's goal is a full object configuration q_goal^u including rotation (explicit for AllegroHand "rotated configuration of the ball," Sec. V-B1; Door Opening tracks a hinge angle; the sim-to-real error metric Δ separately reports mean position error in metres and mean angular error in radians via axis-angle rotations for 3D, Sec. IX-A2).
- Use this note as the paper-vs-RL contrast point in the survey's method-comparison table: no reward shaping, no domain randomization, no training at all — a hard-constraint-then-relax-then-re-enforce treatment of contact and penetration, achieving comparable dexterous in-hand-rotation results to RL "with dramatically less computation" (Abstract) but with acknowledged sim-to-real fragility specifically on the 3D/point-contact tasks that most resemble the RL papers' target domain.
- SOURCE THIN FOR REWARD BLOCK (NARROWED): the precise form of Q in the SOCP objective (27a) is no longer missing — Eq. 27c gives Q := blk-diag(ϵM^u/h, hK^a) and b := −h(τ^u, K^a(u − q^a) + τ^a), recovered by OCR from papers/md/pang_global_planning_2022.ocr.md (OCR text is noisier than the layout parse, symbols may be imperfect) and quoted verbatim in the reward/objective block above, as are Eqs. 31, 34 and 43. What remains thin is only the *numeric* quadratic-cost weight matrices {Qt, Rt, QT} for iMPC's tracking objective (Sec. V-A): the paper prints them only symbolically, and they were not found as explicit numeric config fields in the parsed code beyond `Kp` (joint stiffness) and `unactuated_mass_scale`; anyone needing the literal per-state/control cost weights should consult the original PDF equations or the un-parsed source repository files not captured in code/md.
