# dexhand_open_source_2023 — DexHand: An Open Source Dexterous Humanoid Robot Hand (Rob Knight, The Robot Studio; site by Trent Shumay, IoT Design Shop; open-hardware project, 2023)

sources: papers/md/dexhand_open_source_2023.md [658c16f4 = sha256 of the md on disk; no manifest entry; pages_manifest fetched 2026-09-17 https://www.dexhand.org/] ; code/md/dexhand_open_source_2023.md [e88ebd74, github.com/TheRobotStudio/V1.0-Dexhand]
source type: project web page plus the V1.0 repository README and file tree. Specs are the designer's claims, not measurements. The bib lists the second author as "Trevor Blank"; the page names Trent Shumay (IoT Design Shop) as the site maintainer.

## One-line contribution
A fully 3D-printed, tendon-driven humanoid hand and forearm whose non-printed parts cost "around $300 USD", released under CC BY-NC-SA 4.0 with Onshape CAD (README).

## Hand record
- maker: Rob Knight, The Robot Studio (design; "envisioned and released to Open Source"); electronics, firmware and ROS 2 layers by Trent Shumay, IoT Design Shop (page). country: not stated on either source.
- DoF: no joint count is given. Actuators (README): "16 slim micro-servos that drive the fingers and thumb", plus "2 standard micro servos ... for wrist flexion and extension" and "1 standard servo needed for axial wrist rotation (optional)".
- actuated DoF: 16 finger/thumb servos (+2/+3 wrist) as above.
- actuation: tendon. README: "Kite or fishing line for finger tendons - Sufix 832 ... 80lbs"; "0.8mm kiteline for the finger ligaments and wrist tendons"; STLs Tendon_Spool_01/02a/05, Thumb_Tendon_Hanger_03a; "tendon routing in the forearm and hand" still being finalised. Servos: Emax ES3301 (~$6.6) / ES3302 (~$9.2) / ES3351 (~$8.5) / ES3352 (~$12), plastic or metal gear, analog or digital; wrist Feetech SCS2332 serial-bus servos (~$35 each) or PWM substitutes at half the range.
- fingers: five, implied by the Hand_06 STL names (Palm_Fore/Middle/Ring/Little, *_THUMB parts).
- thumb design: separate CMC_Pitch_15 and CMC_Yaw_15a parts and MLP/PLP/Tip_THUMB phalanges (file tree); no further description.
- weight: not stated.
- fingertip force: not stated.
- tactile sensing: not mentioned (bib "no tactile" is consistent but unconfirmed).
- control interface and rate: original firmware is Arduino sketches Hand_12.ino / Hand_12b.ino with SCServo and SBUS drivers (file tree, "V1.0 DexHand_12/"); IoT Design Shop stack: Arduino Nano RP2040 Connect, BLE firmware, MediaPipe hand-tracking teleop demo, ROS 2 packages with URDF and RViz2 (page, Quick Links). No rate stated.
- price: "additional total cost of components required for the hand around $300 USD"; "the hand uses less than 300 USD of components" (README).
- open-hardware?: yes. CC BY-NC-SA 4.0 (README); CAD "freely and publically available down to a parasolid level" on Onshape; STLs in the repo. Non-commercial licence.
- release status and date: page posts dated Aug 8 2023 (BLE firmware), Aug 27 2023 (electronics build), Oct 1 2023 (ROS 2 support). The V1 hardware release date is not stated. Bib "v2.x ongoing" is not on the page.
- used by (grep -l -i "therobotstudio|robot studio|dexhand.org|dexhand v1|V1.0-Dexhand" over code/md and papers/md): no other key. The bare word "dexhand" hits 19 other files but those are unrelated uses of the word (e.g. zhao_dexhand_survey_2026), so they are not listed.

## Setting
- hand(s): as above; the forearm "can operate as a stand-alone unit allowing unlimited axial rotation for rotational tasks like scrubbing" (README).
- simulator: none; RViz2 only "for testing the packages without a hardware hand" (page).
- objects / data: none.

## Method
- paradigm: hardware design and teleop demo (MediaPipe hand tracking over BLE, page); a ChatGPT gesture demo is mentioned.
- key trick(s): everything printed on any extrusion printer with a 0.6 mm nozzle and 0.4 mm layers; tested in PLA, PETG and CF nylon, ABS not recommended (README).

## Evaluation
None. No metrics, no trials.

## Limitations stated by the authors
- "Some minor updates still required to finalise the tendon routing in the forearm and hand." (README)
- Two divergent repo lineages (Robot Studio mechanical vs IoT Design Shop electronics/ROS) that the site is "working to consolidate" (page FAQ).

## Quotable claims (verbatim, with section)
- "The hand is made entirely by 3dprinting with additional total cost of components required for the hand around $300 USD." (README)
- "The biggest cost item are the 16 slim micro-servos that drive the fingers and thumb." (README)

## Notes for the survey
- Anchors the bottom of the open-hardware cost axis ($300 parts vs LEAP V2 Adv $3000, see leap_hand_v2_adv_2025). No DoF number can be quoted; quote servo counts.
- Not used by any learning paper in the corpus.
