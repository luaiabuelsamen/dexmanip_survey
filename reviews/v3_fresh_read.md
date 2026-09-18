# v3: a fresh read

Reviewer: a robot-learning researcher who had not seen this document, any of its drafts, or any
previous review before opening `paper/survey.md`. Sections 1–4 below were written after one pass
end to end and before opening `reviews/`. Section 5 was written afterwards.

Measurements I took to check my own impressions, so the numbers below are reproducible:

| section | prose words (tables and HTML comments excluded) | total words |
|---|---|---|
| 1 Introduction | 1,377 | 2,258 |
| 2 Taxonomy | 1,418 | 1,954 |
| 3 Hands | 3,394 | 5,937 |
| 4 Simulators | 3,963 | 5,040 |
| 5 Training | 4,993 | 13,153 |
| 6 Bimanual | 2,253 | 2,253 |
| 7 Evaluation | 5,016 | 6,108 |
| 8 Gaps | 1,099 | 1,099 |
| 9 Conclusion | 552 | 552 |
| App. A/B/C | 939 / 205 / 2,328 | 939 / 4,098 / 4,130 |

---

## 1. First impression

### What I did not know before reading

Five things, in the order they surprised me.

**The Allegro cannot be specified from a page a reader can open.** I have used Allegro numbers in
talks. I did not know that "Its product page at allegrohand.com/v4 returned HTTP 404 while the
Wonik wiki timed out" and that "Everything Table 2 confirms about the most-used hand in the corpus
comes from its ROS driver: 16 joints, four fingers, a torque interface, a 333 Hz CAN clock, 12 V,
no tactile sensing. Its weight, joint torque, payload and price have no reachable source." That is
a genuinely new and useful fact about a platform 35 corpus papers run on, and §3.2 lands it in
three sentences.

**`physhoi_2023`.** "Its `compute_humanoid_reward` hardcodes the body position-velocity error and
both object rotation errors to zero, with the real computation commented out beside them, and does
so unconditionally rather than per dataset, while its Table 4 lists non-zero weights of 0.1 and
0.01 for those rotation terms on GRAB." Plus the kicker: "its own position-only success criterion
could not have caught that." This is the best single paragraph in the survey. It is a specific,
checkable, consequential claim about a paper whose 95.4 percent I have seen cited as a baseline.

**The IsaacGymEnvs interpenetration code.** I did not know that NVIDIA's own repository already
computes per-environment maximum interpenetration in Warp and gates the policy update on it:
"Environments are split on `max_interpen_dists <= interpen_thresh` and the surviving reward is
scaled by `1 - tanh(max_interpen_dists / interpen_thresh)`, with `interpen_thresh: 0.001`". The
rhetorical move — the field's own benchmark repository does the thing the field says is hard — is
the strongest argument in the document and it is made with a file and line numbers.

**The Dojo table read correctly.** "MuJoCo penetrates −28 mm at Δt = 0.01 s and −46 mm at
Δt = 0.001 s ... The MuJoCo column is not a trend. A ten-times-smaller step produces more overlap,
which no timestep-independent stabiliser does." I have seen that Dojo table used as evidence that
MuJoCo penetrates. §4.2 refuses to use it that way and says why, then puts Drake's SAP bound
"six orders of magnitude below Dojo's MuJoCo cell at the same step" beside it and concludes "The
depth is a setting." This is real technical reading, not table-copying.

**ORCA's durability run.** "silicone skin degrading on two fingertips after about 2,000 to 4,000
grasp cycles and sensor wires snapping on three after about 4,500 to 7,000. The sensing wore out
an order of magnitude sooner than the hand." I had never seen a hand paper report a wear-out
distribution and I will cite it.

Also new to me, in aggregate rather than as single facts: that the analytic-versus-learned
handover is a *smoothing* equivalence (`pang_global_planning_2022` "proves that the randomised
smoothing implicit in reinforcement learning and an analytic log-barrier relaxation compute the
same local linear model of contact"); that taxel counts have risen three orders of magnitude while
"the policies consuming them have stayed at binary contact"; and that of the eight papers with
tactile hardware on the deployed hand, "Almost none of the eight uses a high-resolution sensor."

### What I skimmed, and where I was bored

I skimmed, honestly and completely:

- **Table 7** (112 rows × 14 columns). I read the header, spot-read four rows, and never came
  back. The algorithm column carries 200-word cells; the `sim` cell for `diffusion_policy_2023`
  is a paragraph. Nothing in the document tells me how to use this table, and §5.9's 83-word
  introduction does not try. It is a database dump printed in a survey.
- **Table 6** (30 rows of teleoperation systems). Same problem in miniature: the "operator
  interface" column is a sentence per row. The four-way retargeting taxonomy in the prose
  underneath is good and I read that instead.
- **Appendix B**, entirely. It is the same 33 hands again at full width. I understand the
  motivation ("Table 2 and Table 3 ... truncate their cells to stay readable") but I did not
  consult it once.
- **Appendix C.1** (77 rows). I read C.2 — the per-paper disagreement text — and that was worth
  reading.
- **§7.5**, second half. "37 pairs per arm at a discordance of 0.2, 57 at 0.3, 77 at 0.4 and 96 at
  0.5" and then "457 pairs" for the correlation axis. This is careful and I believe it, but four
  consecutive paragraphs of interval arithmetic with no worked reason to prefer one number lost me.
  The single sentence that earns the whole subsection — "two rates each carrying ±10 points do not
  resolve a 10-point difference between them, because the difference's standard error is larger by
  a factor of √2" — is buried in the middle of a paragraph.

Boring in a different way: **§3.4 and Table 3**. Thirteen rows of announced hands with 61 percent
of cells empty. The finding is one sentence and §3.6 states it well ("None of the nine
company-announced hands in Table 3 appears in a single method row"). Getting there through
Daxo's actuator arithmetic and Tesla's patent paraphrase felt like reading someone else's
fetch log. The scepticism paragraph is good writing; the table it defends is mostly blank.

### Where I stopped believing it

Three places.

**The bimanual denominator.** §2.3 told me the number is 25: "Section 6.2 narrows again, to the 25
papers whose notes place a learned controller on two dexterous hands." §6 then told me, in bold,
"**The denominator for this section is 28**". §6.2 says "Twenty-one of the 28 put one policy over
both hands". §8.6 says "Nineteen of the twenty-five rows that Section 6.2 counts as putting a
learned controller on two dexterous hands run one policy over a concatenated two-hand
observation." So the same set is 25 and 28, and the same subset is 19 and 21, in four places, one
of which cites another by name. After this I stopped taking any count on trust and started
grepping. That is the wrong reading mode for a survey whose whole pitch is arithmetic hygiene.

**The reproducibility number.** §5.8 spends 815 words arriving at "Ten is the number to quote,
eight at high confidence". §8.1 and §9 repeat ten. Then §7.2 says:

> Section 5.8 decomposes 37 of them — the thirty-eighth, `groot_n16_2025`, arrived after that
> decomposition — into 16 contradictions, 9 limitations of this survey's own parsing, 7 components
> never released, 3 version skews and 2 inconsistencies internal to a paper, and concludes that 16
> is the number to quote. Sixteen of 62 code-releasing rows is 26 percent, and that is the figure
> this section and Table 8 use.

§5.8's actual decomposition is "Ten are contradictions ... Thirteen are limits of this survey's own
parse ... Eight released code without the described component in it, three are version skew ... and
three are a paper disagreeing with itself." §7.2 attributes to §5.8 a five-way split §5.8 does not
contain, and reverses its conclusion. Table 8's reproducibility row then propagates the wrong one:
"16 of the 62 code-releasing method rows carry a true contradiction". A survey that makes its
headline finding out of other people's papers disagreeing with their own code cannot disagree with
itself about that finding, in a table, in the section that proposes the fix.

**The numbers that were audited in §7.1 and not propagated.** §7.1 describes a hand audit of the
extraction nulls and says it "moved the headline from 55 rows to 70 ... and the unseen-object
count ... 32 to 39". §5.9, 400 lines earlier, still reads: "only 31 rows state an environment
count, only 55 state how many real trials are behind the headline number, and only 32 state how
many unseen objects were tested." And Appendix A still describes the audit at its pre-audit size:
"Of the 32 method rows that had a real robot and no recorded trial count, 13 carried a count in
plain text in their own note", against §7.1's "Of the 34 method rows with a real robot and no
trial count, 15 had the count written in their own note". Three different versions of the same
audit in one document, including in the appendix that exists to explain the method.

### Did the tables and figures help or get in the way

**Helped.** Table 1 is the best table in the survey. Six rows, six columns, and the last column —
"shortest honest success criterion" — does something no other table here does: it converts the
literature into a thing a reader can act on, and it is honest where there is nothing to convert
("no agreed criterion"). Table 4's structure is right even where its cells are empty, because the
emptiness is the argument and §4.2 says so. Table 5 is compact and its four-valued marks
(`paper` / `code` / `both` / blank-for-`code (0)`) carry a real distinction. Figures 1, 4 and 6
carry their captions, their denominators and their provenance inside the SVG, which is more
discipline than most published figures have; Figure 6's footer — "Every bar is a floor" — is
exactly right.

**Got in the way.** Table 7 and Table 6, for the reasons above. Table 10 is the worst placement
decision in the document: it is the *first* table a reader meets, on page two, 14 rows wide by 8
columns, five of whose rows are "*source not obtained*" repeated across every cell, and it is
numbered 10. A reader opening a survey and finding Table 10 before Table 1 concludes, correctly,
that this section was written last. It is also the only table at `##` heading level while every
other is `###` — no, inverted: Table 1 is `##` and all nine others are `###`.

**Actively in the way:** lines 1504–1564, between Table 7 and Section 6, are a 678-word HTML
comment containing the specification for Figure 4, including:

> STILL TO DO.
> 1. THE CROSS-LINKS ARE MISSING AND THEY ARE THE POINT. The footer says the branches are not
>    exclusive, then a strict tree is drawn.

I checked: `paper/figures/fig4_taxonomy.svg` contains one `<path>` element and no
`stroke-dasharray`, so the cross-links are indeed still missing. The comment is accurate, it is
addressed to the author, and it is in the manuscript. It also contains the sentence "THE RULE,
after the R3 review", which told me there had been reviews before I was asked not to read them.

One smaller collision: §7.3 quotes `dextrack_2025` saying "Despite severe hand-object penetrations
in Figure 4c and Figure 4a", and this survey's own Figure 4 is the taxonomy tree.

Finally: there is no abstract. The front matter is a title, a subtitle, the one-line claim
"A survey of 218 works, with an evaluation frame and the gaps it exposes", and a provenance note.
For a document of this length that is a structural omission, not a stylistic one — §9 contains
what the abstract should say and a reader reaches it at word 27,000.

---

## 2. Does it hold together as one document

Not yet. It reads as nine well-written pieces with a revision pass that reached some of them.
The seams are not tonal — they are arithmetic, and they are load-bearing.

### Same fact, two numbers

Beyond the three cases in §1 above:

**Isaac Gym.** §1: "Of the 112 method papers in this corpus, 53 train with reinforcement learning
and 35 run in Isaac Gym." §4.3: "Thirty-six of the 112 method papers in this corpus run on it."
Figure 1's own node reads `Isaac Gym 36`. (My crude match over `corpus/rows/*.json` returns 35, so
the intro may be the right one and the figure wrong — which is worse, because the figure claims to
be "Recomputed from corpus/rows at draw time".)

**LEAP.** §3.2: "the Inspire RH56 family for 19, a parallel-jaw gripper for 12 and LEAP for 11."
§3.3: "Eleven of the 103 hand-naming method rows use an open-hardware hand, and all eleven are
LEAP." §5.2.1: "ahead of Shadow at 21 and 6 and LEAP at 12 and 4." §7.1: "Allegro appears in 35,
Shadow in 21, Inspire in 19 and LEAP in 12." The corpus rows say 12, so §3 is stale — and §3.3's
"all eleven are LEAP" is a substantive claim about open hardware built on the stale count.

**Code released.** §7.1: "Sixty-two released code and 46 did not, with four rows unsettled."
§5.8: "they sit inside the 62 rows that released anything." §8.1: "Sixty-one method rows released
code that could be parsed against the paper" and "Ten is a floor, since fifty method rows released
nothing to check." §9: "Sixty-one method papers released code". The corpus rows give 62 / 46 / 4,
so §8.1 and §9 are wrong twice over — 61 for 62, and "fifty" for 46 — and "fifty" is the number
the conclusion uses to bound the finding.

**Generalist policies on hands.** §5.5: "Eighteen method rows carry the `VLA` tag. Eleven evaluate
on a multi-fingered hand and six report no hand result at all ... Seven of the eleven state a hand
size". §8.4: "Eighteen rows carry the generalist tag. Fourteen of them settle whether the reported
evaluation ran on a multi-fingered hand, and eight of those fourteen did ... Of the eight, five
state the hand's degrees of freedom". Eleven versus eight for "evaluates on a hand", seven versus
five for "states a DoF count", and the two paragraphs are the body and the gap statement of the
same finding. §5.5 also says "Of the 59 reward-learning rows, 48 state a count ... their median is
16" while §8.4 compares against "16 over the 44 reinforcement-learning rows that state one."

**AsymDex's baseline.** §6.2: "the full method scores 0.7701 over five seeds, against 0.1086 for
relative frames without asymmetry and 0.0164 for asymmetry without them." §8.6: "`asymdex_2024`
scores 0.7701 on Block in cup over five seeds against 0.0429 for the symmetric monolithic
baseline." 0.0429 appears nowhere else in the document. Either §6.2 omitted the baseline §8.6
needs, or §8.6 invented a number; a reader cannot tell which.

**Paywalls.** §1: "All five are cited by metadata only and nothing here describes their contents."
Appendix A: "Six works are cited by metadata only ... Five are behind publisher paywalls ... The
sixth is Hwangbo et al. 2018 on RaiSim, whose hosted PDF returned no body." §9: "Six works are
paywalled and no claim rests on them." The conclusion converts a failed parse into a paywall.

**Version skew.** §5.8 and §8.1 both say "three version skew". Appendix C.2's own heading reads
"**version-skew, 4 rows.**" and lists four (`hora_2022`, `pi0_2024`, `groot_n1_2025`,
`groot_n16_2025`). The fourth is the `groot_n16_2025` row §7.2 calls "the thirty-eighth", so the
appendix is right and the two body sections did not absorb it.

### Same paper, two characterisations

**`teledexter_2026`.** §5.2.2: "`teledexter_2026` penalises interpenetration with a differentiable
signed-distance term, but during offline reference construction, not in the policy's reward."
§7.3: "That leaves four closed-loop policies in the whole corpus: `clutterdexgrasp_2025`,
`dexmachina_2025`, `dextrack_2025` and `teledexter_2026`." The survey's central finding is that
penetration is handled at the reference and never at the rollout, and §7.3's count of four
closed-loop policies includes a paper §5.2.2 places at the reference — the exact category error the
section is about. Worse, of those four, §6.4 shows `dexmachina_2025` "resolves it once, replaying
retargeted joints against a fixed object 'to eliminate object penetrations' and measuring nothing
during rollout", and §7.3 itself shows `dextrack_2025` "applies it only to the input kinematic
references". So three of the four are, by the survey's own evidence, reference-side. The fourth,
`clutterdexgrasp_2025`, is named twice in the whole document — here and once in a list of
object counts — and is never discussed. The finding survives; the count of four does not.

**Which hand a reader should buy.** §3.1: "Shadow, Sharpa, Wuji, the Ability Hand, RUKA, Faive and
the Allegro driver ship one [a URDF or MJCF]" — seven. §3.6: "A reader choosing a hand on this
corpus's evidence has two well-precedented options, an Allegro or an Inspire, and a third in LEAP
if eleven papers is enough." §9: "If you are choosing hardware, pick from the five real hands a
simulator already names." Seven, three, and five, for the same decision, in the same document. The
"five" traces to §8.5's "the five named are the field's defaults", but §9 does not name them and
the reader who follows the advice has nowhere to go.

**`dexterous_handover_2025`.** §2.1 uses it as a handover-family example; §6 says it "never
enters, because its row records `bimanual: no`"; §6.5 treats it as "The third case" of three
handover papers and then says "it is one of the rows the 28 excludes". Three passes over one
paper, each partially retracting the last.

### A term never defined, and one defined twice

**"Method row" is the survey's unit of account and is never defined.** It appears roughly 60 times
and carries every headline count. §1 says only that "The corpus behind all of this holds 221
bibliography entries, of which 218 carry a structured row read from a note." The other six classes
leak out one at a time — Table 10's footer ("one per corpus entry of class `survey`"), §6
("Benchmarks and datasets are outside the 28 by class"), §8.3 ("Seven corpus rows are evaluation
protocols") — and Appendix A, which describes the note template in detail, never lists the classes
or says how the 218 split into them. A reader cannot reconstruct any denominator in this survey.

**Defined twice, differently:** the interpenetration finding. §1 says "Eleven of the 96 method rows
whose notes settle the question address interpenetration at all, seven of the eleven do it outside
a closed-loop policy in a grasp synthesiser, a trajectory optimiser or a contact model". §7.3 says
"three penalise it, three measure it, five constrain it ... Six of the eleven are grasp synthesisers
or trajectory optimisers ... and `castro_sap_contact_2021` is a contact model rather than a
controller." These reconcile (6 + 1 = 7), but only if the reader does the arithmetic, and §5.2.2
gives a third cut of the same eleven ("85 do not address penetration at all, 5 constrain it, 3
measure it, 3 penalise it and 16 say nothing either way"). Three presentations of one finding, none
of which points at the others.

**Left unparseable:** §3.5, last two sentences of a paragraph: "Sixty-five of the 112 method papers
mention tactile sensing somewhere, which is the gap worth quoting. Thirty-five is the count over
this survey's notes." Thirty-five of what, measuring what, against which of the two preceding
numbers? I read it four times and cannot tell.

**Unexplained restriction:** §2.1 says "In-hand reorientation has 31 rows" and §5.2.1 says "17 of
the 31 reorientation rows". Table 5 is "the 21 in-hand reorientation methods". The ten missing rows
are never mentioned, so the reward-term census — one of the survey's strongest pieces of original
extraction — sits on a silently reduced denominator.

### A thread announced and not run

§1 promises: "`zhao_dexhand_survey_2026` ... already draws the distinction this survey builds on
... That is the reference-versus-rollout split, named by a predecessor before this survey measured
it." The phrase "reference-versus-rollout" then appears exactly once in the document — that
sentence. The idea runs (§5.4's "Penetration is handled at the reference, if at all, and never at
the rollout" is the same thought, well put), but the named frame does not, so the intro's promise
of a *frame* built on a predecessor's axis is never cashed as vocabulary the body uses.

§1 also promises three contributions on the penetration axis where Zhao gave none: "What Sec. IV-C
does not give is a threshold, a measurement method or a count. This survey supplies those three."
§7.7 then says: "The 2 mm penetration threshold is taken from `toporetarget_2026` with no
independent justification, and the captured human grasps in `grab_2020` sit above it at 3.25 mm,
which makes 2 mm a simulator convention rather than a physical bound." The survey supplies a count
and a method. It does not supply a threshold, and it says so 2,000 lines later.

Smaller: §1's roadmap lists sections 2–8 and omits Section 9, which is where the findings are
summarised. And §1 says "Section 5 covers how policies are trained and is the longest section" —
by prose, §7 is 5,016 words and §5 is 4,993.

### Where the style changes

The document has one dominant voice — impersonal, short declaratives, a finding per paragraph,
often a one-sentence verdict at the end of a paragraph. It is a good voice. Four places break it.

**Section 3 is more journalistic than anything else here.** "The Allegro's position is the
uncomfortable part." "A reader deploying torque control is bitten by that first." "The sensing wore
out an order of magnitude sooner than the hand." "The collapse is real at the cheap end and
secondhand at the expensive one, and it has barely moved the literature." This is the most enjoyable
section to read and it is recognisably a different hand from §5.8's "Weights drift." / "Zeroed terms
recur, and are not the same failure."

**Section 4 is the only section that cites by author name.** "Erez et al. built a 35-DOF arm
modelled on the Shadow Hand" (§4.1); "Le Lidec et al. show that per-contact solvers of the
projected Gauss-Seidel family" (§4.1); "Le Lidec et al. supply the taxonomy that organises it"
(§4.2); "Le Lidec et al. classify it as CCP-MuJoCo" (§4.2). Everywhere else in 27,000 words, works
are named by bibkey. Neither "Erez" nor "Le Lidec" is ever bound to a key in the sentence that
introduces it — the reader must infer `physics_engine_comparison_2015` and
`contact_models_comparison_2023` from a parenthetical later in the paragraph.

**Section 7 breaks into the first person and Section 9 into the second.** The section title is
"Evaluation: how we would compare these methods"; §7.7 says "Table 9 is empty because we filled no
cell"; §9 opens three paragraphs with "If you are publishing", "If you are running experiments",
"If you are choosing hardware"; and §5.1 says Table 7 "is the table to scan when looking for work
comparable to your own." These are the only four places with a grammatical person in the document.

**Nine places narrate the survey's own revision history to the reader.** "An earlier version of
this claim said that none reached it" (§5.5); "seven accusations an earlier draft of this section
made were withdrawn under adversarial review" (§5.8); "that pooled figure is the one an earlier
draft of this section quoted" (§7.1); "It is not enough for the ratio to the anchor that an earlier
draft asked each cell to report" (§7.5); "An earlier version of this section quoted 93, 169 and 387
per arm" (§7.5); "Under the bare substring test an earlier version used, 'UniDex' matched inside
'UniDexGrasp'" (§7.6); "The same bill computed from the independent-arm count, which an earlier
draft used, was 1200 rollouts and 20 hours" (§7.7); plus §5.2.2's "Three cells an earlier draft
marked `code`" and the figure comment's "the earlier plan ... is superseded". I want to defend
this — it is a survey about reporting honesty and it is modelling the behaviour it asks for. But
nine of them, in the body, addressed to a reader who never saw the earlier draft, reads as a
changelog leaking into the manuscript. Two or three, gathered in a limitations paragraph, would
carry the same credibility at a tenth of the interruption.

**One notational ambiguity born of the same seam.** `Sec. X.Y` is used for cited papers' sections
throughout ("its Sec. 5.3 measures the cost", of `anyrotate_2024`; "Sec. 5.4", of
`dynamic_handover_2023`) *and* for this survey's own sections in Appendix C ("The class is what
Sec. 5.8 and Sec. 8.1 count") and in the Figure 4 comment. The body otherwise uses "Section 5.8",
"section 5.8" and "§7.5" interchangeably for the same thing.

---

## 3. Structure

### Is Section 5 earning its 5,000 words

Mostly yes, and the subsection that is not earning it is not the one I expected.

Subsection prose lengths: 5.1 196, 5.2 1,534, 5.3 1,021, 5.4 508, 5.5 351, 5.6 231, 5.7 248,
5.8 815, 5.9 83.

**§5.2 and §5.8 earn everything.** §5.2.2's reward-term census and §5.8's paper-versus-code census
are original extraction that exists nowhere else, and they are the survey's actual contribution.
§5.8 at 815 words is the highest-value-per-word passage in the document.

**§5.7 at 248 words is the most under-length section in the survey and it contains the best idea in
it.** "In the variants that dominate 2025 and 2026 work, the reward is no longer the objective of
the deployed policy. It is the objective of the process that produced the deployed policy's
training data. Reward engineering has moved upstream into data curation, and every reward-shaping
pathology in section 5.2 now reaches the shipped policy through a dataset rather than a gradient."
That is a thesis. It reframes §5.2 and §5.8 retroactively, it is the answer to "where has the field
converged", and §5.1 promises it ("Section 5.7 shows why"). It gets a quarter of the words §5.3.1
spends on teleoperation rig costs. If anything in Section 5 should grow, it is this.

**§5.9 at 83 words is not a section.** It is a caption for the largest table in the document, and
two of its three numbers are pre-audit (55 and 32, against §7.1's 70 and 39).

**What I would cut from Section 5:** §5.3.1's cost and latency inventory. The finding — "Only 12 of
the 30 rows carry a latency cell at all, three of those give no number, and only 7 state a rig
cost" and "The column mixes the two, so its spread is not a range" — is two sentences, and it
arrives after 300 words of walking the price column. §5.6 at 231 words is efficient and I would
keep every word; §5.5 at 351 words carries a claim §8.4 contradicts and needs reconciling rather
than cutting.

### Is the evidence in the right place

Three misplacements, in increasing severity.

**Table 10 is in Section 1.** A 14-row related-work comparison, five of whose rows are "*source not
obtained*", is the first table the reader sees, before the survey has said anything of its own. The
material in §1 lines 40–86 — what each predecessor covers and what this survey adds — is a
related-work section wearing an introduction's clothes. It also means the intro is 1,377 prose
words of which roughly 700 are about other surveys. The three contributions a reader needs early
("The three things this survey adds are narrower than a claim of breadth") arrive at word 900, and
the two findings a reader will actually cite — the paper/code census and the penetration census —
are compressed into one paragraph each at lines 62–68.

**Section 6.4 argues entirely from Table 7, which is in Section 5.9.** "Table 7 carries the
bimanual papers on the same columns as every other method here, and three of those columns are
worth reading together." The three columns are then read out in prose, which is the right thing to
do — but it means §6.4 exists only because Table 7 is somewhere else, and the reader who wants to
check it scrolls back 300 lines through a 112-row table with no bimanual marker.

**Section 8 argues from Tables 2, 3, 4 and 7, all of which are between 700 and 1,800 lines away.**
§8.5: "Nineteen of the 33 hands in Tables 2 and 3 appear in no method row, but 14 are neither sold
nor open and appear in none for that reason, so 33 is not the denominator for a software-lag
claim." That is a careful sentence and it is unverifiable in place. This is the structural cost of
putting the gaps last: every gap is a re-derivation from distant evidence, and §8's eight
subsections are 1,099 words for eight findings, so each gets 140 words to restate a case made
across 20,000.

The one placement that works very well: §4.2 puts the IsaacGymEnvs code evidence immediately after
Table 4, in bold, and explicitly says the table it just printed is wrong — "Table 4 records Isaac
Gym as not exposing penetration and `corpus/rows/isaacgym_2021.json` carries
`penetration_exposed: false`, which the code parse in the same corpus contradicts." That is the
right place for it. It also means a table in the published document is knowingly wrong and was
shipped anyway, with the correction in prose beneath it. I would fix the cell and keep the prose.

### Does the reader meet the central findings early enough

No, and the gap is about 20,000 words. The survey has three findings a reader will remember:
papers disagree with their own released code; nobody measures interpenetration on their own
rollouts; the hands that exist and the hands that get published on are different sets. All three
are stated in §1 — the first in one clause of one sentence ("Of the 112 method rows ... none
reports a penetration number for its own trained policy's rollouts"), the second not at all, the
third not at all — and all three are stated properly for the first time in §9, at word 27,000.

Concretely: the `physhoi_2023` case, which is the survey's single most citable fact, appears first
at line 1332 (§5.8), is restated at 2211 (§8.1), 2294 (§9) and in §7.2. It should be in the
abstract the document does not have, and in §1.

---

## 4. The abstract-level claim

The claim is "A survey of 218 works, with an evaluation frame and the gaps it exposes", and §1
narrows it: an evaluation frame, plus measured findings about reporting practice.

**Does it deliver the measured findings?** Yes, and these are the reason to cite it. Four are real,
original and checkable:

1. **The paper-versus-code census.** Ten contradictions in 62 code-releasing method rows, each
   classified, with seven accusations withdrawn and recorded ("a survey that names people should
   carry its retractions beside its accusations"). Appendix C.2 prints them. I have not seen this
   done for any robotics subfield.
2. **The penetration census.** Eleven of 96 rows address interpenetration; none reports it for its
   own rollouts; the engines are not the obstacle, with file and line numbers from IsaacGymEnvs.
3. **The hardware/software divergence.** Seven documented, purchasable-or-buildable hands with zero
   method rows; nine announced hands with zero; 61 percent of the announced table's specification
   cells empty against 39 percent for the purchasable one; the Allegro unspecifiable from any
   reachable page.
4. **The reward-term matrix**, with the `code (0)` distinction — a term present in the code with
   every shipped config zeroing its weight is neither "in the code" nor absent, and the survey is
   right that "Marking them `code` would tell a reader the code optimises something the paper does
   not state."

The reporting-practice statistics (§7.1) are weaker than these four but are handled with unusual
care: the null-audit disclosure — "every miss converts a reporting paper into a silent one, and the
survey's argument is that the field reports badly, so the artefact flatters the argument" — is the
most self-sceptical paragraph I have read in a survey, and the audit that follows it is real work.
The cost is that the audited numbers did not reach §5.9 or Appendix A.

**Does it deliver an evaluation frame?** Partly. Table 8 is a frame: seven axes, each with a
measurement, a count, a derivation, and a stated reason. The derivations are honest about which
statistic each count serves ("a single rate takes a Wilson half-width, a matched comparison takes
McNemar, a ratio takes the standard error of the log ratio, a correlation takes the Fisher-z
interval") and about what the counts do not buy (40 per axis "cannot establish that the
perturbation hurt at all"). The plausibility row is the frame's centre and its rule is exactly
right: "computed on the policy's own rollouts by code that never entered the reward or the
termination rule", because "a measure the policy optimised is not evidence about the policy."

What keeps it from being a frame I would adopt whole:

- **The 2 mm threshold is borrowed and the survey knows it.** "taken from `toporetarget_2026` with
  no independent justification, and the captured human grasps in `grab_2020` sit above it at
  3.25 mm, which makes 2 mm a simulator convention rather than a physical bound." Meanwhile §7.3
  shows the field's two definitions differ by a factor of eight and "neither source states its
  distance function precisely enough to reconcile them". A frame whose headline axis has an
  unjustified threshold and no agreed distance function is a proposal for a frame.
- **Table 9 is empty by design and the design is defensible** ("This survey re-ran nothing, and no
  cell can be filled at the denominator Table 8 asks for"), but §7.6 spends 660 words defending the
  row-selection rule for a table with no content, including two corrections to a ranking that
  selects which twelve empty rows to print. That is the clearest case in the document of effort
  spent in inverse proportion to the reader's need.
- **The bill is honest and damning to the frame itself.** "A two-policy comparison on three tasks
  is then 342 real rollouts on the matched set and 600 on the unseen-object set, 942 in all ...
  about 16 hours of robot time" and "16 hours of rollouts is most of a week of calendar time", in a
  field whose "modal per-cell count is 10 trials". §7.7's four preconditions include "Reviewers
  would have to reward 57 matched trials on one task over 20 unmatched trials on five, and nothing
  in the corpus suggests that is happening." I believe that sentence, which means the frame's own
  section predicts nobody will use it.

**Would I cite it, and for what?**

Yes, four times over:

- For `physhoi_2023`, and for the paper-versus-code census as a general claim about robot learning:
  "A reward table in a paper is a claim about a document, not about a run."
- For the penetration finding, which is directly load-bearing for anyone instrumenting a tracker
  for contact quality, together with the IsaacGymEnvs pointer and the `max_depenetration_velocity`
  observation ("The one knob here that governs interpenetration behaviour is being copied without
  being read").
- For §4.2 and §4.3 as the best available account of why a simulator's *name* no longer fixes its
  physics: "An experiment reported as Isaac Lab may be running PhysX 5 with TGS, or MuJoCo's soft
  constraint rows under Warp, and those two make different contact errors."
- For Table 2 and Table 3 as the only hand table I have seen that puts "what the force is" beside
  the force, and for §3.6's announced-versus-published finding.

I would not cite Table 8 as a protocol to follow, and I would not cite any single count from the
document without checking it against `corpus/rows`, because I found six counts that disagree with
another part of the same document.

---

## 5. Against `reviews/r5_generalist.md`

R5 raised 1 blocking, 13 major and 8 minor findings. Reading it after the survey, two things are
clear: the revision took R5 seriously and did most of the hard work it asked for, and the same
revision is the direct cause of about half the seams in my section 2.

### Addressed, and addressed well

**R5.1 (blocking), four tables and two appendices do not exist.** Fixed. Tables 2, 3, 4, 7 and 10
are all present, Appendix B and Appendix C are present, and Appendix C.2 prints the per-paper
disagreement text in full. This was the finding that made R5 "read the rest as assertions rather
than as a case", and it no longer applies: I read Section 3 with Table 2 in front of me.

**R5.3, the uncited nine-engine review.** Fixed, and better than asked. §1 now carries a full
paragraph — "It runs no benchmark of its own and says so in its Sec. V, that implementing the same
scenarios across nine engines 'goes beyond the scope of this paper'. Its running bodies are
ant-and-humanoid RL benchmarks rather than hands, and it discusses no timestep, no friction model,
no contact formulation and no penetration" — plus a Table 10 row. (R5 also asked for a second
citation "in Sec. 4.2 where the taxonomy is introduced". That did not happen; §4.2 introduces the
taxonomy from `contact_models_comparison_2023` with no back-reference.)

**R5.4, `bai_unified_manip_survey_2025` strawmanned by a parse artefact.** Fixed, and the fix went
further than R5's proposed wording: "Its Sec. 4.3 on dexterous manipulation runs about 720 words,
the third longest of its ten task subsections behind grasping and quadrupedal manipulation, which
is a real treatment and not a passing mention." R5's own measurement put it second, behind grasping
only, with mobile third at 667 words; the survey now says third, behind grasping and quadrupedal.
One of the two is wrong and I cannot tell which from the document. The direction is conservative,
so it is not a problem, but it is an unremarked disagreement with the review that produced the fix.

**R5.5, `zhao_dexhand_survey_2026`.** Fixed almost verbatim, and it is the single biggest
improvement in the document. The "uses the word penetration exactly once" framing is gone, replaced
by "That is the reference-versus-rollout split, named by a predecessor before this survey measured
it ... The contribution here is that measurement and the argument that a measure a policy optimises
cannot also judge it. The idea that contact quality belongs on the evaluation axis is Zhao's." A
survey that gives credit that precisely earns trust it can spend elsewhere.

**R5.6, the taxonomy presented as exhaustive.** Fixed, near-verbatim: "Those six families do not
cover the corpus. Twenty-four of the 112 method rows carry a label from outside them and eight
carry no label from the six at all ... Table 1's six rows are the families with enough papers to
compare, and not a partition of the corpus."

**R5.8, `helix_2025` and `groot_n16_2025` silently absent.** Fixed, including the specific
qualification R5 asked for: "The nearest thing to a counterexample is `helix_2025`, a Figure blog
post claiming a 35-DoF whole-upper-body action space at 200 Hz that includes individual finger
control. It never names the hand, gives no per-hand DoF count, and reports no success rate or trial
count for any task. It is the maker describing its own unreleased hand, which is the evidence class
the finding is about." Appendix A's rowless-entry list now reconciles: three of 221, named.

**R5.9, the analytic verdict on one chapter.** Fixed by softening, which was R5's second option:
"That verdict is one architect's, on one chapter, and this survey did not survey the tradition it
judges", plus "the planning line that took up the dynamic question directly, finger gaiting and
rolling-contact manipulation and regrasp planning, is not in the corpus at all."

**R5.10, Section 8 restates Sections 3 to 7.** Substantially fixed. §8 went from 1,906 words and
ten gaps to 1,099 words and seven, and the three R5 named as failing the generality test — reward
weights, announced hands, failure modes — are exactly the three that are gone. R5's promotion
suggestion for 8.1 was adopted as its opening sentence: "This is a result rather than a gap, and a
result about publishing practice in robot learning: the dexterous corpus is its sample, not its
subject." (R5 asked for ~600 words; 1,099 is closer than it was.)

**R5.11, §3.4 is a list.** Fixed. Roughly 1,000 words down to about 400, keeping the
three-evidence-classes paragraph and the implausibility cases, which is close to R5's prescription.

**R5.12, gap 8.6's denominator.** Fixed verbatim, and propagated to the conclusion: "19 appear in
no method row, but 14 are neither sold nor open and appear in none for that reason, so 33 is not
the denominator for a software-lag claim."

**R5.14, the recency skew.** Fixed: "This is a corpus of the learned era, which is a selection
effect and not a judgement. Of the 221 bibliography entries, 138 are dated 2024 or later and 16
predate 2018 ... Any statement here about a trend over time is a statement about 2022 onward." (The
year histogram R5 asked for in Appendix A is not there; the summary sentence is.)

**R5.19, the penetration breakdown summing to 94.** Fixed: §5.2.2 now reads "85 do not address
penetration at all, 5 constrain it, 3 measure it, 3 penalise it and 16 say nothing either way",
which sums to 112.

**R5.2, figures not embedded.** Half fixed. All six are embedded now, and the Figure 1 comment
block is gone. The Figure 4 comment block is not — see below.

### Not addressed

**R5.13, "A survey of 216 works" counts vendor pages as works.** Unaddressed. The subtitle now
reads "A survey of 218 works, with an evaluation frame and the gaps it exposes" — the same claim
with the count updated. R5's objection was that 218 is a row count including 33 hand rows that are
mostly vendor pages and press releases, and that "Leading with 216 buys a size impression the
corpus does not support, in a document whose whole argument is that numbers need their
denominators." That is still true, and it is now the first line of a document whose §7.1 spends
1,193 words on the proposition that a number without its denominator cannot be compared.

**R5.16, Table 9 is 84 empty cells plus 300 words explaining that it has no content.** Not
addressed and reversed. R5's fix was "Keep Sec. 7.6's two paragraphs, delete the table ... Or keep
the table and cut the prose to two sentences. Not both." The revision kept both and grew the prose
from about 300 words to 660, adding two paragraphs on corrections to the rule that selects which
twelve empty rows to print.

**R5.18, sections that open by announcing themselves.** Not addressed. All three sentences R5
quoted are still the opening sentences of their subsections: §4.2's "Table 4 is the
engine-by-engine comparison, one row per simulator, built only from what a note confirmed";
§6.4's "Table 7 carries the bimanual papers on the same columns as every other method here"; and
§7.6's rule description. §5.9 has since joined them.

**R5.15, Table 6's truncated cells.** The caption count was fixed (it now says 30 rows) and the
truncation was not. Worse, it spread — see below.

**R5.20, the RL count changing from 53 to 59.** Not addressed in the prose. §5.2.1 still opens
"Fifty-nine of the 112 method rows learn from a reward" with no statement that 59 is `RL` plus
`RL+demo`; the reader can only get it from Figure 4's leaf labels. R5 asked for four words.

**R5.21 and R5.22, the hand-list mismatch and the "Figure 03" / "Figure 3" collision.** Partly.
Proception and AgiBot moved to Table 2, which resolves half of R5.21; PaXini is still in the nine
and still discussed nowhere. The specific sentence R5 quoted is gone, but §3.4 still opens a
sentence with the product name — "Figure 03's 'Degrees of freedom, hands | 20' sits on the same
tracker page as 'Number of fingers | 10'" — in a document whose Figure 3 is the simulation-step
diagram.

### What the revision introduced that a reader trips over

This is the part R5 could not have anticipated, and it is the reason my verdict is what it is. Six
of the seams in my section 2 are fresh damage from this revision, not survivals from the draft R5
read.

**1. The reproducibility number was lowered in one place and not the other.** R5 reported the draft
as "16 hard contradictions with 15 at high confidence". The revision did the adversarial
re-reading, withdrew seven accusations, and arrived at ten — a genuinely admirable piece of work,
recorded in `mismatch_review` fields and in Appendix C.2. §5.8, §8.1 and §9 carry ten. §7.2 and
Table 8 still carry sixteen, and §7.2 states the old decomposition while attributing it, by name,
to the section that now contains the new one. A reader who reads §5.8 and §7.2 in either order
concludes the survey does not know its own headline number.

**2. `25` became `28` in Section 6 only.** R5.7's fix was adopted literally — §2.3 now opens
"Three counts describe two hands and they measure different things" and walks 53 / 43 / 25, exactly
as R5 asked. Then §6's denominator was re-derived to 28, with a careful and convincing exclusion
list, and §2.3 and §8.6 were not updated. So the paragraph written to fix R5.7 is now the source of
the same confusion R5.7 was about, and §8.6 cites "the twenty-five rows that Section 6.2 counts"
against a Section 6.2 that counts 28.

**3. The §7.1 null audit did not propagate backwards.** The audit is new and it is the most
intellectually honest passage in the document. It moved trial counts from 55 to 70 and unseen-object
counts from 32 to 39. §5.9's introduction to Table 7 still quotes 55 and 32, and Appendix A still
describes the audit at 32 rows and 13 recoveries against §7.1's 34 and 15.

**4. `asymdex_2024`'s baseline number was orphaned.** R5's summary of the old §8.8 quotes "0.0429
against 0.7701", so 0.0429 was the monolithic baseline in the draft R5 read. The revision rewrote
§6.2 around a different pair of ablations (0.1086 and 0.0164) and left §8.6's 0.0429 in place, now
with no antecedent anywhere in the document.

**5. Truncated table cells spread from one table to five.** R5.15 flagged Table 6 as unreadable
because its cells end in an ellipsis mid-word. The four tables generated since carry the same
defect: 52 truncated cells in Table 2, 32 in Table 3, 36 in Table 4, 53 in Table 7, 44 still in
Table 6 — 217 in all. This matters most in Table 4, where the truncated columns are `contact model`
and `solver`, which is precisely what §4.2 spends 2,000 words arguing about. Table 4's Brax cell
reads "no convex-decompos…" and its MuJoCo Warp solver cell ends "are…". The blocking finding R5
raised was that a third of the document argued from evidence the reader could not see; the tables
are now there and the cells the argument depends on are still cut off.

**6. Prose-rule compliance regressed in the new material.** R5 checked the brief's banned-word and
punctuation list and found the draft "substantially compliant", with "Em-dashes: two, both inside
one verbatim quotation." The document now has 21 in prose outside tables, 16 of them in the
survey's own new sentences, clustered in §7.1, §7.2, §7.3, §7.5, §7.6 and §8.1 — the sections the
revision rewrote. `paper/SECTION_BRIEF.md` says "No em-dashes, no parentheticals, no arrows, no
semicolons joining clauses."

**7. Length went the wrong way.** R5 proposed cutting about 2,550 words. Against R5's own
per-section prose counts, the document gained 4,658:

| section | R5 | now | target | vs target |
|---|---|---|---|---|
| 1 | 826 | 1,377 | 800 | +72% |
| 2 | 1,170 | 1,418 | 900 | +58% |
| 3 | 2,919 | 3,394 | 2,200 | +54% |
| 4 | 3,058 | 3,963 | 2,200 | +80% |
| 5 | 4,450 | 4,993 | 3,500 | +43% |
| 6 | 1,971 | 2,253 | 1,600 | +41% |
| 7 | 2,669 | 5,016 | 2,000 | +151% |
| 8 | 1,906 | 1,099 | 1,400 | −21% |
| 9 | 438 | 552 | 400 | +38% |

Section 8, the one section R5 asked to cut, is the only one that shrank and the only one now under
target. Section 7 nearly doubled. Much of that growth is good — the null audit, the McNemar
correction, the per-cell versus grand-total trial distinction — and all of it is the survey
answering criticism by adding qualification rather than by cutting. The result is that §7 is now as
long as §5 and contains an empty table defended at 660 words.

**8. The Figure 4 comment block survived and acquired a to-do list.** R5.2's fix was "Delete both
comment blocks; the drawing instructions belong in `paper/FIGURES.md`, where they already are." The
Figure 1 block went. The Figure 4 block stayed, grew a header reading "THE RULE, after the R3
review", and now ends with three numbered "STILL TO DO" items, the first of which is "THE
CROSS-LINKS ARE MISSING AND THEY ARE THE POINT." I verified that they still are:
`fig4_taxonomy.svg` has one `<path>` and no dashed strokes. A reader of the manuscript is told, in
the manuscript, that its taxonomy figure omits the thing the figure is for.

One more that R5 flagged as a strength and the revision complicated: R5 praised §6.2 for "9 of 12
monolithic, `asymdex_2024` the only ablation ... the dominant architecture tested once and beaten."
That is now 21 of 28 in §6.2 and 19 of 25 in §8.6, and the ablation's baseline changed. The
judgement is still right and still well made — "The concentration is not the outcome of a
comparison that was won" is as good a sentence as it was — but the arithmetic under it moved twice
and only half of the document moved with it.

---

## Verdict

**Not ready.** It is much closer than R5 found it, and the distance left is not intellectual.

The paper inside this document is real and I would fight for it at a venue. Somebody opened 62
repositories and read their reward functions against their papers, then attacked their own
accusations and withdrew seven of them on the record. Somebody read the Dojo table and the SAP
paper carefully enough to say "The depth is a setting" and mean it. Somebody found that the field's
own benchmark repository computes the exact quantity the field says nobody measures, and cited it
by line number. Somebody wrote §5.7's four sentences about reward engineering moving upstream into
data curation. Those four things are worth publishing and no predecessor in this corpus has any of
them.

What stops it is that the document does not currently satisfy its own standard. Its thesis is that
a number without a denominator cannot be compared and that a table in a paper is a claim about a
document rather than about a run. I found six counts that disagree with another part of the same
document — the bimanual denominator, the reproducibility contradiction count, the trial and
unseen-object counts, the code-release counts, the generalist hand counts, the Isaac Gym count —
and one table, Table 8, that states a number its own source section retracted. A reviewer who finds
that will not weigh it as a typo. They will weigh it against §9's opening sentence, "The binding
constraint on this field is not ideas. It is verification", and they will be right to.

### The three changes I would make before it went out

**1. One arithmetic pass, with `corpus/rows` as the arbiter, and a regression test after it.**
Every count in the body must agree with the rows and with every other statement of the same count.
The specific casualties, in priority order: §7.2 and Table 8's `16` against §5.8's `10`, which must
be fixed first because it is the survey's headline finding disagreeing with itself in the section
that proposes the cure; §2.3 and §8.6's `25` against §6's `28`, and §8.6's `19` against §6.2's
`21`; §5.9 and Appendix A against §7.1's post-audit `70` and `39`; §8.1 and §9's `61` released and
`fifty` releasing nothing against `62` and `46`; §5.5's `11` and `seven` against §8.4's `8` and
`five`; §3.2 and §3.3's LEAP `11` against `12`; §1's Isaac Gym `35` against §4.3 and Figure 1's
`36`; §8.6's orphaned `0.0429`; and Appendix C.2's four version-skew rows against the body's three.
The survey already has `tools/make_survey_table.py` checking table cells against note quotations.
The prose needs the same treatment: every bare integer in the body should be generated from the
rows or asserted against them, and the build should fail when two assertions of the same quantity
differ. Given what this survey is about, that tool is arguably part of the contribution.

**2. Put the findings at the front, and take the working notes out of the back.** Add an abstract
that states the four measured findings and the two claimed contributions in 200 words, with the
`physhoi_2023` case and the IsaacGymEnvs line numbers in it. Move Table 10 and the 700 words of
predecessor comparison out of §1 into a §1.1 or a short related-work section, so the first table a
reader meets is Table 1 and not Table 10. Delete the 678-word Figure 4 comment block, and either
draw the cross-links or delete the claim that they are the point. Reconcile the three different
answers the document gives to "which hand should I buy" (§3.1's seven, §3.6's three, §9's five),
since that is the one place a reader is asked to act. And fix the subtitle: R5 was right that "A
survey of 218 works" is the survey's own reporting failure on its own front page.

**3. Cut §7 back toward its target and make the tables readable.** Untruncate the 217 mid-word
cells, starting with Table 4's `contact model` and `solver` columns, which carry §4.2's argument,
and Table 2's `actuation` column, which carries §3.1's. Move Table 7 and Table 6 to appendices at
full width with two-word category columns in the body, as R5 proposed for Table 6 — Table 7 as it
stands is a 112-row database dump that no reader will use. Take §7.6 to two paragraphs and delete
Table 9, or keep Table 9 and cut §7.6 to two sentences, which is what R5 asked for and the revision
doubled instead. And run the brief's punctuation rules over §7 and §8.1, which is where all 16 of
the new em-dashes are.

Everything above is a day or two of work on a document that has already done the hard part.
