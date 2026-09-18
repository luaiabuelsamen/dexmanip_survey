# okami_2024 — OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation (Li, Zhang, Salhotra, Devaraj, Zeng, Sadeghpour, Zhu, Martin-Martin, Kim, Zhu; CoRL 2024)

sources: papers/md/okami_2024.md [sha256 5f5cb32c] ; code/md/okami_2024.md [commit de4edba5]

## One-line contribution
From a single RGB-D human video, OKAMI reconstructs a SMPL-H body+hand trajectory, uses GPT-4V
plus segmentation/tracking to build an object-centric "reference plan" of subgoals, then
retargets arm motion (task-space IK to shoulder/elbow/wrist targets) and hand motion (joint-angle
mapping via dex-retargeting) onto a Fourier GR1 humanoid, warping the retargeted trajectory to
new object locations at test time — beating an object-only baseline (ORION) by 34-84 points
across 4 tasks/settings (Sec. 4.2).

## Setting
- hand(s): two 6-DoF Inspire dexterous hands (Sec. 4.1, "Hardware Setup"). arm: Fourier GR1
  humanoid's arms (upper-body only; "current focus of OKAMI is on the upper body motion
  retargeting... A promising future direction is to include lower body retargeting," Sec. 5).
  bimanual capability exists (Bagging task is explicitly "dexterous, bimanual manipulation").
- simulator / physics: real-robot primary; RoboSuite [60] used only for 2 of 6 tasks
  (Sprinkle-salt, Close-the-drawer) "for easy reproducibility" (Sec. 4.1, Appendix B.4).
  Joint position controller at 400 Hz, commands computed at 40 Hz and interpolated to 400 Hz "to
  avoid jerky movements" (Sec. 4.1).
- observation: RGB-D from a D435i Intel RealSense (video recording and test-time observation,
  Sec. 4.1); test-time object localization uses 3D point clouds from segmentation + depth.
- action space: full-body (upper-body) joint position commands from inverse kinematics (IK
  solved via the open-source library Pink [64]) at 400 Hz; not vision-conditioned closed-loop
  per-step control except in the separate ACT-based visuomotor-policy experiment (Sec. 4.3).
- objects / data: one human demonstration video per task (single-video imitation), 6 real tasks
  (Plush-toy-in-basket, Sprinkle-salt, Close-the-drawer, Close-the-laptop,
  Place-snacks-on-plate, Bagging) plus 2 simulated versions (Sprinkle-salt, Close-the-drawer).
  No large-scale video dataset — "open-world imitation from observation" from ONE video per task
  (Sec. 3, Problem Formulation), demonstrated by up to 3 different demonstrators for a robustness
  check (Sec. 4.2, Q3; Appendix B.3).

## Method
- paradigm: not RL, not standard behavior cloning on a large demo set — a per-task, single-video
  "reference-plan generation + object-aware retargeting" pipeline that directly produces a
  full-body joint trajectory for execution (open-loop per rollout, replanned/warped at test time
  based on new object locations). A separate downstream experiment (Sec. 4.3) trains a
  closed-loop visuomotor policy via behavior cloning (ACT [61]) on OKAMI-generated successful
  rollouts, filtering out failures — this is the only place standard supervised imitation
  learning is used.
- **human data source and size**: a single RGB-D video per task, recorded by the authors
  (up to 3 different human demonstrators tested for Place-snacks-on-plate/Close-the-laptop,
  Appendix B.3/Fig. 6). Two explicit assumptions: "all the image frames in V capture the human
  bodies, and the camera view of shooting V is static throughout the recording" (Sec. 3). Not a
  large corpus like EpicKitchens/HowTo100M — this is single-shot imitation, the opposite end of
  the data-scale spectrum from videodex_2022/h_rdt_2025.
- **what is extracted from video**: (i) task-relevant object identities via GPT-4V prompted with
  sampled RGB frames (verbatim prompts in Appendix A.2), then Grounded-SAM segmentation + Cutie
  video object tracking to localize/track them; (ii) full human body+hand motion as a SMPL-H
  trajectory, from an extended SLAHMR [55] pipeline: 4D Humans gives an initial body pose,
  ViTPose detects hands, HaMeR estimates 3D hand pose per hand (bodies from 4D-Humans have "flat"
  hands), then a joint optimization refines body location/pose/hand-pose jointly using HaMeR's 2D
  hand-keypoint reprojections as a constraint (Appendix A.1); (iii) a temporally-segmented
  "reference plan" l_0,...,l_N, each step containing point clouds of a target object and a
  reference object (identified by keypoint-velocity-based changepoint detection via CoTracker
  plus GPT-4V-predicted semantic relations for non-contact cases, e.g. identifying the receiving
  cup in a pour) and the corresponding SMPL-H trajectory segment (Sec. 3.1, Appendix A.4). No
  reward signal or latent embedding is extracted — pose + object-segmentation only.
- **human-to-robot mapping**: a factorized two-part retargeting (Sec. 3.2, Appendix A.3), run
  ONCE per demonstration video to build the reference plan, then WARPED at test time to new
  object poses (not re-run from raw video at test time): (1) **Body/arm**: extract SMPL-H
  shoulder/elbow/wrist poses, solve humanoid arm IK (library: Pink) to match shoulder/elbow
  orientation and wrist pose, with fixed weights "0.04, 0.04, 0.08, and 1.0" for
  shoulder-orientation/elbow-orientation/wrist-orientation/wrist-position respectively — i.e.
  wrist POSITION dominates the IK objective. This retargeting is "affine," so it "naturally
  scales and adjusts motions from demonstrators with varied demographic characteristics."
  (2) **Hand**: SMPL-H hand-mesh joint angles are computed, applied to a canonical SMPL-H model
  pre-scaled to match the robot hand hardware, then the resulting 3D hand keypoints are fed to
  "dex-retargeting," an off-the-shelf optimization package (credited to Yuzhe Qin in the
  Acknowledgments — same lineage as dexmv_2021/dexvip_2022-style retargeting tools) to compute
  robot finger joint angles directly. (3) **Object-aware warping**: after localizing objects at
  test time, the retargeted arm trajectory is affinely warped (Appendix A.5 gives the closed-form
  SE(3) warp: `tau_hat_robot(t) = (tau_robot(t) - p_start)/(p_end - p_start) * (T_end*p_end -
  T_start*p_start) + T_start*p_start`) so start/end points match the new target/reference object
  locations, while finger joint angles are retargeted independently of arm warping ("OKAMI first
  adapts the arm motions... Then OKAMI only needs to retarget fingers in the joint configuration
  to mimic how the demonstrator interacts with objects").
- **RL or SL**: neither, for the core method — it is deterministic retargeting + trajectory
  warping executed open-loop, evaluated directly for task success (an R(s) sparse binary
  completion reward is defined in the MDP formulation, Sec. 3, but is not optimized — it is only
  the success criterion). The Sec. 4.3 visuomotor-policy extension is supervised BC (ACT) on
  OKAMI-rollout-generated demonstrations, discarding failed rollouts.
- reward or loss: MDP formalized with "a sparse reward function that returns 1 when a task is
  complete" (Sec. 3), used only as an evaluation criterion, not as a training signal — OKAMI
  itself has no learned reward or policy-gradient loss. Appendix B.1 gives per-task success
  conditions verbatim (e.g. Plush-toy-in-basket: "more than 50% of the toy inside the container";
  Close-the-laptop: "the display is lowered towards the base until the two parts meet at the
  hinge"). ACT visuomotor policy (Sec. 4.3) uses ACT's standard action-chunking BC loss
  (not re-derived in this paper).
- key trick(s): GPT-4V for open-vocabulary task-relevant-object identification without
  task-specific annotation (prompts given verbatim, Appendix A.2); factorized arm/hand
  retargeting so object-location adaptation (arm warping) is decoupled from fine-grained finger
  pose (retargeted independently); using OKAMI's own successful rollouts as a scalable BC data
  source ("reduces the human cost for policy training compared to that required by
  teleoperation," Sec. 5).
- domain randomisation: none in the traditional sim-training sense; object locations are
  "randomly initialized within the intersection of the robot camera's view and the humanoid
  arms' reachable range" at real-robot test time (Sec. 4.1, "Evaluation Protocol") — a test-time
  initial-condition randomization, not training-time domain randomization.
- contact / penetration handling: not addressed as a quantitative check. Object CONTACT is used
  only as a semantic/planning signal — "we compute the relative spatial locations and distances
  between the point clouds of objects. If the distance... falls below a predefined threshold, we
  consider them to be in contact" (Appendix A.4) — this determines subgoal/reference-object
  identification during plan generation, not a hand-object interpenetration or plausibility
  metric. No penetration term appears in code/md's retargeting (`retargeter_wrapper.py`) or
  hand-utility (`hand_utils.py`) function signatures (bodies not present in code/md).

## Evaluation
- metrics: binary real-robot task success over "12 trials for each task," with object locations
  randomized within reachable range (Sec. 4.1, "Evaluation Protocol"); failure modes further
  broken into "Missed grasping" vs. "Failed Completion" (Fig. 4a). Per-task success conditions
  quoted verbatim in Appendix B.1 (see above).
- headline numbers (Fig. 4a, 12 trials/task, main real-robot results): success rates range from
  58.3% to 83.3% across the 6 tasks (exact per-task figure-only values: Sprinkle-salt, Plush-toy,
  Close-laptop, Close-drawer, Place-snacks, Bagging all fall in the 58.3-83.3% band per the
  described bars). OKAMI vs. ORION [4] baseline (Sec. 4.2, Q2): Place-snacks-on-plate 75.0%
  (OKAMI) vs. 0.0% (ORION); Close-the-laptop 83.3% vs. 41.2%; simulated Sprinkle-salt 82.0% vs.
  0.0%; simulated Close-the-drawer 84.0% vs. 10.0%. Cross-demonstrator robustness (Sec. 4.2, Q3;
  Fig. 4b): "no statistical significance in performance change" for Close-the-laptop across 3
  demonstrators; for Place-snacks-on-plate, "the worst policy performance is 16.7% worse than the
  best," attributed to demonstrator 2's faster motion causing "noisy estimation... when doing
  human model reconstruction." Visuomotor-policy scaling (Sec. 4.3, Fig. 5): ACT policies trained
  on OKAMI-generated rollouts improve from 50 to 100 trajectories for both Sprinkle-salt and
  Bagging (exact deltas embedded in figure, not quoted as text numbers).
- baselines beaten: ORION [4] (adapted from parallel-jaw-gripper to humanoid by estimating a
  palm-only trajectory from SMPL-H and warping it, ignoring body-pose/embodiment information) —
  author-adapted with "minimal modifications" (Sec. 4.1, "Baselines"; Appendix B.2). This is the
  paper's explicit embodiment-gap ablation (see Notes below).
- real robot? Yes. Fourier GR1 humanoid, two 6-DoF Inspire hands, D435i RealSense. 12 trials per
  task for the main results (Fig. 4a), same 12-trial protocol implied for the ORION comparison
  and demonstrator-robustness experiments (not independently re-stated as a different N).

## Limitations stated by the authors
- "current focus of OKAMI is on the upper body motion retargeting... particularly for
  manipulation tasks within tabletop workspaces" — no locomotion/lower-body retargeting yet, and
  a "whole-body motion controller" would be needed for loco-manipulation (Sec. 5).
- Requires RGB-D, "which limits us from using in-the-wild Internet videos recorded in RGB"
  (Sec. 5) — a direct contrast with videodex_2022/hudor_2024's RGB-only pipelines.
  "Extending OKAMI to use web videos will be another promising direction" (Sec. 5).
- "the current implementation of retargeting has limited robustness against large variations in
  object shapes" (Sec. 5).
- Faster demonstrator motion "creates a noisy estimation of motion when doing human model
  reconstruction," degrading downstream retargeting/task success (Sec. 4.2, Q3).
- Two hard assumptions baked into the problem formulation: static camera and full human-body
  visibility throughout the video (Sec. 3).

## Quotable claims (verbatim, with section)
- "These behaviors originate from the fact that ORION ignores the embodiment information, thus
  falling short in performance compared to OKAMI. The superior performance of OKAMI suggests the
  importance of retargeting the body motion of the human demonstrators onto the humanoid when
  imitating from human videos" (Sec. 4.2).
- "OKAMI enables efficient collection of trajectory data based on a single human video
  demonstration. OKAMI-based data collection significantly reduces the human cost for policy
  training compared to that required by teleoperation" (Sec. 5).
- "all the image frames in V capture the human bodies, and the camera view of shooting V is
  static throughout the recording" (Sec. 3).
- "Most failures of ORION policies are due to failing to approach objects with reliable grasping
  poses... and failing to rotate the wrist fully to achieve behaviors such as pouring" (Sec. 4.2).

## Notes for the survey
OKAMI is this batch's clearest example of a paper directly measuring "the embodiment gap's cost"
via its own ablation: ORION (object-pose-only, no human body/hand retargeting) vs. OKAMI (full
SMPL-H body+hand retargeting) on the SAME reference-plan/warping pipeline, isolating exactly the
contribution of retargeting human motion. The cost of skipping embodiment retargeting is large
and consistent: -75.0, -42.1, -82.0, -74.0 percentage points across the 4 tested
task/setting pairs (Place-snacks, Close-laptop, sim-Sprinkle-salt, sim-Close-drawer) — the
biggest, cleanest embodiment-gap number in this batch of 11 papers. Also the only paper here
using single-shot (one video per task) imitation rather than a video corpus, and the only one
built on a full-body SMPL-H reconstruction (4D-Humans + HaMeR + SLAHMR extension) rather than
MANO-only hand pose. Feeds the "video -> retargeted trajectory -> direct execution, optionally
distilled into a BC policy" branch, sharing dex-retargeting tooling lineage with
dexmv_2021/dexvip_2022 (via the same author, Yuzhe Qin, credited in Acknowledgments) but applying
it to a humanoid rather than a tabletop hand-only setup. Block D: physical plausibility of the
retargeted hand-object interaction is not quantitatively checked — "contact" is used only as a
semantic/planning signal (a distance threshold for subgoal/reference-object identification), not
as an interpenetration or force-closure check; the only physical-plausibility claim is
qualitative ("retargeted motions are physically feasible for the robot and... execution appears
natural and effective," Appendix A.3) and validated indirectly via real-robot task success, not
via any measured penetration or contact-force statistic.
