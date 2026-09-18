# allegro_hand_v4_2016 — Allegro Hand V4 (Wonik Robotics; commercial research hand)

SOURCE THIN: https://www.allegrohand.com/v4 returned HTTP 404 and the Wonik wiki timed out; the paper-side md holds no product text. Everything confirmed below comes from the ROS driver repository.

sources: papers/md/allegro_hand_v4_2016.md [d9f1ff68 = sha256 of the md on disk; fetch failures only; pages_manifest fetched 2026-09-17] ; code/md/allegro_hand_v4_2016.md [b19b18ea, github.com/simlabrobotics/allegro_hand_ros_v4]
source: vendor repository; specs are manufacturer claims, not measurements.

## One-line contribution
The 16-joint, four-finger torque-interfaced research hand whose ROS driver polls the hand's own 333 Hz clock over CAN and exposes PD, velocity-saturation, torque and pre-defined-grasp controllers (README).

## Hand record (what the repository confirms)
- maker: "manufacturer: 'Wonikrobotics Co. Ltd.'", "origin: 'Seoul, South Korea'" (zero.yaml hand_info, serial SAH040A080R, version 4.0). Older zero files carry "manufacturer: 'SimLab Co. Ltd.'" for version 1.0/2.0 hands, i.e. the hand predates Wonik. country: South Korea.
- DoF: "DOF: 16" (zero.yaml). Joints j00..j33 = 4 fingers x 4 joints (gains_pd.yaml "P and D gains for each of the 16 joints").
- actuated DoF: 16 (one gain set per joint; every controller "implements computeDesiredTorque", README "Packages").
- actuation: each joint is commanded in torque by the driver (torque controller "Direct torque control", README); motor type, gearing and joint torque are not in the repo. Bib "direct-drive DC motors with gearing, 0.7 N m" is a bib-claim.
- fingers: four (index, middle, ring j0x-j2x and thumb j3x; the thumb's home position j30 = 60°, j31 = 25° differs from the fingers' in initial_position.yaml).
- thumb design: a fourth 4-joint finger chain with a distinct home pose; opposition geometry not described in the repo.
- weight: not stated in sources (bib ~1.1-1.2 kg: bib-claim).
- fingertip force / payload: not stated in sources (bib 5 kg payload: bib-claim; the XELA leaflet in xela_uskin_2020 also states 5 kg, but that is a reseller restating Wonik).
- tactile sensing: none in the driver.
- control interface and rate: CAN via a PEAK PCAN-USB adapter; "The preferred sampling method is utilizing the Hand's own real time clock running @ 333Hz by polling the CAN communication" (README, note from Wonik Robotics); "control_period_s: 0.003" (zero.yaml). Input voltage 12 V for v4.0 (8 V listed for a v3.0 file). Controllers: grasp (BHand binary library, gravity compensation), pd (P = 4000, D = 150-300), velsat (v_max 10), torque, sim. ROS Kinetic; Python client library; xacro/URDF left and right.
- price: not stated (bib ~$20-25k: bib-claim).
- open-hardware?: no; software repo with a LICENSE file (text not in md); BHand grasp library ships as 32/64-bit binaries only.
- release status and date: zero files span versions 1.0, 2.0, 3.0 and 4.0; no dates. Bib "V4 2016-2024; V5 announced 2024/25" is a bib-claim.
- used by (grep -l -i "allegro" over code/md and papers/md): 55 other keys. Ten of them: dextreme_2022, hora_2022, penspin_2024, twisting_lids_2024, dexpbt_2023, leap_hand_2023, dime_2022, holo_dex_2022, hato_visuotactile_2024, digit_2020.

## Setting
- Driver only; multiple hands need separate ZEROS files, CAN devices and NUM; "robot_description" is a single global parameter, so two hands overwrite each other's kinematics (README, "Known Issues").

## Method / Evaluation
None (driver repository). One Python file: allegro_hand_description/scripts/detect_pcan.py, `def pcan_search()`.

## Limitations stated in the source
- "ROS's interrupt/sleep combination might cause instability in CAN communication resulting unstable hand motions." (README)
- "At this point no effort has been made to be backwards compatible." (README)

## Quotable claims (verbatim)
- "The preferred sampling method is utilizing the Hand's own real time clock running @ 333Hz by polling the CAN communication" (README)

## Notes for the survey
- The most-cited hand in the corpus (56 files). Confirmed facts: 16 joints, 4 fingers, torque interface, 333 Hz CAN, 12 V, Seoul. Weight, torque, payload and price need a datasheet; refetch allegrohand.com or the Wonik wiki before tabulating them.
