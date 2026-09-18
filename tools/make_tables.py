"""Generate the survey's tables from corpus/rows/*.json. A cell that no note confirmed prints
as an em space, and each table states how many cells are empty."""
import json, glob, re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
ROWS = {}
for f in glob.glob(str(R / "corpus/rows/*.json")):
    try: r = json.load(open(f)); ROWS[r["key"]] = r
    except Exception as e: print(f"[bad] {f}: {e}")
bib = {e["key"]: e for e in json.loads((R / "corpus/bib.json").read_text())}
EM = " "

def cell(v, width=90):
    if v is None or v == "" or v == []: return EM
    if isinstance(v, bool): return "yes" if v else "no"
    if isinstance(v, list): v = ", ".join(str(x) for x in v)
    s = str(v).replace("|", "/").replace("\n", " ").strip()
    return s if len(s) <= width else s[:width - 1].rstrip() + "\u2026"

def table(rows, cols, headers, sort=None):
    if sort: rows = sorted(rows, key=sort)
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    empty = total = 0
    for r in rows:
        vals = [cell(r.get(c)) for c in cols]
        vals[0] = f"`{vals[0]}`"
        empty += sum(1 for v in vals if v == EM); total += len(vals)
        out.append("| " + " | ".join(vals) + " |")
    out.append(f"\n*{len(rows)} rows; {empty} of {total} cells ({100*empty//max(total,1)}%) are values no source stated.*")
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
    "leap_hand_2023":              r"\bleap\b",
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

def used_by(key, methods, cap=3):
    """Method rows whose own experiments run on this hand, as 'n: key, key, ...'."""
    pat = USES.get(key)
    if not pat: return "0"
    ks = sorted(m["key"] for m in methods if re.search(pat, str(m.get("hand") or ""), re.I))
    if not ks: return "0"
    shown = ", ".join(f"`{k}`" for k in ks[:cap])
    return f"{len(ks)}: {shown}" + (", …" if len(ks) > cap else "")

if __name__ == "__main__":
    outdir = R / "paper/tables"; outdir.mkdir(exist_ok=True)
    hands = [r for r in ROWS.values() if r.get("class") == "hand"]
    methods_for_use = [r for r in ROWS.values() if r.get("class") == "method"]
    for h in hands: h["used_by"] = used_by(h["key"], methods_for_use)
    sold = [r for r in hands if r.get("release_status") in ("sold", "open-source", None)]
    unrel = [r for r in hands if r.get("release_status") in ("announced", "prototype", "internal-only")]
    hc = ["key","maker","dof","actuated_dof","actuation","weight_g","fingertip_force_n","tactile","price_usd","open_hardware","release_status","source_quality","used_by"]
    hh = ["hand","maker","DoF","act. DoF","actuation","weight g","tip force N","tactile","price USD","open HW","status","source","corpus methods using it"]
    (outdir/"table2_hands_available.md").write_text("### Table 2. Hands that can be obtained\n\n" + table(sold, hc, hh, sort=lambda r: -(r.get("dof") or 0)))
    (outdir/"table3_hands_announced.md").write_text("### Table 3. Hands announced but not purchasable\n\n" + table(unrel, hc, hh, sort=lambda r: -(r.get("dof") or 0)))
    sims = [r for r in ROWS.values() if r.get("class") == "simulator"]
    sc = ["key","contact_model","solver","solver_iterations","differentiable","gpu","default_timestep_s","penetration_exposed","throughput","hands_shipped","license"]
    sh = ["engine","contact model","solver","iters","diff.","GPU","dt s","penetration exposed","throughput","hands shipped","licence"]
    (outdir/"table4_simulators.md").write_text("### Table 4. Simulators and physics engines\n\n" + table(sims, sc, sh, sort=lambda r: str(r.get("key"))))
    meth = [r for r in ROWS.values() if r.get("class") == "method"]
    mc = ["key","year","task_family","paradigm","algorithm","hand","hand_dof","bimanual","sim","real_robot","real_trials","objects_test_unseen","penetration","code_released"]
    mh = ["method","yr","task","paradigm","algorithm","hand","DoF","bi","sim","real","trials","unseen obj","penetration","code"]
    (outdir/"table7_methods.md").write_text("### Table 7. Methods\n\n" + table(meth, mc, mh, sort=lambda r: (str(r.get("year")), r["key"])))
    # --- Table 5. Reward-term families across the in-hand reorientation RL methods ---
    rm = json.loads((R / "corpus/reward_matrix.json").read_text())
    fams, labs = rm["_families"], rm["_family_labels"]
    MARK = {"paper": "paper", "code": "code", "both": "both", None: EM}
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
    (outdir/"table6_teleop.md").write_text("### Table 6. Teleoperation and human-data systems\n\n"
        + table(tele, tc, th, sort=lambda r: (str(r.get("year")), r["key"])))

    print("hands", len(hands), "sims", len(sims), "methods", len(meth),
          "reward rows", len(rm["rows"]), "teleop rows", len(tele))
    for f in sorted(outdir.glob("*.md")): print(" ", f.name, f.stat().st_size)
