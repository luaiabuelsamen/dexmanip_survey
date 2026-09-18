# pisa_iit_softhand_2014 — Adaptive synergies for the design and control of the Pisa/IIT SoftHand (Catalano, Grioli, Farnioli, Serio, Piazza, Bicchi; IJRR 33(5) 2014)

sources: papers/md/pisa_iit_softhand_2014.md [ee9c3add = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17 from centropiaggio.unipi.it PDF] ; code/md/pisa_iit_softhand_2014.md [174eebc6, github.com/CentroEPiaggio/pisa-iit-soft-hand]
The md has no markdown headings (PDF text); line numbers below refer to the md.

## One-line contribution
One motor, 19 joints: a tendon-differential "adaptive synergy" hand whose rolling-contact joints with elastic ligaments make it shape-adaptive and able to survive over-extension and impacts (Abstract; Sec. IV).

## Hand record
- maker: Centro E. Piaggio / University of Pisa and IIT (from the hand's name and the repo owner CentroEPiaggio; affiliation footnotes are not in the md). country: Italy (Pisa; not spelled out).
- DoF: "The hand has 19 joints, but only uses one actuator to activate its adaptive synergy" (Abstract); "19 DOFs arranged in four fingers and an opposable thumb (fig. 11)" (Sec. IV, l. 880). Plus a compliant wrist "allowing for three passively compliant DOFs" (l. 901-902). Code: soft_hand_full_control.yaml names 19 joints (index/middle/ring/little: abd, inner, middle, outer; thumb: abd, inner, outer), consistent.
- actuated DoF: 1 (soft_hand_synergy_joint is the only controlled joint in every example config, code/md l. 161-193).
- actuation: tendon. "one tendon routed through all joints using passive anti-derailment pulleys. The tendon action flexes and adducts fingers and thumb, counteracting the elastic force of ligaments" (Fig. 15 caption, l. 1024-1026); a servomotor with two differential gears feeds three tendons per stage (l. 840-845). Motor: "6 W Maxon motor RE-max21 with a reduction ratio of 84:1 equipped with a 12 bit magnetic encoder (Austrian Microsystems AS5045) with a resolution of 0.0875°" (Sec. V, l. 1041-1044).
- joints: COmpliant Rolling-contact Element (CORE) joints; "elastic ligaments are polyurethane rubber segments of 2mm diameter, characterized by 88 Shore A hardness. The rest length of the ligaments is 10mm" (l. 995-997); rolling cam radius 6.5 mm, tendon pulleys 3.5 mm (l. 1003-1005).
- fingers: four fingers plus opposable thumb; "Each finger has four phalanges, while the thumb has three" (l. 899-900).
- thumb design: three phalanges, abduction joint plus two flexion joints (code joint names thumb_abd/inner/outer); opposable (Sec. IV).
- weight: not stated in the paper text (no match for weight/kg). Bib "~0.5 kg" for the commercial qb SoftHand is a bib-claim.
- fingertip force / grasp force: "maximum holding torque of 2 Nm and maximum holding force of about 20 N along the z axis. These limits appear to be dictated by the motor size"; "with a stronger motor a holding torque of 3.5 Nm and holding force of 28N were obtained" (Sec. V.A, Fig. 19, l. 1071-1129). Measured with an ATI nano 17 on a 45 mm split cylinder and a 95 mm disk.
- tactile sensing: none. Sensing is the motor encoder; during experiments "the hand worn an off-the-shelf working glove with padded rubber surfaces, supplying contact compliance and grip" (l. 1054-1056).
- control interface and rate: "The opening/closing of the hand is controlled via a single set point reference, communicated via one of the available buses (SPI and RS-485)" (l. 1047-1049); electronics and battery pack in the hand back. Rate not stated. Code: ROS position controller on soft_hand_synergy_joint, joint_state publish_rate 100 (adaptive_example/config/controllers.yaml); README says "These packages assume you use qbTools to move the hand, since it is the electronics the hand is sold with."
- dimensions: ~230 mm span thumb-to-little tip, 235 mm wrist-to-middle tip, 40 mm palm thickness (l. 918-921).
- price: not stated; "cost effectiveness" is a design requirement (l. 878).
- open-hardware?: the ROS/Gazebo model repo is BSD 3-Clause (README); hardware CAD is not in this repo.
- release status and date: IJRR vol. 33 no. 5, pp. 768-782, 2014 (repo README). Commercial qb SoftHand / SoftHand2 (bib) are bib-claims; the sources only say the hand "is sold with" qbTools electronics.
- used by (grep -l -i "pisa/iit|pisa-iit|softhand|qb hand|qbhand|qbrobotics", self excluded): bai_unified_manip_survey_2025, ilda_hand_2021, robotera_xhand1_2024, welte_iil_survey_2025.

## Setting
- hand(s): Pisa/IIT SoftHand prototype; single hand; mounted on a KUKA Light-Weight robot arm for robot experiments (Sec. V.B, l. 1142-1144).
- simulator / physics: none for the hardware paper; the code repo provides Gazebo models (adaptive, full-actuated, kinematic-synergy, two-hands examples).
- observation: motor position only.
- action space: one synergy set point.
- objects / data: household objects (schoolbag, USB cable, glue stick, wallet, credit card, sponge, ..., l. 1202); objects listed with sizes 37-205 mm (l. 1211-1225).

## Method
- paradigm: mechanical co-design; "adaptive synergy" underactuation synthesised to reproduce the first soft synergy from the Santello et al. 1998 human postural database (l. 883-888).
- loss / synthesis: transmission matrix R and joint stiffness matrix K_q^a are chosen numerically so that the underactuated hand matches a desired soft synergy (eqs. (21), (23), l. 889-891). Tendon differential: joint torques relate to actuator force through R with "R_ij is the transmission ratio between the ith actuator to the jth joint" (l. 635-636).
- actuation schemes reviewed before choosing adaptive synergy (Sec. III): fully actuated hand with soft synergies via agonist-antagonist actuators per joint (fig. 4, l. 499-516), versus differential/underactuated transmission that "reduces the number of actuators without decreasing the number of DOF" (l. 582); the paper's count of distinct position/force-controlled cases "is eight" (l. 745).
- key trick(s): rolling-contact joints held by elastic ligaments instead of pins, so joints "can withstand severe force overexertion in all directions, automatically returning to the correct assembly configuration" (Fig. 16 caption, l. 1163).

## Evaluation
- metrics: holding force (N) and holding torque (Nm) on sensorised objects (ATI nano 17; split cylinder 120 mm x 45 mm dia.; disk 20 mm x 95 mm dia., Sec. V.A, l. 1060-1066); qualitative grasp success, no counts.
- grasp conditions (Sec. V.B, l. 1136-1140):
  1) hand wrist fixed on a table, object placed in the grasp (Fig. 20);
  2) object on a table, hand on a robot arm (Fig. 21: handbag, spray, cup, telephone);
  3) hand wrist fixed to the forearm of a human operator (Fig. 22; the operator's EMG/position interface is described around l. 1197-1199).
- objects (l. 1202, 1246): schoolbag, USB cable, glue stick, wallet, credit card, sponge, lock, square ruler, scissors, eyeglasses, deodorant, USB key; listed sizes range 37-205 mm (l. 1211-1225).
- headline numbers: 20 N / 2 Nm with the stock 6 W motor; 28 N / 3.5 Nm with a stronger motor (Sec. V.A). No success rates or counts are reported.
- baselines beaten: none quantified.
- real robot?: yes, KUKA LWR with pre-programmed reach and a closure command, "no grasp planning phase" (l. 1145-1149); on-the-fly grab of a water bottle with the arm sweeping "at a speed of 1 m/s ca." (l. 1169-1170).

## Limitations stated by the authors
- "No in-hand dexterous manipulation is required for this prototype." (Sec. IV, l. 873)
- Force limits "dictated by the motor size rather than by the hand construction" (l. 1125-1126).
- "while all grasps could be easily achieved by the hand when operated by a human, programming the robot to achieve the same grasps was in some cases rather complex" (l. 1255-1258); they suggest learning/planning for soft hands should focus on "constraint-based motion rather than on free-space, multi-DOF hand shaping" (l. 1265-1267).

## Quotable claims (verbatim, with section)
- "The hand has 19 joints, but only uses one actuator to activate its adaptive synergy." (Abstract)
- "The hand should be lightweight and self-contained, to avoid encumbering the forearm and wrist with motors, batteries and cabling, along with cost effectiveness." (Sec. IV)
- "We achieved a maximum holding torque of 2 Nm and maximum holding force of about 20 N along the z axis." (Sec. V.A)

## Notes for the survey
- The canonical single-synergy argument for the actuation-count section; contrast with ILDA (15 motors, 34 N fingertip) and Shadow (20 motors). Note the paper reports whole-hand holding force, not fingertip force, so it is not directly comparable to fingertip numbers.
- Weight and price are absent from the paper; do not quote the bib's 0.5 kg as measured.
