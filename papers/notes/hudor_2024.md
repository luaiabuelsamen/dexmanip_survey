# hudor_2024 — Bridging the Human to Robot Dexterity Gap through Object-Oriented Rewards (Guzey, Dai, Evans, Chintala, Pinto; ICRA 2025)

sources: papers/md/hudor_2024.md [sha256 8a7385b8] ; no code

## One-line contribution
HUDOR retargets a single in-scene human fingertip trajectory (VR-headset hand tracking, ArUco
calibration) onto an Allegro-on-Kinova robot via IK for open-loop replay, then trains a DrQv2
residual policy online using an object-centric, point-tracked trajectory-matching reward (not an
image-matching reward) — beating offline BC baselines (incl. a single-demo BC and a point-cloud
BC) and alternative reward functions (image/point optimal-transport) on 4 real dexterous tasks,
each evaluated over 10 rollouts (Table I, Table II).

## Setting
- hand(s): Allegro Hand, 16-DoF, four-fingered [10]; arm: Kinova JACO 6-DoF (Sec. III-A). Single
  hand, real robot only (no sim).
- simulator / physics: none — real-robot online RL throughout.
- observation: for the residual policy, inputs are (a) human-retargeted fingertip positions in
  robot frame a_r^t (12-D: 4 fingertips x 3D), (b) change in current robot fingertip positions
  Delta s^t = s^t - s^(t-1), (c) centroid of tracked object points P_hat_R^t, (d) object motion
  T_R^t (Sec. III-B). Two RealSense RGB-D cameras for calibration/vision, Meta Quest 3 VR headset
  for hand-pose capture (Sec. III-A).
- action space: residual action a^t_+ = pi_r(.) added to the human-retargeted fingertip target,
  sent through a custom gradient-descent IK module (Jacobian-based, per-joint learning rates:
  hand LR 50x the arm LR) to produce joint position commands (Sec. III-A.d, III-B).
- objects / data: 4 real dexterous tasks — Bread Picking, Card Sliding, Music Box Opening, Paper
  Sliding (Sec. IV-A) — each learned from a SINGLE human demonstration video/trajectory. Data
  collected at the VR/camera native rates then "subsampled to 5 Hz" (Sec. III-A.c).

## Method
- paradigm: NOT imitation learning on retargeted actions, and NOT RL on a hand-crafted reward —
  a hybrid: open-loop IK replay of the single retargeted human trajectory PLUS an online residual
  RL policy (DrQv2 [49]) trained on a reward extracted from video via object point tracking. The
  paper explicitly frames this as "teleoperation-free online dexterous policies" (Sec. III title).
- **human data source and size**: one "in-scene" human video per task — "demonstrator is in the
  same scene as the robot" (Fig. 2 caption) — captured with a Meta Quest 3 VR headset for
  fingertip pose plus an RGB camera; NOT internet/YouTube video and NOT a large corpus (contrast
  videodex_2022/h_rdt_2025's thousands of clips) — a single trajectory per task, most similar in
  scale to okami_2024's single-video-per-task setting, though HUDOR's "video" is VR-tracked
  fingertip poses rather than reconstructed full-body/hand mesh from RGB alone.
- **what is extracted from video/demo**: (i) 4 human fingertip 3D positions per frame from the VR
  headset's built-in hand-pose detector, ArUco-calibrated into the robot's base frame via
  `a_r^{t,i} = H_RW^{-1} * H_OW * a_o^{t,i}` (Sec. III-A.a) — this is the ONLY hand-pose signal
  used for policy execution (no full hand mesh/MANO, no joint angles beyond fingertip Cartesian
  position); (ii) for the reward, object motion is extracted by langSAM (text-prompted
  GroundingDINO + SAM) segmenting the object in frame 1 into N tracked points, then CoTracker
  tracks these points through the video to give a point trajectory tau_p = [P^1,...,P^T]; object
  motion T^t is defined as the mean point-centroid translation delta_trans^t (and, for the
  rotating Music Box task, an added mean rotation term delta_rot^t) from frame 1 (Sec. III-B.a).
  This same object-point-tracking procedure is run on BOTH the human video and the robot rollout,
  and only the resulting OBJECT motion trajectories are compared for reward — no reward or
  supervision signal comes from comparing hand appearance/pose between human and robot.
- **human-to-robot mapping**: direct Cartesian-space fingertip retargeting via rigid-body
  calibration + custom IK, not a kinematic-chain optimization (contrast dexmv_2021's TSV
  optimization or dexvip_2022's parent-relative-frame method): two ArUco markers (one on the
  table, one on the Allegro hand) fix a world frame; the VR-frame-to-world transform H_OW is
  computed by detecting the table marker with the headset's own cameras, and the robot-to-world
  transform H_RW is computed by detecting both markers with the RGB camera via standard
  calibration [40]; human fingertip positions are then directly treated as target Cartesian
  positions for the corresponding robot fingertips (an implicit fingertip-correspondence
  assumption, not solved by any optimization over hand geometry) and converted to joint commands
  by the custom Jacobian-based IK. Explicitly acknowledged as imperfect: "Due to the
  morphological differences between the human and robot, as well as errors in VR hand pose
  estimation, naively replaying the retargeted fingertip trajectories on the robot mostly does
  not successfully solve the task, even when the object is in the same location" (Sec. III-B) —
  this sentence IS this paper's stated cost of the embodiment/estimation gap (see Notes below).
- **RL or SL**: RL (DrQv2, an off-policy actor-critic for pixel-based control) trains only a
  RESIDUAL added on top of the fixed IK-replayed base trajectory, exploring only a hand-picked
  subset of action dimensions per task (e.g. "we focus only on the X and Y axes of the thumb for
  the Card Sliding task," Sec. III-B.b) with scheduled Ornstein-Uhlenbeck exploration noise.
  Trained online, real-robot ("up to one hour of online interactions," Sec. IV-A). Offline BC
  baselines (VQ-BeT-based) are compared against but are not the proposed method.
- reward or loss (Sec. III-B.a, Eq. 5 described in text): `R = -RMSE(T_R^t, T_H^t)`, the negative
  root-mean-squared-error between robot and human object-motion trajectories T^t = delta_trans^t
  (translation only; translation+rotation `[delta_trans^t, delta_rot^t]` for Music Box Opening,
  Sec. IV-A.c). For Music Box Opening specifically, "we observed that a sparse reward was better
  for this task, so we only used the last 5 frames of the trajectory for reward calculation for
  HUDOR and all of our baselines" (Sec. IV-A.c) — a per-task deviation from the dense
  every-timestep reward described in Sec. III-B.a.
- key trick(s): object-CENTRIC (not image- or point-identity-based) reward — ablated directly
  against Image OT (ResNet18 embeddings + optimal transport, as in FISH [30]) and Point OT
  (optimal transport directly on tracked point sets) in Table II, both of which underperform
  HUDOR's trajectory-matching reward, especially when "the camera needs to be closer to the
  object" (Music Box Opening: HUDOR 6/10 vs. Image OT 1/10, Point OT 2/10) because "the visual
  differences between the hand and the robot significantly hinder training" for image-based
  rewards, and because per-index point correspondence is unstable across the two trajectories for
  Point OT (Sec. IV-C); action-subspace restriction for faster online exploration; scheduled OU
  noise for smooth real-hardware exploration.
- domain randomisation: none described (single-video, real-robot online learning; no simulated
  training). Spatial generalization (Sec. IV-E) is achieved post-hoc by a fixed Cartesian offset
  computed from re-detected object position, not by randomized training.
- contact / penetration handling: not addressed. No reward or metric measures hand-object
  interpenetration; "contact"/grasp quality is never separately measured — success is judged
  purely by task outcome (object displacement/held/opened), and reward is purely kinematic
  (point-trajectory matching), with no physical-plausibility or force term.

## Evaluation
- metrics: per-task binary success out of 10 rollouts at varied initial object locations (Table
  I/II caption: "we evaluate the methods by running rollouts on 10 varying initial object
  configurations for every task," Sec. IV-A), except Paper Sliding, measured as "distance the
  paper moves to the right, expressed in centimeters" (Sec. IV-A.d) with mean+-std over
  presumably the same 10 rollouts. Spatial-generalization (Table III) uses per-behavior success
  counts out of 20 (Bread Picking) or 18 (Music Box Opening) evaluations, with SEQUENTIAL
  behavior stages (e.g. "Reached the bread" (20/20) -> "Picked the bread up" (17/20) -> "Held it
  firmly" (15/20)).
- headline numbers (Table I, offline-baseline comparison, out of 10 unless noted): HUDOR — Bread
  8, Card 7, Music Box 6, Paper 17.3+-1.5 cm; vs. best offline baseline (Point Cloud BC, DexCap
  [17]-style PointNet-augmented VQ-BeT) — Bread 3, Card 0, Music 0, Paper 12+-1.3 cm; BC-1-Demo
  (VQ-BeT, single demo) scores 0/10 on Bread/Card/Music and 3.5+-1.1 cm on Paper. Reward-function
  ablation (Table II): HUDOR vs. Image OT vs. Point OT — Bread 8 vs. 6 vs. 6; Music Box 6 vs. 1
  vs. 2; Paper 17.25+-1.47 vs. 16.1+-1.37 vs. 16.5+-1.23 cm (Image/Point OT competitive only when
  "the object occupies a large area in the image," per Sec. IV-C). Generalization to new objects
  (Fig. 8, no retraining): Bread Picking 5/10, 4/10 on some novel objects (e.g. Dobby sculpture)
  down to 0/10 on others (e.g. slippery Red Peg); Card Sliding similarly ranges (values embedded
  in figure). Spatial generalization (Table III): Bread Picking reaches the bread 20/20, picks it
  up 17/20, holds firmly 15/20; Music Box Opening reaches box 18/18, reaches lid 14/18, opens lid
  10/18, stabilizes lid 7/18 (degrading through the more dexterous later stages).
- baselines beaten: BC-1-Demo (VQ-BeT [3], single demonstration), BC (VQ-BeT, 30 demonstrations),
  Point Cloud BC (VQ-BeT + PointNet [50] point-cloud encoder, DexCap-style [17]) — all
  author-implemented offline behavior-cloning baselines given the same auxiliary inputs (tracked
  point centroid, object motion, fingertip positions) as HUDOR's residual policy; Image OT [30]
  (FISH-style ResNet18 + optimal transport reward) and Point OT (OT directly on tracked points) —
  both author-implemented alternative online reward functions using the same DrQv2 residual RL
  backbone as HUDOR, isolating the reward-function choice specifically.
- real robot? Yes, entirely real-robot (Kinova JACO + Allegro hand). Trial counts: 10 rollouts
  per task for the main comparison and reward ablation (Tables I-II); 10 rollouts per novel
  object for generalization (Fig. 8); 20 (Bread) / 18 (Music Box) staged evaluations for spatial
  generalization (Table III). Online training itself runs "up to one hour" per task on hardware.

## Limitations stated by the authors
- "our framework only works with in-scene human videos. We believe integrating in-the-wild data
  collection would significantly enhance its generalization potential" (Sec. V).
- "the exploration mechanism requires prior knowledge of which subset of action dimensions is
  suitable for exploration" — the action-subspace restriction is manually chosen per task, not
  learned (Sec. V).
- "there is no retry mechanism during an episode; when the robot makes a mistake, it can only
  retry in the next episode. This makes training for long-term tasks challenging" (Sec. V).
- Naive fingertip-trajectory replay (before residual RL) "mostly does not successfully solve the
  task, even when the object is in the same location," due to "morphological differences between
  the human and robot, as well as errors in VR hand pose estimation" (Sec. III-B) — this is the
  paper's own statement of the embodiment-gap cost, though not quantified as a bare
  success-rate number without the residual policy.
- Spatial generalization fails for the more dexterous Music Box Opening task specifically because
  of "residual policy predictions and noise in the depth received from the camera" at the edges
  of the evaluated area (Sec. IV-E).
- Point-tracking-based object generalization "is insufficient to overcome substantial differences
  in shape and texture" between training and novel objects (Sec. IV-D).

## Quotable claims (verbatim, with section)
- "Due to the morphological differences between the human and robot, as well as errors in VR
  hand pose estimation, naively replaying the retargeted fingertip trajectories on the robot
  mostly does not successfully solve the task, even when the object is in the same location"
  (Sec. III-B).
- "These differences cause matching to give inconsistent rewards emphasizing the importance of
  matching trajectories rather than points or images" (Sec. IV-C).
- "HUDOR combines an open-loop base policy with a learned residual policy, providing more robust
  behavior against OOD cases" (Fig. 7 caption).
- "point-tracking can enable some degree of policy generalization, [but] it is insufficient to
  overcome substantial differences in shape and texture" (Sec. IV-D).

## Notes for the survey
HUDOR is the clearest "video -> object-motion reward, not hand-pose reward" method in this batch,
directly contrasting with dexvip_2022 (hand-pose-matching reward) and dexmv_2021 (retargeted
hand-trajectory imitation): the human hand/fingertip signal here is used ONLY to seed an open-loop
initial trajectory via direct Cartesian retargeting (no kinematic-chain optimization), while all
of the learning signal (the RL reward) comes from OBJECT point-tracking, explicitly engineered to
sidestep visual/morphological hand differences ("get around this domain gap, we propose a novel
algorithm for object-centric trajectory-matching rewards," Sec. III-B). The clean qualitative
embodiment-gap statement ("naively replaying... mostly does not successfully solve the task") is
the paper's own framing but is not paired with a bare open-loop-only success-rate table entry —
Table I's baselines are all offline-BC variants, not "IK-replay-with-zero-residual," so the exact
numeric cost of skipping the residual RL stage cannot be quoted from the tables given. Real-robot
trial counts (10/task) are comparable in rigor to videodex_2022/cyberdemo_2024/okami_2024. Block
D: physical plausibility of the extracted hand-object interaction is not checked at all — no
interpenetration or grasp-force metric anywhere; "contact" and grasp quality are inferred only
from downstream task success (object held, lid opened) and from the reward's object-motion match,
never from a geometric or force-based plausibility check on the retargeted hand pose itself.
