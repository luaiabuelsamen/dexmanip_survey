# linkerbot_l20_2025 — LinkerBot Linker Hand L20 (and O6) (LinkerBot, commercial product 2025)

SOURCE THIN: the L20 product page (openelab.io/products/linker-hand-linkerbot-l20-21) returned HTTP 404. What is on disk is (a) a reseller page for the O6 (roboticscenter.ai, "SVRC"), and (b) the vendor's ROS SDK repo, which covers L7/L10/L20/L21/L25/O6/T24. No L20 datasheet was read. The bib `specs` for L20 — 21 DoF (16 active + 5 passive), linkage-driven, RMB 49,900 (~$7k) — are unverified bib-claims.

sources: papers/md/linkerbot_l20_2025.md [d0691a40, sha256 of the parsed page; no manifest entry, fetched 2026-09-17] ; code/md/linkerbot_l20_2025.md [fdf0c26d, github.com/linkerbotai/linker_hand_sdk; README says the project moved to github.com/linker-bot/linkerhand-ros-sdk]
source: reseller page + vendor SDK; specs are manufacturer/reseller claims, not measurements.

## One-line contribution
A Chinese hand line whose ROS SDK addresses every model through a fixed 20-entry joint vector over CAN, with per-finger normal/tangential/proximity readings on L10/L20; the O6 entry model is sold with a glove and 16 capacitive tactile regions.

## Setting
- hand(s): Linker Hand L20 (target of most SDK examples); O6 (reseller page). SDK author "CHIUS INC" (README Overview). Country: not stated in either source (SDK comments are Chinese; reseller ships "from San Francisco")
- simulator / physics: SDK ships PyBullet (`linker_hand_pybullet.py _hand_type:=L20`) and an `examples/L20/l20_isaacgym/` directory (file tree)
- observation (SDK 6.3): joint state in radians and 0-255 range (`/cb_left_hand_state_arc`), velocity, current, error code, force sensor data
- action space (SDK 6.4): position (0-255 per entry), speed, current, torque; enable/disable; "remote operation mode" (L25: a disabled hand drives an enabled one). Rate not stated; CAN bitrate 1,000,000 (`ip link set can0 up type can bitrate 1000000`, 4.3)

## Hand record — L20 (SDK unless marked)
- maker / country: LinkerBot / CHIUS INC; country not stated
- DoF: not stated in on-disk sources. SDK `L20_action.yaml` gives 20 position entries per action, and `setting.yaml` says "Regardless of l10 or l20, joint name always has 20 entries", so 20 is the command-vector length, not a DoF count. bib-claim: 21 DoF, 16 active + 5 passive
- actuation: not stated. bib-claim: linkage
- fingers: 5 ("five-finger normal force readings" array of 5, SDK 6.3.2)
- thumb design: not stated
- weight / fingertip force: not stated
- tactile sensing (L10, L20; SDK 6.3.2): per finger, four channels each 0-255: normal force, tangential force, tangential force direction, proximity; i.e. 5 sensing sites x 4 channels. `TOUCH: True/False` flag in `setting.yaml`. Type not stated
- control interface and rate: USB-to-CAN at 1 Mbit/s; optional Modbus/485 ("RML", `setting.yaml`); ROS topics; rate not stated
- price: not stated. bib-claim: RMB 49,900 (~$7k)
- open-hardware?: no; SDK public (`linker_hand_sdk`, `linker_hand_python_sdk`, `linker_unidexgrasp`, `human-dex` repos listed in README 8)
- release status and date: shipping (SDK V2.1.8/2.1.9 supports it); no date on disk. bib-claim: 2025
- used in corpus: an_dexil_survey_2025 (Fig. 3 (g) "Linker Hand L20"), bai_unified_manip_survey_2025 ("Linker Hand L20" among learning-oriented hands)

## Hand record — O6 (reseller page roboticscenter.ai; reseller's own SDK `pip install roboticscenter`, USB serial, differs from the vendor CAN SDK)
- DoF 12 "per hand (5 fingers, 2-3 DOF each)"; 16 capacitive tactile regions; ~580 g; payload "~500 g tip pinch / ~2 kg power grasp"; repeatability +/-0.5 mm; max finger speed ~300 deg/s; 12 V DC, 3 A peak; USB serial 921600 baud, "SVRC framing"; "50 Hz command loop"; price "Custom Quote" / monthly lease; "Open Source | SDK only". bib-claim: ~$1,500. Vendor SDK `O6_positions.yaml` has 6 position entries per action, so the vendor command vector for O6 is 6 wide; whether 12 DoF are all actuated is not stated.

## Method
- n/a (hardware). SDK examples: GUI slider control (L10/L20), rock-paper-scissors, pinch, "Imitation Learning Training" data collection, and a UniDexGrasp module that "maps the shadowhand pose output by the model to the linkerHand L20 pose" (6.6.2).

## Evaluation
- specified: O6 numbers above (reseller); L20 only through SDK structure.
- demonstrated in video: none on disk.

## Limitations stated by the authors
SDK warnings only ("stay away from the dexterous hand's range of motion"). Reseller comparison table (O6 vs Orca/Allegro/Leap) is marketing.

## Quotable claims (verbatim)
- "Right hand five-finger normal force readings: [0.0, 0.0, 0.0, 0.0, 0.0], with a range of 0 to 255, where greater pressure results in higher values." (SDK README 6.3.2)
- "16 capacitive tactile regions per hand included out of the box." (reseller page, "Built-In Tactile Sensing")

## Notes for the survey
- Hardware table: L20 row must be flagged bib-claim for DoF, actuation and price until a vendor page is fetched. The O6 row is reseller-sourced.
- The 20-wide fixed joint vector across models is the SDK convention worth noting for retargeting (UniDexGrasp -> L20 mapping exists in the vendor repo).
