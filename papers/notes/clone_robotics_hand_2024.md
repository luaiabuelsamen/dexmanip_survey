# clone_robotics_hand_2024 — Clone Robotics hydraulic Myofiber hand (27 DoF) (Clone Robotics, company announcement, unreleased)

sources: papers/md/clone_robotics_hand_2024.md [sha256 2ba57045; no manifest entry, hash computed from file] ; no code
source: press. (1) There's A Robot For That newsletter, "Clone's robot hand has artificial muscles" (undated; its other items cite news of 2025-11-24); (2) Interesting Engineering, "Video: Clone demos creepy humanoid hand with human-level grip strength and speed", Atharva Gosavi, Nov 24, 2025, about a Clone X post of November 15, 2025. Specs are vendor claims relayed by press, not measurements. bib year is 2024; the hand demo in both sources is November 2025. bib entry marked verified: false.

## Hand block
- maker / country: Clone Robotics / Poland ("Polish robotics company")
- DoF: 27 ("It has 27 degrees of freedom")
- actuated DoF: not stated as a count; "fully actuated" is claimed in Clone's post ("Building a fully actuated, human-level robotic hand"). Plumbing: "A 500-watt water pump and 36 electro-hydraulic valves"
- actuation: hydraulic artificial muscle ("synthetic Myofiber muscles ... the small tubes of water that contract when pressurized"), on "carbon-fiber bones and ligament-style tethers"; "each Myofiber can generate up to 1 kilogram of grip force"; "survived 650,000 test cycles without fatigue"
- fingers: 5 implied ("anthropomorphic"); not stated
- thumb design: not described
- weight: "under 2 pounds" (≈0.9 kg; conversion mine). Whether the pump is included is not stated.
- fingertip force: not stated; "human-level grip strength and speed" (Clone's own claim, quoted)
- tactile sensing: "pressure pads in the palm detect how firmly the hand grips an object" (count not given); proprioception: "70 inertial sensors tracking angle and speed"
- control interface / rate: not stated. Controller: "Neural Joint V2 Controller", "a neural network trained on hours of footage of human hands moving"; input is an operator "wearing a sensor glove"; "Earlier versions relied on basic, hardcoded control systems"
- price: none
- open-hardware: no
- release status / date: unreleased as a separate product; "a key part of the Clone Alpha Robot", of which Clone "plans to produce only 279 Alpha units" (via Humanoids Daily). Alpha revealed December 2024; Protoclone V1 (full body, ">200 degrees of freedom, around 1,000 Myofibers, and 500 sensors") released February 2025. Not buyable separately.
- demonstrated vs specified: demonstrated only. The evidence is a teleoperated desk video (X, 2025-11-15) showing finger mirroring "with commendable speed and low apparent latency" (IE's description). No datasheet, no force or speed number. "Clone Robotics hasn't released a full demo of the robot with the hand."
- used by (grep clone robotics|myofiber|protoclone|clone alpha over code/md, papers/md): none besides this entry.

## bib `specs` claims vs sources
Confirmed: 27 DoF, Myofiber ~1 kg each, 650k cycles, 500 W pump + 36 valves, < 2 lb, 70 inertial sensors, palm pressure pads, Alpha 279 units. Not in sources: "unreleased (Clone Alpha pre-orders 2025)" wording; "hand shown 2024" (sources date the hand demo to Nov 2025).

## Setting / Method / Evaluation
No task or metric. The controller is glove teleoperation through a learned mapping; no autonomy is claimed.

## Quotable claims (verbatim)
- Clone (X, 2025-11-15): "Building a fully actuated, human-level robotic hand by strength, speed, and range of motion is hard. Making it incredibly durable is even more challenging."
- IE: "A 500-watt water pump and 36 electro-hydraulic valves deliver the right pressure through Clone's synthetic Myofiber muscles"
- Newsletter: "or just another impressive prototype that struggles outside the lab"

## Notes for the survey
- The hydraulic musculoskeletal extreme: 27 DoF, off-hand pump, learned joint controller. Everything is press-relayed and video-only; no number here is a measurement.
- 36 valves for 27 DoF suggests fewer independent channels than muscles (Protoclone quotes ~1,000 Myofibers body-wide); the hand's muscle count is not given.
