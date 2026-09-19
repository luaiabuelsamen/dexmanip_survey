# v5 — final read before posting

Read as rendered: `tex/main.pdf`, 41 pages, 100 dpi, page 1 to page 41. Not the source.
Every item below is actionable; nothing is a compliment.

Build is clean: 0 undefined references, 0 undefined citations, 0 bibtex warnings, 211
entries. All 15 figures and all 8 tables are captioned and referenced. No `??`, no TODO,
no orphaned float.

---

## 1. Does it hold together

The surgery held better than expected. Six seams, in severity order.

**1.1 A topic sentence was moved and also left behind — verbatim.** Page 1, last
paragraph of col. 2:

> "The quantity most specific to a hand is the one closed-loop policies do not record."

Page 25, §VII-B opening:

> "The quantity most specific to a hand is the one closed-loop policies do not record, and
> Fig. 15 is the funnel that narrows to zero."

Same sentence, 24 pages apart. §VII-B is where the claim belongs; page 1 should introduce
it in different words.

**1.2 The IsaacGymEnvs fact is stated six times.** Abstract, p. 2 ("The obstacle is not the
engines…"), the callout inside Fig. 5 on p. 10, p. 11 ("The tooling exists and the number
is still not recorded"), p. 28, and conclusion claim 3 on p. 29. Four would be emphasis;
six is residue from the merge of the gaps section into the conclusion. Cut the Fig. 5
callout and the p. 28 instance.

**1.3 A dangling cross-reference.** Page 10, col. 1:

> "…and the articulated Bullet mode was never run on the grasp test at all, being usable
> only in tests without contact (Appendix)."

Bare `(Appendix)` with no letter. This is a reference to another paper's appendix, but on
the page it reads as a broken `\ref` to one of this paper's five.

**1.4 A term is used in the abstract and defined on page 3.** "method row" appears in the
abstract ("most method rows whose code could be read against the paper") and eight more
times on pp. 1–2 before p. 3 says:

> "'Method row' throughout means one of the 112, and every headline count in this survey
> has one of those eight classes as its denominator."

Every headline number in the paper hangs on that denominator. It is defined too late.

**1.5 An unexplained glyph in a printed table.** Table V (p. 28) puts `*` after seven of
twelve method names — OpenAI, DAPG, Hora, Visual Dexterity, Yin et al., PDDM, HATO. There
is no legend in the caption, no table note, and no sentence naming the mark. The nearest
thing is p. 27:

> "Those have different base rates, so the table marks which kind each row was matched on
> and the two kinds are not comparable with each other."

It never says the mark is an asterisk or which kind it denotes.

**1.6 Two table-numbering conventions, and they collide.** Table III (p. 19) and Appendix C
cite other papers' tables in arabic ("Table 2", "Table 4", "Table 8") — the right
convention, since this paper's own tables are roman. But pp. 9, 10 and 12 use roman for
cited papers' tables, where they collide head-on with this paper's own:

> p. 10: "Its Table II drops an Atlas humanoid…" / "Dojo's Table V times 1000 steps…" /
> "…the SAP-style scheme [23, Table III]."

This paper's Table II is the task families, Table III is the evidence table, Table V is the
empty matrix. Convert pp. 9, 10, 12 to arabic.

**Not a seam, but the largest structural cost of the restructure:** Sections III and IV
(pp. 5–12) argue cell by cell from Tables VI, VII and VIII, which are on pp. 33–34. Eight
pages of prose reading out of tables 25 pages away. The paper discloses this twice (p. 3,
p. 31) and the disclosure is honest, but a reader cannot follow §III without two bookmarks.
Not fixable before posting; worth knowing it will be the first thing a reader complains
about after the accusation.

---

## 2. Is it honest

**The disclosure is real, and it is the best writing in the paper.** Page 20 leads a
paragraph with the bold sentence "Nobody was written to first," states the ten letters are
drafted and unsent and where they sit, gives two limits without hedging them, and names the
correction route. It repeats in the introduction (p. 1), the conclusion (claim 1, p. 29)
and Appendix C (p. 32). `outreach/` does hold exactly ten letters, one per method, matching
Table III's nine plus the withdrawn OmniH2O. The withdrawal history is printed beside the
charges rather than buried. That architecture is sound.

Five places where it does not hold.

**2.1 The correction route the disclosure promises does not exist in the document.** Page
20:

> "The routes are the corresponding author's address on this paper and the issue tracker of
> the deposited corpus, and a correction asked for either way is a commit and a replacement
> version rather than a negotiation."

There is no address on this paper. The author block is the name "Luai Abuelsamen" and
nothing else — no affiliation, no email. There is no repository URL and no DOI anywhere in
41 pages; the thanks footnote says only "the repository accompanying this survey," and p. 31
says the DOI "will carry," future tense. Grep of the rendered text finds no URL outside the
bibliography's vendor citations.

So `outreach/`, `corpus/rows/`, `corpus/code_manifest.json`, `tools/fetch_code.py` and
`tex/PERMISSIONS.md` are all unreachable, and with them the claim on the same page that "a
reader with a browser can confirm or refute any line of Table III without anyone's
agreement." Nine groups are named, and the paper offers them a remedy they cannot use. This
is the single worst thing in the document and it is one line of LaTeX.

**2.2 The abstract makes the accusation and omits the disclosure.** The abstract says "nine
are contradictions, each printed as a repository, a commit, a file and the two values." It
does not say nobody was contacted. Every other load-bearing place does. Abstracts are what
get scraped, quoted and pasted into threads without the paper. The non-contact fact belongs
in the abstract or it is, functionally, buried.

**2.3 The abstract overreaches where the body does not.** Abstract:

> "Nobody measures interpenetration on a rollout"

Body, p. 25: "we found none that reports the measurement for rollouts of its own trained
policy." Page 1: "The claim is about learned closed-loop control and not about the field."
Conclusion claim 2: "No closed-loop policy **in the corpus** reports interpenetration…"
Three careful scopings, and the abstract drops all of them for a flat universal. "Nobody"
also promotes *reports* to *measures*, which the paper's own TopoRetarget row contradicts.

**2.4 Table III prints a medium-confidence row as if it were high.** The caption says "The
9 rows where a paper and its released repository state different values." Nine rows, no
confidence column. One column later the prose says of PenSpin:

> "held at medium because this survey could not establish from the parse whether a second
> task config exists elsewhere in that repository."

Appendix C is blunter: "Held at medium confidence pending a direct code read." So the survey
has not read PenSpin's code directly, has withdrawn half its charge, and still prints it
flat among eight high-confidence rows in the table a hostile reader will screenshot. The
confidence marks exist in Appendix C already; put them in Table III as a column.

The in-figure label on Fig. 9 has the same problem and is worse: "**9 contradictions: the
shipped code states a different objective.**" For DeXtreme the finding is one penalty weight
of −0.25 versus −0.2, not a different objective. The caption below it is careful ("the 9 the
survey stands behind as contradictions"); the label inside the graphic is not, and the
graphic is what travels.

**2.5 The careful framing slips on page 1, where it matters most.** The PhysHOI passage in
the introduction ends:

> "The success criterion behind its 95.4 percent is itself position-only, and that number is
> cited as a baseline."

Page 19 makes the identical point and then closes the door: "Two documents say different
things, and that is the whole of the claim." Page 1 has no such guardrail, so the sentence
reads as *this headline result is inflated and the field has built on it* — an inference
about the work, not a comparison of two artifacts. Import the p. 19 closing sentence.

**Two smaller honesty snags.** Appendix C twice writes "before author contact" — "Narrowed
before author contact" (PenSpin), "Withdrawn as a contradiction before author contact"
(OmniH2O). There was no author contact. It is leftover phrasing from when contact was
planned, and it reads as though contact occurred. And the p. 20 arithmetic does not close:
the narrative enumerates six outright withdrawals plus DexPBT narrowed plus PenSpin
narrowed, all under adversarial review, then the bold sentence says "seven of them under
adversarial review, and the eighth at the point of writing to the authors." One of the two
narrowings is silently not counted. The paper invites exactly this audit; make the rule
explicit or say eight.

---

## 3. What a hostile reviewer opens with

**O1. "You accuse nine research groups and contacted none of them."**
*Answered, and well* — §V-F, conclusion claim 1, Appendix C, and the ten unsent letters. The
substance of the answer is strong: no claim of intent, every charge a public artifact at a
named commit, eight prior charges withdrawn in print. **But it cannot be answered as
posted**, because the remedy the answer names (2.1) is not in the document. Fix: an email
address in the author block and a repository URL/DOI in the thanks footnote. That converts
O1 from fatal to answered.

**O2. "Your headline finding is a null result over your own extraction, and your own
appendix says that field was never audited."**
Page 31: "The same mechanism reaches the penetration, code-release and failure-mode fields,
none of which has been audited that way." The mechanism in question recovered 15 of 34 null
trial counts, moved success-criterion from 79 to 98 and unseen-object from 32 to 39 — a
20–45 % under-count on every field that *was* audited. The penetration count of eleven is
the paper's central claim and sits on an unaudited field. The paper is honest about this and
buries it in Appendix A. **Answerable with a specified change**: hand-audit a random 20 of
the 85 penetration-silent rows, print the recovery rate in §VII-B, and move that admission
out of Appendix A to sit beside the claim. If the recovery rate is zero, the claim gets much
stronger; if it is not, better to find out before nine groups do.

**O3. "You propose a protocol nobody ran and a results matrix with 84 empty cells, one of
which you made up."**
*Answered.* Table V's caption says "row one fabricated," an in-table banner says "Every
number in this row is fabricated," the row is labelled *worked example*, p. 28 lists four
limits on the proposal, and p. 29 says what would close it. Handled about as well as it can
be. A reviewer will still dock the contribution; nothing more to do.

---

## 4. Verdict

**Not ready. Two blockers, both one-line fixes, then post.**

### Blocks posting

1. **Author block has no contact route.** Add an email and the repository URL (and the DOI
   if minted). Page 20 promises "the corresponding author's address on this paper" and
   Appendix B says "the repository is public"; neither is in the document. A paper that
   names nine groups must be answerable. (§2.1)

2. **The running head says the paper is a draft, on 20 of 41 pages.**
   `\markboth{Survey draft, \today}{…}` renders as `SURVEY DRAFT, SEPTEMBER 19, 2026`. It
   also re-dates itself on every rebuild, so a v2 with no content change gets a new date.
   Replace with a fixed preprint line.

3. **Abstract: add the non-contact disclosure and scope the penetration claim.** Two edits:
   append a clause stating no author was contacted before posting, and change "Nobody
   measures interpenetration on a rollout" to name the corpus and match the conclusion's
   wording. These are in the abstract, so they cannot wait for v2. (§2.2, §2.3)

4. **Table III: add the confidence column that Appendix C already carries**, and soften the
   in-figure label on Fig. 9 from "the shipped code states a different objective" to the
   caption's own wording. The nine rows are the ethical core of the paper; one of them is
   held at medium pending a code read the survey has not done. (§2.4)

### Can follow in a revision

- Rewrite the duplicated topic sentence on p. 1 (§1.1).
- Import the p. 19 guardrail sentence into the p. 1 PhysHOI passage (§2.5).
- Fix `(Appendix)` on p. 10 (§1.3).
- Legend the `*` in Table V (§1.5).
- Arabic table numbers for cited papers on pp. 9, 10, 12 (§1.6).
- Drop "before author contact" from the two Appendix C review notes.
- Reconcile the seven-versus-eight withdrawal arithmetic on p. 20.
- Define "method row" at first use rather than on p. 3 (§1.4).
- Cut two of the six IsaacGymEnvs statements (§1.2).
- Move the unaudited-fields admission from Appendix A to §VII-B (O2).
- The bibliography prints 211 entries; the paper says 221 with 218 structured rows. Ten
  corpus entries are never cited, so a reader who counts the reference list gets a different
  number than the paper's denominator. One sentence in Appendix A closes it.
- Bib entries [69] and [73] look mangled: [69] is dated 2005 with a URL ending
  `..._20241204.pdf`, [73] is dated 2014 with a 2026 fetch. Page 7 explains these are design
  dates; the reference list does not.
