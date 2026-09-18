# egoscale_2026 — EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data (Zheng, Niu, Xie, Wang, Xu, Jiang, Castañeda, Hu, Tan, Fu, Darrell, Huang, Zhu, Xu, Fan; NVIDIA/UC Berkeley/UMD, arXiv 2026)

sources: papers/md/egoscale_2026.md [sha 39c691ba] ; no code

## One-line contribution
A flow-based VLA pretrained on 20,854 hours of egocentric human video (>20x prior human-transfer datasets) with wrist-motion + retargeted 22-DoF hand-joint supervision, followed by lightweight aligned human-robot mid-training, exhibits a log-linear scaling law between human-data hours and validation loss (R²=0.9983) that predicts real-robot task-completion performance, and lifts average success rate 54% over a no-pretraining baseline while transferring to a completely different low-DoF robot hand.

## Setting
- hand(s): primary robot is the Sharpa Wave hand, 22-DoF, joint-space control (target joint angles), mounted on a Galaxea R1Pro
  - cross-embodiment transfer target is the Unitree G1 with a 7-DoF tri-finger hand and a shorter arm/reduced workspace.
    - Human hand is represented by 21 keypoints (MANO-style) per frame, retargeted via an optimization-based procedure enforcing joint limits/kinematic constraints into the 22-DoF Sharpa hand joint space for pretraining.
- simulator / physics: none — entirely real-world human video + real-robot teleoperation and evaluation.
- observation: o_t = (I_t, l_t), an image and language instruction, encoded to a vision-language embedding φ_t by a pretrained VLM visual encoder
  - three RGB cameras on the real robot (one head-mounted egocentric, two wrist-mounted facing the palm)
  - robot proprioceptive state q_t is used when available, replaced by a learnable placeholder token for human data (no proprioception signal exists for human demos).
- action space: flow-matching-predicted chunk of future actions
  - arm action = relative wrist motion ΔW^t = (W_w^0)^{-1} W_w^t (SE(3) relative end-effector motion, shared representation across human and robot data, both 7-DoF arms controlled in relative EE space with incremental position/orientation)
  - hand action = retargeted 22-DoF joint targets (Sharpa hand) or, for G1, an embodiment-specific adapter output for the 7-DoF tri-finger hand
  - lightweight embodiment-conditioned MLP adapters (following GR00T N1) encode per-embodiment proprioception and decode per-embodiment hand actions, while wrist-motion prediction, the VLM backbone, and the DiT action expert are shared across embodiments.
- objects / data: Stage I pretraining = 20,854 hours total egocentric video: the bulk is in-the-wild recordings spanning 9,869 scenes, 6,015 tasks, 43,237 objects (household/industrial/retail/educational), 30 FPS RGB with off-the-shelf SLAM + hand-pose estimation (noisy)
  - plus 829 hours of the EgoDex dataset (Apple Vision Pro, 194 tabletop tasks, higher-precision tracking) used to anchor pretraining.
    - Stage II aligned human-robot mid-training = 344 tabletop tasks, ~30 human trajectories + ~5 robot trajectories per task, totaling ~50 hours human + ~4 hours robot data, collected with the same camera rig as the robot (Vive trackers for 3D wrist pose, Manus gloves for 25-joint in-hand pose).
    - Post-training/eval tasks (Stage III): 100 teleoperated demos each for Shirt Rolling (20 demos, deformable), Card Sorting, Tongs-for-Fruit, Bottle-cap Unscrewing (4 bottles x 25 trajectories = 100), Syringe Liquid Transfer.

## Method
- paradigm: VLA pretraining (self/weakly-supervised action prediction on human video) -> aligned human-robot mid-training (co-training) -> task-specific post-training (few-shot fine-tuning)
  - flow-matching generative action model, not RL.
- algorithm: flow-based VLA "similar to GR00T N1" — VLM backbone produces vision-language embedding φ_t, conditioning a DiT ("action expert") trained with a flow-matching objective to denoise a chunk of future wrist+hand actions.
  - Three-stage training recipe (Sec. 2.4): Stage I (human pretraining) — 20K hours, 100K steps, 256 GB200 GPUs, batch 8,192, lr 5e-5, all parameters unfrozen
  - Stage II (aligned mid-training) — 50K steps, batch 2,048, lr 3e-5, VLM backbone frozen, only vision encoder + DiT action expert updated
  - Stage III (post-training) — task-specific demos, 10K steps, batch 512, lr 3e-5, vision encoder frozen if mid-training was used, unfrozen otherwise (to accommodate new embodiments).
- key trick(s): decoupling data scale from embodiment alignment — Stage I supplies scale/diversity/semantic grounding from noisy, unaligned human video
  - Stage II supplies precise human-robot correspondence (same cameras, calibrated intrinsics, matched Vive/Manus motion capture) without needing large paired robot data
  - relative (not absolute) wrist-motion representation shared identically across human and robot data for direct cross-embodiment alignment
  - ablation shows retargeted joint-space hand actions (vs. wrist-only or fingertip-SE(3)-then-MLP) is the most consistent hand-action representation for pretraining (Sec. 3.6, Fig. 8).
- Loss/objective: flow-matching action-prediction loss (standard formulation, not separately restated as a novel term in the parsed text)
  - offline evaluation uses MSE between predicted (16-sample-averaged) and ground-truth wrist+hand actions on a held-out 2,000-episode human validation set, sampled at 20 timesteps/trajectory (Sec. 3.3).

## Evaluation
- metrics: (1) offline human-action-prediction validation loss (MSE) on held-out human video
  - (2) real-robot task completion score (fine-grained, continuous) and (3) real-robot task success rate (binary), Sec. 3.1.
    - Each policy trained with 2 random seeds
  - 10 evaluation trials per checkpoint except Task III (Tongs), evaluated 4 trials x 4 bottle instances = 16 trials
  - initial scene configuration matched via an image-overlay-based initialization procedure to reduce eval variance.
- headline numbers: Fig. 4 (5 tasks, 4 conditions) — human pretraining "improves average task completion by over 55%" over training from scratch
  - combined Pretrain+Midtrain gives the best score on every task (approximate values read off Fig. 4: Shirt completion ~0.83-0.90 vs. ~0.05-0.14 no-pretrain; average completion ~0.79 for Pretrain+Midtrain vs. much lower for scratch — exact per-task bars are only given graphically, not tabulated, so treat individual bar values as approximate).
    - Scaling law (Sec. 3.3, Fig. 5): pretraining on 1k/2k/4k/10k/20k hours of human data gives a fitted log-linear relationship L = 0.024 − 0.003·ln(D) between optimal validation loss L and data hours D, R²=0.9983
  - downstream average task completion score rises monotonically from 0.30 at 1k hours to 0.71 at 20k hours with "no signs of saturation in the explored regime." One-shot transfer (Sec. 3.4, Fig. 6): starting from human-pretrained + mid-trained model, post-training on a single robot demo (+100 aligned human demos) achieves success rate 0.88 on Fold Shirt and 0.55 on Unscrewing Water Bottles (avg across 3 bottle geometries) — models missing either pretraining or mid-training "fail" in this one-shot setting (no numeric floor given).
    - Cross-embodiment (Sec. 3.5, G1 tri-finger hand, Fig. 7): human pretraining + G1-play mid-training gives "over 30% absolute improvement in success rate across both evaluated tasks" (Pen in Bin, Dish in Rack) vs. a G1-embodiment-only baseline without human pretraining, evaluated over 10 trials per seed x 2 seeds.
    - Hand-action-representation ablation (Sec. 3.6, Fig. 8): retargeted full joint-space representation beats wrist-only (e.g., Card ~0.79 vs ~0.24) and fingertip-based (~0.61) representations across Card/Tong/Bottle tasks.
- baselines beaten: no-pretraining (from scratch), mid-training-only (aligned human-robot data without large-scale human pretraining), G1-embodiment-only fine-tuning (no human pretraining), wrist-only and fingertip-based human action representations.
- real robot? Yes — Galaxea R1Pro (22-DoF Sharpa Wave hands, bimanual, base/torso fixed) for the five main tasks, and Unitree G1 (7-DoF tri-finger hand, with a separately trained Homie policy handling lower-body locomotion/balance) for the two cross-embodiment tasks.
  - All numbers above are real-robot trials (10 per checkpoint per seed, or 16 for the multi-bottle task)
  - no sim numbers reported anywhere.

## Limitations stated by the authors
The paper does not extrapolate validation loss or performance beyond the measured 1k-20k hour range, though it states the trend "suggests substantial headroom for further gains" (Sec. 3.3); the fingertip- and wrist-only hand-representation ablations show that representation choice materially affects downstream robustness — small fingertip pose errors after IK/MLP mapping "lead to implausible joint configurations" and unstable grasps (Sec. 3.6). No explicit "Limitations" section was found in the parsed text (not present in the visible section map up to Related Work/Conclusion); Conclusion section (Sec. 6, line 290) was not read in full for additional caveats — treat this as a gap in this note.

## Quotable claims (verbatim, with section)
- "we uncover a log-linear scaling law between human data scale and validation loss.
  - This validation loss strongly correlates with downstream real-robot performance" (Abstract).
- "Average task completion rises monotonically from 0.30 at 1k hours to 0.71 at 20k hours, with no signs of saturation in the explored regime" (Sec. 3.3).
- "The fitted curve achieves an R² of 0.9983, indicating an almost perfect linear relationship in log space" (Sec. 3.3).
- "using a single robot demonstration, the trained policy achieves up to 88% average success on shirt folding, even though the mid-training data contains only folding behaviors" (Sec. 1).
- "policies pretrained and fine-tuned directly on the same G1 dataset, without prior human pretraining, fail to achieve comparable success rates" (Sec. 3.5).

## Notes for the survey (which sections this feeds; contradictions with other notes)
This is the strongest documented scaling-law result in the batch (log-linear fit with R²=0.9983 against real-robot task completion, not just an offline proxy) — directly comparable to dexwild_2025's scaling curve (28.7%→67.8% over 5x data, no fitted law) and dex1b_2025's qualitative-only scaling figure; egoscale_2026 should anchor the survey's "scaling law" subsection since it is the only note in this batch with a fitted functional form and reported R². Its two-stage pretrain+mid-train recipe is architecturally close to unidex_2026 and wm_dex_human_videos_2025 (egocentric-video-to-hand-control) — cross-check those notes for whether they replicate or contradict the finding that wrist-only action supervision underperforms full retargeted joint-space supervision (Sec. 3.6 here). No penetration/contact-force instrumentation; "task completion score" and "success rate" are the only physical-interaction metrics, both human-graded/rubric-based (Appendix B, not read in this pass) rather than measured contact/penetration — flag if the survey needs contact-quality data from this paper, as it is not present in the parsed sections reviewed.
