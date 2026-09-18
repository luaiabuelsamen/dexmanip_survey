# arctic_2022 — ARCTIC: A Dataset for Dexterous Bimanual Hand-Object Manipulation (Fan et al., CVPR 2023)

sources: papers/md/arctic_2022.md [0ca69d38] ; code/md/arctic_2022.md [49f3eb4b]

## One-line contribution
Marker-based mocap (54 Vicon cameras) plus 9 synchronised RGB views of 10 subjects manipulating 11 one-DoF articulated objects with both hands: 339 sequences, 2.1M images, SMPL-X/MANO and articulated-object meshes with per-vertex binary contact, and two benchmark tasks (consistent motion reconstruction, interaction field estimation) with the contact-deviation and motion-deviation metrics.

## Capture setup (Sec. 3.2, App. 1-2)
- mocap: "Vicon MoCap system with 54 infrared Vantage-16 cameras" (Sec. 3.2); "small hemispherical markers with 1.5mm radius on the hands and objects ... placed on the dorsal side of the hand"; body markers 4.5 mm radius (App. Fig. 2). Full body tracked "as they provide more reliable global rotations and translations for each hand" (Sec. 3.2).
- cameras: "8 static allocentric views and 1 moving egocentric view at 30 FPS" (Sec. 3.2); the egocentric camera carries markers (App. 2.1).
- gloves: none; markers only.
- templates: subjects scanned with a 3dMD scanner, SMPL-X registered and unposed to a personalised T-pose template (App. 2.2); objects scanned with an Artec hand-held scanner and split into two parts in Blender (Sec. 3.2).
- fitting: MoSh++ marker-to-vertex correspondence, SMPL-X pose optimised to markers; object 6D base pose from rigid transform of base markers, 1D articulation from marker projection onto the estimated axis (median over markers), axis from least-squares circle fits refined by a cost over the sequence (Sec. 3.2, App. 2.3).

## Scale
- subjects: 10 (5 female / 5 male) (Sec. 3); split 8 train / 1 val (male) / 1 test (female) (Sec. 4).
- objects: 11 articulated, each "two rigid parts that rotate about an axis" (App. 1): notebook, box, espresso machine, waffle iron, laptop, phone, capsule machine, mixer, ketchup bottle, scissors, microwave (App. Table 2). Some are toys "not to scale" (App. 6).
- sequences: 339 (Sec. 3; App. Table 1 per subject: 34, 37, 38, 31, 34, 36, 29, 42, 37, 21). Intents: "use" 1.7M images, "grasp" 457K images (Sec. 3; App. Table 2 says 0.4M).
- frames: "2.1M RGB images" over 9 views; "The average sequence length is 698 frames (view-agnostic), corresponding to 23.3 seconds" (App. 1). Derived, not stated: 339 x 698 = ~237k view-agnostic frames = ~2.2 hours at 30 FPS.
- protocol splits (App. Table 3): allo 1.5M train / 202k val / 195k test images; ego 1.7M / 25k / 24k.

## Annotations
- hands: MANO [53] (theta in R^48 with global orientation, beta in R^10, 778 vertices) and full-body SMPL-X (Sec. 5.1, 3.2). "MANO contains no wrist articulation", hence SMPL-X (Sec. 3.2).
- object: 7-D articulated pose Omega = (omega in R, R_o in R^3, T_o in R^3) (Sec. 5.1) on the scanned two-part mesh.
- contact: per-vertex binary labels computed "following GRAB [65]" between the two hands and the two object parts treated as "four watertight meshes"; "under-shooting" by proximity, and when "there is interpenetration between two meshes, for example, the thumb goes through a thin structure, the vertices of the thumb that 'over-shoot' the thin structure are labeled as in contact as well as the vertices that are inside the structure" (App. 2.4). Contact threshold for metric purposes: "< 3mm distance in ground-truth" (Sec. 4).
- rendered depth and segmentation masks available (App. 1; README).
- two hands and object jointly captured: yes — same marker system, same frames, full body included; "the only dataset that contains both hands, the full human body (in SMPL-X) and articulated objects" (Sec. 3.1).

## Metrics defined (Sec. 4, verbatim where the converter kept the text)
- "Contact Deviation (CDev): For a frame, suppose {(h_i, o_i)}_{i=1}^{C} are C pairs of in-contact hand-object vertices (< 3mm distance in ground-truth), and {(h^_i, o^_i)} are the corresponding predictions. CDev is defined as the average distance between h^_i and o^_i in millimeters: (1/C) sum_i ||h^_i - o^_i||" (Eq. 1). "This metric reflects how much the hand vertices deviate from the supposed contact vertices on the object in the prediction."
- "Motion Deviation (MDev)": for each longest stable-contact window (i, j, m, n) where hand vertex i and object vertex j stay "within a threshold alpha for every frame in the window", the disagreement between per-frame displacements delta h^_i^t and delta o^_j^t; "we only consider longer motions by using windows with at least 0.5 second or 15 frames (i.e., n - m + 1 >= 15) and we choose alpha = 3mm"; averaged over windows. Formula dropped by the converter.
- "Acceleration Error (ACC)": in m/s^2, root-subtracted, centred difference with stencil w = 1/30 s; "previous methods [34, 87] computing the acceleration errors did not divide the error by w^2, leading to significantly smaller errors" (App. 4.1).
- MPJPE (mm, 21 joints, root-relative); "Average Articulation Error (AAE)"; "Success Rate": percentage of object vertices with root-relative L2 error "less than 5% of the object diameter"; "Mean Relative-Root Position Error (MRRPE)" between roots of l, r, o.
- Interaction field: F^{a->b} in R^{V_a}, per-vertex shortest distance to the other mesh; "average distance error" in mm and its acceleration error (Sec. 4, 5.2).
- No interpenetration-depth or penetration-volume metric is defined; interpenetration enters only through the GRAB-style contact labelling (over-shooting) and the Sec. 4 remark that reconstruction "requires precise hand-object 3D alignment".

## Benchmark tasks and headline numbers
- Task 1, consistent motion reconstruction; Table 2 (CDev_ho mm / MRRPE_rl/ro mm / MDev_ho mm / ACC_h/o m/s^2 / MPJPE_h mm / AAE deg / Success %):
  - allo test: ArcticNet-SF 41.6 / 52.4/37.5 / 10.4 / 5.7/7.6 / 21.5 / 5.4 / 71.4; ArcticNet-LSTM 38.9 / 49.2/37.7 / 9.3 / 5.0/6.1 / 21.5 / 5.2 / 73.5.
  - ego test: ArcticNet-SF 44.7 / 28.3/36.2 / 11.8 / 5.0/9.1 / 19.2 / 6.4 / 53.9; ArcticNet-LSTM 43.3 / 31.8/35.0 / 8.6 / 3.5/5.7 / 20.0 / 6.6 / 53.5.
  - per-object (App. Table 6, test): CDev ranges 25.6 (scissors) to 60.8 mm (microwave); success 50.1 % (scissors) to 88.2 % (box).
  - CDev as a training loss (App. Table 8, SF, val): CDev 49.0 -> 41.9 mm, MDev 11.9 -> 10.4 mm.
- Task 2, interaction field estimation; Table 3 (avg distance error mm hand->obj / obj->hand, ACC): allo test InterField-SF 9.0/10.0, 2.7/2.7; InterField-LSTM 8.7/9.1, 1.9/1.9; ego test InterField-LSTM 8.0/9.1, 1.8/1.8.
- Baselines: ArcticNet-SF/LSTM (CNN encoder, MANO + articulated-object decoders, weak-perspective camera), InterField-SF/LSTM (PointNet on image-feature-augmented canonical vertices) (Sec. 5). No prior methods compared.
- real robot: none; a perception dataset.

## License and access
- README: "Licensing: ARCTIC data and software are not available for commercial use." and "See [LICENSE](LICENSE)" (file contents not in the md); download requires "Register ARCTIC Account" at arctic.is.tue.mpg.de/register.php; "MoCap can be downloaded now" (2023.12.20); leaderboard at arctic-leaderboard.is.tuebingen.mpg.de; ECCV'24 HANDS challenge for template-free reconstruction.
- "Subject data was collected with written, prior, informed consent and the data collection was reviewed by the university ethics board." (App. 6)
- Objects purchasable: `docs/purchase.md` (README, 2024.11.27).

## Limitations stated by the authors (App. 6)
- "Known object models in ArcticNet"; "Some of our objects are toys, which are not to scale"; "the human geometry does not capture skin deformation during contact"; markers "potentially introducing label noise"; all objects are 1 DoF.
- Test-split ground truth is not released (ArtiGrasp re-splits train+val for that reason; artigrasp_2023 Sec. 6.1).

## Quotable claims (verbatim, with section)
- "the first large-scale dataset of two hands that dexterously manipulate articulated objects, with multiview RGB images paired with accurate 3D meshes" (Sec. 1).
- "Existing hand-object datasets [8,22,23,37,41] are captured with 1-8 commodity RGB-D cameras, which is insufficient to eliminate occlusion. As a result, their hand-object motion is often slow and they mainly focus on grasping interaction." (Sec. 3.1)
- "ARCTIC has higher contact likelihood in the palm region than other datasets" (Sec. 3.1).

## Notes for the survey
- Feeds: two-hand HOI datasets table; source of references for ArtiGrasp, DexMachina, ManipTrans and BiDexHD-style retargeting; the CDev/MDev metric pair is the closest thing in the corpus to a contact-consistency measure for reconstructed (not simulated) motion.
- Contact labels inherit GRAB's over-shooting convention, so ARCTIC ground truth itself contains hand-object interpenetration that is labelled as contact rather than removed; ArtiGrasp notes "noisy hand pose references from ARCTIC" and poorly labelled index fingers (artigrasp_2023 App. C.2).
- Used or cited by (word-boundary grep over papers/md and code/md): an_dexil_survey_2025, artigrasp_2023, bidexhd_2024, bimangrasp_2024, dexmachina_2025, gigahands_2024, hot3d_2024, maniptrans_2025, oakink2_2024, rp1m_2024, taco_2024, zhao_dexhand_survey_2026. README "Projects that use ARCTIC" adds ArtiGrasp, GeneOH Diffusion, Text2HOI, QuasiSim, InterHandGen, Get a Grip, SMPLer-X (outside the corpus).
