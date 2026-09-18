# physhoi_2023 — PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction (Wang et al.; arXiv 2023)

sources: papers/md/physhoi_2023.md [b0079392] ; code/md/physhoi_2023.md [6095c605]

Parse caveat (updated): nearly every inline reward equation in Sec. 3.6 (Eqs. 2-11: total reward, body/object/IG/CG reward formulas and their sub-terms) rendered blank in the flattened markdown — only the surrounding prose, variable names, and Table 4's weight values survived there. All of Eqs. 2-11 have since been recovered by OCR from papers/md/physhoi_2023.ocr.md (recovered by OCR from papers/md/physhoi_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect): "rt = rb_t ∗ ro_t ∗ rig_t ∗ rcg_t" (Eq. 2); "rb_t = rp_t ∗ rr_t ∗ rpv_t ∗ rrv_t" (Eq. 3); "rp_t = exp(−λp ∗ ep_t), ep_t = MSE(sp_t, sp_t-hat)" (Eq. 4); "rr_t = exp(−λr ∗ er_t), er_t = MSE(sr_t, sr_t-hat)" (Eq. 5); "rpv_t = exp(−λpv ∗ epv_t), epv_t = MSE(spv_t, spv_t-hat)" (Eq. 6); "rrv_t = exp(−λrv ∗ erv_t), erv_t = MSE(srv_t, srv_t-hat)" (Eq. 7); "ro_t = rop_t ∗ ror_t ∗ ropv_t ∗ rorv_t" (Eq. 8, object-side analogue of Eq. 4, sharing its functional form with λop, λor, λopv, λorv); "rig_t = exp(−λig ∗ eig_t), eig_t = MSE(sig_t, sig_t-hat)" (Eq. 9); "ecg_t = |scg_t − scg_t-hat|" (Eq. 10, element-wise absolute value); "rcg_t = exp(−sum_{j=1}^J λcg[j] ∗ ecg_t[j])" (Eq. 11, where J = k(k−1)/2 is the CG edge count, ecg_t[j] a binary per-edge label error (0 or 1), λcg[j] the per-edge sensitivity weight). This confirms the exp(−error·weight) functional form quoted in the Method block below exactly, including the multiplicative (not additive) combination of all four top-level terms, matching what was inferred from code/md (`compute_humanoid_reward`) before this recovery. Code/md's `compute_humanoid_reward` function body is still truncated mid-way (cuts off after computing `ref_body_contact`, before the final CGR combination and `return` statement is shown) — the final multiplicative combination with `r_cg` is now additionally confirmed by the paper's own Eq. 2, not just its prose.

## One-line contribution
A whole-body simulated humanoid (SMPL-X, 51×3 DoF incl. 30×3 for the hands) is trained with PPO to imitate human-object-interaction references by combining a task-agnostic kinematic imitation reward (body + object + interaction-graph) with a general-purpose, aggregated Contact Graph reward that fixes a specific local optimum — "not touching the object" — that the kinematic-only reward falls into (Sec. 3.6, Fig. 7).

## Setting
- hand(s): not a robot hand — a simulated whole-body SMPL-X humanoid with 30×3 DoF hand actuators out of 51×3 total DoF (21×3 for the rest of the body) (Sec. 3.2). No separate "hand model" or vendor; the hand is part of one continuous humanoid kinematic tree, following UHC's body-generation pipeline from an SMPL-X shape parameter β (App. A.1). No arm as a separate entity — whole-body, single "hand" pair, not bimanual in the dexterous-hand sense (basketball tasks use both hands but there is no bimanual-coordination framing).
- simulator / physics: Isaac Gym (Sec. 5.1 "Implementation Details"). 2048 parallel environments, single NVIDIA A100 GPU, fixed simulation initialization; 5000 training epochs on GRAB, 15000 on BallPlay, each epoch = 10 frames of sequential simulation (Sec. 5.1). Control rates: "the simulation and the PD controller run at 60 Hz. The policy is sampled at 30Hz" (Sec. 3.9).
- observation: state-based. Simulated HOI state g_t built from `compute_humanoid_observations_max` (code): root height, local body position (root-relative, heading-rotated), local body rotation (tangent-normal 6D), local body linear/angular velocity, and net contact forces for contact bodies (`body_contact_buf`); plus object observation `compute_obj_observations` (code): local object position, 6D rotation, linear velocity, angular velocity, all root-heading-relative. State s_t = [g_t, ĥ_{t+1}] concatenates this simulated state with the next-frame reference HOI state (Sec. 3.7, Eq. in Sec. 3.7 text). Net contact forces are explicitly added "to identify contact and accelerate training" (Sec. 3.7).
- action space: target joint rotations a_t ∈ R^{51×3} for a PD controller that outputs joint torques (Sec. 3.8); policy is a Gaussian with constant variance over this action, mean from a 2-layer MLP [1024, 512] with ReLU (Sec. 3.8).
- objects / data: GRAB [92] S8 subset, 5 cases (grasping cube, cylinder, flashlight, flute, bottle) (Sec. 5.1); and the authors' own BallPlay dataset — basketball interactions (rebound, single-hand toss and catch, back dribbling, cross-leg dribble, backspin, pass, fingertip spin) (Sec. 4, Fig. 4). Raw HOI data is 30 fps mocap-style frames of human joint/root rotation+position and object position+rotation, parameterised via SMPL-X shape β∈R^10 and pose θ∈R^{51×3} (App. A.1).

## Method
- paradigm: RL only (no IL/distillation stage). Algorithm: PPO (Sec. 3.1, citing standard PPO [79]), following the ASE codebase (App. A.3: "our code is based on the ASE project [72]").
- retargeting / correspondence: the paper does not retarget a separate robot hand — the simulated humanoid IS built to match the SMPL-X mesh directly ("we build the simulation models of robots and objects to match their meshes ... following UHC", App. A.1), so there is no cross-embodiment optimization step; the humanoid's own kinematic tree is fit to the human shape/pose parameters. Not applicable in the sense of a hand-correspondence retargeting map (e.g. fingertip IK to a different DoF hand) — this is a same-embodiment humanoid tracker, not a human→robot-hand retargeting method.
- reward (paper, Sec. 3.6): "the proposed task-agnostic HOI imitation reward consists of four parts: the body motion reward r_t^b, the object motion reward r_t^o, the IG reward r_t^ig, and the CG reward r_t^cg. To obtain balanced reward values, we multiply these rewards": "rt = rb_t ∗ ro_t ∗ rig_t ∗ rcg_t" (Eq. 2, recovered by OCR — see Parse caveat above for the full Eq. 2-11 recovery and marker). Body reward "rb_t = rp_t ∗ rr_t ∗ rpv_t ∗ rrv_t" (Eq. 3, position/rotation/position-velocity/rotation-velocity sub-rewards, each "exp(−λ ∗ e)" with e a per-component MSE against the reference, Eqs. 4-7); object reward "ro_t = rop_t ∗ ror_t ∗ ropv_t ∗ rorv_t" (Eq. 8, analogous, object-side); IG reward "rig_t = exp(−λig ∗ eig_t)" (Eq. 9) from the interaction-graph MSE error; CG reward "rcg_t = exp(−sum_{j=1}^J λcg[j] ∗ ecg_t[j])" (Eq. 11) from the CG error "ecg_t = |scg_t − scg_t-hat|" (Eq. 10, element-wise absolute contact-label mismatch) with independent per-edge weights λ^cg (Sec. 3.6).

- reward (paper, Sec. 3.6, **verbatim OCR**): the summary above tidies the OCR's notation (underscored subscripts, an explicit `sum_{j=1}^J`, `-hat` for the reference marker). For the record, the equations exactly as the OCR gives them — line breaks, spacing and all, with no cleanup — are below; note that the two-line typeset subscripts come out as a stray `t` on its own line, and that in Eq. 11 the summation's Σ glyph is missing entirely, leaving only its `J` / `j=1` bounds (recovered by OCR from papers/md/physhoi_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect).

  ```
  rt = rb
  t ∗ro
  t ∗rig
  t ∗rcg
  t ,
  (2)
  ```

  ```
  rb
  t = rp
  t ∗rr
  t ∗rpv
  t
  ∗rrv
  t ,
  (3)
  ```

  ```
  rp
  t = exp(−λp ∗ep
  t ),
  ep
  t = MSE(sp
  t , ˆsp
  t ),
  (4)
  ```

  ```
  rr
  t = exp(−λr ∗er
  t),
  er
  t = MSE(sr
  t, ˆsr
  t),
  (5)
  ```

  ```
  rpv
  t
  = exp(−λpv ∗epv
  t ),
  epv
  t
  = MSE(spv
  t , ˆspv
  t ),
  (6)
  ```

  ```
  rrv
  t
  = exp(−λrv ∗erv
  t ),
  erv
  t
  = MSE(srv
  t , ˆsrv
  t ),
  (7)
  ```

  ```
  ro
  t = rop
  t
  ∗ror
  t ∗ropv
  t
  ∗rorv
  t
  ,
  (8)
  ```

  ```
  rig
  t = exp(−λig ∗eig
  t ),
  eig
  t = MSE(sig
  t , ˆsig
  t ),
  (9)
  ```

  ```
  ecg
  t = |scg
  t −ˆscg
  t |,
  (10)
  ```

  ```
  rcg
  t
  = exp(−
  J
  j=1
  λcg[j] ∗ecg
  t [j]),
  (11)
  ```
- reward (code, physhoi/env/tasks/physhoi.py `compute_humanoid_reward`): each kinematic sub-reward is an exponential of a negative weighted squared error, e.g. `ep = mean((ref_key_pos - key_pos)**2, dim=-1); rp = exp(-ep*w['p'])`, identically for rotation (`rr`), rotation-velocity (`rrv`), object position (`rop`), object position-velocity (`ropv`); combined `rb = rp*rr*rpv*rrv`, `ro = rop*ror*ropv*rorv`, `rig = exp(-eig*w['ig'])`. **Mismatch (important for "position only vs. position+orientation" question):** in code, `epv` (body position-velocity error) is hard-set to `torch.zeros_like(ep)` — always zero regardless of the true position-velocity difference — so `rpv` is always 1 no matter what `w['pv']` is; likewise the object rotation error `eor` and object rotation-velocity error `eorv` are both hard-set to `torch.zeros_like(ep)` with the true computation commented out (`#torch.mean((ref_obj_rot - obj_rot)**2,dim=-1)`), so `ror` and `rorv` are always 1 regardless of `w['or']`/`w['orv']`. **This means the object is tracked in position only in the actual reward computation, not position+orientation, despite Table 4 listing nonzero λ^or (0.1 for GRAB) and λ^orv (0.01 for GRAB) as if orientation were tracked; those weights are dead code for the reward that ran.** (For BallPlay, the paper does state this is intentional: "we do not consider the basketball rotation since it is not provided, i.e., we set λ^or and λ^orv as zero for experiments on BallPlay", Sec. 5.1 — but for GRAB, Table 4 shows λ^or=0.1, λ^orv=0.01, non-zero, yet the code's hard-coded zeroing means this weight has no effect regardless of dataset.)
- reward weights, Table 4 (App. A.3), body block [λ^p, λ^r, λ^pv, λ^rv], object block [λ^op, λ^or, λ^opv, λ^orv], IG [λ^ig], CG [λ^cg[0], λ^cg[1], λ^cg[2]]: BallPlay = [50, 20, 0.01, 0.01 | 1, 0, 0.01, 0 | 20 | 5, 5, 5]; GRAB = [50, 20, 0.01, 0.01 | 1, 0.1, 0.01, 0.01 | 20 | 50, 5, 5]. For BallPlay, λ^cg[0] (hands↔ball edge) is reduced to 0.01 for the fingertip-spin case specifically "to weak restrictions on contact between hands and the ball" (Table 4 caption).
- key trick(s): **Contact Graph (CG)** (Sec. 3.4) — a complete graph over objects + humanoid body parts with binary edge labels for contact, aggregated into a small number of nodes (3 nodes for both GRAB — table/object/whole-body — and BallPlay — object/aggregated-hands/aggregated-rest-body) to keep it tractable ("the complete CG has 154 nodes ... and 11781 edges, which is costly", Sec. 3.4). The CG reward is introduced specifically to fix a documented RL failure mode: "during the training of grasp tasks, the contact between the humanoid and the object will, in most cases, cause the object to move away from the desired trajectory and the expected return becomes smaller. In this case, the policy may learn not to touch the object and falls into a local optimal" (Sec. 3.6) — i.e., the sparse/dense kinematic reward alone is gameable by non-contact, and the CG reward is added as a second, independent measure to prevent that learned behaviour.
- contact detection implementation (App. A.3, confirmed in code): "Since Isaac Gym does not yet provide contact detection APIs for the GPU pipeline, we use force detections as approximations for contact detections." Code: `body_contact = all(abs(body_contact_buf) < 0.1)` per selected body ids (no contact ⇒ 1); `obj_contact = any(abs(tar_contact_forces[...,0:2]) > 0.1)` (contact ⇒ 1) — i.e. contact is inferred from net contact-force thresholds (0.1, units presumably N, not stated), not geometric collision/penetration detection.

## Contact / penetration handling (block D)
Interpenetration is neither measured nor penalised as a metric or reward term anywhere in the paper or code. Contact itself IS used (as a binary force-threshold signal feeding the CG reward, above), but this is presence/absence of contact force, not penetration depth or volume. The only explicit acknowledgement of interpenetration is a stated limitation: "Due to the low frame rate of HOI data and simulation frequency, some minor penetrations may appear" (App. E.2, Limitations) — no measurement, threshold, or mitigation is offered beyond noting it can happen; no contact-solver softness/stiffness parameters are given in the parsed paper or code for this key.

## Evaluation
- metrics (Sec. 5.1, exact definitions): (1) **Success rate (Succ)**, defined per frame — "success is defined per frame, deeming imitation successful when the object position and body position errors are both under the thresholds and the contact graph edge value is correct... The object threshold is defined as 0.2 m. The body threshold is defined as 0.1 m." Succ is the frame-averaged success indicator. (2) **MPJPE** for humanoid (E_b-mpjpe) and object (E_o-mpjpe), "in mm", following [60]. (3) **Contact accuracy E_cg** ∈ [0,1], "MSE(ŝ_t^cg, s_t^cg)" averaged over all N frames (lower is better despite being an "accuracy").
- failure definition during rollout: early termination on any of three conditions (App. A.2): "(1) the maximum time is reached; (2) the object deviates far from the reference trajectory; (3) the robot positions deviate from the reference. The threshold of position error is set to 0.5m." Random initialization is explicitly avoided: "We do not use random initialization since the HOI data may have severe collisions that eject the object" — fixed first-frame initialization is used instead (Sec. 3.9, App. A.2).
- object tracked position only or position + orientation: **position only in the reward that actually ran** (see Method-block mismatch above: object-rotation and object-rotation-velocity errors are hard-coded to zero in `compute_humanoid_reward`, so no orientation signal reaches the trained policy via r^o, regardless of the Table-4 weight value). The success-rate criterion (Succ) is also position-only per its stated definition ("object position and body position errors ... under the thresholds") — no orientation threshold is part of Succ.
- headline numbers (Table 2, Sec. 5.1; averaged over 10 repeats of all sequences): GRAB — PhysHOI Succ 95.4% vs. DeepMimic* 27.0% vs. Zhang et al.* 38.6%; E_o-mpjpe (mm) PhysHOI 78.0 vs. DeepMimic* 180.2 vs. Zhang* 180.1; E_cg PhysHOI 0.026 vs. DeepMimic* 0.7240 vs. Zhang* 0.3370 (PhysHOI does not win E_b-mpjpe: DeepMimic* 44.7 vs. PhysHOI 71.1, "DeepMimic achieves the best score in body motion metrics ... since it only learns human motions" but fails to control the object). BallPlay — PhysHOI Succ 82.4% vs. DeepMimic* 7.5% vs. Zhang* 13.6%; E_o-mpjpe PhysHOI 82.9 vs. DeepMimic* 1662.5 vs Zhang* 155.3; E_cg PhysHOI 0.0877 vs. DeepMimic* 0.3063 vs Zhang* 0.4124.
- ablation (Table 3, Sec. 5.2): CGR (r^cg) turned on vs. off across 4 BallPlay sequences — e.g. Backspin Succ 0.2% (kinematic only, i.e. neither r^ig nor r^cg) → 21.7% (+r^ig) → 70.3% (+r^cg); Pass Succ 4.8% → 16.2% → 71.2%. The paper's own framing: "the contact graph reward r_t^cg significantly improves the overall performance, especially the success rate" (Table 3 caption).
- baselines beaten: re-implemented DeepMimic [69] (additive reward, incl. added object motion reward), AMP [71] (reference-state swapped for the paper's contact-aware HOI representation), and a "simplified version of Zhang's method [122]" via the paper's own interaction-graph definition (code unavailable for [122], App. A.3). All are re-implemented by the authors, not independently re-run by a third party.
- real robot? none — pure simulation (Isaac Gym); the paper explicitly flags real-world humanoid/robot deployment as future work: "building a real humanoid with 153 DOF seems far away" and suggests instead "retargeting-based HOI Imitation, e.g., teaching a robot arm with a dexterous hand to play basketball via HOI Imitation" (App. E.3) — i.e. this paper's own hand is not a real robot hand, and it names hand-retargeting to a real dexterous hand as unrealized future work.

## Limitations stated by the authors (App. E.2)
- Fails under severe reference-data bias (e.g. ball drop in the rebound case, Fig. 14).
- CG nodes not detailed enough causes local optima on subtle operations — "fingers should be independent CG nodes when learning complex in-hand manipulations."
- "Due to the low frame rate of HOI data and simulation frequency, some minor penetrations may appear."
- Single-frame reference object state insufficient for long-horizon hands-off control (e.g. ball after a jump shot leaves the hand); multi-frame reference states suggested as a fix.
- No generalization across HOI types not trained on: "the policy trained on back dribble can not handle fingertip spin."

## Quotable claims (verbatim, with section)
- "the policy may learn not to touch the object and falls into a local optimal" (Sec. 3.6).
- "Since Isaac Gym does not yet provide contact detection APIs for the GPU pipeline, we use force detections as approximations for contact detections." (App. A.3)
- "Due to the low frame rate of HOI data and simulation frequency, some minor penetrations may appear." (App. E.2)
- "We do not use random initialization since the HOI data may have severe collisions that eject the object." (Sec. 3.9)
- "the humanoid learns the correct contact and avoids the local optimal of kinematic rewards" (Sec. 5.2)

## Reproducibility (block F)
Code released: yes (github.com/wyhuai/PhysHOI, commit 6095c605, per this survey's code manifest). README (code/md) documents pre-trained models and an inference/evaluation entry point plus a training entry point (`## PhysHOI`, `### Pre-Trained Models`, `### Inference`, `### Training` — code/md lines 53-113), so checkpoints appear to be released alongside code. The BallPlay dataset itself is released as a named contribution (Sec. 4; code/md `### The BallPlay dataset`). Of the parsed code, `compute_humanoid_reward` and the observation builders (`compute_obj_observations`, `compute_humanoid_observations_max`, `build_hoi_observations`) are present and match the paper's described reward/observation structure closely enough to reproduce Table 2's reward computation, modulo the object-orientation zeroing noted above; the reset/termination function `compute_humanoid_reset` is only a signature in code/md (body not extracted), so the 0.5 m termination threshold cannot be cross-checked against code from this parse alone.

## Notes for the survey
- Feeds: the contact-graph reward mechanism is a direct ancestor/citation source for DexTrack-style trackers that inherit "reward form" from contact-aware imitation (per the bib entry's own framing: "the reward form DexTrack-style trackers inherit"); useful as the origin point for the survey's discussion of multiplicative kinematic+contact reward composition and the "policy learns not to touch" failure mode that motivates contact-specific reward terms across this batch.
- Important correction to carry into any cross-paper reward table: PhysHOI's own code does not track object orientation in its actual reward, despite the paper's reward formula nominally including r^or and r^orv and Table 4 listing a non-zero λ^or for GRAB — the survey should list PhysHOI as "position-only, orientation term present in formula but zeroed in code" rather than "position + orientation," to avoid overstating what the reward that produced Table 2's numbers actually optimised.
- Contact is operationalized purely as a binary, force-threshold-derived label (not a geometric penetration or overlap measure) — good contrast case for the survey's interpenetration section: this paper's "contact" reward is orthogonal to (does not measure or bound) interpenetration; the two are conflated in the abstract discourse of "contact-aware" methods but are functionally distinct in this implementation.
- The humanoid here is SMPL-X-shaped, not a robot hand asset — flag this when the survey aggregates "hand model" across papers; PhysHOI has no vendor hand, no arm, and does not address hand-object retargeting to a non-human embodiment (explicitly deferred to future work, App. E.3).
