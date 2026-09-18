# videodex_2022 — VideoDex: Learning Dexterity from Internet Videos (Shaw, Bahl, Pathak, CoRL 2022)

sources: papers/md/videodex_2022.md [sha256 3e534fbd] ; no code

## One-line contribution
Human EpicKitchens video is retargeted (hand via a Robotic-Telekinesis-style energy-function
MLP, wrist via PnP+SLAM+heuristic-gravity-alignment) into open-loop robot trajectories that
pretrain a visual+physical-prior (R3M encoder + Neural Dynamic Policy) network per task, which is
then fine-tuned on 120-175 real teleoperated demonstrations, beating open-loop BC baselines on
7 real xArm6+LEAP-Hand tasks, especially on held-out test objects (Table 1).

## Setting
- hand(s): LEAP Hand, 16-DoF (used for main results); Allegro Hand also tried but rejected —
  "we found that the Allegro had higher inaccuracy in control and more hardware failures...
  LEAP Hand outperformed the Allegro Hand 7-12% on average" (Sec. 6, "Choice of Robotic Hand").
  arm: xArm6 [59]. Also tested with a 1-DOF/2-finger xArm gripper (separate action priors
  trained). single-handed throughout, real-robot experiments (not sim).
- simulator / physics: none used for training/eval — this is a real-robot paper end to end; no
  sim environment described.
- observation: single scene RGB image I encoded by a frozen R3M [6] ResNet-18 (E_phi, 512-D
  output) pretrained on human video via "visual-language alignment as well as a temporal
  consistency loss"; concatenated with starting hand/wrist pose, then processed by 3-layer MLP
  (hidden 512) feeding two separate Neural Dynamic Policy (NDP) heads for hand and wrist
  (Sec. 4.3, Appendix D). Not closed-loop: "our method of behavior cloning in the real world is
  currently open-loop" (Sec. 7).
- action space: open-loop trajectory output from the NDP dynamical-system formulation (DMP
  equation, Sec. 3.1) — an NDP predicts goal g and forcing-function shape parameters w per
  (hand, wrist) stream, which are integrated forward into a full trajectory of 200 (rescaled)
  waypoints; not per-step position/torque targets from a reactive policy.
- objects / data: 7 real tasks — pick, rotate, open, cover, uncover, place, push — each with
  120-175 real teleoperated robot demonstrations (Table 7: pick 125/8 objects, rotate 140/8,
  open 120/4, cover 124/12, uncover 145/12, place 175/10, push 136/14) and separately 350-2500
  retargeted EpicKitchens human video clips per task (Table 9: "350 (Cover/Uncover, Rotate,
  Push) - 2500 (Open, Pick, Place)"; main text states "500-3000 video clips... close to 3000...
  picking items").

## Method
- paradigm: two-stage supervised pretrain-then-finetune (NOT RL): (1) pretrain the NDP-based
  policy on human-video-retargeted "pseudo-robot" trajectories with an L1 trajectory-regression
  loss (Algorithm 1: `L_theta = ||tau_R^k - tau_hat_R^k||_1`); (2) fine-tune the same
  architecture on real teleoperated demonstrations with the same L1 loss (`L_theta =
  ||tau_n - tau_hat_n||_1`). This is behavior cloning on trajectories, not RL on an extracted
  reward, and not GAIL/adversarial IL.
- **human data source and size**: EpicKitchens [2] egocentric video ("GoPro Hero 7 Black... new
  data (refresher)"), filtered to clips matching each task category via EpicKitchens' existing
  action annotations (not a custom action detector: "we use the action annotations from the
  EpicKitchens dataset... but an action detection network... can be used"). Clips average
  "5-10 seconds each"; per-task counts 350-2500 clips (see above).
- **what is extracted from video**: per-frame human hand shape/pose (MANO beta, theta) via
  OpenPose hand crop -> FrankMocap [36] (low-pass filtered); wrist pose in the robot frame via
  a compound pipeline (Table 5, Appendix C): PnP (FrankMocap 3D keypoints + 2D detections,
  OpenCV solvePnPRANSAC, COLMAP-calibrated GoPro intrinsics) gives wrist-in-camera-frame M^Wrist_Ct;
  monocular SLAM (ORB-SLAM3) gives camera-motion-compensation M^Ct_C1; a heuristic
  gravity-alignment step (Detic object segmentation of floor/table/counter surfaces + AdaBins
  monocular depth -> surface normal) gives M^C1_World without relying on IMU/gyroscope data;
  and a final heuristic rescale/recenter T^World_Robot fits the trajectory to the robot
  workspace. No object pose, affordance map, or reward signal is extracted — only human
  hand+wrist kinematic trajectories.
- **human-to-robot mapping**: (i) hand: borrowed directly from Robotic Telekinesis [56] — an
  energy function E_pi minimizing distance between manually-defined key vectors v_i^h (human,
  from MANO/FrankMocap) and v_i^r (robot fingertip/palm vectors) with scale parameters c_i, is
  implicitly minimized by a distilled MLP H(.) trained on human poses (not re-derived by this
  paper; "we use H(.) to map hand poses to robot hand poses... a similar re-targeting network to
  Sivakumar et al. [56]", Sec. 4.2, Appendix C). (ii) wrist: the PnP+SLAM+gravity-heuristic+
  rescale chain above (a genuinely new contribution of this paper) maps human wrist motion to
  the xArm6 end-effector trajectory. Both streams' retargeted trajectories are combined into
  tau_R = (tau_R^hand, tau_R^wrist), used only to pretrain network weights theta_h — the
  retargeting is not run online at deployment.
- **RL or SL**: supervised trajectory regression (L1 loss) in both pretrain and fine-tune stages;
  an offline-RL ablation `CQL` [67] (using demonstrations as sparse reward) is tried and
  underperforms BC on the place task (Table 4: CQL train 0.40 / test 0.20 vs. VideoDex 0.90/0.70).
- reward or loss: none for the main method (behavior-cloning L1 as above); CQL ablation uses "the
  demonstrations as a sparse reward" but is not the main method and is described only at that
  level of detail (no reward function given).
- key trick(s): visual prior via R3M's human-video-pretrained encoder (ablated against VGG16 and
  MVP — both underperform, Table 4: VideoDex-VGG 0.20/0.20, VideoDex-MVP 0.40/0.20 vs. VideoDex
  0.90/0.70 on place); physical prior via NDP's smooth dynamical-system rollout (`BC-Open`
  without NDP and `VideoDex-Single` [one NDP instead of two-stream hand/wrist] both underperform
  the two-stream NDP); heuristic (SLAM/Detic/AdaBins-surface-normal) gravity alignment instead
  of IMU — ablation shows VideoDex's surface-normal method beats `VideoDex-Fixed` (alpha_p=[0,0])
  and `VideoDex-Random` (alpha_p in 15-45 deg) and roughly matches/exceeds `VideoDex-IMU`
  (Table 3: place 0.80 (Surface) vs 0.55 (Fixed)/0.45 (Random)/0.70 (IMU)).
- domain randomisation: workspace-scaling ablation trial ("randomize the workspace scaling...by
  10 percent" plus up to 10-degree rotation perturbation of the initial world frame) is described
  as an augmentation the authors tried but did NOT use in final results: "this augmentation...
  was not used as it led to similar results to not using data augmentation" (Appendix C,
  "Rescaling for Robot"). No sim domain randomization (real-robot only).
- contact / penetration handling: not addressed at all — no reward, no penetration metric; the
  method never touches interpenetration since it is open-loop trajectory-regression on real
  hardware with no simulated contact model.

## Evaluation
- metrics: binary 0-1 real-robot task success rate per trial, reported separately for "train"
  (seen objects/locations) and "test" (held-out objects/locations) conditions (Table 1, Table 8
  gives std. dev., e.g. VideoDex pick train 0.81+/-0.09 / test 0.75+/-0.11). Exact per-trial
  success criterion (e.g. object lifted, drawer opened how far) is not spelled out numerically
  beyond the task description in Sec. 5 ("goal is to pickup an object," etc.) — no threshold in
  meters/seconds given; "not stated" for a quantitative success criterion.
- headline numbers (Table 1, train/test success, 7 tasks): VideoDex beats or matches BC-NDP,
  BC-Open, BC-RNN on most tasks, most clearly on test (held-out) objects — e.g. Pick 0.83/0.77
  (VideoDex) vs. BC-NDP 0.64/0.38, BC-Open 0.50/0.44, BC-RNN 0.56/0.31; Place 0.89/0.80 vs.
  BC-NDP 0.70/0.35; Push all methods saturate at 1.00 train, VideoDex/BC-RNN tie at 1.00 test.
  1-DOF gripper (Table 2): VideoDex beats BC-Open on Place (0.69 vs 0.62), Open (0.82 vs 0.69),
  Pick (0.77 vs 0.71). Low-data regime (Table 4, place task): VideoDex-Const-5 (5
  demos/variant) reaches 0.60 test vs. full-data BC-Open baselines around 0.20-0.25 test; text
  states "even with 5 instances per variant, we still see a 30% success rate for unseen objects"
  (figure differs slightly from the 0.60 in Table 4 — flagged as an inconsistency in the source).
  Transfer ablation (Appendix B, Table 6): pretraining on Place and fine-tuning on Uncover (or
  vice versa), `VideoDex-Transfer` place 0.60 / uncover 0.87, vs. `VideoDex-Original` 0.70/0.90 —
  small degradation from cross-task pretraining. Noise ablation: adding Gaussian noise (std 0.01,
  0.05) to demonstration trajectories monotonically hurts performance (0.55/0.87 and 0.50/0.60
  respectively vs. 0.70/0.90 clean).
- baselines beaten: `BC-NDP` (same NDP architecture, no human-video pretraining), `BC-Open`
  (2-layer MLP instead of NDP, from [51]), `BC-RNN` ([51]), `CQL` (offline RL ablation, place
  task only, underperforms even BC). All are author-run in the same real-robot pipeline sharing
  the R3M visual backbone.
- real robot? Yes — this is a real-robot-only paper. Hardware: LEAP 16-DoF hand + xArm6, Intel
  RealSense D415 cameras, 4x NVIDIA RTX 2080Ti (Appendix F). Trial counts: per-task real
  teleoperated training demos 120-175 (Table 7); test-time trial counts per task/condition are
  not explicitly stated as an integer N in the extracted text (success rates in Table 1/8 are
  reported as fractions with std. dev., implying a fixed but unstated number of eval rollouts
  per train/test split) — flagged as "not stated" precisely.

## Limitations stated by the authors
- Uses curated EpicKitchens data "only... as a convenience"; general internet video would need
  an action detector (Sec. 7).
- "we rely on off-the-shelf human hand detection modules that very often have erroneous 6D pose
  detections, especially when the hand is interacting with objects" (Sec. 7).
- Retargeting "must be recomputed for each different set of robot parameters and embodiment"
  (Sec. 7) — not embodiment-agnostic.
- Policy is open-loop: "cannot react to changes in the environment... closed-loop behavior
  cloning is difficult to keep safe in the real world... closed-loop RL it is difficult to
  guarantee the safety of the system" (Sec. 7).
- Allegro Hand hardware was unreliable for data collection ("very unreliable and break many
  times... motors also quickly overheat," Appendix F) — a hardware, not algorithmic, limitation
  but explains the hand choice.

## Quotable claims (verbatim, with section)
- "By pretraining policies with these human hand trajectories, we learn action priors on how the
  robot should behave" (Sec. 4).
- "This wrist re-targeting approach uses only 2D images from human videos" (Sec. 4.2).
- "Networks initialized using action priors on human data without further training are closer to
  ground truth robot trajectories than networks only initialized using visual priors" (Fig. 6
  caption).
- "LEAP Hand outperformed the Allegro Hand 7-12% on average in all experiments" (Sec. 6).
- "our method of behavior cloning in the real world is currently open-loop, so it cannot react to
  changes in the environment" (Sec. 7).

## Notes for the survey
Feeds the "video -> retargeted open-loop trajectory -> BC pretraining, fine-tuned on real teleop
demos" branch — distinct from dexmv_2021/pgdm_2023 (sim RL augmented by translated demos) and
from dexvip_2022/hudor_2024 (video as reward signal). VideoDex is the only one of this batch with
purely real-robot results and trial-count-reported success rates, though exact real-eval trial
counts (N per cell) are not stated as integers, only success fractions with std. dev. (Table 8).
The embodiment-gap ablation that most directly isolates the human-to-robot mapping's cost is
Table 3 (initial-pitch/gravity-alignment method), which is about the wrist heuristic, not the
hand energy-function retargeting — the hand-retargeting network itself (borrowed from [56]) is
never ablated in isolation here, so its specific cost cannot be quoted from this paper alone.
Block D: physical plausibility of the extracted hand-object interaction is not checked at all —
no penetration metric, no force-closure or grasp-quality check anywhere in the pipeline; the
retargeted trajectories are validated only by downstream task success after fine-tuning, and the
authors explicitly note retargeted trajectories "are not used directly on the robot so they do
not need complete accuracy" (Appendix C), i.e. plausibility is implicitly deferred to the
fine-tuning stage rather than checked at extraction time.
