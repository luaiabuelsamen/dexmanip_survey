# R5, the sceptical generalist

Reviewing `paper/survey.md` at the state of 2026-09-18. I read it end to end once without
checking anything, then checked positioning, taxonomy, gaps, scope and length. I did not read the
other reviews.

## First impression, recorded before any checking

What I learned and did not know before: that MuJoCo's soft contact is a deliberate purchase of a
16 ms timestep at the price of tens of millimetres of overlap, and that the two engines carrying
41 of the 110 method papers do not hand penetration depth to the user at all (Sec. 4.2). That the
reward function in `physhoi_2023`'s released code hard-sets the object-rotation error to zero
while its Table 4 weights it at 0.1, and that its own success criterion could not have caught it
(Sec. 5.8). That the dominant bimanual architecture has been ablated once, by `asymdex_2024`, and
lost (Sec. 6.2). That the corpus median real-trial count is 20 and has not moved since 2022
(Sec. 7.1). Those four are worth the price of the paper.

Where I skimmed: Sec. 3.4, which is eight paragraphs of dead vendor URLs; Table 6, whose cells are
truncated mid-word and which I could not read; the second half of Sec. 5.5, which is eight
consecutive quotations before the point arrives; and all of Sec. 8, which I recognised as Sections
3 to 7 again in a template.

Where I stopped believing it: Sec. 3. The section argues from Table 2 and Table 3 nine and ten
times respectively, and neither table is in the document. I read 2,900 words about the contents of
evidence I cannot see. I had the same experience in Sec. 4 with Table 4 and in Sec. 5 and 6 with
Table 7. After that I read the rest as assertions rather than as a case.

The short version: there is a real paper here, and it is about contact measurement and about
paper-versus-code disagreement. It is currently wrapped in a hardware inventory, a gaps section
and a set of absent tables that make it look like a conventional survey and read worse than one.

---

## Findings

### 1. blocking — Four of the survey's nine tables, and two of its three appendices, do not exist

**Location.** Sec. 3.1, "Table 2 therefore prints actuated DoF beside DoF, and the gap is the
informative number." Sec. 4.2, "Table 4 is the engine-by-engine comparison, one row per
simulator, built only from what a note confirmed." Sec. 6.4, "Table 7 carries the bimanual papers
on the same columns as every other method here."

**The problem.** Table 2 is referenced 9 times, Table 3 10 times, Table 4 8 times and Table 7 3
times. None of them appears in `paper/survey.md`. The entire evidence base of Sec. 3 and the
central "which engines expose penetration" claim of Sec. 4.2 live in tables the reader never sees.

**The evidence.** `grep -n "^### Table\|^## Table" paper/survey.md` returns Tables 1, 5, 6, 8 and
9 only. `paper/TABLES.md` specifies Tables 2, 3, 4, 7 and also a Table 10, "Existing surveys and
what each covers", which is neither present nor referenced anywhere. `paper/OUTLINE.md` lines
108-109 promise Appendix B, "The full hand table with sources", and Appendix C, "Per-paper reward
term extraction"; `paper/survey.md` ends after Appendix A. The two occurrences of "Appendix B" in
the draft both refer to `dextrack_2025`'s appendix, not to this survey's.

**The fix.** Generate and insert Tables 2, 3, 4 and 7 before any further review. If Table 7 is too
long for the body, put it in Appendix B and say so in the text. Either build Table 10 or delete
the plan for it and accept that Sec. 1 carries the positioning alone, which is finding 3 below.

### 2. major — Four of six figures are referenced, load-bearing, and not embedded

**Location.** Sec. 3.2, "Figure 2 counts, per hand, the method papers whose own experiments use
it." Sec. 3.6, "The bottom rows of Figure 2 carry the finding." Sec. 6.2, "Figure 5 sets the four
architectures side by side with the counts on the panel borders."

**The problem.** Only `fig4_taxonomy.svg` and `fig6_reporting.svg` are embedded. Figures 1, 2, 3
and 5 are referenced in the text and never rendered, and Sec. 3.6 explicitly locates a finding in
Figure 2's bottom rows. Meanwhile 1,017 words of drafting scaffolding for Figures 1 and 4 are left
in the file as HTML comments, and Figure 4 has both a comment spec and an embed.

**The evidence.** `paper/figures/` contains all six SVGs. `grep -n "^!\[fig" paper/survey.md`
returns two hits, at lines 766 and 1465. The comment blocks run lines 81-126 and 1205-1267.

**The fix.** Embed all six. Delete both comment blocks; the drawing instructions belong in
`paper/FIGURES.md`, where they already are.

### 3. major — The survey claims engine comparison as a contribution while a review of nine engines sits uncited in its own corpus

**Location.** Sec. 1, "What none of them provides is a comparison of the physics engines these
policies are trained in, a treatment of two hands on one object as its own problem, and an
evaluation frame that asks whether the contact a policy produces is physically plausible. Those
three are what this survey adds."

**The problem.** The first of the three claimed contributions is stated against six named
overviews. The corpus contains a seventh that is squarely on that topic and is never mentioned in
the draft at all.

**The evidence.** `corpus/bib.json` carries `nine_physics_engines_review_2024`, "A Review of Nine
Physics Engines for Reinforcement Learning Research". It has a full structured note at
`papers/notes/nine_physics_engines_review_2024.md` including a reproduced feature table for Brax,
Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity and Webots, and a per-engine conclusion. It has
a row at `corpus/rows/nine_physics_engines_review_2024.json`. `grep -c
"nine_physics_engines_review_2024" paper/survey.md` returns 0.

The distinction the survey needs is available and is in the note: that review runs no benchmark of
its own (Sec. V, "This goes beyond the scope of this paper"), derives no LCP/CCP/NCP-level solver
characterisation, uses ant and humanoid bodies rather than hands, and never discusses timestep,
friction model or penetration exposure. Every one of those is a real difference. But the survey
must state them rather than omit the paper.

**The fix.** Add a sentence to Sec. 1: name `nine_physics_engines_review_2024`, say it scores nine
engines on documentation, URDF support and MARL readiness rather than on contact formulation,
quote its own limitation that it ran no quantitative comparison, and say that this survey's Table 4
adds contact model, solver, timestep and penetration exposure conditioned on hands. Cite it again
in Sec. 4.2 where the taxonomy is introduced.

### 4. major — `bai_unified_manip_survey_2025` is strawmanned by a parse-artefact measurement

**Location.** Sec. 1, "`bai_unified_manip_survey_2025` spans all of manipulation across 212 pages
and gives dexterous manipulation about thirty lines in Sec. 4.3, deferring the subject to other
surveys in its Sec. 1.2."

**The problem.** "About thirty lines" is a count of wrapped markdown lines in this survey's own
converted copy, presented beside "212 pages" so that it reads as a page-proportion claim. Sec. 4.3
is 723 words and is the second-longest of that paper's ten task subsections. A reader who opens
the PDF will find roughly two printed pages, not thirty lines, and will conclude the survey
misrepresented a predecessor to make room for itself.

**The evidence.** `papers/md/bai_unified_manip_survey_2025.md`, Sec. 4.3 at line 646, measured
against its siblings: 4.1 grasping 1,158 words, 4.3 dexterous 723, 4.6 mobile 667, 4.5 deformable
514, 4.4 soft 454, 4.8 humanoid 168, 4.2 basic 87. The note at
`papers/notes/bai_unified_manip_survey_2025.md` records the same fact honestly as "about 30 lines
of 5919", which is a statement about the parse, not about the paper.

**The fix.** Write "about 700 words, the second-longest of its ten task subsections, in a paper
whose Sec. 1.2 defers dexterous manipulation to other surveys". That is still a strong
differentiation and it is one its authors cannot dispute. The `deferring` half of the sentence is
correct and load-bearing; keep it.

### 5. major — `zhao_dexhand_survey_2026` already draws the survey's central distinction, and the draft's characterisation hides it

**Location.** Sec. 1, "`zhao_dexhand_survey_2026` ... has no simulator section, names Isaac Gym and
MuJoCo once each, and uses the word penetration exactly once." And Sec. 1, the third claimed
contribution, "an evaluation frame that asks whether the contact a policy produces is physically
plausible."

**The problem.** Every clause of the characterisation is true, and the word-count framing is
chosen to make the one occurrence sound incidental. It is not incidental. That occurrence is in
Zhao's Sec. IV-C, "Evaluation Metric", where it names physical plausibility including penetration
as one of the two layers on which the field assesses work. The other layer is downstream execution
success. That two-layer split — plausibility checked on poses before execution, success measured
during execution — is precisely the distinction this survey builds Sec. 7.3 and Sec. 8.2 on.

**The evidence.** `papers/notes/zhao_dexhand_survey_2026.md`, Evaluation section, quoting Sec. IV-C
verbatim: "existing works usually assess at least two layers of performance: the quality of grasps
or poses prior to execution, and the performance of policies or generators during downstream
execution. For grasp- and pose-centric datasets, the most common criteria concern physical
plausibility, including penetration, analytic or quasi-static stability, and diversity". The note
then confirms what Zhao does not do: "no penetration threshold or measurement method is given",
"Interpenetration is never treated as a measured quantity".

**The fix.** Say what is actually new. Zhao names physical plausibility as an evaluation layer and
gives no threshold, no measurement method and no count. This survey measures how many papers do it
(11 of 110), shows that seven of the 11 do it offline, and argues that a measure a policy
optimises cannot judge it. The contribution is the measurement and the trap argument, not the idea
that contact quality is an evaluation axis. Rewrite the third claimed contribution in those terms
and drop the "exactly once" word-count.

The other three characterisations check out against their notes and are fair. `an_dexil_survey_2025`
giving RL no taxonomy, treating bimanual as one "multi-agent" subsection, comparing no simulator and
defining no metric is supported line by line by `papers/notes/an_dexil_survey_2025.md`, including
its own "What it does NOT cover" block. `welte_iil_survey_2025` at seven dexterous IIL works, a
fifteen-hand commercial table, no bimanual section, no benchmark table and no contact modelling is
supported by `papers/notes/welte_iil_survey_2025.md`. The bimanual contribution claim survives:
none of the four gives two hands on one object more than a subsection.

### 6. major — The Sec. 2 taxonomy does not cover the corpus, and the draft does not say so

**Location.** Sec. 2.1, which names six task families and gives a count for each: grasping 55,
functional and tool use 43, in-hand reorientation 31, tracking a human reference 12, bimanual
coordination 42, handover 9.

**The problem.** The taxonomy is observed from the rows, which is to its credit. But it is
presented as exhaustive and it is not. The schema carries three further values, and the draft
mentions none of them.

**The evidence.** Over `corpus/rows/*.json` restricted to `class: method`, the `task_family` counts
are grasp 55, functional/tool 43, bimanual-coord 42, reorient 31, **other 20**, track-human-ref 12,
handover 9, **locomanipulation 2**, **music 1**. Seven method rows carry no label from the six
families at all: `cross_embodiment_world_models_2025`, `gemini_robotics_15_2025`, `openvla_2024`,
`pi0_2024`, `pi05_2025`, `pistar06_2025`, `pianomime_2024`. Twenty-three rows carry at least one
out-of-taxonomy label.

Three of those are not rounding error. `dexdeform_2023` is deformable-object manipulation, a task
family with its own physics that Sec. 2.2's four difficulties do not describe.
`robopianist_2023`, `rp1m_2024` and `pianomime_2024` are discussed at length in Sec. 6 and have no
home in Sec. 2.1; the schema invented a `music` family for them and the prose never admits it.
`humanplus_2024` and `omnih2o_2024` are locomanipulation, where the gravity argument of Sec. 2.2
changes character because the base is not fixed.

**The fix.** Add a sentence after the handover paragraph: "Twenty of the 110 rows carry no family
from this list, and seven carry none at all. Most are generalist policies evaluated on task suites
rather than on a dexterous task family, and three are piano playing, two locomanipulation and one
deformable-object manipulation. The taxonomy describes what the dexterous literature studies, not
everything in the corpus." That single sentence converts a tidy-looking taxonomy into an observed
one, which is what it is.

### 7. major — "Bimanual" carries two different denominators in two adjacent subsections

**Location.** Sec. 2.1, "Bimanual coordination has 42 rows and handover has 9." Sec. 2.3, "Fifty-one
of the 110 method rows run two hands." Sec. 6, "Of the 51 corpus method papers whose row records
`bimanual: true`". Sec. 6.2, "The denominator is the 25 corpus papers whose notes place a learned
controller on two dexterous hands."

**The problem.** Three denominators for one word, in the same document, none of them reconciled to
the others in the text. A reader tracking the bimanual claim sees 42, then 51, then 25, and cannot
tell whether these are nested, overlapping or inconsistent.

**The evidence.** Both the 42 and the 51 are correct against `corpus/rows/*.json`: 42 rows carry
`task_family` containing `bimanual-coord`, and 51 carry `bimanual: true`, with 56 false and 3 null.
They measure different things. Sec. 6 then narrows to 25 and, separately, to 12 "that describe a
learned controller" in Sec. 8.8. Only the 51-to-25 step is explained.

**The fix.** State the relationship once, in Sec. 2.3: 51 rows put two hands on the robot, 42 of
those study coordination as the task, and Sec. 6.2 narrows to the 25 that put a learned controller
on two dexterous hands. Then use one number per claim and name which.

### 8. major — Two corpus entries with parsed text on disk are silently absent, and one of them contradicts a headline finding

**Location.** Sec. 3.6, "None of the nine company-announced hands in Table 3 appears in a single
method row. Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi, Clone, Daxo and PaXini together
account for zero of the 110 method papers' experiments." And Sec. 8.5, "Generalist policies are
largely not evaluated on hands."

**The problem.** `helix_2025` is in the bibliography, marked `verified: true`, and its page is
parsed and stored. It is Figure AI's own vision-language-action model, and its first stated claim
is control of "the entire humanoid upper body, including wrists, torso, head, and individual
fingers" on the Figure robot. It has no note, no row, and no mention anywhere in the draft.
`groot_n16_2025` is in the same position, and Sec. 5.5 complains that `groot_n1_2025`'s repository
is a later generation while the survey holds the later generation's page unread.

Neither appears in `paper/METHOD.md`'s list of sources that could not be obtained. The draft's
Sec. 1 says the corpus holds "221 bibliography entries, of which 216 carry a structured row read
from a note", which is arithmetically true and gives the reader no way to discover that two of the
five missing rows are obtained industrial evidence dropped without comment.

**The evidence.** `corpus/bib.json` entries `helix_2025` (Figure AI blog, Feb 2025, why-field:
"Dual-system VLA controlling a 35-DoF humanoid upper body including individual fingers at 200 Hz on
onboard GPUs") and `groot_n16_2025` (NVIDIA GEAR release, Dec 2025). `papers/md/helix_2025.md` and
`papers/md/groot_n16_2025.md` both exist and are parsed. No files under `papers/notes/` or
`corpus/rows/` for either. `grep -c "helix\|groot_n16" paper/survey.md` returns 0. The five bib
entries without rows are `bicchi_grasping_chapter_2001`, `bicchi_hands_2000`, `dlr_hand_ii_2001`,
`groot_n16_2025` and `helix_2025`, which is not the five-work paywall list in `paper/METHOD.md`.

**The problem behind the problem.** Sec. 3.4 accepts a Teslarati paraphrase of a patent, a WeChat
post relayed by a trade magazine and a Y Combinator post as sources for hand specifications. A
Figure AI engineering blog is better evidence than any of those, and it is the one source that
would have complicated the cleanest finding in Sec. 3.6. Whether or not that is what happened, the
inclusion rule has to be stated, because a reader who notices will assume it.

**The fix.** Write the note and the row for both, or state the exclusion rule explicitly in
`paper/METHOD.md` and in Sec. 1: industrial blog posts with no success rate, no trial count and no
task definition are recorded as vendor claims and are not counted as method rows. Then, in Sec.
3.6, keep the claim but qualify it: no company-announced hand appears in a method row in this
corpus, and the nearest thing to an exception is `helix_2025`, which reports finger-level control
on Figure's hand with no numbers of any kind. Reconcile `paper/METHOD.md`'s unobtainable-sources
list against the five rowless keys while you are there.

### 9. major — A verdict on fifty years of analytic work rests on one book chapter

**Location.** Sec. 1, "The analytic theory answered the static question and stalled on the dynamic
one." Sec. 2.2, whose four paragraphs cite `bicchi_grasping_chapter_2001` three times.

**The problem.** This is the survey's historical thesis and it is sourced almost entirely to a
single 2001 Springer book chapter, quoted six times across Sections 1, 2.2 and 2.3. The three
canonical reviews of that tradition are in the bibliography as metadata only. What is missing
entirely is the planning literature that took up exactly the dynamic question the survey says the
tradition stalled on: finger gaiting, rolling-contact manipulation, regrasp planning. None of it is
in the corpus, so the claim that the tradition stalled is untested against the work that did not
stall.

**The evidence.** `corpus/bib.json` holds 16 entries dated before 2018 and only four of those are
analytic-manipulation theory: `ferrari_canny_1992`, `okamura_overview_2000`, `bicchi_hands_2000`,
`ma_dollar_dexterity_2011`, plus `roa_suarez_grasp_quality_2015`. Three of the five could not be
obtained, per `paper/METHOD.md` and Sec. 7.3. `bicchi_grasping_chapter_2001` is the only readable
one with substantive content, and it does not have a row, only a note. 138 of the 221 entries are
dated 2024 or later.

**The fix.** Either add two or three works from the finger-gaiting and rolling-contact planning
line and test the claim against them, or soften the claim to what the evidence supports: the
analytic tradition produced closure tests and quality measures that a controller cannot use
directly, on the evidence of one chapter by one of its architects, and this survey did not survey
that tradition. Say plainly in Sec. 1 that the corpus's pre-2018 coverage is four works and that
the survey is therefore a survey of the learned era.

### 10. major — Section 8 restates Sections 3 to 7 in a template

**Location.** All of Sec. 8, 1,906 words.

**The problem.** 8.1 is Sec. 5.8 again, with the same `physhoi_2023` example and the same
`dexpbt_2023` line of code. 8.2 is Sec. 7.3 again, with the same `toporetarget_2026` numbers and
the same `dextrack_2025` quotation, which by then has appeared four times in the document. 8.3 is
Sec. 5.2.2's last two paragraphs. 8.5 is Sec. 5.5. 8.7 is Sec. 3.4. 8.8 is Sec. 6.2 and 6.5. 8.9
is Sec. 5.3.1 and 5.3.4.

Each gets a heading, three paragraphs and a "What would close it" line. The template is what makes
the generic entries look like findings: 8.3, 8.7 and 8.10 read like the others because they are
shaped like the others.

**The evidence.** The `dextrack_2025` quotation "Despite severe hand-object penetrations ... the
hand still interacts effectively with the object" appears in Sec. 4.2, Sec. 5.4, Sec. 7.3 and Sec.
8.2. `physhoi_2023`'s zeroed reward appears in Sec. 5.8, Sec. 7.2, Sec. 8.1 and Sec. 9.

**The fix.** Cut Sec. 8 to about 600 words. Keep the "what would close it" lines, which are the only
new content, and attach each to the section that established the finding. If a standalone gaps
section is wanted, make it one page of numbered claims with a cross-reference and the closing
action, and nothing else. The conclusion already does this well and does it in 438 words.

### 11. major — Section 3.4 is a list pretending to be an argument

**Location.** Sec. 3.4, "Announced and unreleased hands", 1,000 words.

**The problem.** Eight paragraphs, each of the same shape: vendor page, HTTP 404 or empty fetch,
circulating number, "has no reachable source". There is one argument in the subsection and it is
stated in the opening line, that three kinds of evidence are being conflated. Everything after it
is an inventory. The finding that matters — the hands with the highest advertised DoF have the
least specification behind them — arrives in Sec. 3.6 as a single number and lands harder there.

**The evidence.** Read Sec. 3.4 with Table 3 in front of you and every sentence is a cell. Table 3
does not exist yet, see finding 1, but when it does this subsection becomes its caption.

**The fix.** Cut to 300 words: the three-kinds-of-evidence paragraph, the Figure 03 case as the
worked example because it is the one where the tracker contradicts the circulating number, and the
Xiaomi case because it is the one where the readable source contradicts both circulating figures.
Everything else goes into Table 3's source-quality column. Then delete Sec. 8.7, which says it a
third time.

### 12. major — Gap 8.6's headline number is mostly hands that cannot be bought

**Location.** Sec. 8.6, "Fourteen of the 33 table hands appear in at least one method row and 19
appear in none", under the heading "Hardware is multiplying faster than the software that carries
it."

**The problem.** Sec. 8.7 states that 14 of the same 33 hands "are neither sold nor open", and Sec.
3.6 states that no company-announced hand appears in any method row. The two facts together mean
most of the 19 unused hands are unused because they do not exist to be bought. Netting them out
leaves roughly five buyable-but-unused hands, which Sec. 3.6 names as seven. Either way, the claim
that hardware is outrunning software is carried by press releases, and a reader who does the
subtraction will discount the whole gap.

**The evidence.** Sec. 8.6 and Sec. 8.7 as quoted, and Sec. 3.6's list of sold-and-unused hands:
Unitree Dex5, Tesollo DG-5F, ORCA, RUKA, Ruka-v2, BiDexHand, DexHand. Also note that the hand list
was assembled by a dedicated hands-and-vendors bibliography search that deliberately sought
announced hardware, per `paper/METHOD.md`, while the method list was assembled by topic searches.
The two lists were built to different inclusion rules, so a comparison of their sizes measures the
search design in part.

**The fix.** Restate the gap on the buyable hands only: seven documented, purchasable hands take
zero method rows between them, and the simulators ship six hands of any kind. Move the announced
hands into 8.7 where they belong and say in 8.6 that the 33-hand denominator includes 14 hands
nobody can buy, so it is not the right denominator for a software-lag claim.

### 13. major — "A survey of 216 works" counts vendor product pages as works

**Location.** The subtitle, "A survey of 216 works, with an evaluation frame and the gaps it
exposes."

**The problem.** The 216 is the row count, and it includes 33 hand rows that are mostly vendor
pages and press articles, 14 other surveys, 15 datasets, 15 simulators and 8 sensors. The
literature the survey actually analyses is 110 method papers. Leading with 216 buys a size
impression the corpus does not support, in a document whose whole argument is that numbers need
their denominators.

**The evidence.** `corpus/rows/*.json` by class: method 110, hand 33, dataset 15, simulator 15,
survey 14, benchmark 14, sensor 8, eval-protocol 7.

**The fix.** "A survey of 110 method papers, 33 hands, 15 simulators and 14 benchmarks, with an
evaluation frame and the gaps it exposes." Longer, accurate, and it previews the structure.

---

## Which of the ten gaps survive

The test: would the same sentence be true of robot locomotion, or of robot learning generally? If
so it is a complaint about the field's culture, not a finding about dexterous manipulation.

**Survive, six.**

- **8.2, no method reports interpenetration for its own rollouts.** Specific by construction.
  Contact multiplicity and the light-object mass ratio are what make penetration load-bearing for
  hands, and the survey establishes that in Sec. 4.1 with Le Lidec's own Solo-12 result showing the
  contact model "hardly affects" a walking robot on flat ground. The gap is the survey's best, and
  the 11-of-110 count with the seven-offline breakdown is a measurement rather than an opinion.
- **8.4, the evaluation-methodology literature contains no dexterous hand.** A claim about the
  intersection of two literatures, checkable, and false of locomotion, which has its own transfer
  and benchmarking protocols. The denominator of seven is small and should be stated as such.
- **8.5, generalist policies are largely not evaluated on hands.** Dexterity-specific by
  definition, since the claim is about hands against grippers. The DoF-median contrast, 6 for VLA
  rows against 16 for RL rows, is the sharpest single number in Sec. 8.
- **8.6, hardware is multiplying faster than the software that carries it.** Survives the
  locomotion test: quadrupeds have converged on a handful of platforms, hands have not. Does not
  survive finding 12 above without repair, because its denominator is wrong.
- **8.8, bimanual runs on one coordination architecture and one paper has ablated it.** Specific,
  well-evidenced, and it makes a judgement: 9 of 12 monolithic, `asymdex_2024` the only ablation,
  0.0429 against 0.7701, the dominant architecture tested once and beaten. This is the second-best
  gap in the section.
- **8.9, human data does not port across hands and the map is usually unstated.** Retargeting
  across hand morphologies has no locomotion analogue of comparable difficulty. The `objdex_2024`
  counterexample, that more correspondence made things worse, is what raises this above a
  complaint.

**Fails the test, three.**

- **8.3, reward weights are not recoverable.** Equally true of any RL subfield, and the draft
  concedes that five of its six cases are its own converter's limitation. It is also a sub-case of
  8.1. Fold the `robot_synesthesia_2023` case, which is a genuine irreproducibility and not a parse
  artefact, into 8.1 and delete the heading.
- **8.7, announced hands cannot be checked.** This is a finding about press releases, not about
  dexterous manipulation research, and it is equally true of humanoids, quadrupeds and grippers.
  Nothing in the research programme is blocked by it, because Sec. 3.6 establishes that nobody uses
  those hands. Merge into 8.6 as one sentence.
- **8.10, failure modes are reported as prose or not at all.** Generic across robot learning, and
  the draft says so itself: "This gap is the weakest evidenced of the ten, and the weakness is
  ours." Admirable honesty, and the correct response to it is deletion, not publication with a
  caveat. The point survives inside Table 8's reporting column.

**Real, but misfiled, one.**

- **8.1, released code does not implement the published reward.** The measurement is excellent and
  original: 61 released, 37 disagreements, 16 hard contradictions with 15 at high confidence, and
  the honest classification of the other 21. But the finding is a finding about robot learning, not
  about dexterous manipulation. `dreureka_2024`'s counted repository is a locomotion repository.
  This is the survey's strongest empirical result and it deserves better than the Sec. 8 template.
  Promote it: make Sec. 5.8 the numbered finding it already is, and in the conclusion claim it as a
  contribution to robot learning generally with a dexterous corpus as its sample. Then it is not a
  gap in this field and does not need to pretend to be one.

**Count: six of ten survive as stated, one is a real result in the wrong section, three should go.**

---

## Scope and selection

### 14. major — The corpus is a 2024-2026 corpus and the survey does not say what that costs

**Location.** `paper/METHOD.md`, "What this method cannot do", and Sec. 1's scope paragraph.

**The problem.** `paper/METHOD.md` concedes that search favours "work that is indexed, in English,
and posted as a preprint". It does not concede the recency skew, which is the larger effect, and
Sec. 1 does not mention selection bias at all.

**The evidence.** `corpus/bib.json` year histogram: 2026 26, 2025 61, 2024 51, 2023 28, 2022 15,
2021 9, 2020 8, and 23 entries in total across every year before 2020. 138 of 221 entries, 62
percent, are 2024 or later. Among method rows: 2025 32, 2024 31, 2023 16, 2026 13, 2022 10, and 8
across all earlier years combined.

Two of the survey's claims are sensitive to this. The historical verdict in Sec. 1, see finding 9.
And Sec. 5.7's convergence thesis, "In the variants that dominate 2025 and 2026 work, the reward is
no longer the objective of the deployed policy", which is an argument about a trend measured on a
corpus that is three-quarters recent by construction. The thesis is the best idea in the paper and
it deserves a denominator that can support a trend claim.

**The fix.** Add the year histogram to Appendix A and one sentence to Sec. 1: the corpus is 62
percent 2024 or later, so it describes the learned era well and the analytic era barely, and any
statement here about a trend over time is a statement about 2022 onward.

### 15. minor — Table 6's cells are truncated mid-word and it cannot be read

**Location.** Table 6, e.g. "four RealSense D415 RGB-D cameras tracking a bare hand, markerless; a
coloured glove is w…".

**The problem.** Roughly half the cells in the first three columns end in an ellipsis mid-word.
`paper/SECTION_BRIEF.md` requires that a table be discussed rather than pointed at, and Sec. 5.3.1
does discuss it, but a reader cannot check the discussion against the table.

**The fix.** Drop the operator-interface and retargeting-objective columns to a two-word category
each, since the prose already gives the four retargeting families in full. Or move the whole table
to an appendix at full width. The caption also says "29 rows" while the table has 30 data rows.

### 16. minor — Table 9 is 84 empty cells

**Location.** Sec. 7.6 and Table 9.

**The problem.** A table with no content, plus 300 words explaining that it has no content, plus a
caption repeating it. The idea is good and the argument is made completely by the prose: no
published number carries the interval, the denominator and the criterion that Table 8 asks for.

**The fix.** Keep Sec. 7.6's two paragraphs, delete the table, and say the matrix is released as
`corpus/` machinery for someone else to fill. Or keep the table and cut the prose to two sentences.
Not both.

---

## Length, and what to cut

Prose word counts against `paper/SECTION_BRIEF.md` targets, excluding tables and the HTML comments:

| section | prose words | target | over |
|---|---|---|---|
| 1 | 826 | 800 | +3% |
| 2 | 1,170 | 900 | +30% |
| 3 | 2,919 | 2,200 | +33% |
| 4 | 3,058 | 2,200 | +39% |
| 5 | 4,450 | 3,500 | +27% |
| 6 | 1,971 | 1,600 | +23% |
| 7 | 2,669 | 2,000 | +33% |
| 8 | 1,906 | 1,400 | +36% |
| 9 | 438 | 400 | +9% |

The brief allows 20 percent over for substance. Seven of the nine sections exceed that. Which do
not earn it:

**Section 8, cut 1,300 words.** Finding 10. It is the only section where the overrun is pure
duplication.

**Section 3.4, cut 700 words.** Finding 11.

**Section 3.3, cut 300 words.** Six bills of materials quoted verbatim in sequence is a price
column, and Table 2 has one. Keep the framing sentence about inconsistent bases, keep ORCA as the
worked case because it is why the column is empty rather than converted, keep the two hands with no
cost figure, and put the rest in the table.

**Section 5.5, cut 250 words.** Two paragraphs of consecutive quotations, five gripper-only and
eight hand-evaluating, each introduced with "X writes". The finding is the DoF contrast in the
third paragraph. Compress the roll-call to two sentences with the keys in parentheses and lead with
the finding.

**Section 4.4, keep as is.** It is 39 percent over and every paragraph does work. The four-headline-
figures-measure-four-quantities opening is the clearest writing in the draft.

**Section 7.4 and 7.5, keep as is.** The Wilson-width-to-trial-count derivation and the power
calculation are the most reusable pages in the survey, and the honesty of "So 100 trials buys a
20-point effect and nothing finer, and the protocol says so rather than implying more" is the voice
the brief asked for.

Net: about 2,550 words out, which brings the draft close to its targets without touching anything I
would want to read.

---

## What is good, and why

Named so the authors do not cut the wrong things.

**Sec. 4.1 and 4.2 are the best part of the survey and the reason to publish it.** The argument is
mechanistic rather than rhetorical: a grasp is many persistent contacts near stiction on an object
much lighter than the mechanism, that makes it hyperstatic and ill-conditioned, per-contact solvers
inject spurious jamming forces at stiction, and locomotion does not have this problem because a
walking robot makes a few contacts against ground far heavier than itself. Then it is priced:
Erez's factor-of-500 timestep spread, Dojo's −28 mm and −46 mm against MuJoCo's speed advantage in
its own Table V, ComFree-Sim's 1.7 ± 4.9 mm on fingertip-sized primitives. The conclusion, that the
two simulators carrying 41 of 110 method papers create the depth every step and do not hand it to
the user, is earned. No predecessor in this corpus has any of it.

**Sec. 5.8 is original empirical work.** Reading 61 repositories against their papers is not a
literature summary, and the `physhoi_2023` finding — the rotation term weighted 0.1 in Table 4 and
`torch.zeros_like` in the shipped reward, with a position-only success criterion that could not
have caught it — is the kind of thing a survey exists to find. The observation that a zeroed term
is worse than a missing one because it survives a reader's check of the file is the best single
sentence in the draft.

**Sec. 5.7's convergence argument is the survey's one genuine idea.** That reward engineering has
moved upstream into data curation, so every reward-shaping pathology now reaches the shipped policy
through a dataset rather than a gradient, is a claim no predecessor makes and the corpus supports.
Give it more room than Sec. 8, not less.

**Table 1's last column, "shortest honest success criterion", does real work.** It is where the
"no agreed criterion" finding becomes visible rather than asserted, and the closing observation
that both such cells are families with a second body involved is a genuine pattern.

**Sec. 6.2 makes a judgement and shows its evidence.** "The concentration is not the outcome of a
comparison that was won", followed by the two papers that compared and disagreed, followed by
`asymdex_2024`'s ablation with numbers. That is what the brief asked for.

**Sec. 7.1's first three paragraphs.** 87 with a real robot, 55 stating a trial count, median 20,
Wilson interval 39 to 78 at a reported 60 percent, and "Two methods separated by 20 points at the
median trial count are not separated at all." Four sentences, one conclusion, no hedging.

---

## Minor, at the end

### 17. Banned words and prose rules: substantially compliant

I checked `paper/SECTION_BRIEF.md`'s list across the draft with the HTML comments stripped.

- **Banned words: clean.** The only hit is "realm" inside the product name "RealMan RM75-6F" in
  Sec. 5.5, which is a false positive. No occurrence of novel, seminal, paradigm-shifting,
  leverage, delve, landscape, crucial, pivotal, tapestry, testament, underscore or showcase.
- **Em-dashes: two,** both inside one verbatim quotation of trade press in Sec. 3.4,
  "gripper—three fingers and an opposable thumb—equipped with tactile sensing". Quoted material,
  acceptable, but consider paraphrasing since the quote is doing no work the paraphrase would not.
- **Arrows: none** outside the figure comment blocks, which should be deleted anyway.
- **"many works" / "several papers": zero occurrences.** This is hard and the draft did it.
- **Semicolons joining clauses: eight lines,** of which three are table captions and five are
  Appendix A. Appendix A is a verbatim copy of `paper/METHOD.md`, which was written before the
  prose rules bound it. Either rewrite Appendix A to the rules or state that it reproduces the
  method document unchanged.

### 18. Sections that open by announcing themselves

`paper/SECTION_BRIEF.md`: "Do not open a section by announcing what the section will do." Sec. 4.2
opens "Table 4 is the engine-by-engine comparison, one row per simulator, built only from what a
note confirmed." Sec. 6.4 opens "Table 7 carries the bimanual papers on the same columns as every
other method here." Sec. 7.6 opens with a description of how its rows were chosen. In each case the
first fact should come first and the table provenance should follow.

### 19. The penetration breakdown reads as a partition of 110 and sums to 94

Sec. 5.2.2, "Across all 110 method rows, 83 do not address penetration, 5 constrain it, 3 measure
it and 3 penalise it." That is 94. The missing 16 are the rows where the note does not settle it,
and Sec. 8.2 states them correctly as "16 do not settle it". Add the 16 here too. In a survey whose
argument is that denominators are not stated, an unstated denominator is expensive.

### 20. The RL count changes from 53 to 59 without explanation

Sec. 1, "53 train with reinforcement learning". Sec. 5.1, "53 carry the tag `RL`". Sec. 5.2.1,
"Fifty-nine of the 110 method rows learn from a reward." Both are right: 59 is `RL` plus `RL+demo`,
verified against `corpus/rows/*.json`. Say so in Sec. 5.2.1, in four words.

### 21. The nine company-announced hands are not the nine hands Sec. 3.4 discusses

Sec. 3.6 lists "Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi, Clone, Daxo and PaXini".
PaXini is discussed nowhere in Sec. 3.4, and Proception and AgiBot are discussed at length in Sec.
3.4 but are not in the nine. Align the two lists or say why they differ.

### 22. Figure 03 and Figure 3 collide

Sec. 3.4 calls the Figure AI product "Figure 03" in a document where "Figure 3" is a diagram of the
simulation step. On first use write "the Figure 03 hand" or "Figure AI's 03", and never start a
sentence with it, as Sec. 3.4 currently does: "Figure 03 is the clearest case of a number outrunning
its source."

---

## Counts

- **blocking: 1** (finding 1)
- **major: 13** (findings 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
- **minor: 8** (findings 15, 16, 17, 18, 19, 20, 21, 22)

**Gaps surviving the generality test: six of ten** — 8.2, 8.4, 8.5, 8.6, 8.8, 8.9. One more, 8.1,
is a real and original result misfiled as a gap and should be promoted rather than cut. Three fail
— 8.3, 8.7, 8.10 — and should be merged or deleted.

## Verdict

Publish it, after the tables are put back and the positioning is repaired. There is a real paper
here and it is not the one the table of contents advertises. The survey's contribution is not
breadth: on breadth it is one of five overlapping 2025-2026 reviews and it has not fairly
characterised two of them. Its contribution is that somebody finally opened the repositories and
the simulators and measured two things nobody had measured — that 37 of 61 released codebases
disagree with their own paper about the objective that was trained, with 16 hard contradictions,
and that 11 of 110 methods address interpenetration at all while not one reports a number for its
own policy's rollouts. Those two results are worth a venue on their own, and Sections 4.1, 4.2, 5.7,
5.8, 6.2 and 7.1 to 7.5 build the case for them properly, with mechanism and with numbers. What
stands between that paper and this draft is a blocking production failure, four absent tables and
two absent appendices that leave a third of the document arguing from evidence the reader cannot
see; a positioning paragraph that omits a physics-engine review sitting in its own corpus,
measures a predecessor's coverage in parse artefacts, and claims as new an evaluation layer that
the most recent predecessor already named; a taxonomy presented as complete that leaves twenty
rows homeless without saying so; and about 2,500 words of inventory and restatement, concentrated
in Section 8 and Section 3.4, that make generic complaints look like findings and will cost the
paper credit for the six gaps that are real. None of that is a reason to reject. All of it is a
reason not to accept as it stands.
