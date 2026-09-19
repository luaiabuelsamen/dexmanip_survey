"""Generate the survey's tables from corpus/rows/*.json. A cell that no note confirmed prints
as an em space, and each table states how many cells are empty.

No cell is truncated. Every free-text column here holds a clause, not a token, and the earlier
150-character cut fell mid-word: Table 4's Brax contact-model cell ended "no convex-decompos" and
its MuJoCo Warp solver cell ended "are", which are exactly the two columns Section 4.2 spends
2,000 words arguing about. Raising the cut would not have helped either, because these values run
to 480 characters and a 480-character cell is a paragraph printed sideways. Instead every cell
carries its full value, soft-wrapped at a word boundary with `<br>` so the rendered column has a
bounded width and the row grows downwards instead of sideways. WRAP_MAX is the widest a column is
allowed to render, in characters, and a column's declared width narrows it further.
"""
import json, glob, re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
ROWS = {}
for f in glob.glob(str(R / "corpus/rows/*.json")):
    try: r = json.load(open(f)); ROWS[r["key"]] = r
    except Exception as e: print(f"[bad] {f}: {e}")
bib = {e["key"]: e for e in json.loads((R / "corpus/bib.json").read_text())}
EM = " "
WRAP_MIN, WRAP_MAX = 16, 52

def soft_wrap(s, width):
    """Break a cell onto further rendered lines at word boundaries. Nothing is cut, and a word
    longer than the column is left whole rather than split."""
    w = max(WRAP_MIN, min(int(width), WRAP_MAX))
    if len(s) <= w: return s
    lines, cur = [], ""
    for word in s.split():
        if cur and len(cur) + 1 + len(word) > w:
            lines.append(cur); cur = word
        else:
            cur = word if not cur else cur + " " + word
    if cur: lines.append(cur)
    return " <br>".join(lines)

def cell(v, width=WRAP_MAX):
    if v is None or v == "" or v == []: return EM
    if isinstance(v, bool): return "yes" if v else "no"
    if isinstance(v, list): v = ", ".join(str(x) for x in v)
    s = str(v).replace("|", "/").replace("\n", " ").strip()
    return soft_wrap(s, width)

WRAPPED = ("\n*No cell is truncated. A value wider than its column is wrapped at a word boundary, "
           "so a cell that runs to several rendered lines is one value and not several.*")

def table(rows, cols, headers, sort=None, widths=None):
    """One row per record, with per-column rendered widths. `widths` is a column-to-width map;
    a column absent from it renders at WRAP_MAX."""
    if sort: rows = sorted(rows, key=sort)
    widths = widths or {}
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    empty = total = 0
    for r in rows:
        vals = [cell(r.get(c), widths.get(c, WRAP_MAX)) for c in cols]
        vals[0] = f"`{vals[0]}`"
        empty += sum(1 for v in vals if v == EM); total += len(vals)
        out.append("| " + " | ".join(vals) + " |")
    out.append(f"\n*{len(rows)} rows; {empty} of {total} cells ({100*empty//max(total,1)}%) are values no source stated.*"
               + WRAPPED)
    return "\n".join(out)

def cite(k): return f"`{k}`"

# TABLES.md asks Table 2 and Table 3 to carry "the corpus papers that use it". A hand row and a
# method row name the same hand in different words, so the link is made by an explicit pattern
# per hand key rather than by string equality. A key with no pattern here has none by design:
# no method row names it under any spelling. The count is of method rows whose OWN experiments
# use the hand (the `hand` field), not of mentions.
USES = {
    "allegro_hand_v4_2016":        r"allegro",
    "shadow_dexterous_hand_2005":  r"shadow(?!.*dex-?ee)",
    "shadow_dex_ee_2024":          r"dex-?ee",
    # \bleap\b missed `teledexter_2026`, whose hand field reads "also LeapHand (16-DoF)": a LEAP
    # hand written as one word. The boundary goes before the name only, so the count is 12 and
    # agrees with tools/check_numbers.py, section 3.2's prose and both editions' figure.
    "leap_hand_2023":              r"\bleap",
    "leap_hand_v2_adv_2025":       r"leap hand v2",
    "inspire_rh56dfx_2023":        r"inspire",
    "psyonic_ability_hand_2021":   r"psyonic|\bability\b",
    "robotera_xhand1_2024":        r"xhand",
    "sharpa_wave_2026":            r"sharpa",
    "wuji_hand_2025":              r"wuji",
    "faive_hand_2023":             r"faive",
    "brainco_revo2_2025":          r"brainco",
    "linkerbot_l20_2025":          r"linker",
    "agibot_omnihand_2025":        r"agibot",
    "unitree_dex5_2025":           r"dex5|dex-5",
    "orca_hand_2025":              r"\borca\b",
    "ruka_2025":                   r"\bruka\b",
    "ruka_v2_2026":                r"ruka[- ]?v2",
    "bidexhand_2025":              r"bidexhand",
    "dexhand_open_source_2023":    r"therobotstudio|dexhand v1",
    "tesollo_dg5f_2024":           r"tesollo|dg-5f",
    "ilda_hand_2021":              r"\bilda\b",
    "pisa_iit_softhand_2014":      r"pisa|softhand",
    "tesla_optimus_hand_2025":     r"optimus hand",
    "figure_03_hand_2025":         r"figure 0[23] hand",
    "onex_neo_hand_2026":          r"neo hand|1x hand",
    "sanctuary_phoenix_hand_2024": r"phoenix hand",
    "boston_dynamics_atlas_hand_2026": r"atlas hand",
    "xiaomi_cyberone_hand_2026":   r"cyberone",
    "clone_robotics_hand_2024":    r"myofiber|clone hand",
    "daxo_muscle_v0_2025":         r"muscle v0|daxo",
    "proception_prohand_2026":     r"prohand",
    "paxini_dexh13_2024":          r"dexh13|paxini",
}

# The hand bar chart in each edition counts the same quantity as the `uses` column above, so it
# reads its patterns from USES rather than keeping a second set. Four categories it draws have no
# hand row of their own and carry their pattern here: two research fixtures, a gripper that is not
# a dexterous hand, and the Adroit, which is the MuJoCo model of a Shadow hand. The Adroit is a
# line of its own rather than folded into Shadow, because the prose, the `uses` column and
# tools/check_numbers.py all count `shadow`: folding it in printed 24 in the LaTeX figure against
# the 21 three lines below it.
FIG_EXTRA = {
    "adroit":           r"adroit",
    "gripper":          r"parallel.?jaw|gripper",
    "dclaw_trifinger":  r"d.?claw|trifinger",
    "fourier":          r"fourier",
    "psibot":           r"psibot",
    "schunk":           r"schunk",
    "oymotion":         r"oymotion",
    "bytedexter":       r"bytedexter",
}

def uses_pattern(slug):
    """The one pattern for `method rows whose own experiments use this hand`, by hand key or slug."""
    if slug in USES: return USES[slug]
    return FIG_EXTRA[slug]


def used_by(key, methods, cap=3):
    """Method rows whose own experiments run on this hand, as 'n: key, key, ...'."""
    pat = USES.get(key)
    if not pat: return "0"
    ks = sorted(m["key"] for m in methods if re.search(pat, str(m.get("hand") or ""), re.I))
    if not ks: return "0"
    shown = ", ".join(f"`{k}`" for k in ks[:cap])
    return f"{len(ks)}: {shown}" + (", …" if len(ks) > cap else "")


# --- Table 2 and Table 3 -------------------------------------------------------------------
# One hand row holds several kinds of number that a single column would conflate. "force N" is
# whatever the source measured and "what the force is" says which quantity that was, because
# pull-out resistance, pinch force, fingertip normal force and a vendor's unlabelled spec are
# not comparable. Payload is separate again: no two hands here report it under the same test.
# Actuator counts are kept apart from actuated DoF, because a servo count is not a DoF count.
# claim_date carries the date of the claim, per SECTION_BRIEF rule 5; an undated page says so.
HAND_COLS = [
    ("key",               "hand",                  28),
    ("maker",             "maker",                 44),
    ("dof",               "joints",                12),
    ("actuated_dof",      "act. DoF",              12),
    ("actuators",         "actuators",             12),
    ("actuation",         "actuation",             70),
    ("weight_g",          "weight g",              12),
    ("fingertip_force_n", "force N",               12),
    ("force_kind",        "what the force is",    130),
    ("payload",           "payload",               90),
    ("control_rate",      "control rate",          80),
    ("sim_model",         "URDF or MJCF",          80),
    ("tactile",           "tactile",               70),
    ("price_usd",         "price USD",             12),
    ("open_hardware",     "open HW",                8),
    ("release_status",    "status",                18),
    ("source_quality",    "source",                26),
    ("claim_date",        "claim date",            70),
    ("used_by",           "corpus methods using it", 90),
]
# The emptiness figure is quoted over the specification columns only. The key, maker, provenance
# and usage columns can never be blank, and counting them dilutes the finding (R1, finding 29).
HAND_SPEC_COLS = {"dof", "actuated_dof", "actuators", "actuation", "weight_g", "fingertip_force_n",
                  "force_kind", "payload", "control_rate", "sim_model", "tactile", "price_usd"}

def hand_table(rows, sort=None):
    """Table 2 or Table 3, with the force column split by quantity and every claim dated.

    Returns the markdown table, its caption, and numbered footnotes carrying each row's
    spec_caveat, which is where a figure with no reachable source is named as such."""
    if sort: rows = sorted(rows, key=sort)
    cols = [c for c, _, _ in HAND_COLS]
    notes, marks = [], {}
    for r in rows:
        if r.get("spec_caveat"):
            notes.append(f"{len(notes)+1}. `{r['key']}`: {r['spec_caveat']}")
            marks[r["key"]] = f" [{len(notes)}]"
    out = ["| " + " | ".join(h for _, h, _ in HAND_COLS) + " |",
           "|" + "|".join(["---"] * len(HAND_COLS)) + "|"]
    empty = total = 0
    for r in rows:
        vals = [cell(r.get(c), w) for c, _, w in HAND_COLS]
        vals[0] = f"`{vals[0]}`" + marks.get(r["key"], "")
        for (c, _, _), v in zip(HAND_COLS, vals):
            if c in HAND_SPEC_COLS:
                total += 1
                empty += (v == EM)
        out.append("| " + " | ".join(vals) + " |")
    pct = 100 * empty // max(total, 1)
    out.append(f"\n*{len(rows)} rows. {empty} of {total} specification cells ({pct}%) over the "
               f"{len(HAND_SPEC_COLS)} specification columns are values no source stated; the key, maker, "
               "provenance and usage columns are excluded because they are never blank. Every figure "
               "here is the maker's or the authors' own claim. Nobody outside the maker has measured "
               "any DoF, force, weight or price cell in this table, except the rows sourced to a "
               "peer-reviewed paper with a stated protocol. The force column is not a ranking: read "
               "'what the force is' first, because pull-out resistance, pinch force, a fingertip "
               "normal force under an indenter and an unlabelled vendor spec are different "
               "measurements. A blank cell means no source stated the value. No cell is truncated: "
               "a value wider than its column is wrapped at a word boundary, so a cell that runs "
               "to several rendered lines is one value and not several.*")
    if notes:
        out.append("\nFigures with no reachable source, and other caveats on individual rows:\n")
        out.extend(notes)
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    outdir = R / "paper/tables"; outdir.mkdir(exist_ok=True)
    hands = [r for r in ROWS.values() if r.get("class") == "hand"]
    methods_for_use = [r for r in ROWS.values() if r.get("class") == "method"]
    for h in hands: h["used_by"] = used_by(h["key"], methods_for_use)
    sold = [r for r in hands if r.get("release_status") in ("sold", "open-source", None)]
    unrel = [r for r in hands if r.get("release_status") in ("announced", "prototype", "internal-only")]
    # Sorted by joint count descending. A row whose joint count has no reachable source has a
    # null there and sorts last, rather than being ranked by a number nobody stated.
    by_joints = lambda r: -(r.get("dof") or 0)
    (outdir/"table2_hands_available.md").write_text(
        "### Table 2. Hands that can be obtained\n\n" + hand_table(sold, sort=by_joints))
    (outdir/"table3_hands_announced.md").write_text(
        "### Table 3. Hands announced but not purchasable\n\n" + hand_table(unrel, sort=by_joints))
    sims = [r for r in ROWS.values() if r.get("class") == "simulator"]
    sc = ["key","contact_model","solver","solver_iterations","differentiable","gpu","default_timestep_s","penetration_exposed","throughput","hands_shipped","license"]
    sh = ["engine","contact model","solver","iters","diff.","GPU","dt s","penetration exposed","throughput","hands shipped","licence"]
    # `contact_model` and `solver` carry Section 4.2's argument, so they render at full width.
    sw = {"key": 26, "contact_model": 52, "solver": 52, "solver_iterations": 28, "differentiable": 8,
          "gpu": 8, "default_timestep_s": 10, "penetration_exposed": 12, "throughput": 44,
          "hands_shipped": 40, "license": 24}
    (outdir/"table4_simulators.md").write_text("### Table 4. Simulators and physics engines\n\n" + table(sims, sc, sh, sort=lambda r: str(r.get("key")), widths=sw))
    meth = [r for r in ROWS.values() if r.get("class") == "method"]
    mc = ["key","year","task_family","paradigm","algorithm","hand","hand_dof","bimanual","sim","real_robot","real_trials","objects_test_unseen","penetration","code_released"]
    mh = ["method","yr","task","paradigm","algorithm","hand","DoF","bi","sim","real","trials","unseen obj","penetration","code"]
    # Fourteen columns over 112 rows: the categorical columns are narrow so the two free-text
    # columns, `algorithm` and `hand`, have room to wrap rather than to cut.
    mw = {"key": 26, "year": 6, "task_family": 24, "paradigm": 20, "algorithm": 48, "hand": 30,
          "hand_dof": 6, "bimanual": 6, "sim": 24, "real_robot": 6, "real_trials": 8,
          "objects_test_unseen": 8, "penetration": 14, "code_released": 6}
    (outdir/"table7_methods.md").write_text("### Table 7. Methods\n\n" + table(meth, mc, mh, sort=lambda r: (str(r.get("year")), r["key"]), widths=mw))
    # --- Table 5. Reward-term families across the in-hand reorientation RL methods ---
    rm = json.loads((R / "corpus/reward_matrix.json").read_text())
    fams, labs = rm["_families"], rm["_family_labels"]
    MARK = {"paper": "paper", "code": "code", "both": "both", "code-zero": "code (0)", None: "\u2003"}
    t5 = ["| method | yr | " + " | ".join(labs[f] for f in fams) + " | terms | code | paper/code mismatch |",
          "|" + "|".join(["---"] * (len(fams) + 5)) + "|"]
    empty = total = 0
    for row in sorted(rm["rows"], key=lambda x: (ROWS.get(x["key"], {}).get("year", 0), x["key"])):
        src = ROWS.get(row["key"], {})
        cells = [MARK[row[f]] for f in fams]
        empty += sum(1 for c in cells if c == EM); total += len(cells)
        t5.append("| `%s` | %s | %s | %s | %s | %s |" % (
            row["key"], cell(src.get("year")), " | ".join(cells),
            cell(src.get("reward_terms")), cell(src.get("code_released")),
            "yes" if src.get("paper_code_mismatch") else ("no" if src.get("code_released") else EM)))
    t5.append("\n*%d rows; %d of %d term cells (%d%%) are families the method does not use. "
              "`paper` means the term is in the paper and either no code was released or it is absent from "
              "the released reward code; `code` means it is in the released code and not in the paper's "
              "stated reward; `both` means it is in both. Marks are read from papers/notes/, term by term; "
              "the per-method source section is in corpus/reward_matrix.json.*"
              % (len(rm["rows"]), empty, total, 100 * empty // max(total, 1)))
    (outdir/"table5_rewards.md").write_text("### Table 5. Reward terms across in-hand reorientation methods\n\n" + "\n".join(t5))

    # --- Table 6. Teleoperation and human-data systems ---
    tele = [r for r in ROWS.values() if "operator_interface" in r]
    def collected(r):
        bits = []
        if r.get("data_trajectories"): bits.append(f"{r['data_trajectories']:,} traj")
        if r.get("data_hours"): bits.append(f"{r['data_hours']} h")
        return ", ".join(bits) or None
    for r in tele: r["_collected"] = collected(r)
    tc = ["key","operator_interface","hand","retargeting_objective","latency","rig_cost_usd","_collected"]
    th = ["system","operator interface","robot hand","retargeting objective","latency","rig USD","data collected"]
    tw = {"key": 24, "operator_interface": 46, "hand": 28, "retargeting_objective": 48,
          "latency": 22, "rig_cost_usd": 10, "_collected": 16}
    (outdir/"table6_teleop.md").write_text("### Table 6. Teleoperation and human-data systems\n\n"
        + table(tele, tc, th, sort=lambda r: (str(r.get("year")), r["key"]), widths=tw))

    # --- Table 11. The nine artefact comparisons ---
    # The paper-against-code finding, set as what it is: a repository, the commit that was
    # fetched, the file inside it, and the two values. Every cell is the row's
    # `mismatch_artifact` field, whose repo and commit are copied from corpus/code_manifest.json,
    # so this table cannot name a commit the corpus did not fetch. No cell states a cause.
    cg = sorted((r for r in ROWS.values() if r.get("mismatch_class") == "contradiction"),
                key=lambda r: (r.get("year") or 0, r["key"]))
    miss = [r["key"] for r in cg if not r.get("mismatch_artifact")]
    assert not miss, f"contradiction rows with no mismatch_artifact: {miss}"
    # The confidence column is read from `mismatch_confidence`, not typed. Eight of the nine are
    # high and one is medium; printing nine rows flat put the qualification a column away in the
    # prose, where a screenshot of the table loses it.
    noconf = [r["key"] for r in cg if not r.get("mismatch_confidence")]
    assert not noconf, f"contradiction rows with no mismatch_confidence: {noconf}"
    t11 = ["| method | confidence | repository, fetched commit | file in it, and where | "
           "what the paper prints | what that file contains |",
           "|---|---|---|---|---|---|"]
    for r in cg:
        a = r["mismatch_artifact"]
        slug = re.sub(r"^https?://github\.com/", "", a["repo"]).rstrip("/")
        t11.append("| `%s` | %s | %s <br>`%s` | `%s` <br>`%s` | %s | %s |" % (
            r["key"], r["mismatch_confidence"], slug, a["commit"][:10], a["file"], a["locator"],
            cell(a["paper"]), cell(a["code"])))
    from collections import Counter as _C
    nconf = _C(r["mismatch_confidence"] for r in cg)
    split = ", ".join(f"{nconf[k]} {k}" for k in ("high", "medium", "low") if nconf.get(k))
    held = [r["key"] for r in cg if r["mismatch_confidence"] != "high"]
    t11.append("\n*%d rows. The repository and the commit are the ones "
               "`corpus/code_manifest.json` records, and the file is in the parsed copy at "
               "`code/md/<key>.md`. `what the paper prints` names the table or equation the "
               "value was read from. `confidence` is the row's own `mismatch_confidence` field, "
               "%s; %s %s held below high pending a direct code read this survey has not made, "
               "and Appendix C prints the review note. No cell states a cause, and none is a "
               "claim about what the work's authors did: a reader with a browser settles every "
               "line of this table without asking anyone.*"
               % (len(cg), split, ", ".join("`%s`" % k for k in held),
                  "is" if len(held) == 1 else "are"))
    (outdir/"table11_codegap.md").write_text(
        "### Table 11. Paper and released repository, the nine rows that state different values"
        "\n\n" + "\n".join(t11))

    print("hands", len(hands), "sims", len(sims), "methods", len(meth),
          "reward rows", len(rm["rows"]), "teleop rows", len(tele),
          "contradiction rows", len(cg))
    for f in sorted(outdir.glob("*.md")): print(" ", f.name, f.stat().st_size)
