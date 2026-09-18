# dexteleop0_2026 — DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy (Liu, Jiang, Park, Xue, Wang; NTU Singapore / OOJU, arXiv 2026)

sources: papers/md/dexteleop0_2026.md [sha de4598a6] ; no code

## One-line contribution
DexTeleop-0 augments VR-headset-based bimanual dexterous teleoperation with a real-time, tactile-driven shared-autonomy correction: a per-cycle quadratic-program (QP) computes a residual joint command Δq that keeps fingertip contact forces inside a safe window and balances net object force/torque, cutting destructive contact forces roughly in half versus uncorrected kinematic teleoperation while raising multi-stage task success rates on both simulated and real 56-DoF bimanual rigs.

## Setting
- hand(s): two Sharpa Wave dexterous hands (22-DoF each), one per arm
  - arm: two Universal Robots UR7e arms (6-DoF each)
  - bimanual, 56 DoF total (2×(6+22)=56). Human tracked via a Meta Quest 3 VR headset (egocentric, no external mocap), 26 tracked hand-joint transforms per hand (M=26) retargeted to N=22 robot hand DoFs.
- simulator / physics: NVIDIA IsaacSim 4.5, built as a "digital twin" matching the real hardware
  - simulation evaluation done via strict replay of the same recorded teleoperation trajectory under different residual-control methods, with object mass and friction coefficient randomized per trial but held identical across methods within a trial index (for fair comparison).
- observation: per-finger contact force in the world frame f_i^w ∈ R^3 and contact point position p_i^w ∈ R^3 (tactile sensing on the Sharpa Wave fingertips)
  - an object-centric reference frame is estimated on the fly as the mean of all active contact positions p_obj = mean(p_i^w) (no external object pose/model required)
  - contact reliability is weighted by a smooth activation function w_i ∈ [0,1] computed via a logistic function of contact-force magnitude with a hysteresis deadband (midpoint (f_release+f_contact)/2) to handle noisy contact-phase transitions.
- action space: q_final = q_tele + Δq — q_tele is the raw teleoperated joint command (from VR retargeting: q_h = F_hand(H) for the hand via vector-based DexPilot-style retargeting, q_a = F_arm(T_w) for the arm via analytical IK on the wrist pose)
  - Δq is a compliant residual computed by a box-constrained QP solved at 30 Hz, subject to joint limits (q_min, q_max) and a slew-rate/velocity saturation limit derived from v_max.
- objects / data: no dataset is collected/released here — this is a teleoperation-control paper, evaluated task-by-task rather than via a demonstration corpus. Task set (Table 1): simulation — Ball Assembly (single-arm), Stir in Cup (dual-arm), Gear Assembly (single-arm)
  - real-world — Insert Peg into Tube (single-arm), Fruit and Vegetable Sorting (dual-arm), Chemistry Experiment / Tube Operation (dual-arm), plus a real Gear Mesh task. Evaluation protocol: real-world trajectories collected from 5 inexperienced + 2 professional operators, 5 trials per task per method per operator.

## Method
- paradigm: shared autonomy — a human teleoperator supplies coarse tracking intent (retargeted joint targets), and a real-time optimization-based (non-learned) controller computes a compliant correction
  - this is not RL or IL for the controller itself (no policy network, no reward/loss training an action-prediction model) — the "learning" component, if any, is confined to the retargeting mapping, which is a fixed vector-alignment (DexPilot-inspired) IK solve, not a trained network.
- algorithm: hand retargeting F_hand extracts K critical inter-joint/finger-to-palm target vectors v*_k from the tracked human hand and matches them to structural vectors computed via robot forward kinematics (DexPilot-style vector retargeting, not absolute joint-angle copying, to avoid morphology mismatch). The force-aware correction is a per-cycle QP with three cost terms: (1) localized force tracking ℓ_F — force-domain error r_i^F (how far each active finger's contact force ∥f_i∥ exceeds a desired window [f_min, f_max]) is projected into joint-displacement space via a virtual stiffness K_F giving residual ρ_i^F, and ℓ_F = weighted quadratic cost over ρ_F across active fingers, weighted by λ_F scaled by the per-finger activation w_i, using the operational-space contact Jacobian J_i(q) (interaction matrix A_F = −∂force/∂q, sign ensures corrections counteract destructive force buildup)
  - (2) multi-contact force-torque balance ℓ_B — net object-centric force F ∈ R^3 and torque τ ∈ R^3 are computed from all active contacts relative to the estimated object center p_obj, compared against target F*, τ* with a deadband filter ε to avoid fighting minor tracking noise, and mapped to joint space via ΔF ≈ A_F·Δq (force) and a skew-symmetric cross-product term [p_i]_× (torque), weighted by λ_fb, λ_tb
  - (3) a nominal stabilization term (Hessian H_0, linear term g_0) for smooth joint tracking. All three combine into a single box-constrained QP solved every control cycle at 30 Hz via a projected-gradient box-QP solver, subject to joint limits and a slew-rate saturation bound.
- key trick(s): estimating an object-centric reference frame purely from the mean of active contact points (no external object pose/model needed) is what lets the force-torque balance term work without object-specific instrumentation
  - the hysteresis-based logistic activation weight w_i smoothly fades a finger's contribution in/out around contact transitions rather than hard-thresholding, avoiding chattering.

## Evaluation
- metrics: Multi-Stage Success Rate — long-horizon tasks decomposed into stages, with failures in non-sequential stages (e.g., initial grasp in bimanual routines) not propagating to penalize later independent stages
  - Force Statistical Data — mean ± std of thumb contact force (N) through the task, used as a physical-safety/compliance index the authors explicitly note is "not... monotonically correlated with performance" (i.e., lower is not simply better if it comes with lower success — the goal is minimizing force while preserving success).
- headline numbers: Simulation (Table 2) — Ball Assembly: No-Residual Stage1/2/3 = 99%/10%/4%, force 31.58±10.48N
  - PD = 100%/6%/1%, force 29.96±9.75N
  - Force-Tracking-only ablation = 84%/78%/78%, force 11.03±5.01N
  - DexTeleop-0 = 100%/98%/97%, force 11.15±5.01N. Stir in Cup: No-Residual 100%/100%/60%, force 15.56±6.59N
  - PD 100%/100%/6%, force 12.45±5.28N
  - Force-Tracking 100%/100%/49%, force 8.01±2.50N
  - DexTeleop-0 100%/100%/59%, force 7.93±2.67N (DexTeleop-0 trades a marginally lower Stage-3 rate, 59% vs No-Residual's 60%, for half the contact force). Real robot (Table 3) — Gear Mesh: No-Residual 62.86%/11.43% (Stage1/2), force 2.12±1.60N
  - PD 77.14%/37.14%, 2.20±0.95N
  - Force-Tracking 94.29%/42.86%, 2.42±1.44N
  - DexTeleop-0 97.14%/57.14%, 2.47±1.07N. Peg Insertion: No-Residual 74.29%/25.71%, 3.98±2.12N
  - PD 80.00%/34.29%, 3.68±1.17N
  - Force-Tracking 91.43%/62.86%, 3.72±0.98N
  - DexTeleop-0 97.14%/60.00%, 5.17±3.13N (here DexTeleop-0 does not have the lowest force, attributed to operator caution/conservative strategies rather than the controller). Food Sorting (Table 4, 4 stages): DexTeleop-0 91.43%/97.14%/82.86%/74.29%, force 4.94±1.80N — best Stage-4 rate and lowest force among all 4 methods (No-Residual 71.43/51.43/54.29/48.57%, 6.92±1.48N; PD 65.71/68.57/62.86/51.43%, 5.13±0.83N; Force-Tracking 82.86/94.29/85.71/57.14%, 5.21±0.87N). Tube Operation (Table 5, 3 stages): DexTeleop-0 94.29%/100.00%/77.14%, force 6.87±1.91N vs No-Residual 60.00%/71.43%/34.29%, 7.80±3.50N.
- baselines beaten: No-Residual (exact kinematic mapping, no correction), Joint-Level PD Control (localized PD damping from raw tactile thresholds), Single-Force-Tracking ablation (only ℓ_F, no multi-contact balance ℓ_B) — the ablation shows ℓ_B (the balance term) is necessary for the largest gains, e.g. Ball Assembly Stage 3 rises from 78% (Force-Tracking only) to 97% (full DexTeleop-0) while force stays essentially flat (11.03N vs 11.15N), showing the balance term adds success without added force cost.
- real robot? Yes — twin UR7e + Sharpa Wave hardware rigs (56 DoF total), Meta Quest 3 teleoperation, 7 operators (5 inexperienced + 2 professional) × 5 trials/task/method, across Gear Mesh, Peg Insertion, Food Sorting, and Tube Operation.

## Limitations stated by the authors
Not stated as a dedicated Limitations section in the parsed text; the Conclusion frames remaining work as: integrating predictive slip-detection to adapt to unexpected object physical properties, and leveraging DexTeleop-0's collected visual-tactile trajectories to train generalizable IL policies for industrial/lab assembly tasks (Sec. 5) — both framed as future extensions rather than acknowledged weaknesses. The paper does note one honest negative result: on Peg Insertion, DexTeleop-0 does not achieve the lowest tactile force among methods, attributing this to operator caution rather than a controller failure (Sec. 4.2.2).

## Quotable claims (verbatim, with section)
- "the negative sign ensures that the calculated joint modifications actively counteract the accumulation of destructive contact forces" (Sec. 3.3.2).
- "without tracking adjustments, rigid kinematic overrides induce extreme interaction pressures (31.58±10.48 N for No Residual), causing the slippery spherical object to blast out of the multi-fingered grasp. In contrast, DexTeleop-0 regulates localized contact pressures to a safe distribution (11.15±5.01 N), maintaining a 97% success rate through Stage 3" (Sec. 4.2.1).
- "The No Residual method registers a mean tactile force of 15.56±6.59 N, which is twice the pressure exerted by DexTeleop-0 (7.93±2.67 N)" (Sec. 4.2.1).
- "incorporating localized tactile corrections and physical force-balancing directly into a tracking optimization loop is more critical for closing the embodiment gap and ensuring interaction safety than merely increasing baseline tracking resolution" (Sec. 5).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the "teleoperation quality / shared autonomy" section directly alongside teledexter_2026 and dexteritygen_2025 — but unlike both of those (which use a learned/RL low-level controller trained in simulation), DexTeleop-0's correction layer is a classical model-based QP with no learning component at all, making it the survey's clearest "non-learned shared-autonomy" contrast case. It is the only paper in this batch that reports actual contact-force magnitudes in Newtons as its safety metric (vs. teledexter_2026's differentiable-SDF penetration loss used only during offline retargeting, and vs. every IL/VLA paper's binary success-rate-only evaluation) — cite this directly when the survey builds its contact/force-measurement comparison table, since it is a genuinely different (and arguably more physically grounded) instrumentation choice than success rate alone. No dataset is produced for others to reuse; this paper is purely a teleoperation-quality mechanism, not a data-scaling contribution, so it should not be counted alongside dexwild_2025/dexumi_2025/dex1b_2025/unidex_2026/egoscale_2026 when the survey tallies "dataset hours/trajectories produced."
