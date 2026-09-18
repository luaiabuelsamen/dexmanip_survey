# bidexgrasp_2026 — BiDexGrasp: Coordinated Bimanual Dexterous Grasps across Object Geometries and Sizes (Lin et al., arXiv 2026)

sources: papers/md/bidexgrasp_2026.md [261cf7c6] ; no code

## One-line contribution
A two-stage bimanual grasp synthesis pipeline (GWS-based region-pair initialisation + decoupled per-hand QP force-closure optimisation, MuJoCo-validated) producing 9.53M grasps on 6,351 objects at 30-80 cm, plus a diffusion generator with a bimanual coordination module and scale-adaptive anchors (66.8 % SUC-L in sim, 74.6 % real, Table 4 / Sec. 6.6).

## Setting
- hand(s): Shadow Hand pair in simulation (Sec. 6.1); real world: Inspire and BrainCo hands, "three robotic arms (Unitree G1, Piper, and Nero)" (Sec. 6.6); Shadow grasps "retargeted [35] to the Inspire and BrainCo hands". Bimanual; dataset has tabletop IK configurations, but "our model operates in the floating-hand setting and does not use the dataset's IK configurations" (Sec. 8).
- simulator / physics: MuJoCo, "tangential/torsional friction coefficients of 0.6/0.02, gravity 9.8 m/s^2, object density 2.5 kg/m^3" (Sec. 6.1; the density unit as printed is implausible for a solid and is quoted as-is). Synthesis "on eight NVIDIA 3090 GPUs with 40 parallel worlds per GPU and 20 grasps per world" (Sec. 6.2).
- observation: object point cloud O_pc (Sec. 5); real world: single-view RGB-D crop via Grounded-SAM, or full point cloud from reconstruction [45] + 6D pose [46] (Sec. 6.6, App. G.1).
- action space: G^bi = ((t^r, r^r, q^r), (t^l, r^l, q^l)) wrist translation/rotation + joint poses per hand (Sec. 4.1); generator predicts relative wrist pose (delta t, delta r) to a scale-adaptive anchor plus q (Sec. 5.2). Execution: pre-grasp G_pre at 1 cm contact distance, squeeze pose G_squ = 2 G^bi - G_pre (Sec. 4.4).
- objects / data: "6,351 objects from [10] and [37]" (DexGraspNet + Objaverse), "scale each to 11 discrete sizes from 30 to 80 cm" (Sec. 4.1); Table 1: 9.53M grasps, max 80 cm, range 50 cm, tabletop, IK, pre-grasp. Generator trained on the DexGraspNet tabletop subset: 2,397 objects, 4:1 split, 3,112,117 training grasps; 139,956 test grasps (Sec. 6.1).

## Method
- paradigm: optimisation-based synthesis (bi-level: ReLU-QP ADMM inner solve, gradient outer loop) + DDPM generator with SmoothL1 view supervision, L2/Chamfer/physics losses. No RL.
- optimisation objective (Sec. 4.3, App. B.2). The main equation was dropped by the PDF converter in the layout parse; the text says: "we formulate the overall optimization as follows to optimize G^bi by minimizing the QP-Energy decoupled into two single-hand energy terms", i.e. Q(G^left) + Q(G^right) plus:
  - "a distance term E_dis to encourage proximity between c_{i,w} and p_i" (hand contact point i in world frame and its closest object-surface point)
  - "a region consistency term E_region to keep the contacts close to the initialized contact regions", with effective distance d_i to region R passed through "a piecewise penalty function phi(.)" with "a denoting a distance threshold, b = 2a defining the transition bandwidth, and H(t) = 3t^2 - 2t^3 being a cubic Hermite interpolation function" (App. B.2)
  - constraints: "joint limits, object contact constraints, and collision-free conditions ... we directly adopt the energy functions provided by cuRobo[48], including joint limitation energy, self-penetration energy, and inter-hand penetration energy" (App. B.2)
  - weights: "w_QP = 1000, w_dis = 100, w_region = 50" (Sec. 6.2)
  - QP-Energy (Sec. 3): "Q = sum_{j=1}^{6} min_{w_j in W} ||beta t_j - w_j||_2, where beta is a scaling factor", disturbances t_j along +-x, +-y, +-z; App. A adds a second hyperparameter gamma. "the grasp matrix is constructed by associating each c_{i,w} with its closest point p_i on the object surface" (Sec. 4.3).
  - full App. B.2 equations, quoted verbatim from the OCR pass: "min Gbi (wQP Q(Gleft) + wQP Q(Gright) + wdisEdis + wregionEregion), s.t. Gbi min ≤Gbi ≤Gbi max, ci,w = FK(Gbi, ci,l), No collision. (11)"; "Edis = m i=1 (||ci,w −pi||)2. (12)"; "Eregion = m i=1 ϕ(di), (13)"; "di =min r∈R∥ci,w −r∥, (14)"; "ϕ(d) = 0, d ≤a, H( d −a / b −a )(d −a), a < d ≤b, d −a, d > b, (15)" (recovered by OCR from papers/md/bidexgrasp_2026.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect).
  - App. A QP-Energy full form and gamma, quoted verbatim from the OCR pass: "Q ≜ 6 j=1 min fj,1,...,fj,m βtj − m i=1 Gifj,i 2 , s.t.fj,i ∈Fi, m i=1 fi,1 ≥γ, (7)", "where β and γ are two positive hyperparameters." (recovered by OCR from papers/md/bidexgrasp_2026.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect).
- initialisation (Sec. 4.2, App. B.1): FPS K_a = 200 anchors, k = 256 points within 8 cm; region pairs with inter-region distance >= tau_2 = 5 cm; stability score "s = min_{1<=j<=6} max_{1<=k<=M} t_j^T w_k" from the TDG-estimated GWB with N = 5 contacts, M = 1000 boundary wrenches; top K_r = 40 pairs kept; palm placed on the dilated convex hull facing the region, rotated to a preferred direction "(1, -1, -1) for the left hand and (1, 1, -1) for the right hand"; fingers opened on flat regions (angular variance V < tau = 0.005).
- generator losses (Sec. 5.2): "L2 losses separately to the translation, rotation, and joint parameter regressions. In addition, we incorporate Chamfer loss [42] to explicitly supervise hand geometry. We further introduce a physics-based loss to penalize hand-object penetration as well as intra- and inter-hand self-penetration." K = 16 views, K_p = 256, K_c = 16 (Sec. 6.2). Full form recovered from App. C.2 via the OCR pass, quoted verbatim: overall objective "L = λsingle-viewLsingle-view + λbi-viewLbi-view + λparaLpara + λchamferLchamfer + λphysicLphysic. (16)"; "Lsingle-view = K i=1 mi · SmoothL1(pi, yi) / K i=1 mi + ϵ (17)"; "Lbi-view = K i=1 K j=1 mi · SmoothL1(pbi i,j, ybi i,j) / K i=1 mi · K + ϵ (18)"; "Lpara = Gbi pred −Gbi gt 2 2 . (19)"; "Lchamfer = 1 |Ppred| x∈Ppred min y∈Pgt ∥x −y∥2 2 + 1 |Pgt| y∈Pgt min x∈Ppred ∥y −x∥2 2. (20)"; "Lphysic = λself-penLself-pen + λobj-penLobj-pen + λspfLspf (21)"; "Lself−pen = i̸=j max 0, δ −∥ki −kj∥2 . (22)"; "Lobj−pen = i max(0, si). (23)"; "Lspf = 1 |I| i∈I di, I = {i | di < τ}. (25)"; weights "λsingle-view = 10.0, λbi-view = 1.0, λpara = 15.0, λchamfer = 0.25, λphysic = 1.0, λobj-pen = 100.0, λself-pen = 50.0, and λspf = 50.0." (recovered by OCR from papers/md/bidexgrasp_2026.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect). Note the OCR names the third physics term "Lspf" and calls it a "Contact Loss" pulling contact points toward the object surface (Eq. 24-25), distinct from Lobj-pen — the note's original description above ("hand-object penetration as well as intra- and inter-hand self-penetration") did not anticipate this third contact-pull term.
- key trick(s): decoupled force closure "discourages single-hand-dominated solutions" (Sec. 4.3); bimanual coordination module predicts a primary view then a compatible second view via bi-view features MLP(cat(f_i, f_j, f_i - f_j, f_i * f_j)) (Sec. 5.1); scale-adaptive anchor at the intersection of the view ray with the minimum bounding sphere (Sec. 5.2).

## Physical validation and metric definitions (Sec. 6.3, App. D, verbatim)
- "Grasp Success Rate (SUC). The hand executes a grasp from the pre-grasp pose G_pre^bi to the squeeze pose G_squ^bi. A grasp is considered successful if the object's translation and rotation remain within 5 cm and 15 degrees for at least 3 seconds after execution. SUC-F evaluates force-closure success under external disturbances along six orthogonal directions. SUC-L evaluates lift success in a tabletop scenario with a floating hand. SUC-A evaluates lift success in a tabletop scenario with an arm-controlled hand."
- "Penetration Depth (PD). The maximum intersection distance between the object mesh and the hand mesh."
- "Self-Penetration Depth (SPD). The maximum penetration distance among all hand collision meshes, including both intra-hand and inter-hand self-penetrations."
- "Contact Distance Consistency (CDC). The range between the maximum and minimum signed contact distances across all fingers, reflecting the uniformity of finger-object contacts."
- "Diversity (D). The explained variance ratio of the first principal component from PCA applied to the generated grasp distribution".
- Speed (S) and SGS: raw / successful grasps per second on one RTX 3090; "baseline speeds are cited from their original reports".
- Validation set for synthesis comparison: 1,000 objects from DexGraspNet and Objaverse x 6 sizes (30-80 cm) = 12,000 instances, 5 grasps each, 60,000 grasps per method; BimanGrasp pre-grasp/squeeze obtained "by translating the palm by +-1 cm and perturbing finger joints by +-0.1 rad" (Sec. 6.1).

## Evaluation
- headline numbers, Table 2 (SUC-F / SUC-L / SUC-A / S / PD cm / SPD cm / CDC cm / D):
  - DexGraspNet: BimanGrasp 26.80 / - / - / 0.16 / 1.52 / 0.26 / 1.87 / 0.150; Ours(Float) 75.84 / - / - / 6.73 / 0.17 / 0.02 / 0.59 / 0.190; Ours(TableTop) 77.11 / 80.83 / 71.34 / 6.87 / 0.15 / 0.02 / 0.52 / 0.165.
  - Objaverse: BimanGrasp 30.21 / - / - / 0.16 / 0.87 / 0.23 / 1.38 / 0.156; Ours(Float) 70.82 / - / - / 4.55 / 0.20 / 0.04 / 0.67 / 0.180; Ours(TableTop) 62.41 / 70.41 / 62.40 / 5.10 / 0.20 / 0.05 / 0.67 / 0.158.
  - Text: "roughly 2.8x" SUC and "a 40x synthesis speedup" on DexGraspNet (Sec. 6.4); the abstract says "over 2.8x higher success rate and 30x faster synthesis".
- Table 3 (synthesis ablation, SUC-L / SUC-A / SGS / PD / SPD): Baseline (BODex extended to two hands) 28.3 / 12.9 / 2.1 / 0.18 / 0.08; +R 44.4 / 39.8 / 2.8 / 0.13 / 0.03; +R+Dc 57.7 / 49.5 / 4.0 / 0.15 / 0.03; +R+Dc+Ps 80.8 / 71.3 / 5.6 / 0.15 / 0.03.
- Table 4 (generator vs SOTA, SUC-L / PD / SPD / CDC / D): SceneDiffuser [17] 15.2 / 3.29 / 0.11 / 3.79 / 0.174; DGTR [43] 41.5 / 2.24 / 0.13 / 3.02 / 0.201; Ours 66.8 / 1.53 / 0.01 / 2.32 / 0.197. Tables 3-5 are flattened into one block in the markdown; the column assignment above follows the header order.
- Table 5 (framework ablation on a one-pose-per-object subset, 20 epochs; SUC-L / PD / SPD / CDC): none 41.2 / 2.25 / 0.01 / 2.87; BCM only(?) 44.7 / 2.28 / 0.01 / 2.96; BCM+GAF 52.7 / 2.05 / 0.02 / 2.82; all 61.9 / 1.73 / 0.02 / 2.56 (the check-mark columns are garbled; only the full-model row is unambiguous).
- real robot: "260 trials on 30 objects" with Inspire and BrainCo hands; "66.0% success on single-view and 76.7% on full point clouds, averaging 74.6%" (Sec. 6.6). Per-hand and per-arm breakdown not given.
- baselines beaten: BimanGrasp [19] (synthesis); SceneDiffuser, DGTR, a DDPM bimanual baseline (generation).

## Limitations stated by the authors (Sec. 8)
- "our synthesis pipeline assumes fixed hand contact points, which restricts the contact-space diversity of generated grasps."
- "our method is stability-oriented and may struggle on tasks requiring specific functional contacts".
- "our model operates in the floating-hand setting and does not use the dataset's IK configurations".
- Failure cases (App. F.4): "Minor object penetration or floating grasps may occur when the generative model fails to perfectly balance the penetration penalty and contact supervision"; "a small number of objects undergo lateral sliding due to insufficient force closure".

## Quotable claims (verbatim, with section)
- "comprising 6351 diverse objects with sizes ranging from 30 to 80 cm, along with 9.53 million annotated grasp data" (Abstract).
- "Bimanual grasp optimization is inherently challenging because the enlarged search space induces a tightly coupled objective that destabilizes optimization and often yields imbalanced solutions, where one hand dominates stability while the other contributes marginally" (Sec. 4.3).
- "Penetration Depth (PD). The maximum intersection distance between the object mesh and the hand mesh." (App. D)
- "We find that the common failure cases are caused by object-hand penetration and non-contact." (Fig. 10 caption)

## Notes for the survey
- Feeds: bimanual grasp synthesis; penetration metrics reported as max-depth numbers (PD, SPD in cm) rather than pass/fail gates, so the 1.52 cm PD attributed to BimanGrasp is directly comparable with the ~0.15-0.20 cm of this pipeline under the same MuJoCo evaluation.
- Contradiction with bimangrasp_2024: BimanGrasp reports 54.03 % success in Isaac Gym at friction 3 and rho = 2500 (its Table II); here it scores 26.80-30.21 % SUC-F in MuJoCo at friction 0.6 with +-1 cm/+-0.1 rad pre-grasp perturbation (Table 2). Same grasps, different physics and protocol; neither number transfers to the other.
- Success criterion (5 cm / 15 deg for 3 s after squeeze) is a hold test, not a lift-and-shake; SUC-F adds six-direction disturbances but their magnitude is not stated in the extracted text.
- Corpus usage: no other paper in papers/md or code/md mentions BiDexGrasp (word-boundary grep). Code: none in the corpus; project page is the only pointer.
