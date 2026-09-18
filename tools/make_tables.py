"""Generate the survey's tables from corpus/rows/*.json. A cell that no note confirmed prints
as an em space, and each table states how many cells are empty."""
import json, glob
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

if __name__ == "__main__":
    outdir = R / "paper/tables"; outdir.mkdir(exist_ok=True)
    hands = [r for r in ROWS.values() if r.get("class") == "hand"]
    sold = [r for r in hands if r.get("release_status") in ("sold", "open-source", None)]
    unrel = [r for r in hands if r.get("release_status") in ("announced", "prototype", "internal-only")]
    hc = ["key","maker","dof","actuated_dof","actuation","weight_g","fingertip_force_n","tactile","price_usd","open_hardware","release_status","source_quality"]
    hh = ["hand","maker","DoF","act. DoF","actuation","weight g","tip force N","tactile","price USD","open HW","status","source"]
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
    print("hands", len(hands), "sims", len(sims), "methods", len(meth))
    for f in sorted(outdir.glob("*.md")): print(" ", f.name, f.stat().st_size)
