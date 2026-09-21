# v6: reading the reframed paper

Read: `tex/main.pdf`, 40 pages, rendered at 100 dpi with PyMuPDF and read as a reader sees it,
page 1 to page 40. Plus `outreach/README.md`, `outreach/RECIPIENTS.md`, `README.md`.
Commits since the last review: `7567c2e` (letters sent) through `958aef8` (appendices C, D, E in).
Nothing was changed. `tools/check_numbers.py` reports 0 problems, so nothing below is caught by it.

Severity order. Quotes are from the rendered page given.

---

## Blockers

### 1. Appendix C says the letter to PenSpin was never sent. It was sent. (p. 33)

> *Review:* Narrowed at the point of drafting the letter to its authors, **which was never sent.**

PenSpin is one of the nine. `outreach/RECIPIENTS.md` lists it — `penspin_2024` to its senior author
— and `outreach/README.md` opens "**Status: nine sent on 19 September 2026, one withdrawn before it
went out.**" So this sentence is false, and it contradicts three other places in the same PDF:
Section V-F ("The authors of the nine works were written to on 19 September 2026", p. 20),
Conclusion claim 1 ("all of their authors were written to before this was posted", p. 27), and
Appendix C's own opening two pages earlier ("All of those authors were written to before this
survey was posted", p. 31). A reader who reaches Appendix C learns that the paper's central
disclosure is wrong for at least one of the nine.

The OmniH2O entry on p. 34 carries the same clause and there it is **true** — that is the tenth
note, withdrawn before it went out. Only the PenSpin instance is false. Same text in
`tex/sections/appendix_c_rewards.tex:51` and in the Markdown edition
(`paper/APPENDIX_C.md:112`, `paper/survey.md:2703`, `paper/survey.html:7690`).

Consequence the author must decide on, not act on from here: the sent letter
`outreach/penspin_2024.md:95` reproduces this same sentence as part of "the wording that would
actually appear", so the letter that went to PenSpin's authors told them the letter was never sent.
Nothing in this review contacts anyone; recording it is all that is in scope.

### 2. The repository front page still says nobody was written to (`README.md`, lines 21–25, 53)

> **None of the nine sets of authors was written to** before the survey was posted, so each of the
> nine is stated as a comparison between two public documents … Section 5.6 says that beside the
> finding, and `outreach/` holds the **letters that were drafted and not sent.**

and the layout table:

> | `outreach/` | the letters … **drafted, not sent before posting**, kept so a reader can see what
> each would have been asked |

This is the first thing anyone opening the repository reads, and it is now the opposite of the
paper. Same paragraph also says "the **eight** accusations this survey has withdrawn after review"
where the paper says seven withdrawn and two narrowed (p. 20, p. 27).

### 3. The paper never states where contact stood on the day it was posted (p. 20)

> each was given until **10 October 2026**, and told that silence would be recorded as silence
> rather than as agreement … **replies are recorded in the row they concern.**

Letters went 19 September; the PDF is dated September 2026. The reply window closes roughly three
weeks *after* posting, so at posting no silence has been established and no reply could have been
folded in. "Replies are recorded in the row they concern" is written in a tense that lets a reader
assume replies were received and reflected. Missing, and cheap: a sentence saying no reply had been
received at the time of posting, and that the record at 10 October goes into the next version.
As it stands a reader in November cannot tell whether v1 already carries the outcome.

### 4. The paper never says what the letters were *for*, having argued they are unnecessary (p. 31, p. 20)

> so the entry **can be settled without asking anyone. All of those authors were written to** before
> this survey was posted. (Appendix C, p. 31)

This is the flipped-polarity paragraph the reframing left half-argued. The clause before the full
stop is the justification written for publishing without contact; the clause after it is the new
fact. Together they argue for something nobody disputes and leave the obvious question unanswered:
if the comparison needs no reply, why write? `outreach/README.md` answers it well — "What the
letters add is information the artefacts cannot give: which shipped config belongs to which stage,
whether the fetched commit is the one behind the reported numbers" — and none of that reasoning is
in the paper. Section V-F has the same shape: the contact paragraph is followed immediately by
"The comparison is nonetheless limited to two public artefacts", which is the old defence.

---

## High

### 5. Four of the six bars in Fig. 13 disagree with the prose on the same page (p. 23–24)

The figure prints `98 (88%)`, `89 (79%)`, `70 (62%)`, `62 (55%)`, `39 (35%)`, `11 (10%)` — every
one against 112. The prose gives per-statistic denominators:

| bar | figure | prose |
|---|---|---|
| real-robot experiment | 79% | "which is **80 percent of the 111** the note settled" (p. 23) |
| real trial count stated | 62% | "Among those 89, 70 state how many real trials … **79 percent of them**" (p. 23) |
| code released | 55% | "**57 percent of the 108** the note settled" (p. 23) |
| contact or penetration handled | 10% | "Eleven of the 96 rows … **11 percent**" (p. 24) |

And both the caption and the prose assert the arithmetic the figure does not do:

> Fig. 13: … six shares of the 112 corpus method rows, **each bar drawn against the denominator the
> text gives** … (caption, p. 23)

> **Fig. 13 draws these six shares, each against the denominator that belongs to it.** (p. 23)

Worse, the paragraph immediately before argues the 112 denominator is the wrong one — "The 89 is
the denominator that belongs to this statistic: the 22 rows with no real robot cannot state a real
trial count, and counting them as silent turns a definitional impossibility into a reporting
failure" — and then the figure counts them as silent.

### 6. Section VII-A claims all six Fig. 13 fields were audited; Appendix A says two of them were not (p. 23 vs p. 30)

> The nulls behind those **six shares** were therefore **audited by hand** against the notes they
> came from, and **every number above is post-audit.** (p. 23)

> **The code-release and failure-mode fields have still not been audited this way**, and their
> counts stay floors. (p. 30)

Code release is one of the six shares. One of the two statements has to go.

### 7. The roadmap says Appendices C and E are *not* in the paper (p. 3)

> Appendix A describes the method and the underlying corpus. Appendix B carries the three reference
> tables used in Sections III and IV. **The complete discrepancy catalogue and the statistical
> derivations behind the proposed protocol are supplied with the reproducibility materials rather
> than repeated in the article.**

Appendix C *is* the complete discrepancy catalogue (pp. 31–36) and Appendix E *is* the statistical
derivation (pp. 36–37). The roadmap sentence was true before `958aef8` and is now false, and the
roadmap still names only A and B — C, D and E are never introduced to the reader. This is the
clearest thing the reframing stranded.

### 8. The same paragraph strands Appendix D (p. 3)

> The supporting sentences **remain in the reproducibility materials**, in
> `paper/tables/table10_surveys.md`.

Appendix D (p. 36) is those supporting sentences, printed: "This appendix is the prose behind those
three levels: one glyph in that table coarsens one of the sentences below."

### 9. "Section VII is the longest" is no longer true (p. 3)

> **Section VII is the longest**, and it proposes an evaluation frame rather than a leaderboard.

Measured off the rendered headings: Section V runs p. 13 to p. 20, about 7.0 pages; Section VII
runs p. 23 to p. 27, about 3.7. Section V is the longest by a wide margin, and Section III (4.3) is
also longer than VII.

---

## Medium

### 10. The reframing reached the abstract but not the introduction's ordering (p. 1)

Abstract: "**First**, experiments concentrate on four established hands … **Second**, no closed-loop
policy … **Third**, nine of the 62 methods with inspectable code state a training objective …"

Introduction, same page: "The survey has three main findings. **The first concerns the link between
papers and their code.**" Then "The second finding concerns physical plausibility" and (p. 2) "The
third finding concerns hardware coverage."

The two orderings are exact reverses. The abstract demotes the audit to third; the introduction
still leads with it, and so does the conclusion (claim 1 of seven, p. 27). Answer to "did the
reframing land": in the title, the abstract, Fig. 1 and the section balance, yes — the audit is
Section V-F, about 1.7 of 27 body pages. In the introduction's ordering and the conclusion's lead,
no. Fixing the introduction's order is the single change that would make the emphasis consistent.

### 11. The introduction makes the accusation with no contact disclosure (p. 1)

> Thirty-eight comparisons required an explanatory note, and **nine contain a direct conflict**
> between a published value and the corresponding public implementation. PhysHOI [3], for example,
> assigns weights to object-rotation errors in its paper but sets those errors to zero …

The first place a reader meets the charge — and the only place a named work is accused on page one
— carries no mention that the authors were written to. The abstract has it, V-F has it, the
conclusion has it, Appendix C has it; the introduction does not.

### 12. The evidence of contact is in a corpus the paper says it will not link (p. 20, p. 30)

> **The letters are in `outreach/`**, with the address each went to and its provenance in
> `outreach/RECIPIENTS.md` … (p. 20)

> **The corpus is not deposited yet, and this paper prints no link to it for that reason.** It is
> available from the author at the address in the author block … (p. 30)

So the only verification of the paper's most sensitive claim is a directory path with no route to
it. Appendix C at least admits the chain ("the letters are in `outreach/` in the corpus, which is
available from the author at the address in the author block", p. 31); Section V-F and the
conclusion just cite the path. Either V-F should carry the same caveat or the letters should be
posted somewhere a reader can reach.

### 13. Appendix A says two fields were re-audited; it then reports four (p. 29–30)

> **Two fields** carrying a headline claim were re-read against the sources afterwards, **the trial
> counts and the penetration field**, and both audits are below.

Below it audits four: trial counts (55→70), success criterion (79→98), unseen-object count (32→39),
penetration (0 of 25). p. 30 then refers to "the **two earlier audits** … on the fields above",
plural fields. The count is wrong twice in the paragraph that exists to be trustworthy.

### 14. The language-model disclosure: honest on recall, silent on the failure that matters (p. 29)

> **The reading into notes was done with language-model assistance, from the parsed files only.**
> The template's conventions are the safeguard against what that can get wrong: a quotation rather
> than a paraphrase, "not stated" rather than an inference, and a named source beside every value …

What it does well, and it does use the hard evidence rather than waving: the pipeline's measured
failure is given in numbers — 55→70, 79→98, 32→39, "which is **44 percent of the audited nulls** and
moved the 'never says' figure from 34 of 89 down to 19" (p. 29) — and the fourth field's null is
given too: "**Recoveries: none of the 25**, against the 20 to 45 percent the two earlier audits
recovered on the fields above" (p. 30), with the reason the fourth behaved differently ("the
recovered trial counts and criteria were numbers present in the source and dropped by a field
shaped to hold a scalar, whereas a penetration number is absent from the source altogether").
That is better than most disclosures in this literature.

Three gaps, in order of how much they matter:

- **It never says whether the code-side reading was LM-assisted.** The sentence before the
  disclosure is "For method papers the reward or loss was quoted from the paper and, separately,
  from the released code" — so the reader infers yes, but is never told. That reading is what
  produces the nine accusations in Table III. This is the one thing a reader needs to judge the
  audit and it is left to inference.
- **Every measured failure is a recall failure, none is a fidelity failure.** The audits count
  numbers the extraction missed. They do not measure the rate at which a quoted value or file
  locator is *wrong*, which is the failure mode a language model actually introduces and the one
  that turns into a false accusation. The nine rows' locators are checked by `check_numbers.py`
  against the manifest, which catches a wrong file but not a wrong value.
- **"A human checked" is never said in Appendix A.** It says the fields "were re-read against the
  sources", agentless. p. 23 says "audited **by hand**" and p. 30 describes reading every regex hit
  "in its context", so the fact is elsewhere in the paper; the disclosure paragraph itself does not
  carry it. No model or version is named.

### 15. The OmniH2O withdrawal is told three times, and two of the tellings disagree (p. 19, 20, 34)

> … one, OmniH2O [48], **once writing to its authors** sent someone back to the evidence (p. 19)

> a seventh was reclassified when its apparent weight mismatch proved **consistent with a curriculum
> factor** (p. 20)

> *Review:* Withdrawn as a contradiction at the point of drafting the letter to its authors,
> **which was never sent.** (p. 34)

p. 19 reads as though a letter went to OmniH2O; p. 34 says it never did. Both are meant to describe
drafting. One of the two phrasings should go, and p. 20 repeats p. 19's story with a different
cause a paragraph later.

---

## Low

- **Conclusion claim 1 cites the same section twice in one sentence** (p. 27): "**Section V-F** says
  that beside the finding, with the letters in `outreach/` and the route by which a disputed case is
  corrected (**Section V-F**)."
- **`tools/check_numbers.py:633`** still documents the old world in the docstring that guards the
  nine: "The finding is published **without having written to any of the accused authors**, so what
  stands in for a reply is that a reader can check the claim". The check itself is fine.
- **Table III's caption is the one place a reader meets the nine as a table and it says nothing
  about contact** (p. 19): "The 9 rows where a paper and its released repository state different
  values, at the commit fetched, with confidence." No caption anywhere carries stale wording — this
  is an omission, not a survivor.
- **p. 23 drops a third of Appendix A's unsettled residue**: "19 trial counts and 4 criteria remain
  genuinely unsettled" against Appendix A's "19 trial counts, **8 unseen-object evaluations** … and
  4 criteria remain genuinely unsettled" (p. 29).
- **The IsaacGymEnvs 1 mm gate is stated three times** in near-identical words (p. 2, p. 11, p. 27)
  plus the README. Intro/body/conclusion, so defensible, but p. 2 and p. 27 are the same sentence.
- **Float placement**: every float is referenced and none is orphaned. Furthest from first
  reference: Table II (referenced p. 4, prints p. 6), Fig. 5 (referenced p. 9, prints p. 11),
  Table IV (discussed pp. 26–27, prints p. 28, on the page where Appendix A begins). Appendix A's
  "The proposed evaluation protocol appears in the body alongside its justification" (p. 30) is
  true only just.
- **`outreach/README.md` heading is garbled**: "## The ten notes, and the two that are no longer
  nine". It also cites "Section 5.6" and "Table 11", which are the Markdown edition's numbering —
  correct for `paper/survey.md`, confusing next to the PDF's V-F and Table III.

## Cheap checks, all clean

- No draft marker anywhere. The nine hits on "draft" are all "an earlier draft of this section",
  which is the paper's own withdrawal record, plus one quotation of another repository's TODO list.
  Running head is "PREPRINT, SEPTEMBER 2026" on every page; no self-dating, no "draft".
- LaTeX log: no undefined or multiply-defined references, one small overfull hbox, one benign
  "Text page 32 contains only floats" (Tables V and VI).
- Every table and figure is referenced in the text. Abstract claims all check against the body:
  218 records (112+33+15+15+14+14+8+7 = 218, p. 3), eight hands at zero (p. 9, p. 27), no
  closed-loop penetration (p. 25, Fig. 15), nine of 62 (Table III), 38 = 9+13+8+4+4 (Appendix C).
- Page one reads well. Title, single author, address, abstract, index terms, correspondence
  footnote. The abstract is 209 words.
- Author block prints `luai_abuelsamen@berkeley.edu` and the correspondence footnote repeats it,
  so the correction route the disclosure promises exists on the page. **One thing this review
  cannot settle from the repository**: `outreach/EMAIL_TEMPLATE.md` signs off with the unfilled
  `[NAME]` / `[AFFILIATION / CONTACT]`, and no file records which address the ten notes were sent
  from. If the letters went from an address other than the one in the author block, a recipient
  replying to the sender does not reach the address the paper names. That is for the author to
  confirm against the sent mail; it is not checkable here and nothing outside this machine was
  touched to try.
