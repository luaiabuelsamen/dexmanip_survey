# STATUS — survey (dexmanip-survey)
Goal: Post the dexterous-manipulation survey to arXiv cs.RO, led by the taxonomy and findings, with every number traced to a committed results file.
Finish line: arXiv cs.RO posted by Luai. Agent work ends at a clean package plus "Blocked: needs Luai approval to post".
Deadline: 2026-10-10 (author-reply window closes; brief item 3 then applies)
Milestone: 4/5 done; item 3 waits on the date, item 5 waits on approval
Last result: arXiv package PASS, 39 pages, 209/209 bibliography, 1.5 MB (reviews/penetration_claim_dgrasp.md; CHANGELOG.md)
Blocked: needs Luai approval to push. Everything is committed and ready, 33 commits ahead of origin/main, but outreach/RECIPIENTS.md is new to the remote and tabulates 13 researchers' email addresses. Each is individually public already (the DeXtreme and Visual Dexterity PDFs print theirs, Levine's is on his CV, He Wang's and Xu's are on the UniDexGrasp project page), and none was private or guessed; the new thing is the consolidation. It sits in commits 7567c2e and c4e9e17, so it cannot be removed from the push without a force-push, which is ruled out. Two ways forward, both one line from Luai: (a) push as is, the addresses are public and the file documents letters he sent; (b) I rewrite RECIPIENTS.md to keep the provenance column and drop the literal addresses, and he accepts that the two commits above still carry them. Also still blocked: approval to post to arXiv. No paid compute requested: this session needs none, now or later — the work is text, LaTeX and a corpus of JSON rows, and it all runs on the Jetson CPU in seconds. If that ever changes it will be requested here with job, GPU type, count, hours and dollar estimate. Also needs Luai: (1) correspondence address Berkeley vs McGill — the paper and every letter sent say berkeley.edu; (2) should D-Grasp become a corpus row rather than a cited related work? It moves 46 prose sites and 32 derived facts, and adding only the counterexample a reviewer found would misrepresent a sample whose own search missed it; (3) this session pushed tex/ to Overleaf by git all week at Luai's request and the brief forbids pushing — stopped, confirm whether Overleaf sync is exempt.
Next: Nothing executable before 2026-10-10. On that date, record each of the nine letters as replied or silent in its row's mismatch_review, update CHANGELOG.md, and rebuild.
Updated: 2026-10-06 22:05

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
