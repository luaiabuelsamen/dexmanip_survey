# Changelog

Corrections to claims this survey has made, newest first. Public-facing documents
state what the survey finds; this file states what it has changed its mind about.
Every entry names the evidence and the commit.

## 2026-10-06 — the interpenetration headline, restated

**Was:** no closed-loop policy in the corpus reports interpenetration for the
rollouts of its own trained policy.

**Now:** where interpenetration is reported at all, it is not measured in the
physics that produced the motion.

**Why:** D-Grasp (Christen et al., CVPR 2022, arXiv 2112.03028) trains a
reinforcement-learning grasping policy and reports a penetration volume in its
Table 1, 1.74 cm³ against 4.41 and 9.08 for its baselines. The old claim was
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
