# daxo_muscle_v0_2025 — Daxo Robotics Muscle V0 (120-actuator compliant tendon hand) (Daxo Robotics, company announcement, unreleased)

SOURCE THIN: the vendor page (https://www.daxo-robotics.com/) returned HTTP 404. The only fetched source is a third-party catalogue post (humanoid.guide, "Welcome, Muscle V0!", September 16, 2026). Nothing below is from the maker directly.

sources: papers/md/daxo_muscle_v0_2025.md [sha256 df5eff45; no manifest entry, hash computed from file] ; no code
source: third-party catalogue page; specs are as relayed by humanoid.guide, not measurements. bib entry marked verified: false.

## Hand block (from humanoid.guide only)
- maker / country: Daxo Robotics / not stated
- DoF: not stated as a number; the post gives a "5 out of 5" DoF rating on its own scale
- actuated DoF: "120 individual actuators" ("distributes motion across 120 small motors")
- actuation: tendon ("ultra redundant tendon driven architecture"), "compliant structure contains no rigid joints, using flexible materials and tendon routing"
- fingers: "five finger layout"
- thumb design: not described
- weight: 0.75 kg
- fingertip force: not stated; "strength rating is in a lower tier"; "precise, adaptable interaction takes precedence over high force handling"
- tactile sensing: not stated ("tactile interaction experiments" named as a use case only)
- control interface / rate: not stated
- price: not stated
- open-hardware: not stated
- release status / date: "currently a prototype, with Daxo Robotics preparing a limited release for Fall 2026"; "tested the design through more than 100,000 actuation cycles and continues durability testing". Not buyable at post date. Redundancy claim: "supporting continued operation when individual actuators are unavailable".
- demonstrated vs specified: neither; a catalogue description with a site-specific "Hand Score of 6".
- used by (grep daxo over code/md, papers/md): none besides this entry.

## bib `specs` claims NOT confirmed by the page (unverified)
"108 artificial muscles (3x human)"; "all actuators backdrivable with force sensing"; "~$1,200 prototype cost"; "V2 Q3 2026". The page says 120 actuators and a V0 limited release in Fall 2026; it never mentions 108, a V2, backdrivability, force sensing, or a price.

## Setting / Method / Evaluation
None.

## Quotable claims (verbatim, humanoid.guide)
- "engineered around an ultra redundant tendon driven architecture with 120 individual actuators"
- "Its compliant structure contains no rigid joints"
- "Muscle V0 is currently a prototype, with Daxo Robotics preparing a limited release for Fall 2026."

## Notes for the survey
- The redundant-actuation extreme of the design space (120 actuators, 0.75 kg), but only as a third-party description; cite as "reported by humanoid.guide", never as a spec.
- Re-fetch the vendor site before the hand enters any table.
