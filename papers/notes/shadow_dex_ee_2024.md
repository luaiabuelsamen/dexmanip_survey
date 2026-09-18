# shadow_dex_ee_2024 — DEX-EE and DEX-EE Chiral: Shadow Robot hands developed with Google DeepMind (commercial product)

sources: papers/md/shadow_dex_ee_2024.md [b1b386c6 = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17 https://shadowrobot.com/dex-ee_series/] ; no code
source: vendor page; specs are manufacturer claims, not measurements. The page links a technical specification PDF (uploads/2026/05/Shadow-DEX-EE-Series-Technical-Specifications.pdf) that was not fetched, so most bib specs remain unverified.

## One-line contribution
A three-finger, 12-DoF, 4.1 kg hand designed with Google DeepMind for "long-running reinforcement learning experiments", with stereo-camera fingertip tactile sensors and 3-DoF taxel arrays on the middle and proximal phalanges; the Chiral variant offsets one finger like a thumb for teleop and bimanual imitation (page).

## Hand record
- maker: Shadow Robot Company, "in collaboration with Google DeepMind" (page). country: not on this page (UK per the shadow_dexterous_hand_2005 spec address).
- DoF: "12 DoF" for both DEX-EE and DEX-EE Chiral (page spec tiles).
- actuated DoF: not stated on the page (bib "15 Maxon DCX16 motors, >1 motor per joint" is a bib-claim).
- actuation: not stated on the page (bib "tendon" is a bib-claim). Page: "High bandwidth torque and position control loops give delicate and precise fingertip dexterity".
- fingers: "A robust 3 fingered robot" (page). DEX-EE "is a symmetric hand, unlike the human hand"; DEX-EE Chiral "moves the third finger down and to the side, creating an offset like the human thumb", sold as Left, Right and Bi-Manual Pair (page).
- thumb design: none on DEX-EE; on Chiral the offset third finger plays the thumb role.
- weight: "4.1 kg" (page). Height "350mm".
- fingertip force: not stated on the page (bib "0.01-18 N sensing, 10 N pinch" are bib-claims).
- tactile sensing: "Stereo camera-based fingertip tactile sensors ... hundreds of taxels each, with a massive dynamic range"; "Multi-taxel, 3 DOF tactile sensors on middle and proximal phalanges"; "hundreds of channels of tactile sensor data per finger"; plus "position, force and inertial measurements" and "Torque and inertial measurement throughout" (page). Counts are not given.
- control interface and rate: "high-speed sensor networks"; "Fully ROS integrated"; fail-safes and "a graceful shutdown routine" (page). No rate stated (bib "10 kHz internal force control" is a bib-claim).
- price: not stated ("Book a call"). Bib "~2/3 the price of the Dexterous Hand" is a bib-claim.
- open-hardware?: no.
- release status and date: "Now available for purchase, DEX-EE & DEX-EE Chiral" (page, © 2026); no launch date on the page (bib "released 2024" is a bib-claim).
- used by (grep -l -i "dex-ee|dex_ee|dexee", self excluded): an_dexil_survey_2025 (shadow_dexterous_hand_2005 also matches via its page navigation only).

## Setting
- Robustness claims: "tested for maximal endurance in harsh learning experiments"; "Resistant against repeated impacts from its environment and aggressive use from an untrained policy"; "Long mean time to failure and reduced time for repair" (page).
- Case studies on the page concern the Shadow Dexterous Hand, not DEX-EE: OpenAI's Rubik's cube ("trained their system entirely in simulation via reinforcement learning ... No fine-tuning needed"), Google Brain's deep dynamics models ("manipulate multiple objects with just four hours of real-world data"), Human Brain Project simulation.

## Method / Evaluation
None on the page; no numbers beyond DoF, weight and height.

## Limitations stated by the vendor
- DEX-EE's symmetric kinematics are a poor match for human teleoperation, which motivates Chiral: "If you want to do human teleoperation, or copy bi-manual human manipulation styles, you want a robot hand that more closely matches the human hand" (page).

## Quotable claims (verbatim)
- "Designed to reliably meet the needs of long-running reinforcement learning experiments" (page)
- "Stereo camera-based fingertip tactile sensors provide an unprecedented level of 3D interaction detail in a robust package" (page)

## Notes for the survey
- Feeds the "hardware designed for the learning loop" section and the vision-based tactile column (stereo fingertip cameras). Only 12 DoF / 3 fingers / 4.1 kg / 350 mm are page-confirmed; fetch the linked spec PDF before quoting motor count, force range or control rate.
- Only one corpus paper (an_dexil_survey_2025) mentions DEX-EE.
