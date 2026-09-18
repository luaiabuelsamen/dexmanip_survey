# egozero_2025 — EgoZero: Robot Learning from Smart Glasses (Liu, Hansen, Shafiullah, Pinto, NYU; CoRL 2025)

sources: papers/md/egozero_2025.md [sha256 876d46f8] ; code/md/egozero_2025.md [commit 51dc1c62]

## SCOPE FLAG
EgoZero deploys on a Franka Panda **parallel-jaw gripper**, not a multi-fingered dexterous hand —
"we use a Franka Panda gripper robot" (Sec. 3.2, "Policy inference"); the action space's "gripper
closure" is a single scalar binarized at inference (Sec. 3.1). The authors themselves flag this
gap: "We hope that EGOZERO will serve as a framework on which future research can extend to fully
dexterous and bimanual setups" (Sec. 5). Recorded here for completeness since it was named in the
batch; its "hand pose" extraction (HaMeR 21-keypoint hand model) is richer than its 2-DoF
end-effector actually uses.

## One-line contribution
EgoZero trains a closed-loop policy with ZERO robot data, purely from ~100 Project-Aria
egocentric human demonstrations per task, by mapping both human and robot into a shared
"morphology-agnostic" 3D-point state-action space: object state as SLAM-camera-trajectory
triangulated 3D keypoints (not depth-sensor or stereo), and action as thumb/index 3D coordinates
+ a thresholded grasp signal derived by fusing HaMeR hand-mesh estimates with Aria's own 6-DoF
palm pose — achieving true zero-shot (no in-domain robot data, no fine-tuning) transfer to a real
Franka gripper across 7 tasks (Table 1), where image-based and open-loop-affordance baselines
both fail entirely or partially.

## Setting
- hand(s)/end-effector: Franka Panda parallel-jaw gripper (see SCOPE FLAG). No arm-only
  observation beyond the gripper; single-armed, no bimanual tasks.
- simulator / physics: none — human data collection and robot evaluation are both entirely real
  world; no simulation anywhere in the pipeline.
- observation (state space S~): "the concatenated space of egocentric object point sets and
  robot end-effector actions" (Sec. 3.1) — i.e. a set of tracked/triangulated 3D object keypoints,
  NOT raw RGB, NOT depth maps. At inference, an iPhone (not Aria) provides the egocentric view
  because it can unproject points into 3D with accurate depth directly, unlike Aria (Sec. 3.2).
- action space (A~): "the concatenated space of 3D end-effector egocentric coordinates and
  gripper closures" (Sec. 3.1) — specifically the 3D thumb and index fingertip coordinates plus a
  binary grasp flag (thresholded thumb-index Euclidean distance), NOT full per-finger joint
  angles; converted to robot-executable actions via the Franka gripper controller's own inverse
  kinematics mapping A -> A~ at inference.
- objects / data: 7 real tasks (open oven door, put bread on plate, sweep board with broom, erase
  board, sort fruit into bowl, fold towel, insert book in shelf); "we collect 100 demonstrations
  per task, varying the environment and object positions... We collect zero data in our
  inference-time environment" (Sec. 4.1) — i.e. training data are entirely out-of-domain relative
  to the eval workspace.

## Method
- paradigm: pure supervised behavior cloning (closed-loop Transformer policy) on human-only
  demonstrations projected into a morphology-agnostic 3D-point representation — NOT RL, NOT
  reward-from-video, and NOT any robot teleoperation data at any stage ("training a robot policy
  using only human data," Sec. 1/Abstract-level framing).
- **human data source and size**: self-collected in-the-wild egocentric video via Project Aria
  smart glasses (fisheye RGB + 2 SLAM cameras + onboard Machine Perception Services for 6-DoF
  hand pose and camera pose), 100 demonstrations per task x 7 tasks = 700 total, collected "in
  2-3 different environments, on tabletops of different heights, with various background
  distractors, with multiple unique demonstrators... moving around, standing still, and sitting
  down" (Sec. 4.4, "Human-scale generalization") — deliberately maximizing demonstrator/scene
  diversity since none of it will match the eval environment.
- **what is extracted from video**: (i) per-frame 6-DoF palm pose H_t from Aria MPS directly
  (camera-frame homogeneous transform); (ii) a 21-keypoint egocentric hand mesh h_t via HaMeR
  [54], used only for its RELATIVE (hand-frame) finger geometry since "HaMeR's end-effector
  predictions in camera frame are inaccurate" but its intra-hand predictions are reliable — the
  two are fused by constructing a HaMeR-derived palm frame H_hat_t (translation = centroid of
  ThumbCMC/IndexMCP/MiddleMCP; rotation = basis from Wrist-MiddleMCP and IndexMCP-MiddleMCP
  vectors), then correcting it with Aria's own H_t and projecting into the first frame (Eq. 1,
  Sec. 3.1); (iii) object state via 2D-point tracking (CoTracker3) of expert-labeled keypoints
  (localized per-frame via Grounding DINO + DIFT correspondence) across the demonstration
  trajectory, triangulated into static 3D points using Aria's SLAM camera extrinsics — NOT depth
  sensing or stereo (explicitly ruled out: Aria's 3 cameras have "little field-of-view overlap,
  making stereo triangulation unreliable," and monocular metric depth models were tested and
  found to have ">5cm error," Sec. 3.1, Sec. 4.3). Triangulation solves for the 3D point q* in
  the first frame minimizing reprojection error over inlier frames (RANSAC + epipolar
  consistency), with a Huber loss and an added "soft depth penalty" to counteract CoTracker3's
  "stickiness" (points appearing further away than true due to lag), converging to "a mean inlier
  reprojection error of 2-4 pixels per demonstration" (Sec. 3.1). No reward signal or affordance
  map is separately extracted.
- **human-to-robot mapping**: NOT a kinematic hand-to-hand retargeting (no MANO-to-robot-joint
  IK) — because both human and robot are represented in the SAME morphology-agnostic 3D-point
  space (object keypoints + end-effector 3D coordinates + grasp scalar), there is no explicit
  cross-embodiment pose transfer step at all. The "mapping" is instead a representational
  choice: reducing both the human hand and the robot gripper to "3D end-effector egocentric
  coordinates and gripper closures" so the same policy input/output space applies to both without
  ever converting one kinematic chain into another. At inference, only a one-time iPhone-to-robot
  extrinsic calibration (via an ArUco tag, covered during policy execution) is needed to place
  predicted 3D points into the robot frame (Sec. 3.2, "Policy inference"; Sec. 4.1).
- **RL or SL**: pure SL (behavior cloning). Loss: negative log-likelihood of a Gaussian policy
  output with fixed sigma=0.1, `L = -log N(a~; pi_theta(s~), sigma)` (Sec. 3.2, quoted structure);
  augmented with a history buffer and temporally-aggregated action chunking (as in prior point-
  based policy work [27, 62]).
- reward or loss: none beyond the above BC NLL; no reward function anywhere (no RL used).
- key trick(s), directly ablated (Table 1, Sec. 4.3): (1) **3D data augmentation** — random
  rotations R ~ U(-pi/6, +pi/6) and translations t ~ U(-0.5, +0.5) m applied to states/actions
  during training; removing this ("EGOZERO - 3D augmentations") collapses success to 0/15 on
  every task, because "the policy learns a smaller and sparser 3D-to-3D mapping volume" and
  becomes OOD on any new egocentric view. (2) **Triangulated (not monocular-estimated) depth**
  for object localization — removing this ("EGOZERO - triangulated depth", i.e. substituting a
  metric monocular depth model) also collapses success to 0/15 on every task, since "the best
  metric depth models... produce depth measurements of >5cm error." (3) Filtering: discard
  near-stationary consecutive points (<1cm apart) to disambiguate proprioception from grasp
  closure, subsample longer-task demos by 2x, and discard demonstrations whose object points are
  ">1 median absolute deviation" from the nearest fingertip (removing likely DIFT correspondence
  failures) (Sec. 3.2).
- domain randomisation: not simulation-based (no sim used); the closest analog is deliberate
  environment/demonstrator diversity during human data COLLECTION (see above) plus the 3D
  augmentation noise/rotation/translation applied during training (which functions like a
  geometric domain-randomization step on the point-based state-action space).
- contact / penetration handling: not addressed. Grasp state is a simple thresholded
  thumb-index distance signal; no interpenetration or contact-force term exists anywhere in the
  pipeline, consistent with using a 1-DoF gripper rather than a multi-finger hand.

## Evaluation
- metrics: binary real-robot task success out of 15 trials per task/method, "evaluated on
  zero-shot object poses (unseen from training), cameras (iPhone vs Aria), and environment (robot
  workspace vs in-the-wild)" (Table 1 caption).
- headline numbers (Table 1, x/15 real trials): EgoZero — Open oven 13/15, Pick bread 11/15,
  Sweep broom 9/15, Erase board 11/15, Sort fruit 11/15, Fold towel 10/15, Insert book 9/15.
  "From vision" baseline (image-input variant of Baku [62]): 0/15 on all 7 tasks. "From
  affordances" baseline (open-loop linear trajectory between predicted initial/final grasp
  points, inspired by [18]): 12/15 (open oven), 0/15 (pick bread), 0/15 (sweep broom), 0/15
  (erase board), 7/15 (sort fruit), 10/15 (fold towel), 5/15 (insert book) — competitive only on
  simple/near-linear tasks, failing on tasks needing "complex nonlinear motions" (bread-on-plate,
  erase-board). Both ablations ("EGOZERO - 3D augmentations", "EGOZERO - triangulated depth")
  score 0/15 on every single task.
- baselines beaten: image-based closed-loop policy (Baku-style, adapted since "no prior work
  operates under the same assumptions... learning a closed-loop policy in-the-wild, untethered,
  without robot data, from only smart glasses"); open-loop affordance-based policy (linear
  interpolation between predicted grasp landmarks, inspired by prior egocentric-affordance
  learning). Both are author-adapted approximations of prior methods' ideas, not direct
  re-implementations of a single existing system, because "no prior work operates under the same
  assumptions."
- real robot? Yes, entirely real (Franka Panda gripper), with explicit 15-trial-per-cell
  evaluation across 7 tasks x 4 methods = 28 cells in Table 1 (420 total real trials for the main
  comparison alone).

## Limitations stated by the authors
- "Limitations of 3D representations": "the largest source of error during inference comes from
  the correspondence model DIFT... the policy is upper-bounded by the accuracy of its 3D point
  inputs. Though policy learning is made simple with 3D points, it does not have information to
  correct 3D measurement errors" (Sec. 4.5).
- "Limitations of triangulation": requires camera movement and STATIONARY objects pre-grasp —
  "triangulation requires stationary objects, which means that we cannot track objects" once
  manipulation begins; robustness degrades "when the camera has limited movement" (Sec. 4.5).
- "Limitations of hand models": both Aria's hand pose and HaMeR "introduce slight inaccuracies...
  the action labels contain 1-2cm error, preventing the policy from solving high-precision tasks"
  (Sec. 4.5) — this is the paper's explicit, quantified statement of what the hand-pose extraction
  pipeline costs in absolute error.
- Not yet dexterous or bimanual: "We hope that EGOZERO will serve as a framework on which future
  research can extend to fully dexterous and bimanual setups" (Sec. 5).

## Quotable claims (verbatim, with section)
- "We collect zero data in our inference-time environment" (Sec. 4.1).
- "the action labels contain 1-2cm error, preventing the policy from solving high-precision
  tasks" (Sec. 4.5).
- "the best metric depth models, even when grounded with many Aruco tags in the scene, produce
  depth measurements of >5cm error... All policies trained with estimated depth fail
  unequivocally" (Sec. 4.3).
- "Because EGOZERO learns policies from 3D point sets, EGOZERO is completely camera-agnostic"
  (Sec. 4.4).

## Notes for the survey
Belongs in this batch as another scope-boundary case (see SCOPE FLAG, shared with egomimic_2024):
EgoZero's end-effector is a 2-finger gripper, and its "human-to-robot mapping" is not a kinematic
retargeting but a shared morphology-agnostic 3D-point representation that sidesteps embodiment
mapping altogether — a genuinely different strategy from every other paper in this batch
(dexmv_2021/dexvip_2022/okami_2024 retarget hand kinematics; hudor_2024/pgdm_2023 skip hand
retargeting but still use fingertip IK for a dexterous hand; videodex_2022/cyberdemo_2024/
h_rdt_2025/egomimic_2024 use learned networks to bridge the domains). EgoZero's ablations (Table
1) are the sharpest all-or-nothing embodiment-robustness result in the batch: removing 3D
augmentation or switching from triangulated to monocular-estimated depth each independently drops
EVERY task from double-digit success to a hard 0/15 — a much starker failure mode than the
graded degradations seen in dexmv_2021's retargeting ablation or hudor_2024's reward ablation.
The quantified hand-pose extraction error (1-2cm, Sec. 4.5) is one of the few numeric
"extraction accuracy" figures given directly in this batch, comparable to dexmv_2021's MPJPE
table. Block D: physical plausibility of the extracted hand-object interaction is not checked at
all — grasp state is a simple thumb-index distance threshold, with no interpenetration, contact,
or force-closure check anywhere in the pipeline; the closest the paper comes to a plausibility
statement is the triangulation error diagnostic (2-4 pixel reprojection error) and the general
admission that 3D point errors "prevent... solving high-precision tasks," which is a geometric
accuracy claim, not a physical-plausibility check on the hand-object interaction itself.
