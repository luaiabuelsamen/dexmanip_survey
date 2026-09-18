# unidex_2026 — UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos (Zhang, Xu, Zhang, Ma, He, Bao, Ping, Yuan, Lu, Yuan, Liang, Tian, Shao, Zhang, Ding, Gao, Zhao, Zhao, Xu; Tsinghua/Shanghai Qizhi/SYSU/UNC, arXiv 2026)

sources: papers/md/unidex_2026.md [sha 2ccb2df9] ; no code

## One-line contribution
UniDex converts four egocentric human-video datasets into a 9M-frame, 52K-trajectory, 8-robot-hand "robot-centric" dataset via human-in-the-loop kinematic retargeting and visual hand-masking/re-attachment, defines a Function-Actuator-Aligned Space (FAAS) unified action space across hands, and pretrains a 3D VLA (UniDex-VLA) that reaches 81% average task progress on 5 real-world tool-use tasks (vs. 38% for π0), with zero-shot cross-hand transfer and a measured ~2:1 human-demo-for-robot-demo substitution rate.

## Setting
- hand(s): dataset spans 8 dexterous hand platforms (Inspire, Leap, Shadow, Allegro, Ability, Oymotion, XHand, Wuji), active DoF 6-24.
  - Real-robot evaluation uses 3 end-effectors on a 7-DoF Franka arm: Inspire Hand (6 active/12 full DoF), Wuji Hand (20 active DoF), Oymotion Hand (6 active/11 full DoF). arm: Franka Panda (real robot)
  - single-hand only (no bimanual).
- simulator / physics: none — human-video-to-robot transformation and all evaluation are real-world
  - PyBullet is used only as an IK solver inside the retargeting pipeline (multi-end-effector IK for fingertip alignment), not as a training/eval simulator.
- observation: o_t = [P_t, l_t, q_t] — P_t a single-view colored pointcloud from RGB-D (cropped/downsampled), l_t a language instruction, q_t robot proprioceptive state (wrist as absolute pose in FAAS, hand joints in FAAS)
  - real hardware uses an Intel RealSense L515 for egocentric RGB-D.
- action space: FAAS (Function-Actuator-Aligned Space), an 82-dim unified action vector: first 18 dims = wrist poses (9 per hand: 6D continuous rotation [two 3D axis vectors] + 3D translation), remaining 64 dims = joint commands (32 slots per hand, of which 21 "base" actuator slots are shared across all hands and the rest are hand-specific/reserved for future hands)
  - action output is an H-step chunk A_t=[a_t,...,a_{t+H-1}]
  - wrist action is relative to the first frame of the chunk (UMI-style), hand joints likewise "abstracted" in both q_t and a_t.
- objects / data: UniDex-Dataset built from H2O, HOI4D, HOT3D, and TACO egocentric RGB-D datasets — 9M paired image-pointcloud-action frames at 30 fps, >50K (Table 1 states 52K) trajectories across the 8 hands
  - compared against ActionNet (30K traj/2 hands), RoboMind (19K/1 hand), RealDex (2K/2 hands) in Table 1 — UniDex-Dataset is the only one with RGB+depth+pointcloud+language+varied scenes all checked.
    - Fine-tuning uses only 50 teleoperated demonstrations per task (collected via OpenTeleVision + dex-retargeting on Apple Vision Pro) for 5 real-world tasks: Make Coffee (Inspire), Sweep Objects (Inspire), Water Flowers (Wuji), Cut Bags/scissors (Wuji), Use Mouse (Wuji).

## Method
- paradigm: VLA pretraining on a human-video-derived robot-centric dataset, then task-specific fine-tuning (IL)
  - plus a co-training study mixing transformed human demos with real robot demos.
- algorithm: architecture "largely follows π0" but replaces the SigLIP 2D vision encoder with Uni3D, a ViT-based 3D pointcloud encoder (initialized from a 2D pretrained ViT) so the backbone consumes pointclouds instead of images
  - a Gemma-based language/flow-matching backbone fuses pointcloud, text, and proprioception features and decodes FAAS action chunks
  - trained with a conditional flow-matching objective, denoised at inference via forward-Euler integration.
- key trick(s): (1) two-stage human-in-the-loop kinematic retargeting — an automatic stage solves fingertip-based IK via PyBullet's multi-end-effector solver using a 6-DoF "dummy base" alignment offset T_offset (inserted between the real robot base and a virtual base fixed to the human hand transform T_hand) to minimize per-fingertip position error while respecting joint limits/damping, plus an iterative mimic-joint correction (js updated from master joint jm via mimic constraints k,c, repeated N iterations)
  - then an interactive stage where a GUI exposes the 6 DoF of T_offset and lets a human visually correct alignment (typically converges in a few manual tweaks) — done per (human-dataset, target-hand) pair, with extra manual correction focused on contact-rich frames. (2) Visual alignment: mask human hands from the pointcloud (WiLoR + SAM2), render the retargeted robot-hand mesh into the scene pointcloud, then reproject the fused cloud back through a pinhole camera model to fix occlusion/depth-ordering, matching the single-view real-deployment setting. (3) FAAS itself: actuators grouped by shared functional role (e.g., thumb-index pinch, finger curl, lateral ab/adduction) into common coordinate indices, discarding embodiment-specific nuisance factors — contrasted explicitly against EgoVLA, which needs a separate IK post-training alignment stage that FAAS avoids (Sec. 2.2).
- Reward/loss: no RL reward
  - training loss is the conditional flow-matching objective (formula given in Appendix A.1, not reproduced in the parsed main-text sections read).

## Evaluation
- metrics: "average task progress" = mean success rate across all task stages for each of the 5 tool-use tasks (each task decomposed into named stages, e.g. Make Coffee = Grasp + Pour)
  - also "final success rate" (full-task completion) reported in the aggregate table.
- headline numbers (Fig. 11, 20 trials per task/algorithm): Average Task Progress — DP 29.0%±19.9, DP3 35.0%±17.1, π0 38.0%±7.4, UniDex-VLA(No Pretrain) 32.5%±18.5, UniDex-VLA 81.0%±12.1
  - Final Success Rate — DP 22.0%±22.5, DP3 30.0%±18.7, π0 35.0%±10.0, UniDex-VLA(No Pretrain) 23.0%±12.0, UniDex-VLA 76.0%±17.8.
    - Per-task progress values (read from Fig. 11 bar chart, approximate): Make Coffee ~87.5%, Sweep Rubbish ~82.5%, Water Flowers ~85.0%, Cut Bags ~90.0%, Use Mouse ~81.0% for UniDex-VLA (vs. much lower, roughly 12-60%, for all baselines). "UniDex-VLA achieves the largest gain on the hardest setting, Use Scissors to Cut Bags, with an 84.6% increase in average task progress" [relative improvement over the best competing method] (Sec. 5.2).
- generalization results (10 trials each unless noted): Spatial (Fig. 8) — UniDex-VLA generalizes well to out-of-distribution kettle/dripper placements, and "with DemoGen augmentation, it approaches very high success rate over full workspace" (no exact number given in parsed text).
  - Object (Fig. 9) — swapping the training kettle for an unseen smaller purple kettle (different color/size/handle/spout), UniDex-VLA "maintains strong performance" (exact bar values not tabulated in parsed text).
  - Cross-hand zero-shot transfer (Fig. 10) — a policy trained only on Inspire Hand (Make Coffee) deployed zero-shot: Wuji Hand 40% average task progress, Oymotion Hand 60%, vs. baselines "near zero" (explicit cell: π0 gives Wuji 0%, Oymotion 10%; UniDex-VLA No-Pretrain gives Wuji 0%, Oymotion 5%; UniDex-VLA gives Wuji 40%, Oymotion 60%).
- human-robot co-training (Sec. 5.4, UniDex-Cap, Fig. 13, 20 trials/point): average task progress on Make Coffee as a function of (h human demos, r robot demos) — with r=50 robot demos alone the result is 87% (used as the reference "green" high-performance band)
  - e.g. r=30,h=60 gives 87%, r=20,h=70 gives 80%, r=10,h=80 gives 77% — the paper reads off a "human:robot exchange rate ≈ 2:1" (slope of the iso-performance boundary) and states success "always remains near zero without any robot data" even as h increases at r=0 (explicit row: r=0 gives 0% for every h value 0-90).
    - Human demos are reported as "~5.2x faster to collect" than real robot demos for the Make Coffee task.
- baselines beaten: Diffusion Policy (DP), 3D Diffusion Policy (DP3), π0 (gripper-pretrained VLA baseline), and UniDex-VLA(No Pretrain) — an ablation isolating the effect of UniDex-Dataset pretraining while keeping FAAS and the same architecture.
- real robot? Yes — all headline numbers above are real Franka+Inspire/Wuji/Oymotion trials
  - only 50 demos/task used for fine-tuning
  - evaluation trial counts: 20 trials/task/method for main performance (Fig. 11), 10 trials each for spatial/object/hand-generalization studies (Figs. 8-10), 20 trials/point for the co-training study (Fig. 13).

## Limitations stated by the authors
The Conclusion section states "a limitation of our cur-" and is truncated in the parsed markdown before the actual limitation text (page break/figure interleaving) — the specific limitation was not recoverable from the parsed sections read; flagged as a gap rather than inferred.

## Quotable claims (verbatim, with section)
- "UniDex-VLA achieves 81% average task progress and outperforms prior VLA baselines by a large margin" (Abstract).
- "e.g., 81% average task progress vs. π0 [7] at 38%" (Sec. 1).
- "UniDex-VLA achieves the largest gain on the hardest setting, Use Scissors to Cut Bags, with an 84.6% increase in average task progress" (Sec. 5.2).
- "UniDex-VLA achieves 60% success on Oymotion and 40% on Wuji without any fine-tuning, whereas baselines are near zero" (Sec. 5.3).
- "Retargeted human data helps, but robot data is indispensable... success always remains near zero without any robot data" and "Human-robot exchange rate ≈ 2:1... roughly two human demos can substitute for one robot demo" (Sec. 5.4).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds "unified/cross-embodiment action spaces" (FAAS is a direct architectural counterpart to egoscale_2026's shared relative-wrist-motion + per-embodiment adapter approach, and to GR00T-style designs cited by both) and "human-video-to-robot transformation pipelines" alongside dexcap_2024, dexumi_2025 (exoskeleton, no retargeting needed) and dexwild_2025 (glove + optimization-based retargeting, no visual re-attachment step). UniDex's explicit human-robot cost/exchange-rate measurement (~2:1, ~5.2x collection speed) is a rare quantified answer to "how much does human data actually save" — worth citing directly against DexWild's collection-throughput numbers (201 vs 43 demos/hour) since both quantify collection-cost tradeoffs but with different units (throughput vs. substitution ratio). No interpenetration/contact-force instrumentation is reported; "physically plausible hand-object contact" during retargeting is qualitative/human-inspected via the GUI, not measured — flag this if the survey cross-references contact-fidelity claims against opposition-deficit's own dense-grid contact measurement standard. The FAAS DoF/dimension numbers (82-dim vector, 21 shared "base" actuator slots) and the retargeting IK formulation are the paper's most concrete, reproducible technical contributions and should be quoted directly if the survey builds a cross-embodiment action-space comparison table.
