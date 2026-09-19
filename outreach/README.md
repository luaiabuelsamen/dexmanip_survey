# Outreach: the letters that were written and not sent

**Status: prepared, not sent.** These ten letters were drafted to go to the authors of the works
the survey names for a paper-against-code disagreement, and none of them was sent before the
survey was posted. They are kept here, unedited, because the paper's claim about other people's
repositories is published without a reply and a reader is owed the chance to see exactly what each
author would have been asked. Section 5.6 of the paper says the same thing beside the finding
itself, and points here.

## Why they were not sent

The decision was to publish without waiting on anyone (`PUBLISHING.md`). Waiting on ten replies
puts the posting date in someone else's hands, and a claim that needs a reply before it can be
made is a claim that should be narrowed instead. So it was narrowed. Each of the nine surviving
claims is now stated as what it is, a comparison between two public documents: a repository, the
commit `corpus/code_manifest.json` records, the file inside it, and the two values. Nothing is
attributed to intent, nothing is asserted about what any author did or trained, and any reader
with a browser can settle a line in a minute. That form of claim needs nobody's permission and
nobody's agreement, which is why it can be published without these letters.

What the letters would have added is not permission but information: which shipped config belongs
to which stage, whether the fetched commit is the one behind the reported numbers, whether a
branch nobody tagged holds the real code. The paper says plainly that it does not have that
information, and prints the correction route instead of a reply.

## What is in here, and it is not archived history

`EMAIL_TEMPLATE.md` is the cover letter. Each `outreach/<key>.md` note holds, for one work: the
paper and its authors from `corpus/bib.json`; the claim, quoting the paper's value and the shipped
value and naming the file; the evidence, as a path into `code/md/` plus the line or function and
the commit from `corpus/code_manifest.json`; the sentences the survey prints; and three questions,
which ask whether the reading is right, whether there is a reason the shipped configuration
differs, and whether the authors want the wording changed.

These letters are still the letters that would be sent. If an author writes first, or if there is
ever reason to open the correspondence, the note for that work is what goes out, after being
brought into step with whatever the paper currently prints.

## The ten notes, and the two that are no longer nine

The directory holds ten notes: `dexpbt_2023`, `dexpoint_2022`, `dextreme_2022`, `omnih2o_2024`,
`pddm_2019`, `penspin_2024`, `physhoi_2023`, `pianomime_2024`, `unidexgrasp_2023`,
`visual_dexterity_2022`. The survey names nine. The tenth, `omnih2o_2024`, is the one that
drafting the letter broke: writing it meant reading the evidence again, four of the five weight
comparisons turned out to match the paper's own table to the digit once a systematic x1.25
curriculum factor is applied, and the charge was withdrawn and the row reclassified as an internal
inconsistency before it was ever sent. Its note is kept here with its doubt notice intact, because
the withdrawal is part of the record and the note is the evidence for it.

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

There is no pre-publication exchange to record, so the post-publication one has to be real. An
author who shows that a file says something other than what the paper's Table 11 prints, or that
the fetched commit is not the one behind their numbers, changes the row: `mismatch_class` and
`mismatch_review` in `corpus/rows/<key>.json`, the counts that follow from those fields, and the
sentence in the next version, with the correction printed beside the original charge exactly as
the eight withdrawals already are. The routes are the corresponding author's address on the paper
and the issue tracker of the deposited corpus.

A correction is a commit and a replacement version, not a negotiation, and nothing about it is
private: the repository is public and its history is the record of what changed and why.

## What silence does not mean

Nobody was asked, so nobody's silence is evidence of anything, and the survey does not treat the
absence of a reply as agreement with a claim, a defence of a claim, or a reason to raise a claim's
confidence. Every one of the nine is published at exactly the confidence its own evidence
supports, with the caveats that evidence carries.
