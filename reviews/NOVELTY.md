# Novelty review: has this been done before?

Reviewer brief: check the survey's three claimed contributions against prior work, in robotics and
outside it, and be willing to come back with "this has been done". Written 2026-09-18 from web
search plus the corpus already on disk (`papers/notes/`, `corpus/rows/`). Numbers taken from a
paper's own abstract or body are marked as such; numbers I could not confirm at the primary source
are marked **unverified** and must not be cited without checking.

The three claims under test, as `paper/sections/01_introduction.md` currently states them:

1. **Artifact-level reward audit.** Of 112 method rows, 62 released code that could be parsed
   against the paper; 38 record a discrepancy; 10 are contradictions where the shipped code states
   a different objective from the published one; 7 further accusations were withdrawn.
2. **Interpenetration census.** 11 of the 96 method rows whose notes settle it address
   interpenetration at all, 4 of the 11 inside a closed-loop policy, and none reports a penetration
   number for its own trained policy's rollouts.
3. **Reproducible corpus and recorded retractions.** Both results computed over a corpus that was
   assembled, fetched and parsed by scripts, with the withdrawn accusations kept beside the charge.

---

## 1. What has been done before, and by whom

### A. Audits of published reward functions across a body of work

**Knox, Allievi, Banzhaf, Schmitt, Stone, "Reward (Mis)design for Autonomous Driving", Artificial
Intelligence 316 (2023), arXiv:2104.13906.** The closest prior work to claim 1 by intent. They
review **19 publications** on RL for autonomous driving — "every publication on RL for autonomous
driving we found that had been published by the beginning of this survey process at a top-tier
conference or journal" — and exhaustively characterise the reward function of **10 focus papers**,
rewriting each in a standard form in an appendix, then apply **8 sanity checks** and report
"near-universal flaws in reward design for AD".

- How it differs: their ground truth for what the reward was is **the authors, not the repository**.
  The method says the characterisation was done "typically through detailed correspondence with the
  authors", and details so obtained are marked with a dagger in Appendix A. They also report that
  "Only 1 of the 10 focus papers thoroughly described the reward function, discount factor,
  termination conditions and time step duration used" — i.e. they establish **incompleteness** of
  published reward descriptions, not **contradiction** between a paper and its shipped code. Field
  is autonomous driving; scale is 19/10 against this survey's 112/62; the defect class is
  normative (would this reward produce safe behaviour?) rather than referential (does the code
  compute the reward the paper prints?).
- Consequence for this survey: it cannot claim to be the first audit of published reward functions.
  It can claim to be the first to take the repository as the arbiter.

**Gilbert, Dean, Lambert, Zick, Snoswell, "Reward Reports for Reinforcement Learning" (AIES 2023).**
A prospective documentation framework for reward design, in the spirit of model cards. Not a
retrospective audit; no counts of existing practice.

No paper was found that tabulates reward terms across dozens of manipulation or locomotion papers,
and no paper was found that counts contradictions between shipped and described rewards in robotics.

### B. "The code is not the paper" in reinforcement learning

**Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph, Madry, "Implementation Matters in Deep
Policy Gradients: A Case Study on PPO and TRPO" (ICLR 2020), arXiv:2005.12729.** Identifies
"code-level optimizations: algorithm augmentations found only in implementations or described as
auxiliary details to the core algorithm" and shows they are "responsible for most of PPO's gain in
cumulative reward over TRPO". The canonical precedent for the phenomenon this survey measures at
scale. Difference: **two algorithms, one reference codebase**, and the divergences are optimiser and
normalisation tricks, not the objective's own terms. (The count of nine such optimizations is
**unverified** at the primary source.)

**Huang et al., "The 37 Implementation Details of Proximal Policy Optimization" (ICLR Blog Track
2022).** Reconstructs one algorithm from one codebase's git history. Same shape, N = 1.

**McLean et al., "Meta-World+: An Improved, Standardized, RL Benchmark" (NeurIPS 2025),
arXiv:2505.11289.** The closest robotics-side precedent for "the shipped reward is not the
documented reward": Meta-World accumulated "numerous undocumented changes which inhibit a fair
comparison of algorithms", and the paper runs "an empirical comparison of various multi-task and
meta-RL algorithms across past reward functions, highlighting the inconsistencies in cross-version
comparisons" (the V1 reward reaches roughly 1200 at success, V2 reaches 10). Difference: it audits
**one benchmark codebase across its own versions**, not N papers each against its own text, and the
remedy is a new release rather than a census.

**Henderson et al., "Deep Reinforcement Learning that Matters" (AAAI 2018)**; **Islam, Henderson et
al. (ICML repro workshop 2017)**; **Andrychowicz et al., "What Matters in On-Policy RL?" (2020)**;
**Agarwal et al., "Deep RL at the Edge of the Statistical Precipice" (NeurIPS 2021)**; **Patterson
et al., "Empirical Design in RL" (JMLR 2024)**. Variance, seeds, statistics and experimental
method. None opens many papers' repositories to compare implementation against description.

### C. Paper-code consistency as its own research problem (2025-2026)

This is the literature that has moved closest to claim 1's *method*, and the survey must cite it.

**"SciCoQA: Quality Assurance for Scientific Paper--Code Alignment", arXiv:2601.12910 (2026).** A
benchmark of **635 paper-code discrepancies (92 real, 543 synthetic)** with a taxonomy of
discrepancy types, spanning AI, physics and quantitative biology; 22 models evaluated, the best
reaching **46.7 % accuracy on the real discrepancies**. The real discrepancies were **mined from
GitHub issues and reproducibility reports**, not found by the authors auditing a field. Framed as
an automated-QA benchmark, not a survey with a field-level contradiction rate. (Repository count of
204 and the authors' affiliation are **unverified**.)

**"Do Papers Tell the Whole Story? A Benchmark and Framework for Uncovering Hidden Implementation
Gaps in Bioinformatics", arXiv:2603.22018 (2026).** Introduces "paper-code consistency detection"
and **BioCon: 48 bioinformatics software projects and their associated publications**, aligned at
sentence-to-function granularity with **expert annotation**; reports that "some projects exhibit
high inconsistency ratios exceeding 40 %". **This is the nearest structural twin to claim 1: a
field-scoped, human-annotated audit of shipped code against paper prose.** It is in bioinformatics,
it targets method descriptions generally rather than one semantic object such as the reward, and its
purpose is to train and evaluate detectors.

**"Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results",
arXiv:2604.21965 (2026).** Agents reimplement the analyses of **48 social-science papers** "under
strict information isolation -- agents never see the original code, results, or paper", then a
deterministic cell-level comparison of reproduced outputs to the original results traces
divergences; failures "stem both from agent errors and from underspecification in the papers
themselves". N-papers scale, same spirit, different field,
and the comparison is agent-reimplementation versus published results rather than human reading of
the shipped reward.

**"Dude: Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection" (EMNLP 2026)** and
**"Enhancing Code Consistency in AI Research with LLMs and RAG", arXiv:2502.00611.** Detectors for
the same task. Details **unverified**.

### D. Field-level reproducibility censuses (precedent for the shape, not the object)

- **Collberg & Proebsting, "Repeatability in Computer Systems Research", CACM 59(3) 2016.** 601
  papers examined, 402 claiming code; roughly **32 % built within 30 minutes** and about **54 % at
  best**. Buildability only — no comparison of what the code computes against what the paper says.
  (Exact thresholds **partially unverified**; cite the threshold, not "most code didn't build".)
- **Raff, "A Step Toward Quantifying Independently Reproducible Machine Learning Research"
  (NeurIPS 2019)**, with the AAAI 2021 survival-analysis follow-up. **255 papers reimplemented from
  the text alone**, and deliberately *without* looking at the authors' code — the exact opposite
  design to this survey.
- **Gundersen & Kjensmo, "State of the Art: Reproducibility in Artificial Intelligence" (AAAI
  2018).** **400 IJCAI/AAAI papers** scored on documentation variables. A census of what papers
  *state*, not of what their code does.
- **Pineau et al., "Improving Reproducibility in Machine Learning Research" (JMLR 22, 2021).**
  Programme report and checklist; no artifact audit.
- **ML Reproducibility Challenge and ReScience C.** One paper per report, by volunteers; the journal
  had on the order of 200 published replications in total (**unverified**). Never a single study
  auditing dozens of repositories under one rubric.
- **Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-based Science", Patterns 4(9)
  2023.** Collates leakage reports across **17 fields**, implicating on the order of **300 papers**
  (sources give 294 and 329; **unverified**), with a civil-war-prediction case study that does open
  code. Literature-level census plus small-N code deep dive; the unit of defect is a leakage type.
- **Heumüller et al., "Publish or Perish, but Do Not Forget Your Software Artifacts", EMSE 25(6)
  2020.** **789 ICSE papers**; artifact availability and its citation correlation, not fidelity.
- **"An Audit of Machine Learning Experiments on Software Defect Prediction", arXiv:2601.18477 /
  EMSE 2026.** **101 papers** sampled from about 1,585, **427 issues**, median 4 per paper, only one
  paper with none. A field audit at comparable scale, conducted **by reading the papers**.
- **Fair-comparison re-measurement genre:** Blalock et al., "What is the State of Neural Network
  Pruning?" (MLSys 2020), **81 papers** plus their own ShrinkBench runs; Ferrari Dacrema et al.
  (RecSys 2019), **18 papers, 7 reproducible**, most beaten by tuned heuristics; Musgrave et al.,
  "A Metric Learning Reality Check" (ECCV 2020); Lucic et al., "Are GANs Created Equal?" (NeurIPS
  2018), 7 variants under one budget; Errica et al., "A Fair Comparison of Graph Neural Networks for
  Graph Classification" (ICLR 2020), "re-evaluate five popular models across nine common
  benchmarks". All of these re-run the field under one protocol; none makes the paper-versus-code
  diff its object.
- **Code-defect censuses in the natural sciences:** Ziemann et al., "Gene name errors are widespread
  in the scientific literature" (Genome Biology 2016) and its 2021 rescan finding no improvement —
  a defect census over published supplementary artifacts, not a paper-versus-code comparison; and
  the `glob.glob` ordering bug in the Willoughby-Hoye NMR scripts, reported in Organic Letters
  (2019) as potentially affecting more than 100 papers. Both are precedents for "opening the
  artifacts of a literature finds errors the papers do not mention".
- **"Auditing widely used biomolecular benchmarks reveals systematic data inconsistencies"** (PMC,
  2026): 51 benchmark configurations audited for data defects. Benchmark data, not code.

### E. The fourteen in-corpus surveys and the seven eval-protocol works

Evidence already on disk, from `papers/notes/`:

- `an_dexil_survey_2025`, `bai_unified_manip_survey_2025`, `zhao_dexhand_survey_2026`,
  `welte_iil_survey_2025`: **none opens code.** Their notes record `no code` except
  `bai_unified_manip_survey_2025`, whose code artifact is an awesome-list README with "Config files
  (0)" and "reward/observation bodies (0 files)". On penetration: `welte` has 0 occurrences of
  "penetrat"; `an_dexil` 0; `bai` 1, in an unrelated contact-map context; `zhao_dexhand` 1, a single
  sentence listing penetration among physical-plausibility criteria with no threshold or method, and
  its note records "seed" 0, "variance" 0, "confidence" 0.
- Off-corpus check: **Weinberg, Shirizly, Azulay, Sintov, "Survey of learning-based approaches for
  robotic in-hand manipulation" (Frontiers in Robotics and AI, 2024)**, roughly 50 papers tabulated,
  does not tabulate reward functions, does not inspect released code, and does not tabulate
  penetration. It is not in `corpus/bib.json` and is a gap worth closing for the related-work
  section.
- `nine_physics_engines_review_2024` is explicitly a literature-and-documentation review that runs
  no simulation; `physics_engine_comparison_2015` measures five engines and
  `contact_models_comparison_2023` four contact formulations. These audit **engines**, not the
  field's code, and the survey already says so.
- `kress_gazit_policy_eval_2024`, `lbm_careful_examination_2025`, `beyond_binary_success_2026`,
  `simpler_2024`, `autoeval_2025`, `roboarena_2025`, `suresim_2025`: evaluation-protocol rigour,
  statistics and sim-real agreement. None reads another paper's source.

Conclusion for this group: the survey's positioning against the fourteen is supported by the notes
on disk, and no in-corpus survey does either audit.

### F. Interpenetration across a body of work — the counterweight the survey must handle

This is where the claim is most exposed, and search does not support the bare sentence
"interpenetration is measured by almost nobody".

In **dexterous grasp synthesis and hand-object reconstruction, penetration is a standard
cross-method table column** and has been since roughly 2019:

- Maximum penetration depth, intersection/penetration volume (voxelised, commonly 0.5 cm voxels) and
  penetration percentage are routine metrics traceable to the ObMan-era hand-object reconstruction
  work and reported comparatively across methods on ObMan, DexYCB and HO-3D.
- **DexGraspNet** reports maximal penetration depth and a non-penetration ratio under a 5 mm
  threshold; several works gate grasp success on penetration below 0.5 cm or 0.1 cm.
- **DexGraspBench**, released with BODex (ICRA 2025), is "a standard and unified simulation benchmark
  in MuJoCo for dexterous grasping" whose metrics include penetration depth and which **re-runs
  prior baselines** (DexGraspNet, FRoGGeR, SpringGrasp) under one protocol — a cross-method
  penetration comparison, though of synthesised grasps rather than policy rollouts.
- In this corpus, `bidexgrasp_2026` reports Penetration Depth and Self-Penetration Depth in
  centimetres for itself and for a prior method, which its note uses to compare 1.52 cm against
  0.15-0.20 cm.

What search did **not** find is any prior census of *who measures it*, and nothing that separates
per-sample grasp evaluation from closed-loop policy rollouts. The corpus's own rows support the
narrow version of the claim: of the 11 method rows that address penetration
(`bidexgrasp_2026`, `bimangrasp_2024`, `castro_sap_contact_2021`, `clutterdexgrasp_2025`,
`deximit_2026`, `dexmachina_2025`, `dextrack_2025`, `pang_global_planning_2022`, `teledexter_2026`,
`toporetarget_2026`, `unidexgrasp_2023`), the sharpest case is `dextrack_2025`, whose note records
that penetration is measured "only as a property of the INPUT kinematic reference ... not as a
property of the policy's own rollouts", via Eq. 24's mean `PeneDepth` over reference frames. That is
the distinction the claim rests on, and it must be in the sentence itself.

---

## 2. What appears genuinely new here

1. **Taking the repository, rather than the paper or the authors, as the arbiter of what was
   trained, across a two-digit corpus in robotics.** Knox et al. audited 19 reward functions by
   asking the authors; Engstrom et al. and Meta-World+ established that shipped code diverges from
   documented algorithms, each on a single codebase; BioCon did the field-scoped paper-code audit,
   in bioinformatics, on method text in general. No work was found that opens N released robotics
   repositories, reads the shipped reward body and task config, and compares them with the paper's
   own reward table. As far as this search establishes, contribution 1 is new **in robotics**, and
   new **in its object** (the objective function specifically) anywhere.
2. **The defect class.** "The paper's reward table lists a nonzero weight for a term the released
   `compute_*_reward` hardcodes to zero, with the real computation commented out beside it"
   (`physhoi_2023`) is a stronger and more checkable charge than the field's existing vocabulary of
   "undocumented implementation detail", "not reproducible" or "incompletely described". The
   10-of-62 contradiction count, separated from the 38 disagreements, has no precedent found.
3. **The interpenetration census, scoped to closed-loop policies.** No prior census of penetration
   *measurement practice* was found in any literature searched, and the specific observation that a
   paper can measure penetration of its input reference while never reporting it for its own
   rollouts (`dextrack_2025`) appears to be original. The paired observation that the tooling is not
   the obstacle — IsaacGymEnvs computing per-environment maximum interpenetration depth in Warp and
   gating on 1 mm — was not found elsewhere either.
4. **Recording the withdrawn accusations inside the artifact.** Reproducibility reports in ReScience
   and the ML Reproducibility Challenge publish author responses, and Ziemann's 2021 rescan revisits
   its own earlier claims, but no survey was found that keeps its retracted charges beside the
   surviving ones in the released corpus. This is a practice worth stating plainly; it is not a
   scientific first and should not be sold as one.
5. **Weaker but real:** Table 4's engine columns (contact model, solver, iteration count, default
   timestep, penetration exposure) conditioned on what a hand does to a solver, as an addition to
   `nine_physics_engines_review_2024`'s documentation-and-usability axes.
   `physics_engine_comparison_2015` and `contact_models_comparison_2023` already measure engines, so
   the novelty is the conditioning and the field context, not the act of comparing engines.

---

## 3. What to claim in the introduction, and how to word it

**Say "in dexterous manipulation", or "in robotics", every time.** The unqualified forms — "the
first artifact-level audit of a research field", "the first audit of a field's released code" — are
false: Collberg & Proebsting 2016 (601 papers), BioCon 2026 (48 projects), SciCoQA 2026 (92 real
discrepancies) and the SDP audit (101 papers) all precede it. The defensible form is:

> the first audit we are aware of that reads a field's released reward implementations against the
> rewards its papers describe

with "field" instantiated as dexterous manipulation and "we are aware of" kept in.

**Prefer "we found no prior X" to "no X exists", and "first we are aware of" to "first".** The
corpus is 221 entries; the field is larger. Every "first" in the introduction should be checkable
against the corpus, not against the literature as a whole.

**Cite the precedents in the same paragraph as the claim.** Specifically:
- Engstrom et al. 2020 and McLean et al. 2025, for the prior finding that shipped code diverges from
  the documented algorithm and that this changes conclusions. Not citing Engstrom in a paper whose
  first contribution is a code-versus-paper audit will read as unfamiliarity with the RL literature.
- Knox et al. 2023, for the prior audit of published reward functions, and for the sharper framing
  it enables: they showed reward descriptions are *incomplete* (1 of 10 focus papers complete) and
  had to ask the authors; this survey shows that where code exists it sometimes *contradicts* the
  description, and needs no correspondence to show it.
- SciCoQA 2026 and BioCon 2026, for paper-code consistency as an established task. The right
  sentence is that this survey supplies for one robotics subfield what those supply as benchmarks:
  a human-read, field-scoped tally on one semantic object.
- Raff 2019, as the deliberate opposite design (reimplement from text, never look at the code),
  which makes the choice of ground truth an explicit methodological position rather than an
  accident.

**Scope the penetration claim three ways, in the sentence.** (a) closed-loop policy rollouts, (b)
this corpus and the rows whose notes settle the question, (c) "we found none" rather than "none
does". Then **concede the grasp-synthesis and reconstruction literature explicitly** — penetration
depth, intersection volume and non-penetration ratios are standard comparative columns there, and
DexGraspBench re-runs baselines on them. A reviewer who works on grasp synthesis will otherwise
reject the sentence "interpenetration is measured by almost nobody" from their own Table 1. The
README's version of this sentence is currently the weakest wording in the repository and should be
brought into line with the introduction's, which already says "11 of the 96 method rows whose notes
settle the question".

**State the audit's own exposure next to the count.** The ground truth is a repository at a fetched
commit, which may postdate, precede or diverge from the code that produced the paper's numbers;
`hora_2022`'s own README says as much. This is the most likely reviewer counterattack on all 10
contradictions, and the count should be quoted with the commit hashes in `corpus/code_manifest.json`
and one sentence admitting that a repository is evidence about a repository. The seven withdrawn
accusations belong in the same paragraph, not only in section 5.8, because they are the strongest
available evidence that the remaining ten were checked rather than counted.

**Do not call the corpus exhaustive or the rates rates.** `METHOD.md` and the README already have
the right language ("a floor rather than a rate"); the introduction should carry it too, since the
audit's denominators (62 of 112, 96 of 112) are properties of what could be parsed.

**One claim to drop or soften:** "papers disagree with their own released code" as a general
statement about the field. What was measured is that **38 of 62 parseable repositories disagree with
their paper in some respect and 10 contradict it about the objective**. The general form invites the
reader to hear "most of the field is wrong", which the numbers do not support and which the seven
withdrawals actively caution against.

---

## Verdict

Not done, with qualifications. The *method* — opening released code and comparing it with the
paper's method description — is an established and currently active research task (SciCoQA and
BioCon, both 2026), and the *phenomenon* in reinforcement learning is a known result (Engstrom et
al. 2020; Meta-World+ 2025). The *audit of published reward functions across a body of work* has
been done once, by Knox et al. (2023), on 19 autonomous-driving papers, using author correspondence
rather than code. What has not been done, as far as this search can establish, is the combination
this survey claims: a human-read, field-scoped audit in dexterous manipulation that treats the
shipped reward as the ground truth for what was trained, reports a contradiction count with the
retracted charges beside it, and pairs it with a census of a physical-plausibility measurement
practice — the interpenetration half of which has no precedent found anywhere. The overclaiming
risks are two: an unqualified "first artifact-level audit of a field", which is false; and
"interpenetration is measured by almost nobody", which is false in grasp synthesis and
reconstruction and true only of closed-loop policy rollouts.
