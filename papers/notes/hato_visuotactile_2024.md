# hato_visuotactile_2024 — Learning Visuotactile Skills with Two Multifingered Hands (Lin, Zhang, Li, Qi, Yi, Levine, Malik; ICRA 2025)

sources: papers/md/hato_visuotactile_2024.md [2dd43b38] ; code/md/hato_visuotactile_2024.md [3b6f4496]

## One-line contribution
HATO: Meta Quest 2 teleoperation of two UR5e arms with two prosthetic Psyonic Ability Hands (fingertip touch sensors), a 10 Hz multimodal data pipeline, and diffusion policies trained on 100-300 demos per task that complete four bimanual tasks; ablations show touch and wrist cameras matter and depth does not (abstract; Sec. I).

## Setting
- hand(s): two Psyonic Ability Hands (prosthetic, repurposed with custom PCBs); five fingers, 6 actuated DoF per hand (one per finger, two for the thumb), MCP-PIP four-bar linkage adds an underactuated DoF per non-thumb finger; six touch sensors per fingertip, 60 readings total across both hands (Sec. III.A, Fig. 3, III.C). Arms: two UR5e, 6 DoF each. bimanual.
- simulator / physics: none; real hardware only.
- observation: proprioception = end-effector pose (translation + axis-angle) per arm and finger positions; arm joint positions are recorded but "do not include the arm joint positions" in the policy input because UR5 joints "vary very unpredictably near singularity" (Sec. IV.A). Vision: three RealSense RGB-D cameras (two wrist-mounted, one fixed "head-view"), 480×640 resized to 240×320 (Sec. III.C). Touch: h ∈ R^60, raw ADC ≈ [200, 400] without contact, > 1000 on contact (Sec. III.C). Observation horizon 1 (Sec. IV.A).
- action space: 24-dim absolute joint targets — 6 per UR5e arm (IK from the desired EEF pose during teleop) and 6 per hand, normalised per-dimension to [−1, 1]; hand joint maxima [110, 110, 110, 110, 90, 120] (Sec. III.C, IV.A). Control and data at 10 Hz (Sec. III.C; code README `run_env.py --hz 10`).
- objects / data: teleoperated demos: Slippery Handover 100 demos (~6 s each), Tower Block Stacking 100 (~20 s), Wine Pouring 300 (~25 s), Steak Serving 300 (~40 s); 5-10 min operator practice per task (Sec. V). Released as `banana`, `stack`, `pour`, `steak` datasets (code README).

## Method
- paradigm: IL ; algorithm: DDPM diffusion policy [47], CNN-based, action horizon 16 from one observation, square-cosine noise schedule, 100 training diffusion steps, 15 at inference (Sec. IV.A-B). Encoders: two-layer ReLU MLP (hidden 256, out 64) each for proprioception and touch; ResNet-18 with GroupNorm per camera (no weight sharing), FC out 32 (Sec. IV.A). AdamW lr 1e-4, weight decay 1e-5, batch 128, EMA weights (Sec. IV.A).
- no reward (IL). The loss is not written out in the paper beyond "Following [47]" (DDPM denoising objective); the code md contains only class/function signatures for env.py and run_env.py and the README, so the training loss cannot be quoted from code either. Training entry point: `learning/dp/pipeline.py` with `--representation_type` in {eef, img, depth, touch, pos, hand_pos} and `--camera_indices` (code README).
- coordination of the two hands: one policy over both arms and both hands — a single 24-dim action and a single concatenated observation (both EEF poses, both hands' finger positions, all 60 touch values, three cameras) (Sec. IV.A). No explicit role assignment or relative-hand feature; roles are whatever the teleoperator demonstrated (e.g. "One hand needs to pick up the object and hand it over to the other hand", Sec. V). Teleoperation maps each Quest controller to one hand-arm pair (Sec. III.B).
- key trick(s): hand teleop by grip button → four non-thumb fingers (power grasp proportional to pressing force) and thumbstick → 2-DoF thumb, "sacrifices the ability to perform sophisticated fingergaiting" (Sec. III.B); pause-and-adjust via trigger; asynchronous remote inference with temporal ensembling of overlapping action-sequence predictions, "different from how deployment is done in [47]" (Sec. IV.B).
- interpenetration / contact: not applicable (no simulation); contact is sensed, not modelled.

## Evaluation
- metrics: task success over 10 deployment trials per policy; "pickup success" = both objects picked up (Sec. V.B, Table I caption). Learning-efficiency metric: ActionMSE on a held-out set (10 trajectories for Handover/Stacking, 20 for Pouring/Serving) (Sec. V.C). Success definitions: Handover — receiving hand holds the object and moves > 10 cm from the first hand; Stacking — two moved blocks stay stably on the yellow block after release; Serving — spatula with steak served onto the plate (Sec. V).
- headline numbers (Table I, 10 trials each): pickup 10/10 on all four tasks; task success Handover 10/10, Stacking 10/10, Pouring 9/10, Serving 5/10. Handover and Pouring policies use image + proprioception only; Stacking and Serving use image + proprioception + touch (Table I caption).
- ablations (Tables II-IV are flattened into one table in the parse; values read column-wise):
  - Table II, Block Stacking, default / rare init: Ours 10/10, 10/10; w/o Touch 10/10, 4/10; w/o Vision 10/10, 0/10.
  - Table III, Steak Serving, pickup / success: Ours 10/10, 5/10; w/o Touch 10/10, 0/10; w/o Vision 0/10, 0/10; EEF Only 0/10, 0/10. Text: ActionMSE 0.07 (w/o touch) vs 0.08 (with touch) yet 0/10 vs 5/10 success (Sec. V.D).
  - Table IV, Steak Serving cameras, pickup / success: Ours 10/10, 10/10 as printed (conflicts with Table I/III's 5/10 for the same configuration; ambiguous in the parse); w. Depth 10/10, 1/10; Only Wrist 0/10, 1/10; Only 3rd View 0/10, 0/10.
  - Fig. 6: ActionMSE saturates at ~75 demos (Stacking), ~100 (Serving), ~200 (Pouring); Fig. 8: wrist-only beats third-view-only on three of four tasks; depth gives no marked benefit and hurts on Pouring (Sec. V.D).
- baselines beaten: none external. Robotiq parallel-jaw gripper compared qualitatively in teleoperation only (Sec. V.A, Fig. 4). Concurrent work [26] (vision + proprioception) cited as lacking touch.
- real robot? yes — all results are real: two UR5e + two Ability Hands, 3 RealSense, 10 Hz, 10 trials per condition (Sec. III, V).

## Limitations stated by the authors
- "our policy is learned entirely from scratch with no pre-training, making it susceptible to appearance changes in the scene" (Sec. VI).
- No haptic feedback to the operator (Sec. VI).
- The hand mapping cannot perform finger gaiting (Sec. III.B).
- ActionMSE "cannot fully capture how well the diffusion policy fits the dataset distribution" (Sec. V.D).
- Steak Serving reaches only ~50 % "due to its long task horizon and the demand for high-precision control" (Sec. V.B).

## Quotable claims (verbatim, with section)
- "To the best of our knowledge, our work is the first at the intersection of bimanual dexterous manipulation and imitation learning from visuotactile inputs." (Sec. II)
- "From only 30 minutes to 2 hours of teleoperation data collected using HATO (including around 5 to 10 minutes of practice time), we are able to obtain dexterous bimanual manipulation policies" (Sec. I)
- "Without touch or vision, the policies are not able to consistently succeed or sometimes completely fail" (Sec. I)
- "even though the ActionMSE metric is similar for the policies trained with or without touch (0.07 vs 0.08), these policies have vastly different success rates: 0/10 (without touch) vs. 5/10 (with touch)" (Sec. V.D)
- "adding depth does not provide a marked benefit in terms of the ActionMSE metric, sometimes even hurting performance" (Sec. V.D)

## Notes for the survey
- Feeds: bimanual dexterous IL on real hardware; tactile sensing; low-cost teleop for multifingered hands; demo-count scaling.
- Same first author and hardware family as twisting_lids_2024 (Allegro there, Ability here; UR5e both): one lab's RL-sim-to-real vs IL-from-teleop answers to the same bimanual question.
- Effective hand DoF is 6 per hand with a 2-button mapping, so "multifingered" here means power grasp + thumb, not in-hand dexterity; compare against Allegro/LEAP/Inspire RL work before treating success rates as comparable.
- No simulation, no contact model, no penetration question; the survey's interpenetration section cannot draw on this paper except as evidence that touch sensing substitutes for contact modelling on the real system.
- Trial counts are small (10 per condition); the Table IV / Table I inconsistency on Steak Serving should be checked against the PDF before quoting.
