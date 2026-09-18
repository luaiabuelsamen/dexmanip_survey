# ilda_hand_2021 — Integrated linkage-driven dexterous anthropomorphic robotic hand (Kim, Jung, Jeong, Park, Jung, Cheong, Choi, Do, Park; Nature Communications 12:7177, 2021)

sources: papers/md/ilda_hand_2021.md [007809c4 = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17 from nature.com PDF] ; no code
The md has no markdown headings (PDF text); line numbers refer to the md.

## One-line contribution
A five-finger hand with all 15 motors, drivers and fingertip F/T sensors inside the palm, each finger a 3-DoF linkage module (2-DoF MCP parallel mechanism + 1-DoF PIP serial linkage), reaching 34 N fingertip force at 1.1 kg (Abstract; Table 1).

## Hand record
- maker: Ajou University (Suwon), Korea Institute of Machinery & Materials (Daejeon), Korea University (Sejong) and a fourth department cut off in the md (author affiliations, l. 33-34). country: Korea.
- DoF: "15-degree-of-freedom (20 joints)" (Abstract); Table 1 "Active DOF 15 DOF/20 joints". Per finger: 2-DoF MCP (flexion 0-90°, abduction ±35°) and 1-DoF PIP (0-90°) driven independently; DIP coupled to PIP through a second four-bar (l. 205-213, 299, 451-457).
- actuated DoF: 15 (15 motors, "three motors" per finger, l. 228, 419).
- actuation: linkage-driven, direct linear drive. Per finger three Maxon DCX 8 M motors (8 mm) with GPX8 16:1 gearboxes and ENX 8 mag encoders driving KSS SR0401K ball screws on IKO LWL3 linear guides; two PSS chains form the MCP parallel mechanism, one PSU chain plus a crossed four-bar drives PIP, another four-bar drives DIP (Methods, l. 719-731; Fig. 3). Rod ends act as ball joints (l. 398-407). Frame parts SUS303 steel, rest aluminium 6061.
- fingers: five, "all fingers were designed with the same structure ... Only the lengths of the thumb and little fingers were different" (l. 419-423).
- thumb design: same 3-DoF module as the fingers with different link lengths; no dedicated opposition mechanism is described in the text read.
- weight: 1.1 kg (Table 1; Abstract). Max hand length 218 mm, overall 261 mm.
- fingertip force: 28 N stretched pose, 34 N bent pose (Table 1; Fig. 6b, l. 486-487); 25 N per finger measured while crushing an aluminium can (l. 499-500). Payload 18 kg (Table 1). Backdrive torque 25.9 mNm (MCP), 6.3 mNm (PIP) (l. 458-460). Joint speed 53, 103, 81 °/s (q1, q2, q3) (Table 1).
- tactile sensing: one six-axis F/T sensor per fingertip, five total (l. 434-437, 798-806); Table 1 "Force resolution 62 mN, Force range ±35 N"; a rubber-covered rigid inner part transmits load; contact location and triaxial force derived by algorithm (Supplementary Text 4). Validated against an ATI Nano25: 0.9 N average static error, 0.53 N dynamic error on a 21 N sinusoid (l. 487-493). Not a distributed skin.
- control interface and rate: CAN bus to a desktop; DC 15 V, 2 A max (Table 1). Electronics: main STM32F407, eight STM32F411 slaves over SPI, eight Allegro A3909 dual full-bridge drivers, fingertip sensors over I2C (l. 745-752). Position control of motors along synergy trajectories (l. 763-785). Loop rate not stated.
- price: not stated; low cost and "market penetration" are stated goals (l. 380-384, 670-679).
- open-hardware?: no. No repository; "All data ... available from the corresponding author upon reasonable request" (l. 818-819).
- release status and date: research prototype; received 10 Sep 2020, accepted 5 Nov 2021 (l. 815).
- used by (grep -l -i "\bilda\b|ilda hand", self excluded): an_dexil_survey_2025, gr_dexter_2025, zhao_dexhand_survey_2026.

## Setting
- hand(s): ILDA hand; single; mounted on a UR-5 (payload 5 kg) synchronised by digital I/O (l. 754-758).
- simulator / physics: a "visual simulator of the ILDA hand" is used only to predict joint-angle vectors per grasp type (l. 774-776); no physics engine named.
- observation: motor encoders and fingertip F/T.
- action space: motor position targets computed from synergy coefficients (q = S σ, l. 767-769).
- objects / data: YCB objects (Supplementary Fig. 6, Video 3); aluminium can, egg, scissors, tweezers, a 0.9 mm x 6 mm chip (l. 602).

## Method
- paradigm: mechanism design plus hand-synergy control: "The joint angle representation using synergy vectors is given by q = Sσ where q is the joint angle of the robotic hand, S is the synergy vector, and σ is the coefficient of the synergy vector" (l. 767-769). 14 grasp types chosen from Feix's taxonomy; PCs computed from simulated joint trajectories over object sizes (l. 773-779). Manipulation actions taught and decomposed into single-PC components (l. 786-796).
- key trick(s): parallel + serial linkage fusion to get an independent PIP ("a linkage-driven robotic finger with 3-DOF has not been investigated so far", l. 197-199); rod ends as high-load ball joints; LM guide arranged to cancel ball-screw torque (l. 700-703).

## Evaluation
- metrics: fingertip force vs reference sensor, force magnitude F_mag = sqrt(Fx^2 + Fy^2 + Fz^2) compared between fingertip and Nano25 (Fig. 6a-c, l. 461-493); qualitative grasp/manipulation success.
- joint ranges measured (l. 451-457): MCP flexion 0-90°, PIP flexion 0-90° independent of MCP, abduction/adduction ±35°.
- reliability tests (Fig. 7, Supplementary Text 5, l. 518-524): long-time operation, long-duration grasp, repeatability, high payload, heating/current. Results are in the supplement, not in the md.
- headline numbers: 34 N bent / 28 N stretched fingertip force; 18 kg payload; 1.1 kg; 218 mm (Table 1).
- baselines beaten: none quantified; the Discussion contrasts with tendon hands that need a forearm (l. 644-648).
- prior hands the introduction positions against (l. 59-132): the JHU/APL hand "with active 22 DOF and a compact design integrating actuators and electronics" (l. 70-72) but high finger inertia and cost; tendon hands with forearm actuators (l. 84); the Schunk SVH 5-finger hand (l. 120); linkage fingers so far limited to 1-2 subordinated DoF (Supplementary Table 1, l. 195-199).
- real robot?: yes, UR-5; scissors paper cut and tweezers chip transfer (Fig. 8); no trial counts or success rates given.

## Limitations stated by the authors
- "it was difficult to accurately quantify the effectiveness of the hand in manipulating tools using scissors" (l. 654-655).
- Holding tweezers "is not easy" (l. 660-662).
- High-DoF dexterous hands remain "an open issue" (l. 668-670).

## Quotable claims (verbatim, with section)
- "It has the following features: 15-degree-of-freedom (20 joints), a fingertip force of 34N, compact size (maximum length: 218 mm) without additional parts, low weight of 1.1 kg, and tactile sensing capabilities." (Abstract)
- "most of the integrated hands that implement a high DOF have weak gripping force (or fingertip force) and payload." (Discussion, l. 644-646)

## Notes for the survey
- Reference point for linkage-driven, forearm-free hands: 15 motors in the palm, 34 N fingertip, 1.1 kg. Compare Shadow (20 motors, 4.3 kg with forearm, 4 kg payload) and Inspire RH56DFX (6 motors, 540 g, 10-15 N).
- "Tactile" here means a 6-axis F/T sensor per fingertip, not a taxel array; keep this distinct from XELA/Shadow STF style skins in the tactile table.
- No public code or CAD; cites a $150-parts hand (ref. l. 852) and low-cost antagonistic servo hands (l. 855) as prior low-cost work.
