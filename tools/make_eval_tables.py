"""Write Tables 8 and 9 for section 7.

Table 8 is the proposed protocol. It is hand-written here rather than derived from the corpus,
because it states what a future evaluation should measure, not what a past one did. Its trial
counts come from the binomial-interval derivation printed by --derive, which is the same
derivation the section text gives in prose.

Table 9 is the empty results matrix. Its rows are selected from the corpus, so the selection is
auditable: method rows whose own experiments use a multi-fingered hand and that produce a
policy, ranked by how many other corpus papers name them in papers/md. That count is a count of
mentions, not of use, exactly as corpus METHOD.md says. Teleoperation systems are dropped,
because an interface is not a policy and cannot be scored on these axes.

Section 7 pulls both in through the {{table:...}} placeholders that tools/assemble.py expands,
so the section text and these files cannot drift apart. Regenerate with:

    python tools/make_eval_tables.py            # write paper/tables/table8_*.md, table9_*.md
    python tools/make_eval_tables.py --derive   # print the trial-count derivation only
"""
import glob
import json
import math
import os
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
Z = 1.959963985  # two-sided 95 percent normal quantile
ROW_COUNT = 12
TELEOP_ONLY = {"teleop-system"}

AXES = ["task success", "robustness", "unseen objects", "physical plausibility",
        "cost", "transfer", "reproducibility"]


def wilson_halfwidth(p: float, n: int) -> float:
    """Half-width of the Wilson score interval, the width a reported rate actually carries."""
    d = 1 + Z * Z / n
    return Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d


def n_for_halfwidth(h: float, p: float = 0.5) -> int:
    """Smallest n whose Wilson half-width at p is at most h. p=0.5 is the worst case."""
    n = 2
    while wilson_halfwidth(p, n) > h:
        n += 1
    return n


def n_per_arm(p1: float, p2: float, power: float = 0.80) -> float:
    """Trials per arm for a two-sided two-proportion test at alpha=0.05 with the given power."""
    zb = {0.80: 0.8416212336, 0.90: 1.2815515655}[power]
    pbar = (p1 + p2) / 2
    num = Z * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return (num / abs(p1 - p2)) ** 2


def derivation() -> str:
    out = ["Trial-count derivation (95 percent Wilson interval, worst case p = 0.5):"]
    for h in (0.20, 0.15, 0.10, 0.05):
        out.append(f"  half-width {h:.2f} -> n = {n_for_halfwidth(h)}")
    out.append("Observed widths at the corpus median of 20 trials:")
    for p in (0.6, 0.8):
        out.append(f"  {p:.0%} on 20 trials -> +/- {wilson_halfwidth(p, 20) * 100:.1f} points")
    out.append("At the proposed 100 trials:")
    for p in (0.5, 0.8):
        out.append(f"  {p:.0%} on 100 trials -> +/- {wilson_halfwidth(p, 100) * 100:.1f} points")
    out.append("Paired A/B, alpha 0.05 two-sided, 80 percent power, trials per arm:")
    for a, b in ((0.5, 0.7), (0.5, 0.65), (0.5, 0.6)):
        out.append(f"  {a:.0%} vs {b:.0%} -> {n_per_arm(a, b):.0f}")
    out.append("Continuous score, half-width in standard deviations:")
    for n in (30, 100):
        out.append(f"  n = {n} rollouts -> +/- {Z / math.sqrt(n):.2f} sd")
    return "\n".join(out)


TABLE8 = """### Table 8. The proposed evaluation protocol

| axis | what is measured | how | minimum trial count | reported alongside it | why |
|---|---|---|---|---|---|
| Task success | fraction of episodes meeting a criterion, and a graded rubric score in [0,1] over equally weighted milestones | criterion written before the run by the designer and scored by someone else; terminal predicate held for a 0.5 s dwell; initial conditions matched by image overlay; policies interleaved blind in one session | 100 real and 200 sim, per task per policy per condition | Wilson 95 percent interval, raw counts, the criterion verbatim, the rubric, the initial-condition protocol | a rate without a denominator and an interval cannot be compared; the rubric separates a near-miss from inaction |
| Robustness | success under each perturbation axis, reported as the ratio to the unperturbed anchor | axes that must not change the action and axes that must are scored separately; ranges stated; anchor replayed exactly | 40 per axis per policy in sim; the two worst axes repeated at 100 real | both absolute rates, the ratio, the axis ranges, and which split each axis is in | the ranking at the anchor is not the ranking under shift |
| Unseen objects | mean over held-out objects of per-object success | objects drawn from a stated distribution disjoint from training; bootstrap over objects, not trials | 20 objects at 5 trials for a screening claim; 93 objects for a 10-point claim | the object list, per-object rates, the bootstrap interval, the object-count caveat | the resampling unit is the object, so trial counts overstate the precision |
| Physical plausibility | maximum and mean hand-object penetration depth per rollout, and the fraction of frames above 2 mm | dense surface sample against the object mesh or SDF, computed on the policy's own rollouts by code that never entered the reward or the termination rule | 100 rollouts, simulation only | interval over rollouts, sample density, threshold, solver depenetration settings, and at least one rendered rollout | a measure the policy optimised is not evidence about the policy |
| Sample and wall-clock cost | environment steps and wall-clock to the checkpoint that produced the headline number | counted to that checkpoint, not to the end of training; GPU model and count stated | 3 training seeds | the range over seeds, and the statement that 3 seeds is a range and not an interval | training variance is not rollout variance and the two are routinely conflated |
| Real-robot transfer | paired real and simulated outcomes on matched initial conditions, and their correlation | the same 100 initial conditions run in both; report the paired correlation and the rectifier variance | the 100 real trials, paired to 100 sim | correlation, rectifier variance against real variance, and whether simulation narrowed the interval | a simulator earns a real-world claim only through its measured paired correlation |
| Reproducibility | code, checkpoints, and the exact config that produced the headline run | diff the paper's stated objective against the released config and name the file and line of every disagreement | not a trial count | the named file and line for each disagreement, or an explicit statement that none was found | 37 of the 110 method rows already carry such a disagreement |
"""


def method_name(key: str) -> str:
    first = open(R / f"papers/notes/{key}.md", errors="ignore").readline()
    m = re.match(r"#\s*\S+\s+—\s*(.+)", first)
    return re.split(r"[:(,]", m.group(1))[0].strip() if m else key


def table9_rows():
    rows = [json.load(open(f)) for f in sorted(glob.glob(str(R / "corpus/rows/*.json")))]
    meth = [r for r in rows if r.get("class") == "method" and r.get("hand")]
    # papers/md holds both <key>.md and, where the layout parse was thin, <key>.ocr.md. Both
    # belong to the same paper, so they are merged under one key; otherwise every mention of a
    # re-OCRed paper would be counted twice.
    texts = {}
    for f in glob.glob(str(R / "papers/md/*.md")):
        key = re.sub(r"\.ocr$", "", os.path.basename(f)[:-3])
        texts[key] = texts.get(key, "") + open(f, errors="ignore").read().lower()
    scored = []
    for r in meth:
        if set(r.get("paradigm") or []) <= TELEOP_ONLY:
            continue
        hand = r["hand"].lower()
        if "parallel" in hand or "gripper" in hand:
            continue
        name = method_name(r["key"])
        if len(name) < 4:
            continue
        n = sum(1 for k, t in texts.items() if k != r["key"] and name.lower() in t)
        scored.append((n, r["key"]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[:ROW_COUNT]


def main():
    if "--derive" in sys.argv:
        print(derivation())
        return
    outdir = R / "paper/tables"
    outdir.mkdir(exist_ok=True)
    (outdir / "table8_protocol.md").write_text(TABLE8)

    picked = table9_rows()
    head = "| method | " + " | ".join(AXES) + " |"
    rule = "|" + "|".join(["---"] * (len(AXES) + 1)) + "|"
    body = [f"| `{k}` |" + " |" * len(AXES) for _, k in picked]
    cells = len(picked) * len(AXES)
    txt = ("### Table 9. The matrix, for someone else to fill\n\n"
           + "\n".join([head, rule] + body)
           + f"\n\n*{len(picked)} rows, {cells} cells, all {cells} empty. Rows are the "
             f"{len(picked)} most-mentioned dexterous-hand policy methods in the corpus; "
             "mention counts are counts of mentions, not of use.*\n")
    (outdir / "table9_matrix.md").write_text(txt)
    print("wrote table8_protocol.md and table9_matrix.md")
    for n, k in picked:
        print(f"  {n:3d} {k}")


if __name__ == "__main__":
    main()
