# egomimic_2024 — EgoMimic: Scaling Imitation Learning via Egocentric Video (Kareer, Patel, Punamiya, Mathur, Cheng, Wang, Hoque, Xu; ICRA 2025)

sources: papers/md/egomimic_2024.md [sha256 227fe304] ; code/md/egomimic_2024.md [commit 6d63e9a3]

## SCOPE FLAG
EgoMimic's robot end-effector is a parallel-jaw gripper on a 6-DoF ViperX 300 S arm (ALOHA-style
bimanual rig), NOT a multi-fingered dexterous hand — "Robot proprioception data includes...
Joint positions R_q in R^(2x7) (including the gripper jaw joint position)" (Sec. III-B, Table I).
Recorded here for completeness since it was named in the batch, but it does not test a dexterous
hand's finger-level retargeting; its "hand pose" signal is a 6-DoF wrist/palm pose used to derive
an end-effector target, not per-finger joint angles.

## One-line contribution
EgoMimic co-trains a single ACT-based transformer policy on paired egocentric human video (Aria
glasses, 3D hand pose from onboard SLAM+hand-tracking) and teleoperated bimanual robot
demonstrations, bridging the domains via a shared camera viewpoint (a second Aria mounted on the
robot), per-embodiment Gaussian action/proprioception normalization, and SAM-based visual
masking+red-line overlay of hand/gripper — yielding 8-33% higher success and up to 228% higher
task score than ACT-only and Mimicplay baselines on 3 real long-horizon bimanual tasks (Table
III), with an ablation showing removing human data costs 47% of task score (Table IV).

## Setting
- hand(s)/end-effector: parallel-jaw gripper (see SCOPE FLAG); arm: 6-DoF ViperX 300 S x2 (custom
  low-cost bimanual rig, "<$1,000 excluding the ViperX arms," inverted-mount torso rig,
  ALOHA-inspired). Bimanual: yes.
- simulator / physics: none — real-robot only, no sim training or eval.
- observation: robot — egocentric Aria-glasses RGB (mounted on the robot torso "at a location
  similar to that of human eyes") + 2 wrist RealSense D405 cameras; proprioception R_p (SE(3) x
  SE(3) EEF poses) and R_q (joint positions in R^(2x7), gripper jaw as a joint). Human — Aria
  egocentric RGB + 3D hand poses H_p in SE(3) x SE(3) from Aria's Machine Perception Service
  (MPS) SLAM+hand-tracking (Table I). Both hand and robot arm are visually masked via SAM2 with a
  red directional line overlay before being encoded by a shared ResNet18 visual encoder
  (Appendix A; code: `egomimic/scripts/masking/hand_overlay.py`).
- action space: dual heads — pose-space action chunks a_p (human hand pose track / robot EEF
  pose track, both supervised) and joint-space action chunks a_q (robot-only, since joint control
  is used for actual robot execution due to "low solution redundancy" of the 6-DoF ViperX causing
  singularities under Cartesian control, Sec. III-C). Action chunk size 100, robot chunk horizon
  4s vs. human chunk horizon 1s (a 4x "slow-down" alignment factor, Appendix A) — recorded at
  30 Hz (human)/50 Hz (robot) natively.
- objects / data: 3 real long-horizon bimanual tasks (Table II): Continuous Object-in-Bowl (1400
  human demos / 60 min, 270 robot demos / 120 min), Groceries (160 human / 80 min, 300 robot /
  300 min), Laundry (590 human / 100 min, 430 robot / 300 min).

## Method
- paradigm: supervised imitation learning (BC) via a shared-backbone ACT [1] variant jointly
  trained on human and robot action-chunk regression losses — NOT RL, NOT reward-from-video.
  Explicitly contrasted with hierarchical human-data approaches (e.g. Mimicplay's high-level
  planner + low-level policy), which EgoMimic argues bottleneck on the low-level policy's own
  performance (Sec. III-C).
- **human data source and size**: self-collected egocentric video via Project Aria glasses
  (head-worn, 75g), NOT a preexisting internet dataset — "large scale data collection efforts
  underway with Project Aria" are noted as future integration, not used here. Per-task counts:
  1400 demos (Object-in-Bowl), 160 (Groceries), 590 (Laundry) (Table II) — collected far faster
  per unit time than robot teleop demos: "one hour of human data yields 1400 demonstrations,
  compared to only 135 demonstrations from an hour of robot data" (Sec. IV-B).
- **what is extracted from video**: per-frame 3D hand pose H_p in SE(3) x SE(3) (both hands) from
  Aria's onboard MPS (cloud SLAM + hand-tracking service, using the glasses' RGB + side mono
  scene cameras which keep tracking hands even when they leave the main RGB FOV, Sec. III-A) and
  device pose T_F^W for camera-frame stabilization; NO object pose, affordance map, or reward
  signal is extracted. Notably, "human data lacks information for the grasping action, since Aria
  only records hand pose" (Appendix C) — grip/close state is never observed from the human
  stream at all.
- **human-to-robot mapping**: NOT a kinematic hand-pose retargeting (no MANO, no per-finger IK) —
  because the end effector is a gripper, only a 6-DoF pose-track alignment is needed. Three
  explicit alignment stages (Sec. III-B): (1) unify BOTH streams into a common per-timestep
  camera-centered reference frame (`a_t:t+h^p` transformed into the observation camera frame F_t
  using Aria's SLAM pose for human data, and hand-eye calibration's fixed camera frame for robot
  data) so the policy needn't reason about future camera motion; (2) per-embodiment Gaussian
  (Z-score) normalization of proprioception/actions independently for hand vs. robot, since raw
  pose distributions differ ("discrepancies arise from biomechanical differences, task execution
  variations, and measurement precision disparities," Sec. III-B) — "we found this simple
  technique to be empirically effective" (ablated: -38% score without it, see below); (3) visual
  appearance masking — SAM2 masks the hand/gripper region (using projected 3D keypoints, robot
  via forward-kinematics-derived wrist/gripper/forearm coordinates, human via 3D hand-pose
  coordinates) and overlays a red directional line, applied identically at train and test time
  (test-time SAM2 runs live on the robot). This is a domain-ALIGNMENT scheme, not a
  finger-embodiment retargeting scheme — there is no finger DoF to map since the robot is a
  gripper.
- **RL or SL**: supervised (BC), joint MSE regression losses per Algorithm 1: `L_H_p =
  MSE(a_hat_p, a_p)` (human pose branch), `L_R_q = MSE(a_hat_q, a_q)` and `L_R_p = MSE(a_hat_p,
  a_p)` (robot joint and pose branches), optimized jointly as `L = L_H_p + L_R_p + L_R_q` each
  step (Alg. 1, Appendix C gives the fuller form including the ACT/CVAE KL regularizer:
  `L = L_robot + L_hand` where each includes an L1 pose/joint term plus the CVAE KL term as in
  ACT). Grasp/gripper action is supervised ONLY via the robot joint loss (since human data has no
  grasp signal): "the grasping action is supervised only via the robot joint prediction loss
  L1(R_a_hat^j, R_a^j), where the gripper is represented as another joint" (Appendix C).
- key trick(s): matched camera hardware (a second Aria mounted on the robot) to minimize the
  observation-domain gap directly in hardware, rather than only in software; shared-transformer
  architecture with only 2 shallow input/output heads differing by embodiment ("Since the two
  branches are separated by only one linear layer, we effectively force the model to learn joint
  representations for both domains," Sec. III-C); dual pose+joint action heads specifically
  because the 6-DoF ViperX arm has low IK redundancy and cannot be reliably Cartesian-controlled.
- domain randomisation: no simulated randomization (real-robot only); robot data collection
  deliberately perturbs "the robot's position" during teleop to "improve robustness" (Sec.
  IV-A), and task-level initial-condition randomization is used at eval (object positions within
  specified cm ranges, shirt rotation +-30 deg, etc., Sec. IV-A) but this is evaluation-condition
  variation, not training-time domain randomization.
- contact / penetration handling: not addressed — no reward, no interpenetration or grasp-force
  metric. Success/points are behavioral/outcome-based (toy placed in bowl, sleeve folded, pack
  placed in bag), never a contact-quality measurement.

## Evaluation
- metrics: task-specific point scores (Pts, partial credit per completed stage) and binary
  full-task success rate (SR), plus a task-specific "Open Bag" sub-metric for Groceries (Sec.
  IV-A, Table III). Object-in-Bowl: "45 total evaluation rollouts across 9 bowl-toy-position
  combinations." Laundry: "40 total evaluation rollouts across 8 shirt-position combinations."
  Groceries: "50 evaluations across 10 bag positions."
- headline numbers (Table III): EgoMimic beats ACT and Mimicplay on all 3 tasks — Object-in-Bowl
  Pts: EgoMimic 128 vs. ACT 39 vs. Mimicplay 71 vs. EgoMimic-w/o-human 68 (a 228% score
  improvement over ACT per Sec. IV-B); Laundry Pts/SR: EgoMimic 114/88% vs. ACT 82/55% vs.
  Mimicplay 78/50% vs. w/o-human 104/73%; Groceries Pts/SR/OpenBag: EgoMimic 110/30%/70% vs. ACT
  82/22%/54% vs. Mimicplay 53/8%/40% vs. w/o-human 92/28%/60%. Text: "relative improvement in
  score of 34-228%, and an improvement in absolute task success rate from 8-33% over ACT."
  Human-data ablation (comparing EgoMimic to EgoMimic-w/o-human, isolating data contribution from
  architecture): "10-88% improvement in score and 2-15% improvement in success rate." Component
  ablation (Table IV, Object-in-Bowl points only): full EgoMimic 128; w/o red-line overlay 112
  (-13%); w/o line+mask 95 (-26%); w/o action normalization 79 (-38%); w/o hand data at all 68
  (-47%). Generalization (Fig. 7): unseen shirt colors — ACT 25% SR vs. EgoMimic 85% SR (fully
  retained); unseen scene for Object-in-Bowl — EgoMimic scores 63 pts using zero additional robot
  data, vs. Mimicplay (same human data, hierarchical architecture) scoring only 4 pts. Data-ratio
  scaling (Fig. 8): EgoMimic with 2h robot + 1h human data (128 pts) beats ACT with 3h robot data
  alone (74 pts); note EgoMimic at matched 2h robot data (no human) already beats ACT at 2h,
  "so some improvement is attributed to architecture."
- baselines beaten: ACT [1] (same backbone, robot-only data), Mimicplay [5] (hierarchical
  human-data planner + low-level policy, re-implemented with the same transformer backbone and
  goal-conditioning removed for fair single-task comparison), EgoMimic (0% Human) / "w/o human
  data" (architecture-only ablation isolating the value of the human data itself, not just the
  unified architecture).
- real robot? Yes, entirely real (custom ViperX bimanual rig). Trial counts explicit per task:
  45 (Object-in-Bowl), 40 (Laundry), 50 (Groceries) rollouts for the main comparison; generalization
  and scaling experiments use additional but not separately itemized rollout counts (embedded in
  Fig. 7/8).

## Limitations stated by the authors
- Human data provides no grasp-state signal at all: "the human data lacks information for the
  grasping action, since Aria only records hand pose" (Appendix C) — the gripper-close decision
  is learned purely from the smaller robot dataset.
- Joint-space (not Cartesian) robot control is required only because of this specific hardware's
  low IK redundancy: "more capable robots that better support end-effector space control can
  eliminate the need for predicting joint-space actions" (Sec. III-C) — a hardware-specific
  workaround, not a general claim.
- Future work: "generalizing to new robot embodiments and entirely new behaviors demonstrated
  only in human data, such as folding pants instead of shirts" (Sec. V) — cross-embodiment and
  behavior transfer beyond the trained tasks is not yet demonstrated.
- Alignment techniques (temporal slow-down factor of 4, per-embodiment normalization) were tuned
  empirically ("we found empirically that a factor of 4 sufficiently aligned both domains,"
  Appendix A) rather than derived, and the authors note plans to explore alternatives such as
  action quantization instead of Gaussian normalization (Sec. III-B).

## Quotable claims (verbatim, with section)
- "Without mitigating this gap, the policy tends to learn separate representations for the two
  data sources, preventing performance scaling with human data" (Sec. III-B).
- "one hour of human data yields 1400 demonstrations, compared to only 135 demonstrations from an
  hour of robot data" (Sec. IV-B).
- "EgoMimic trained without any hand data, yields a large 47% drop, which highlights how
  effective hand-robot co-training is on our stack" (Sec. IV-B).
- "the human data lacks information for the grasping action, since Aria only records hand pose"
  (Appendix C).

## Notes for the survey
Belongs in this batch as a scope-boundary case (see SCOPE FLAG): its "dexterity" is a 2-finger
gripper's binary open/close, not a multi-finger hand, so there is no per-finger kinematic
retargeting to compare against dexmv_2021/dexvip_2022/okami_2024's hand-mapping pipelines. What
it DOES offer that is directly useful for the survey's "embodiment gap cost" question is the
cleanest ablation ladder in this batch isolating each domain-alignment component's individual
contribution to closing a human-robot data gap: action normalization (-38% without it), visual
masking+line overlay (-26% without both), and human data itself (-47% without any) — all measured
on the identical task/architecture, letting the survey directly rank which alignment technique
matters most for cross-embodiment co-training. Feeds the "human video co-trained directly with
robot demos in one shared policy" branch, distinct from every other method in this batch, which
either (a) retargets video into standalone demonstrations/rewards used alone or alongside RL
(dexmv_2021, dexvip_2022, hudor_2024, okami_2024, pgdm_2023) or (b) pretrains then fine-tunes
sequentially (videodex_2022, h_rdt_2025) rather than co-training jointly at every gradient step.
Block D: physical plausibility of the extracted hand-object interaction is not checked at all —
no interpenetration or grasp-force metric; the human stream does not even carry a
contact/grasp-state signal ("Aria only records hand pose"), so no plausibility check on hand-object
contact is possible from the human data by construction, only from the robot's own gripper-state
supervision.
