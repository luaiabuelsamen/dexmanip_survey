# Changelog

Corrections to claims this survey has made, newest first. Public-facing documents
state what the survey finds; this file states what it has changed its mind about.
Every entry names the evidence and the commit.

## 2026-10-06 — D-Grasp is a corpus row, and the counts it moves

**Was:** D-Grasp was cited as prior work from outside the corpus, carried no
structured row, and entered no count.

**Now:** it is `corpus/rows/dgrasp_2022.json`, read under the same protocol as the
other 112: PDF fetched and hashed into `corpus/manifest.json`
(sha256 4f0b919b…, 20 pages, pymupdf4llm), equations recovered by OCR into
`papers/md/dgrasp_2022.ocr.md`, repository shallow-cloned and parsed at commit
8816d1ba into `code/md/dgrasp_2022.md`, note in `papers/notes/dgrasp_2022.md`.

**What moved.** 112 method rows become 113 and 218 structured rows 219; 221 corpus
bibliography entries become 222 and the prior-work entries outside the corpus drop
from 8 to 7. Papers whose notes settle the penetration question: 96 to 97, of which
11 to 12 handle it, and the closed-loop policies among them 4 to 5. Code released
and readable: 62 to 63; disagreements recorded: 38 to 39, the new one a version
skew, so the contradiction census stays at 8. Reward-learning rows 59 to 60, PPO 48
to 49, hand-naming rows 103 to 104, criteria stated 98 to 99, unseen-object counts
40, environment counts 32, and the grasp task family 57 to 58. The 85 rows recorded
as not addressing penetration are unchanged, so the seeded audit behind that null
and its 8-of-85 bound stand as they were, and the floor it supports moves from
eleven to twelve.

**What did not move.** The restated headline above. D-Grasp is now the corpus's own
example of it rather than a counterexample from outside: it reports zero inside the
physics and a non-zero volume from re-measuring one frame outside it.

**Also corrected here.** The entry below, and the bibliography note it was written
from, attributed 1.74, 4.41 and 9.08 cm³ to the paper's Table 1. They are Table 2,
the generalisation experiment on unseen objects. Table 1 reports 1.75 to 3.40 cm³
for the method across its four label sources. Both tables are quoted in the note.

**Also recorded.** The paper's own appendix argues that a success rate needs a
penetration number beside it, because a deeply penetrating reference can raise the
rate: "the objects can become entangled within the hand mesh and will therefore not
be able to fall down", so "the success rate metric should always be interpreted in
combination with the other metrics" (its Sec. C). Section 7.2 now cites that rather
than arguing it.

## 2026-10-06 — the interpenetration headline, restated

**Was:** no closed-loop policy in the corpus reports interpenetration for the
rollouts of its own trained policy.

**Now:** where interpenetration is reported at all, it is not measured in the
physics that produced the motion.

**Why:** D-Grasp (Christen et al., CVPR 2022, arXiv 2112.03028) trains a
reinforcement-learning grasping policy and reports a penetration volume in its
Table 2, 1.74 cm³ against 4.41 and 9.08 for its baselines on unseen objects. The old claim was
literally true only because it was scoped to the corpus and D-Grasp has no corpus
row, while the corpus's own ArtiGrasp note cites D-Grasp as a baseline. What
D-Grasp shows is sharper than the null it refutes: it reports zero inside the
physics simulation, because the simulated meshes are simplified for speed, and
1.74 cm³ when the policy's output pose is re-measured on the original meshes with
"no physical simulation involved". Evidence and quotes in
`reviews/penetration_claim_dgrasp.md`. A search of all 96 penetration-mentioning
notes found no other counterexample; every corpus paper reporting the quantity
measures a reference.

## 2026-09-20 — the paper-against-code census, nine to eight

**Was:** nine of the 62 papers with inspectable code state a training objective
in the paper that differs from the repository.

**Now:** eight.

**Why:** the corresponding author of `dexpoint_2022` replied to the letter of 19
September and showed three parts of the comparison did not hold. The lift term
the survey called a departure from Eq. 5 *is* Eq. 5, because `object_lift` is
already the height difference against a resting height fixed at reset, and the
line defining it was never in this survey's parse. The rotation bonus is inactive
at the paper's settings. The reach-term difference is version skew, since the
paper's reported variance is the plain-distance formula's. The row moved to
`parse-limitation`. Recorded in that row's `mismatch_review`.

## Before posting — sixteen comparisons to eight

Sixteen rows were first drawn as contradictions. Eight have left the class: six
under adversarial re-reading (`maniptrans_2025`, `eureka_2023`,
`open_television_2024`, `dexmachina_2025`, `artigrasp_2023`, `graspxl_2024`), one
when the letter to its authors was being drafted (`omnih2o_2024`), and one
because a reply arrived (`dexpoint_2022`). Two more were narrowed and remain in
the count (`dexpbt_2023`, `penspin_2024`). Each revision is recorded in the row
it concerns, beside the comparison it revises.
