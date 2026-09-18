# gigahands_2024 — GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities (Fu et al., CVPR 2025 highlight)

sources: papers/md/gigahands_2024.md [72ec0e0e] ; code/md/gigahands_2024.md [8ad3ef9a] (brown-ivl/GigaHands: download links, data format, text2motion training code; no capture pipeline)

## One-line contribution
A 51-camera markerless studio and an LLM-scripted "Instruct-to-Annotate" protocol yield 2,034 minutes (34 h) of bimanual activity from 56 subjects with 417 objects: 14k clips, 183M frames, 3.7M MANO hand-pose pairs, 84k text descriptions (1,467 verbs), plus automatically tracked 6-DoF poses for rigid objects; benchmarked on text-to-motion, motion captioning and dynamic radiance fields.

## Capture setup (Sec. 4.2, App. 7-8)
- cameras: "51 RGB cameras uniformly arranged within a cubic capture volume, with each face of the cube containing a 3 x 3 grid of cameras evenly illuminated by LED lights. Inside the cube, a transparent glass surface serves as a supportive platform for objects. Each camera records at 30fps with a resolution of 1280 x 720. Cameras are software-synchronized, with the temporal phase misalignment being less than 3 ms." Calibration by COLMAP with fiducials. Data layout names the cameras `brics-odroid-<id>` (README).
- mocap / gloves: none; fully markerless ("Our markerless capture setup", Abstract). Supp. Table 2 marks GigaHands as the only studio dataset with markerless hand and object tracking (ARCTIC, TACO, OakInk2, HOT3D: mocap).
- instructions: LLM-generated scripts, "5 scenarios, 25 scenes, 191 activities, and 1370 instructions containing a total of 533 verbs" (Sec. 4.1), played as audio; subjects re-record on mismatch (Sec. 4.2).

## Scale (Sec. 3, Supp. Table 2)
- subjects: 56. objects: 417 ("310 multiview scanned meshes and 31 single-view generated meshes"; non-rigid objects get masks only) (Sec. 3).
- minutes: 2,034 (Abstract: "34 hours"). motions: 13k instructed sequences refined into 14k clips (Sec. 4.3); Supp. Table 2: 13.9k motions.
- frames: "183M RGB frames (and 366M unique hand images)" over 51 views; 3.7M bimanual 3D hand poses (Sec. 3). Derived: 183M / 51 = ~3.6M view-agnostic frames, consistent with 3.7M poses at 30 fps (~2,000 min).
- text: 84k motion-text pairs after 5x LLM rephrasing, 1,467 unique verbs, 580 unique to GigaHands (Sec. 3, 4.3).
- Supp. Table 2 comparison row values as printed (mins / motions / poses / views / frames / subjects / objects / verbs): ARCTIC 121 / 339 / 218k / 9 / 2.1M / 10 / 11 / x; TACO 202 / 2.3k / 363k / 13 / 4.7M / 14 / 196 / 13; OakInk2 557 / 2.8k / 993k / 4 / 4.01M / 9 / 75 / 55; HOT3D 833 / 4.1k / 1.7M / 2-3 / 3.7M / 19 / 33 / x; GigaHands 2,034 / 13.9k / 3.7M / 51 / 183M / 56 / 417 / 1467. (These are GigaHands' tallies of other datasets; TACO's own paper says 2.5K sequences / 5.2M frames, OakInk2's says 627 sequences.)

## Annotations (Sec. 3, 4.4, 4.5, App. 7-8)
- hands: 2D/3D keypoints and MANO meshes for both hands. Pipeline: YOLO-v9 hand boxes (main text says YOLOv8), HaMeR per-view meshes for 2D keypoints, ViTPose side-aware handedness (">60% of the detected keypoints"), RANSAC triangulation, one-euro filtering, MANO fit "following the EasyMoCap pipeline" with "PCA components [disabled] and a flat mean shape" (App. 7). Valid-frame rate of the chosen detector/keypoint combination: 97.9 % on 60 clips (App. Table 10).
- objects: 6-DoF pose of pre-scanned or single-view-generated meshes; DINOv2 + Grounding DINO + OpenCLIP + SAM2 masks, Instant-NGP density-field initialisation, FoundPose-style rotation retrieval, differentiable rendering refinement with multi-view silhouette loss (Sec. 4.5, App. 8). Mask coverage: 45.2 % coarse, 91.1 % first-frame refinement, 78.5 % over sequences (App. Table 11); "for sequences with fast motion or where the object is severely occluded due to manipulation, the pose might lose track and accumulate errors" (App. 8). README (2025-09-04): 3.3k object motion sequences released with a per-scene "tracking success" csv.
- contact: "we can use them to estimate contact maps on both hands, following the approach in [101]" (Sec. 3, Fig. 3); contact maps are derived from the meshes, not captured; no contact threshold stated in the extracted text.
- segmentation masks, camera poses, text (annotations_v2.jsonl, `rewritten_annotation` used for training) (README).
- two hands and objects jointly captured: yes, same 51-view videos; hand and object tracks are estimated independently and later "aligned with the object coordinate system" (README, keypoints_3d_mano_align).

## Interpenetration / contact metrics
- None defined. The paper reports no hand-object penetration or contact-quality number for its annotations; physical plausibility is not among the evaluation metrics of any experiment (text-to-motion uses R-Precision, MM Dist, FID, Diversity, MultiModality; forecasting uses J_e, T_e, R_e; tracking uses valid-frame rate and mask coverage).

## Benchmarks and headline numbers
- Text-driven motion synthesis (Table 2, model trained per dataset; R-Precision @1/@2/@3 %, MM Dist, FID, Div, MM): TACO 18.9 / 37.7 / 52.9, 7.39, 11.0, 11.1, 6.83 (upper bound 64.4 / 86.2 / 89.4, 2.86, 0.045, 14.2); OakInk2 17.9 / 31.7 / 47.9, 7.75, 19.6, 6.88, 3.45 (ub 50.4 / 71.2 / 81.1, 3.67, 0.022, 9.30); GigaHands 31.2 / 44.7 / 53.1, 6.68, 4.70, 10.5, 9.11 (ub 77.4 / 88.8 / 91.3, 2.96, 0.002, 11.9). Each dataset has its own feature extractor and upper bound, so rows are not directly comparable.
- Task-aware motion fulfilment vs OakInk2 (Supp. Table 8, MDM with object-trajectory conditioning): OakInk2 23.4 / 35.7 / 49.8, 7.41, 13.1, 6.24, 3.71; GigaHands 27.2 / 46.2 / 54.6, 6.12, 5.91, 10.2, 9.73.
- Hand-object motion forecasting vs TACO (Supp. Table 9, N = M = 10 frames; J_e right/left mm, T_e mm, R_e deg): TACO 71.7 / 58.4, 52.8, 73.2; GigaHands 69.3 / 62.3, 47.6, 67.5. "hand-object motion forecasting still remains a challenging task."
- Motion captioning (Sec. 5.2) and dynamic radiance fields (Sec. 5.3): not extracted here.
- real robot: none.

## License and access
- README: "GigaHands is released under the Creative Commons Attribution-NonCommercial 4.0 International License." Data hosted on Globus: multiview RGB videos (tar per 10 views), hand_poses.tar.gz (keypoints_3d, keypoints_3d_mano, MANO params, camera parameters), keypoints_3d_mano_align.tar.gz, scans_publish.zip (object meshes), object pose zips (4 files, 3.3k sequences, 2025-09-04), object_meta.zip, annotations_v2.jsonl, instruction_script.json. "More data coming soon!" (README). No sign-up described.

## Limitations stated by the authors (Sec. 6)
- "The studio setting confines data collection to a limited space"; "fully automatic tracking of articulated and non-rigid objects remains challenging"; robotics applications left as "further research".
- Pipeline caveats (App. 7-8): HaMeR meshes "lack accurate depth" so only their 2D keypoints are used; object tracking can drift under fast motion or occlusion; single-view-generated meshes for small objects.

## Quotable claims (verbatim, with section)
- "GigaHands includes 3.7 million bimanual 3D hand poses, represented by both 3D keypoints and MANO [86] hand meshes, comparable to the scale of Ego-Exo4D [33]" (Sec. 3).
- "Since existing hand shape and pose estimation did not work well enough, we built our own hybrid method." (Sec. 4.4)
- "Since no existing method for object pose estimation worked well [75], we decided to build our own robust method that exploits our dense multi-view setting." (Sec. 4.5)
- "The right hand interacts with objects more frequently than the left, since a majority of our subjects were right-handed." (Sec. 3)

## Notes for the survey
- Feeds: two-hand HOI dataset table (largest by hours and views; only markerless one); text-conditioned hand motion generation.
- Caution for contact-centric use: hands and objects are estimated separately from RGB with no penetration term or contact metric reported, and object tracks are released with a per-sequence success flag; any interpenetration statistic on GigaHands has to be measured, not read off.
- Supp. Table 2 is a convenient cross-dataset tally but its ARCTIC/TACO/OakInk2 counts differ from those datasets' own papers (see Scale); cite the primary notes for those.
- Used or cited by (word-boundary grep over papers/md and code/md): maniptrans_2025 (reference-list citation only, no usage found in the grep line).
