# Handoff

## Goal
A survey of dexterous manipulation, single-hand and bimanual: the hands and their makers
including unreleased ones, the simulators and contact models, how policies are trained, an
evaluation frame, and the gaps. Target: an arXiv preprint, cs.RO, CC BY.

## State
Postable. `tex/main.pdf` is the submission edition, 39 pages, IEEEtran two-column. `paper/survey.pdf`
is the longer markdown edition, 119 pages, kept because its numbers were checked by eight reviewers.
Both build clean: no LaTeX errors, no undefined citations or references, no overfull boxes.
`tools/check_numbers.py` recomputes every load-bearing number from `corpus/rows/` against **both**
editions and reports zero disagreements. `tools/check_notes.py`: 219 notes, zero flagged.
`tools/make_arxiv.py` assembles and verifies the submission package by compiling it outside the
repository; it last reported PASS.

## Key results
- Corpus: 218 structured rows from parsed sources, of which 112 are method papers. 228 bibliography
  entries. Every number in both editions is generated from the rows, never typed.
- 62 method rows released code readable against the paper. 38 record a disagreement. **8 are
  contradictions**, each printed as repository, fetched commit, file and two values. The other 30:
  14 limits of this survey's own parse, 8 components never released, 4 version skew, 4 a paper
  disagreeing with itself.
- Interpenetration: 11 of the 96 rows whose notes settle it handle it at all, 4 inside a closed-loop
  policy, none reports a number for its own trained policy's rollouts. The null was audited on a
  seeded sample of 25 of the 85 silent rows with zero recoveries, bounding hidden rows at 9.4%
  (`reviews/penetration_audit.md`, `tools/audit_penetration.py`).
- Hardware: 33 hands tabulated, 19 in no method row, 8 of those buyable or buildable today.

## Known problems and overclaims
- **The sent letter to PenSpin quotes a sentence that was false.** Nine letters went out 19 Sept 2026;
  `outreach/penspin_2024.md` told those authors the letter "was never sent". The paper is fixed; the
  sent record is not, deliberately, because editing it would alter what actually went out. Your call.
- **No file records which address the letters were sent from**, and `outreach/EMAIL_TEMPLATE.md` has an
  unfilled contact placeholder. If that differs from the author block, replies miss the printed route.
- **`tools/make_tex_tables.py` cannot run to completion**: `table7()` asserts Section VII still states
  protocol figures 342/600/942/1200, which it no longer does. Tables are not regenerable until that
  assertion is reconciled. Pre-existing.
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
