# cross_embodiment_world_models_2025 — Scaling Cross-Embodiment World Models for Dexterous Manipulation (He, Ai, Mu, Liu, Wan, Fu, Du, Christensen, Su; UCSD/SJTU/Stanford/Harvard/Sudo AI, arXiv 2025)

sources: papers/md/cross_embodiment_world_models_2025.md [sha 03999898] ; no code

## One-line contribution
A graph-neural-network (DPI-Net) world model represents any hand (human or robot, 6-24 DoF) and object as 3D particle sets with actions as end-effector particle displacements, is trained jointly on random-interaction data from 6 simulated dexterous hands plus real human demonstrations, and is deployed with sampling-based MPC directly on two real robot hands (6-DoF Ability Hand, 12-DoF XHand) with no motion retargeting or expert demonstrations, showing a clear "embodiment scaling" trend (more training hands -> lower prediction error on an unseen hand) and a 1:1 sim:human co-training mix that roughly doubles real-world plasticine-reshaping success (18/20 and 17/20 vs. 10/20 and 9/20 for human-data-only).

## Setting
- hand(s): 6 simulated dexterous hands used for cross-embodiment scaling study — Ability Hand (6-DoF), Allegro Hand (16-DoF), XHand (12-DoF), Leap Hand (16-DoF), Shadow Hand (24-DoF), and a forearm-less Shadow Hand URDF variant (24-DoF)
  - real-world deployment hands: PSYONIC Ability Hand (6-DoF) and Robot Era XHand (12-DoF), both mounted on a 7-DoF UFACTORY XArm 7. Human hand data collected via multi-view reconstruction (POEM-v2), no exoskeleton/glove. Single-hand only (no bimanual).
- simulator / physics: SAPIEN for rigid-body Object Pushing data collection
  - Rewarped (a differentiable multiphysics simulator) for deformable Plasticine Reshaping data collection
  - 100 random-action trajectories collected per hand per task (no expert/task-directed demonstrations — purely random exploration within a predefined action space).
- observation: unified particle-based world state X_t = (X_t^(e), X_t^(o)) — end-effector represented by N_e 3D particles, object by N_o 3D particles
  - multi-view camera perception (4 Intel RealSense cameras in the real setup) reconstructs particles via POEM-v2 hand-mesh + FPS (human hand), Poisson surface reconstruction + FPS (deformable objects), or FoundationPose + FPS (rigid objects)
  - at deployment, robot particles come from proprioception/forward kinematics and only the object needs to be perceived.
- action space: end-effector particle displacement field (not joint targets) — for model-based control, sampled robot joint actions u_t are converted to particle-space actions via forward kinematics before being rolled out through the world model
  - for real MPC, motion primitives constrain the sampling space: for Object Pushing, straight-line end-effector trajectories in a fixed x-y plane perturbed with Gaussian noise (random number of contacting fingers)
  - for Plasticine Reshaping, three hand-crafted primitives — FingersPinch (z-axis rotation + index-thumb relative motion), PalmPress (z-rotation + z-translation), ThumbPinch (z-rotation + thumb-specific DoF actuation).
- objects / data: simulation — 100 random-action trajectories per hand per task across the 6 hands (rigid box for Object Pushing, plasticine for Reshaping)
  - real-world human data — 30 minutes of demonstrations each for ThumbPinch, FingersPinch, PalmPress (90 minutes total)
  - real-robot evaluation — 4 target letter shapes ("X","R","T","A") x 5 trials x 2 hands = 20 real trials per hand per model condition.

## Method
- paradigm: particle-based world-model learning (self-supervised dynamics prediction from random-interaction data, no reward/task supervision at training time) + sampling-based model-predictive control at deployment — architecturally the cross-embodiment counterpart to wm_dex_human_videos_2025's latent-video world model.
- algorithm: world model = DPI-Net, a graph neural network modeling local particle interactions via message passing with multi-step hierarchical propagation. Graph state ⟨X_t, E_t⟩: vertices X_t are particles, edges E_t are a radius graph
  - per-particle node encoder f_O^enc and edge encoder f_E^enc extract features
  - propagation over L steps updates edge influence ε_k,t^l and node influence h_i,t^l via node/edge propagators f_O, f_E over the neighbor set N_i
  - future state predicted from the final propagated node features. Training objective: L(O_t, Ô_t) = ℓ(O_t, Ô_t), with ℓ = MSE when simulation gives paired point correspondence, or Chamfer Distance (CD) / Earth Mover's Distance (EMD) for unpaired real-world point sets (Eq. 3, Sec. III-C).
- key trick(s): unifying arbitrary-DoF hands into one representation by discarding joint space entirely and representing everything as 3D particles with displacement actions — this is what lets the model be co-trained across 6 morphologically different simulated hands plus real human hands with zero motion retargeting
  - spatial locality (radius-graph message passing) and equivariance (relative coordinates + shared update functions, invariant to global translation/rotation/particle permutation) are cited as the specific inductive biases that let a GNN (vs. a Point Transformer baseline with attention instead of structured message passing) generalize across embodiments.
- Model-based planning (Sec. III-D): sampling-based MPC — 500 candidate action sequences sampled per iteration, planning horizon 4 steps, 10 optimization iterations (CEM-like refinement implied but not named "CEM" explicitly in this section), executes first 2 steps before replanning
  - ~60s per planning update on an RTX 4090. Cost function J(X,G) = L_CD(X,G) + L_EMD(X,G) between the rolled-out predicted particle cloud X and a target point-cloud goal G, consistent with the training loss.
- Particle/graph hyperparameters: Plasticine Reshaping uses 300 object particles + 200 hand particles, radius graph inner/outer radius 0.025m/0.04m
  - Object Pushing uses 100 object + 50 hand particles, radius 0.04m (both radii equal) — higher particle density used for Reshaping to capture finer local contact.

## Evaluation
- metrics: MSE on an unseen (held-out) hand's dynamics prediction, used as the "embodiment scaling" generalization metric (Sec. IV-B)
  - for real-world control, per-target-letter CD and EMD (mean ± 95% CI) plus binary success rate, with success defined as achieving (CD+EMD) loss below 0.0125 (Sec. IV-D).
- headline numbers: Embodiment scaling (Fig. 2) — for each of the 6 hands held out as target, training on more of the remaining hands (x=1..5) "consistently lowers prediction error" for the GNN (DPI-Net), and at x=5 (fully zero-shot on the target hand) performance "often matches or surpasses target-only training"
  - the Point Transformer baseline "shows weaker and less consistent gains." Sim-to-real co-training recipe (Fig. 5): simulation-only training gives the highest (worst) prediction error on held-out human interactions
  - human-only is a stronger baseline
  - a 1:1 simulation:human data ratio gives the lowest error among tested mixtures ("simulation data can act as a useful regularizer for human data rather than a substitute"). Real-robot control (Table I, Plasticine Reshaping, 20 trials per hand per condition = 4 letters x 5 trials): Ability Hand — Co-train (human+6 sim hands) 18/20 success (per-letter 5/5, 4/5, 5/5, 4/5), CD 6.95±0.10e-3, EMD 4.92±0.13e-3
  - Human-only 10/20 success (3/5, 2/5, 4/5, 1/5), CD 7.15±0.16e-3, EMD 5.23±0.23e-3. XHand — Co-train 17/20 success (5/5, 5/5, 4/5, 3/5), CD 6.85±0.12e-3, EMD 4.78±0.14e-3
  - Human-only 9/20 success (4/5, 2/5, 2/5, 1/5), CD 7.22±0.18e-3, EMD 5.18±0.21e-3. Task-specific finding: errors are generally lower for deformable reshaping than rigid pushing (rigid rotations move particles over larger scale), but the embodiment-scaling effect is more pronounced for deformable reshaping (larger contact surfaces make end-effector geometry more influential).
- baselines beaten: Point Transformer (PT) as an alternative particle-dynamics architecture (same inputs/outputs/loss, weaker and less consistent cross-embodiment scaling)
  - human-data-only training (as a zero-shot-transfer baseline, beaten by co-training on both real success rate and CD/EMD).
- real robot? Yes — PSYONIC Ability Hand and Robot Era XHand on a UFACTORY XArm 7, Plasticine Reshaping task, 4 target letters x 5 trials = 20 trials per hand per model (co-trained vs. human-only), success defined by a CD+EMD threshold (0.0125) rather than human judgment.

## Limitations stated by the authors
No dedicated "Limitations" section is present (paper ends at "V. CONCLUSION & DISCUSSION"); within that section the authors note the embodiment-scaling benefit is architecture-dependent (PT shows weaker gains, "consistent with its higher sensitivity to which training subset is used") and, in Sec. IV-B, that scaling benefits are non-uniform across hand morphologies, tied to intrinsic graph density from the radius-graph construction (larger/sparser hands like Shadow/Leap need more training embodiments than smaller/denser hands like Ability) — the authors flag "developing model architectures that are less sensitive to graph densities" as an open direction.

## Quotable claims (verbatim, with section)
- "we represent human and robot hands as sets of 3D particles and define actions as end-effector particle displacement fields... allowing world models to provide a common interface for learning and control" (Abstract).
- "with five source embodiments (zero-shot) it often matches or surpasses target-only training while Point Transformer (PT) shows weaker and less consistent gains, potentially due to the lack of inductive bias" (Fig. 2 caption).
- "a 1:1 ratio performs best across tasks, suggesting that simulation data can act as a useful regularizer for human data rather than a substitute" (Sec. IV-C).
- "On Ability Hand, co-training achieves 18/20 successes, while the human-only model reaches only 10/20 successes... On XHand, co-training similarly attains 17/20 successes, compared to 9/20 for human-only" (Sec. IV-D).
- "the transferable structure across embodiments lies not in their joint spaces, but in the physical interactions they induce in the world" (Sec. V).

## What is predicted and how it is used for control
The world model predicts future 3D particle positions (both end-effector/hand particles and object particles) — not pixels, not latents, not contact forces per se, though particle proximity/contact is implicitly encoded via the radius-graph edges. Control is model-predictive: robot joint-action candidates are sampled from hand-crafted motion primitives, mapped to particle-space displacements via forward kinematics, rolled out through the learned GNN dynamics model, and scored against a target point cloud using a CD+EMD cost; the best sampled sequence's first 2 steps are executed before replanning (receding-horizon MPC), directly analogous to wm_dex_human_videos_2025's CEM-over-joint-angles but in a particle rather than latent-embedding state space, and with a graph/message-passing model rather than a transformer/diffusion predictor.

## Notes for the survey (which sections this feeds; contradictions with other notes)
This is the survey's clearest "cross-embodiment scaling law" result stated in explicit embodiment-count terms (x=1..6 training hands) rather than data-hours — a useful structural contrast to egoscale_2026's data-hours scaling law (1k-20k hours) and dex1b_2025's demonstration-count scaling. Pairs directly with wm_dex_human_videos_2025 as the survey's two "world-model for dexterous control" entries: both use a learned dynamics model + planning (MPC/CEM) rather than a direct policy, both fold human data into a shared state/action representation, but this paper predicts particle geometry from simulation-heavy multi-hand data while wm_dex_human_videos_2025 predicts DINOv2 latents from human-video-heavy data with a single target hand — cite both together when the survey compares "predicted representation" (particles vs. latents) across the world-model subsection. No penetration measurement is present, but the graph is built with an explicit radius/contact threshold (0.025-0.04m) that functions as a proximity/contact detector — closer to a contact-graph representation than any of the pure-IL papers in this batch, worth flagging when the survey assesses which papers have any contact-aware structure at all.
