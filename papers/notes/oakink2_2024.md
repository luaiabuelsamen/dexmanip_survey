# oakink2_2024 — OAKINK2: A Dataset of Bimanual Hands-Object Manipulation in Complex Task Completion (Zhan et al., CVPR 2024)

sources: papers/md/oakink2_2024.md [1f3a28b3] ; code/md/oakink2_2024.md [502a0280] (oakink2_toolkit: loaders, preview GUI, dataset format; no annotation pipeline)

## One-line contribution
Mocap-annotated (12 OptiTrack cameras, 4 RGB views) long-horizon bimanual manipulation: 627 sequences, 4.01M frames, 9 subjects, 75 objects, organised as Affordance -> Primitive Task -> Complex Task with Primitive Dependency Graphs and expert commentary; SMPL-X/MANO plus rigid and articulated object poses; benchmarks for hand mesh recovery, task-aware motion fulfilment (MF-MDM) and LLM-planned complex task completion.

## Capture setup (Sec. 3.2.1, App. A)
- mocap: "12 Optitrack Prime 13W infrared cameras to track the surface markers affixed to the subject's upper body, left and right hand, and interacting objects".
- cameras: "4 commodity RGB cameras, 3 of which are from allocentric views and 1 is from the egocentric view"; "synchronized at 30 fps, with resolution 848 x 480" (Sec. 4.1); cameras carry reflective markers and are calibrated to the mocap frame with ArUco cubes; ROS2 software sync (App. A.1).
- gloves: none; markers on hands and upper body.
- cleaning: three annotators fix ghost, merged and mislabelled markers in the vendor software and a multi-view editor with triangulation for occluded markers (App. A.2).

## Scale (Sec. 1, 4.2, Table 1)
- subjects: 9. objects: 75, 39 affordances, 60 Primitive types.
- scenarios: 4 (kitchen table, study room table, demo chem lab, bathroom table); 38 complex goals instantiated as 150 Complex Tasks.
- sequences: 627 (363 Primitive, 264 Complex Task). frames: 4.01M over 4 views. Hours not stated; derived: 4.01M / 4 / 30 fps = ~9.3 h.
- Table 1 (paper's comparison row): OAKINK2 848x480, 4.01M frames, 4 views, 9 subj, 75 obj, real, mocap, hand pose + obj pose + affordance + dynamic + long-horizon + task decomposition; ARCTIC listed as 2800x2000, 2.1M, 9 views, 10 subj, 11 obj.

## Annotations (Sec. 3.2.2, 4.1, App. A.3)
- hands / body: SMPL-X fitted MoSh++-style in two stages (shape + marker correspondence from a T-pose capture, then per-frame pose); "Other body representations like MANO are derived from this result."
- objects: rigid 6-DoF "directly solved via the MoCap system"; articulated parts either marker-tracked as rigid bodies or, if too small, one marker whose canonical position is calibrated and the joint parameter (revolute or prismatic) solved by least squares (Sec. 3.2.2).
- contact: no stored contact label is described; hand-object intersection is a fitting cost (below).
- task specification: affordances, Primitives with start/terminal conditions, Complex Tasks with goals, initial conditions, PDGs, subject completion order and GPT-4-refined expert commentary (Sec. 3.2.2, 4.1).
- two hands and objects jointly captured: yes, single mocap volume, upper body + both hands + all objects (Sec. 3.2.1).

## Interpenetration / contact terms and metrics (verbatim)
- Fitting (App. A.3, Eq. 3): "min_theta_t E = lambda_1 E_recon(theta_t) + lambda_2 E_prior(b)(theta_t) + lambda_3 E_plau(h)(theta_t) + lambda_4 E_plau(ho)(theta_t) + lambda_5 E_reg(theta_t)"; "E_plau(ho) penalizes the penetration and intersection between the interacting hands and objects by sampling internal points inside hand meshes and computing the sum of their signed distance function values of the objects." E_plau(h) is "an implementation of anatomy loss in [65]"; E_reg "contains velocity regularization terms". Weights lambda_i not given.
- Dataset quality (App. C.2, Table 6; "objects in interaction need to be grasped and lifted"): OAKINK2-Grasp vs OakInk-Core vs OakInk-Shape — Penet. Depth (cm) 0.25 / 0.18 / 0.11; Solid Intsec. Vol. (cm^3) 0.61 / 1.03 / 0.62; Sim. Disp. Mean (cm) 1.83 / 0.98 / 0.94; Sim. Disp. Std (cm) 1.16 / 1.74 / 1.62. Definitions of Penet. Depth and Sim. Disp. are not given in the extracted text; the authors read this as "annotation quality on par with OakInk".
- TaMF metrics (App. D.1): "CR, Contact Ratio. This metric measures the ratio of the frames within the motion trajectories where the hand-object contact (minimum distance) is within a 5 mm threshold." "SIV, Solid Intersection Volume. This metric measures how much space intersection occurs during estimation. We voxelize the object mesh into 100^3 voxels, and calculate the sum of the voxel volume inside the hand surface." PSKL-J (acceleration-spectrum KL, both directions) and FID over a 64-d transformer motion feature.

## Benchmarks and headline numbers
- Hand mesh recovery (Table 2, mm; table is garbled in the markdown, values read from the picture text): mono METRO PA-MPJPE 6.90, PA-MPVPE 6.47, RR-MPJPE 17.56 (AUC 0.410); RLE + HandTailor 5.46 / 6.86 / 13.08 (0.441); multi-view KP-based Fit 9.20 / 8.83 / 15.63 (0.349), MPJPE 19.30; POEM 6.18 / 6.61 / 12.12 (0.581), MPJPE 9.17, MPVPE 9.52. Splits ~70/5/25 % by sequence.
- TaMF, MF-MDM (Table 3): CR 0.90, SIV 4.17 cm^3, PSKL-J (gt,p) 0.0446 / (p,gt) 0.0460, FID 1.369, perceptual score dataset 4.66 +- 0.48 vs generated 3.64 +- 0.85.
- Complex Task Completion (Sec. 5.3): GPT-4 emits a program of execute(primitive, ...) calls checked against the PDG; object trajectories retargeted from an "Oracle" (dataset demonstrations); hands from TaMF; primitives joined by interpolation. No success-rate number in the main text (details deferred to Sup. Mat. E, not extracted).
- real robot: none; Sec. 6 lists retargeting to "heterogeneous hands and platforms" as future work.

## License and access
- No licence statement appears in either parsed source (grep for license/licence/CC/agreement over papers/md and code/md returns nothing). Data is distributed as tarballs on Hugging Face (`kelvin34501/OakInk-v2`) with a download script `script/download.py`; needs data, anno_preview, object_raw, object_repair, object_affordance and program tarballs (README). A 2024-12 note says some annotation files were re-uploaded and sequence offsets changed. Project page oakink.net/v2. Licence terms are therefore unknown from the corpus.

## Limitations stated by the authors
- None enumerated as a limitations section; Sec. 6 frames future work (VLA pre-training, retargeting to embodiments, transfer into simulators). App. A.2 acknowledges mocap failure modes (missed markers under occlusion, ghost markers, label swaps) handled manually.

## Quotable claims (verbatim, with section)
- "OAKINK2 contains 627 sequences of real-world bimanual manipulation sequences, where 264 of these sequences are for Complex Tasks. These sequences contain 4.01M frames from four different views (one egocentric and three allocentric views)." (Sec. 1)
- "despite the use of the mocap system as the primary annotation method for easily scaling up the capture process, OAKINK2 still achieved annotation quality on par with OakInk built upon the hybrid of manual and mocap annotation." (App. C.2)
- "E_plau(ho) penalizes the penetration and intersection between the interacting hands and objects by sampling internal points inside hand meshes and computing the sum of their signed distance function values of the objects." (App. A.3)

## Notes for the survey
- Feeds: two-hand HOI dataset table; the long-horizon / task-decomposition axis no other corpus dataset has; evaluation set for ManipTrans-style transfer.
- The dataset's own ground truth carries a stated mean penetration depth of 0.25 cm on lifted grasps (Table 6), larger than OakInk's 0.11-0.18 cm; this is the only corpus dataset that publishes a penetration number for its annotations, and any retargeting from it starts from that floor.
- Frame count is per-view (4.01M over 4 views); comparing with ARCTIC's 2.1M over 9 views or TACO's 5.2M over 13 views needs division by view count.
- Used or cited by (word-boundary grep over papers/md and code/md): an_dexil_survey_2025, bidexhd_2024, gigahands_2024, maniptrans_2025.
