# leap_hand_v2_adv_2025 — LEAP Hand V2 Advanced: Dexterous, Low-Cost Hybrid Rigid-Soft Hand for Robot Learning (Shaw and Pathak, IEEE Humanoids 2025 per bib; page itself carries no venue)

sources: papers/md/leap_hand_v2_adv_2025.md [f7d63dc7 = sha256 of the md on disk; corpus/manifest.json has no entry, pages_manifest fetched 2026-09-17 https://v2-adv.leaphand.com/] ; code/md/leap_hand_v2_adv_2025.md [a0936196, github.com/leap-hand/LEAP_Hand_V2_Adv_API]
source type: project page (abstract + feature captions) plus API README. No paper body was fetched; everything below is what the page and README say, i.e. author claims, not measurements.

## One-line contribution
A $3000 five-finger hand whose fingers are multi-material 3D printed (TPU soft exterior over PLA internal bones), with two powered palm articulations and a side-swing MCP joint, positioned for teleop and imitation-learning data collection (page, Abstract).

## Hand record
- maker: Kenneth Shaw, Deepak Pathak, Carnegie Mellon University (page header). country: USA (CMU; the page does not spell the country out).
- DoF: "21 DOF with 17 powered motors" (page, "Dexterous MCP Side Joint" caption). The README calls it a "17-DOF hybrid rigid-soft robotic hand", i.e. it counts motors, not joints. Note the mismatch when quoting.
- actuated DoF: 17 motors. README "Motor Command Order" table: per finger (Index, Middle, Ring, Pinky, Thumb) MCP side, MCP forward, curl = 15, plus Palm (Thumb) and Palm (Fingers) = 17.
- actuation: tendon for the finger curl ("The MCP joints have a strong rigid structure, while the PIP and DIP joints are coupled via a single tendon", page; README: "you do not have independent control of PIP and DIP as they are coupled by a tendon"). Motor type is not named on the page or in the README; the README's realign.py "uses current control mode to find fully open and closed positions" and warns about "tendon slippage".
- fingers: five (README finger order Index, Middle, Ring, Pinky, Thumb).
- thumb design: README pose array gives the thumb MCP side, "palm thumb forward", "MCP thumb forward" and "thumb curl"; the page adds a powered palm articulation "near the thumb" (Abstract).
- weight: not stated.
- fingertip force: not stated.
- tactile sensing: none mentioned.
- control interface and rate: ROS 2 Humble on Ubuntu 22.04, pure-Python API; position control; accepts a 20-D pose array (glove/mocap) or a direct 17-D motor vector; joint position/velocity/effort via ROS 2 services (README). Command ranges: MCP side -1.57..1.57 rad, MCP forward 0..~3 rad, PIP/DIP 0..1.57 rad, palm_4_fingers ~max 1 rad (README). Control rate not stated.
- price: "$3000" (page, Abstract). Bib "~$3000" confirmed. README: the non-Advanced LEAP Hand v2 is "a lightweight, 8-DOF version ... (~$200)".
- open-hardware?: claimed. Page: "We plan to release 3D printer files and assembly instructions ... upon acceptance of the paper"; page nav has Parts, CAD (link named "cad_request") and Assembly; "can be built within a day using our full instructions". A LICENSE file exists in the repo (leap_v2/LICENSE) but its text is not in the md.
- release status and date: API repo at commit a0936196; page has an arXiv link but no date. "IEEE Humanoids 2025", "released 2025" are bib-claims not confirmed by the page.
- used by (grep -l -i "leap hand v2|leap_hand_v2|leap v2|leapv2|v2-adv" over code/md and papers/md, self excluded): an_dexil_survey_2025, bidex_teleop_2024, dexwild_2025.

## Setting
- hand(s): as above; single hand; the page recommends Manus gloves for teleop ("I highly recommend Manus Gloves to take full advantage of the high DOF").
- simulator / physics: the telekinesis node "loads the URDF into PyBullet ... applies SDLS inverse kinematics" for fingertip-target retargeting (README, "Telekinesis Node").
- observation / action: position targets only (README).
- objects / data: page lists demo tasks only: drill operating, pouring in the wild, plate pickup (learned from mocap gloves); dining tray, hang shirt, grape pluck (teleop).

## Method
- paradigm: hardware design; the learning demos link to the Bidex teleop project (bidex-teleop.github.io) and the Robotic Telekinesis retargeting method (README).
- key trick(s): "3d printed soft exterior combined with a 3d printed internal bone structure"; "two powered articulations in the foldable palm: one spanning the four fingers and another near the thumb"; "dexterous Metacarpophalangeal (MCP) kinematic structure" (Abstract).

## Evaluation
- metrics / headline numbers: none on the page. The abstract says "Through thorough real-world experiments, we show that LEAP Hand v2 exceeds the capabilities of many existing robot hands for grasping, teleoperated control, and imitation learning" but gives no numbers.
- real robot?: yes by video captions; no trial counts.

## Limitations stated by the authors
None on the page. README notes calibration drift: "Re-run this occasionally if you notice inaccuracies or tendon slippage."

## Quotable claims (verbatim, with section)
- "We call our solution LEAP Hand v2, a dexterous, $3000, simple anthropomorphic hybrid rigid-soft hand that bridges this gap." (Abstract)
- "In total LEAP Hand v2 has 21 DOF with 17 powered motors." (page, MCP caption)
- "Note that you do not have independent control of PIP and DIP as they are coupled by a tendon." (README)

## Notes for the survey
- Feeds the open-hardware / low-cost hand table and the hybrid rigid-soft design section. Quote 21 joints / 17 motors, not "17 DoF".
- No weight, force, or tactile figures anywhere in the sources; do not fill them from memory.
