# Outreach: the letters that were sent

**Status: nine sent on 19 September 2026, one withdrawn before it went out.** The nine letters
went to the authors of the works the survey names for a paper-against-code disagreement, before
the survey was posted, each asking whether the reading is right and whether the authors want
the wording changed. They are kept here as sent, because a reader is owed the chance to see
exactly what each author was asked. `RECIPIENTS.md` records the address each went to and where
that address came from. Section 5.6 of the paper says the same thing beside the finding itself,
and points here.

## What they ask, and what they do not assume

The letters do not ask permission. Each claim is stated as what it is, a
comparison between two public documents: a repository, the commit `corpus/code_manifest.json`
records, the file inside it, and the two values. Nothing is attributed to intent, nothing is
asserted about what any author did or trained, and any reader with a browser can settle a line
in a minute. That form of claim stands or falls on the artefacts, which is why the reply window
is two to three weeks rather than open-ended: a claim that needs a reply before it can be made
is a claim that should be narrowed instead.

What the letters add is information the artefacts cannot give: which shipped config belongs to
which stage, whether the fetched commit is the one behind the reported numbers, whether an
untagged branch holds the real code. Where a reply supplies it, the row changes and the change
is recorded in `mismatch_review`.

## What is in here, and it is not archived history

`EMAIL_TEMPLATE.md` is the cover letter. Each `outreach/<key>.md` note holds, for one work: the
paper and its authors from `corpus/bib.json`; the claim, quoting the paper's value and the shipped
value and naming the file; the evidence, as a path into `code/md/` plus the line or function and
the commit from `corpus/code_manifest.json`; the sentences the survey prints; and three questions,
which ask whether the reading is right, whether there is a reason the shipped configuration
differs, and whether the authors want the wording changed.

Each note was brought into step with what the paper prints before it went out, on 19 September
2026. If the paper's wording moves again, a note quoted in a later exchange has to be brought
into step again the same way.

## The ten notes, and why nine went out

The directory holds ten notes: `dexpbt_2023`, `dexpoint_2022`, `dextreme_2022`, `omnih2o_2024`,
`pddm_2019`, `penspin_2024`, `physhoi_2023`, `pianomime_2024`, `unidexgrasp_2023`,
`visual_dexterity_2022`. Nine of the ten went out; the survey now names eight, because one of
the nine replied. The tenth, `omnih2o_2024`, is the one that drafting the letter broke: writing
it meant reading the evidence again, four of the five weight comparisons turned out to match
the paper's own table to the digit once a systematic x1.25 curriculum factor is applied, and
the charge was withdrawn and the row reclassified as an internal inconsistency before it was
ever sent. Its note is kept here with its doubt notice intact, because the withdrawal is part
of the record and the note is the evidence for it.

`penspin_2024`'s note carries a doubt notice too, and half of that charge went the same way: the
tactile-channel half is withdrawn, since the config that was read is consistent with the paper's
proprioception-only student, which the paper never claims has tactile input. What the survey
prints is the other half, the disturbance force, and it is one line of a shipped YAML against one
line of the paper's Table 8. It is held at medium confidence in `corpus/rows/penspin_2024.json`,
and the paper says why: this survey could not establish from the parse whether a second task
config exists elsewhere in that repository.

Two notes, `dexpbt_2023` and `dextreme_2022`, also carry status notices narrowing what they ask
about. Those narrowings are in the paper too, in Section 5.6 and Appendix C.

## How a correction happens now

The pre-publication exchange is on the record above; the post-publication one has to be just as
real. An author who shows that a file says something other than what the paper's Table 11
prints, or that the fetched commit is not the one behind their numbers, changes the row:
`mismatch_class` and `mismatch_review` in `corpus/rows/<key>.json`, the counts that follow from
those fields, and the sentence in the next version, with the correction printed beside the
original comparison exactly as the seven withdrawals and two narrowings already are. The routes
are the corresponding author's address on the paper and the issue tracker of the deposited
corpus.

A correction is a commit and a replacement version, not a negotiation, and nothing about it is
private: the repository is public and its history is the record of what changed and why.

## What the replies changed

The window closed on 10 October 2026: of nine letters, one substantive reply, one acknowledgement
without an answer, seven silent.

Only the reply changed anything. Yuzhe Qin, corresponding author on DexPoint,
answered on 20 September 2026 and showed that three parts of the claim did not hold: the lift term
this survey called a departure from the paper's formula *is* the paper's formula, because
`object_lift` is already the height difference against a resting height fixed at reset; the rotation
bonus is inactive at the paper's settings, its weight defaulting to zero; and the reach-term
difference is a later, lower-variance revision rather than a disagreement about what produced the
reported numbers. The row moved from contradiction to parse-limitation, the count fell from nine to
eight, and the reason is recorded in `mismatch_review` beside the original comparison.

The lift claim is the one worth dwelling on, because this survey should have caught it. The parse
captured the reward function body but not the line defining `object_lift`, so the claim rested on
material the snapshot did not contain, and it was filed at high confidence anyway. That is the
failure mode the parse-limitation class exists for, and it took an author's reply to find it.

On UniDexGrasp a copied coauthor forwarded the letter to two further coauthors on 2 October,
asked whether they recalled the cause of the difference, and copied this survey's author on the
forward. No answer followed before the window closed, and that row is unchanged. The letter was
read and passed on rather than ignored, which is worth recording, and the question in it is open:
a forward is neither a confirmation of the claim nor a dispute of it, so the row is recorded as
unanswered rather than as agreed. Reading the question in that forward as a concession would be
exactly the kind of inference the rest of this file refuses.

Two of the seven silences come with a delivery qualification. The letters on DexPBT and DeXtreme
went to the same recipient with three coauthors in copy, and that mail server rejected two of the
three copied addresses, so two coauthors never received them. In both cases the addressed
recipient was not among the rejections, so each letter did reach a coauthor of the paper it
concerns, and the bounces are in the sent threads. On DexPBT a copied coauthor's mailer returned
an automatic out-of-office message, naming a week of travel that had already ended when the letter
was sent; it is not an answer and is not counted as one.

## What silence does not mean

Everyone was asked, and every letter said so in terms: silence is recorded as silence. The
survey does not treat the absence of a reply as agreement with a claim, as a defence of a
claim, or as a reason to raise or lower a claim's confidence. Every surviving claim is
published at exactly the confidence its own evidence supports, with the caveats that evidence
carries.