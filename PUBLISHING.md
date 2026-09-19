# Getting this published

A plan, in the order the steps actually have to happen. Dates are relative because the gating
step is other people replying to email.

## The decision this plan is written against

No permission will be requested and no author will be written to before posting. That is a
deliberate choice and it changes what the paper has to do for itself. Three consequences, each of
which has been handled rather than waived.

**Nothing in the paper depends on a reply.** Every reproduced figure whose reuse needed an email
has been redrawn or dropped. What remains is the survey's own artwork plus figures under a licence
that permits reuse with attribution. The permissions register records the final position.

**The claim about other people's code is framed as a claim about public artifacts.** The paper says
what a named repository contains at a named commit, which anyone can check in a minute, rather
than what its authors did or intended. Beside that finding the paper states plainly that the
authors were not contacted first, that a commit may not be the code behind a paper's reported
numbers, and how a disputed case will be corrected. The letters that would have been sent are kept
in `outreach/` and the paper points at them, so a reader can see exactly what each author would
have been asked.

**Correction is a published route, not a private one.** Because there is no pre-publication
exchange, the post-publication one has to be real. The route is stated in the paper and the
repository is public, so a correction is a commit and a replacement version, not a negotiation.

## Posting


**4. arXiv, cs.RO.** This is the right first move. It is free, it is immediate, it establishes the
date, and it costs nothing if a journal later wants changes. Choose the licence deliberately:
CC BY 4.0 lets other people reuse your figures the way you want to reuse theirs, and it is the
consistent choice given what this survey argues about openness.

The package is built and tested by `python tools/make_arxiv.py`, which assembles `dist/arxiv/`
from the documents `main.tex` actually reads, then proves it by compiling a copy outside the
repository with two `pdflatex` passes and no bibtex, which is close to what arXiv does. It writes
`dist/arxiv/SUBMISSION.md` with every field the form asks for and `dist/arxiv/CHECKLIST.md` with
what to verify in the five minutes before clicking submit. Rebuild it immediately before
uploading; the numbers in both files are recomputed from the sources each time.

Do not hand-assemble the upload. Two things about it are not obvious. arXiv does not run bibtex,
so `main.bbl` has to be in the package: without it the bibliography does not error, it silently
disappears and every citation prints as a question mark. Measured, by deleting the file from the
assembled package and compiling it: no reference list at all, four pages shorter, and 666
undefined citations, with a clean exit status. And arXiv sets no `TEXINPUTS`, while TeX's default
search path does not descend into subdirectories, so a vendored `sty/IEEEtran.cls` is never found
and the build dies at `\documentclass` with no PDF at all; the class has to sit at the top level
of the upload. `make_arxiv.py` puts it in both places and checks both failures.

`figs/extracted/` is never uploaded. It is 367 MB, the whole rendered figure catalogue, and the
paper reproduces only what `figs/selected/` holds. The assembled package is about 1.4 MB.

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

The finding people will repeat is the one sentence about nine papers whose code does not implement
their published reward, and the one about nobody reporting penetration for their own rollouts.
Those need to be in the abstract, in the first figure, and in whatever you post alongside the
preprint. Everything else in the paper is the evidence that earns them.

Do not oversell. The survey's own coverage statistics measure what its extraction captured, it
has withdrawn eight accusations under review, and it re-ran no method. Saying all three plainly is what
makes the rest credible.

## A note on what belongs in the paper and what belongs in the repository

The survey's evidence is a corpus of 218 structured rows, 222 notes and 126 parsed repositories.
Printing that evidence as tables put nearly a third of the paper into tabulation that a reader
consults rather than reads. It has been cut back: the body keeps the figures and the two or three
tables a reader actually reads, and the full tabulation lives in the repository, which gets a DOI
and is cited.

This is the consistent position for a paper that argues researchers should publish checkable
artefacts. The artefact is the corpus. The paper is the argument about it.
