# dexwild_2025 — DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies (Tao, Srirama, Liu, Shaw, Pathak; RSS 2025)

sources: papers/md/dexwild_2025.md [sha e69ee7d5] ; code/md/dexwild_2025.md [commit 5fa34af5]

## One-line contribution
A portable, calibration-free wearable rig (mocap glove + two palm cameras + wrist ArUco tracking) lets untrained people collect dexterous hand demonstrations in the wild at 201 demos/hour, and co-training a diffusion policy on this human data with a small teleoperated robot set raises unseen-environment success from 22.0% (robot-only) to 62.7% (Sec. V-A).

## Setting
- hand(s): robot side is LEAP Hand and LEAP Hand V2 Advanced (17-DoF hand joint targets)
  - human side is the operator's bare hand, tracked with a motion-capture glove + palm-mounted stereo cameras + ArUco wrist marker
  - arm: xArm (primary) and Franka Panda (cross-arm transfer)
  - single/bimanual: both (bimanual Florist and Clothes Folding tasks duplicate obs/action and append inter-hand pose).
- simulator / physics: none for data collection (real world only)
  - Isaac Lab is used only for a Riemannian Motion Policy (RMP) low-level controller at deployment (Sec. IV-E), not for training.
- observation: two synchronized palm camera images (I_pinky, I_thumb) at the current timestep, plus a history of relative end-effector position deltas {Δp_i, Δp_{i-step}, ..., Δp_{i-H}} sampled over a horizon H
  - images encoded by a ViT (Soup 1M-initialized, per code/md obs_config.yaml `data4robotics.transforms.get_transform_by_name(name=preproc)`)
  - for bimanual tasks the inter-hand relative pose is appended.
- action space: 26-dim action a_i = [a_arm (9-dim: 3D relative end-effector position + 6D orientation), a_hand (17-dim: robot-hand finger joint position targets)]
  - policy predicts a chunk of n such actions
  - control at whatever rate the RMP/Isaac Lab low-level controller consumes (rate not stated).
- objects / data: human dataset D_H = 9,290 demonstrations across 5 tasks and 93 environments — Spray Bottle 3,000 demos/30 envs, Toy Cleanup 3,000 demos/30 envs, Pour 621 demos/6 envs, Florist 1,545 demos/15 envs, Clothes Folding 1,124 demos/12 envs (Sec. IV-A).
  - Robot dataset D_R = 1,395 teleoperated demos: 388 Spray, 370 Toy Cleanup, 111 Pour, 236 Florist, 290 Clothes Folding, collected with xArm + LEAP Hand V2.
  - Train/test object counts per task given in Fig. 5 (e.g. Spray Bottle 25 train/11 test objects).

## Method
- paradigm: IL (behavior cloning), co-trained on human and robot demonstration streams.
- algorithm: diffusion U-Net policy (cited to Chi et al. [6]) predicting an action chunk
  - paper also implements Action Chunking Transformer (ACT [59]) as an alternate policy class for comparison (Table I).
    - Training procedure given as Algorithm 1: sample a batch of {x_h} from D_H and {x_r} from D_R by fixed co-training weights (ω_h, ω_r)
  - encode images with ViT φ_vit
  - sample noise scale t ~ U(1,T), add noise ε_t ~ N(0, σ_t) to the ground-truth action chunk
  - predict ε̂_θ = π_θ(Z_i, a_{i:i+n-1}+ε_t, t)
  - loss L_θ = ||ε_t − ε̂_θ||²₂ (diffusion denoising loss, Algorithm 1 lines 8-11).
- key trick(s): relative (delta) state-action representation removes any need for a global coordinate frame, so the wrist tracking camera can be placed anywhere without calibration
  - palm cameras are rigidly, identically mounted on human and robot hands so RGB observations look the same across embodiments (Fig. 3), which is what lets a single policy be co-trained across domains
  - retargeting optimizes robot hand kinematics to match observed human fingertip positions (fixed hyperparameters, no per-user tuning)
  - a heuristic demo-filtering pipeline drops human trajectories whose wrist pose could not be tracked for >75% of the episode duration, and action outliers are clipped outside the 2nd/97th percentile before Gaussian smoothing (Sec. VII-C).

## Evaluation
- metrics: task success rate (fraction of trials scored success per Appendix VII-A per-task scoring criteria)
  - no distance/angle threshold given in the parsed text beyond task-specific pass/fail descriptions in the appendix task list.
- headline numbers: robot-only vs. 1:2 (robot:human) co-training — In-Domain 64.7% → 79.8%, In-the-Wild 28.5% → 75.1%, In-the-Wild Extreme 22.0% → 62.7% (Sec. V-A, text and Fig. 6)
  - human-only policies score 3.6% in-domain / 7.3% in-the-wild.
    - Bimanual in-the-wild-extreme: 68.1% (co-trained) vs. 13% (robot-only).
    - Cross-task zero-shot (pour, using only spray robot data + pour human data): 94% vs. 0% (robot-only) / 11% (human-only).
    - Cross-arm (xArm→Franka): 37.5% vs. 4.5% (8.3× improvement).
    - Cross-hand (LEAP V2 Adv.→LEAP V1): 65.3% vs. 13.3%.
    - Scaling (Fig. 7 right): average success rises from 28.7% at 20% of D_H to 67.8% at 100% of D_H (2.36× improvement over that range), with especially steep gains in the 25-50% range
  - performance has not plateaued at 100% data.
    - Data-collection rate: 201 demos/hour with DexWild-System vs. 43 demos/hour with a Gello teleoperation baseline (4.6×, Fig. 8), "nearly matching" bare-hand collection speed.
- baselines beaten: robot-only BC, human-only BC, Gello teleoperation (for collection throughput)
  - ACT vs.
  - Diffusion policy-class ablation (Table I) — diffusion benefits more from co-training in every reported cell.
- real robot? Yes — xArm + LEAP Hand V2 Advanced (primary), Franka + LEAP Hand V2 Advanced (cross-arm), xArm + original LEAP Hand (cross-hand)
  - per-trial counts per condition are not given in the parsed text (percentages only; no N reported for the eval episode counts).

## Limitations stated by the authors
Still depends on a limited amount of teleoperated robot data to bridge human-to-robot action gaps; human demonstrations are almost always successful so they contain no error-recovery examples, making learned policies struggle to recover from failures; the method uses only visual and kinematic data with no tactile/haptic sensing, limiting performance on contact-rich tasks (Sec. VI).

## Quotable claims (verbatim, with section)
- "achieving a 68.5% success rate in unseen environments—nearly four times higher than policies trained with robot data only—and offering 5.8× better cross-embodiment generalization" (Abstract).
- "DexWild-System achieves an average collection rate of 201 demos/hour across five representative tasks—nearly matching the rate of demonstrations collected using bare hands and 4.6× faster than a traditional robot teleoperation system based on Gello" (Sec. V-C).
- "there is a clear positive correlation between dataset size and average task performance—rising from 28.7% at 20% dataset size to 67.8% with the full dataset, marking a 2.36× improvement... performance continues to improve all the way to 100% data usage, indicating that the system has not yet plateaued" (Sec. V-C).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the "scaling hardware / cost of data collection" and "human-video / wearable-glove data" sections: DexWild is a glove+palm-camera rig (not a vision-only or exoskeleton rig — contrast with dexumi_2025's exoskeleton-plus-inpainting approach and dexcap_2024's portable mocap glove without palm cameras). Its scaling curve (Fig. 7, unsaturated at 100% of 9,290 demos) is a useful contrast point for dex1b_2025's synthetic-data scale (1B demos, no real robot) and egoscale_2026's egocentric-video scaling claims — all three report "still climbing" scaling curves but on very different data modalities (real teleop-cotrained human data vs. purely synthetic vs. passive video). No interpenetration or contact-force measurement anywhere in this paper — purely a vision+kinematic BC pipeline.
