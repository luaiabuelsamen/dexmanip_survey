# being_h0_2025 — Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Luo et al., arXiv 2025)

sources: papers/md/being_h0_2025.md [sha256 45da27c6] ; code/md/being_h0_2025.md [commit ae92e46f]

## One-line contribution
`Physical instruction tuning`: pretrain an autoregressive VLA to generate discretized MANO hand-motion tokens from large-scale human video (`UniHand`, 11 sources), then post-train a small MLP action head on top of that backbone with 50-100 real teleop trajectories per task to drive a 7-DoF Franka arm + 6-DoF Inspire dexterous hand.

## Setting
- hand(s): pretraining representation is the parametric **MANO** hand model (no physical hardware; §4.1.2). Real-robot end-effector: **6-DoF Inspire hand** on a **7-DoF Franka Research 3** arm (§6.1.3, "Robot System").
- simulator / physics: none used for training or eval — human video pretraining plus real-robot post-training/eval. No simulator is named anywhere in the paper.
- observation: pretraining — RGB image (dynamic-resolution tiled patches, InternViT-300M encoder) + text instruction (§4.1.1, §4.1.3). Post-training/robot control — "an egocentric RGB image and robot proprioception" (§6.1.3) fed through a proprioceptive projector `f_p` combined with visual-text tokens into context `ctx` (§4.3).
- action space: pretraining output is discrete **motion tokens** decoded to MANO parameters (not robot actions). Post-training output is "end-effector poses and dexterous hand joint positions" (§6.1.3) produced by a regression head `f_r` over learnable query tokens (§4.3); not stated whether these are position targets or deltas.
- objects / data: `UniHand` — 11 aggregated benchmarks, >440K task trajectories, >130M frames, >1,100 hours, >165M generated motion-instruction pairs (Table 1, §5.1); a balanced 2.5M-sample subset `UniHand-2.5M` used for pretraining. Post-training: real-robot teleop, "50-100 teleoperation trajectories" per task (§6.1.3).

## Method
- paradigm: autoregressive VLA pretraining (next-token prediction over vision/text/motion tokens) → non-autoregressive MLP-based action-head post-training via imitation learning (§4.1, §4.3). No RL, no diffusion, no flow-matching.
- backbone VLM: **InternVL3** architecture (§4.1.1): "a pre-trained InternViT-300M as the visual encoder and a 2-layer MLP as the projector." Three backbone scales are trained: **1B, 8B, and 14B** parameters (§6.1.1; code README Model Checkpoints table: "Being-H0-1B-2508 ... 1B", "Being-H0-8B-2508 ... 8B", "Being-H0-14B-2508 ... 14B"). Figure 2 shows the LLM decoder as "InternLM3 / Qwen2.5."
- hand-pose representation (quoted, §4.1.2): "We use the 3D model MANO [139] to represent hand pose, which is parameterized as m = {θ, r_rot, τ, β}." Five feature variants are compared (MANO-D51/D99/D109/D114/D162); the paper "choose[s] MANO-D162 as the feature for hand motion," i.e. 6D rotations for θ (15×6) and r_rot (6D), translation τ, plus auxiliary joint positions j∈R^(21×3) used only during reconstruction training (joint positions "only serve as auxiliary features during the reconstruction training, while in evaluation and inference, we solely utilize the 51 dimensional parameters" — note this sentence is written under MANO-D114 but the trained default is MANO-D162+Part-Level, §6.4.1, Table 5/6).
- action head / tokenization (quoted, §4.1.2, "Grouped Residual Quantization"): "Given a motion sequence M ∈ R^(T×D), an encoder transforms it into a feature map z ∈ R^(⌈T/α⌉×d). The tokenizer then discretizes the feature map z through a multi-stage residual quantization process." This is **discrete hand-pose tokenization** (GRQ-VAE, not diffusion or flow matching), with a **part-level** split: separate wrist-code and finger-code streams (Figure 4: "<wrist_0>...<wrist_Kw> <finger_0>...<finger_Kf>"). Codebook sizes K_w = K_f = 4096, code dim d = 512, 8 RQ layers, group size n = 2, temporal downsampling α = 4 (§6.1.1). A motion block is "128 tokens per second" (§4.1.3).
- downstream action head (post-training, quoted §4.3): "we leverage the VLA backbone as a pretrained encoder, where a lightweight MLP f_p projects the dexterous hand's proprioceptive states into its embedding space... For action generation, we employ a set of learnable query tokens {q_1, ..., q_Na} that attend to these contexts within the pretrained encoder, with a regression policy head MLP f_r transforming the pretrained encoder's outputs into executable dexterous poses." This is a **regression head over learnable queries**, not the discrete-token GRQ decoder used for pretraining — the two "action" mechanisms in the paper are different (motion tokens for pretraining generation; continuous MLP regression for robot post-training).
- action chunk length / control rate: post-training loss uses chunk size N_a (§4.3, symbol only, no numeric value stated in the paper). Code (README "Evaluation" commands, code/md lines for `run_server` and `eval_policy.py`) invokes both with `--action-chunk-length 16`; the paper text does not restate this number. No control-rate (Hz) figure is given anywhere in the paper or code excerpts for either motion tokenization output (128 tokens/sec motion blocks, §4.1.3) or the real robot's execution frequency — "not stated" for robot Hz.
- reward or loss (quoted): tokenizer loss combines "reconstruction and commitment losses [28], as well as the wrist term" with weights λ1=0.02, λ2=1.0 (§4.1.2, exact loss equations originally rendered as images/not extracted as text in the md; recovered from OCR: "Lwrist = ||w −ˆw||2 2, w = [rrot, τ], (5)" and "L = Lrecon + λ1Lcommit + λ2Lwrist, (6)" — recovered by OCR from papers/md/being_h0_2025.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect). VLA pretraining loss: standard next-token cross-entropy with "Vocabulary-Level Logit Masking" (probability P=50%) and "Token-level Loss Masking" (percentile filter [15%, 95%]) (§4.1.4). Post-training loss (quoted, §4.3): "Given an expert action sequence a* = {a_i*}, we optimize the model by minimizing the L1 loss between predicted actions a and the expert data" — an **L1 imitation-learning loss** over the action chunk.
- key trick(s): part-level (wrist vs. finger) GRQ tokenization; physical space alignment (weak-perspective camera normalization, §4.2.1) and view-invariant motion distribution balancing via depth scaling + in-plane rotation (§4.2.2) to unify heterogeneous camera sources before pretraining.

## Embodiment block
- hand model + DoF + vendor: real-robot — **6-DoF Inspire hand** (vendor name "Inspire" only, no model number given); pretraining representation — MANO parametric hand (no DoF stated, standard MANO joint set).
- arm/floating base: 7-DoF Franka Research 3 arm (real robot); no arm/base modeled during pretraining (human video only).
- bimanual?: pretraining data and motion generation support both single- and dual-hand ("hand_mode ... left, right, or both", code README); real-robot manipulation tasks (Table 7) are not stated as bimanual — described only as single dexterous hand + arm.
- simulator + version: none stated; no simulation is used anywhere in the paper for training or evaluation.
- physics engine: not applicable / not stated.
- sim timestep and control rate: not stated (no sim). Real-robot control rate (Hz): not stated in paper; action-chunk-length=16 only appears in the code's example commands, not in the paper text.
- number of parallel envs: not applicable (no sim envs; real robot only).
- GPU used and wall-clock training time: "training on 32 NVIDIA A800-80G GPUs" (§6.1.1); wall-clock time not stated.

## Learning block
- paradigm: autoregressive discrete-token VLA pretraining (human video) → imitation-learning (L1 regression) post-training on real teleop data.
- algorithm and implementation: next-token prediction with dual-level masking (vocabulary-level logit masking + token-level loss percentile filtering, §4.1.4); post-training regression head trained end-to-end with L1 loss (§4.3). No RL algorithm used.
- teacher-student / distillation: none described; not a privileged→vision distillation setup.
- observation vector: pretraining — image (448×448 scene image, dynamically tiled patches) + text instruction, tokenized (§6.1.1, §4.1.3). Post-training — "egocentric RGB image and robot proprioception" (§6.1.3); exact proprioception vector fields not itemized in the paper text, and the code excerpt only shows the class signature `State_Acton_Transform` (`norm`/`denorm`) with no body (code/md, `state_action_norm.py`) — cannot confirm exact fields from code.
- action space and whether position/torque/residual: "end-effector poses and dexterous hand joint positions" (§6.1.3); not stated whether joint positions are absolute targets or deltas.
- domain randomisation: none stated; real-robot evaluation instead uses "randomized initial object positions" across 20 trials per task (§6.1.3) — this is trial-position randomization, not training-time domain randomization, and no ranges are given.

## Reward / objective block
- tokenizer objective (§4.1.2): reconstruction loss + commitment loss [28] + wrist-specific term, combined with weights "λ1 = 0.02, λ2 = 1.0" (§6.1.1); exact term is described in text as "we introduce a wrist-specific reconstruction loss term to the overall quantization objective" — the underlying equations, quoted verbatim from the OCR pass: "Lwrist = ||w −ˆw||2 2, w = [rrot, τ], (5)" and "L = Lrecon + λ1Lcommit + λ2Lwrist, (6)" (recovered by OCR from papers/md/being_h0_2025.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect). The residual-quantization step equations (3)-(4) — r0 = z(g)_i, ql = arg min_{c∈C(g)} ||r_{l-1} − c||^2, r_l = r_{l-1} − q_l, and ẑ(g)_i = Σ_{l=1}^L q_l — are likewise present in the OCR pass but were not part of the original "lost" claim.
- VLA pretraining objective: standard next-token cross-entropy over motion+text+vision tokens, restricted by the two masking strategies above (§4.1.4); "The final motion loss is computed as the mean over the masked losses."
- post-training objective (quoted, §4.3): L1 loss "between predicted actions a and the expert data," i.e. behavior cloning with no auxiliary term, no penetration term, no contact term.
- code confirmation: `beingvla/models/vla/config.py`'s `BeingVLAConfig.__init__` signature includes a `loss_func` argument (code/md, "Config files"/"Python signatures" section) but the function body implementing it is not included in the code/md excerpt — cannot verify from code whether extra loss terms exist beyond what the paper states. This is a **paper/code gap**: the actual action-head module (queries q_i, f_p, f_r) referenced in §4.3 is not present in the parsed code/md at all; only config classes and a training mixin skeleton are shown, and the repo's own TODO list marks "Training code and scripts" as unreleased (code/md README "TODO" section: "- [ ] Training code and scripts.").

## Contact / penetration handling
Not addressed. The only contact-related content is the use of "contact states" as a semantic label in the video-instruction annotation pipeline (§5.2.2: per-second annotations "detail contact states, object attributes, hand parts, and motion trajectories"), used purely for generating text captions/instructions — not as a physical penalty, measurement, or solver setting. No contact solver, interpenetration metric, or penetration term appears anywhere in the paper or code excerpts.

## Evaluation block
- Hand-motion-generation evaluation (§6.1.2): held-out 5% of `UniHand` videos, split into a "head split" (held-out EgoDex) and "tail split" (TACO, HOI4D, H2O, OakInk2). Metrics: MPJPE, MWTE, PA-MPJPE, M2T R@3 / T2M R@3, FID (defined in §6.1.2). Headline numbers, Table 3: `Being-H0`-14B visual-grounded generation MPJPE 6.87 cm (head) / 8.11 cm (tail) vs. GR00T N1.5 baseline 9.82 / 15.35 cm. Table 2: generation validity rate `Being-H0`-14B = 100.0% vs. `Being-H0`-1B = 64.8%.
- Dexterous-manipulation evaluation (§6.1.3, Table 7): 7 real-world tasks — `Pick-Place-Toy` (Seen/Unseen/Clutter sub-scenarios), `Close-Toolbox`, `Close-Lid`, `Pour-Cup`, `Unfold-Clothes`. "Each task undergoes 20 randomized trials with varied initial object positions." Success criterion: "strict binary criteria (e.g., complete lid closure, accurate toy placement)." Baselines: GR00T N1.5 and InternVL3 (same architecture, no hand-motion pretraining), "All models receive identical post-training on the same teleoperation datasets."
- Headline success rates (%, Table 7, out of 20 trials each):
  | Task | GR00T N1.5 | InternVL3 | Being-H0 |
  |---|---|---|---|
  | Pick-Place-Toy (Seen) | 75 | 55 | 75 |
  | Pick-Place-Toy (Unseen) | 40 | 55 | 65 |
  | Pick-Place-Toy (Clutter) | 50 | 50 | 60 |
  | Close-Toolbox | 80 | 50 | 85 |
  | Close-Lid | 50 | 25 | 60 |
  | Pour-Cup | 90 | 55 | 100 |
  | Unfold-Clothes | 60 | 45 | 75 |
- Data-efficiency ablation (Figure 13, §6.6): Being-H0 at 25% teleop data ≈ InternVL3 baseline at 100% data on `Pick-Place-Toy`; on `Close-Lid` baseline is "0% success rate" at 25% data vs. Being-H0 "15% success rate" (quoted numbers from text, not a table).
- baselines beaten: GR00T N1.5 (only large-scale VLA "pre-trained on egocentric human videos with a focus on dexterous manipulation," per the paper's own baseline-selection rationale, §6.1.3) and InternVL3 (same architecture/scale, no physical instruction tuning) — both re-run by the authors with identical post-training data, not quoted from prior papers.
- real robot? Yes — see below.

**dexterous-hand-evaluated: yes**
"Our experiments are conducted using a hardware setup including a 7-DoF Franka Research 3 arm, a 6-DoF Inspire hand, and a RealSense L515 camera for RGB streaming." (§6.1.3, "Robot System"). This real 6-DoF Inspire hand is distinct from the MANO parametric hand used only for human-video pretraining representation (§4.1.2); MANO itself is never physically instantiated as a robot.

## Limitations stated by the authors
No dedicated "Limitations" section exists; limitations are folded into the Conclusion/Future Work (§7, quoted): the action-transfer method is acknowledged as simple — "we adopt a simple MLP-based projection method that employs a fixed set of learnable queries as action chunks for downstream manipulators. In future work, we aim to investigate more efficient and adaptive control transfer strategies" (§3.2/"Adaptive Robot Control Transfer"). The authors also note they "do not incorporate the interactive object modeling (e.g., 6D pose) in this version, leaving it as the future exploration" (§2, Hand Motion Generation related work) and flag missing depth/tactile/multi-sensory signals as future work (§4.2.3, §7).

## Quotable claims (verbatim, with section)
- "Can we pretrain a dexterous VLA from large-scale human videos, analogous to GPT-3, to explicitly imitate human actions and adapt to robot hands via post-training?" (§1)
- "we treat hand motion as a foreign language to facilitate seamless integration with the LMM." (§4.1.1)
- "we choose MANO-D162 as the feature for hand motion." (§4.1.2)
- "we select GR00T because it is the only large-scale VLA model pre-trained on egocentric human videos with a focus on dexterous manipulation." (§6.1.3)
- "Our experiments are conducted using a hardware setup including a 7-DoF Franka Research 3 arm, a 6-DoF Inspire hand, and a RealSense L515 camera for RGB streaming." (§6.1.3)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the "was it evaluated on a multi-fingered hand" survey question directly: yes, on a real 6-DoF Inspire hand, 20 trials/task, 7 tasks, with ablations isolating the human-video-pretraining effect (Being-H0 vs. InternVL3, identical post-training data). Caution for cross-paper comparison: Being-H0's real-robot success-rate table (Table 7) is a single-seed run per condition (no repeated-training-seed error bars reported, only 20 trial repeats per task at fixed weights) — flag this against any paper in the survey that reports multi-seed policy variance. Also flag the paper/code gap: the actual action-head module code (queries, f_p, f_r) is not in the released repo per its own TODO list ("Training code and scripts" unchecked), so the action-chunk-length=16 and any exact proprioception-vector fields come only from the inference/eval CLI examples, not from a verifiable implementation.
