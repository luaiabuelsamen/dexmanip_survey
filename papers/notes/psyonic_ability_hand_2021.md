# psyonic_ability_hand_2021 — PSYONIC Ability Hand (PSYONIC, commercial product 2021)

sources: papers/md/psyonic_ability_hand_2021.md [dc373b8d, sha256 of the parsed page; no manifest entry, page fetched 2026-09-17 from psyonic.io/robots] ; code/md/psyonic_ability_hand_2021.md [34c9a932, github.com/psyonicinc/ability-hand-api]
source: vendor page; specs are manufacturer claims, not measurements. The page fetched cleanly but is a marketing page: it states the motor count, the sensor stream and the interfaces and nothing else. The datasheet (ABILITY-HAND-ICD.pdf) and spec sheet it links were not fetched.

## One-line contribution
A prosthesis-derived five-finger hand sold to robotics labs with an open API (Python/C++/ROS2/MATLAB), URDFs and MuJoCo/Isaac simulators; the page's entire hardware claim is "6 BLDC motors, 6 encoders, 30 touch values".

## Setting
- hand(s): Ability Hand, PSYONIC (San Diego, CA, USA per page footer); sold as a stand-alone end-effector ("Designed to integrate with leading robotics platforms", "Book a call"; no price on page)
- simulator / physics: vendor repo ships `python/ah_simulators/ah_mujoco.py` (MuJoCo, with `mimic_joints` in the controller) and an Isaac Sim 4.5 path (README); URDFs for left/right, large/small, and a `right_large_no_fsr` variant (`URDF/`)
- observation (from the API, `python/ah_wrapper/observer.py`): position, velocity, current, FSR, hot/cold status
- action space (page): "Torque, velocity, and position control of the 6 brushless DC motors"; rate not stated on page or in the README (`speed_tests.py` exists, no number)

## Hand record (page unless marked; bib-claim = from `specs` field, not confirmed by page)
- maker / country: PSYONIC, USA
- DoF: not stated as a count; page says 6 motors. bib-claim: 6 DoF. actuated DoF: 6 (one per motor)
- actuation: linkage. Page does not say; the repo's `MATLAB/get_abh_4bar_driven_angle.m` and `python/finger_4bar/abh_finger_4bar.py` name a four-bar finger, so "linkage" rests on code file names.
- fingers: 5 implied by URDF meshes (`idx-F1/F2`, `thumb-F1/F2`, palm); page does not count them
- thumb design: not stated; thumb has two mesh links (`thumb-F1`, `thumb-F2`) and left/right variants of F2
- weight: not stated. bib-claim: 490 g
- fingertip force: not stated
- tactile sensing: "30 touch sensor values" streamed (page); type FSR (API `update_fsr`, `fsr_offset`, URDF `no_fsr` variant). Per-finger split not on page. bib-claim: 6 FSR per finger
- control interface and rate: "BLE, I2C, UART, or RS485" (page); hand ships in I2C mode, UART recommended (`We16`), RS-485 (`We35`), 8-12 V supply (README). Rate not stated. bib-claim: up to ~500 Hz
- price: not stated. bib-claim: ~$15-20k
- open-hardware?: no. API, URDFs, meshes and simulators are public (repo has a LICENSE file; terms not in the dump); mechanical design is not.
- release status and date: shipping ("Powering Top Brands", "Ready for industrial scale"); date not on page. bib-claim: since 2021
- used in corpus: hato_visuotactile_2024 (two Ability Hands on UR5e, real teleop and tactile data), bunny_visionpro_2024 (real control code, XArm7 + Ability Hand), maniskill3_2024 (dual XArm7 with Ability hand in sim), an_dexil_survey_2025 (cites HATO), zhao_dexhand_survey_2026 (Dex1B row: "Inspire; Ability Hand"), dexmachina_2025 (cites the website only)

## Method
- paradigm: n/a (hardware). Control modes exposed by the API: position, velocity, torque (page); the Python `Hand` class tracks target position/velocity/current/duty.
- key trick(s): touch stream and motor stream over one serial link; `ah_wrapper/ppp_stuffing.py` frames packets; the observer pattern delivers pos/vel/cur/fsr callbacks.

## Evaluation
- specified in a datasheet: only the motor count, sensor count and interfaces are on the page; everything else lives in the unfetched ICD/spec-sheet PDFs.
- demonstrated in video: none on the page (no demo text).
- real robot: the page names no integrator; "Powering Top Brands" has no names in the extracted text.

## Limitations stated by the authors
None stated. README: the hand "cannot operate ... while it is charging"; hand ships in I2C mode and must be switched.

## Quotable claims (verbatim, with section)
- "Torque and position control across all 6 BLDC motors enables hyper-precise tasks with steady, human-level stability." (page, "From micro-movements")
- "Torque, velocity, and position control of the 6 brushless DC motors as well as streaming of all 6 encoder values and 30 touch sensor values over BLE, I2C, UART, or RS485." (page, "Simulation ready.")

## Notes for the survey
- Feeds the hardware table (commercial hands, prosthetic crossover) and the tactile column. Weight, force, price, rate and closing time must be marked bib-claim until the ICD is read.
- The corpus uses it mostly as a real-robot end-effector on UR5e/XArm7 (HATO, Bunny-VisionPro), not as a sim target except ManiSkill3.
