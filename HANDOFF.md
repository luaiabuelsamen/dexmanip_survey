# Handoff

## Goal
A survey of dexterous manipulation, single-hand and bimanual: the hands and their makers
including unreleased ones, the simulators and contact models, how policies are trained, an
evaluation frame, and the gaps. Target: an arXiv preprint, cs.RO, CC BY.

## State
Postable. `tex/main.pdf` is the submission edition, 40 pages, IEEEtran two-column. `paper/survey.pdf`
is the longer markdown edition, 119 pages, kept because its numbers were checked by eight reviewers.
Both build clean: no LaTeX errors, no undefined citations or references, no overfull boxes.
`tools/check_numbers.py` recomputes every load-bearing number from `corpus/rows/` against **both**
editions and reports zero disagreements. `tools/check_notes.py`: 220 notes, zero flagged.
`tools/make_arxiv.py` assembles and verifies the submission package by compiling it outside the
repository; it last reported PASS.

## Key results
- Corpus: 219 structured rows from parsed sources, of which 113 are method papers. 229 entries in
  `corpus/bib.json`, 222 of them corpus entries and 7 prior work from outside it. Every number in
  both editions is generated from the rows, never typed.
- 63 method rows released code readable against the paper. 39 record a disagreement. **8 are
  contradictions**, each printed as repository, fetched commit, file and two values. The other 31:
  14 limits of this survey's own parse, 8 components never released, 5 version skew, 4 a paper
  disagreeing with itself.
- Interpenetration: 12 of the 97 rows whose notes settle it handle it at all, 5 inside a closed-loop
  policy, and none reports a number measured in the physics its own policy ran in. `dgrasp_2022` is
  the near case: it reports a volume for a pose its own policy reached, measured outside the physics
  on undecimated meshes, and zero inside it. The null was audited on a seeded sample of 25 of the 85
  silent rows with zero recoveries, bounding hidden rows at 9.4%
  (`reviews/penetration_audit.md`, `tools/audit_penetration.py`).
- Hardware: 33 hands tabulated, 19 in no method row, 8 of those buyable or buildable today.

## Known problems and overclaims
- **The sent letter to PenSpin quotes a sentence that was false.** Nine letters went out 19 Sept 2026;
  `outreach/penspin_2024.md` told those authors the letter "was never sent". The paper is fixed; the
  sent record is not, deliberately, because editing it would alter what actually went out. Your call.
- Settled 2026-10-06: the paper prints `luai_abuelsamen@berkeley.edu`, the address the nine letters
  went from, under the affiliation Independent Researcher, so a reply reaches the printed route.
  `outreach/EMAIL_TEMPLATE.md` still has an unfilled contact placeholder in the stored template.
- Fixed 2026-10-06: `tools/make_tex_tables.py` ran to completion once Section VII of the LaTeX
  edition derived the trial bill the way the markdown edition does (342 matched, 600 unseen, 942 in
  all, against 1200 under an independent-arm design). The assertion that caught it is unchanged.
- Novelty is scoped deliberately. Artifact audits of a field exist (Collberg and Proebsting; a
  bioinformatics study); the closest relative is Knox et al. on autonomous-driving rewards, via author
  correspondence rather than code. `reviews/NOVELTY.md` has the wording the paper may use.
- Coverage statistics measure what the extraction captured, so each is a floor. Appendix A says so and
  discloses language-model assistance. Three fields were audited and under-counted by 20-45%; the
  code-release and failure-mode fields have not been audited.
- The LaTeX edition has had one full read as a finished document (`reviews/v6_reframed_read.md`); its
  unactioned items are listed there, including that the introduction still leads with the audit while
  the abstract leads with the survey.

## Next steps
1. Decide what to do about the PenSpin letter, and confirm the sending address matches the author block.
2. Reconcile the `table7()` assertion so tables regenerate.
3. Deposit the corpus for a DOI; the paper currently promises deposit rather than claiming it.
4. `python tools/make_arxiv.py`, work down `dist/arxiv/CHECKLIST.md`, upload `dist/arxiv/`, metadata in
   `dist/arxiv/SUBMISSION.md`. The CC BY choice is irreversible on arXiv.
5. Optional: act on the remaining `reviews/v6_reframed_read.md` items before posting, or in a v2.
