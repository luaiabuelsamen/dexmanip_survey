# clutterdexgrasp_2025 — ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (Chen et al., CoRL 2025)

sources: papers/md/clutterdexgrasp_2025.md [sha256 5c24e6cc] ; (no code)

## One-line contribution
A teacher-student pipeline (PPO teacher with a hand-to-object distance representation and a two-stage curriculum, distilled into a point-cloud DP3 student) for closed-loop, target-oriented dexterous grasping in cluttered scenes, with zero-shot sim-to-real transfer (Abstract; Sec.4).

## Setting
- hand: AgiBot 6-DoF dexterous hand (6 actuated **J**_f_ + 6 underactuated **J**_u_ joints, total **J**_h_ ∈ R^12) (Sec.3, Appendix D).
- arm: RealMan RM75-6F 7-DoF arm (**J**_a_ ∈ R^7) (Appendix D). Single-arm/single-hand tabletop setup; not bimanual.
- simulator / physics: Isaac Gym [63]; timestep/solver settings not stated. N_env = 16384 during teacher training (Appendix B.1).
- compute: single RTX 4090 + i9-13900K for both stages (Appendix B.6, Table 6). Teacher: 22 GB / 8 days. Student: 22 GB / 1 day (Table 6).
- observation (teacher): privileged state — joint positions, EE pose/velocity, object pose/velocity/goal pose, geometry-spatial distance features; full 128-dim layout in Table 4 (Appendix B.2).
- observation (student): robot joint positions + partial point cloud, O_pc ∈ R^(4×5120) (Sec.3), split in Appendix C.1 into R^(4×3584) scene points, R^(4×512) synthetic ground points, R^(4×1024) synthetic robot points (3584+512+1024=5120, consistent with Sec.3).
- action space: A ⊆ R^13 = 7D relative ("delta") arm joint change + 6D absolute joint-position targets for the actuated hand joints (Sec.3). Underactuated hand joints are not directly actuated.
- objects / data: teacher trained on 88 objects from GraspNet-1Billion [61], used to build 270 training scenes (Sec.5.1).
- generalization test objects: 2029 objects from Omni6DPose [62] (Sec.5.1).
- real world: 41 objects of varied shape/size/material (Sec.5.2).

## Method
- paradigm: RL (teacher, PPO) → IL distillation (student, 3D diffusion policy / DP3 [35]) — teacher-student privileged-to-vision distillation (Sec.4; Sec.3 "Objective").
- teacher algorithm: PPO [57]. Hyperparameters (Table 5): 4096 mini-batches, 5 opt-epochs, horizon 8, hidden [1024,512,256], clip 0.2, max grad norm 1, lr 3e-4, γ=0.99, GAE λ=0.95, desired KL 0.02, ent-coef 0.0.
- student algorithm: DP3 [35], AdamW. Hyperparameters (Table 7): downsample dims [128,256,384], encoder out dim 64, horizon 4, obs steps 2, action steps 1, 100 diffusion training steps / 10 inference steps, lr 1e-4, weight decay 1e-6, cosine schedule, 500 warmup steps.
- teacher-student distillation: yes. Privileged info given only to the teacher = the geometry-and-spatial (GS) distance representation — d_pos, d_neg computed from 200 sampled target-surface points and 50 non-target-surface points per env, to 11 finger-link base positions (N_env×11×3 tensors, "6ms" compute cost, Appendix B.1) — plus full object pose/velocity/goal state (Table 4). The student never sees these; it only gets joint positions and the point cloud (Appendix C.1).
- observation vector (teacher, Table 4 / Appendix B.2): 0–19 DoF positions (J_a,J_h); 19–22 EE position; 22–25 EE orientation (Euler); 25–28 EE lin. vel; 28–31 EE ang. vel; 31–34 object→midpoint vector; 34–37 midpoint position; 37–44 object pose; 44–47 object lin. vel; 47–50 object ang. vel; 50–57 object goal pose; 57–90 d_pos (flattened); 90–123 d_neg (flattened); 123–128 fingertip-to-table height (5 values, safety).
- domain randomisation: not itemized as a list/table anywhere in the text. Sim-to-real relies instead on (a) system identification (Sec.4.2.3 / Appendix C.4 — "iteratively compares trajectories from simulation and the real world under identical commands, optimizing parameters until behaviors closely match"; exact parameters/ranges not given) and (b) point-cloud alignment via synthetic robot/ground point clouds (Sec.4.2.2, Appendix C.3). No per-parameter randomization range is given anywhere — recorded as "not stated".

## Method / Reward block (verbatim where possible — no code to cross-check)
The PDF's reward equations did not survive text extraction in the layout parse (pymupdf4llm dropped the equation images/typeset math in Sec.4.1.1 and Appendix B.3); only surrounding prose was available there. The full equations were recovered by OCR from papers/md/clutterdexgrasp_2025.ocr.md (OCR text is noisier than the layout parse, symbols may be imperfect):
- Sec.4.1.1: "where c1, c2 > 0 are weighting coefficients. Here, r_pos provides a reward term encouraging proximity to the target, while r_neg imposes a penalty for risky closeness to non-target objects, and r_grasp represents the base grasping reward."
- Appendix B.3 (quoted from OCR): "rpos = exp(−αpos ·∥dpos∥2) (5)" and "rneg = exp(−αneg · d̄min neg) (6)". "r_pos provides a positive reward that encourages the dexterous hand to approach the target object. Conversely, r_neg introduces a global penalty term based on d̄_neg^min, the minimum absolute distance to any non-target (negative) object surface observed throughout the entire grasping episode."
- r_grasp's equation (quoted from OCR): "rgrasp = c4 · c5 ·(0.2−∥pcurrent −pgoal∥2) [goal distance reward] +c6 ·exp(−αmid ·∥dmid∥2) [middle point reward] (8)"; text names its coefficients as "c1, c2, c4, c5, c6, α_pos, α_neg, α_mid > 0"; d_mid is "the 3D vector from middle-point between index finger and thumb to center of object"; p_current/p_goal are current vs. goal-lift object position. Per-timestep complete reward (quoted from OCR): "r = (c1 ·rgrasp +c2 ·rpos)·(1−rneg) (7)".
- Stage 1 (single-object, quoted from OCR): "rstage1 = c1 ·rgrasp +c2 ·rpos (9)" — GS-representation terms zero-padded in observation and reward.
- Stage 2 (cluttered, quoted from OCR): "rstage2 = r (10)" "where r is defined in Eq. 7" — same r_pos/r_neg/r_grasp form.
- Stage 3 (safety fine-tune, Sec.4.1.3 / Appendix B.3–B.4, quoted from OCR): "rstage3 = rsafe = r −c3 ·rforce (11)", "where c3 > 0 are weighting coefficients," plus sparse force penalty: "rforce = 1 if maxi(fz,i) > f, 0 otherwise, (12)" "with fz,i representing the z-direction contact force at the i-th fingertip and f being the predefined force threshold." Exceeding f̄ also triggers early termination.
(recovered by OCR from papers/md/clutterdexgrasp_2025.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect)
- **None of c1, c2, c3, c4, c5, c6, α_pos, α_neg, α_mid have numeric values anywhere in the extracted text, including the OCR pass.** This is a genuine gap that survives both extractions, not an omission on my part — there is no code release to check an implementation against, so the weight values remain unrecoverable from this source.
- key trick 1: two-stage clutter-density curriculum, single-object → clutter (Sec.4.1.2; Fig.8 shows 0% success training on clutter from scratch).
- key trick 2: interaction-safety curriculum tightening a contact-force threshold f̄ from f0=200 down to 50 (steps of 5) once a rolling success-rate average exceeds threshold w̄, gated by minimum iteration gap ΔT_min (Algorithm 1, Appendix B.4).
- key trick 3: coarse-to-fine action masking — hand DoFs frozen during approach until privileged hand-object distance d_hand < d̄=0.08, then unfrozen (Appendix B.5).
- key trick 4: hand-table collision disabled in sim, with early termination on deep table penetration (Sec.4.1.3).

## Evaluation
- exact success criterion, sim: "a trial is successful if the target object is lifted 0.1 meters" (Sec.5.1); mean±std over 3 random seeds. No hold-duration stated beyond the lift itself.
- exact success criterion, real world: Success Rate = N successfully grasped objects / N total attempts (Sec.5.2); scenes end after three consecutive failures. No explicit height/duration threshold given for the real-world criterion (only a finger-torque heuristic that *triggers* a scripted lift, Appendix E.1) — recorded as "not stated" precisely.
- AUC metric: "Area under the Curve... to evaluate the efficiency of our system," cumulative success vs. time (Sec.5.2).
- clutter-specific success clause: none stated — no "collision-free extraction" requirement folded into the success-rate definition. Collision/force is scored separately (Table 2's "Force (unit)" column, Isaac Gym default force units) via the safety curriculum, not as part of success.
- grasp-pose generation: not analytic and not a separate generative grasp-pose model — the teacher is an **end-to-end RL policy** outputting low-level joint actions (7D arm delta + 6D hand absolute targets) every timestep; no discrete "propose pose, then plan/execute" stage (Sec.3, Sec.4).
- held-out counts, seen-object generalization: 88 GraspNet-1Billion training objects (Sec.5.1) rearranged into 500 unseen layouts, ratio sparse:dense:ultra-dense = 3:4:3.
- held-out counts, unseen-object generalization: 2029 Omni6DPose test objects arranged into 550 unseen layouts, ratio 6:3:2 (Sec.5.1).
- held-out counts, real world: 41 real objects across 9 sparse + 5 dense + 3 ultra-dense scenes, 167 total grasping attempts (Sec.5.2).
- grasp quality check: **physically only, via task completion** — the 0.1 m lift in sim, an actual pick-and-attempt in the real world. No separate geometric quality check (no force-closure/antipodal metric reported). Contact force (Table 2, Fig.6) is a safety diagnostic, not a grasp-quality criterion.
- headline numbers, Table 1: teacher 91.9±0.3% seen-objects/seen-layouts; teacher unseen-layout sparse/dense/ultra-dense = 92.5±0.8 / 87.5±0.3 / 80.9±0.2; student same splits = 89.7±0.5 / 83.4±0.3 / 73.5±0.5; teacher on unseen objects (Omni6DPose) sparse/dense/ultra-dense = 92.6±0.4 / 86.6±0.4 / 81.6±0.3; student = 90.8±0.7 / 82.1±1.6 / 74.2±1.8. Text: "less than a 5% average success rate drop" student vs teacher (Sec.5.1.1).
- ablation, Table 2 (unseen layouts + unseen objects): full method 87.0±0.3% success / 43.2±0.7 force units; without safety curriculum 88.9±0.3% / 80.6±1.9 (+1.9% success but ~87% more peak force, Sec.5.1.2).
- curriculum ablation (Sec.5.1.2, Fig.8 text): training directly on clutter with no curriculum → 0% success.
- real world (Table 3): SR@20s/40s/60s = 61.8 / 79.5 / 83.9, AUC = 0.617; overall real success rate 83.9% over 167 attempts (Sec.5.2.1).
- baselines beaten: none numerically — all comparisons are internal ablations (w/o GS-representation, w/o negative representation, w/o safety curriculum, w/o density curriculum, Appendix A, Sec.5.1.2). Prior single-object work ([26],[27]) is discussed qualitatively as not extending to clutter, not re-run.
- real robot: AgiBot hand + RealMan RM75-6F arm, 41 objects, 167 attempts, 83.9% overall success (Sec.5.2, Table 3).

## Clutter-specific modeling (vs. single-object grasping)
- observation: GS representation adds a second distance channel d_neg (nearest non-target surface point per finger link, 50 sampled points) alongside the target channel d_pos (200 sampled points) (Appendix B.1).
- reward: adds r_neg, "a global penalty term based on d̄_neg^min, the minimum absolute distance to any non-target object surface observed throughout the entire grasping episode" (Appendix B.3).
- single-object fallback: for single-object scenes these clutter channels are "zero-padded" in both observation and reward (Appendix B.1; Stage 1).
- safety: the safety curriculum is presented as needed specifically because of "contact-rich interactions common in cluttered environments" (Sec.4.1.3).
- density buckets: sparse [4,8] objects, dense [9,15], ultra-dense [16,25] (Sec.5.1).

## Limitations stated by the authors
"it still faces limitations with tiny objects due to imprecise grasps caused by the sim-to-real gap and frequent occlusions by the hand and surrounding objects," needing "enhanced perception strategies—such as multi-view fusion or active vision" (Sec.7). Appendix F adds: fails on large or excessively flat objects due to hand morphology, and objects sometimes leave the arm's working range because scene generation wasn't strictly constrained to it.

## Quotable claims (verbatim, with section)
- "To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes" (Abstract).
- "training directly in clutter results in complete failure (0% success) due to complex interactions, whereas initializing from the general grasp policy achieves 87.0% success rate" (Sec.5.1.2).
- "the teacher policy without safety training achieves slightly higher success rate (1.9%), it exhibits excessive force due to risky actions such as poking, jabbing, or squeezing the object, making it unsafe for deployment" (Sec.5.1.2).
- "achieving an overall 83.9% success rate on unseen layouts with unseen objects over 167 grasping attempts, without any cluttered scene being early-stopped due to three consecutive failures" (Sec.5.2.1).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the RL-teacher/vision-student distillation section and the clutter/collision-avoidance subsection. The reward equations themselves are now recovered by OCR (Eq. 5-12 above), but the reward-weight numeric values (c1, c2, c3, c4, c5, c6, α_pos, α_neg, α_mid) are still unrecoverable from this source and there is no code repo (github: null in the bib entry) to check against — flag this note as reward-block-thin on weights if the survey cross-checks weight values against other clutter-grasping papers. No domain-randomization table exists here, unlike some single-object sim-to-real RL papers in this survey that give explicit per-parameter ranges — worth flagging as a contrast when comparing sim-to-real rigor across notes. The sim success criterion (0.1 m lift, no hold-duration check) is looser than papers that require a timed hold; note this when comparing headline success rates across papers.

## Reproducibility
- code released: no. github field is null in the bib entry; no repository link appears in the paper text (only a project website https://clutterdexgrasp.github.io/ for videos, Abstract). This note is therefore built entirely from papers/md/clutterdexgrasp_2025.md, with no code/md/clutterdexgrasp_2025.md to cross-check reward, observation, or hyperparameter claims against an implementation.
- checkpoints / assets: not stated as released.
- reproducible tables from code: none — no code exists to parse (code md: False, per `tools/show.py clutterdexgrasp_2025`).
