# sanctuary_phoenix_hand_2024 — Sanctuary AI Phoenix hydraulic hand (21 DoF) (Sanctuary AI, company announcement 2024, unreleased)

sources: papers/md/sanctuary_phoenix_hand_2024.md [f81786ef, sha256 of the parsed page; no manifest entry, fetched 2026-09-17: sanctuary.ai press release + automationmag.com reprint dated Dec 17 2024] ; no code
source: vendor press release and a trade-press reprint of it; specs are manufacturer claims, not measurements.

## One-line contribution
A 21-DoF hand actuated by miniaturised hydraulic valves, claimed an order of magnitude higher power density than cable or electromechanical drives, with valve actuators cycled >2 billion times, demonstrating in-hand manipulation on video (Dec 2024).

## Setting
- hand(s): Phoenix hands, Sanctuary AI, Vancouver, Canada; internal to the Phoenix general-purpose robot; site navigation lists them as "In Development: Robotic Hands" — not sold
- simulator / physics: none in the text (a sidebar headline "Sanctuary AI Leverages NVIDIA Isaac Lab to Accelerate Dexterous Learning" exists as a title only)
- observation / action space: not stated

## Hand record (press release unless marked; bib-claim = from `specs`, not on disk)
- maker / country: Sanctuary AI (Sanctuary Cognitive Systems Corporation), Canada
- DoF: 21 ("The company's 21 degrees of freedom (DOF) dexterous robotic hands"); actuated DoF: not stated. bib-claim: includes finger abduction
- actuation: hydraulic, "unique miniaturized hydraulic valves"
- fingers: not stated
- thumb design: not stated
- weight / fingertip force: not stated
- tactile sensing: not in the release text. Sidebar headlines only: "Sanctuary AI Equips General Purpose Robots with New Touch Sensors for Performing Highly Dexterous Tasks", "New Tactile Sensors Enable Richer Sense of Touch". bib-claim: haptic/tactile 2025 upgrade
- control interface and rate: not stated
- price: none; not sold
- open-hardware?: no
- release status and date: press release undated on the Sanctuary page; Automation Mag reprint Dec 17 2024; "In Development"; unreleased. bib-claim: internal to Phoenix Gen 7/8, 2024-2025 (sidebar titles mention a seventh and an eighth generation of Phoenix)
- used in corpus: none besides this key (the humanoid.guide tracker in figure_03_hand_2025 lists a "Phoenix" robot at 40,000 USD, a robot listing, not the hand)

## Method
- n/a. Claimed advantages of the hydraulic approach: "speed, strength, controllability, cycle life, impact resistance and heat management". Hands and the Carbon control system "designed in a modular format" for non-humanoid and humanoid integration.

## Evaluation
- demonstrated in video: in-hand manipulation (YouTube link in release); no task list, trials or success rates.
- specified in a datasheet: none; the only numbers are 21 DoF and 2 billion valve cycles, both in prose/quotes.
- real robot: Phoenix, in-house.

## Limitations stated by the authors
None stated.

## Quotable claims (verbatim, with section)
- "This method of hydraulic actuation offers an order of magnitude higher power density than cable and electromechanical-based systems" (release, para 2)
- "We have also recently achieved a milestone of testing our hydraulic valve actuators over 2 billion cycles without any signs of leakage or degradation." (James Wells quote)
- "Dexterous capability is directly proportional to the size of the addressable market for general-purpose humanoid robots" (James Wells quote)

## Notes for the survey
- Actuation taxonomy: the sole hydraulic entry; the power-density claim has no number or test behind it on disk. Pair with onex_neo_hand_2026 (tendon QDD) and tesla_optimus_hand_2025 (forearm tendon) as the three unreleased humanoid-hand architectures.
- Sidebar titles say Sanctuary trains policies for these hands with RL and Isaac Lab sim-to-real; those pages are not on disk, so do not cite results.
