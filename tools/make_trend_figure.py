"""The one figure the survey was missing: what the field trained on, by year.

Writes results/trends.json and results/trend.png. Every number is recomputed from
corpus/rows/*.json here, so the README figure and the README number come from the
same committed file and cannot drift from each other.

Local, CPU, matplotlib Agg. No paid compute.
"""
import json, glob, re
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = Path(__file__).resolve().parents[1]
SIM = {"RL", "RL+demo", "distillation"}
DEMO = {"BC", "VLA", "diffusion", "flow", "teleop-system", "data-collection"}
YEARS = list(range(2021, 2027))


def year(r):
    y = r.get("year")
    if y:
        return int(y)
    m = re.search(r"(\d{4})$", r["key"])
    return int(m.group(1)) if m else 0


def main():
    rows = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
    M = [r for r in rows if r.get("class") == "method"]
    out = {"method_papers": len(M), "by_year": {}}
    for y in YEARS:
        rs = [r for r in M if year(r) == y]
        out["by_year"][str(y)] = {
            "papers": len(rs),
            "simulator_trained": sum(1 for r in rs if set(r.get("paradigm") or []) & SIM),
            "demonstration_trained": sum(1 for r in rs if set(r.get("paradigm") or []) & DEMO),
        }
    # the crossover year: first year the demonstration branch leads and keeps leading
    lead = [y for y in YEARS
            if out["by_year"][str(y)]["demonstration_trained"]
            > out["by_year"][str(y)]["simulator_trained"]]
    out["crossover_year"] = next((y for y in lead if all(
        out["by_year"][str(z)]["demonstration_trained"]
        > out["by_year"][str(z)]["simulator_trained"] for z in YEARS if z >= y)), None)
    (R / "results/trends.json").write_text(json.dumps(out, indent=1) + "\n")

    sim = [out["by_year"][str(y)]["simulator_trained"] for y in YEARS]
    demo = [out["by_year"][str(y)]["demonstration_trained"] for y in YEARS]
    # 2026 is a partial year. Drawn dashed and hollow so the fall-off reads as a cut-off
    # rather than as a decline, which is what a solid line to the last point would imply.
    full, part = YEARS[:-1], YEARS[-2:]
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=170)
    for ys, vals, c, mk, lab in ((full, sim[:-1], "#1b3b6f", "o", "trained in a simulator (RL, distillation)"),
                                 (full, demo[:-1], "#c2410c", "s", "trained from demonstration (BC, VLA, diffusion, flow)")):
        ax.plot(ys, vals, mk + "-", lw=2.4, ms=6, color=c, label=lab)
    ax.plot(part, sim[-2:], "o--", lw=1.6, ms=6, color="#1b3b6f", mfc="white", alpha=0.8)
    ax.plot(part, demo[-2:], "s--", lw=1.6, ms=6, color="#c2410c", mfc="white", alpha=0.8)
    cx = out["crossover_year"]
    top = max(sim + demo)
    if cx:
        ax.axvline(cx, color="black", lw=0.9, ls=":", alpha=0.5)
        ax.annotate(f"the branches cross in {cx}", xy=(cx, 2.0), xytext=(cx + 0.12, 2.0),
                    ha="left", va="center", fontsize=9)
    ax.axvspan(YEARS[-1] - 0.5, YEARS[-1] + 0.35, color="black", alpha=0.045, lw=0)
    ax.text(YEARS[-1], top * 1.13, "2026 partial", ha="center", va="center",
            fontsize=8, color="#666")
    ax.set_xlabel("year"); ax.set_ylabel("method papers")
    ax.set_title("What dexterous-manipulation papers train on", fontsize=11.5, loc="left", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.25, lw=0.6)
    ax.set_xticks(YEARS); ax.set_xlim(2020.6, 2026.4); ax.set_ylim(0, top * 1.22)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0, 1.02))
    ax.text(1.0, -0.26, f"{len(M)} method papers. Counts recomputed from corpus/rows/ into results/trends.json.",
            transform=ax.transAxes, ha="right", fontsize=7, color="#555")
    fig.tight_layout()
    fig.savefig(R / "results/trend.png", bbox_inches="tight")
    print(f"results/trends.json and results/trend.png written; crossover {cx}")
    for y in YEARS:
        d = out["by_year"][str(y)]
        print(f"  {y}: {d['papers']:3} papers   sim {d['simulator_trained']:3}   demo {d['demonstration_trained']:3}")


if __name__ == "__main__":
    main()
