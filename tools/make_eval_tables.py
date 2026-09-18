"""Write Tables 8 and 9 for section 7.

Table 8 is the proposed protocol. It is hand-written here rather than derived from the corpus,
because it states what a future evaluation should measure, not what a past one did. Every trial
count in it comes from the derivation printed by --derive, and every line that derivation prints
is used somewhere in section 7, so the tool's output and the prose stay in one-to-one
correspondence.

Each axis is derived for the statistic that axis actually reports. A single rate takes a Wilson
half-width; a matched A/B comparison takes McNemar, because the protocol matches initial
conditions and interleaves the policies, which is a paired design; a ratio to an unperturbed
anchor takes the standard error of the log ratio; a correlation takes the Fisher-z interval.
An earlier version of this file derived the A/B count from n_per_arm, the independent-samples
formula, while printing the word "Paired" above it.

Table 9 is the empty results matrix. Its rows are selected from the corpus, so the selection is
auditable. The rule, stated here and restated in section 7.6 in the same words:

  1. method rows only, with a non-null `hand`;
  2. the hand string must not contain "parallel" or "gripper", so the matrix is about
     multi-fingered hands;
  3. the row must carry at least one paradigm tag that produces a closed-loop policy, and must
     not carry `teleop-system`: an interface is scored on latency and operator effort, not on a
     policy's success rate, so it is not a row of this matrix even when the paper also trains a
     policy from the data its interface collected;
  4. the method's name must be at least 4 characters, so that a short string does not match
     everything;
  5. score = the number of OTHER corpus papers whose parsed text in papers/md contains that name
     as a whole word, ranked by count and then by key, top 12.

The word-boundary match matters. Under a bare substring test "UniDex" is a prefix of
"UniDexGrasp" and "UniDexGrasp++", and `unidex_2026` inherited 34 mentions of a different and
much older paper; as a whole word it has 3. The count is a count of mentions, not of use,
exactly as corpus METHOD.md says.

Section 7 pulls both tables in through the {{table:...}} placeholders that tools/assemble.py
expands, so the section text and these files cannot drift apart. Regenerate with:

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
ZB80 = 0.8416212336  # 80 percent power
ROW_COUNT = 12

# Paradigm tags that produce a closed-loop policy, and the tag that disqualifies a row however
# many of the others it also carries.
POLICY_TAGS = {"RL", "BC", "diffusion", "flow", "RL+demo", "distillation", "VLA", "MPC",
               "world-model"}
INTERFACE_TAG = "teleop-system"

AXES = [
    "task success (rate &plusmn; Wilson 95, n)",
    "robustness (per-axis rate &plusmn; Wilson 95, n; ratio to anchor)",
    "unseen objects (mean per-object rate, bootstrap 95, k objects)",
    "plausibility (max / mean mm, frac frames > 2 mm)",
    "cost (env steps, GPU-h, 3-seed range)",
    "transfer (&rho; [lo, hi], rectifier var / real var)",
    "reproducibility (file:line of each disagreement, or none)",
]

# A worked row, so that the format of a cell is unambiguous. Every number in it is invented.
EXAMPLE = [
    "*worked example &mdash; every number fabricated*",
    "0.72 &plusmn; 0.09 (100)",
    "lighting 0.41 &plusmn; 0.15 (40), ratio 0.57; anchor 0.72 &plusmn; 0.09 (100)",
    "0.55, [0.41, 0.68], 20 objects",
    "3.1 / 0.8 mm, 0.12",
    "1.2e9 steps, 46 GPU-h, 0.68&ndash;0.74",
    "0.61 [0.47, 0.72], 0.43",
    "`cfg/train.yaml:88` orient weight 0.0 vs paper 0.5",
]


# ---------------------------------------------------------------- one rate, fixed n
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


def phi(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def two_prop_z(k1: int, n1: int, k2: int, n2: int):
    """Pooled two-sided two-proportion test. Overlapping intervals are not this test."""
    p1, p2 = k1 / n1, k2 / n2
    pool = (k1 + k2) / (n1 + n2)
    se = math.sqrt(pool * (1 - pool) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se
    return z, 2 * (1 - phi(abs(z)))


# ---------------------------------------------------------------- A/B, two designs
def n_per_arm(p1: float, p2: float, power: float = 0.80) -> float:
    """Trials per arm for a two-sided two-proportion test on INDEPENDENT arms, alpha = 0.05.

    This is the right formula only when the two arms are separate draws. The protocol in Table 8
    matches initial conditions and interleaves the policies, which is a paired design, so the
    count that governs it is n_pairs_mcnemar below. This function is kept to print the
    independent-arm number for comparison.
    """
    zb = {0.80: ZB80, 0.90: 1.2815515655}[power]
    pbar = (p1 + p2) / 2
    num = Z * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return (num / abs(p1 - p2)) ** 2


def n_pairs_mcnemar(p1: float, p2: float, discordance: float, power: float = 0.80) -> float:
    """Matched pairs per arm for McNemar's test at alpha = 0.05.

    A matched-pair binary comparison depends on the discordance rate -- the share of initial
    conditions on which the two policies disagree -- and not on p1 and p2 alone. Discordance is
    at least |p1 - p2|, and equals p1(1-p2) + p2(1-p1) when the pairing buys nothing; at that
    value the count returns to the independent-arm count, which is the honest worst case.
    """
    d = abs(p1 - p2)
    if discordance < d * d:
        raise ValueError("discordance below the squared difference is not attainable")
    zb = {0.80: ZB80, 0.90: 1.2815515655}[power]
    return (Z * math.sqrt(discordance) + zb * math.sqrt(discordance - d * d)) ** 2 / (d * d)


# ---------------------------------------------------------------- a ratio of two rates
def logratio_ci(p_anchor: float, p_shift: float, n: int):
    """95 percent interval for the ratio p_shift / p_anchor at n trials in each, via log RR."""
    rr = p_shift / p_anchor
    se = math.sqrt((1 - p_anchor) / (n * p_anchor) + (1 - p_shift) / (n * p_shift))
    return rr, math.exp(math.log(rr) - Z * se), math.exp(math.log(rr) + Z * se)


def n_for_ratio(p_anchor: float, p_shift: float, power: float = 0.80) -> float:
    """Trials per arm to show the ratio differs from 1 at 80 percent power, via the log ratio."""
    zb = {0.80: ZB80, 0.90: 1.2815515655}[power]
    v = (1 - p_anchor) / p_anchor + (1 - p_shift) / p_shift
    return ((Z + zb) / math.log(p_shift / p_anchor)) ** 2 * v


# ---------------------------------------------------------------- a correlation
def rho_ci(rho: float, n: int):
    """Fisher-z 95 percent interval for a correlation on n pairs."""
    s = 1 / math.sqrt(n - 3)
    z = math.atanh(rho)
    return math.tanh(z - Z * s), math.tanh(z + Z * s)


def n_for_rho(rho: float, h: float) -> int:
    """Smallest n whose Fisher-z interval keeps BOTH limits within h of rho."""
    n = 6
    while True:
        lo, hi = rho_ci(rho, n)
        if max(rho - lo, hi - rho) <= h:
            return n
        n += 1


# ---------------------------------------------------------------- the protocol's bill
POLICIES, TASKS = 2, 3
DISC = 0.30  # assumed discordance for the headline paired count


def bill():
    """Real rollouts for a two-policy, three-task comparison run to Table 8."""
    pairs = math.ceil(n_pairs_mcnemar(0.5, 0.7, DISC))
    matched = POLICIES * TASKS * pairs
    unseen = POLICIES * TASKS * 100           # 20 held-out objects at 5 trials
    old = POLICIES * TASKS * 200              # the unpaired route: 100 matched + 100 unseen
    return pairs, matched, unseen, matched + unseen, old


def derivation() -> str:
    out = ["A. One reported rate, fixed n (95 percent Wilson, worst case p = 0.5):"]
    for h in (0.20, 0.15, 0.10, 0.05):
        out.append(f"  half-width {h:.2f} -> n = {n_for_halfwidth(h)}")
    out.append("   observed widths at the corpus median of 20 trials:")
    for p in (0.6, 0.8):
        out.append(f"     {p:.0%} on 20 trials -> +/- {wilson_halfwidth(p, 20) * 100:.1f} points")
    z, p = two_prop_z(12, 20, 16, 20)
    out.append(f"   and 12/20 against 16/20 is z = {z:.2f}, p = {p:.2f}"
               "  (overlapping intervals are not a test)")
    out.append("   at the proposed 100 trials:")
    for p in (0.5, 0.8):
        out.append(f"     {p:.0%} on 100 trials -> +/- {wilson_halfwidth(p, 100) * 100:.1f} points")
    out.append(f"   simulated cell at 200 -> +/- {wilson_halfwidth(0.5, 200) * 100:.1f} points")

    out.append("B. A/B comparison, INDEPENDENT arms (alpha 0.05 two-sided, 80 percent power),"
               " trials per arm:")
    for a, b in ((0.5, 0.7), (0.5, 0.65), (0.5, 0.6)):
        out.append(f"  {a:.0%} vs {b:.0%} -> {n_per_arm(a, b):.0f}")
    out.append("C. A/B comparison, MATCHED PAIRS (McNemar, alpha 0.05, 80 percent power),"
               " 50 vs 70 percent, pairs per arm by discordance:")
    for d in (0.2, 0.3, 0.4, 0.5):
        e = n_pairs_mcnemar(0.5, 0.7, d)
        tail = "  (pairing buys nothing; equals the independent count)" if d == 0.5 else ""
        out.append(f"  discordance {d:.1f} -> {e:.1f} -> {math.ceil(e)} pairs per arm,"
                   f" {2 * math.ceil(e)} rollouts{tail}")

    out.append("D. Ratio to an unperturbed anchor (log-ratio standard error):")
    rr, lo, hi = logratio_ci(0.5, 0.3, 40)
    out.append(f"  anchor 0.50, perturbed 0.30, n = 40 each -> RR = {rr:.2f},"
               f" 95 percent CI {lo:.2f} to {hi:.2f}  (contains 1)")
    out.append(f"  same drop at 80 percent power -> n = {math.ceil(n_for_ratio(0.5, 0.3))} per arm")

    out.append("E. Paired correlation (Fisher z):")
    lo, hi = rho_ci(0.70, 100)
    out.append(f"  rho = 0.70 on 100 pairs -> 95 percent CI {lo:.2f} to {hi:.2f}")
    for h in (0.10, 0.05):
        out.append(f"  both limits within {h:.2f} of rho = 0.70 -> n = {n_for_rho(0.70, h)} pairs")

    out.append("F. Held-out objects, resampling unit the object (Bernoulli per object):")
    out.append(f"  20 objects -> +/- {wilson_halfwidth(0.5, 20) * 100:.1f} points;"
               f" 10-point claim -> {n_for_halfwidth(0.10)} objects")

    out.append("G. Continuous score, half-width in standard deviations:")
    for n in (30, 100):
        out.append(f"  n = {n} rollouts -> +/- {Z / math.sqrt(n):.2f} sd")

    pairs, matched, unseen, total, old = bill()
    out.append(f"H. Bill for {POLICIES} policies on {TASKS} tasks, at the paired count"
               f" (discordance {DISC:.1f}):")
    out.append(f"  matched set  {POLICIES} x {TASKS} x {pairs} = {matched} real rollouts")
    out.append(f"  unseen set   {POLICIES} x {TASKS} x 100 = {unseen} real rollouts")
    out.append(f"  total {total} rollouts = {total / 60:.1f} h at one minute each"
               f"  (was {old} = {old / 60:.1f} h on the independent-arm count)")
    return "\n".join(out)


def table8() -> str:
    pairs, matched, unseen, total, old = bill()
    rr, lo, hi = logratio_ci(0.5, 0.3, 40)
    rlo, rhi = rho_ci(0.70, 100)
    n_ratio = math.ceil(n_for_ratio(0.5, 0.3))
    n_rho = n_for_rho(0.70, 0.05)
    return f"""### Table 8. The proposed evaluation protocol

| axis | what is measured | how | minimum trial count | reported alongside it | why |
|---|---|---|---|---|---|
| Task success | fraction of episodes meeting a criterion, and a graded rubric score in [0,1] over equally weighted milestones | criterion written before the run by the designer and scored by someone else; terminal predicate held for a 0.5 s dwell; initial conditions matched by image overlay; policies interleaved blind in one session | 100 real and 200 sim per policy per task per condition for an absolute rate at a 10-point interval; a comparison alone needs {pairs} matched pairs per arm (McNemar, 50 against 70 percent, discordance {DISC:.1f}) | raw counts, the criterion verbatim, the rubric, the initial-condition protocol, and an interval whose kind is named: Wilson for a cell run to a fixed n, an anytime-valid confidence sequence (WSR, as in `beyond_binary_success_2026`) for a cell stopped early by a sequential test, because a Wilson interval computed at a data-dependent stopping time is not a 95 percent interval. Intervals are marginal, not simultaneous: a paper comparing k policies corrects its k(k&minus;1)/2 pairwise tests to a global 95 percent level, as `lbm_careful_examination_2025` does, or says it has not | a rate without a denominator and an interval cannot be compared; the rubric separates a near-miss from inaction; the design is paired, so the count that governs it is paired |
| Robustness | success under each perturbation axis as an absolute rate; the ratio to the unperturbed anchor is reported descriptively and is not tested at the screening count | axes that must not change the action and axes that must are scored separately; ranges stated; anchor replayed exactly | 40 per axis per policy in sim to rank the axes; {n_ratio} per axis and {n_ratio} at the anchor before any claim that a named axis hurt | both absolute rates with their Wilson intervals, the ratio without an interval unless the certifying count was run, the axis ranges, and which split each axis is in | the ranking at the anchor is not the ranking under shift; at 40 per arm a fall from 0.50 to 0.30 is a ratio of {rr:.2f} with a 95 percent interval of {lo:.2f} to {hi:.2f}, which contains 1 |
| Unseen objects | mean over held-out objects of per-object success | objects drawn from a stated distribution disjoint from training; bootstrap over objects, not trials | 20 objects at 5 trials for a screening claim; 93 objects for a 10-point claim | the object list, per-object rates, the bootstrap interval, the object-count caveat, and the within-object trial count, since the 93 is a Wilson width that treats one object as one Bernoulli draw | the resampling unit is the object, so trial counts overstate the precision |
| Physical plausibility | maximum and mean hand-object penetration depth per rollout, and the fraction of frames above 2 mm | dense surface sample against the object mesh or SDF, computed on the policy's own rollouts by code that never entered the reward or the termination rule | 100 rollouts, simulation only | interval over rollouts, sample density, threshold, solver depenetration settings, and at least one rendered rollout | a measure the policy optimised is not evidence about the policy |
| Sample and wall-clock cost | environment steps and wall-clock to the checkpoint that produced the headline number | counted to that checkpoint, not to the end of training; GPU model and count stated | 3 training seeds | the range over seeds, and the statement that 3 seeds is a range and not an interval | training variance is not rollout variance and the two are routinely conflated |
| Real-robot transfer | paired real and simulated outcomes on matched initial conditions, their correlation, and the rectifier variance against the variance of the real evaluation | the same 100 initial conditions run in both; correlation on the pairs; variance ratio bootstrapped over the same pairs | the 100 real trials paired to 100 sim, which fixes the correlation to about &plusmn;0.10; about {n_rho} pairs for a claim that separates two correlations 0.1 apart | the correlation with its Fisher-z interval, the variance ratio with its bootstrap interval, and which of the two decisions the count supports | a simulator earns a real-world claim only through its measured paired correlation; at 100 pairs &rho;&#770; = 0.70 carries {rlo:.2f} to {rhi:.2f}, enough to say a simulator tracks reality at all and not enough to separate `suresim_2025`'s 0.70 regime from its 0.59 one |
| Reproducibility | code, checkpoints, and the exact config that produced the headline run | diff the paper's stated objective against the released config and name the file and line of every disagreement | not a trial count | the named file and line for each disagreement, or an explicit statement that none was found | 16 of the 62 code-releasing method rows carry a true contradiction between the paper's stated objective and the released code, and 38 carry a recorded disagreement of any kind (&sect;5.8) |
"""


def method_name(key: str) -> str:
    first = open(R / f"papers/notes/{key}.md", errors="ignore").readline()
    m = re.match(r"#\s*\S+\s+—\s*(.+)", first)
    return re.split(r"[:(,]", m.group(1))[0].strip() if m else key


def table9_rows():
    """Rank the corpus's dexterous-hand policy methods by whole-word mentions in other papers."""
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
        tags = set(r.get("paradigm") or [])
        if not (tags & POLICY_TAGS) or INTERFACE_TAG in tags:
            continue
        hand = r["hand"].lower()
        if "parallel" in hand or "gripper" in hand:
            continue
        name = method_name(r["key"])
        if len(name) < 4:
            continue
        # Whole word: no alphanumeric on the left, and no alphanumeric, + or - on the right, so
        # "UniDex" does not match inside "UniDexGrasp" or "UniDexGrasp++".
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(name.lower()) + r"(?![A-Za-z0-9+-])")
        n = sum(1 for k, t in texts.items() if k != r["key"] and pat.search(t))
        # A name with no space is the work's short name, matched in running text; a name with a
        # space is its title, matched mostly inside reference lists. The two have different base
        # rates, so the kind travels with the count.
        scored.append((n, r["key"], name, "short name" if " " not in name else "title"))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[:ROW_COUNT]


def main():
    if "--derive" in sys.argv:
        print(derivation())
        return
    outdir = R / "paper/tables"
    outdir.mkdir(exist_ok=True)
    (outdir / "table8_protocol.md").write_text(table8())

    picked = table9_rows()
    head = "| method | " + " | ".join(AXES) + " |"
    rule = "|" + "|".join(["---"] * (len(AXES) + 1)) + "|"
    body = [f"| `{k}`{'&#10035;' if kind == 'title' else ''} |" + " |" * len(AXES)
            for _, k, _, kind in picked]
    body.insert(0, "| " + " | ".join(EXAMPLE) + " |")
    cells = len(picked) * len(AXES)
    counts = "; ".join(f"`{k}` {n}" for n, k, _, _ in picked)
    txt = ("### Table 9. The matrix, for someone else to fill\n\n"
           + "\n".join([head, rule] + body)
           + f"\n\n*{len(picked)} rows, {cells} cells, all {cells} empty; the first row is a "
             "worked example and every number in it is fabricated. Rows are the "
             f"{len(picked)} most-mentioned dexterous-hand policy methods in the corpus, by the "
             "rule in §7.6, scored on whole-word matches over `papers/md`: "
           + counts
           + ". Mention counts are counts of mentions, not of use. &#10035; marks a work matched "
             "on its title rather than a short name; a title is matched mostly inside reference "
             "lists and a short name in running text, so the two kinds of count are not "
             "comparable with each other.*\n")
    (outdir / "table9_matrix.md").write_text(txt)
    print("wrote table8_protocol.md and table9_matrix.md")
    for n, k, name, kind in picked:
        print(f"  {n:3d} {k:32s} {name[:44]:46s} [{kind}]")


if __name__ == "__main__":
    main()
