# metis_2025 — METIS: Multi-Source Egocentric Training for Integrated Dexterous Vision-Language-Action Model (Fu et al., arXiv 2025)

sources: papers/md/metis_2025.md [sha256 61264b36] ; no code

## One-line contribution
A VLA for dexterous manipulation pretrained on a unified human+robot egocentric dataset (EgoAtlas), supervised with compact discretized "motion-aware dynamics" tokens, that interleaves autoregressive chain-of-thought reasoning with action generation (Sec 4.3).

## Setting
- hand(s): real-robot eval hand is a pair of Inspire 6-DoF dexterous hands on a Unitree G1 humanoid (Sec 5.1: "we use a Unitree G1 humanoid robot equipped with a pair of Inspire 6-DoF dexterous hands"). Cross-embodiment eval hand: a pair of 22-DoF SharpaWave Dexterous Hands on the "Sharpa Beta" embodiment (Sec 5.4, App. F).
- arm: Unitree G1 humanoid arms; "2*7 DoF arm joints" is the arm DoF used to match baselines' action space (App. E). single/bimanual: bimanual — 3 of 6 real tasks are explicitly bimanual (Grasp Two Drinks into Basket, Put Cola into Basket, Open Drawer and Put Bread; App. C), plus the cross-embodiment "Tool Use" task.
- simulator / physics: none stated anywhere — real-world only, no sim.
- observation: o_t = {I_t, S_t}, egocentric RGB image + proprioceptive state (Sec 4.1), captured by a head-mounted Intel RealSense D435 (Sec 5.1); images "center-cropped to a resolution of 480×640, and subsequently resized to 224×224" (App. D.2); proprioceptive history length = 1 (App. D.2).
- action space: unified cross-embodiment space = 18D wrist pose (3D position + 6D rotation vector per hand) + 30D finger pose (3D fingertip positions in wrist frame) (Sec 3.3, Sec 4.1); "Dexterous hand's joint angles can be mapped to fingertip positions through forward kinematics (FK)... fingertip targets predicted by the policy are converted back to joint angles via inverse kinematics (IK)" (Sec 3.3).
- objects / data: EgoAtlas, 8 sources, "343K trajectories and 89.72M image–action pairs" (Sec 3.2); downstream real tasks: 6 tasks × 100 demonstrations each (Sec 5.1).

### Embodiment block
- hand model + DoF + vendor: Inspire hand, 6-DoF ×2 (main eval); SharpaWave hand, 22-DoF ×2 (cross-embodiment eval, App. F).
- arm / floating base: Unitree G1 humanoid, dual arm; bimanual (see above).
- simulator + version / physics engine / sim timestep / #parallel envs: not applicable — no simulator anywhere in the paper.
- control rate: real-world data "collected at 30 Hz" (App. D.2); human wearable capture system "operates at 20HZ" (Sec 3.1).
- GPU used / wall-clock training time: pretraining on "a cluster of 24 NVIDIA H100 GPUs. Empirically, we find that 60k training steps are sufficient... which requires approximately 72 hours" (App. D.1); post-training uses "an 8-GPU setup with a per-device batch size of 4" (App. D.2, GPU model not restated).

## Method
- paradigm: VLA, pretrain (autoregressive discrete-token modeling) then LoRA fine-tune; paper's own framing: "integrates reasoning and acting within a unified framework" (Sec 4.3).
- algorithm: next-token cross-entropy over discretized "motion-aware dynamics" tokens (VQ-VAE for visual dynamics, RQ-VAE for motion dynamics), plus a supervised continuous-action regression head.
- reward or loss (quoted):
  - "The auto-regressive objective of METIS π is to minimize the sum of next-dynamics negative log-probabilities" (Sec 4.3) — the equation itself (Eq. 1) was an unrendered figure/image in the extracted layout-parse markdown, but is recovered from the OCR pass, which appears to have captured raw leaked LaTeX source: "\mathcal{L}_{ar} = \mathbb{E}_{o_t, l, a_{d,<i}}[-\sum_{i=1}^{N}log\; \pi_{\phi}(\hat{a}_{d,i|o_t,l,a_{d,<i}})]" (recovered by OCR from papers/md/metis_2025.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect); N = 44 tokens total, "4 for visual dynamics and 40 for motion dynamics" (Sec 4.3).
  - "The final loss is L = Lar + λLaction." (Sec 4.3, Action Decoder paragraph) — value of λ not stated.
  - Visual dynamics "quantized with the VQVAE objective" (Sec 4.2), codebook size |C_v| = 16, V = 4 tokens selected (App. B).
  - Motion dynamics "quantized using RQ-VAE... two-layer residual quantization" (Sec 4.2), codebook size |C_m| = 512, R = 40 tokens selected, decoded by a TCN (App. B). Shared codebook feature dimension d = 128 (App. B).
- key trick(s): unified fingertip-space action representation lets a policy trained on one hand transfer across hand kinematics via FK/IK — "As METIS predicts fingertip trajectories rather than direct joint angles, the policy is naturally transferable and remains unaffected by variations in hand kinematics" (Sec 5.4); adaptive reasoning/acting switch via two special tokens [BOA] and [BOD], entering reasoning "only when a subtask transition occurs" (Sec 4.3).

### Contact / penetration handling
Not addressed. No mention of interpenetration, a contact penalty term, or contact-solver settings anywhere in the paper (consistent with real-robot-only, no-sim scope).

## Evaluation
- backbone VLM: initialized from Prismatic-7B (Sec 4.3); hybrid vision encoder = SigLIP + DINOv2; LLM backbone = LLaMA-2, "7B" parameters, "decoder-only Transformer architecture with 32 sequential blocks" (Sec 4.3).
- action head (quoted formulation — autoregressive discrete tokens, not diffusion/flow-matching): "METIS first extends the LLaMA tokenizer vocabulary with |C1 + C2| special tokens... Each dynamics feature is assigned to its nearest codebook entry, and the resulting discrete index is mapped to a unique special token... enabling autoregressive supervision for training" (Sec 4.3). A separate Action Decoder (multi-head attention pooling over dynamics + visual features, proprioception via 2-layer MLP, linear projection head) then converts predicted dynamics tokens into continuous low-level actions (Sec 4.3, "Action Decoder" paragraph).
- action chunk length: main text says the decoder predicts "a sequence of actions over one second (30 future steps at 30 Hz)" (Sec 4.3), but Appendix D.2 states "we ... use an action chunk length of 32" — these two numbers disagree and the paper does not reconcile them.
- pretraining data mixture (Table 6, App. D.1, weights as stated): H2O 0.8%, OAKINK 1.9%, PH2D 5.4%, ARCTIC 2.8%, EgoDex 40.3%, Holoassist 10.6%, ActionNet 13.4%, "Our Enhanced Data" 25.4%. Per-source traj/frame counts (Table 1): ARCTIC 296 traj/214.5K frames; H2O 109/65.3K; HoloAssist 100/777.3K; Oakink 134/146K; EgoDex 314.8K/77.9M; PH2D 1.8K/416.5K (66.1% human / 33.9% robot); ActionNet 15.7K/7.4M (0% human / 100% robot, "a dataset for dexterous bimanual manipulation" per ref [8]); Ours 10K/2.8M (100% human).
- embodiments in the mixture / eval — every one named: human hands (via wearable Manus Quantum Metagloves + VIVE trackers, and via the vision-based/VR-based human datasets ARCTIC, H2O, HoloAssist, Oakink, EgoDex); ActionNet's teleoperated dexterous bimanual robot hands (100% robot, ref [8]); PH2D's mixed human/teleoperated-robot dexterous-hand data (Sec 3.2, item 3, "teleoperated robot data... human operators remotely controlling dexterous robotic hands"); the paper's own Unitree G1 + Inspire 6-DoF hands (main eval, Sec 5.1); the Sharpa Beta + 22-DoF SharpaWave hands (cross-embodiment eval, Sec 5.4/App. F). No parallel-jaw gripper embodiment is named anywhere in the mixture or evaluation — every named end-effector is a multi-fingered/dexterous hand.
- fine-tuning recipe: App. D.2 — LoRA rank 32 applied to LLM backbone and vision encoder, full-parameter fine-tuning of the action decoder only; AdamW, lr 3.5e-4, weight decay 1e-3, StepLR decayed by 0.1 after 80% of steps; LLM/vision encoder in bfloat16, action decoder in float32; 8-GPU setup, per-device batch size 4.
- metrics: "Success Rate (SR), indicating the entire task is successfully completed, and Progress Rate (PSR), capturing the average completion ratio of sub-tasks relative to the overall task in long-horizon settings" (Sec 5.1). Success criterion is a qualitative per-task description (App. C, e.g. "Success is achieved if the apple is successfully placed into the plate"); no numeric threshold (metres/seconds) is given for any task.
- trial counts: "Each task is collected with 100 high-quality demonstrations and is evaluated with 20 trials by default" (Sec 5.1); Table 2 caption: "Each experiment is evaluated with 20 trials."
- baselines: ACT, OpenVLA-OFT, π0.5, GR00T N1.5 — all re-trained by the authors on matched/adapted action spaces per App. E (own hyperparameter tables given), not quoted from their original papers.
- headline numbers (Table 2, SR/PSR, 20 trials each): Pick and Place — METIS 85.0% vs ACT 35.0%, OpenVLA-OFT 50.0%, π0.5 60.0%, GR00T N1.5 70.0%. Close Laptop — METIS 95.0% (best) vs 65.0/80.0/85.0/80.0%. Open Drawer — ACT best 95.0%; METIS 90.0%; OpenVLA-OFT 10.0%; π0.5 70.0%; GR00T N1.5 80.0%. Grasp Two Drinks into Basket — METIS best, 75.0% SR / 85.0% PSR vs ACT 25.0/40.0%, OpenVLA-OFT 40.0/57.5%, π0.5 65.0/72.5%, GR00T N1.5 65.0/70.0%. Put Cola into Basket — π0.5 best SR 75.0%; METIS 70.0% SR, ties π0.5 for best PSR at 76.7%. Open Drawer and Put Bread — METIS best, 75.0% SR / 82.5% PSR vs ACT 5.0/5.0%, OpenVLA-OFT 0.0/1.0%, π0.5 60.0/65.0%, GR00T N1.5 70.0/72.5%.
- sample efficiency (Sec 5.3, Fig. 6): "when fine-tuned with only 10% of the data, METIS still achieves a 50% success rate on the Pick and Place task" (other curve points are graphical only, not tabulated).
- OOD generalization (Table 3, "Open Drawer and Put Bread" task): unseen background — π0.5 50.0%, GR00T N1.5 65.0%, METIS 70.0%; unseen lighting — π0.5 70.0%, GR00T N1.5 65.0%, METIS 65.0%; unseen object — π0.5 65.0%, GR00T N1.5 65.0%, METIS 70.0%; cluttered — π0.5 55.0%, GR00T N1.5 60.0%, METIS 70.0%.
- cross-embodiment (Sec 5.4, Fig. 7, Sharpa Beta + 22-DoF SharpaWave hands): "85.0% success rate on the Grasp Apple into Basket task and 70.0% on the Tool Use task."
- ablations: Table 4 (pretraining source) — METIS-NoPretrain 60.0%/35.0%, METIS-HumanPretrain 70.0%/60.0%, METIS-FullPretrain 85.0%/75.0% (Pick and Place / Open Drawer and Put Bread). Table 5 (motion-aware dynamics) — w/o: 30.0%/0.0%, w/: 85.0%/75.0%.
- real robot? Yes for every number above; no simulated numbers are reported anywhere in the paper.

dexterous-hand-evaluated: yes
"For hardware platform, we use a Unitree G1 humanoid robot equipped with a pair of Inspire 6-DoF dexterous hands for fine-grained manipulation." (Sec 5.1) — corroborated by the cross-embodiment evaluation: "we employ the Sharpa Beta embodiment equipped with a pair of 22-DoF SharpaWave Dexterous Hands." (App. F)

## Limitations stated by the authors
"our model relies solely on egocentric observations, which may restrict its ability to perceive complete object geometry and fine interaction details. This limitation could be mitigated by incorporating additional wrist-mounted or external cameras." "the pretraining process currently excludes large-scale third-person data available online. Extending pretraining to broader multi-view manipulation datasets represents a promising direction for future work." (Sec 6)

## Reproducibility
Code released: no (github field in bib is null; "no code" per HOWTO — no repo to check). Checkpoints / assets: not stated. Project webpage listed (https://aureleopku.github.io/METIS) but not fetched as source. No table in this note can be independently reproduced from code; all numbers are as reported in the paper.

## Quotable claims (verbatim, with section)
- "we propose METIS, a vision-language-action (VLA) model for dexterous manipulation pretrained on multi-source egocentric datasets." (Abstract)
- "EgoAtlas spans four major categories and eight sources, all aligned under a unified action space." (Sec 1)
- "As METIS predicts fingertip trajectories rather than direct joint angles, the policy is naturally transferable and remains unaffected by variations in hand kinematics." (Sec 5.4)
- "METIS enters reasoning mode only when a subtask transition occurs, which substantially reduces inference latency." (Sec 4.3)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the VLA/generalist-policy section as a dexterous-hand VLA (not gripper-only), trained on mixed human+robot egocentric data unified into a fingertip-space action representation. The FK/IK-based cross-embodiment transfer (6-DoF Inspire hand → 22-DoF SharpaWave hand, Sec 5.4/App. F) is directly relevant to any survey comparison of cross-embodiment strategies for dexterous hands (e.g. against joint-angle-retargeting approaches elsewhere in the survey). No physics simulator, domain randomization, or contact/penetration treatment appears anywhere — mark this as real-world-only, no-sim, no-code, unlike RL-in-sim dexterous papers in this survey. Flag the action-chunk-length discrepancy (30 in Sec 4.3 vs 32 in App. D.2) if this paper's chunk length is compared numerically against other VLA notes in the survey table.
