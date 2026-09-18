# bimangrasp_2024 — Bimanual Grasp Synthesis for Dexterous Robot Hands (Shao and Xiao, IEEE RA-L 2024)

sources: papers/md/bimangrasp_2024.md [dac020a2] ; no code

## One-line contribution
BimanGrasp: a MALA-optimised energy function over two Shadow Hands (56-D) that synthesises bimanual grasps, verified in Isaac Gym into the BimanGrasp-Dataset (>150k verified grasps on 900 GSO objects), then distilled into BimanGrasp-DDPM (69.87 % success on unseen objects at rho = 500 kg/m^3).

## Setting
- hand(s): a pair of Shadow Hands, "22 actuated joints" each plus "a 6 dimensional rigid body pose"; "(22 + 6) x 2 = 56 dimensions in total" (Sec. III-C). Arm: none (floating hands). Bimanual.
- simulator / physics: Isaac Gym (Sec. III-C). "friction coefficient for both the objects and hands are fixed at 3"; "PD controller ... stiffness Kp = 1000.0 and damping Kd = 10.0"; "2.0 seconds of simulation time (i.e. 120 steps at 60 Hz)"; gravity 9.8 m s^-2. Object density rho = 2500 kg m^-3 in the main sweep (Sec. IV-A). #envs not stated; dataset synthesis "on a server with four Nvidia A40 GPUs ... 170 GB of GPU memory ... 117 minutes to generate 4,500 grasps per batch" (Sec. IV-C).
- observation: for the optimiser, the object mesh O; for the DDPM, "a feature vector O in R^1024 (extracted by PointNet from a point cloud sampled from O)" (Sec. III-D).
- action space: grasp pose = (T_l in SE(3), theta_l in R^22) for l in {1,2} (Sec. III-A); no closed-loop control, only the PD hold during verification.
- objects / data: Google Scanned Objects (GSO), 900 objects, 500 poses per object = 450k candidates (Sec. IV-A); verified subset ">150k" (Abstract). Generalisation test: 60 objects from DDG, YCB, ContactDB (Sec. IV-B).

## Method
- paradigm: stochastic optimisation (MALA) for synthesis; DDPM (U-Net, reparameterisation, Eq. 4-5) for data-driven generation. No RL.
- energy (Table I, "The minimization objective of the algorithm is the weighted sum of all terms"; d(p,q) Euclidean distance, d(p,O) = min_{q in O} d(p,q); H_l hand mesh, P(H_l) anchor points on the hand mesh; weights not given):
  - E_dis: Hand-object distance = sum_{a=1}^{n} d(x_a, O), with "n = 4000 points sampled from both hands' surfaces"
  - E_fc: Force Closure = ||G c||_2, where "c is the contact normal vector at the contact points x_j, j in {1,...,8}"; "8 contact points for grasp collaboration (4 from each hand)" build the grasp matrix G (matrix itself dropped by the converter)
  - E_vew: Wrench Ellipse Volume = sqrt(det(G G^T)^-1) [flattened; formula in Table I reads "det (GG^T)^-1 ... 2"]; "prevent the Gram matrix GG^T from being ill-conditioned"; "optimizing E_fc and E_vew establishes the differential force closure condition proposed by [12]" (Sec. III-B)
  - E_objpen: Hand-Object Penetration = sum_{l in {1,2}} sum_{p_l in P(H_l)} max(delta - d(p_l, O), 0)
  - E_selfpen: Hand Self-Penetration = sum_{l in {1,2}} sum_{p,q in P(H_l)} max(delta - d(p,q), 0)
  - E_bimpen: Inter-Hands Penetration = sum_{p in P(H_1), q in P(H_2)} max(delta - d(p,q), 0)
  - E_joint: Violation of Joint Limits = sum_{i=1}^{44} (max(theta_i - theta_i^max, 0) + max(theta_i^min - theta_i, 0))
  The text says each penetration term "is calculated with the distance between some anchor points ... unless it is lower than a fixed small threshold epsilon" while the table uses delta; the two symbols are not reconciled in the paper. Weights of the sum are never stated.
- optimiser: "Metropolis-adjusted Langevin algorithm (MALA) ... which introduces stochasticity to circumvent local optima [12]" (Sec. III-B); 10000 steps for BimanGrasp, 100 steps for DDPM post-processing (Sec. III-C/D).
- key trick(s): symmetric initialisation "on an inflated convex hull enveloping the object, with the palms facing the object", hull shrunk until contact, with randomised joint angles and poses (Step 1, Sec. III-B, Fig. 3); DDPM outputs are post-processed by 100 steps of the Table I energy because "penetrations are not explicitly considered during the generative process" (Sec. III-D).

## Physical validation (Sec. III-C and IV-A)
- "A grasp configuration is labeled as successful if the object remained in the hand for 2.0 seconds of simulation time (i.e. 120 steps at 60 Hz) over 6 evaluation trials under a gravity of 9.8 m s^-2. During each evaluation, the object and hands were randomly rotated together to verify the grasp under varying gravity force directions."
- Penetration gate: "We also checked for the three types of penetration described in Sec. III-B. If the total penetrations exceeded 1.5 mm, the grasp configuration fails the evaluation." Success requires both "1) no penetration occurs, and 2) object does not slip away during the physics verification process" (Sec. IV-A). How "total penetrations" is aggregated across the three types is not defined beyond the Table I terms.
- No separate interpenetration metric is reported as a number; penetration enters only as the 1.5 mm pass/fail gate and as the failure-mode observation "penetration remains the primary cause of grasp failure" (Sec. IV-C, Fig. 9: hand-object, self, inter-hand penetration, failure to establish contact).

## Evaluation
- metrics: grasp success rate (%) under the gate above; diameter sweep (Fig. 7, seven diameter bins, values only plotted); density sweep (Table II); friction sweep (Table III); human-likeness by "GPT-4 Vision to score each bimanual grasp on a scale of 1 to 3 points (evaluating 1,000 grasps, with 3 views per grasp). The average score obtained was 2.67" (Sec. IV-A); diversity "entropy metric H_mean adapted from [4], [26]" (Sec. IV-C).
- headline numbers:
  - Table II (all objects normalised to d = 0.2 m, 900 objects), success % at rho = 5000 / 2500 / 500: Both hands 41.02 / 54.03 / 71.42; Uni2Bim (opt) 32.87 / 45.26 / 56.69; Left Hand Only 23.38 / 41.48 / 68.42; Right Hand Only 21.85 / 41.95 / 68.48.
  - Table III (rho = 2500), success % vs friction 0.5 / 1.0 / 1.5 / 2.0 / 2.5 / 3.0: 45.40 / 47.04 / 49.32 / 51.14 / 52.4[4] / 54.03 (the 2.5 entry is split across table cells as "52.4" and "4"; read as 52.44).
  - Fig. 7: "Unimanual grasps almost entirely fail for objects larger than d = 0.5 m, while bimanual grasping remains effective for objects up to d = 0.7 m" (text only).
  - BimanGrasp-DDPM on 225 unseen GSO objects, 500 grasps each, d = 0.2 m (Sec. IV-B): "42.39% for rho = 5000 kg m^-3, 54.06% for rho = 2500 kg m^-3, and 69.87% for rho = 2500 kg m^-3" — the third value is a typo in the paper; by construction of the sweep it is rho = 500. The abstract's 69.87 % is this number.
  - Baselines at rho = 2500: CVAE 11.85 % (18 ms per grasp), Uni2Bim (dm) 36.52 % (Sec. IV-B).
  - Cross-dataset (60 DDG/YCB/ContactDB objects, d in [0.2, 0.4] m, rho = 1000): 63.23 % (Sec. IV-B).
  - Diversity: H_mean 4.39 (BimanGrasp) vs 3.72 (DDPM), H_std 0.47 vs 0.49 (Sec. IV-C).
  - Speed: DDPM "parallelize the inference of 64 grasps, with the inference time being 8.19 seconds" on an RTX 4090 (Sec. IV-C).
- baselines beaten: Uni2Bim (opt), Left/Right Hand Only (unimanual [4]); CVAE and Uni2Bim (dm) for the generator. No prior bimanual dexterous synthesis baseline exists per the authors.
- real robot? No. "We also plan to conduct experimental validations of the proposed algorithms using a real-world bimanual humanoid robot" (Sec. V).

## Limitations stated by the authors (Sec. IV-C)
- "the DDPM's grasp synthesis process does not explicitly consider penetration. Consequently, the generative model can still produce infeasible grasp poses. This issue is currently mitigated through a postprocessing step."
- "the algorithms may generate grasp poses that are not human-like."
- "penetration remains the primary cause of grasp failure. The optimization procedure occasionally fails to retract the hand from objects due to local optima."

## Quotable claims (verbatim, with section)
- "The dataset comprises over 150k verified grasps on 900 objects" (Abstract).
- "If the total penetrations exceeded 1.5 mm, the grasp configuration fails the evaluation." (Sec. III-C)
- "Note that this advantage is not solely due to the larger forces generated by more motors from two hands, but also because of the cooperation between them." (Sec. IV-A, on Uni2Bim (opt) vs Both hands)
- "When the friction coefficient was significantly reduced to 0.5, the grasp success rate decreased to 45.40% from 54.03%, indicating that around 84% of all grasps are still valid." (Sec. IV-A)
- "Our observations indicate that penetration remains the primary cause of grasp failure." (Sec. IV-C)

## Notes for the survey
- Feeds: bimanual grasp synthesis; interpenetration as a hard gate (1.5 mm total, three penetration types) rather than a reported metric; friction = 3 as a shared convention with [4], [26] (unrealistically high; BiDexGrasp uses 0.6/0.02 in MuJoCo).
- Contradiction / follow-up: bidexgrasp_2026 re-evaluates BimanGrasp in MuJoCo and reports SUC-F 26.80 % (DexGraspNet) / 30.21 % (Objaverse) with PD 1.52 / 0.87 cm (its Table 2) — far below the 54.03 % here, under different physics, friction and object sets. The only corpus paper that uses BimanGrasp or its dataset is bidexgrasp_2026 (word-boundary grep over papers/md and code/md).
- Table I energy terms with symbols but no weights: the note cannot reproduce the objective; the weights are the missing quantity for any reimplementation.
