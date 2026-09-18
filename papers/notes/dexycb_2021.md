# dexycb_2021 — DexYCB: A Benchmark for Capturing Hand Grasping of Objects (Chao et al., CVPR 2021)

sources: papers/md/dexycb_2021.md [19915a87] ; code/md/dexycb_2021.md [64551b00]

## One-line contribution
Markerless 8-view RGB-D capture of 10 subjects grasping 20 YCB objects (1,000 sequences, 582K frames) with MANO hand and 6D object poses solved from crowd-sourced 2D keypoints plus multi-view depth, benchmarked on COCO detection, BOP 6D pose, 3D hand pose, and a handover grasp coverage/precision task (Abstract, Sec. 2, 5, 6).

## Setting
- hand(s): human hands, MANO mesh (778 vertices, θ ∈ R^51 pose, β ∈ R^10 shape pre-calibrated per subject and fixed) (Sec. 2.3). Robot only in the handover evaluation: a Franka Panda parallel-jaw gripper is assumed (Sec. 6).
- sensor setup: 8 RealSense D415 RGB-D cameras, extrinsically calibrated and temporally synchronized, 30 fps, colour and depth at 640×480 (Sec. 2.1). Black background (App. B.4).
- objects / data: 20 YCB-Video objects (toolkit list: 002_master_chef_can, 003_cracker_box, 004_sugar_box, 005_tomato_soup_can, 006_mustard_bottle, 007_tuna_fish_can, 008_pudding_box, 009_gelatin_box, 010_potted_meat_can, 011_banana, 019_pitcher_base, 021_bleach_cleanser, 024_bowl, 025_mug, 035_power_drill, 036_wood_block, 037_scissors, 040_large_marker, 052_extra_large_clamp, 061_foam_brick; Tab. 3). Per trial: one target plus 2–4 other objects; subject picks up the target and holds it, some pretend to hand over; 3 s recordings; 5 trials per object (2 right hand, 2 left, 1 random); 100 trials per subject; 1,000 total (Sec. 2.2).
- counts (App. Tab. 9, "all"): 10 subjects, 20 objects, 8 views, 1,000 sequences, 581,968 images, 2,317,312 object annotations of which 581,968 grasped, 508,384 hand annotations (254,000 right, 254,384 left).
- annotation types: 2D keypoints labelled by MTurk workers in a VATIC-based tool for every view of every sequence; hands: 21 joints (3 joints + tip per finger + wrist) tracked with per-frame invisibility flags; objects: 2 annotator-chosen distinctive landmark points per object per view (Sec. 2.2). 3D pose per frame by minimising E = E_depth + E_kpt + ℓ2 regulariser on MANO pose: E_depth = SDF of the merged multi-view point cloud to all hand/object meshes (mm, GPU point-parallel); E_kpt = reprojection error over N_C = 8 views, N_J = 21 joints and N_K = 2 object keypoints weighted by visibility; Adam lr 0.01, 100 iterations, initialised from the previous frame; first frame from PoseCNN with manual selection (Sec. 2.3). Accuracy check: fingertip reprojection errors mean < 5 px (App. B.2, Tab. 8). No contact, force, or penetration labels are computed.

## Method
- paradigm: dataset + benchmark; representative approaches re-trained (Mask R-CNN, SOLOv2; PoseCNN, DeepIM, DOPE, PoseRBPF, CosyPose; Spurr et al. with ResNet50/HRNet32, A2J) (Sec. 5).
- splits (Sec. 5.1, Tab. 9): S0 default 800/40/160 sequences; S1 unseen subjects 7/1/2; S2 unseen views 6/1/1; S3 unseen grasping 15/2/3 objects, "Objects being grasped in the test split are never being grasped in the train/val split, but may appear static on the table".
- key trick(s): user-defined object keypoints instead of predefined ones, mapped once to a mesh vertex by back-projection (Sec. 2.3).

## Evaluation
- metrics (exact):
  - 2D: COCO AP for 20 object classes + 1 hand class (masks rendered from GT), keypoint AP for 21 joints reprojected (Sec. 5.2).
  - 6D: BOP protocol, recall under VSD, MSSD, MSPD averaged into AR; evaluated on grasped objects only; keyframes subsampled by 4 (Sec. 5.3, App. C.1; "6D eval" column in Tab. 9).
  - 3D hand: MPJPE in mm and PCK AUC over [0, 50 mm] in 100 steps; absolute, root-relative (wrist replaced by GT), Procrustes (Sec. 5.4).
  - handover (Sec. 6): reference set R = 100 grasps per object farthest-point-sampled from [7], moved by GT object pose, minus those colliding with GT object or hand mesh. "coverage [7] of R, defined by the percentage of grasps in R having at least one matched grasp in χ that is neither collided with the object nor the hand"; "precision, defined as the percentage of grasps in χ that have at least one matched successful grasp in R". "two grasps g, h are considered matched if |g_t − h_t| < σ_t and arccos(|⟨g_q, h_q⟩|) < σ_q ... We use σ_t = 0.05 m and σ_q = 15°." Baseline: transform the 100 grasps by the estimated pose, drop any with a gripper-to-hand point-cloud distance below ε ∈ [0, 0.07 m], hand from Mask R-CNN segmentation + depth. Test images = last frame of each video, 1,280 in S0 (Tab. 9). Two objects (master chef can, wood block) have no feasible Panda grasps (App. D.1).
- code: toolkit exposes the four evaluations (`examples/evaluate_coco.py`, `evaluate_bop.py`, `evaluate_hpe.py`, `evaluate_grasp.py`); grasp eval consumes a BOP csv + COCO json and prints coverage/precision per (radius 0.05 m, angle 15°, dist th 0.00–0.07 m); category ids 1–21 objects, 22 hand (`dex_ycb_toolkit/dex_ycb.py#L35-57`); HPE result lines are 63 numbers in mm camera coordinates; `is_bop_target` flags keyframes. The md's "Python signatures and reward/observation bodies" section is empty (0 files), so metric bodies were not captured; definitions above are from the paper. Paper and README agree on the four tasks and thresholds.
- headline numbers: cross-dataset Tab. 2 (MPJPE root-relative / Procrustes, ResNet50): HO-3D→DexYCB 48.30 / 24.23 vs DexYCB→DexYCB 12.97 / 7.18; DexYCB→HO-3D 31.76 / 15.23 vs HO-3D→HO-3D 18.05 / 10.66. 6D Tab. 6: PoseCNN RGB AR "all" S0 41.65, S1 38.26, S2 45.18, S3 37.41; on S1 PoseCNN+depth 43.27, DeepIM RGB-D 57.54, CosyPose RGB 57.43, PoseRBPF RGB-D 46.48. Hand Tab. 7, S0: Spurr+HRNet32 absolute 52.26 mm (AUC 0.328), root-relative 17.34 (0.698), Procrustes 6.83 (0.864); A2J (depth) absolute 27.53 but Procrustes 12.07; S2 HRNet32 absolute 80.63. Handover: precision-coverage curves only (Fig. 4, Fig. 9); no scalar reported in the md.
- vs HO-3D (Sec. 3.2): 20 vs 10 objects, 8 vs 1–5 views, 582K vs 78K frames, 1,000 vs 27 sequences; "Among the 27 sequences from HO-3D, we found 17 with hand always rigidly attached to the object".
- baselines beaten: n/a (dataset paper).
- real robot? none; handover is evaluated geometrically against meshes.

## Limitations stated by the authors
- Subjects always face the same direction, so unseen-view hand pose is hard (Sec. 5.4). Missed or partial hand detection under occlusion yields pinching grasps (Sec. 6, App. D.2). Black background chosen deliberately (App. B.4). Not stated but evident: 3 s clips of pick-and-hold only, no in-hand manipulation, no contact labels.

## Quotable claims (verbatim, with section)
- "The dataset, DexYCB, consists of 582K RGB-D frames over 1,000 sequences of 10 subjects grasping 20 different objects from 8 views" (Sec. 1)
- "the introduction of hand-attached devices may be intrusive and thus bias the naturalness of hand motion" (Sec. 1)
- "the main edge actually lies in the diversity of captured grasps as shown by the distribution of hand pose" (App. B.3)

## Notes for the survey
- Feeds the datasets section. As a source of reference grasps for tracking policies it gives kinematics only; physical plausibility (penetration, contact) must be computed downstream, for which grab_2020 gives the recipe.
- Count bookkeeping: Sec. 1 says 582K frames, Tab. 9 says 581,968 images; the paper's Tab. 1 lists GRAB as 1,624K frames / 1,335 sequences whereas GRAB's own Table 1 gives 1,622,459 / 1,334.
- The handover coverage/precision metric is a collision-based grasp score in SE(3), not a wrench-space quality; contrast with ferrari_canny_1992 (SOURCE THIN).
