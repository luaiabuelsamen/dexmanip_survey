# wm_dex_human_videos_2025 — World Models for Learning Dexterous Hand-Object Interactions from Human Videos (Goswami, Bar, Fan, Yang, Zhou, Krishnamurthy, Rabbat, Khorrami, LeCun; FAIR at Meta / NYU, arXiv 2025)

sources: papers/md/wm_dex_human_videos_2025.md [sha caa49482] ; no code

## One-line contribution
DexWM is a latent-space (DINOv2) world model trained on 829 hours of egocentric human video (EgoDex) plus DROID robot data, using MANO fingertip-keypoint differences as its action representation and an auxiliary hand-consistency (heatmap) loss to preserve fine hand detail, that plans via CEM/MPC in latent space and transfers zero-shot to a real Franka+Allegro robot with 83% grasping success after only ~4 hours of task-agnostic simulation fine-tuning — beating Diffusion Policy by over 50 points on average across reach/grasp/place.

## Setting
- hand(s): human hand represented with 21 MANO keypoints per hand (left+right, H^L, H^R ∈ R^{21×3})
  - robot hand is an Allegro Hand (4-finger) mounted on a Franka Panda arm — mapped into DexWM's 5-finger action space by re-using the last (ring-equivalent) Allegro finger's keypoints to also stand in for the missing pinky. arm: Franka Panda.
    - Parallel-jaw grippers in the DROID dataset are approximated as dexterous hands using dummy keypoints on concentric circles at the end-effector, radius varying with gripper open/close state to mimic finger spread (Fig. 3b) — this is how non-dexterous robot data is folded into the same action space.
- simulator / physics: RoboCasa simulation (built on a Franka Panda + Allegro gripper) used only for ~4 hours of exploratory fine-tuning data and for the 50-trial-per-task simulated reach/grasp/place evaluation
  - no physics-engine detail (contact model, timestep) is given in the parsed text.
- observation: state s_ki ∈ R^{P×d} is a frozen DINOv2 patch-level embedding of an egocentric RGB image I_ki (P = number of patches, d = feature dim per patch) — not raw pixels
  - this state is used both for prediction and for MPC-style planning cost.
- action space: action vector a_{k1→k2} = hand keypoint differences (H_k2 expressed in the k1 camera frame via known rigid transform T_k1^k2, minus H_k1) concatenated with camera-motion delta translation δt ∈ R^3 and delta orientation δq ∈ R^3 (Euler angles) — flattened to 44×3=132 dimensions fed into the predictor via AdaLN conditioning.
  - For real/sim robot deployment, keypoints are computed via forward kinematics from known joint angles
  - robot task planning optimizes joint angles Θ_0,...,Θ_{T-1} via the Cross-Entropy Method (CEM), converted to keypoint-space actions a_k through the robot's forward kinematics function G.
- objects / data: EgoDex (829 hours of 1080p egocentric human video with hand+pose annotations) + DROID (diverse parallel-jaw-gripper robot manipulation) for pretraining
  - ~4 hours of "exploratory, non-task-specific" random-motion sequences in RoboCasa (Franka+Allegro) for embodiment fine-tuning — two exploration strategies compared: Lift-Initialized Random Exploration (noisy Lift-dataset trajectories, deliberately made unsuccessful) vs. fully programmatic random-3D-target reaching (no teleoperation/prior dataset needed)
  - Lift-Initialized data gave slightly better downstream performance (53% vs 49% average sim success across reach/grasp/place), so that dataset is used for the headline results.

## Method
- paradigm: latent-space world model (self-supervised next-state prediction from human+robot video, deterministic), used for zero-shot planning/control via MPC — not IL/RL end-to-end policy learning
  - DexWM itself is never trained with a task reward.
- algorithm: encoder E_φ = frozen DINOv2 (patch features as state)
  - predictor f_θ based on Conditional Diffusion Transformers (CDiT) architecture but modified to directly regress future latent states (no iterative denoising, for faster inference) rather than diffuse them, conditioned on the 132-dim flattened action vector via AdaLN layers at every transformer block
  - environment assumed deterministic (unlike prior stochastic world models NWM/PEVA) for faster inference
  - trained with random (non-fixed-frequency) timestep skipping to improve generalization.
    - Multistep/autoregressive rollout: predicted ŝ_{kn+1} and the next action are fed back in to generate ŝ_{kn+2}, etc.
    - Planning: goal-conditioned CEM optimization over joint-angle sequences Θ_0..Θ_{T-1}, minimizing cost C = C_state + μ·C_kp (μ=0.001), where C_state = L2 distance between predicted final latent state s_T and goal latent s_g, and C_kp = Euclidean pixel distance between predicted and goal fingertip/wrist heatmap locations (V̂_T vs V̂_g) — combining both costs outperforms C_state alone, "indicating latent embeddings alone may be suboptimal for planning" (Sec. 3.4)
  - an added end-effector-orientation cost term is used specifically for the grasping task to keep a neutral pose.
- key trick(s) / loss: overall training loss L = L_state + λ·L_HC with λ=100 (image encoder frozen throughout training).
  - L_state = MSE between predicted patch embeddings ŝ_{kn+1} and the ground-truth DINOv2 embedding of the true next frame.
  - L_HC (hand-consistency loss) = an auxiliary loss where a transformer network g_θ predicts 12×H×W heatmaps V̂_{kn+1} of fingertip+wrist locations from the predicted state, penalized against ground-truth heatmaps V_{kn+1} — introduced because "relying solely on L_state is insufficient for capturing the fine-grained details necessary for modeling dexterous dynamics, as the hands occupy only a small region of the image" (Sec. 3.3).
  - Ablation (Table 1) shows adding DROID to EgoDex training data lowers embedding L2 error and raises PCK@20 on RoboCasa transfer (e.g., PCK@20 avg 13→17 on RoboCasa when combining EgoDex+DROID vs. EgoDex alone), i.e. non-dexterous robot data still helps cross-embodiment generalization.

## Evaluation
- metrics: embedding L2 error (perceptual similarity of predicted vs ground-truth DINOv2 features) and PCK@20 (percentage of predicted hand keypoints within 20 pixels of ground truth) for open-loop rollout evaluation (4-second/20-frame @5Hz horizon, Sec. 4.4)
  - simulation robot-transfer success rate (%) for reach/grasp/place in RoboCasa (50 trials/task, success = Euclidean distance threshold for reach/place, object-robot contact for grasp)
  - real-world grasping success (%, 12 trials, "manually observing whether the object is in the hand").
- headline numbers: Open-loop (Table 3, referenced but table itself not captured in this excerpt) — DexWM "achieves over 5 points higher PCK@20 on average" than the next best baseline (PEVA*), though PEVA* has slightly lower raw L2 error (the paper argues L2/perceptual similarity does not guarantee accurate hand position).
  - Table 1 ablation numbers (EgoDex vs DROID vs EgoDex+DROID pretraining, measured on held-out EgoDex and downstream RoboCasa): on RoboCasa, Embedding L2 Error "At 4s"/"Avg" = 1.03/0.79 (EgoDex only) vs 1.3/0.96 (DROID only) vs 0.79/0.57 (EgoDex+DROID, best)
  - PCK@20 "At 4s"/"Avg" = 3/13 (EgoDex only) vs 2/12 (DROID only) vs 7/17 (EgoDex+DROID, best) — combining human and non-dexterous robot data beats either alone on the downstream RoboCasa domain.
    - Robot transfer (Table 4, success rates in %): RoboCasa sim — Diffusion Policy: Reach 16, Place 8, Grasp 0
  - DexWM w/o pretraining: Reach 18, Place 8, Grasp 14
  - DexWM (ours, full): Reach 72, Place 28, Grasp 58.
    - Real robot grasping: Diffusion Policy 0%, DexWM w/o PT 0%, DexWM (ours) 83% (10/12 trials).
    - A control experiment pretraining Diffusion Policy on the same human data with a similar action space still only reaches 4% average simulation success (vs. DexWM's 53% average across the 3 sim tasks), used to argue the gain is from modeling dexterous dynamics, not pretraining alone (Sec. 4.5).
- scaling result: not a data-quantity scaling curve — instead an ablation over data *sources* (EgoDex vs DROID vs both; Table 1), showing added human data + added non-dexterous robot data both help downstream transfer
  - no explicit "performance vs. dataset size" plot is present in the parsed text (Sec. 4.2/4.3 headers seen but full ablation table content beyond Table 1 not captured in this pass).
- baselines beaten: Cosmos-Predict2 (text-conditioned video diffusion "World-to-Video" model), Navigation World Model (NWM*, camera-motion-only variant), PEVA* (upper-body-pose-only variant, no finger articulation), Diffusion Policy (goal-image-conditioned action policy), and a "DexWM (w/o PT)" ablation trained on RoboCasa from scratch without human-video pretraining.
- real robot? Yes — Franka Panda + Allegro Hand, zero-shot (no real-world fine-tuning data used at all): 12 grasping trials with varied objects, 10/12 (~83%) success, using CEM-planned trajectories executed via low-level controllers (Fig. 10 shows an example goal-image-conditioned plan).

## What is predicted and how it is used for control
DexWM predicts future latent (DINOv2 patch-embedding) states of the environment, conditioned on past latent states and a dexterous hand-keypoint-plus-camera-motion action — i.e., it predicts compressed visual/semantic latents plus (via the auxiliary head) explicit fingertip/wrist heatmap locations, not raw pixels and not contact forces/penetration. Control uses the world model purely for planning, not as a policy: a goal image is encoded to a target latent s_g, and CEM optimizes a sequence of robot joint angles Θ_0..Θ_{T-1} (converted to keypoint actions by the robot's own forward kinematics) to minimize the combined latent-distance + keypoint-heatmap-distance cost between the rolled-out final state s_T and s_g; the resulting waypoint trajectory is executed by a separate low-level controller. This is explicitly framed against behavior-cloning approaches (which predict actions/waypoints directly from observations): "DexWM is used as a state-transition model within an MPC optimization framework for planning waypoint trajectories... thus offering greater robustness" (Sec. 1).

## Limitations stated by the authors
Currently only demonstrates image-based goal planning, though the framework "can be extended to accommodate text-specified goals"; relies on ~4 hours of exploratory simulation data to bridge the embodiment gap, and removing this dependency is left to future work; the setup assumes static scenes without external agents (true of both pretraining datasets, EgoDex and DROID) — handling dynamic/interactive environments "may require incorporating stochasticity, e.g., via an additional latent variable optimized at test time" (Sec. 5).

## Quotable claims (verbatim, with section)
- "DexWM outperforms prior world models conditioned on text, navigation, or full-body actions in future-state prediction and demonstrates strong zero-shot transfer to unseen skills on a Franka Panda arm with an Allegro gripper, surpassing Diffusion Policy by over 50% on average across grasping, placing, and reaching tasks" (Abstract).
- "relying solely on L_state is insufficient for capturing the fine-grained details necessary for modeling dexterous dynamics, as the hands occupy only a small region of the image" (Sec. 3.3).
- "DP achieves only 4% average simulation success, far below DexWM's 53%, indicating that the improvement stems from modeling dexterous dynamics rather than pretraining alone" (Sec. 4.5).
- "Without any finetuning on real robot data, DexWM achieves 10 successes out of 12 trials (≈83% success rate)...
  - By planning in latent space rather than directly predicting actions, DexWM shows strong generalization" (Sec. 4.5).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Primary entry for the "world models predicting latents + MPC for control" thread, contrasted directly with cross_embodiment_world_models_2025 (graph-based world model + MPC on multiple embodiments) — both use a world model as a planning substrate rather than a direct policy, unlike every IL/VLA paper in this batch (dexwild_2025, dexumi_2025, egoscale_2026, unidex_2026, teledexter_2026). DexWM's action representation (MANO keypoint deltas + camera motion) is architecturally close to egoscale_2026's wrist-motion-plus-hand-articulation representation and to unidex_2026's fingertip-based kinematic retargeting, so cross-reference when the survey compares "how hand action is represented for cross-embodiment transfer." No interpenetration/contact-force channel is predicted or measured; the one physical-interaction signal is qualitative ("the cup moves forward when the hand collides with the cup," Sec. 4.4 "Controllability") — flag that this paper's "physics" is entirely emergent behavior in a learned latent space, not a measured or simulated contact channel, which matters if the survey is grading papers by contact/penetration rigor per CLAUDE.md's measurement standards.
