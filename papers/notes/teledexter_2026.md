# teledexter_2026 — Towards Human-level Dexterous Teleoperation (Li, Chen, Wu, Wei, Li, Wang, Shi, Yu, Jia, Zhu, Liu, Huang; Tsinghua/BIGAI/PKU, arXiv 2026)

sources: papers/md/teledexter_2026.md [sha ee5ffe42] ; no code

## One-line contribution
TELEDEXTER is a hand-object co-tracking low-level controller, trained with single-stage RL (SAPG, Isaac Gym) on "consecutive subgoal" targets derived from geometry-aware-retargeted human hand-object reference motions, that lets a teleoperator specify fingertip+object-pose goals rather than raw joint angles, transferring zero-shot to real robots and reaching 75.2% average success rate / 87.1% average task progress across 7 real-world in-hand reorientation and long-horizon tool-use tasks on two dexterous hands, where every kinematic-retargeting or prior-learned-action-prior baseline (DexRT, GeoRT, DexGen, SimToolReal) fails almost completely.

## Setting
- hand(s): LeapHand (4-finger, 16 DoF) and SharpaWave (5-finger, human-like, 22 DoF)
  - both mounted on a Franka FR3 arm (arm tracked via IK to the operator's wrist pose, independent of the hand controller)
  - single-hand only.
- simulator / physics: Isaac Gym for RL training
  - SAPG used as the RL optimizer/parallelization scheme, ~62,000 parallel environments on 4 NVIDIA RTX 5090 GPUs, converging within ~10^10 environment steps
  - all reference motions for one object (~50 minutes of human data) loaded simultaneously per training run — i.e. one controller is trained per object.
- observation: o_t = [current hand joint positions q_t, object pose (x_t^o, R_t^o), gravity direction in the wrist frame, previous action a_{t-1}]
  - policy also conditioned on the co-tracking goal g_t = (p̂_t^tip, T̂_t^o) — target fingertip positions (N_f×3) and target object SE(3) pose.
    - Real-world perception uses a NOKOV motion-capture system tracking operator hand pose and object 6D pose (not vision-based hand tracking, not tactile).
- action space: a_t ∈ R^{n_dof}, target joint positions; robot arm separately IK-tracks the wrist pose. All quantities expressed in the wrist frame.
- objects / data: human hand-object reference motions recorded by motion capture, spanning 3 categories — in-hand translation, in-hand rotation, and free-play (arbitrary grasps, finger gaiting, tool-use sequences)
  - ~50 minutes of reference motion per object used for training.
    - This is human motion data (not robot teleoperation data) converted into robot-executable reference trajectories via retargeting — the RL controller itself is trained purely in simulation on these retargeted trajectories, not on raw human video/keypoints as an action-prediction target.

## Method
- paradigm: RL (single-stage, no staged skill decomposition, no per-task reward engineering) using human hand-object motion as reference/subgoal supervision — "hybrid reward that couples sparse subgoal objectives with dense tracking rewards"
  - distinct from IL/BC (the controller is not behavior-cloned from demonstrations; demonstrations are only used indirectly, first to build reference motions for RL, and later — via TELEDEXTER's own teleoperation output — as BC training data for a separate downstream autonomous-policy experiment, Sec. 4.3).
- algorithm: policy a_t = π_θ(o_t, g_t) trained via RL (SAPG optimizer) in Isaac Gym. "Consecutive subgoal co-tracking": each reference trajectory is converted into a sequence of co-tracking subgoals g_k = (p̂_k^tip, T̂_k^o) sampled at varying intervals
  - the policy must reach each subgoal in order (indicator 1_reach(t) fires when the active subgoal is reached) before advancing, discovering its own contact strategy freely between subgoals — contrasted explicitly against dense frame-wise tracking, which the paper argues is "overly restrictive for single-stage policy learning" (Sec. 2, Related Work) and empirically confirmed in the ablation (Table 4).
- Reward/objective block (quoted structurally, Sec. 3.1): reward = weighted combination of a reaching reward (fires via 1_reach(t), scaled by w_step, the inter-subgoal step size) and a dense tracking reward r_dense (uses the same per-finger, object-position, and object-rotation tracking-error terms at every timestep, scaled by α_dense, "providing a small dense signal during early training")
  - r_score measures per-subgoal match quality using per-finger tip error, object position error, and object rotation error terms (exact formulas not fully recoverable from the parsed markdown — equations appear as unrendered blocks in the source, e.g. "the per-finger, object position, and object rotation tracking errors are" with the equation itself missing from the parsed text; flagged as a parsing gap, not inferred).
- key trick(s): (1) Curriculum learning over three axes — gravity annealed from reduced to full
  - subgoal tolerances (ε_tip, ε_pos, ε_rot) tightened from permissive to strict
  - inter-subgoal step size grown from small to large
  - episodes initialize at random reference-motion frames and cross-trajectory-reset on successful traversal. (2) Random action masking for sim-to-real: sample binary mask m_t ∈ {0,1}^{n_dof}, apply ã_t = m_t⊙a_t + (1−m_t)⊙ã_{t-1} — masked joints are frozen at the previous command for a randomly sampled duration, forcing the policy to succeed with stale/desynchronized joint commands, explicitly to prevent overfitting to simulation-only actuation synchrony. (3) Geometry-aware retargeting (Sec. 3.2): two-stage pipeline — Stage 1 is standard vector-based retargeting (directional/inter-finger vector alignment, loss L_vec) to match human hand geometry
  - Stage 2 refines with an object-mesh-aware optimization combining L_surf (ReLU(sdf_O(p)) pulling near-contact hand points onto the object surface, for points with sdf < τ_surf), L_pen (ReLU(−sdf_O(p)) penalizing hand-mesh interpenetration into the object), L_col (a self-collision term using collision spheres of radii r_i,r_j at finger centers c_i,c_j to prevent inter-finger overlap), and L_smooth (Curobo temporal-smoothness energy to suppress mocap jitter).
    - Fingertip targets are then p̂_t^tip = FK_tip(q_t*) and object targets T̂_t^o = T_t^o from the optimized trajectory.
- D.
  - Contact/penetration handling: the retargeting pipeline explicitly quantifies and penalizes hand-object mesh interpenetration via L_pen = Σ_p∈H_t ReLU(−sdf_{O_t}(p)) as part of constructing the reference motion (this is the only paper in this batch with an explicit, differentiable-SDF penetration term used during data construction, distinct from a policy reward).
  - The RL training reward itself is tracking-based (subgoal + dense tracking), not explicitly penetration-penalized — contact/penetration handling is confined to the reference-motion construction stage, not the controller's reward function.

## Evaluation
- metrics: Success Rate (SR) = percentage of trials completing all task stages
  - Task Progress (TP) = average percentage of stages completed per trial (each stage weighted equally)
  - trial terminated on unrecoverable grasp loss or object drop
  - 15 trials per task per method.
- headline numbers (Table 1, SharpaWave hand, SR/TP %): TELEDEXTER average 75.2/87.1 across 7 tasks, vs.
  - DexRT 5.7/37.6, GeoRT 0.0/28.5, DexGen 0.0/25.0, SimToolReal† (3 tasks only) 8.9/28.9, SimToolReal‡ (all categories) 6.7/20.6.
  - Per-task TELEDEXTER results: CylinderReorient 80.0/86.7, CuboidReorient 80.0/86.7, BunnyReorient 66.7/77.8, HammerUse 66.7/86.7, BrushSweep 73.3/89.5, ScrewdriverUse 73.3/86.7, BulbReplace 86.7/95.6 — all far above every baseline's near-zero SR on tool-use tasks.
  - LeapHand (Table 2, same reference motions, only retargeting stage adapted): CylinderReorient 60.0/73.3, CuboidReorient 73.3/82.2.
  - Stage-level detail: on BulbReplace, 15/15 trials survive through stage 4 of 6 (screw-in + unscrew), with the only failures at final placement (13/15 succeed there)
  - on ScrewdriverUse, 13/15 trials sustain continuous finger gaiting through the tightening stage.
- ablations: consecutive subgoal vs. dense frame-wise tracking (Table 4, simulation, held-out motions for Cuboid/Hammer/Screwdriver) — under dense evaluation, "ours" (subgoal-trained) gets episode length 378.6/376.9/373.2 vs. dense-trained baseline's 115.8/131.2/88.7
  - under sparse evaluation (goals reached), ours gets 32.6/186.6/178.5 vs. dense baseline's 2.6/2.7/2.7 — orders-of-magnitude gap.
    - Random action masking (Table 5, real robot, 3 tasks): w/ AM vs w/o AM — HammerUse 66.7/86.7 vs 33.3/57.1, ScrewdriverUse 73.3/86.7 vs 0.0/36.0, CuboidReorient 80.0/86.7 vs 26.7/51.1 — removing action masking causes "substantial degradation across all evaluated tasks."
- baselines beaten: DexRT (pure kinematic retargeting, [5,6]), GeoRT (learned neural retargeting), DexGen (dexteritygen_2025 — learned generative action prior; this note's DexGen baseline corresponds to the same DexterityGen method reviewed separately in this batch), SimToolReal (object-centric sim-to-real tool policy, not itself a teleoperation method, included as "a strong reference").
- real robot? Yes, exclusively — all numbers above are real Franka FR3 + LeapHand/SharpaWave trials (15 trials/task/method), teleoperated at 30 Hz via NOKOV mocap.
  - Separate downstream autonomous-policy experiment (Sec. 4.3): Diffusion Policy (Conv-UNet architecture) trained via BC on 50 TELEDEXTER-collected demonstrations per task, evaluated over 15 real trials per task on BulbInstall (46.7% SR, stage breakdown 13/15→12/13→8/12→7/8), HammerDriver (73.3% SR, 15/15→15/15→11/15), BrushForward (40.0% SR, 7/15→7/7→6/7) — "no baseline teleoperation system evaluated in Table 1 can reliably complete any of these three tasks, making it infeasible to collect comparable demonstration data with existing methods."

## Limitations stated by the authors
TELEDEXTER "currently learns an object-specific controller" — adapting to a new object requires collecting new human hand-object interaction data and training a dedicated policy from scratch; scaling to a unified object-conditioned controller across categories without per-object data/training is left as future work. Real-world deployment depends on a motion-capture system for real-time hand and object pose estimation; replacing this with markerless vision-based tracking "would significantly lower the barrier to deployment" (Sec. 6).

## Quotable claims (verbatim, with section)
- "achieving a 75% average success rate where all baselines consistently fail" (Abstract).
- "TELEDEXTER achieves 75.2% average SR and 87.1% average TP across all seven tasks, while all baselines near-uniformly fail" (Sec. 4.2).
- "TELEDEXTER's narrow SR-to-TP gap (75.2% vs. 87.1%) indicates that most failures happen at late task stages, whereas baselines consistently collapse at the first stage requiring in-hand reorientation or finger gaiting" (Sec. 4.2).
- "Despite this substantial morphological gap, LeapHand achieves 60.0–73.3% SR on the reorientation tasks, confirming that the framework generalizes across embodiments without re-collecting human reference motions" (Sec. 4.2).
- "TELEDEXTER currently learns an object-specific controller.
  - Adapting to a new object requires collecting human hand-object interaction data and training a dedicated policy" (Sec. 6).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the "teleoperation with a learned low-level dynamics/contact controller" section directly against dexteritygen_2025 (its DexGen prior is used here as a baseline that TELEDEXTER beats decisively, 0.0% SR vs. 66.7-86.7% SR on the same class of reorientation/tool-use tasks — a rare direct head-to-head between two papers in this batch) and dexteleop0_2026 (also a teleop-quality paper, check for overlap/contradiction on force-aware shared autonomy). TELEDEXTER's retargeting-stage penetration loss (L_pen, differentiable SDF) is the most explicit, quotable penetration-handling formulation in this entire batch — directly relevant to the survey's "contact/penetration handling" comparison table, and notably it penalizes penetration only during offline reference-motion construction, not during the RL reward itself, which is a design choice worth flagging against opposition-deficit's own dense-grid, policy-independent contact measurement philosophy (the reward the policy optimizes is subgoal/tracking-based, not penetration-based — consistent with CLAUDE.md's warning that "the measure a policy optimises is never the measure that judges it," though this paper does not raise that concern itself). Its single-stage RL + subgoal-tracking recipe (vs. dense frame-wise imitation) is a clean, quantified ablation (Table 4, orders-of-magnitude gap) that the survey should cite when comparing reference-motion-tracking formulations across RL-from-human-motion papers.
