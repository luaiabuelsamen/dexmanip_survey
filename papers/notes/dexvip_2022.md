# dexvip_2022 — DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video (Mandikal and Grauman, CoRL 2021)

sources: papers/md/dexvip_2022.md [sha256 2ac5bb0f] ; no code

## One-line contribution
DexVIP mines a "consensus" grasp hand pose per object category from ~715 curated HowTo100M
video frames (via FrankMocap 3D hand pose + k-medoid clustering), retargets it to the Adroit
hand, and adds it as an auxiliary pose-matching term in a PPO reward alongside a lift-success
term and a GRAFF-style affordance term, beating affordance-only and demo-based baselines on
grasp success/stability/functionality/posture (Sec. 3.2, Fig. 5, Eq. 1).

## Setting
- hand(s): Adroit hand [51], "24-DoF... a five-fingered 24-DoF actuator attached to a 6-DoF arm,"
  30-DoF total, position-controlled (Sec. 3.1). No real hardware: "Due to lack of access to a real
  robotic hand, we perform all experiments in simulation" (Sec. 3.1). Single hand only.
- simulator / physics: MuJoCo [53]; version, timestep, #envs, GPU, wall-clock not stated.
  Table A (Appendix E.1) gives contact/damping parameters "taken from [2]" (DAPG): sliding
  friction 1N, torsional friction 0.5N, rolling friction 0.01N, hand-wrist damping 0.5N,
  hand-finger damping 0.05N, object rotational damping 0.1N, object mass 1kg.
- observation: egocentric hand-mounted RGB image I_t^r and depth D_t^r; a binary affordance map
  A_t^r from a GRAFF-style [18] affordance network; robot proprioception P_t^r (joint angles +
  angular velocities); hand-object contact distance d_t^r (pairwise distance, hand points to
  tracked affordance-region points); 21 touch sensors T^r on palm/fingers (Sec. 3.1, Fig. 2).
  Visual stream -> 3-layer CNN (filters [8,4,3], 512-D bottleneck) -> V_t; motor stream ->
  2-layer FC ([512,512]) -> M_t; concatenated for actor-critic (Sec. 4, "Implementation details").
- action space: 30 continuous joint-angle values (position targets) sampled from a 30-D
  unit-variance Gaussian policy output (Sec. 3.1).
- objects / data: 27 objects total — 16 ContactDB [37] objects (for comparability with GRAFF/
  DAPG) + 11 additional, sourced from ContactDB, 3DNet, YCB, Free3D, 3D Warehouse (Sec. 3.2).
  One policy trained jointly across all 27 objects, 150M agent steps, episode length 200 steps,
  4 random seeds, Adam lr 5e-5 (Sec. 4, "Implementation details").

## Method
- paradigm: pure on-policy RL (PPO [52]) with a video-derived auxiliary reward term — NOT
  imitation learning / behavior cloning on retargeted trajectories, and NOT RL-on-a-single
  full retargeted trajectory. Only one static "consensus" target pose per object category is
  used as a reward target, not a rolled-out demonstration sequence (Sec. 3.2, "Video-informed
  reward function").
- **human data source and size**: HowTo100M [58] ("13.6M instructional YouTube videos");
  authors curate an "object interaction repository I_h of 715 video frames" containing a human
  hand grasping one of the 27 objects, "to yield on average 26 grasp images per object" (Sec.
  3.2, "Video frame dataset"). Selection via weak category/task-id filters (e.g. "care for
  nonstick pans"), not automated hand/action detection.
- **what is extracted from video**: per-frame 3D human hand pose p^h via FrankMocap [44]
  (monocular 3D hand+body pose, SMPL-X hand model: 15 ball joints x 3 DoF = 45 DoF + 6-DoF root,
  joint space J^h in R^(21x3): wrist + 15 finger joints + 5 fingertip locations) — right-hand
  detections only (Sec. 3.2, Appendix D). No object pose, affordance signal is a separate
  pretrained network [18] output (not learned from these frames), and no reward/latent is
  extracted directly from pixels beyond that. Per object class c, the set of poses P(c) is
  k-medoid clustered; "the medoid hand pose of the largest cluster" is the consensus target
  p^h_c* (Sec. 3.2, "Target hand pose acquisition").
- **human-to-robot mapping**: a 4-stage deterministic geometric retargeting from FrankMocap's
  21x3 joint space to Adroit's 30-DoF revolute joint space (Appendix D, Fig. B): (a) FrankMocap
  pose in world coordinates; (b) shift origin to wrist joint -> root-relative frame; construct
  the palmar plane through wrist + fore-finger-knuckle + ring-finger-knuckle joints to set Adroit
  arm orientation; (c) sequential per-joint rotational transform (X/Y/Z, angles alpha/beta/gamma)
  walking the kinematic tree to get a parent-relative frame per joint; (d) azimuth/elevation of
  each parent-relative joint mapped to the corresponding Adroit revolute joint angle (e.g. Adroit
  fore-finger middle joint j9^r = elevation of FrankMocap j6^h relative to parent j5^h, ignoring
  azimuth/tilt); the Adroit little-finger metacarpal j19^r (unmodeled in FrankMocap) is set to
  "0.25 of the elevation at j13^h" — an ad hoc scalar rule, not a learned or optimization-based
  map (contrast dexmv_2021's per-frame NLopt TSV optimization). Authors caveat: "the mapping is
  approximate — due to the inherent differences in kinematic chains" (Appendix D). This mapping
  is applied once, offline, to produce a single static target pose p^r_c* per object; it is not
  run per-timestep at rollout/deployment time.
- **RL or SL**: RL (PPO) on a hand-crafted reward containing the mapped pose as a target, not
  supervised action-cloning on retargeted trajectories.
- reward or loss (Eq. 1, Sec. 3.2, weights from Sec. 4 "Implementation details"; full form
  Appendix B): `R_t = R_succ + alpha*R_aff + beta*R_pose + gamma*R_entropy` — coefficients given
  in the paper as `alpha=1, beta=1, gamma=1, eta=0.001` (note: paper text names the entropy
  coefficient eta in Sec. 4 while Eq. 1 as described uses alpha/beta/gamma/eta for
  affordance/pose/entropy weights; exact symbol-to-term binding is ambiguous in the extracted
  text beyond "eta=0.001" clearly being the entropy weight). Terms (Appendix B):
  `R_succ`: "+1 reward for that time step" if hand-object contact and no object-table contact
  (lift held, effectively a per-step sparse success bonus, not a one-time bonus).
  `R_aff`: negative Chamfer distance between M=10 hand-surface points and N=20 object-affordance
  points (following GRAFF [18]); drops to 0 as the hand approaches the affordance region.
  `R_pose`: negative mean per-joint angle error between current pose p_t^r and target p_c^r*,
  ignoring arm azimuth/elevation, "hierarchically weighted over the joint angles such that errors
  on parent joints are more heavily penalized... gamma_1=1.0, gamma_2=0.75, gamma_3=0.5,
  gamma_4=0.25" (root-to-tip decay per finger link), and gated: "applied only when 30% of the
  robot's touch sensors are activated."
  `R_entropy`: entropy bonus over the action distribution for exploration (standard PPO term).
  No code available to cross-check term implementation.
- key trick(s): k-medoid consensus pose per object class to denoise multi-modal video poses
  (e.g. knife with/without extended index finger); hierarchical (root-to-tip) joint-error
  weighting in R_pose; gating R_pose on touch-sensor contact so pose-matching only fires once the
  hand is near/on the object.
- domain randomisation: object initial orientation "randomly rotate[d] from its canonical
  orientation" each episode, evaluated over "initial orientations ranging from [0,180 degrees]"
  (Sec. 3.1, Sec. 4 "Metrics"). Separate robustness study (Appendix E.2, not training-time
  randomization): object mass swept 0.5-1.5 kg, scale swept 0.8x-1.2x. Noise study (Appendix A):
  proprioceptive/actuation Gaussian noise (mean 0, std 0.01) on joint angles/velocities and
  actuation; pixel perturbation +-5 (clipped [0,255]) on RGB; tracking noise on affordance points
  (Gaussian std 1cm, plus freezing tracking for 20 frames at random intervals).
- contact / penetration handling: not addressed. Reward and metrics reference hand-object
  "contact" (via touch sensors and a lift/no-table-contact test for R_succ) but no term or metric
  measures or penalizes interpenetration depth or volume; MuJoCo's own contact model is used as
  given, no solver settings beyond friction/damping in Table A are reported.

## Evaluation
- metrics (Sec. 4, "Metrics"), all normalized to [0,100%]: (1) Grasp Success — object lifted off
  the table "for at least the last 50 time steps (a quarter of the episode length)". (2) Grasp
  Stability — object still held after applying "perturbation forces of 1 Newton in six orthogonal
  directions" post-episode. (3) Functionality — "percentage of successful grasps in which the
  hand lies close to the GT affordance region." (4) Posture — distance between target human pose
  p^h_c* and final agent pose p^r_T after a successful grasp. "We evaluate 100 episodes per
  object... mean and standard deviation... across all models trained with four random seeds."
- headline numbers: Fig. 5 (left) — DexVIP "consistently outperforms all the methods on all
  metrics" vs. COM, TOUCH, GRAFF, DAPG (exact per-metric percentages not extracted as text,
  embedded in the figure). Ablation (Sec. 4, "Ablations", text values): R_aff-only 60% success on
  ContactDB; +touch -> 63%; +pose (full model) -> 68%. Generalization to the 11 non-ContactDB
  objects (no mocap/affordance ground truth for these): DAPG success drops "from 59% to 50% — a
  15% relative drop"; DexVIP drops "a marginal 4% from 68% to 65%." Under heavy sensing/actuation
  noise, "DEXVIP still yields a grasp success rate of 64%, even outperforming noise-free models of
  the other methods." Training speed: "learns successful policies 20% faster than the next best
  method, GRAFF." Demo-collection cost: DAPG demos take "5 minutes" each via VR/mocap vs. "a few
  seconds" per curated video/image for DexVIP (Sec. 4, "Expert data").
- baselines beaten: COM (center-of-mass affordance prior), TOUCH (touch-only reward, no pose
  supervision), GRAFF [18] (affordance-only RL, no pose prior), DAPG [2] (VR-mocap
  imitation+RL, 25 demos/ContactDB object, borrowed demos for non-ContactDB objects) — DexVIP
  beats all on all 4 metrics per Fig. 5; GRAFF and DAPG are pre-existing methods re-run by the
  authors in their own environment/architecture "for a fair comparison."
- real robot? None. "We are so far unable to deploy our system on a real robot, since we lack
  access to a dexterous hand robot" (Appendix A). All numbers are simulation, stress-tested with
  injected sensing/actuation/perception/tracking noise as a real-world-robustness proxy, not a
  physical trial.

## Limitations stated by the authors
- No real robot: "Due to lack of access to a real robotic hand, we perform all experiments in
  simulation" (Sec. 3.1); "we lack access to a dexterous hand robot" (Appendix A).
- Retargeting is approximate: "the mapping is approximate — due to the inherent differences in
  kinematic chains" (Appendix D).
- Right-hand-only pose estimation, no bimanual handling: "We keep right hand detections only,
  since our robot is one-handed; we leave handling bimanual grasps for future work" (Sec. 3.2).
- Curation is manual/weakly supervised: "the curation step could be streamlined further by
  deploying vision methods for detecting hands, actions, and objects in video" (Sec. 3.2).
- Fixed target pose per object can fail under atypical initial orientation: "a knife with the
  handle on the left would ideally be picked up differently... Failure cases arise when some
  objects are in orientations not amenable to the target hand pose" (Sec. 4).
- Sim-to-real gap parameters not modeled: "friction coefficients, damping factors... could
  further be accounted for using automatic domain randomization techniques" (Appendix A).
- Scope limited to grasping, not manipulation: future work is "expanding the repertoire of
  tasks beyond grasping to learn fine-grained manipulation skills" (Sec. 5).

## Quotable claims (verbatim, with section)
- "we combine three rewards: R_succ..., R_aff..., and — most notably — R_pose, a positive reward
  when the agent's pose p_t^r matches the target grasp pose p_r_c* for that object" (Sec. 3.2).
- "The proposed approach permits imitation by visual observation of the human how-to videos, yet
  without requiring access to the state-action trajectories of the human activity" (Sec. 3.2).
- "DAPG's success rate drops from 59% to 50% — a 15% relative drop in performance — while DEXVIP
  experiences a marginal 4% drop from 68% to 65%" (Sec. 4, "Expert data").
- "the mapping is approximate — due to the inherent differences in kinematic chains as discussed
  above" (Appendix D).

## Notes for the survey
Feeds the "video -> static pose prior -> RL reward shaping" branch, distinct from dexmv_2021's
"video -> full retargeted trajectory -> demo-augmented RL" and from hudor_2024's
"video -> tracked object motion -> reward" (DexVIP's video signal is the human HAND pose only, a
single consensus target per object, not a trajectory and not an object-motion reward). Embodiment
gap is never isolated by an ablation that swaps the retargeting method or removes it — the paper
never runs a "no-pose-prior-vs-perfect-pose-prior" comparison beyond the GT-mocap-vs-inferred-pose
check in Table B (Appendix G.1: policy trained on ContactPose GT poses performs "comparably" to
one trained on FrankMocap-inferred poses), so the retargeting/mapping's own cost is not
separately quantified — only the pose-estimation noise's cost is (and found small). No real-robot
results exist. Block D: physical plausibility of the extracted hand-object interaction is not
checked at all — no interpenetration metric, no force-closure check, no contact-solver detail
beyond friction/damping table values; the R_succ contact and lift condition is the only
hand-object physical event referenced, and it is a lift/no-table-contact boolean, not a
plausibility check on the retargeted pose itself.
