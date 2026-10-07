# STATUS — survey (dexmanip-survey)
Goal: Post the dexterous-manipulation survey to arXiv cs.RO, led by the taxonomy and findings, with every number traced to a committed results file.
Finish line: arXiv cs.RO posted by Luai. Agent work ends at a clean package plus "Blocked: needs Luai approval to post to arXiv, and that stays blocked until after 2026-10-10 by the plan. Two decisions still open: the correspondence address, where the paper and all nine sent letters say berkeley.edu while every commit is authored from luai.abuelsamen@mail.mcgill.ca; and whether D-Grasp should become a corpus row rather than a cited related work, which would move 46 prose sites and 32 derived facts.
Next: Nothing executable before 2026-10-10. On that date, record each of the nine letters as replied or silent in its row's mismatch_review, update CHANGELOG.md, and rebuild.
Updated: 2026-10-06 22:40

## Brief items
1. D-Grasp vs the interpenetration headline — DONE. Claim restated in the abstract, section 7 and the conclusion; D-Grasp cited as related work; the search of all 96 penetration-mentioning notes is recorded and found no other counterexample.
2. Reconcile README / PUBLISHING.md / outreach / the paper — DONE. Nine letters sent, eight claims standing; every document now states both and why they differ. Two stale counts in section 5.6 fixed, one with its arithmetic (38 less 8 is 30, not 29).
3. After Oct 10, record replies or silence — BLOCKED on the date. One reply is already in (DexPoint); eight outstanding.
4. Cut length, lead with taxonomy and findings, move process narrative out — DONE. 39 pages from 42; sections 2.3 and 2.4 added for the vocabulary and the trend; retractions moved to CHANGELOG.md; no process narrative left in README.md or PUBLISHING.md.
5. Clean arXiv package — DONE and PASSing; BLOCKED for approval to post.

## What a reviewer would still push on
- Penetration is 9 percent of the paper, down from 25, but it is still the one
  finding with a figure and a protocol slot attached. If the restated version is
  not worth that much space, it should shrink again.
- The corpus is a sample whose search missed D-Grasp. Appendix A does not yet say
  so. That is a limitation worth one sentence, and it is a better disclosure than
  silently adding the one paper a reviewer found.

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

One external network call: `WebFetch` of `arxiv.org/pdf/2112.03028` to read
D-Grasp, which is a 6.2 MB download and not billable compute. The PDF was left in
the tool-results cache rather than added to the repo, so it is not on the repo's
disk budget.

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
