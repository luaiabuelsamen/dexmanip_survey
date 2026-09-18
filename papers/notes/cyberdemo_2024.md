# cyberdemo_2024 — CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation (Wang, Qin, Kuang, Korkmaz, Gurumoorthy, Su, Wang; CVPR 2024)

sources: papers/md/cyberdemo_2024.md [sha256 60891017] ; no code

## SCOPE FLAG
CyberDemo collects human demonstrations via **teleoperation** (a human operator directly drives
the simulated/real robot hand and arm through a vision-based hand-tracking interface), not by
extracting hand/object pose from independently-recorded human activity video. It therefore sits
outside this batch's "without robot teleoperation" framing even though the source data collection
is camera-based and cheap; recorded here for completeness since it was named in the batch, but
its "human-to-robot mapping" is a live teleoperation retargeting system [55], not an offline
video-to-demo translation pipeline like dexmv_2021/dexvip_2022.

## One-line contribution
Human teleoperation demonstrations are collected once in a SAPIEN sim replica of the real scene,
then massively augmented in-sim (camera view, lighting/texture, novel objects via
noise-perturbed replay, and object-pose changes via a "Sensitivity-Aware Kinematics
Augmentation" that reallocates the end-effector pose change across the trajectory by segment
sensitivity), trained with ACT + an auto-curriculum, and fine-tuned on 3 minutes of real
demonstrations — beating real-only visual-pretraining baselines (R3M/PVR/MVP) on a real Allegro
+ xArm6 hand across pick-and-place, pour, and rotate tasks (Table 1).

## Setting
- hand(s): Allegro Hand attached to an XArm6 arm (Sec. 4.1); real hardware. Single hand only.
- simulator / physics: SAPIEN [74]; task environments built to replicate real tables/objects.
  Object properties/contact model, timestep, #envs, GPU/wall-clock not stated.
- observation: RGB image + robot proprioception (Sec. 3.1, "we record the observation (RGB
  image, robot proprioception)... for each frame at a rate of 30Hz"). Vision-based policy input,
  not full state.
- action space: "6-dim delta end effector pose of the robot arm and a 16-dim finger joint
  position of the dexterous hand, with PD control employed for both arm and hand" (Sec. 4.1);
  recorded as "6D Cartesian velocity of robot end effector, finger joint position control target"
  (Sec. 3.1).
- objects / data: 3 tasks — Pick and Place (2 training objects: mustard bottle, tomato soup can;
  tested on more), Rotate (tri-valve for data collection, tested on tetra-/penta-valve), Pour
  (bottle -> bowl, 4 small boxes). Policy training uses "100 simulation demonstrations" (Appendix
  B.3) fine-tuned with real demos — the real-demo count is internally inconsistent in the
  extracted text: Sec. 3.3/Abstract say "3-minute trajectory" of real data collected at 30Hz for
  each task (Sec. 3.1: "we collect only three minutes of robot trajectories for each task on the
  real robot"), while Appendix B.3 states the model "was fine-tuned with 15 real-world
  demonstrations." Both may be consistent (a small number of short clips totaling ~3 minutes) but
  the exact demo count per task is not cleanly stated — flagged as ambiguous.

## Method
- paradigm: imitation learning (behavior cloning via a conditional VAE / Action Chunking with
  Transformers, ACT [85]) on sim-collected + augmented + real-fine-tuned teleoperation
  demonstrations — NOT RL, NOT reward-from-video. No teacher-student/privileged-to-vision
  distillation described.
- **human data source and size**: live teleoperation, not passive video. "we utilize the
  low-cost teleoperation system referenced in [55]. This vision-based teleoperation system
  solely needs a camera to capture human hand motions as input, which are then translated into
  real-time motor commands for the robot arm and the dexterous hand" (Sec. 3.1) — i.e. a single
  RealSense camera observes the operator's hand and drives the robot in real time (the mapping
  happens continuously during collection, not as an offline retargeting stage over a fixed
  video). Real-world demo budget: "we collect only three minutes of robot trajectories for each
  task on the real robot" (Sec. 3.1). Simulation demos for the same teleop system: 100 base
  demonstrations before augmentation (Appendix B.3). NOTE (flag): Appendix B.1/B.2 separately
  describe a "human play data" collection protocol with "no defined task objective... they
  interact freely with the environment" for "30 seconds" per trajectory — this description
  contradicts the task-directed teleoperation described everywhere else in the paper (Sec. 3.1,
  Sec. 4.1, Abstract) and reads like boilerplate misattributed by the PDF extraction; treat the
  B.1/B.2 "human play" framing as unreliable and prefer the main-text description.
- **what is extracted from video**: nothing offline — the teleoperation system [55] performs
  real-time hand detection and retargeting as part of data collection; CyberDemo's own
  contribution operates entirely on the resulting robot-frame state-action trajectories (RGB +
  proprioception -> Cartesian/joint actions), not on raw video or hand pose parameters. No
  object pose, affordance, or reward signal is separately extracted from video by this paper.
- **human-to-robot mapping**: delegated to the cited teleoperation system [55] ("vision-based
  teleoperation system... translated into real-time motor commands"); CyberDemo does not
  describe or modify this mapping, and treats its output (recorded robot trajectories) as the
  base demonstration data to be augmented. This is fundamentally different from an offline
  video-pose-to-robot-pose retargeting pipeline: no MANO/kinematic-chain optimization is
  performed by this paper.
- **RL or SL**: supervised imitation learning. "we train a manipulation policy with Automatic
  Curriculum Learning and Action Aggregation" (Sec. 3) using ACT (Sec. 3.3); a conditional VAE
  head (Appendix B.3) is used for training. No RL objective or extracted reward anywhere.
- loss / training signal: standard ACT behavior-cloning loss on action chunks (chunk size 50,
  "in line with the methodology adopted in [85]," Appendix B.3); exact loss equation not quoted
  in the extracted text (ACT's own reconstruction + KL loss is referenced by citation, not
  reproduced here).
- key trick(s) — quoted: (1) **Sensitivity-Aware Kinematics Augmentation** for object-pose
  randomization: divide the action trajectory of length N into M segments of size K=N/M; per
  segment, "we perturb the action within a segment... by adding Gaussian noise of scale delta_a"
  and increase delta_a "until the task fails to determine max delta_a"; segment robustness
  psi_seg = exp(max delta_a) s.t. eval(tau') = 1 (Eq. 1); the new object-pose change Delta T =
  T_W^Onew (T_W^Oold)^-1 is then redistributed across segments in proportion to normalized
  robustness psi_seg_j, generating a new end-effector trajectory rather than prepending a
  reaching segment. (2) **Add Diverse Objects**: replace the manipulated object and "perturb the
  action sequence from the original demo with Gaussian noises to generate new trajectories," using
  cheap simulator sampling to "enumerate the perturbation until it is successful" — explicitly
  not feasible with real demonstrations. (3) **Automatic Curriculum Learning** (Algorithm 1):
  4 discrete augmentation levels; advance a level when eval success rate r_succ >= r_up or after
  N_max consecutive failures, else generate more augmented data at the current level. (4)
  **Action Aggregation**: merge consecutive small-motion steps (thresholded on end-effector and
  finger motion) into one action to remove teleoperation noise/shaking from the demo.
- domain randomisation (in-sim, listed explicitly, Sec. 3.2): camera pose (rendered by replaying
  simulator state from new viewpoints, "respects the perspective projection in a physically
  realistic manner"); light direction/color/shadow/ambient illumination; object
  specularity/roughness/metallicity/texture; object identity (novel object substitution); object
  initial pose (via the kinematics augmentation above). No numeric ranges given for any of these
  in the extracted text.
- contact / penetration handling: not addressed — no interpenetration term or metric anywhere;
  success is defined purely by task outcome (object on plate, valve rotated 720 degrees, boxes in
  bowl).

## Evaluation
- metrics: binary real-robot task success per trial, reported as trial fractions over 4
  robustness "levels" — "Level 1: In Domain, Level 2: Out of Position, Level 3: Random Light,
  Level 4: Out of Position and Random Light" (Table 1 caption) — each cell evaluated over 20
  real-world trials ("x / 20"). Task-specific success criteria (Sec. 4.1): Pick and Place —
  "object is properly placed onto the red plate"; Rotate — "robot rotates the valve to 720
  degrees"; Pour — "all four boxes have been poured into the bowl."
- headline numbers (Table 1, real robot, x/20 trials): CyberDemo (Ours) beats R3M/PVR/MVP on
  every task x level, e.g. Pick-Place Mustard Bottle Level 1: Ours 7/20 vs. R3M 2/20, PVR 4/20,
  MVP 2/20; Pick-Place Tomato Can Level 1: Ours 14/20 vs. R3M 7/20; Rotate Level 1: Ours 15/20 vs.
  MVP 8/20 (best baseline). Text: "average performance boost of 31.67% averaged on all tasks" at
  Level 1 (in-domain); "35% higher for quasi-static pick and place... 20% higher for
  non-quasi-static rotate" vs. R3M specifically (Abstract). Novel-object generalization
  (Fig. 4/5): best baseline solves the hardest condition (novel object + random light + out of
  position) "by chance with a 2.5% success rate" for rotating; CyberDemo achieves 30%
  (Pick-and-Place generalization) and 42.5% success rotating novel tetra-/penta-valves despite
  training only on tri-valve (Abstract, Sec. 5.2). Data-augmentation ablation (Table 2, 200 sim
  trials / 20 real trials): success climbs monotonically with more augmentation levels — Level-1
  only (100 demos): sim 78%/real (In Domain) 20%; all 4 levels (810 demos): sim Level-1 92.5%,
  real In-Domain 35%, Out-of-Position+Random-Light 40%. Sim-vs-real ratio ablation (Table 4, same
  total demo count): 50 real demos alone -> 0% real success (both In-Domain and Out-of-Position);
  35 sim + 15 real -> 25% In-Domain / 35% Out-of-Position (best out-of-position result); 15 sim +
  35 real -> 50% In-Domain (best in-domain) / 15% out-of-position; text notes pure real-demo
  training "overfits to joint positions rather than utilizing the visual information in images."
- baselines beaten: R3M [46] (Ego4D-pretrained ResNet50, time-contrastive + video-language
  alignment), PVR (MoCo-v2 ResNet50 on ImageNet), MVP (MAE-pretrained ViT on human-interaction
  frames) — all "fine-tune[d]... using our real-world demonstration dataset," i.e. same real data
  budget as CyberDemo's fine-tuning stage, re-run by the authors.
- real robot? Yes — the entire evaluation (Table 1, Figs. 4-5, Tables 2-4's real columns) is on
  the physical Allegro+xArm6 setup, with explicit trial counts: 20 real trials per task/level cell
  in the main comparison, and 20 real trials in the augmentation/curriculum/ratio ablations
  (200 additional sim trials used alongside for those ablations).

## Limitations stated by the authors
- "the necessity to design a simulated environment for each real-world task, thereby increasing
  the human effort involved" (Sec. 6) — though the authors argue this is offset by not needing
  RL reward design.
- Sim2real controller gap remains significant for non-quasi-static tasks: "This gap becomes more
  challenging in our tasks, where the end effector is a high-DoF multi-finger dexterous hand...
  This controller gap can significantly impact non-quasi-static tasks like rotating a valve"
  (Sec. 3.3) — motivating the real-data fine-tuning stage.
- Direct fine-tuning on real data "risks overfitting" due to discrepancies in demo collection
  patterns between sim and real (Sec. 3.3).
- Training purely on real demonstrations causes the policy to "overfit to joint positions rather
  than utilizing the visual information in images" (Sec. 5.5).

## Quotable claims (verbatim, with section)
- "This vision-based teleoperation system solely needs a camera to capture human hand motions as
  input, which are then translated into real-time motor commands for the robot arm and the
  dexterous hand" (Sec. 3.1).
- "we collect only three minutes of robot trajectories for each task on the real robot" (Sec.
  3.1).
- "our methodology outperforms the baselines trained exclusively on real data in the in-domain
  setting (Level 1), exhibiting an average performance boost of 31.67% averaged on all tasks"
  (Sec. 5.1).
- "training solely on 50 real demonstrations results in poor performance, and the policy overfits
  to joint positions rather than utilizing the visual information in images" (Sec. 5.5).

## Notes for the survey
Belongs in the survey only as a boundary case: CyberDemo's "human demonstration" is a live
teleoperation stream (camera-driven, but real-time human-in-the-loop control of the actual
robot/sim-robot), not an independently-recorded human activity video later retargeted offline —
contrast dexmv_2021/videodex_2022/dexvip_2022, which all process pre-existing human video with no
robot in the loop during recording. The paper's real contribution (simulator data augmentation +
curriculum + action aggregation) is downstream of, and orthogonal to, the human-to-robot mapping
question this survey tracks — the mapping itself is entirely outsourced to a cited system [55]
and never described or ablated here, so "what the embodiment gap costs" cannot be quoted from
this paper; the closest analogous ablation is sim-vs-real DATA ratio (Table 4), not
retargeting-quality. Real-robot trial counts (20 per cell) are the most concrete in this batch
alongside videodex_2022's. Block D: physical plausibility of the extracted hand-object
interaction is not checked at all — no interpenetration metric or force-closure check; the paper
only checks final task-outcome success on real hardware. Flag for cross-checking: Appendix
B.1/B.2's "human play data... no defined task objective" description does not match the rest of
the paper's task-directed teleoperation framing and should not be cited as CyberDemo's data
collection protocol without checking the original PDF/project page.
