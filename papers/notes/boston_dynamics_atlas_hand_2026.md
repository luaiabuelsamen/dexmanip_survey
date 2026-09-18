# boston_dynamics_atlas_hand_2026 — Boston Dynamics electric Atlas hands (Boston Dynamics, company announcement Jan 2026, unreleased)

sources: papers/md/boston_dynamics_atlas_hand_2026.md [00dd08d0, sha256 of the parsed page; no manifest entry, fetched 2026-09-17: bostondynamics.com CES press blog (Jan 5 2026) + humanoidsdaily.com CES 2026 article] ; no code
source: vendor press blog and trade press; claims, not measurements. Note: the Boston Dynamics blog text contains no hand content at all (robot-level only); every hand statement below is from Humanoids Daily. The bib `specs` for the 2025 hand — 3 fingers, 7 DoF, 7 actuators — do not appear on disk (Humanoids Daily links a "three-fingered gamble" article that was not fetched) and are unverified bib-claims.

## One-line contribution
The production electric Atlas (CES, Jan 5 2026) carries a four-digit gripper — three fingers plus an opposable thumb — with tactile sensing in fingers and palm, replacing the earlier three-finger hand; the counterexample to five-finger humanoid hands.

## Setting
- hand(s): Atlas production hand; Boston Dynamics (Boston, USA; majority owner Hyundai Motor Group). Not sold separately; the robot's 2026 output is "fully committed" to Hyundai RMAC and Google DeepMind
- robot context (BD blog): "56 degrees of freedom, fully rotational joints, a reach extending to 2.3M (7.5 ft), and the strength to lift up to 50 kg (110 lbs)"; -20 to 40 C; controlled "autonomous mode, teleoperated, or by using a tablet steering interface"; actuators supplied by Hyundai Mobis
- simulator / observation / action: not stated

## Hand record (Humanoids Daily unless marked; bib-claim = from `specs`, not on disk)
- maker / country: Boston Dynamics, USA
- DoF: not stated for the production hand. bib-claim (2025 hand): 7 DoF, 7 actuators. actuated DoF: not stated
- actuation: electric (robot is "fully electric"); mechanism not stated
- fingers: 4 digits — "three fingers and an opposable thumb"; earlier design three-fingered ("we previously analyzed their strategy as a three-fingered gamble")
- thumb design: "opposable thumb"; nothing more
- weight / fingertip force: not stated
- tactile sensing: "equipped with tactile sensing in the fingers and palms"; type and count not stated
- control interface and rate: not stated
- price: none; not sold
- open-hardware?: no
- release status and date: unveiled Jan 5 2026 at CES; production "immediately" at Boston HQ; deployments 2026 at Hyundai RMAC and Google DeepMind, additional customers "early 2027" (BD blog); HMGMA Georgia "by 2028"; 30,000 robots/yr factory planned. The robot on the CES stage "was a research prototype piloted by a Field Applications Engineer"
- used in corpus: no paper or repo uses the hand. Robot-level mentions: humanoidbench_2024 ("Boston Dynamics Atlas, Tesla Optimus, Unitree H1" hardware progress), bai_unified_manip_survey_2025 ("Boston Dynamics Atlas" listed), isaaclab_2025 / isaac_lab_2025 (Atlas athletic skills figure), humanplus_2024 and physics_engine_comparison_2015 (older hydraulic Atlas citations), ilda_hand_2021 (cites bostondynamics.com/atlas), figure_03_hand_2025 (tracker names a former BD CTO)

## Method
- n/a. Design rationale (Humanoids Daily): "function over form"; four digits as the "sweet spot" for reliability in "parts sequencing and machine tending" (the article's inference, "likely aims"). Robot uses "only two unique actuator designs"; System 1 / System 2 control split with Gemini Robotics integration.

## Evaluation
- demonstrated in video: none hand-specific on disk; "autonomous material handling has already been proven in field tests at HMGMA" (article, no numbers).
- specified in a datasheet: robot-level only (56 DoF, 1.9 m, 90 kg, 50 kg instant / 30 kg sustained payload, ~4 h dual swappable batteries, IP67). Nothing for the hand.

## Limitations stated by the authors
Executives "acknowledge that the industry is still in Phase One — the grueling grind of proving hardware reliability" (Humanoids Daily).

## Quotable claims (verbatim, with section)
- "The production-ready version of Atlas features a four-digit gripper—three fingers and an opposable thumb—equipped with tactile sensing in the fingers and palms." (Humanoids Daily, "The Four-Digit Compromise")
- "Atlas has 56 degrees of freedom, fully rotational joints, a reach extending to 2.3M (7.5 ft), and the strength to lift up to 50 kg (110 lbs)." (BD blog)

## Notes for the survey
- Hardware table: the one non-five-finger humanoid hand; DoF cell must be blank (or "7, bib-claim for the 2025 three-finger hand"). Tactile-in-palm is the only sensing fact.
- Contrast with 1X (25 DoF) and Tesla V3 (22 DoF reported): Boston Dynamics trades DoF for reliability, explicitly for industrial sequencing rather than general manipulation.
