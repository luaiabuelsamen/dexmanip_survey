# Outreach: correcting the paper/code mismatch claims before publication

This directory holds the correspondence prepared for the ten methods the survey names as having
released code that contradicts the reward or objective their paper describes:

`dexpbt_2023`, `dexpoint_2022`, `dextreme_2022`, `omnih2o_2024`, `pddm_2019`, `penspin_2024`,
`physhoi_2023`, `pianomime_2024`, `unidexgrasp_2023`, `visual_dexterity_2022`.

Before any of these ten claims is published, we write to the paper's authors, show them the exact
claim and its evidence, and give them the chance to correct it or object — before the survey goes
out, not after.

## Who to contact

The corresponding author listed on the paper (check the paper's own title page or the venue's
listing; `corpus/bib.json` records the author list we have, but not which of them is
corresponding). If the paper lists no corresponding author explicitly, write to the first author,
copying the senior/last author. Use `outreach/EMAIL_TEMPLATE.md` as the cover letter and attach or
paste the matching `outreach/<key>.md` note, which contains the exact claim, the file and line of
evidence, the commit, and the sentences the survey currently plans to print.

## What each per-paper note contains

Each `outreach/<key>.md` file has:
- the paper's title and authors (from `corpus/bib.json`);
- the exact claim, quoting the paper's stated value and the shipped value, and naming the file;
- the evidence, as a path into `code/md/` plus the line or function, and the commit recorded in
  `corpus/code_manifest.json`;
- the sentences that will actually appear in `tex/sections/05_training.tex`,
  `tex/sections/08_gaps.tex`, and `tex/sections/appendix_c_rewards.tex` if the authors do not
  reply;
- three questions: whether our reading is correct, whether there is a reason the shipped
  configuration differs from the paper, and whether they would like the wording changed.

Two files, `omnih2o_2024.md` and `penspin_2024.md`, carry a prominent doubt notice at the top.
Both are already held at medium confidence in the survey's own data (`mismatch_confidence:
"medium"` in the corresponding `corpus/rows/*.json`), and in both cases a closer read of the
underlying note and the survey's own adversarial review (`reviews/r3_methods.md`, items 11 and 13)
raised specific reasons to think part of the claim may not hold up — a likely typo signature in
one case, a config that may belong to a different stage of the pipeline in the other. We are still
sending these two, because a direct answer from the authors is the fastest way to resolve exactly
that uncertainty, but the letters are written to ask rather than assert, and we would not be
surprised, or unhappy, to drop either claim after a reply.

## What a reply changes

A reply from the authors is not just filed — it changes two things:

1. **The row's `mismatch_review` field** (`corpus/rows/<key>.json`). Whatever the authors say gets
   recorded there in the same way the seven adversarial-review withdrawals already are: what was
   said, and what changed as a result. If they confirm the reading, the field records that. If they
   point out an error, or explain a difference we misread as a contradiction, the field records
   that instead, and the `mismatch_class`/`mismatch_confidence` are revised accordingly — including
   downgrading a claim to a different class (e.g., version skew, or no longer a mismatch at all) or
   removing it from the ten entirely, if that is what the evidence now shows.
2. **The text.** Any sentence in `tex/sections/05_training.tex`, `08_gaps.tex`, or
   `appendix_c_rewards.tex` that states the claim is updated to match what the row now says.
   Nothing about a paper's code is asserted in the final document that its authors have
   contradicted with a reply we have no reason to doubt.

## What a non-reply does not change

If an author does not reply within the letter's stated window (two to three weeks from when it was
sent), the survey does not treat that silence as agreement, and it does not upgrade the claim's
confidence or drop the caveats already attached to it. Instead, the row records that outreach was
attempted and not answered — a plain statement of fact, not an inference about the claim's truth in
either direction. The claim is published exactly as it would have been published anyway, at
whatever confidence and with whatever hedges the evidence already supported, with an added note
that the authors were given the chance to respond.

## Sending and tracking

Keep a plain log (date sent, address used, any reply, and what changed in the row/text as a result)
somewhere outside this directory — `NOTES.md`-style, dated, append-only — so that "we wrote to them
and they didn't answer" versus "we wrote to them and they confirmed it" is itself an auditable
claim, not a memory.
