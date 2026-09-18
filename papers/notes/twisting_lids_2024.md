# twisting_lids_2024 — Twisting Lids Off with Two Hands (Lin, Yin, Qi, Abbeel, Malik; CoRL 2024)

sources: papers/md/twisting_lids_2024.md [869f0aac] ; no code

## One-line contribution
Sim-to-real PPO for two Allegro hands twisting the lid of a bottle-like articulated object: a brake-link object model, a two-keypoint object observation, and a keypoint-based finger-contact reward; one policy, no demonstrations, transferred zero-shot to five printed bottles and ten household containers (abstract; Sec. 1).

## Setting
- hand(s): two 16-DoF Allegro Hands (Wonik Robotics), each on a fixed UR5e arm; arms not moved during the task (Sec. 5.1). bimanual.
- simulator / physics: Isaac Gym (Sec. 7). Object = two rigid parts (base, lid) joined by a continuous revolute joint plus a "Brake Link" on a prismatic joint that "constantly presses against the bottle lid", producing static friction between base and lid (Sec. 3.1, Fig. 2A). Authors: "naively tuning static friction properties between two revolute-joint-connected bodies is not realistic enough with our simulator" (Sec. 3.1). Timestep and #envs not stated.
- observation (policy): "proprioceptive hand joint positions q_t, the estimated center-of-mass 3D positions of the bottle base and lid, and previously commanded target joint positions" (Sec. 3.3). Asymmetric critic additionally sees joint velocities, fingertip positions, contact keypoint positions, object orientation/velocity/angular velocity, random forces, brake torque, and the mass/friction/shape randomisation scales (Sec. 9, "Asymmetric States").
- action space: relative joint-position target for a PD controller, q̃_{t+1} = q̃_t + η·EMA(a_t); output clipped to [−1,1], action scale 0.1, EMA parameter 0.75 (Sec. 3.3; Sec. 9). Control and perception at 10 Hz (Sec. 3.4, 5.1).
- objects / data: no human data. Sim training objects are cylindrical bottles with varying aspect ratio (multi-object) or one mean bottle (single-object) (Sec. 4.1). Sec. 7 lists body diameter "82cm to 86cm", height "55cm to 67cm", cap "62cm to 70cm" diameter — units as printed, almost certainly mm given Fig. 1 object sizes of 7–12 cm. Real: 5 3D-printed bottles (4 round in-distribution, 1 square OOD; Fig. 2C, Fig. 6) and 10 household objects (Fig. 2D).

## Method
- paradigm: RL, sim-to-real ; algorithm: PPO with asymmetric critic; ε=0.2, horizon 16, γ=0.99, GAE τ=0.95, actor MLP [256,256,128] ELU, critic MLP [512,512,512], adaptive LR with KL threshold 0.016, minibatch 8192 (Sec. 9).
- coordination of the two hands: a single policy outputs targets for both hands; there is no explicit role assignment in the observation, but the contact reward assigns roles by construction — left fingertips are rewarded near keypoints on the base, right fingertips near keypoints on the lid (Sec. 3.3, reward (2)). The paper describes the expected behaviour as "the hand that is closer to the object lid should place its finger around the lid ... the two hands should coordinate to avoid dropping the object while one hand twists the lid" (Sec. 3).
- reward (paper, Sec. 3.3, verbatim where the parse allows):
  1. Twisting: "r_twisting = Δθ = q_bottle^{t+1} − q_bottle^t which is the rotation angle of the lid during one-step execution."
  2. Finger contact: two sets of reference points X^L ∈ R^{n×3} on the base and X^R ∈ R^{m×3} on the lid; "r_contact = Σ_i [ 1/(1+α d(X^L, F^L_i)) + 1/(1+α d(X^R, F^R_i)) ]", F^L, F^R ∈ R^{4×3} the left/right fingertip positions, d(A,x) = min_i ‖A_i − x‖₂. "we require each fingertip to stay as close to one of the reference contact points as possible."
  3. Pose: "r_pose = −arccos(⟨x_axis, v⟩)" aligning the bottle axis with a fixed direction v.
  4. Regularisation: "work penalty and action penalty ... We leave the details of the definition to the appendix" — the appendix gives only weights, not the formulas.
  Weights: "α1 = 2.5, α2 = 500.0, α3 = 20, α4 = −0.001, and α5 = −1.0" (Sec. 9). The paper does not say which α belongs to which term; the order suggests twisting/contact/pose/work/action but that is inference.
- no code released (bib: github null), so the reward cannot be checked against an implementation.
- interpenetration / contact: nothing about penetration is stated. Contact is handled only through the reward (fingertip-to-keypoint distance) and the brake-link friction model; early termination if the hands fail to reach a twisting pose within a time limit or the bottle z drops below a threshold (Sec. 3.3, "Reset Strategy").
- key trick(s): brake link for static friction (Sec. 3.1); two-point object representation from SAM + XMem masks and depth (Sec. 3.4); domain randomisation (Table 3): mass [0.03,0.1] kg, friction [0.5,1.5], shape ×U(0.95,1.05), random force scale 2.0 with prob 0.2, bottle-position obs noise 0.02, joint obs noise N(0,0.4), action noise N(0,0.1), frame/action lag prob 0.1. Sec. 9.3: obs and action noise were the highest-variance parameters.

## Evaluation
- metrics (Sec. 4.1): "Angular Displacement (AD) is the total number of degrees through which the lid has been twisted"; "Time-to-Fail (TTF) is the period measured from the moment the bottle is held to the point when it either slips from the hand or becomes lodged"; "Velocity (Vel) is AD divided by TTF". Sec. 5.4 adds lid-removal success = "the object's lid being completely detached from the object body".
- sim results: Fig. 4 only (curves, 5 seeds); no table. Reduced contact reward fails to learn; no-vision is "substantially worse"; multi-object training slightly better than single-object (Sec. 4.2).
- headline real numbers (Table 1; 30 s trials; AD in degrees, TTF in s): Ours BlueBottle AD 946.33±383.81, TTF 23.67±10.97, Vel 41.26; WoodBottle 499.50±578.23, TTF 30.0; RedBottle 150.67±113.47, TTF 30.0; GoldBottle 98.67±66.91, TTF 30.0; SquareBottle 43.00±12.12, TTF 30.0. Best baseline AD on any object: Replay 128.33±217.96 (BlueBottle) with TTF 7.67. Sec. 5.2: "one of the deployed policies can achieve 4 full turns (360 degrees) in 30 seconds on average" on the blue bottle; "can rotate 3 out of 5 objects at a reasonable speed".
- trial counts: Sec. 5.1 says "20 trials, with each trial lasting for a maximum of 30 seconds" and "three best policies out of ten policies trained on ten different random seeds"; the Table 1 caption says "3 policies trained on 3 different seeds". Whether 20 trials is per policy or total is not stated.
- lid removal on household objects (Table 4): PeanutButter 10 %, EmptyNutella 10 %, Nutella 40 %, FiberGummies 50 %, Earplugs 20 %, OilCapsules 40 %, StressGummies 40 %, HairMask 60 %, overall 33.75 %. Table 4 lists 8 objects although Sec. 5.4 says 10; trials per object not stated. Sec. 9.1: for in-distribution objects "the success rates are consistently 100%" if one turn counts as removal.
- baselines beaten: open-loop Replay, No-Vis, No-Asym, Large actor (Table 1). No external method: "there is no learning-based method directly comparable to ours on the proposed task" (Sec. 2).
- real robot? yes — two Allegro hands on fixed UR5e, one RealSense D435, 10 Hz, ZeroMQ (Sec. 5.1, Sec. 8). Perturbation test (Sec. 5.3) is qualitative and uses marker-based tracking instead of the segmentation pipeline. Vertical-setup variant (Sec. 9.2) is qualitative, perception turned off.

## Limitations stated by the authors
- The large actor matches the full policy in simulation but "does not transfer to the real world ... some overfitting occurs" (Sec. 5.2).
- Household objects needing 5 turns reach only 10 % removal (Sec. 5.4, Table 4).
- Perturbation experiment needed marker-based tracking "to disentangle the visual occlusion effect" (Sec. 5.3).
- Brake link is "the only way we find" to get static friction; per Sec. 3.1 the simulator's native joint friction was not realistic enough.
- No explicit limitations section; Sec. 6 states only what was shown.

## Quotable claims (verbatim, with section)
- "To the best of our knowledge, this is the first sim-to-real RL system that enables such capabilities on bimanual multi-fingered hands." (abstract)
- "a two-point sparse object representation, extracted from off-the-shelf object segmentation and tracking tools, is sufficient to solve the perception problem." (Sec. 1)
- "we discover a simple keypoint-based contact reward that yields natural lid-twisting behavior on the robot fingers." (Sec. 1)
- "After decreasing the scale of finger contact reward, learned policies fail to master the desired lid-twisting skill" (Sec. 4.2)
- "Replaying a successful trajectory will not lead to a stable grasp for most of the time, and the bottle will directly roll on the fingers and then drop off the palm." (Sec. 5.2)

## Notes for the survey
- Feeds: bimanual RL sim-to-real; reward design for contact (keypoint attraction with fixed left/right role); articulated-object simulation tricks; the "small policy transfers, large does not" observation.
- Coordination is baked into the reward, not the architecture: roles are fixed (left = base, right = lid) via X^L/X^R. Contrast with bidexhd_2024 / dexmachina_2025 / maniptrans_2025, where reference trajectories from human data fix the roles instead.
- Contact reward is a distance-to-keypoint attraction with no penetration term and no measured penetration; the object is a simple cylinder pair, so this is the weakest evidence in this batch on interpenetration handling.
- Reward-weight-to-term mapping is not given; do not quote "contact weight 500" without the caveat.
- Object dimension units in Sec. 7 are printed as cm but are physically mm-scale relative to Fig. 1; quote with the caveat.
