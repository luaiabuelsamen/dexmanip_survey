# dexterous_functional_grasping_2023 — Dexterous Functional Grasping (Agarwal et al., CoRL 2023)

sources: papers/md/dexterous_functional_grasping_2023.md [c12f68a5] ; (no code)

## One-line contribution
A one-shot DINOv2 affordance model localizes a *functional* (not just stable) pre-grasp region from a single annotated internet image per object category, then a blind proprioceptive RL policy — trained in an eigengrasp-compressed 9-dim action space distilled by PCA from human mocap hand poses — picks the object up and folds it into a firm power grasp so a 6-DoF arm can execute the post-grasp task motion (Fig. 1, 2, Sec. 2).

## Setting
- hand(s): LEAP hand [12], described only as "low-cost dexterous"; 16 joints total, 4 per digit across three fingers + one thumb (Sec. 1, Appx. C). No DoF-per-joint or vendor detail beyond the citation.
- arm: xArm6, 6 actuated joints (Appx. C). Single hand, arm-mounted; not bimanual.
- simulator / physics: IsaacGym [64] via IsaacGymEnvs; rl_games as the RL library (Appx. D). Sim timestep and contact-solver parameters not stated.
- control rate: hardware arm and hand both run at 30Hz (Appx. C); the matching sim control rate is not explicitly stated.
- scale: 8192 parallel environments, trained for 400 epochs over 5 seeds (Appx. D; Sec. 4.1). GPU and wall-clock training time not stated.
- observation: 7-dim end-effector target pose (position + quaternion) plus 16 hand joint-angle positions fed to the policy (Appx. D). Note: Appx. D calls this o_t ∈ R^16 in its own notation immediately after listing 7+16 dims — the paper's stated dimensionality is internally inconsistent; quoted as written, not corrected.
- observation/action noise: "Gaussian noise" is added to both observations and actions (Sec. 2.2, Appx. E); no noise magnitude is given.
- action space: eigengrasp-compressed, a_t ∈ R^9, m=9 PCA eigenvectors of 16-DoF mocap hand poses; raw joint angles are reconstructed as a linear combination of the eigenvectors (Sec. 2.2).
- objects / training data: policy trained only on procedurally generated hammers with randomized physical parameters (Sec. 2.2).
- objects / sim eval (Table 1): Hammer, Drill, Screwdriver — Drill and Screwdriver are out-of-distribution relative to the hammer-only training set.
- objects / real eval (Table 2): 7 objects — Hammer (heavy), Hammer (light), Saucepan, Drill (heavy), Drill (light), Stapler, Screwdriver. Only the two hammers are "quite similar to the training distribution"; drill, stapler, screwdriver, and saucepan are explicitly called out-of-distribution by geometry (Sec. 3, Sec. 4.2).
- eigengrasp mocap dataset size: described only as "a small amount of human data" / "a small dataset of hand poses" — exact trajectory or pose count not stated.

## Method
- paradigm: RL (PPO) for the blind grasp-execution policy; one-shot feature matching (not learned end-to-end) for pre-grasp localization; the post-grasp trajectory is scripted from mocap/keypoint interpolation, not learned (Sec. 2.3).
- grasp-pose generation — where: pre-grasp position/orientation is retrieved, not synthesized: DINOv2 features match a single human-annotated affordance mask onto a DETIC segmentation of the new object instance (Sec. 2.1, method of Hadjivelichkov et al. [18]); orientation is set perpendicular to the object mask's largest principal component; best of 3 orthogonal cameras is chosen by affordance-match score (Sec. 2.1, Appx. A).
- grasp-pose generation — how: the grasp joint configuration itself is produced end-to-end by RL, restricted to the PCA eigengrasp subspace. The paper is explicit that this is not a generative model: "doing PCA (as opposed to training a generative model) allows the policy to output hand poses that were not seen in the dataset" (Sec. 2.2).
- function vs. stability: the affordance mask encodes intended use, not geometric grasp quality — "by just looking at the geometry or by computing grasp metrics we could conclude that grabbing a hammer from the head or handle are both equally valid... [but] the correct usage is to grab the handle" (Sec. 2.1). Grasp quality in this paper is therefore task-appropriate contact region (function), with the RL reward separately handling grip firmness/stability.
- reward or loss (quoted, Sec. 2.2 "Rewards"): "a simple reward function that is a combination of two terms r_threshold and r_hand-obj."
  - r_threshold(t) = 𝟙[(r_obj(t))_z ≥ 0.04cm] — binary signal for object lift height.
  - r_hand-obj: described in prose as "a sum of exponentials and an L2 distance to incentivize the object to be close to the palm of the hand," with constants d1=10cm, d2=5cm, d3=1cm given in text. The equation itself is not present in the layout-parsed markdown (an inline image lost in PDF→markdown conversion), but was recovered by OCR from papers/md/dexterous_functional_grasping_2023.ocr.md (OCR text is noisier than the layout parse, symbols may be imperfect), quoted verbatim as OCR renders it (line breaks preserved since the OCR run collapses the summation notation):
    "rhand-obj(t) = [Σ, 3 over i=1] exp(−∥robj −rhand∥ / di) − 4∥robj −rhand∥"
    i.e. OCR gives a summation symbol with bounds "i=1" to "3" applied to "exp(−∥robj−rhand∥/di)" (matching the three d1/d2/d3 constants and the "sum of exponentials" description), followed by a separate "−4∥robj−rhand∥" term (matching the "and an L2 distance" description). Whether the "−4∥robj−rhand∥" term is inside or outside the summation, and whether "4" is itself an OCR misread of a different coefficient or symbol, cannot be determined from this OCR pass — quoted as-is, not reconstructed.
  - overall: r(t) = r_hand-obj(t) + 0.1·r_threshold(t) + 1 (Sec. 2.2, verbatim).
  - "Due to the eigengrasp parameterization additional reward shaping is not needed" (Sec. 2.2) — no auxiliary terms (e.g. penetration, smoothness) are reported.
- key trick 1: eigengrasp action-space reduction (16→9 dims) to constrain RL to physically realistic, self-collision-free poses and shrink the exploration space.
- key trick 2: recurrent (GRU) policy so the hand can implicitly infer joint velocity (hardware exposes no joint-velocity sensing) and adapt online to domain randomization and pre-grasp error (Sec. 4.1, Appx. D).
- key trick 3: multi-camera (3-axis) affordance voting to handle upright/arbitrarily-oriented objects (drills, mugs) (Sec. 2.1, Appx. A).

## Evaluation
- sim success criterion (Table 1): "a success is counted when the arm does not drop the object at anytime" during a fixed pickup-then-spin task — arm held near ground 1s, then spun in a circle; episode terminates early if hand-object distance exceeds 20cm (Sec. 2.2, Table 1 caption). No lift-height or hold-duration number beyond the 0.04cm threshold inside r_threshold.
- real-world success criterion (Table 2): success rate over 10 trials per object per method; the per-trial pass/fail definition itself (e.g. a specific lift height or hold duration) is not stated beyond "does not drop"/successfully "picks it up" and, for non-saucepan objects, survives a post-grasp waving trajectory (Sec. 4.2).
- affordance metric (Table 3): "pick success" (fraction of trials) and IoU between predicted and human-annotated ground-truth affordance mask, on the simulated CLIPort dataset.
- quality check: physical (does the object stay held through the spin/wave motion) for the grasping policy; geometric (IoU against a human-annotated mask) for the affordance model — the two are evaluated separately and never combined into one metric.
- headline numbers, sim (Table 1), Ours vs. best baseline: Hammer reward 327.40±11.61 / success 1.00±0.00; Drill reward 129.03±22.58 / success 0.23±0.16; Screwdriver reward 211.13±11.14 / success 0.95±0.10. Baselines (Unconstrained 16-dim, VAE, Feed-forward) are all lower-mean and much higher-variance, e.g. Unconstrained Hammer success 0.60±0.55.
- headline numbers, real (Table 2), Ours vs. Teleop Oracle vs. Hardcoded: Hammer (heavy) 0.8 / 0.5 / 0.0; Hammer (light) 0.9 / 0.6 / 0.3; Saucepan 0.9 / 0.9 / 0.3; Drill (heavy) 0.5 / 0.9 / 0.2; Drill (light) 0.8 / 0.9 / 0.3; Stapler 1.0 / 0.9 / 0.3; Screwdriver 0.7 / 0.5 / 0.0. Ours beats the oracle on 4/7 objects, ties on Saucepan, trails on both drills.
- headline numbers, affordance (Table 3), Ours vs. CLIPort vs. CLIPSeg: Hammer (unseen) 9/10 (IoU 0.33) vs 2/10 (0.034) vs 1/10 (0.05); Spatula (seen) 8/10 (0.23) vs 6/10 (0.15) vs 2/10 (0.06); Frying Pan (seen) 7/10 (0.17) vs 7/10 (0.15) vs 1/10 (0.014).
- baselines beaten: sim — Unconstrained (full 16-dim action space), VAE (latent space of a mocap-trained VAE), Feed-forward (same method, RNN replaced by MLP); real — hardcoded pinch-grasp (open-to-closed eigengrasp interpolation over 1s), teleop oracle (Manus VR glove, one operator, 20h experience); affordance — CLIPort, CLIPSeg.
- real robot: LEAP hand on xArm6, 10 trials per object per method, 7 objects (list above), success rates as in Table 2 (Sec. 4.2). Object pose randomized per trial: orientation in [−π, π], position within 1m × 0.5m.

## Limitations stated by the authors
"While our method is robust to slight errors in pre-grasp pose if errors are large a blind grasping policy cannot recover." Proposed but unimplemented fix: "equip the robot with a local field of view around the wrist." Also: "Our method currently does not leverage joint pose information from the affordance model" — not necessary for the tested object set, but flagged as potentially needed for fine-grained manipulation of very thin objects such as coins or credit cards (Sec. 6).

## Quotable claims (verbatim, with section)
- "eigengrasp action space beats baselines in simulation and outperforms hardcoded grasping in real and matches or outperforms a trained human teleoperator" (Abstract).
- "grabbing a hammer from the head or handle are both equally valid ways of using it. However, because we have seen other people use it we know that the correct usage is to grab the handle." (Sec. 2.1)
- "doing PCA (as opposed to training a generative model) allows the policy to output hand poses that were not seen in the dataset." (Sec. 2.2)
- "Due to the eigengrasp parameterization additional reward shaping is not needed." (Sec. 2.2)
- "Note that our method also perfectly solves the training task for all seeds." (Sec. 4.1)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds: action-space-reduction / eigengrasp methods comparison; affordance-driven (functional) vs. purely geometric grasp-quality section; sim2real transfer with RNN vs. feedforward policies; low-cost-hand (LEAP) sim2real results section.

Reward block (C): the binary threshold term and the overall linear combination (r_hand-obj + 0.1·r_threshold + 1) are verbatim from the text; the exact functional form of r_hand-obj — the "sum of exponentials and an L2 distance" — did not survive PDF→markdown layout conversion (likely an inline equation image), but was recovered by OCR from papers/md/dexterous_functional_grasping_2023.ocr.md (see the "reward or loss" bullet above for the quoted, noisy OCR rendering — the grouping of the "−4∥robj−rhand∥" term relative to the summation is still ambiguous in the OCR output). There is no code to further recover or cross-check it. Flag this if the survey later compares reward-shaping density across papers.

Success criteria are looser than papers that state a numeric lift-height/hold-duration threshold: sim success is only "does not drop," real success is per-trial pass/fail with no stated physical threshold beyond the 0.04cm term buried inside the reward, not the eval criterion itself.
