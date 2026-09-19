"""Generate Table 10, the survey-comparison table, from the survey-class rows and their notes.

Table 10 is the survey's positioning. Every cell therefore has to be a statement a reader can
check against the predecessor itself, not a characterisation written to make room for this
survey. Two rules follow, and both are enforced by the code below.

First, a cell is filled only from `papers/notes/<key>.md`. The cell text is written here, short
enough to fit a table, but each cell carries an `anchor`: a substring that must occur in that
note. If the anchor is gone, the note has changed and the cell is no longer supported, so the
script prints the cell as empty and reports it rather than printing an unsupported claim. Run
the script after editing a note and the table tells you which of its sentences stopped being
true.

Second, a predecessor whose source could not be obtained gets a row that says so in every
column. Those rows are the honest half of the positioning: this survey cannot claim to have
read four of the fourteen works in its own survey class.

Row identity, year and class come from `corpus/rows/*.json`. The bibliography supplies
nothing here, because a `why` field in `corpus/bib.json` is this survey's opinion of a work rather than
a reading of it.

The LaTeX edition sets the same comparison as a matrix instead of as prose, with one of three
coverage levels per cell. `LEVELS` below holds those levels and `level()` prints one only while the
prose cell it coarsens still has its quotation, so the glyph in the matrix and the sentence in the
appendix cannot disagree.

Usage: python3 tools/make_survey_table.py
Writes: paper/tables/table10_surveys.md
"""
import glob
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
EM = " "
UNOBTAINED = "source not obtained"
# A source can be on disk and still unread. `ma_dollar_dexterity_2011` is the case: the fetch
# that failed when its note was written succeeded later, and the manifest records the PDF, but
# no note has been read from it. That row says so rather than claiming either that the work was
# unobtainable or that this survey knows what is in it.
UNREAD = "PDF fetched %s after the note was written, no note read from it"

# Per survey, per column: (cell text, anchor that must be present in papers/notes/<key>.md).
# The anchor is quoted from the note, so a cell and its evidence move together.
SPEC = {
    "zhao_dexhand_survey_2026": {
        "scope": ("dexterous hands end to end: hardware anatomy, methods, datasets, directions",
                  "organises dexterous-hand research into four aspects"),
        "taxonomy": ("five task categories, each split by learning paradigm. Hardware is split by "
                     "actuation, transmission and perception",
                     "five task categories, each split by method paradigm"),
        "bimanual": ("one subsection, III-F, 16 cited works, no coordination analysis",
                     "one 1.5-page sub-section (III-F) of 16 cited works"),
        "hardware": ("Table I, 29 hands, 12 columns, secondary values",
                     "lists 29 hands"),
        "evaluation": ("names two layers: physical plausibility including penetration before "
                       "execution, success during it. No threshold, method or count",
                       "no penetration threshold or measurement method is given"),
        "gaps": ("hardware feasibility, perception fusion, learning beyond benchmark-centric "
                 "optimisation, industrialisation, absent evaluation standards",
                 "the absence of unified performance evaluation standards"),
    },
    "isaac_sim_2026": {
        "scope": ("one simulator's ecosystem and application domains, reviewed rather than measured",
                  "A survey positioning NVIDIA Isaac Sim"),
        "taxonomy": ("qualitative capability matrix, Table 1, over simulators",
                     "Table 1 is a qualitative capability matrix"),
        "bimanual": ("one cited GR00T task called bimanual, no hand, DoF or number",
                     "bimanual humanoid actions"),
        "hardware": ("no hand named anywhere in paper or code parse",
                     "no hand model, DoF count, or vendor is given"),
        "evaluation": ("none. The paper runs no experiment of its own",
                       "this paper reports no experiments of its own"),
        "gaps": ("computational cost, configuration complexity, learning curve",
                 "the high computational cost and steep learning curve remain practical obstacles"),
    },
    "an_dexil_survey_2025": {
        "scope": ("imitation learning for multi-fingered end-effectors",
                  "IL for multi-fingered end-effectors organised by IL family"),
        "taxonomy": ("IL family by end-effector class by demonstration source. RL gets none",
                     "no RL taxonomy, no reward design"),
        "bimanual": ("one subsection, II.E, framed as multi-agent",
                     'one subsection (II.E) framed as "multi-agent"'),
        "hardware": ("hands named in prose, no hand table",
                     "no hand table"),
        "evaluation": ("no metric defined and no trial count. Calls for protocols, proposes none",
                       "VI.B calls for protocols but proposes none"),
        "gaps": ("contact dynamics in engines, data-collection standards, cross-hand transfer, "
                 "failure datasets, end-effector morphology",
                 "physics engines struggle to model contact dynamics"),
    },
    "welte_iil_survey_2025": {
        "scope": ("interactive imitation learning, seven dexterous works found",
                  "finds only seven IIL-related dexterous works"),
        "taxonomy": ("IIL feedback type, plus a keyword bibliometric of 326 papers",
                     'keyword bibliometric of 326 "dexterous manipulation" papers'),
        "bimanual": ("three mentions in 687 lines, no section",
                     'three "bimanual" mentions in 687 lines'),
        "hardware": ("Table 1, 15 commercial hands, manufacturer figures",
                     "lists 15 commercial hands"),
        "evaluation": ("no metric defined, no benchmark table",
                       "no metric definitions, no benchmark table"),
        "gaps": ("tactile feedback, long-horizon tasks, generalisation, human-feedback interface",
                 "the limited use of tactile feedback and generalization in unstructured environments"),
    },
    "bai_unified_manip_survey_2025": {
        "scope": ("all of robot manipulation. Dexterous manipulation is one of ten task "
                  "subsections, about 720 words, and Sec. 1.2 defers it to other surveys",
                  "Sec. 1.2 defers to An et al."),
        "taxonomy": ("high-level planning, action modelling, actuation control, plus a "
                     "bottleneck taxonomy of data and generalisation",
                     "the first dedicated taxonomy of key bottlenecks"),
        "bimanual": ("bimanual means two arms. One dual-hand mention in the paper",
                     "Dexora is the only dual-hand mention"),
        "hardware": ("hands named, no DoF or actuation table",
                     "no DoF / actuation / tactile table"),
        "evaluation": ("success rate and checkpoint selection, six lines. Never says how success "
                       "is judged for a dexterous task",
                       "Sec. 2.4 is six lines; no trial counts, seeds"),
        "gaps": ("no scaling law, sim-to-real for contact-rich tasks, fragmented datasets, "
                 "reliability as important as success",
                 "the gap between simulated and real interaction remains particularly severe for "
                 "contact-rich manipulation"),
    },
    "nine_physics_engines_review_2024": {
        "scope": ("nine physics engines for RL research, scored on documentation and usability",
                  "nine engines (Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity, Webots)"),
        "taxonomy": ("13-axis feature and usability matrix, Table II, plus citation-count popularity",
                     '"Feature and Usability Comparison,"'),
        "bimanual": ("none. MARL readiness is the multi-agent axis",
                     "capabilities for multi-agent reinforcement learning"),
        "hardware": ("none. Ant and humanoid RL bodies are the running examples",
                     "not dexterous hands"),
        "evaluation": ("no benchmark of its own. Throughput claims are second-hand",
                       "This goes beyond the scope of this paper"),
        "gaps": ("no cross-engine MARL performance comparison exists in the literature",
                 "a research gap"),
    },
    "contact_models_comparison_2023": {
        "scope": ("LCP, CCP, RaiSim and NCP contact models re-implemented in one framework and ranked",
                  "re-implementing LCP, CCP, RaiSim, and NCP contact formulations"),
        "taxonomy": ("contact model by solver, with the physical property each one violates",
                     "PGS, ADMM, Newton, staggered projections, per-contact bisection"),
        "bimanual": ("none", "Solo-12 quadruped"),
        "hardware": ("one Allegro hand as a benchmark system, a ball dropped into it",
                     "Allegro hand (16-dof), used as one of three benchmark systems"),
        "evaluation": ("NCP criterion, self-consistency against a 1e-5 s reference, iteration cost",
                       "integral consistency error"),
        "gaps": ("no fully satisfactory contact model, and gradients through simulation "
                 "artifacts are unexplored",
                 "there is no fully satisfactory approach at the moment"),
    },
    "physics_engine_comparison_2015": {
        "scope": ("five engines on one shared model: speed, self-consistency, conservation, grasp "
                  "stability",
                  "comparing MuJoCo, Bullet, ODE, PhysX and Havok"),
        "taxonomy": ("none. Four test systems, one comparison per test",
                     "each engine performs best on the type of system it was designed"),
        "bimanual": ("none", "single/bimanual: single"),
        "hardware": ("one 35-DoF rig modelled on the Shadow Hand",
                     "modeled after the Shadow Hand robot"),
        "evaluation": ("largest timestep that holds a grasp, and a speed-accuracy Pareto curve",
                       "the largest timestep h for which the object remains in the hand"),
        "gaps": ("restricted feature subset by design, and the authors are MuJoCo's developers",
                 "we are the developers of the MuJoCo engine"),
    },
    "zhao_sim2real_survey_2020": {
        "scope": ("sim-to-real transfer in deep RL, eight pages, 21 works tabulated",
                  "sorts sim-to-real methods for deep RL"),
        "taxonomy": ("zero-shot, system identification, domain randomisation, domain adaptation, "
                     "learning with disturbances, simulator choice",
                     "zero-shot transfer, system identification, domain randomization, domain "
                     "adaptation, learning with disturbances"),
        "bimanual": ("none, zero occurrences", 'Bimanual: 0 occurrences of "bimanual"'),
        "hardware": ("two cited hand works, no hand table",
                     "no per-hand discussion, no hand table"),
        "evaluation": ("no metric defined, no trial count, no success rate",
                       "no metric definitions, no trial counts"),
        "gaps": ("domain randomisation has no formal account, and domain adaptation assumes "
                 "matched feature spaces",
                 "it is hard to explain formally how and why it works"),
    },
    "firoozi_foundation_models_2023": {
        "scope": ("foundation models in robot decision-making, perception and embodied AI",
                  "survey of LLMs / VLMs / generative models in robot decision-making"),
        "taxonomy": ("background, robotics, and robotics-adjacent papers, then by application",
                     '"Background Papers", "Robotics Papers"'),
        "bimanual": ("none, zero occurrences", 'Bimanual: absent (0 occurrences)'),
        "hardware": ("none. Parallel-jaw end effectors throughout",
                     "Parallel-gripper world throughout"),
        "evaluation": ("none defined. Benchmarking appears as a reproducibility problem",
                       "benchmarking appears only as a reproducibility problem"),
        "gaps": ("data scarcity, variability, uncertainty, safety, real-time inference, and "
                 "simulators that neglect contact physics",
                 "greatly simplifying contact physics"),
    },
    # Four survey-class entries whose sources were never obtained. Their rows say so in every
    # column, because this survey has read nothing of them beyond a title and a DOI.
    "okamura_overview_2000": {},
    "ma_dollar_dexterity_2011": {},
    "piazza_century_2019": {},
    "roa_suarez_grasp_quality_2015": {},
}

COLS = ["scope", "taxonomy", "bimanual", "hardware", "evaluation", "gaps"]
HEADERS = ["survey", "yr", "scope", "taxonomy used", "bimanual covered", "hardware covered",
           "evaluation covered", "gaps it names"]

# --- the three-level coverage encoding ------------------------------------------------------------
# The LaTeX edition sets this comparison as a matrix near the front of the paper, where a reader
# meets it, and a matrix cannot hold the prose cells above: fourteen rows of clauses is the page of
# text that used to sit in an appendix. So each prose cell is coarsened to one of three levels, and
# the level is printed as a tick, a circle or a cross. What the three mean, and the rule that
# decides between them:
#
#   full  the work gives the topic a structure of its own: a section, a table of its own, or a
#         measurement it defines.
#   part  the topic is there without such a structure: a subsection with no analysis, a handful of
#         mentions, a metric named but never defined, or a scope that contains the topic as one
#         item among many.
#   none  the topic is absent, or the work puts it outside its scope.
#
# A level is a coarsening of the prose cell in SPEC above it and of nothing else, so it carries that
# cell's anchor rather than an anchor of its own: `level()` returns None, and the table prints an
# empty cell, exactly when the quotation behind the prose cell has gone from the note. Appendix D
# and `paper/tables/table10_surveys.md` keep the prose, which is what a reader checks a glyph
# against. `level_problems()` refuses a level for a cell that has no prose cell, and a prose cell
# with no level, so the two cannot come apart.
FULL, PART, NONE = "full", "part", "none"
LEVELS = {
    "zhao_dexhand_survey_2026": {
        # Hardware anatomy, a task-by-paradigm taxonomy and a 29-hand table; III-F is one
        # subsection on bimanual with no coordination analysis, and IV-C names penetration as a
        # criterion without a threshold, a method or a count.
        "scope": FULL, "taxonomy": FULL, "bimanual": PART, "hardware": FULL,
        "evaluation": PART, "gaps": FULL,
    },
    "bai_unified_manip_survey_2025": {
        # All of manipulation: dexterous work is one of ten task subsections and Sec. 1.2 defers
        # it; bimanual means two arms; hands are named but not tabulated; Sec. 2.4 names success
        # rate in six lines without saying how success is judged.
        "scope": PART, "taxonomy": FULL, "bimanual": PART, "hardware": PART,
        "evaluation": PART, "gaps": FULL,
    },
    "an_dexil_survey_2025": {
        # Imitation learning for multi-fingered hands, so the scope is the subject; the taxonomy
        # covers IL only and RL gets none; II.E is one bimanual subsection; hands are named in
        # prose; VI.B calls for protocols and proposes none.
        "scope": FULL, "taxonomy": PART, "bimanual": PART, "hardware": PART,
        "evaluation": PART, "gaps": FULL,
    },
    "welte_iil_survey_2025": {
        # Interactive imitation learning, inside which seven dexterous works were found; a full
        # taxonomy of its own feedback types and a 15-hand table; three bimanual mentions in 687
        # lines and no section; no metric definitions and no benchmark table at all.
        "scope": PART, "taxonomy": FULL, "bimanual": PART, "hardware": FULL,
        "evaluation": NONE, "gaps": FULL,
    },
    "firoozi_foundation_models_2023": {
        # Foundation models in decision-making: zero occurrences of bimanual, a parallel-gripper
        # world throughout, and benchmarking present only as a reproducibility problem.
        "scope": NONE, "taxonomy": PART, "bimanual": NONE, "hardware": NONE,
        "evaluation": PART, "gaps": FULL,
    },
    "zhao_sim2real_survey_2020": {
        # A full taxonomy of sim-to-real transfer, which is its subject rather than dexterous
        # manipulation; zero occurrences of bimanual; two cited hand works and no hand table; no
        # metric, trial count or success rate anywhere.
        "scope": NONE, "taxonomy": FULL, "bimanual": NONE, "hardware": PART,
        "evaluation": NONE, "gaps": FULL,
    },
    "isaac_sim_2026": {
        # One simulator's ecosystem, reviewed rather than measured: a capability matrix over
        # simulators rather than over methods, one cited task called bimanual with no number, no
        # hand named anywhere, and no experiment of its own.
        "scope": NONE, "taxonomy": PART, "bimanual": PART, "hardware": NONE,
        "evaluation": NONE, "gaps": FULL,
    },
    "nine_physics_engines_review_2024": {
        # Nine engines on a 13-axis feature and usability matrix, which is a taxonomy of its
        # subject; multi-agent readiness is the nearest thing to bimanual; ant and humanoid bodies
        # rather than hands; it scores documentation and runs no benchmark of its own.
        "scope": NONE, "taxonomy": FULL, "bimanual": NONE, "hardware": NONE,
        "evaluation": PART, "gaps": FULL,
    },
    "contact_models_comparison_2023": {
        # Contact model by solver, with the property each violates; no bimanual anything; one
        # Allegro hand as one of three benchmark systems; and an evaluation it defines, the NCP
        # criterion against a 1e-5 s reference.
        "scope": NONE, "taxonomy": FULL, "bimanual": NONE, "hardware": PART,
        "evaluation": FULL, "gaps": FULL,
    },
    "physics_engine_comparison_2015": {
        # Five engines on one shared model, with no taxonomy at all: four test systems, one
        # comparison each. One 35-DoF rig modelled on the Shadow Hand, and a defined measurement:
        # the largest timestep that holds a grasp.
        "scope": NONE, "taxonomy": NONE, "bimanual": NONE, "hardware": PART,
        "evaluation": FULL, "gaps": FULL,
    },
}

# --- how the rows group -------------------------------------------------------------------------
# The rows are a taxonomy of three kinds, and the kind is read off the corpus rather than asserted
# here. A survey that entered the corpus through `corpus/bib_sim.json` is a simulator or
# contact-model study; one with no readable source is its own group, because the anchor rule is
# what puts it there; everything else is a survey of the field.
SIM_BIB = "corpus/bib_sim.json"
GROUPS = [
    ("field", "Surveys of the field"),
    ("engine", "Simulator and contact-model studies"),
    ("unread", "Sources not obtained, or on disk and never read"),
]


def sim_bib_keys():
    """The keys this corpus first collected as simulator literature."""
    d = json.loads((R / SIM_BIB).read_text())
    return set(d) if isinstance(d, dict) else {e.get("key") for e in d}


def group_of(key, readable):
    if not readable:
        return "unread"
    return "engine" if key in sim_bib_keys() else "field"


def level(key, col, note):
    """The coverage level for one cell, or None where the prose cell it coarsens is unsupported."""
    spec = SPEC.get(key, {})
    if col not in spec:
        return None
    _, anchor = spec[col]
    if anchor not in note:
        return None
    return LEVELS[key][col]


def level_problems():
    """A level with no prose cell, a prose cell with no level, or a level outside the vocabulary."""
    out = []
    for key, spec in SPEC.items():
        lv = LEVELS.get(key, {})
        if spec and not lv:
            out.append(f"{key}: has prose cells and no coverage levels")
        if lv and not spec:
            out.append(f"{key}: has coverage levels and no prose cells")
        for col in spec:
            if col not in lv:
                out.append(f"{key}.{col}: prose cell with no coverage level")
        for col, val in lv.items():
            if col not in spec:
                out.append(f"{key}.{col}: coverage level with no prose cell to coarsen")
            if val not in (FULL, PART, NONE):
                out.append(f"{key}.{col}: {val!r} is not one of full, part, none")
    return out


def load_rows():
    rows = {}
    for f in glob.glob(str(R / "corpus/rows/*.json")):
        r = json.load(open(f))
        if r.get("class") == "survey":
            rows[r["key"]] = r
    return rows


def note_text(key):
    p = R / f"papers/notes/{key}.md"
    return p.read_text() if p.exists() else ""


def fetched_but_unread(key, note):
    """Date the manifest records a parsed PDF for an entry whose note reports no source."""
    if "SOURCE THIN" not in note:
        return None
    man = json.loads((R / "corpus/manifest.json").read_text()).get(key) or {}
    if man.get("sha256") and (man.get("md_chars") or 0) > 1000:
        return man.get("fetched") or "later"
    return None


def main():
    rows = load_rows()
    missing_spec = sorted(set(rows) - set(SPEC))
    stale_spec = sorted(set(SPEC) - set(rows))
    out, unsupported, unobtained, unread = [], [], [], []

    out.append("### Table 10. Existing surveys and what each covers")
    out.append("")
    out.append("| " + " | ".join(HEADERS) + " |")
    out.append("|" + "|".join(["---"] * len(HEADERS)) + "|")

    for key in sorted(rows, key=lambda k: (-(rows[k].get("year") or 0), k)):
        note = note_text(key)
        spec = SPEC.get(key, {})
        if not spec:
            # An entry with no readable source. Say it once per column rather than leave blanks,
            # so the row cannot be mistaken for a survey that covers nothing.
            if "SOURCE THIN" not in note:
                unsupported.append(f"{key}: has no spec and its note is not marked SOURCE THIN")
            when = fetched_but_unread(key, note)
            if when:
                unread.append(key)
                cells = [f"*{UNREAD % when}*"] * len(COLS)
            else:
                unobtained.append(key)
                cells = [f"*{UNOBTAINED}*"] * len(COLS)
        else:
            cells = []
            for col in COLS:
                text, anchor = spec[col]
                if anchor in note:
                    cells.append(text)
                else:
                    unsupported.append(f"{key}.{col}: anchor not found in note: {anchor!r}")
                    cells.append(EM)
        out.append("| `%s` | %s | %s |" % (key, rows[key].get("year") or EM, " | ".join(cells)))

    n_unob = len(unobtained)
    tail = (f", and {len(unread)} of which was fetched too late to be read into a note"
            if unread else "")
    out.append("")
    out.append(
        f"*{len(rows)} rows, one per corpus entry of class `survey`, {n_unob} of which could not "
        f"be obtained and are entered as such{tail}. Every filled cell is read from "
        f"`papers/notes/<key>.md` and is checked against a quotation from that note by "
        f"`tools/make_survey_table.py`. A cell whose evidence has gone from the note prints "
        f"empty rather than printing an unchecked claim. The columns record what each work "
        f"covers, not how well, and a blank cell in `bimanual covered` or `hardware covered` is "
        f"a scope decision by its authors rather than a failure.*")

    (R / "paper/tables").mkdir(exist_ok=True)
    (R / "paper/tables/table10_surveys.md").write_text("\n".join(out) + "\n")

    print(f"table10_surveys.md: {len(rows)} rows, {n_unob} unobtained, {len(unread)} unread")
    for p in level_problems():
        print("LEVEL", p)
    if missing_spec:
        print("survey rows with no spec (add one or the row prints as unobtained):", missing_spec)
    if stale_spec:
        print("spec keys with no row:", stale_spec)
    for u in unsupported:
        print("UNSUPPORTED", u)


if __name__ == "__main__":
    main()
