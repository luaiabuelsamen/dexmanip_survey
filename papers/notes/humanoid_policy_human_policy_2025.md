# humanoid_policy_human_policy_2025 — Humanoid Policy ~ Human Policy (Qiu, Yuan, Bhardwaj, Li, Yuan, Tang, Chen, Zhu, Watanabe, Ramanan, et al.; CoRL 2025)

sources: papers/md/humanoid_policy_human_policy_2025.md [sha256 1452568a] ; code/md/humanoid_policy_human_policy_2025.md [commit 2d9d73cc]

## One-line contribution
PH2D (task-oriented egocentric human demonstrations collected with consumer VR devices: Apple
Vision Pro / Meta Quest 3, optionally with a ZED stereo camera) is co-trained with real
teleoperated humanoid data in a single Human Action Transformer (HAT) via a unified
human-and-robot state-action space (6D wrist rotations + wrist/fingertip 3D positions, bijectively
mapped since both use 5-fingered dexterous hands), giving ~100% relative improvement in
out-of-distribution success over robot-only ACT training and enabling few-shot cross-humanoid
transfer with only 20 target-robot demonstrations (Table 2, Fig. 5).

## Setting
- hand(s): 6-DoF Inspire dexterous hands (5-fingered) on both humanoid platforms (Sec. 4,
  "Hardware Platforms"). arm/base: Humanoid A = Unitree H1; Humanoid B = Unitree H1-2 with
  "different arm motor configurations" — used to test cross-humanoid transfer. Both humanoids
  have "actuated necks" (2-DoF) for egocentric head movement and no wrist cameras, mirroring
  human head motion (Sec. 3.2, Sec. 4). Bimanual: yes, "bimanual humanoid robots."
- simulator / physics: none — real-robot teleoperation data collection and real-robot evaluation
  throughout; no simulation training.
- observation: unified 54-D proprioceptive vector — "6D rotations of the head, left wrist, and
  right wrist; x/y/z of left and right wrists and 10 finger tips" (Sec. 3.2, "Unified
  State-Action Space") — used identically for human and robot states via a bijective
  finger-tip-to-finger-tip mapping (enabled because both use 5-fingered hands). Visual input:
  frozen DinoV2 ViT-S [67] encoder over egocentric RGB (human: VR-device camera or mounted ZED;
  robot: head-mounted camera on the actuated neck, no wrist cameras).
- action space: same unified 54-D representation predicted as action chunks by a
  transformer-based architecture (ACT-style [5]); at robot deployment, forward/inverse kinematics
  convert between the humanoid's native joint space and this wrist-pose + fingertip
  representation (Fig. 3 diagram: "Inverse Kinematics" / "Forward Kinematics" boxes bridge
  humanoid joint control and the shared 6-DoF-wrist + fingertip space).
- objects / data: PH2D — task-oriented human demos collected via 2 device configurations: (1)
  Apple Vision Pro + built-in camera with ARKit 3D head/hand pose; (2) Meta Quest 3 / Apple Vision
  Pro + a 3D-printed ZED Mini stereo-camera mount, via an OpenTelevision-based web app, "<$700"
  (Sec. 3.1). Robot data: "approximately 250-400 robot demonstrations" per task via teleoperation
  (Sec. 4, "Implementation Details"). 4 real dexterous tasks: Passing, Horizontal Grasp, Vertical
  Grasp, Pouring (Table 2).

## Method
- paradigm: supervised imitation learning (action-chunking transformer, ACT-style) co-trained
  jointly on human and teleoperated-robot demonstrations in one shared architecture — NOT RL, NOT
  hierarchical (no separate human-data planner + robot low-level policy, unlike Mimicplay-style
  approaches referenced in egomimic_2024's related work) NOT reward-from-video.
- **human data source and size**: self-collected task-oriented egocentric demonstrations (PH2D),
  NOT internet video — explicitly designed as "a scalable source of cross-embodiment training
  data" gathered with consumer VR hardware, with language instructions per demo (e.g. "grasp a
  can of coke zero with right hand"). Human data volume is asserted to be much larger than robot
  data: "it is reasonable to assume M >> N due to significantly better human data collection
  efficiency" (Sec. 3.2). Quantified collection-time comparison (Appendix A, Table 5): regular
  human demo 3.79+-0.27s (grasping) / 4.81+-0.35s (pouring); human demo while wearing VR
  4.09+-0.30s / 4.90+-0.26s (near-identical, VR doesn't slow humans down); Humanoid teleop demo
  19.72+-1.65s / 37.31+-6.25s — roughly 5-8x slower per demo than human collection, with most
  overhead attributed to "the retargeting process from human actions to robot actions... latency
  and the constrained workspace of 7-DoF robotic arms."
- **what is extracted from video**: on-device SDK outputs only — world-frame 3D head pose and 3D
  hand keypoint tracking, obtained directly from Apple ARKit or the OpenTelevision-based Quest/
  ZED pipeline (Sec. 3.1) — no separate offline pose-estimation model (e.g. no MANO/SLAHMR/HaMeR
  fitting as in dexmv_2021/okami_2024/egozero_2025); the VR device's own real-time hand tracking
  IS the extraction step, "which has proved to be stable enough to teleoperate robot in
  real-time." No object pose, affordance, or reward signal is separately extracted.
- **human-to-robot mapping**: because both embodiments are represented in the identical 54-D
  unified space, there is largely no separate offline retargeting network — the paper states "we
  design a unified state-action space... for both bimanual robots and humans," with "a bijective
  mapping between the finger tips of robot hands and human hands" since the deployed hands are
  also 5-fingered (Sec. 3.2) — i.e. correspondence, not kinematic-chain optimization. Robot-side
  execution still needs inverse kinematics from the shared wrist/fingertip space to native joint
  commands (Fig. 3), but this is a standard IK step, not a human-specific retargeting
  optimization. Two domain gaps are explicitly bridged with heuristics, not learned mappings: (1)
  ACTION SPEED — humans complete tasks much faster than teleoperated robots, so human action
  trajectories are slowed by interpolation with factor "alpha_slow = 4... obtained by normalizing
  the average task completion time of humans and humanoids... empirically distributed around 4"
  (Sec. 3.1); (2) WHOLE-BODY MOVEMENT — humans involuntarily move their torso/shoulders during
  manipulation in ways the robot cannot replicate, mitigated only by INSTRUCTING human collectors
  to "sit in an upright position" (Sec. 3.1) rather than by any algorithmic correction.
- **RL or SL**: supervised behavior cloning, transformer action-chunking loss:
  `L = sum ||A_hat - A||^2 + lambda * sum_{i in EEF} ||A_hat_i - A_i||^2` (paraphrased from Sec.
  3.2's description: an overall action-chunk loss plus an extra-weighted term on the "translation
  vectors of the left and right wrists," lambda=2, "used to balance loss to emphasize the
  importance of end effector positions over learning unnecessarily precise finger tip
  keypoints" — quoted structure, exact equation not fully recovered as text).
- key trick(s): unified 54-D cross-embodiment state-action space (ablated directly, see below);
  action slow-down interpolation (alpha_slow=4, ablated); basic visual augmentation (color
  jitter, Gaussian blur) instead of heuristic visual masking or generative domain adaptation —
  "we find it not a strict necessity to apply heuristic processing such as visual artifacts [16]
  or generative methods [69]... with sufficiently large and diverse data" (Sec. 3.2); frozen
  DinoV2 visual backbone (not fine-tuned).
- **explicit embodiment-gap ablation (Table 3, "Importance of unifying policy inputs and
  outputs," Vertical Grasping task, out of 10 trials)**: unified-state + slowed-action (full
  method) = 4/10; unified state WITHOUT action-speed interpolation = 1/10 ("the speed of the
  predicted actions fluctuates between fast (resembling humans) and slow (resembling
  teleoperation), which leads to instability"); action-speed interpolation WITHOUT a unified
  state (separate joint-position state for robot vs. EEF-representation state for human) = 0/10
  ("the policy is given a 'shortcut' to distinguish between embodiments, which leads to on-par
  in-distribution performance and significantly worse OOD performance"). This is the paper's
  direct, quantified statement of what naively NOT bridging the embodiment/speed gap costs.
- domain randomisation: none in a simulated sense (real-robot only); the closest analog is
  deliberately collecting human data with far more environmental diversity (backgrounds, object
  types/positions, human-to-table relative position) than the robot teleoperation data (Sec. 4,
  "Experimental Protocol").
- contact / penetration handling: not addressed — no interpenetration term, no contact-force
  metric; success is judged by task completion (object passed/grasped/poured).

## Evaluation
- metrics: binary real-robot task success, reported as trial fractions, separately for
  in-distribution (I.D., matching training scene/object setup) and out-of-distribution (O.O.D.,
  "novel setups that were presented in human data but not in robot data") conditions (Sec. 4,
  "Experimental Protocol"; Table 2).
- headline numbers (Table 2, 4 tasks x I.D./O.O.D., trial counts vary by task): overall I.D.
  success ACT 42/60 vs. HAT(no data-norm ablation) 45/60 vs. HAT(with data norm) 49/60; overall
  O.O.D. success ACT 59/170 vs. HAT(w/o norm) 97/170 vs. HAT(with norm) 101/170 — "nearly 100%
  relative improvement" OOD from co-training with human data (Sec. 4.1). Per-task OOD deltas are
  large and consistent: Horizontal Grasp OOD 7/30 (ACT) vs. 12/30 (best HAT); Vertical Grasp OOD
  15/70 (ACT) vs. 30/70 (best HAT); Pouring OOD 1/10 (ACT) vs. 8/10 (best HAT). I.D. performance
  is comparable across methods ("human data has minor effects on I.D. testing," Sec. 4.1).
  Cross-humanoid few-shot transfer (Fig. 5, Sec. 4.2): with only 20 Humanoid-B demonstrations,
  co-training with Humanoid A + Human data "substantially outperformed the Humanoid B-only
  baselines on all task settings"; co-training also "consistently outperformed isolated training
  as Humanoid B demonstrations increase... even in low-data regimes." Sampling-efficiency
  experiment (Fig. 6, fixed 20-minute collection budget): robot-only data (60 or 30 Humanoid-A
  demos) achieves 28/90 grid-cell successes vs. mixed robot+human data (120 human demos added)
  achieving 35/90. Background-generalization deep-dive (Appendix C, Table 7, cup-passing task):
  ACT 16/40 overall vs. HAT 21/40 overall across 4 backgrounds/objects, with HAT winning or tying
  every column.
- baselines beaten: ACT [5] (same action-chunking-transformer architecture, robot-only data,
  joint-position state representation) — the paper's controlled baseline isolating the value of
  human co-training and the unified representation; internal ablations (HAT without data
  normalization, HAT without unified state space, HAT without action-speed interpolation) serve
  as additional baselines within the same architecture.
- real robot? Yes, entirely real (Unitree H1/H1-2 humanoids with Inspire hands). Trial counts
  given per task/condition in Table 2 (e.g. Passing I.D. 20 trials, O.O.D. 60 trials; Vertical
  Grasp O.O.D. 70 trials); overall totals 60 I.D. / 170 O.O.D. trials across 4 tasks for the main
  comparison; additional trial counts for cross-humanoid (Fig. 5), sampling-efficiency (90-cell
  grid, Fig. 6), and background-generalization (40 trials, Appendix C) experiments.

## Limitations stated by the authors
- "one limitation of the current version of the paper uses a relatively simple architecture for
  learning policy" — no large language-conditioned cross-embodiment policy yet, planned as future
  work (Sec. 6).
- VR hand-tracking SDKs are consumer-grade and can fail: "hand keypoint tracking can fail for
  certain motions with heavy occlusion" since the SDKs "were trained mostly for VR applications"
  (Sec. 6).
- "though the proposed method conceptually extends to more robot morphologies, current
  evaluations are done on robots equipped with dexterous hands" — no test of the unified-space
  idea on grippers or other embodiments (Sec. 6).
- Human whole-body movement during manipulation "leads to degraded performance" when replicated
  by current humanoids, mitigated only by instructing operators to minimize movement, not solved
  algorithmically (Appendix A).
- Most retargeting/teleoperation overhead (and hence most of the human-vs-robot speed advantage)
  comes from "latency and the constrained workspace of 7-DoF robotic arms," an infrastructure
  limitation rather than an algorithmic one (Appendix A).

## Quotable claims (verbatim, with section)
- "it is reasonable to assume M >> N due to the significantly better human data collection
  efficiency" (Sec. 3.2).
- "Without a unified state space, the policy is given a 'shortcut' to distinguish between
  embodiments, which leads to on-par in-distribution performance and significantly worse OOD
  performance" (Sec. 4.3).
- "co-training drastically improves O.O.D. settings, achieving nearly 100% relative improvement
  in settings unseen by the robot data" (Sec. 4.1).
- "wearing a VR device does not significantly impact human manipulation speed, as the completion
  time remains nearly the same as in standard human demonstrations" (Appendix A).

## Notes for the survey
Feeds the "human video/demo co-trained jointly with robot demos in one shared policy" branch,
alongside egomimic_2024, but differs in two structural ways worth flagging for comparison: (1)
this paper's robot uses genuine 5-fingered dexterous hands with a claimed BIJECTIVE
fingertip-to-fingertip correspondence to the human hand (no kinematic optimization needed),
whereas egomimic_2024's gripper needed only a 6-DoF pose alignment and dexvip_2022/dexmv_2021's
retargeting needed full kinematic-chain optimization because DoF counts differ; (2) human pose
extraction here is live on-device VR SDK output (ARKit / OpenTelevision), not an offline
video-processing pipeline (contrast egozero_2025's HaMeR+Aria-MPS fusion or okami_2024's
SLAHMR+HaMeR reconstruction) — a genuinely different "what is extracted" answer worth
distinguishing in the survey table. Table 3 is one of the best-isolated "embodiment-gap-mitigation
cost" ablations in this batch: removing action-speed alignment alone or removing the unified state
space alone each roughly halves-to-zeros success (4/10 -> 1/10 or 0/10) on the same task,
comparable in sharpness to egozero_2025's 0/15 ablation collapses. Block D: physical plausibility
of the extracted hand-object interaction is not checked at all — no interpenetration or
contact-force metric anywhere in the pipeline or its ablations; all evaluation is real-robot task
success, and the closest the paper comes to a plausibility statement is the qualitative note that
VR hand tracking "can fail for certain motions with heavy occlusion" (Sec. 6), which is a tracking
reliability caveat, not a check on whether the tracked hand-object interaction itself is physical.
