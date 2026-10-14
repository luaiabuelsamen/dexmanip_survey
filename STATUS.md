# STATUS — survey (dexmanip-survey)
Goal: Post the dexterous-manipulation survey to arXiv cs.RO, led by the taxonomy and findings, with every number traced to a committed results file.
Finish line: arXiv cs.RO posted by Luai. Agent work ends at a verified package with every count recomputed from the corpus.
Deadline: 2026-10-10 for the author-reply window; posting after that and after Luai's IP check.
Milestone: all five brief items done, plus the prose pass of 2026-10-14. The survey reads as an introduction to the field: 37 pages, no bold label lead-ins outside the glossary, no paper called a row, and the per-paper counts in the tables rather than stacked in the sentences.
Last result: nine letters, one substantive reply, one acknowledgement without an answer, one redirect, six silent; no claim changed at the close (outreach/RECIPIENTS.md, CHANGELOG.md, each row's mismatch_review). check_numbers 0 problems over both editions, check_notes 220/0, make_arxiv PASS at 40 pages.
Blocked: (1) arXiv posting needs Luai's approval and his Waymo/Tesla IP check. The reply-window condition is satisfied as of 2026-10-10. Push approval is standing for incremental work on this repo with no history rewrites. Overleaf is no longer blocked: Luai approved the sync on 2026-10-13 and waived the privacy condition, and the sync is done.
Next: Nothing. The agent work is finished at a verified package. Posting is Luai's, after the IP check.
Updated: 2026-10-13 10:20

## Decisions taken 2026-10-06 (from the orchestrator)
1. **D-Grasp becomes a corpus row.** Done, under the protocol in `paper/METHOD.md`:
   PDF hashed into `corpus/manifest.json`, equations recovered by OCR, repository
   parsed at commit 8816d1ba, note in `papers/notes/dgrasp_2022.md`, row extracted
   from the note. Every affected count was recomputed and every prose site updated
   in both editions; `CHANGELOG.md` lists what moved. The penetration claim is
   restated: no row reports penetration measured in the physics its own policy ran
   in, and D-Grasp is now the corpus's own demonstration of that distinction.
   The contradiction census stays at 8, because the new row's finding is a version
   skew its authors state in their own README.
2. **Correspondence.** The paper prints `luai_abuelsamen@berkeley.edu`, the address
   the nine letters went from, under the affiliation Independent Researcher. Both
   editions and `CITATION.cff` carry it, and both say in one clause that the
   address is personal rather than institutional, because an .edu address under a
   name is otherwise read as an affiliation claim. The McGill address stays as the
   git author and appears nowhere in the paper.
3. **Overleaf** counts as a push and is allowed while the project is private. Held:
   see Blocked (2).
4. **The reply to Yuzhe Qin is Luai's to send.** No longer tracked here. The draft
   is still in Gmail drafts, untouched and unsent.

## Brief items
1. D-Grasp vs the interpenetration headline — DONE, twice. First restated with D-Grasp cited as related work; then, on the orchestrator's decision, D-Grasp was read into the corpus as a row and the claim restated against the larger corpus. The search of all 97 penetration-mentioning notes is recorded and found no other case.
2. Reconcile README / PUBLISHING.md / outreach / the paper — DONE. Nine letters sent, eight claims standing; every document now states both and why they differ. Two stale counts in section 5.6 fixed, one with its arithmetic (39 less 8 is 31).
3. After Oct 10, record replies or silence — DONE 2026-10-10, corrected 2026-10-14. One substantive reply (DexPoint, already acted on), one acknowledgement without an answer (UniDexGrasp, forwarded to two coauthors on 2 October, copying the author), one redirect (PianoMime: a coauthor replied on 22 September for the senior author and pointed the question at first author Cheng Qian, who was never written to before the window closed), six silent. Two of the seven come with a delivery qualification: the DexPBT and DeXtreme letters had two copied addresses rejected by the recipient's mail server, and DexPBT also drew an automatic out-of-office reply. Nothing in the paper changed at the close.
4. Cut length, lead with taxonomy and findings, move process narrative out — DONE. 40 pages from 42, one page back for the new row; sections 2.3 and 2.4 added for the vocabulary and the trend; retractions moved to CHANGELOG.md; no process narrative left in README.md or PUBLISHING.md.
5. Clean arXiv package — DONE and PASSing; BLOCKED for approval to post.

## What a reviewer would still push on
- Penetration still carries more of the paper than it probably deserves: 4,463 of
  the 24,637 words in `paper/sections/` sit in a paragraph that mentions it, 18
  percent, and it is the one finding with a figure and a protocol slot attached.
  That share is measured by paragraph, counting a whole paragraph if it mentions
  the word at all, so it is an upper bound; an earlier note in this file claimed 9
  percent without recording how it was measured, and that number should not be
  reused. If the restated finding is not worth 18 percent, it should shrink again.
- The corpus is a sample whose search missed D-Grasp. Appendix A now says so, in
  the Selection section: the paper entered three weeks after the cutoff, a corpus
  paper's own note cites it as that paper's baseline, and the search still did not
  surface it. A search that missed the work most relevant to one of two findings
  has probably missed others.

## Paid-compute account for 2026-10-06 (requested by the orchestrator)

Launched: nothing. No Modal app, no RunPod pod, no cloud GPU of any kind, no
detached job. Zero dollars.

Everything this session ran was local to the Jetson:
- `pdftotext`, `grep`, `python3` for the corpus checkers, the assembler and the
  figure generators (seconds each, CPU)
- `pdflatex` and `bibtex` via `tools/build_tex.sh` (about 30 s per build, CPU)
- headless Chromium once via `tools/make_pdf.py` to render the markdown edition
  (a few minutes, CPU; this is the slowest thing here)
- `git` commits, all local, no push

Network and disk, for the D-Grasp row: `arxiv.org/pdf/2112.03028` fetched once
through `tools/fetch_papers.py` (6.4 MB, now at `papers/pdf/dgrasp_2022.pdf`, which
`.gitignore` excludes), 20 pages OCR'd locally with tesseract (about 2 minutes,
CPU), and `github.com/christsa/dgrasp` shallow-cloned by `tools/fetch_code.py`
(2.8 GB, parsed to one 89 KB markdown and then deleted, so disk free is unchanged
at 59 GB). None of it is billable compute.

The stopped detached app did not come from this session. Per PLAN.md the sessions
that train are `flagship` and `libphys`, and PLAN.md directs both to Modal
("Train on Modal, not the Jetson"); `~/projects/_ops/board.sh` prints per-session
state and would identify it.

## Pushed 2026-10-06, second push

`git push origin main`, plain, no force. Range `872e206..9febfb0`, 5 commits: the
affiliation, the D-Grasp row with every count it moved, the Selection disclosure,
four derived counts with pins, and the re-rendered markdown edition.

The pre-push address check over `@{u}..HEAD` returned the author's own two
addresses, the co-author trailer, and one third-party address, in
`code/md/dgrasp_2022.md` at the line beginning "Copyright (c) 2016". It was pushed
deliberately. It is the pybind11 BSD copyright notice, reproduced verbatim where
the D-Grasp repository vendors pybind11, and that licence requires the notice be retained on redistribution. The
same line is already on `origin/main` in `code/md/raisim_2018.md`,
`code/md/artigrasp_2023.md` and `code/md/graspxl_2024.md`, so nothing new was
disclosed, and stripping one of four copies would have mangled a licence header
without improving anyone's privacy. The rule this check enforces is about not
publishing researchers' contact details gathered for outreach, which a vendored
licence notice is not.

Push approval is standing from 2026-10-06 for incremental work with no history
rewrites, with the address check run before each push.

## Pushed 2026-10-06, first push

`git push origin main`, plain, no force. Range `46a3e6f..060a0ea`, 35 commits.
Head now `060a0ea44bccbc41172bddee47375d4b7626090d`.

Before pushing, the address table was removed from `outreach/RECIPIENTS.md` in
every unpushed commit with `git filter-branch` over `origin/main..HEAD`. Neither
address-bearing commit was on any remote ref, checked with `git branch -r
--contains`, so nothing already published was rewritten and no force-push was
needed. A second pass caught `reviews/v6_reframed_read.md`, which quoted one
address in prose outside the table.

Verification after the push, over the range that is now public: the only
addresses are `luai_abuelsamen@berkeley.edu` (5, the paper's own correspondence
address), `luai.abuelsamen@mail.mcgill.ca` (35, the git author) and
`noreply@anthropic.com` (33, the co-author trailer). No third-party address. The
parsed papers under `papers/md/` and `code/md/` do carry their own authors'
addresses, as printed in those papers, but every one of those files was already
on `origin/main` before this push.

`outreach/RECIPIENTS.md` still records, per letter, who it went to, how the
address was found, and the reply state. `check_numbers.py` was changed to verify
those three rather than to assert an address is present, and it now fails if an
address appears in that file at all.

## Pushed 2026-10-10

`git push origin main`, plain, no force. Range `3572cba..71b5a91`, one commit: the closed reply
window. The pre-push address check over `@{u}..HEAD` returned only the git author and the
co-author trailer, no third-party address; nothing from the mailbox was written into the
repository, and `outreach/RECIPIENTS.md` still prints no addresses.

## The reply window, closed 2026-10-10

Nine letters went out on 19 September 2026, each giving until 10 October and each saying that
silence would be recorded as silence. At the close: **one substantive reply, one acknowledgement
without an answer, one redirect, six silent.** No claim and no count changed at the close.

- `dexpoint_2022` — replied 20 September. Three parts of the comparison did not hold; the row
  moved from contradiction to parse-limitation and the census went from nine to eight. This was
  already in the paper before today.
- `unidexgrasp_2023` — on 2 October a copied coauthor forwarded the letter to two further
  coauthors, asked whether they recalled the cause of the difference, and copied this survey's
  author on the forward. No answer followed. The row is unchanged and recorded as unanswered
  rather than as agreed: a forward is neither a confirmation nor a dispute, and reading the
  question in it as a concession is the inference the outreach policy exists to refuse.
- `dexpbt_2023`, `dextreme_2022` — silent, with a delivery qualification. Both went to one
  recipient with three coauthors in copy, and that mail server rejected two of the three copied
  addresses, so two coauthors never received them. The addressed recipient was not among the
  rejections in either case, so each letter did reach a coauthor of the paper it concerns.
  `dexpbt_2023` also drew an automatic out-of-office message from a copied coauthor, naming a
  week of travel that had ended before the letter was sent; it is not counted as an answer.
- `pianomime_2024` — a redirect, recorded as silence until 2026-10-14 and corrected. On 22
  September a coauthor replied on the senior author's behalf and pointed the question at the first
  author, Cheng Qian, who had not been written to; the window closed before anyone asked him. The
  letter reached the group and someone who could route it, not the person who could answer it in
  time. That is this survey's miss and the cost of sending four of the nine letters to a senior
  author for want of a published address for the first author. Luai is writing to him directly.
- `physhoi_2023`, `pddm_2019`, `penspin_2024`, `visual_dexterity_2022` — silent, no bounce, no
  auto-reply.

Recorded in each row's `mismatch_review`, in `outreach/RECIPIENTS.md` per letter, in
`CHANGELOG.md`, and in section 5.6 of both editions. `outreach/README.md` carries the policy and
what silence does not mean.

## Overleaf synced 2026-10-13

`tools/overleaf_sync.sh push`. Overleaf went from `664dc2d` (a sync from `a6b1022`, 2026-10-05)
to `ff3232b`, "Sync from repository (c01a997)". 19 files changed, 334 insertions, 269 deletions.

Luai asked for `71b5a91` and the commit label says `c01a997`, which is the same sources: the one
commit between them touches `STATUS.md` only, and `git diff 71b5a91 c01a997 -- tex/ sty/` is
empty. Nothing outside `tex/` is part of the package.

Nothing was overwritten. Overleaf's HEAD before the push was itself the previous sync commit, so
no edit had been made on the Overleaf side since 2026-10-05. The push path replaces tracked
content wholesale, so this was checked before running it rather than after.

**Build check.** The project was cloned back from `git.overleaf.com` and compiled from what
Overleaf now serves, with `latexmk -pdf` and no `TEXINPUTS`, which is the layout Overleaf and
arXiv both use: 40 pages, 0 LaTeX errors, 0 undefined citations, 0 undefined references, no
overfull box over 20pt, 209 `\bibitem` entries rendered, `IEEEtran.cls` read from the project
root. Every file Overleaf holds is byte-identical to its counterpart in `tex/` (53 tracked
files). What this does not do is press Recompile in Overleaf's own container: its TeX Live
release may differ from this machine's, so the check is a faithful local reproduction rather
than Overleaf's own compiler output.

Luai waived the privacy condition. Worth noting for the record that the LaTeX sources were
already public in the GitHub repository before this sync, so the sync disclosed nothing that was
not already published. arXiv remains held for the IP check; an Overleaf project is not a posting.

## The prose pass, 2026-10-14

Luai's six rules, each with what it cost and where it stands.

1. **No paper is ever called a row.** 115 replacements across both editions, then two more passes
   for the awkward ones. "Row" now means a line in a table and nothing else, and the glossary entry
   is "Method paper".
2. **At most two figures a paragraph in the body.** Paragraphs carrying more than two:
   markdown 107 of 215 before, 58 of 221 after; LaTeX 78 of 157 before, 42 of 177 after. Nothing in
   either edition now carries more than six, and most of what is left is a single comparison
   quoting two values and a unit, or the Wilson formula, whose symbols the counter reads as
   figures. The surplus went into Tables 2, 3, 4, 7, 9 and 11 and into Figures 2 and 6, which are
   generated from the corpus and so cannot drift from it.
3. **No pipeline narration in the main text.** Gone: "the extraction", "recovered", "this survey's
   own parsing", "withdrawn", the raw-versus-adjusted rate pair, and the two paragraphs of
   screening and withdrawal history. They live in Appendix A and in `CHANGELOG.md`. What stayed in
   the body is the floors-not-rates caveat in one clause with a pointer, because a reader who
   misses it misreads every coverage figure.
4. **Paper-against-code is one paragraph plus the table**, down from about 2,200 words of prose in
   the markdown edition and 1,400 in the LaTeX one. Penetration is 6.7 percent of the body by
   sentence in both editions, against a 10 percent ceiling. By paragraph it is 15 percent, because
   several paragraphs mention it once in passing; the sentence measure is the honest one for a
   share-of-the-paper claim and both are reported here.
5. **The tics are out.** 46 bold label lead-ins reduced to the six glossary definitions, where bold
   is correct typography. "Is the question this corpus cannot settle", "that is not X, since Y" and
   "which is a selection effect rather than" are gone.
6. **Section 1.1, "How to read this survey"**, is new: the shape of the paper, three reading paths
   for a newcomer, for someone already in the field and for someone who wants the data, and three
   things to carry while reading.

The checker followed the paper rather than the reverse. Three checks that required the prose to
restate a figure's or a caption's arithmetic now only forbid the prose from contradicting it, since
moving that arithmetic into the figures is what rule 2 asked for. Three phrase pins were dropped
with their sentences. 32 facts are now carried by tables and figures alone and are listed as such
in `tools/check_numbers.py`, so a number returning to the prose unpinned still fails the build.

Two things the pass found rather than made: Section 1 still said the corpus held 221 bibliography
entries and 218 records, both stale since D-Grasp entered, and the LaTeX conclusion's penetration
item had been left half-edited and ungrammatical since an earlier session.
