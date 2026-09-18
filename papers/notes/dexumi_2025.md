# dexumi_2025 — DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation (Xu, Zhang, Hou, Xu, Fan, Veloso, Song; CoRL 2025)

sources: papers/md/dexumi_2025.md [sha 91858c34] ; code/md/dexumi_2025.md [commit acddb8f8]

## One-line contribution
A hand-specific 3D-printed wearable exoskeleton (optimized per target robot hand for shared joint-to-fingertip kinematics) plus a SAM2-segment/inpaint/composite video pipeline turns human demonstrations directly into robot-hand-looking training data, reaching 86% average task success across two dexterous hands with no teleoperation and 3.2x the data-collection throughput of teleoperation.

## Setting
- hand(s): Inspire Hand (12 DoF total, 6 active — thumb 2 active/2 passive, other 4 fingers 1 active/1 passive each, underactuated) and XHand (12 active DoF, fully actuated — thumb 3, index 3, other fingers 2 each)
  - arm: 6-DoF end-effector wrist action (arm hardware not named in parsed text, controlled via ARKit-tracked wrist pose during collection)
  - single/bimanual: single-hand.
- simulator / physics: none — entirely a real-world data collection and real-robot evaluation paper
  - "Simulate Linkage Design" step (code README) uses simulation only to optimize the exoskeleton's mechanical linkage, not for policy training.
- observation: policy input is processed visual observation o_t (150° DFoV OAK-1 wrist-mounted camera, identical mount pose on exoskeleton and robot hand) plus tactile reading f_t
  - images encoded with pretrained DINO-v2 (CLS token), fine-tuned (not frozen) during policy training
  - visual augmentation = random crop, color jitter, random grayscale, Gaussian blur (Appendix E.3).
- action space: policy predicts a chunk of 16 steps of actions a_t, each a 6-DoF relative end-effector action plus hand action (6-DoF for Inspire Hand, 12-DoF for XHand)
  - finger action can be relative (delta) or absolute — relative is default/best (Table 1)
  - wrist action is always relative.
- objects / data: 310 trajectories (Cube Picking), 175 (Egg Carton Opening), 400 (Tea Picking with Tools, shared across both hands), 370 (Kitchen, 4 sub-tasks) + 100 additional trajectories for knob-closing only (Appendix E.1).
  - Recording rate 45 FPS (Inspire Hand: ARKit wrist pose, camera, joint encoders, tactile) or 30 FPS (XHand — tactile becomes unstable at higher rates)
  - data downsampled 3x before training. No aggregate hour count stated.

## Method
- paradigm: IL (behavior cloning) with a diffusion policy; no simulation-based RL/distillation.
- algorithm: diffusion policy (cited to [78,79], i.e. Diffusion Policy / DDPM-style action-chunking)
  - policy p(a_t | o_t, f_t) → chunk of 16 future actions
  - trained 400 epochs per task per hand (Appendix E.3).
    - No reward function — the objective is the IL paper's diffusion denoising loss (paper does not restate the loss formula in the parsed method text; not quoted in this source).
- key trick(s): (1) exoskeleton mechanism design solved as a bi-level optimization max_p S(W_exo^tip(p), W_robot^tip) over exoskeleton design parameters p = {joint positions j_i, linkage lengths l_j}, matching fingertip SE(3) workspace to the target robot hand's forward kinematics while keeping W_exo^tip(p) ⊆ W_robot^tip (Sec 3.1, Eq. in Fig. 3 caption text) — solved by sampling K robot configurations and N exoskeleton configurations and minimizing workspace mismatch, subject to wearability bound constraints j_i ∈ C_i, l_j^min ≤ l_j ≤ l_j^max
  - (2) joint encoders (Alps resistive encoders) at every actuated joint read exoskeleton angles directly, with a learned per-joint regression model mapping exoskeleton encoder value θ_exo^i to robot motor value M_i^robot (calibrated by overlaying exoskeleton and robot visuals at matched motor values) — this avoids visual fingertip retargeting error
  - (3) same tactile sensor type installed on exoskeleton and target robot hand (FSR for Inspire Hand, the XHand's own electromagnetic tactile sensor) to match observation distributions
  - (4) 4-step visual-gap pipeline: SAM2 segments human hand+exoskeleton -> ProPainter inpaints the background -> replay the recorded joint action on the physical robot hand alone to render a robot-hand-only video, SAM2-segment that -> composite by intersecting the exoskeleton mask and robot mask to get an occlusion-aware visible mask and only overwrite the inpainted background with robot-hand pixels inside that mask (Sec. 4, Fig. 4).
- Latency handling (Appendix E.2): per-sensor capture time t_capture = t_receive − l_sensor
  - camera/iPhone latency measured via rolling-QR-code trick from UMI
  - encoder latency tuned by eye until exoskeleton and replayed-robot fingers visually align in the overlay.

## Evaluation
- metrics: stage-wise accumulated success rate per episode (Table 1); each long-horizon task (e.g. Kitchen) scored by successive stage completion.
- headline numbers (Table 1, 20 eval episodes per task per condition): best configuration (relative finger action + tactile + inpainted vision) — Cube 1.00, Egg Carton 0.85, Tea (tool) 1.00, Tea (leaf) 0.85 [Inspire Hand]
  - Tea (tool) 1.00, Tea (leaf) 0.85, Kitchen-knob 0.95, Kitchen-pan 0.95, Kitchen-salt 0.75 [XHand].
    - Abstract's headline "average task success rate of 86%" is the paper's overall summary across the four tasks/two hands.
    - Ablations in the same table: absolute vs relative finger action (relative always ≥ absolute, e.g. Cube 1.00 vs 0.10 on Inspire Hand)
  - with vs. without tactile (mixed — tactile helps salt-picking, 0.75→0.15 without tactile on XHand-salt with relative action, but tactile sometimes hurts due to sensor drift)
  - with vs. without software adaptation (Inpaint vs Mask vs Raw, Inspire-only rows) — Cube drops from 0.95 (no-tactile+inpaint) to 0.60 (mask) to 0.20 (raw), Egg Carton 0.90→0.10→0.05.
- baselines beaten: teleoperation and bare-hand data-collection throughput comparison (Fig. 7, tea-picking-with-tool task, 15-minute sessions): bare hand 51 successful demos, DexUMI 36, teleoperation 11 — DexUMI is "3.2 times greater efficiency than traditional teleoperation" though still slower than bare hand.
- real robot? Yes, all numbers above are real-hardware rollouts (Inspire Hand and XHand), 20 evaluation episodes per task/condition with randomized initial object placement (Sec. 5, "Evaluation protocol").

## Limitations stated by the authors
Hardware: exoskeleton design still needs per-robot-hand tuning (not automated); optimization only matches fingertip workspace, not palm/other contact geometry; wearability still constrained by 3D-print material strength (human hand can distort the exoskeleton linkage in ways the encoder cannot capture); tactile sensors drift under load and are sensitive to attachment (a persistent embodiment-gap source). Software: still needs the physical robot hand to render the composited robot video (no learned image generator yet); inpainting cannot reproduce illumination changes and leaves some blur; camera must be rigidly mounted to the hand (no moving-camera support). Hardware in general: both target hands (Inspire, XHand) lack sufficient precision due to backlash/friction — fingertip position differs depending on approach direction (Sec. 7).

## Quotable claims (verbatim, with section)
- "achieving an average task success rate of 86%" (Abstract).
- "Our approach achieves 3.2 times greater data collection efficiency compared to teleoperation and an average success rate of 86% across four tasks, including long-horizon and complex tasks requiring multi-finger contacts" (Sec. 1).
- "Relative finger trajectories are more robust to noise and hardware imperfections... relative action learns a reactive behavior where the delta action keeps accumulating until a key event is reached... the absolute action learns a static mapping and would stall if the mapping has errors" (Sec. 5.1).
- "Only relative finger trajectories can benefit from the noisy tactile feedback... the tactile sensor on the XHand can drift and become inconsistent after experiencing high pressure.
  - Therefore, in most cases, having tactile makes the results worse" (Sec. 5.1).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds "wearable data-collection hardware" alongside dexwild_2025 (glove+palm-camera, no exoskeleton) and dexcap_2024 (mocap glove, retargeting-based). DexUMI's central claim is that avoiding retargeting entirely (exoskeleton reads robot-joint-space directly) and avoiding the human-hand visual domain gap (inpainting) removes the need for any robot teleoperation data — a stronger claim than DexWild, which still needs teleoperated robot data for co-training grounding. No world-model or interpenetration/contact-force measurement instrumentation here; tactile signal is used as raw policy input, not for any penetration/force analysis. Dataset sizes are per-task trajectory counts, not hours — smaller scale than dexwild_2025 (9,290 demos) or dex1b_2025 (1B) by orders of magnitude; this note's per-task N (175-470 trajectories) should be flagged when the survey compares "scale" across these papers, since DexUMI's contribution is data quality/embodiment-fidelity per trajectory, not raw volume.
