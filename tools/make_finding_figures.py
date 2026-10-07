"""Draw the survey's three headline findings, and the real-trial distribution, as TikZ figures.

The findings are stated in numbers in Section I, Section V-H, Section VII-C and Section VIII, and
until now a reader had to reconstruct each one from a table. Each figure here is the argument of one
finding: a funnel that ends where the evidence ends.

  fig_codegap.tex      113 method rows narrowed to the 8 whose shipped code states a different
                       objective from the paper, with the 31 disagreements that fall in the four
                       other classes drawn at the same weight as the 8 contradictions. Those 31 are
                       not retractions: the accusations this survey withdrew are counted separately,
                       in each accused row's `mismatch_review` field.
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
CLOSED_LOOP = {"clutterdexgrasp_2025", "dexmachina_2025", "dextrack_2025", "dgrasp_2022",
               "teledexter_2026"}
# Audited by hand in Section VII-C against all twelve rows. Four of the five closed-loop policies
# score a pose or a trajectory before execution: DexTrack defines a maximum penetration depth and
# applies it to its input references, and TopoRetarget reports 1.07 mm on 25 ContactPose grasps and
# then never re-measures the rollouts its PPO controller produced. D-Grasp is the near case and the
# reason this set is a set rather than a boolean. It does report a volume for a pose its own policy
# reached, so it is not scoring someone else's reference, but the measurement is one frame rather
# than a rollout and it is taken outside the physics, on the original MANO mesh and the
# full-resolution object mesh, "no physical simulation involved" (its Sec. B.3), while inside the
# simulation the paper reports zero. It therefore does not report what this set counts, and the set
# stays empty. The assertion below forces the audit to be redone rather than assumed if the twelve
# ever change.
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
    # Not "withdrawn": these are the four other classes of disagreement, and most were never
    # charged as contradictions at all. The accusations the survey did withdraw are counted in
    # `mismatch_review` and named in section 8.1; a figure that called these 31 withdrawn
    # mislabelled the survey's own ledger.
    f["other_class"] = len(mismatch) - by_class["contradiction"]
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
        sys.exit("a row outside the twelve is marked as reporting rollout penetration")
    f["pen_closed_loop"] = len(CLOSED_LOOP)
    f["pen_rollout"] = len(ROLLOUT_REPORTED)
    # --- reporting coverage: each axis with the denominator that belongs to it ---
    # (label, stated, denominator, rows the note did not settle). Four of the six denominators are
    # not 112, and the figure used to draw all six against 112 while Section VII-A quoted these:
    # the bars then printed 79, 62, 55 and 10 per cent where the prose beside them said 80, 79, 57
    # and 11. A row with no real robot cannot state a real trial count, so that share is against
    # the 89 that have one; `real_robot`, `code_released` and `penetration` carry nulls that mean
    # the note did not settle the question rather than "no", so those shares are against the rows
    # it did settle, with the unsettled rows drawn as a tail beyond the track. The markdown
    # edition's Figure 6 has always been drawn this way; tools/check_numbers.py now pins both.
    real = sum(1 for r in M if r.get("real_robot") is True)
    real_settled = sum(1 for r in M if r.get("real_robot") is not None)
    code_settled = sum(1 for r in M if r.get("code_released") is not None)
    f["axes"] = [
        ("success criterion stated", sum(1 for r in M if r.get("success_criterion")), N, 0),
        ("real-robot experiment", real, real_settled, N - real_settled),
        ("real trial count stated", sum(1 for r in M if r.get("real_trials") is not None),
         real, 0),
        ("code released", f["code_released"], code_settled, N - code_settled),
        ("unseen-object count stated",
         sum(1 for r in M if r.get("objects_test_unseen") is not None), N, 0),
        ("contact or penetration handled", f["pen_handled"], f["pen_settled"],
         N - f["pen_settled"]),
    ]
    trials_off_real = sum(1 for r in M if r.get("real_trials") is not None
                          and r.get("real_robot") is not True)
    if trials_off_real:
        sys.exit(f"{trials_off_real} rows state a real trial count with no real robot, so 89 is "
                 "not the denominator Section VII-A gives for that share")
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
W = 7.6          # the bar for the full 113 rows
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


# --- figure: papers disagree with their own released code ----------------------------------------
def funnel(out, steps, w, x0=0.0, y0=0.0, bh=0.52, gap=0.26, labx=None):
    """A funnel that narrows: centred bands whose width is the count, joined by sloping wedges.

    `steps` is [(count, label, fill)], widest first, each band's width proportional to its count
    against the first. The wedge between two bands is the drop, so the reader sees what is lost
    rather than reading two numbers. Returns the y of the last band's bottom edge and its width.
    """
    top = steps[0][0]
    y = y0
    prev = None
    for n, label, fill in steps:
        bw = w * n / top
        cx = x0 + w / 2
        l, r = cx - bw / 2, cx + bw / 2
        if prev is not None:
            pl, pr, py = prev
            out.append(rf"\fill[black!7] ({pl:.2f},{py:.2f}) -- ({pr:.2f},{py:.2f}) -- "
                       rf"({r:.2f},{y:.2f}) -- ({l:.2f},{y:.2f}) -- cycle;")
        out.append(rf"\fill[{fill}] ({l:.2f},{y:.2f}) rectangle ({r:.2f},{y - bh:.2f});")
        dark = fill != "barlight"
        col = "white" if dark else "black!75"
        out.append(rf"\node[font=\small\bfseries\color{{{col}}}] at ({cx:.2f},{y - bh / 2:.2f}) "
                   rf"{{{n}}};")
        out.append(rf"\node[lbl,anchor=west,align=left] at ({labx:.2f},{y - bh / 2:.2f}) {{{label}}};")
        prev = (l, r, y - bh)
        y -= bh + gap
    return prev[2], prev[1] - prev[0]


def unit_strip(out, y, x0, x1, n, n_hit, h=0.42, gap_frac=0.30):
    """`n` tick marks, one per case, the first `n_hit` accented.

    The last step of the funnel is the one the survey stands behind, and it is too small a slice
    to read off a bar. Drawn one mark per paper it can be counted, and the accented run is the
    finding at a glance. Nothing here is drawn twice: the marks are the only picture of the 38.
    """
    span = x1 - x0
    pitch = span / n
    tw = pitch / (1 + gap_frac)
    for i in range(n):
        x = x0 + i * pitch
        sty = "baracc" if i < n_hit else "barlight"
        out.append(rf"\fill[{sty}] ({x:.2f},{y:.2f}) rectangle ({x + tw:.2f},{y - h:.2f});")
    return x0 + n_hit * pitch - (pitch - tw)


def fig_codegap():
    """113 papers, 63 with readable code, 39 that disagree with it, 8 of them contradictions.

    Four quantities, each drawn once. The funnel narrows because a band's width is its count;
    the final split is a strip of 39 marks rather than a fourth band, because 8 of 113 is a
    slice too thin to see and the last step is the one the argument rests on.
    """
    c = F["classes"]
    fw = 4.90          # the funnel, left of the label column
    labx = 5.20        # labels start here, clear of the widest band
    out = [PRE]
    ybot, wlast = funnel(out, [
        (F["method_rows"], "method papers\\\\in the corpus", "barlight"),
        (F["code_released"], "released code that could\\\\be read against the paper", "barmid"),
        (F["disagreements"], "disagree with their\\\\own code somehow", "bar"),
    ], w=fw, labx=labx)

    # the 38, one mark each, with the 9 the survey stands behind at the head of the run
    ys = ybot - 0.66
    c = F["classes"]
    # the same 38, re-opened at its own scale: a wash fan rather than a leader line, so the strip
    # is visibly the last band magnified and not a fourth, separate count
    out.append(rf"\fill[black!5] ({(fw - wlast) / 2:.2f},{ybot:.2f}) -- "
               rf"({(fw + wlast) / 2:.2f},{ybot:.2f}) -- ({W:.2f},{ys:.2f}) -- (0,{ys:.2f}) -- cycle;")
    out.append(rf"\node[anchor=south east,font=\scriptsize\color{{black!45}}] at "
               rf"({W:.2f},{ys + 0.06:.2f}) {{one mark, one paper}};")
    unit_strip(out, ys, 0.0, W, F["disagreements"], F["contradictions"])
    yt = ys - 0.42 - 0.14
    out.append(rf"\draw[lnk] (0,{yt + 0.08:.2f}) -- ({W:.2f},{yt + 0.08:.2f});")
    # The label inside a graphic travels further than the caption under it, so it says only what is
    # true of all nine. "A different objective" was true of most and too strong for DeXtreme, where
    # the difference is one penalty weight of -0.25 against -0.2, so the label states the form the
    # finding actually takes: a value or a term, paper against shipped code.
    out.append(rf"\node[anchor=north west,align=left,font=\scriptsize\color{{accent}}] "
               rf"at (0,{yt:.2f}) {{\textbf{{{F['contradictions']}}} contradictions: paper and "
               rf"shipped code state a different value or term}};")
    out.append(rf"\node[anchor=north west,align=left,font=\scriptsize\color{{black!58}}] "
               rf"at (0,{yt - 0.26:.2f}) "
               rf"{{\textbf{{{F['other_class']}}} of another kind, classified and not retracted: "
               rf"{c['parse-limitation']} a limit of this\\survey's own parse, "
               rf"{c['code-absent']} a component never released, {c['version-skew']} version skew, "
               rf"{c['internal-inconsistency']} a paper\\disagreeing with itself}};")
    out.append(r"\end{tikzpicture}")
    (OUT / "fig_codegap.tex").write_text("\n".join(out) + "\n")
    return F["contradictions"], F["other_class"]


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

    Each bar is drawn against the denominator that belongs to its statistic, which is what Section
    VII-A quotes and what this figure used to contradict: the bar is the count against 113, so the
    six counts stay comparable to each other, and the pale track behind it is that statistic's own
    denominator, so the share a reader reads off the track is the share the text states. Where the
    note left rows unsettled they are drawn as a lighter tail beyond the track and named in the
    label, because a row the note could not settle is not a row that reported nothing.
    """
    axes = sorted(F["axes"], key=lambda t: -t[1] / t[2])
    lowest = {t[0] for t in axes[-2:]}
    # narrow enough that \resizebox to one column scales the figure up rather than down:
    # this chart's text is the smallest in the paper and must not be shrunk further
    width, rowsep = 5.2, 0.44
    # The count, its own denominator and the share. The unsettled rows are drawn as a tail rather
    # than named here: spelling them out in every label widened the picture by a third, and this
    # chart is \resizebox'd to one column, so a wider picture is a smaller font on the page.
    labels = {t[0]: rf"{t[1]} of {t[2]} ({round(100 * t[1] / t[2])}\%)" for t in axes}
    out = [PRE]
    y = 0.0
    ys = {}
    for label, n, denom, unk in axes:
        w = width * n / N
        track = width * denom / N
        acc = label in lowest
        style = "baracc" if acc else "bar"
        lsty = r"lbl,text=accent" if acc else "lbl"
        nsty = r"font=\scriptsize\color{accent}" if acc else "num"
        out.append(rf"\node[{lsty},anchor=east] at (0,{-y:.2f}) {{{esc(label)}}};")
        out.append(rf"\fill[barlight] (0.12,{-y - 0.1:.2f}) rectangle ({0.12 + track:.2f},"
                   rf"{-y + 0.1:.2f});")
        if unk:
            out.append(rf"\fill[black!8] ({0.12 + track:.2f},{-y - 0.1:.2f}) rectangle "
                       rf"({0.12 + track + width * unk / N:.2f},{-y + 0.1:.2f});")
        out.append(rf"\fill[{style}] (0.12,{-y - 0.1:.2f}) rectangle ({0.12 + w:.2f},"
                   rf"{-y + 0.1:.2f});")
        out.append(rf"\node[{nsty},anchor=west] at ({0.12 + width + 0.12:.2f},{-y:.2f}) "
                   rf"{{{labels[label]}}};")
        ys[label] = -y
        y += rowsep
    # a square bracket down the right-hand side of the two lowest bars, clear of the widest label:
    # the labels now carry their own denominator and run about twice as long as "11 (10%)" did
    xb = 0.12 + width + 0.24 + 0.115 * max(len(v) for v in labels.values())
    y0, y1 = (ys[l] for l in [a[0] for a in axes[-2:]])
    out.append(rf"\draw[line width=0.4pt,draw=accent] ({xb:.2f},{y0 + 0.16:.2f}) -- "
               rf"({xb + 0.10:.2f},{y0 + 0.16:.2f}) -- ({xb + 0.10:.2f},{y1 - 0.16:.2f}) -- "
               rf"({xb:.2f},{y1 - 0.16:.2f});")
    out.append(rf"\draw[lnk] (0.12,{-y + 0.16:.2f}) -- ({0.12 + width:.2f},{-y + 0.16:.2f});")
    # The annotation sits under the bar track, aligned with the bars it is about, and names the
    # colour the two rows are already drawn in. Set at x = -2.4 it floated under the row labels at
    # the far end of the chart from the bracket, with nothing joining the two; set to the right of
    # the bracket instead it would widen the picture and the \resizebox would shrink every label
    # in it, and this chart's text is already the smallest in the paper.
    out.append(rf"\node[anchor=north west,align=left,text width={width}cm,"
               rf"font=\scriptsize\color{{accent}}] "
               rf"at (0.12,{-y + 0.04:.2f}) {{the two rows in this colour are the pair a reader "
               rf"needs in order to compare any two methods}};")
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
        "fnOtherClass": F["other_class"],
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
    print("code gap:      %d contradictions, %d in the other four classes" % fig_codegap())
    print("penetration:   %d handled, %d closed-loop, %d rollout numbers" % fig_penetration())
    print("reporting:     %d axes, marked %s" % fig_reporting())
    n, med, bins = fig_trials()
    print("trials:        %d per-cell counts, median %g, bins %s" % (n, med, bins))
    print("caption macros:", numbers())
