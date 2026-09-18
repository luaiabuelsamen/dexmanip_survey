# shadow_dexterous_hand_2005 — Shadow Dexterous Hand, technical specification Dec 2024 (Shadow Robot Company; commercial product)

sources: papers/md/shadow_dexterous_hand_2005.md [1c060ce6 = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17: spec PDF shadow_dexterous_hand_e_technical_specification_20241204.pdf and https://shadowrobot.com/dexterous-hand-series/] ; code/md/shadow_dexterous_hand_2005.md [172c3d9c, github.com/shadow-robot/sr_common]
source: vendor page and datasheet; specs are manufacturer claims, not measurements.

## One-line contribution
A 24-joint, 20-motor tendon-driven anthropomorphic hand with the motors in the forearm, EtherCAT at 1 kHz to the host and a 5 kHz tendon-force loop in each motor module (spec Secs. 1, 3.2, 5).

## Hand record
- maker: Shadow Robot Company, London NW5 1LP, United Kingdom (spec, last page). country: UK.
- DoF: "20 actuated DOF and a further 4 under-actuated movements for a total of 24 joints" (page, comparison table); "provides 24 movements" (spec Sec. 1). Thumb 5 DoF / 5 joints; each finger 3 DoF / 4 joints with FF1..LF1 "Coupled" to J2 (spec Sec. 2.3 table); LF5 extra palm joint 0-45°; wrist WR1 -40..28°, WR2 -28..8°. Joint ranges: J1/J2 0-90°, J3 -15..90°, J4 ±20°, TH1 -15..90°, TH2 ±40°, TH3 ±12°, TH4 0-70°, TH5 ±60° (spec Sec. 2.3).
- actuated DoF: 20 ("20 DC motors", page table; "twenty Smart Motor nodes", spec Sec. 5). Code: Gazebo effort controllers on FFJ0 (coupled J1+J2), FFJ3, FFJ4, ..., LFJ5, THJ1-5, WRJ1-2 (hand_effort_controller_gazebo.yaml).
- actuation: tendon-driven; "Each of the twenty Smart Motor nodes drives a Maxon motor using PWM"; each module integrates "force and position control electronics, motor drive electronics, motor, gearbox, force sensing and communications", 20 packed into the hand base (spec Secs. 1, 5). Motors are in the forearm ("all actuation and sensing are built into the hand and forearm").
- fingers: "4 + 1 (thumb)" (page table); fingers equal length with staggered knuckles (spec Sec. 2.1).
- thumb design: 5 joints TH1-TH5 including a ±60° base rotation (TH5) and a 0-70° TH4 (spec Sec. 2.3).
- weight: "Hand and forearm have a total weight of 4.3 kg" (spec Sec. 2.4). Lite 2.4 kg, Extra Lite 2.1 kg, Super Lite 1.8 kg (page table).
- fingertip force: not stated. Payload: "while in a power grasp, can hold up to 4 kg" (spec Sec. 2.4). Speed: "full-range joint movement in free space ... at a frequency of 1.0 Hz" (Sec. 2.5).
- tactile sensing: two Shadow Tactile Fingertips (STF) standard on thumb and index, up to 5; "The STF has 17 x 3 DoF taxels. Each taxel consists of a magnet and an accompanying 3-axis Hall effect sensor. The data is uncalibrated and sampled by a 12-bit ADC" (spec Sec. 4.2), 1000 Hz (Sec. 4 table). Code message set also carries Biotac.msg, BiotacAll.msg, MST.msg, UBI0.msg, ShadowPST.msg, i.e. BioTac/MST/UBI0/PST fingertip options exist in the software (sr_robot_msgs/msg). Other sensing: Hall-effect joint position, 0.2° typical, 12-bit, 1000 Hz; tendon-pair force sensors 500 Hz, ~30 mN resolution, "zeroed but not calibrated" (Sec. 4.3); 40 tendon load sensors, 1 IMU (page table); temperature/current/voltage 100 Hz. Page: "over 100 sensors running at up to 1KHz". Bib "129 sensors" is a bib-claim.
- control interface and rate: EtherCAT 100 Mbps; position control in the host by default; "The torque loop is closed inside the motor unit at 5kHz ... All other control loops run at 1kHz through the host" (Sec. 3.2). PIC18Fxx80 / PIC32 / PSoC microcontrollers; firmware under NDA (Sec. 3.3). ROS, Python/C++, supplied Ubuntu laptop; Gazebo model; code repo adds MuJoCo models for Hand E, E plus, left/right and UR10 combinations (sr_description/mujoco_models). Power 48 V @ 2.5 A (Sec. 7).
- price: not stated ("discuss pricing", page). Bib "~$100k class" is a bib-claim.
- open-hardware?: no. Software "under GNU GPL or BSD as appropriate"; controller source and schematics "on request under the Non-Disclosure Agreement" (Sec. 6.1). sr_common configs are BSD-licensed (file headers).
- release status and date: spec dated December 2024; "Over 20 years' research and development" (page). Bib "commercial since 2005" is a bib-claim consistent with that phrase. Variants: Dexterous Hand, Lite (13 DoF/16 joints), Extra Lite (10/12), Super Lite (7/8); left hand and UR10e integration options (Sec. 8).
- used by (grep -l -i "shadow hand|shadow dexterous|shadow robot|shadowhand"): 43 other keys. Ten of them: dextreme_2022, visual_dexterity_2022, unidexgrasp_2023, unidexgrasp_pp_2023, bidexhands_2022, dexpbt_2023, plappert_multigoal_2018, robopianist_2023, pddm_2019, faive_hand_2023.

## Setting
- Comparison table (page): Lite drops the wrist and one finger, "35% power saving"; STFs standard 2/2/1/1, max 5/4/3/2; tendon load sensors 40/26/20/14; all 1 kHz EtherCAT.

## Method / Evaluation
None (datasheet). Precision claim: "All joints except the finger distal joints are controllable to +/- 1° across the full range of movement" (Sec. 2.3).

## Limitations stated in the source
- Tendon force sensors are zeroed, not calibrated (Sec. 4.3); STF taxel data uncalibrated (Sec. 4.2).
- Distal finger joints are coupled and not independently controllable (Sec. 2.3).

## Quotable claims (verbatim)
- "The torque loop is closed inside the motor unit at 5kHz." (spec Sec. 3.2)
- "The Hand and forearm have a total weight of 4.3 kg. The Hand, while in a power grasp, can hold up to 4 kg." (spec Sec. 2.4)

## Notes for the survey
- Reference full-anthropomorphic hand: 24 joints / 20 motors / 4.3 kg with forearm. Its "24 DoF" in learning papers usually means joints, with 20 actuated and 4 coupled (this spec). The sim models most papers use (MuJoCo shadow hand) are separate from sr_common's own MuJoCo files.
- The OpenAI/Google Brain case studies appear on the DEX-EE page (shadow_dex_ee_2024), not here.
