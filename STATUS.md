# STATUS — survey (dexmanip-survey)
Goal: Post the dexterous-manipulation survey to arXiv cs.RO, led by the taxonomy and findings, with every number traced to a committed results file.
Finish line: arXiv cs.RO posted by Luai. Agent work ends at a verified package with every count recomputed from the corpus.
Deadline: 2026-10-10 for the author-reply window; posting after that and after Luai's IP check.
Milestone: 5/5 brief items done. D-Grasp is a corpus row, 113 method rows of 219, and section 7.2 is restated against the new corpus.
Last result: check_numbers 0 problems over both editions, check_notes 220/0, make_arxiv PASS at 40 pages, 113 method rows (results/trends.json, paper/APPENDIX_C.md, corpus/rows/dgrasp_2022.json)
Blocked: (1) arXiv posting needs Luai's approval and is held until after 2026-10-10 **and** Luai's Waymo/Tesla IP check. (2) Overleaf sync is allowed only while the project is private, and nothing available here reports a project's sharing state: the MCP server exposes files and sections, not visibility, and the sync path is git over git.overleaf.com. Needs one line from Luai confirming "Dexterous Manipulation Survey" (project 6aaef4d2) is private and not link-shared or published to the gallery; Overleaf is 15 commits behind, at a sync from a6b1022. (3) Pushing this round. The previous approval was scoped to the batch it named; these two commits are local and ready, plain push, no force.
Next: On 2026-10-10, record each of the nine letters as replied or silent in its row's mismatch_review, update CHANGELOG.md, rebuild, re-run check_numbers and make_arxiv.
Updated: 2026-10-06 23:30

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
3. After Oct 10, record replies or silence — BLOCKED on the date. One reply is already in (DexPoint); eight outstanding.
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

## Pushed 2026-10-06

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
