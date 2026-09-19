# Getting this published

A plan, in the order the steps actually have to happen. Dates are relative because the gating
step is other people replying to email.

## Before anything is public

**1. Contact the ten authors whose code the survey says contradicts their paper.**
`outreach/` holds one file per paper with the exact claim, the evidence, and the wording that
would appear in print, plus a covering letter to adapt. Give two to three weeks. A reply that
corrects the survey changes the row and the text. A reply that disputes it without evidence is
recorded as a dispute. No reply is recorded as no reply, not as agreement.

This step is not optional politeness. Naming a research group as having shipped an objective
different from the one they published is a serious claim, and the cheapest way to find out you are
wrong is to ask before you publish rather than after.

**2. Settle the figure permissions.** `tex/PERMISSIONS.md` is the register. The routes are: a
Creative Commons licence on the source permits reuse with attribution and needs no request; a
publisher's version goes through that publisher's permissions process, which is usually automated
and usually free for academic reuse; anything else is an email to the authors. Redrawing a figure
yourself removes the question entirely and is the right answer for any figure that is a diagram
rather than a photograph.

**3. Decide the novelty claim.** `reviews/NOVELTY.md` records what prior work exists and what the
introduction can honestly say. Claim what the evidence supports and not a word more, because the
first reviewer who finds a prior artifact audit will discount everything else in the paper.

## Posting the preprint

**4. arXiv, cs.RO.** This is the right first move. It is free, it is immediate, it establishes the
date, and it costs nothing if a journal later wants changes. Choose the licence deliberately:
CC BY 4.0 lets other people reuse your figures the way you want to reuse theirs, and it is the
consistent choice given what this survey argues about openness.

Practical notes for the submission: arXiv wants the LaTeX source, not the PDF, so upload the
contents of `tex/` with `sty/IEEEtran.cls`, `sty/IEEEtran.bst`, `refs.bib`, the `sections/`,
`tables/` and `figs/` trees, and the `.bbl` file, since arXiv does not run bibtex. Check the size:
the figures put the source near 20 MB and arXiv's limit is 50 MB.

**5. Put the corpus somewhere citable.** The survey's whole argument is that claims should be
checkable against artefacts. Deposit the repository, get a DOI from Zenodo, and cite it in the
paper. A survey that audits other people's reproducibility and is not itself reproducible will be
noticed.

## Choosing a venue

There is no single obvious home, because the work is half survey and half audit.

**If the audit is the contribution**, the natural homes are venues that publish meta-science and
reproducibility work. Transactions on Machine Learning Research takes survey and analysis papers,
reviews openly, and has no page limit. A reproducibility-focused workshop at a robotics or machine
learning conference would reach exactly the people who should read it, and is fast.

**If the survey is the contribution**, the robotics homes for a long review are IEEE Transactions
on Robotics, the International Journal of Robotics Research, and the Annual Review of Control,
Robotics, and Autonomous Systems. The Annual Review is usually invited, so it is not a submission
target without a prior conversation. IEEE Robotics and Automation Magazine takes shorter, more
readable pieces and would suit a condensed version aimed at practitioners.

**Conferences** mostly do not take surveys. Do not spend a cycle finding out.

My own reading is that the audit is the contribution and the survey is its setting, so a journal
that values the method over the breadth is the better target, with the preprint doing the work of
reaching people in the meantime.

## What would make it land

The finding people will repeat is the one sentence about ten papers whose code does not implement
their published reward, and the one about nobody reporting penetration for their own rollouts.
Those need to be in the abstract, in the first figure, and in whatever you post alongside the
preprint. Everything else in the paper is the evidence that earns them.

Do not oversell. The survey's own coverage statistics measure what its extraction captured, it
withdrew seven accusations under review, and it re-ran no method. Saying all three plainly is what
makes the rest credible.

## A note on what belongs in the paper and what belongs in the repository

The survey's evidence is a corpus of 218 structured rows, 222 notes and 126 parsed repositories.
Printing that evidence as tables put nearly a third of the paper into tabulation that a reader
consults rather than reads. It has been cut back: the body keeps the figures and the two or three
tables a reader actually reads, and the full tabulation lives in the repository, which gets a DOI
and is cited.

This is the consistent position for a paper that argues researchers should publish checkable
artefacts. The artefact is the corpus. The paper is the argument about it.
