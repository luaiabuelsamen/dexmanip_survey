# robotera_xhand1_2024 — ROBOTERA XHAND1 dexterous hand (ROBOTERA, commercial product 2024)

sources: papers/md/robotera_xhand1_2024.md [0702f2f0, sha256 of the parsed page; no manifest entry, fetched 2026-09-17 from humanoid.guide/product/xhand1/] ; no code
source: third-party tracker page (humanoid.guide), not the vendor; specs are manufacturer claims relayed by a tracker, not measurements. The vendor page (robotera.com/en/goods1/4.html) is linked but was not fetched.

## One-line contribution
A five-finger, 12-active-DoF hand with a tactile sensor on every fingertip and a 25 kg palm-up lift claim, listed at 14,000 USD by a tracker and sold separately from ROBOTERA's humanoid.

## Setting
- hand(s): XHAND1, Robotera, China (tracker "Nationality | China"); "Availability | In production"
- simulator / physics: none on the page
- observation / action space: none on the page

## Hand record (tracker page unless marked; bib-claim = from `specs`, not confirmed by page)
- maker / country: Robotera, China
- DoF: 12 ("Degrees of freedom, hands | 12"); actuated DoF: 12 ("12 active degrees of freedom, letting each finger operate independently"; "fully actuated"). bib-claim: 3 thumb, 3 index, 2 each other finger
- actuation: "Gear-driven force-controlled joint modules for each finger segment" (Motor tech row); "joints support back-drivable motion". bib-claim: direct motor drive
- fingers: 5
- thumb design: not stated
- weight: 1.1 kg ("Weight [kg] | 1.1"); size 191 x 94 x 47 mm
- fingertip force: not stated. Strength: 25 kg ("Strength [kg] | 25"; "over 25 kg when gripping palm-up"). bib-claim: 80 N grip
- tactile sensing: "Tactile/Force Sensors | Yes"; "high-resolution tactile sensors on every fingertip, the hand senses contact, force, and even temperature". Count and array size not stated. bib-claim: 5 arrays of 12x10, 3D force + temperature, 270-degree wrap
- control interface and rate: not stated on this page
- price: "14 000 USD" (tracker headline, with "Inquire about price"). bib-claim: ~$10k class, on request
- open-hardware?: no (nothing on page)
- release status and date: "In production"; no date on page. bib-claim: shipping since 2024
- used in corpus: dexmachina_2025 (one of four sim hands: "Inspire, Allegro, Xhand, Schunk"), maniptrans_2025 (XHand URDF withheld "due to licensing restrictions"), tactile_genesis_2026 (`--robot=xhand1` in-hand repose task, "screwdriver-xhand1"), dexumi_2025 ("XHand Exoskeleton" CAD for teleop), welte_iil_survey_2025 (table row "XHAND1 (ROBOTERA, 2025) | 12 | 12 | direct drive | 5 | 15 N | 16-25 kg | 1.1 kg | yes"), zhao_dexhand_survey_2026 (table row "XHAND1 | 2024 | EA | GT | 5 | 12 | 72V | 2.5A | 25kg | 1.1kg | USB | Robot Era")

## Method
- n/a (hardware). Design claim: independent force-controlled joint modules per segment, back-drivable.

## Evaluation
- specified: DoF, weight, size, strength as tracker table rows.
- demonstrated in video: none on page.
- real robot: the tracker text does not name STAR1 or any integrator (the bib "why" does).

## Limitations stated by the authors
None on the page.

## Quotable claims (verbatim, with section)
- "It moves with 12 active degrees of freedom, letting each finger operate independently." (Description)
- "Because Robotera equips it with high-resolution tactile sensors on every fingertip, the hand senses contact, force, and even temperature during interaction." (Description)
- "the hand's strength lets it lift significant loads — over 25 kg when gripping palm-up" (Description)

## Notes for the survey
- Hardware table: fully actuated 12 DoF at 1.1 kg with fingertip tactile; the survey-table rows in welte_iil_survey_2025 ("direct drive", "15 N") and zhao_dexhand_survey_2026 ("72V, 2.5A, USB") add numbers this page lacks; quote them under their own keys.
- Contradiction to watch: welte's "15 N" fingertip vs bib's "80 N grip" measure different things; the tracker gives neither.
- Sim-side: XHand is a licensed asset (maniptrans withholds the URDF), which limits reproducibility of dexmachina/tactile_genesis results on it.
