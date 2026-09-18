# proception_prohand_2026 — Proception ProHand 1.0 (22-DoF tendon-driven hand) (Proception Inc, company announcement 2026)

sources: papers/md/proception_prohand_2026.md [sha256 ae97ab2f; no manifest entry, hash computed from file] ; no code
source: vendor launch post (Y Combinator launch page, JSON dump, created 2026-06-29) and press (TechCrunch, "Robot hand company settles Tesla trade secret suit and announces $11M raise", June 29, 2026, Sean O'Kane). Specs are manufacturer claims, not measurements. bib entry marked verified: false.

## Hand block
- maker / country: Proception Inc (YC W25; "We are building ProHand in Mountain View") / USA
- DoF: 22 ("Twenty-two degrees of freedom, with multiple joints per finger"; TechCrunch: "The hand has 22 degrees of freedom and multiple joints per finger")
- actuated DoF: not stated
- actuation: tendon ("Tendon-driven actuation, where motors pull cables to move the fingers while keeping the hand lightweight and compact")
- fingers: five implied by "human-like"; count not stated explicitly
- thumb design: not described
- weight: not stated ("lightweight")
- fingertip force: not stated
- tactile sensing: "Integrated skin-like sensors, which detect contact and support grip control"; the same "sensor skin" is used in the ProGlove; type and count not stated. bib "dense tactile feedback" is a paraphrase, not a page number.
- control interface / rate: not stated. "ProHand supports standard teleoperation workflows out of the box."
- price: not stated; orders via proception.ai/product/pro-hand/gen1 ("you can order ProHand on our website")
- open-hardware: no
- release status / date: "the first batch of units is shipping this week to researchers and robotics companies" (launch post dated 2026-06-29; TechCrunch same day: shipping first batch "while opening up to wider orders"). Sold separately, yes. Funding: $11M seed led by First Round Capital with Y Combinator and BoxGroup. Founder Jay Li was "a technical lead on Tesla's Optimus humanoid robot program"; Tesla's trade-secret suit was settled and "dismissed earlier this month" (June 2026).
- demonstrated vs specified: no datasheet in either source. The launch post links a YouTube video (S61xWpz7_qM), content not in the source. Design claims: "built to be impact tolerant, serviceable"; "worked closely with hand surgeons".
- used by (grep proception|prohand over code/md, papers/md): none besides this entry.

## Setting / Method / Evaluation
No task or metric. Data-collection thesis: teleoperation "loses important human interaction signals"; ProGlove "turns the same sensor skin used on ProHand into a wearable data collection system ... without needing a robot in the loop", paired with a headset for vision.

## Limitations stated by the vendor
None stated. TechCrunch quotes Kevin Lynch (Northwestern) via WSJ that human-equivalent hands are "a decade" away, as the counter-view.

## Quotable claims (verbatim)
- "Tendon-driven actuation, where motors pull cables to move the fingers while keeping the hand lightweight and compact." (launch post)
- "Our bet is simple: the fastest path to dexterous robots is to build hardware close enough to the human hand that we can learn from human hands directly." (launch post)
- Bill Trenchard (First Round): "We think they will have the best hand in the market, maybe the most sophisticated hand today" (TechCrunch; investor opinion)

## Notes for the survey
- Startup-hand row: 22 DoF tendon, skin sensor, shipping June 2026, all numbers beyond "22" absent. Do not fill weight/force/tactile from the bib; the bib has none either.
- Pairs with the human-data-glove theme (Xiaomi tactile gloves, Wuji Glove, Sharpa): same "sensor skin on hand and glove" argument.
