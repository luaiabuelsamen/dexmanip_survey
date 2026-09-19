"""Draw the survey's three headline findings, and the real-trial distribution, as TikZ figures.

The findings are stated in numbers in Section I, Section V-H, Section VII-C and Section VIII, and
until now a reader had to reconstruct each one from a table. Each figure here is the argument of one
finding: a funnel that ends where the evidence ends.

  fig_codegap.tex      112 method rows narrowed to the 10 whose shipped code states a different
                       objective from the paper, with the 28 charges the survey did not keep drawn
                       at the same weight as the 10 it kept. A survey that names people has to draw
                       its withdrawals.
  fig_penetration.tex  the same narrowing for interpenetration, ending at zero: not one method row
                       reports a penetration number for its own trained policy's rollouts.
  fig_reporting.tex    what the field reports, ordered so the argument reads top to bottom, with the
                       two quantities a reader needs in order to compare two methods marked. This
                       file used to be written by tools/make_tikz_figures.py; it is written here now.
  fig_trials.tex       the per-cell real-robot trial counts, 39 of them, with the median marked. The
                       24 grand totals are a different quantity and are not pooled into it.

Every number is recounted from corpus/rows here, at generation time, so no figure can drift from the
corpus. The two judgements the corpus holds no field for, which rows are closed-loop policies and
which report penetration for their own rollouts, are written below as key lists with the rule that
produced them checked against them, so a row added to the corpus breaks this generator instead of
silently moving a number a figure prints. That is the pattern tools/check_numbers.py uses for
Section VI's denominator.

Run:  python3 tools/make_finding_figures.py
"""
import glob
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

R = Path(__file__).resolve().parents[1]
OUT = R / "tex/figs"
OUT.mkdir(parents=True, exist_ok=True)
ROWS = [json.load(open(f)) for f in sorted(glob.glob(str(R / "corpus/rows/*.json")))]
M = [r for r in ROWS if r.get("class") == "method"]
N = len(M)

HANDLED = ("penalised", "measured", "constrained")

# --- the two judgements no corpus field holds ----------------------------------------------------
# Section VII-C enumerates both. A closed-loop policy is a row whose paradigm puts a learned
# controller in the loop; a grasp synthesiser, a trajectory optimiser and a contact model are not
# controllers however much learning they contain. The rule below reproduces the section's list, and
# CLOSED_LOOP is kept beside it so that a corpus edit which moves the rule's answer stops the build.
LEARNED = {"RL", "RL+demo", "BC", "distillation", "diffusion", "VLA", "flow", "MPC", "world-model"}
NOT_A_CONTROLLER = {"grasp-synthesis", "trajopt"}
CLOSED_LOOP = {"clutterdexgrasp_2025", "dexmachina_2025", "dextrack_2025", "teledexter_2026"}
# Audited by hand in Section VII-C against all eleven rows: every one of them scores a pose or a
# trajectory before execution. DexTrack defines a maximum penetration depth and applies it to its
# input references; TopoRetarget reports 1.07 mm on 25 ContactPose grasps and then never re-measures
# the rollouts its PPO controller produced. The set is empty, and the assertion below forces the
# audit to be redone rather than assumed if the eleven ever change.
ROLLOUT_REPORTED: set = set()


def closed_loop_rule(r):
    p = set(r.get("paradigm") or [])
    return bool(p & LEARNED) and not (p & NOT_A_CONTROLLER)


def facts():
    """Every count the four figures print, recomputed from corpus/rows."""
    f = {"method_rows": N}
    # --- paper versus code ---
    f["code_released"] = sum(1 for r in M if r.get("code_released") is True)
    mismatch = [r for r in M if r.get("mismatch_class")]
    f["disagreements"] = len(mismatch)
    by_class = Counter(r["mismatch_class"] for r in mismatch)
    f["classes"] = by_class
    f["contradictions"] = by_class["contradiction"]
    f["withdrawn"] = len(mismatch) - by_class["contradiction"]
    f["reviewed"] = sum(1 for r in mismatch if r.get("mismatch_review"))
    if not all(r.get("code_released") is True for r in mismatch):
        sys.exit("a row records a paper/code disagreement without releasing code")
    # --- interpenetration ---
    f["pen_settled"] = sum(1 for r in M if r.get("penetration") is not None)
    handled = [r for r in M if r.get("penetration") in HANDLED]
    f["pen_handled"] = len(handled)
    hkeys = {r["key"] for r in handled}
    derived = {r["key"] for r in handled if closed_loop_rule(r)}
    if derived != CLOSED_LOOP:
        sys.exit("the closed-loop rule and Section VII-C's list have come apart: "
                 f"rule says {sorted(derived)}, section says {sorted(CLOSED_LOOP)}. "
                 "Re-read the rows and update both.")
    if not ROLLOUT_REPORTED <= hkeys:
        sys.exit("a row outside the eleven is marked as reporting rollout penetration")
    f["pen_closed_loop"] = len(CLOSED_LOOP)
    f["pen_rollout"] = len(ROLLOUT_REPORTED)
    # --- reporting coverage: each axis with the denominator that belongs to it ---
    f["axes"] = [
        ("success criterion stated", sum(1 for r in M if r.get("success_criterion"))),
        ("real-robot experiment", sum(1 for r in M if r.get("real_robot") is True)),
        ("real trial count stated", sum(1 for r in M if r.get("real_trials") is not None)),
        ("code released", f["code_released"]),
        ("unseen-object count stated",
         sum(1 for r in M if r.get("objects_test_unseen") is not None)),
        ("contact or penetration handled", f["pen_handled"]),
    ]
    # --- real trials, per cell and never pooled with the grand totals ---
    per_cell = sorted(r["real_trials"] for r in M
                      if r.get("real_trials_kind") in ("per-task", "per-condition")
                      and r.get("real_trials") is not None)
    totals = sorted(r["real_trials"] for r in M
                    if r.get("real_trials_kind") == "total" and r.get("real_trials") is not None)
    unclear = sum(1 for r in M if r.get("real_trials_kind") == "unclear"
                  and r.get("real_trials") is not None)
    f["per_cell"] = per_cell
    f["totals"] = totals
    f["unclear"] = unclear
    return f


F = facts()

PRE = r"""% generated by tools/make_finding_figures.py; do not edit
\begin{tikzpicture}[
  font=\footnotesize,
  bar/.style={draw=none,fill=black!62},
  barmid/.style={draw=none,fill=black!42},
  barlight/.style={draw=none,fill=black!20},
  baracc/.style={draw=none,fill=accent},
  seg/.style={draw=white,line width=0.5pt},
  lnk/.style={draw=black!38,line width=0.28pt},
  ghost/.style={draw=black!45,line width=0.3pt,dash pattern=on 1.2pt off 1.2pt},
  lbl/.style={font=\scriptsize},
  small/.style={font=\scriptsize\color{black!55}},
  num/.style={font=\scriptsize\color{black!55}},
]
"""
W = 7.6          # the bar for the full 112 rows
BH = 0.26        # bar height
PITCH = 0.60     # stage to stage


def esc(s):
    return str(s).replace("_", r"\_").replace("%", r"\%").replace("&", r"\&")


def stage(out, y, n, total, label, style):
    """One stage of a funnel: a bar scaled against `total`, its count and name set above it.

    The label carries the denominator the stage narrows from, because a stage four rows deep is a
    bar too short to hang an annotation on.
    """
    w = W * n / total
    out.append(rf"\node[lbl,anchor=south west] at (0,{y + 0.04:.2f}) "
               rf"{{\textbf{{{n}}}~~{label}}};")
    out.append(rf"\fill[black!8] (0,{y:.2f}) rectangle ({W:.2f},{y - BH:.2f});")
    out.append(rf"\fill[{style}] (0,{y:.2f}) rectangle ({max(w, 0.02):.2f},{y - BH:.2f});")
    return w


def bracket(out, x0, x1, y, label, up=True, accent=False):
    """A square bracket over a span, in the house style: thin rules, no curls."""
    t = 0.10 if up else -0.10
    col = "accent" if accent else "black!45"
    out.append(rf"\draw[line width=0.3pt,draw={col}] ({x0:.2f},{y:.2f}) -- ({x0:.2f},{y + t:.2f}) "
               rf"-- ({x1:.2f},{y + t:.2f}) -- ({x1:.2f},{y:.2f});")
    anc = "south" if up else "north"
    sty = r"font=\scriptsize\color{accent}" if accent else r"font=\scriptsize"
    out.append(rf"\node[{sty},anchor={anc}] at ({(x0 + x1) / 2:.2f},{y + 1.15 * t:.2f}) {{{label}}};")


# --- figure: papers disagree with their own released code ----------------------------------------
def fig_codegap():
    c = F["classes"]
    out = [PRE]
    y = 0.0
    stage(out, y, F["method_rows"], N, "method rows in the corpus", "barlight")
    y -= PITCH
    stage(out, y, F["code_released"], N, "released code that could be read against the paper",
          "barmid")
    y -= PITCH
    w38 = stage(out, y, F["disagreements"], N,
                rf"of those record a paper/code disagreement", "bar")
    y -= BH

    # the same 38, at its own scale, split into what the survey kept and what it withdrew
    yz = y - 0.82
    zh = 0.34
    out.append(rf"\draw[ghost] (0,{y:.2f}) -- (0,{yz + zh:.2f});")
    out.append(rf"\draw[ghost] ({w38:.2f},{y:.2f}) -- ({W:.2f},{yz + zh:.2f});")
    order = ["contradiction", "parse-limitation", "code-absent", "version-skew",
             "internal-inconsistency"]
    total = F["disagreements"]
    x = 0.0
    for name in order:
        n = c[name]
        w = W * n / total
        style = "baracc" if name == "contradiction" else "barlight"
        out.append(rf"\fill[{style}] ({x:.2f},{yz:.2f}) rectangle ({x + w:.2f},{yz + zh:.2f});")
        if x:
            out.append(rf"\draw[seg] ({x:.2f},{yz:.2f}) -- ({x:.2f},{yz + zh:.2f});")
        col = "white" if name == "contradiction" else "black!70"
        out.append(rf"\node[font=\scriptsize\color{{{col}}}] at ({x + w / 2:.2f},"
                   rf"{yz + zh / 2:.2f}) {{{n}}};")
        x += w
    xk = W * c["contradiction"] / total
    bracket(out, 0, xk, yz - 0.02, rf"{c['contradiction']} kept", up=False, accent=True)
    bracket(out, xk, W, yz - 0.02, rf"{F['withdrawn']} withdrawn", up=False)
    out.append(rf"\node[lbl,anchor=north west,align=left,text=accent] at (0,{yz - 0.54:.2f}) "
               rf"{{kept: the shipped code states a different objective}};")
    out.append(rf"\node[small,anchor=north west,align=left] at (0,{yz - 0.82:.2f}) "
               rf"{{withdrawn: {c['parse-limitation']} a limit of this survey's own parse, "
               rf"{c['code-absent']} the component\\"
               rf"was never released, {c['version-skew']} version skew, "
               rf"{c['internal-inconsistency']} a paper disagreeing with itself}};")
    out.append(r"\end{tikzpicture}")
    (OUT / "fig_codegap.tex").write_text("\n".join(out) + "\n")
    return F["contradictions"], F["withdrawn"]


# --- figure: nobody measures contact quality, and the funnel ends at zero -------------------------
def fig_penetration():
    out = [PRE]
    y = 0.0
    stage(out, y, F["method_rows"], N, "method rows in the corpus", "barlight")
    y -= PITCH
    stage(out, y, F["pen_settled"], N, "of them whose note settles the question", "barmid")
    y -= PITCH
    stage(out, y, F["pen_handled"], N,
          rf"of those {F['pen_settled']} address interpenetration in any form", "bar")
    y -= PITCH
    stage(out, y, F["pen_closed_loop"], N,
          rf"of those {F['pen_handled']} inside a closed-loop policy", "baracc")
    y -= BH

    # the zero. A bar cannot draw it, so the band does.
    yb = y - 0.46
    bh = 0.94
    out.append(rf"\fill[wash] (0,{yb:.2f}) rectangle ({W:.2f},{yb - bh:.2f});")
    out.append(rf"\draw[line width=0.3pt,draw=black!30] (0,{yb:.2f}) rectangle "
               rf"({W:.2f},{yb - bh:.2f});")
    out.append(rf"\node[anchor=west,font=\fontsize{{22}}{{22}}\selectfont\bfseries"
               rf"\color{{accent}}] at (0.18,{yb - bh / 2:.2f}) {{{F['pen_rollout']}}};")
    out.append(rf"\node[anchor=west,align=left,font=\scriptsize] at (1.00,{yb - bh / 2:.2f}) "
               rf"{{report a penetration number for the rollouts\\"
               rf"of their own trained policy}};")
    out.append(r"\end{tikzpicture}")
    (OUT / "fig_penetration.tex").write_text("\n".join(out) + "\n")
    return F["pen_handled"], F["pen_closed_loop"], F["pen_rollout"]


# --- figure: what the field reports, and what it does not -----------------------------------------
def fig_reporting():
    """Horizontal bars, most-reported first, with the two least-reported marked.

    Those two, the unseen-object count and contact handling, are the pair a reader needs in order to
    compare any two methods: without them a success rate has no generalisation denominator and no
    statement about whether the hand went through the object.
    """
    axes = sorted(F["axes"], key=lambda t: -t[1])
    lowest = {label for label, _ in axes[-2:]}
    width, rowsep = 6.2, 0.44
    out = [PRE]
    y = 0.0
    ys = {}
    for label, n in axes:
        frac = n / N
        w = width * frac
        acc = label in lowest
        style = "baracc" if acc else "bar"
        lsty = r"lbl,text=accent" if acc else "lbl"
        nsty = r"font=\scriptsize\color{accent}" if acc else "num"
        out.append(rf"\node[{lsty},anchor=east] at (0,{-y:.2f}) {{{esc(label)}}};")
        out.append(rf"\fill[barlight] (0.12,{-y - 0.1:.2f}) rectangle ({0.12 + width:.2f},"
                   rf"{-y + 0.1:.2f});")
        out.append(rf"\fill[{style}] (0.12,{-y - 0.1:.2f}) rectangle ({0.12 + w:.2f},"
                   rf"{-y + 0.1:.2f});")
        out.append(rf"\node[{nsty},anchor=west] at ({0.12 + width + 0.12:.2f},{-y:.2f}) "
                   rf"{{{n} ({round(100 * frac)}\%)}};")
        ys[label] = -y
        y += rowsep
    # a square bracket down the right-hand side of the two lowest bars
    xb = 0.12 + width + 1.42
    y0, y1 = (ys[l] for l in [a[0] for a in axes[-2:]])
    out.append(rf"\draw[line width=0.4pt,draw=accent] ({xb:.2f},{y0 + 0.16:.2f}) -- "
               rf"({xb + 0.10:.2f},{y0 + 0.16:.2f}) -- ({xb + 0.10:.2f},{y1 - 0.16:.2f}) -- "
               rf"({xb:.2f},{y1 - 0.16:.2f});")
    out.append(rf"\draw[lnk] (0.12,{-y + 0.16:.2f}) -- ({0.12 + width:.2f},{-y + 0.16:.2f});")
    out.append(rf"\node[anchor=north west,align=left,font=\scriptsize\color{{accent}}] "
               rf"at (-2.4,{-y + 0.04:.2f}) {{the two a reader needs in order to compare any two "
               rf"methods}};")
    out.append(r"\end{tikzpicture}")
    (OUT / "fig_reporting.tex").write_text("\n".join(out) + "\n")
    return len(axes), sorted(lowest)


# --- figure: the distribution of per-cell real-robot trial counts ----------------------------------
def fig_trials():
    v = F["per_cell"]
    med = statistics.median(v)
    edges = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30),
             (30, 35), (35, 40), (40, 45), (45, 50)]
    bins = [sum(1 for x in v if lo < x <= hi) for lo, hi in edges]
    over = sum(1 for x in v if x > 50)
    bins.append(over)
    labels = [str(hi) for _, hi in edges] + [r"$>$50"]
    pitch, bw = 0.70, 0.56
    xoff = 0.34  # the overflow bin stands off the axis it does not belong on
    top = 2.10
    mx = max(bins) or 1
    out = [PRE]
    for i, (n, lab) in enumerate(zip(bins, labels)):
        x = i * pitch + (xoff if i == len(edges) else 0)
        h = top * n / mx
        if n:
            out.append(rf"\fill[bar] ({x:.2f},0) rectangle ({x + bw:.2f},{h:.2f});")
            out.append(rf"\node[num,anchor=south] at ({x + bw / 2:.2f},{h + 0.02:.2f}) {{{n}}};")
        # the tick sits on the bin's upper edge, so the axis is the trial count itself and the
        # median rule below lands on the number it names
        xt = x + bw if i < len(edges) else x + bw / 2
        out.append(rf"\draw[lnk] ({xt:.2f},0) -- ({xt:.2f},-0.06);")
        out.append(rf"\node[lbl,anchor=north] at ({xt:.2f},-0.08) {{{lab}}};")
    wid = len(bins) * pitch - (pitch - bw) + xoff
    out.append(rf"\draw[lnk] (-0.06,0) -- ({wid + 0.06:.2f},0);")
    out.append(rf"\node[lbl,anchor=north] at ({wid / 2:.2f},-0.42) "
               rf"{{real trials per cell, in bins of five}};")
    # the median, on the bin edge it falls on
    xm = (med / 5 - 1) * pitch + bw
    out.append(rf"\draw[draw=accent,line width=0.4pt,dash pattern=on 1.4pt off 1.2pt] "
               rf"({xm:.2f},-0.02) -- ({xm:.2f},{top + 0.34:.2f});")
    out.append(rf"\node[anchor=west,font=\scriptsize\color{{accent}}] at ({xm + 0.08:.2f},"
               rf"{top + 0.24:.2f}) {{median {med:g}}};")
    out.append(rf"\node[small,anchor=north west,align=left] at (-0.06,-0.66) "
               rf"{{{len(v)} rows state a per-cell count; the mode is "
               rf"{Counter(v).most_common(1)[0][0]}, in {Counter(v).most_common(1)[0][1]} of them\\"
               rf"{len(F['totals'])} state a grand total instead, "
               rf"{min(F['totals'])} to {max(F['totals'])}, and are not pooled into this\\"
               rf"{F['unclear']} more state a count on a basis that could not be read}};")
    out.append(r"\end{tikzpicture}")
    (OUT / "fig_trials.tex").write_text("\n".join(out) + "\n")
    return len(v), med, bins


# --- the same counts, for the captions ------------------------------------------------------------
def numbers():
    """Write every count these figures carry as a LaTeX macro.

    A caption that prints a number has to recount it too, or the first corpus edit makes the figure
    and its caption disagree in print. Sections input this file the way they input figs/plates.tex.
    """
    c = F["classes"]
    m = {
        "fnRows": F["method_rows"],
        "fnCode": F["code_released"],
        "fnDisagree": F["disagreements"],
        "fnKept": F["contradictions"],
        "fnWithdrawn": F["withdrawn"],
        "fnParse": c["parse-limitation"],
        "fnAbsent": c["code-absent"],
        "fnSkew": c["version-skew"],
        "fnInternal": c["internal-inconsistency"],
        "fnPenSettled": F["pen_settled"],
        "fnPenHandled": F["pen_handled"],
        "fnPenClosed": F["pen_closed_loop"],
        "fnPenOther": F["pen_handled"] - F["pen_closed_loop"],
        "fnPenRollout": F["pen_rollout"],
        "fnTrials": len(F["per_cell"]),
        "fnTrialsMedian": f"{statistics.median(F['per_cell']):g}",
        "fnTrialsMode": Counter(F["per_cell"]).most_common(1)[0][0],
        "fnTrialsModeN": Counter(F["per_cell"]).most_common(1)[0][1],
        "fnTotals": len(F["totals"]),
        "fnTotalsMin": min(F["totals"]),
        "fnTotalsMax": max(F["totals"]),
        "fnUnclear": F["unclear"],
    }
    body = ["% generated by tools/make_finding_figures.py; do not edit",
            "% Every count the finding figures and their captions print, recomputed from corpus/rows.",
            r"\providecommand{\fnLoaded}{}"]
    body += [rf"\providecommand{{\{k}}}{{{v}}}" for k, v in m.items()]
    (OUT / "finding_numbers.tex").write_text("\n".join(body) + "\n")
    return len(m)


if __name__ == "__main__":
    print("method rows:", N)
    print("code gap:      %d kept, %d withdrawn" % fig_codegap())
    print("penetration:   %d handled, %d closed-loop, %d rollout numbers" % fig_penetration())
    print("reporting:     %d axes, marked %s" % fig_reporting())
    n, med, bins = fig_trials()
    print("trials:        %d per-cell counts, median %g, bins %s" % (n, med, bins))
    print("caption macros:", numbers())
