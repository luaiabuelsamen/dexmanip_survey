"""Write the LaTeX edition of every survey table into tex/tables/, one file per table.

The markdown edition (tools/make_tables.py, tools/make_eval_tables.py,
tools/make_survey_table.py) prints a cell at its full length and lets the table grow as wide as it
must, which suited a landscape page. An IEEEtran column is 8.8 cm and a two-column float is
18.1 cm, so a table here is designed for the page instead of transliterated from the markdown.
Three rules do the work, in this order of priority:

  1. a table fits 18.1 cm at footnotesize, or it is not in the body;
  2. a column is cut before the type is shrunk;
  3. a paragraph of free text does not appear in a body table. Where the markdown carried one --
     a simulator's contact model, a hand's actuation, a method's hand string, a predecessor
     survey's coverage -- the body prints a short controlled vocabulary and an appendix longtable
     carries the source text verbatim.

Nothing is recomputed here. The row partitions, the emptiness convention, the hand-usage patterns,
the trial-count derivation, the mention ranking and the survey anchors are all imported from the
tools that the markdown edition already used, so the two editions cannot disagree about a number.

A value no source stated prints as \\na, and every caption states how many cells in that table are
\\na and over which columns, because an emptiness figure quoted over a key column that can never be
blank is diluted (see make_tables.py on the same point).

Controlled vocabularies are applied by CLASSIFIERS below. Every input value that no pattern matches
is reported on stderr at the end of a run, so a new corpus row cannot be silently binned as
"other".

    python tools/make_tex_tables.py            # write tex/tables/*.tex
    python tools/make_tex_tables.py --probe    # also write tex/tables_probe.tex
"""
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
OUT = R / "tex" / "tables"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, str(R / "tools" / f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


MT = _load("make_tables")          # ROWS, cell(), USES, HAND_SPEC_COLS
EV = _load("make_eval_tables")     # bill(), table9_rows(), method_name(), the derivation
SV = _load("make_survey_table")    # SPEC and its anchors, note_text(), UNOBTAINED, UNREAD
HU = _load("hand_usage")           # the one hand partition
CN = _load("check_numbers")        # norm_sim(), FACTS
CS = _load("cite_subjects")        # the key -> readable-name map used by the prose style pass

# The name the field uses for each work, derived from corpus/bib.json by tools/cite_subjects.py.
# A row label is that name with its citation, not the corpus key: a key is a filename, it wraps
# into three lines in a narrow column, and it tells a reader nothing the name does not.
SUBJECT = {k: v[0] for k, v in CS.build_map(CS.load()).items()}

ROWS = MT.ROWS
METHODS = [r for r in ROWS.values() if r.get("class") == "method"]
HANDS = [r for r in ROWS.values() if r.get("class") == "hand"]
SIMS = [r for r in ROWS.values() if r.get("class") == "simulator"]
TELE = [r for r in ROWS.values() if "operator_interface" in r]

NA = r"\na"
UNCLASSIFIED = []          # (classifier, key, value) reported at the end of a run

# --- LaTeX text ----------------------------------------------------------------------------------
UNI = {
    "—": "---", "–": "--", "’": "'", "‘": "`", "“": "``", "”": "''",
    "±": r"$\pm$", "×": r"$\times$", "°": r"$^\circ$", "²": r"$^2$",
    "³": r"$^3$", "µ": r"$\mu$", "μ": r"$\mu$", "≈": r"$\approx$",
    "→": r"$\rightarrow$", "≥": r"$\ge$", "≤": r"$\le$", "…": r"\ldots",
    " ": " ", "−": "-", "é": r"\'e", "ü": r'\"u', "ö": r'\"o',
    "ä": r'\"a', "è": r"\`e", "í": r"\'i", "ç": r"\c{c}", "ñ": r"\~n",
    "′": "'", "½": r"$\frac{1}{2}$", "⁄": "/", "ł": r"\l{}",
    "ś": r"\'s", "ń": r"\'n", "á": r"\'a", "ó": r"\'o", "ú": r"\'u",
    "č": r"\v{c}", "š": r"\v{s}", "ž": r"\v{z}", "å": r"\aa{}",
    "ø": r"\o{}", "ß": r"\ss{}", "‑": "-", "ˈ": "'", "®": "",
    "™": "", "·": r"$\cdot$", "‘": "`",
}
ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
       "~": r"\textasciitilde{}", "^": r"\textasciicircum{}", "\\": r"\textbackslash{}"}


def tex(s):
    """Escape a corpus string for LaTeX text. Non-ASCII that has no mapping is reported."""
    s = str(s)
    out = []
    for ch in s:
        if ch in ESC:
            out.append(ESC[ch])
        elif ord(ch) < 128:
            out.append(ch)
        elif ch in UNI:
            out.append(UNI[ch])
        else:
            UNCLASSIFIED.append(("unicode", hex(ord(ch)), ch))
            out.append("?")
    return "".join(out)


def key_tt(k):
    """A corpus key, breakable at its underscores so a long key wraps instead of overflowing."""
    parts = str(k).split("_")
    return r"\texttt{" + r"\_\allowbreak ".join(tex(p) for p in parts) + "}"


def subject(key):
    """A row label: the name the field uses for the work, with its citation.

    Names come from tools/cite_subjects.py, which derives them from corpus/bib.json, so the label
    in a table and the noun phrase in the prose are the same string. A few names are already
    LaTeX -- $\\pi_0$, \\texttt{dm\\_control} -- and are passed through unescaped. A key with no
    name keeps the key, which is the only case where a raw key is still printed.
    """
    name = SUBJECT.get(key)
    if not name:
        return key_tt(key)
    body = name if ("\\" in name or "$" in name) else tex(name)
    return r"%s~\cite{%s}" % (body, key)


def clip(s, n):
    """Cut at a word boundary, marking the cut. The full value is in the appendix longtable."""
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return (cut or s[:n]) + "…"


def num(v, fmt="{:g}"):
    if v is None or v == "":
        return NA
    if isinstance(v, (int, float)):
        return fmt.format(v)
    return tex(v)


def yesno(v):
    return NA if v is None else ("yes" if v else "no")


def thousands(v):
    """A count with a thin space every three digits. A field that holds a range or a note rather
    than a number keeps its own text."""
    if v is None or v == "":
        return NA
    if isinstance(v, (int, float)):
        return f"{v:,}".replace(",", r"\,")
    return tex(clip(v, 18))


# --- controlled vocabularies ---------------------------------------------------------------------
# Each is an ordered list of (pattern, token). The first match wins, so the list is ordered by
# which mechanism the survey treats as primary, not alphabetically.
ACTUATION = [
    (r"hydraulic|pneumat|artificial muscle|myofiber|water-filled", "fluidic muscle"),
    (r"tendon|cable|bowden|pull-pull|twisted string", "tendon"),
    (r"linkage|four-bar|4-bar|crank|slider", "linkage"),
    (r"worm|lead[- ]screw|ball[- ]screw|harmonic|planetary|gearbox|gear[- ]?(?:ed|driven|train|"
     r"module)", "geared"),
    (r"direct[- ]drive|direct drive|quasi-direct", "direct drive"),
    (r"servo|motor|electric|actuator", "geared"),
]
FORCE_KIND = [
    (r"pull-?out", "pull-out"),
    (r"pinch", "pinch"),
    (r"normal force|indenter|fingertip force", "fingertip normal"),
    (r"grip|grasp force|clamp", "grip"),
    (r"payload|lift|hold|carry", "lift"),
    (r"unlabelled|no protocol|not stated|unspecified|vendor", "vendor, no protocol"),
]
TACTILE = [
    (r"^\s*(none|no tactile|not present)|none \(|none mentioned|no tactile|"
     r"none on the physical|future work|plan to", "none"),
    (r"not stated|not in the press|unknown|not given on", "unstated"),
    (r"optional|supports|available as|can be fitted|third-party", "optional"),
    (r"taxel|array|matrix|full[- ]palm|palm|per-link|whole[- ]surface|units|sq ?mm", "array"),
    (r"fingertip|finger pad|F/T sensor|force[/ ]torque", "fingertip"),
    (r"pressure|capacitive|hall|barometric|magnetic|vision-based|camera", "fingertip"),
]
CONTACT = [
    # "complementarity-free" must be tested before "complementarity", or the one engine in the
    # corpus that advertises the absence of a complementarity solve is binned as having one.
    (r"complementarity-free|no complementarity", "complementarity-free"),
    (r"nonlinear complementarity|\bNCP\b", "hard NCP"),
    (r"\bLCP\b|linear complementarity|complementarity", "complementarity"),
    (r"convex", "convex relaxation"),
    (r"soft|compliant|spring|penalty|regularis|regulariz|elliptic|softness|"
     r"stiffness|damping|Baumgarte", "soft"),
    (r"impulse|velocity-level|position-based|PBD|substep", "impulse"),
    (r"signed distance|SDF|mesh|primitive|collision", "rigid, model unstated"),
]
SOLVER = [
    (r"complementarity-free|no complementarity solve|closed[- ]form", "closed form"),
    (r"projected Gauss-?Seidel|\bPGS\b", "PGS"),
    (r"\bTGS\b|temporal Gauss", "TGS"),
    (r"Newton", "Newton"),
    (r"conjugate gradient|\bCG\b", "CG"),
    (r"interior[- ]point", "interior point"),
    (r"\bADMM\b|primal[- ]dual", "primal-dual"),
    (r"Gauss-?Seidel|iterative|relaxation", "Gauss-Seidel"),
    (r"spring|explicit|Euler|semi-implicit", "explicit/spring"),
    (r"Featherstone|articulated[- ]body|analytic", "analytic"),
]
INTERFACE = [
    (r"\bVR\b|Vision Pro|Quest|headset|head-mounted|HMD", "VR headset"),
    (r"exoskelet|leader arm|puppet|kinesthetic|joystick|SpaceMouse|gamepad", "exoskeleton/leader"),
    (r"glove", "glove"),
    (r"mocap|motion capture|Vicon|OptiTrack|marker-based", "motion capture"),
    (r"camera|RealSense|webcam|monocular|stereo|RGB|video|vision", "camera"),
    (r"\bnone\b|no live", "none"),
]
CLASSIFIERS = {"actuation": ACTUATION, "force_kind": FORCE_KIND, "tactile": TACTILE,
               "contact_model": CONTACT, "solver": SOLVER, "operator_interface": INTERFACE}


def vocab(field, value, key="?"):
    """Map a corpus free-text value to this field's controlled vocabulary."""
    if value is None or value == "" or value == []:
        return NA
    if isinstance(value, list):
        value = "; ".join(str(v) for v in value)
    s = str(value)
    for pat, token in CLASSIFIERS[field]:
        if re.search(pat, s, re.I):
            return token
    UNCLASSIFIED.append((field, key, clip(s, 70)))
    return "other"


PENETRATION = {"not addressed": "none", "penalised": "penalised", "measured": "measured",
               "constrained": "constrained"}
TASK_SHORT = {"track-human-ref": "track-ref", "functional/tool": "tool",
              "bimanual-coord": "bi-coord", "locomanipulation": "loco", "handover": "handover",
              "reorient": "reorient", "grasp": "grasp", "music": "music", "other": "other"}
PARADIGM_SHORT = {"RL": "RL", "BC": "BC", "RL+demo": "RL+demo", "distillation": "distil",
                  "VLA": "VLA", "diffusion": "diff", "flow": "flow", "MPC": "MPC",
                  "world-model": "world", "teleop-system": "teleop", "trajopt": "trajopt",
                  "grasp-synthesis": "grasp-syn", "data-collection": "data"}

MAKER_ABBREV = [
    (r"\bUniversity of ([A-Z][a-z]+)", r"Univ.\ \1"), (r"\bUniversity\b", "Univ."),
    (r"\bInstitute of Technology\b", "Inst.\\ Tech."), (r"\bInstitute\b", "Inst."),
    (r"\bTechnologies\b|\bTechnology\b", "Tech."), (r"\bCorporation\b|\bCompany\b", "Co."),
    (r"\bLaboratory\b", "Lab"), (r"\bCarnegie Mellon Univ\.", "CMU"),
    (r"\bNew York Univ\.", "NYU"), (r"\bRobotics\b", "Robotics"),
]


def maker_short(r):
    """A maker for a column 52 pt wide: the institution, not the author list.

    A hand row sourced to a paper carries its author list here; a vendor row carries one name.
    Taking the last comma-separated segment of a long list keeps the institution that built the
    hand, which is what the column is for; the full field stays in the appendix hand table.
    """
    v = r.get("maker")
    if not v:
        return NA
    s = " ".join(str(v).split())
    # A parenthetical carries its own commas -- "Psyonic Inc. (Chicago, USA)" -- and taking the
    # last comma-separated segment of that gives "USA)". Drop the parenthetical first, then treat
    # two or more remaining commas as an author list and keep its last segment, the institution.
    s = re.sub(r"\s*\([^)]*\)?", "", s).strip(" ,;")
    if s.count(",") >= 2:
        s = s.split(",")[-1].strip()
    for pat, rep in MAKER_ABBREV:
        s = re.sub(pat, rep, s)
    return tex(clip(s, 42))


def claim_when(r):
    """The date of the claim: an ISO date, else a year, else the fact that the source is undated."""
    v = r.get("claim_date")
    if not v:
        return NA
    s = str(v)
    m = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", s)
    if m and not re.search(r"fetched\s+" + re.escape(m.group(1)), s):
        return m.group(1)
    if re.search(r"undated|no source", s, re.I):
        return "undated"
    m = re.search(r"\b(19|20)\d{2}\b", s)
    return m.group(0) if m else "undated"


def evidence_class(r):
    """datasheet, video or press: what kind of artefact the claim was read off."""
    sq = (r.get("source_quality") or "").lower()
    cd = (r.get("claim_date") or "").lower()
    if "video" in cd or "video" in sq:
        return "video"
    if sq in ("paper", "datasheet") or "datasheet" in sq:
        return "datasheet"
    if "vendor" in sq or "project page" in sq or "driver repo" in sq:
        return "datasheet"
    if "press" in sq or "tracker" in sq:
        return "press"
    if sq == "unavailable" or not sq:
        return NA
    UNCLASSIFIED.append(("evidence", r["key"], sq))
    return "press"


def uses_count(key):
    """Method rows whose OWN experiments run on this hand. Same patterns as make_tables.USES."""
    pat = MT.USES.get(key)
    if not pat:
        return 0
    return sum(1 for m in METHODS if re.search(pat, str(m.get("hand") or ""), re.I))


def hand_short(v, n=36):
    """A hand string for a narrow column: the first named hand.

    The row's hand field lists every end effector the work used and often the arm it hung on.
    Taking the run before the first separator, and before the clause that names the arm, gives
    the hand itself, which is a whole value rather than a cut one: the longest in the corpus is
    34 characters, so at the widths used here nothing is marked with an ellipsis.
    """
    if not v:
        return NA
    s = " ".join(str(v).split())
    s = re.sub(r"\s*\(.*?\)", "", s)
    s = re.split(r";|/|,| and | mounted on | attached to | on a ", s)[0].strip()
    return tex(clip(s or "?", n))


def latency_short(r):
    v = r.get("latency")
    if not v:
        return NA
    s = str(v)
    m = re.search(r"(\d[\d.,]*)\s*(ms|kHz|Hz|s\b)", s)
    if m:
        return tex(f"{m.group(1)} {m.group(2)}")
    if re.search(r"no number|not stated|claimed|no figure", s, re.I):
        return NA
    return tex(clip(s, 20))


def collected(r):
    """Data collected, as the markdown edition composed it, abbreviated for a narrow column."""
    bits = []
    t, h = r.get("data_trajectories"), r.get("data_hours")
    if t:
        bits.append(f"{t/1000:g}k traj" if t >= 10000 else f"{t:,} traj".replace(",", r"\,"))
    if h:
        bits.append(f"{h:g} h")
    return ", ".join(bits) or NA


# --- the table writer ----------------------------------------------------------------------------
ALIGN = {"l": r">{\raggedright\arraybackslash\hspace{0pt}}p{%s}",
         "r": r">{\raggedleft\arraybackslash}p{%s}",
         "c": r">{\centering\arraybackslash}p{%s}"}


def note_block(note, total):
    """The note line under a table, set to the table's own measure.

    A caption says what the table shows and how many of its cells are empty, and stops. What a
    controlled vocabulary token means, how a ranking was scored, which column the reader should
    read first: that is a note under the rules, where a reader meets it after the table rather
    than before it.
    """
    if not note:
        return []
    return [r"\par\vspace{2pt}",
            r"\parbox{%gpt}{\scriptsize\raggedright %s\par}" % (total, note)]


def write_table(fname, label, caption, cols, body, wide=True, env=None, colsep=3,
                size=r"\footnotesize", pos="!t", note=None):
    """One table file. `cols` is a list of (header, width in pt, alignment).

    Width discipline: the sum of the column widths plus 2*colsep per column must not exceed the
    text measure, 252 pt in one column and 516 pt in two. The sum is asserted here rather than
    discovered in the log, so a column added without taking width from another fails at generation
    time instead of silently overflowing the page.
    """
    measure = 516.0 if wide else 252.0
    total = sum(w for _, w, _ in cols) + 2 * colsep * len(cols)
    assert total <= measure, f"{fname}: {total:.0f} pt of column over a {measure:.0f} pt measure"
    env = env or ("table*" if wide else "table")
    spec = "".join(ALIGN[a] % f"{w:g}pt" for _, w, a in cols)
    head = " & ".join(r"\hdr{%s}" % h for h, _, _ in cols)
    lines = [
        f"% generated by tools/make_tex_tables.py -- do not edit",
        rf"\begin{{{env}}}[{pos}]",
        r"\centering",
        r"\caption{%s}" % caption,
        r"\label{%s}" % label,
        size,
        r"\setlength{\tabcolsep}{%gpt}" % colsep,
        r"\setlength{\emergencystretch}{1.5em}",
        r"\begin{tabular}{%s}" % spec,
        r"\toprule",
        r"\rowcolor{wash} " + head + r" \\",
        r"\midrule",
    ]
    lines += [" & ".join(row) + r" \\" for row in body]
    lines += [r"\bottomrule", r"\end{tabular}"]
    lines += note_block(note, total)
    lines += [rf"\end{{{env}}}", ""]
    (OUT / fname).write_text("\n".join(lines))
    return dict(file=fname, cols=len(cols), width="two" if wide else "one", rows=len(body),
                pt=round(total))


def write_longtable(fname, label, caption, cols, body, colsep=3, size=r"\scriptsize", note=None,
                    extra_labels=()):
    """An appendix longtable, run across both columns by switching to one-column mode."""
    total = sum(w for _, w, _ in cols) + 2 * colsep * len(cols)
    assert total <= 516.0, f"{fname}: {total:.0f} pt over a 516 pt measure"
    spec = "".join(ALIGN[a] % f"{w:g}pt" for _, w, a in cols)
    head = " & ".join(r"\hdr{%s}" % h for h, _, _ in cols)
    lines = [
        f"% generated by tools/make_tex_tables.py -- do not edit",
        r"\clearpage",
        r"\onecolumn",
        size,
        r"\setlength{\tabcolsep}{%gpt}" % colsep,
        r"\setlength{\emergencystretch}{2em}",
        r"\begin{longtable}{%s}" % spec,
        # extra_labels are the names an older placeholder table used, kept so that a cross
        # reference written against the placeholder still resolves to the table that replaced it.
        r"\caption{%s}\label{%s}%s\\" % (caption, label,
                                         "".join(r"\label{%s}" % x for x in extra_labels)),
        r"\toprule",
        r"\rowcolor{wash} " + head + r" \\",
        r"\midrule",
        r"\endfirsthead",
        r"\multicolumn{%d}{l}{\footnotesize\itshape Table~\ref{%s}, continued.}\\" % (len(cols), label),
        r"\toprule",
        r"\rowcolor{wash} " + head + r" \\",
        r"\midrule",
        r"\endhead",
        r"\midrule",
        r"\multicolumn{%d}{r}{\footnotesize\itshape continued on the next page}\\" % len(cols),
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    lines += [" & ".join(row) + r" \\" for row in body]
    lines += [r"\end{longtable}"]
    lines += note_block(note, total)
    lines += [r"\twocolumn", r"\normalsize", ""]
    (OUT / fname).write_text("\n".join(lines))
    return dict(file=fname, cols=len(cols), width="two (longtable, one-column mode)",
                rows=len(body), pt=round(total))


def emptiness(body, idx, total_note):
    """How many of the counted cells are \\na, phrased for a caption."""
    cells = [row[i] for row in body for i in idx]
    n = sum(1 for c in cells if c.strip() == NA)
    pct = 100 * n / max(len(cells), 1)
    return (f"{n} of the {len(cells)} cells in the {len(idx)} {total_note} "
            f"({pct:.0f}\\%) are \\na: no source stated the value.")


# --- Table I and Table II: the hands ---------------------------------------------------------
# The release partition is the markdown edition's: sold, open-source or unstated can be obtained;
# announced, prototype and internal-only cannot.
OBTAINABLE = ("sold", "open-source", None)
UNRELEASED = ("announced", "prototype", "internal-only")
BY_JOINTS = lambda r: (-(r.get("dof") or 0), r["key"])


def hand_row(r, wide_kind=34):
    return [
        subject(r["key"]),
        maker_short(r),
        num(r.get("dof")),
        num(r.get("actuated_dof")),
        vocab("actuation", r.get("actuation"), r["key"]),
        thousands(r.get("weight_g")),
        num(r.get("fingertip_force_n")),
        vocab("force_kind", r.get("force_kind"), r["key"]),
        vocab("tactile", r.get("tactile"), r["key"]),
        (NA if r.get("price_usd") is None else thousands(r["price_usd"])),
        yesno(r.get("open_hardware")),
        tex(r.get("release_status") or "unstated"),
        str(uses_count(r["key"])),
    ]


HAND_SPEC_IDX = [2, 3, 4, 5, 6, 7, 8, 9]   # the specification columns, as in make_tables


def table1():
    rows = sorted([r for r in HANDS if r.get("release_status") in OBTAINABLE], key=BY_JOINTS)
    body = [hand_row(r) for r in rows]
    cols = [("hand", 88, "l"), ("maker", 62, "l"), ("DoF", 16, "r"), (r"act.\ DoF", 16, "r"),
            ("actuation", 42, "l"), ("mass g", 20, "r"), ("force N", 18, "r"),
            ("force kind", 40, "l"), ("tactile", 34, "l"), ("price USD", 26, "r"),
            ("open HW", 18, "c"), ("status", 36, "l"), ("uses", 14, "r")]
    cap = (r"Hands that can be obtained: sold, open-source, or with no release status stated. "
           + str(len(rows)) + r" rows, sorted by joint count. "
           + emptiness(body, HAND_SPEC_IDX, "specification columns (DoF through price)"))
    note = (r"A row whose joint count no source states sorts last rather than being ranked by a "
            r"number nobody stated. The hand, maker, open-hardware, status and usage columns are "
            r"left out of the emptiness count because they are never blank, and counting them "
            r"would dilute the finding. \emph{actuation}, \emph{force kind} and \emph{tactile} "
            r"are controlled vocabularies; the source sentence each was read from is in "
            r"Table~\ref{tab:app-hands}. \emph{force N} is not a ranking: read \emph{force kind} "
            r"first, because pull-out resistance, pinch force, a fingertip normal force under an "
            r"indenter and an unlabelled vendor number are different measurements. \emph{uses} "
            r"counts the method rows whose own experiments run on that hand. Every figure is the "
            r"maker's or the authors' own claim.")
    return write_table("table1_hands_available.tex", "tab:hands-available", cap, cols, body,
                       note=note)


def table2():
    rows = sorted([r for r in HANDS if r.get("release_status") in UNRELEASED], key=BY_JOINTS)
    body = []
    for r in rows:
        body.append(hand_row(r) + [claim_when(r), evidence_class(r)])
    cols = [("hand", 84, "l"), ("maker", 46, "l"), ("DoF", 16, "r"), (r"act.\ DoF", 16, "r"),
            ("actuation", 34, "l"), ("mass g", 18, "r"), ("force N", 16, "r"),
            ("force kind", 34, "l"), ("tactile", 30, "l"), ("price USD", 22, "r"),
            ("open HW", 17, "c"), ("status", 36, "l"), ("uses", 14, "r"),
            ("claim date", 38, "l"), ("evidence", 30, "l")]
    cap = (r"Hands announced, prototyped or held internally, which cannot be bought or built. "
           + str(len(rows)) + r" rows, the columns of Table~\ref{tab:hands-available} plus the "
           r"date of the claim and the class of artefact it was read off. "
           + emptiness(body, HAND_SPEC_IDX, "specification columns (DoF through price)"))
    note = (r"That share is far higher than in Table~\ref{tab:hands-available} and it is the "
            r"finding of this table rather than a defect of it: an unreleased hand is announced "
            r"without a specification. \emph{evidence} is \emph{datasheet} for a paper, datasheet "
            r"or vendor specification page, \emph{video} for a demonstration reel, \emph{press} "
            r"for a press release or a third-party tracker. \emph{claim date} prints "
            r"\emph{undated} where the source page carries no date of its own; a fetch date is "
            r"not a claim date.")
    return write_table("table2_hands_announced.tex", "tab:hands-announced", cap, cols, body,
                       colsep=2, note=note)


# --- Table III: the simulators -----------------------------------------------------------------
HAND_NAME_CLEAN = re.compile(r"\s*\(.*?\)\s*")


def hands_shipped_names(r):
    """The first-party hand models the parsed snapshot ships, as a list of names."""
    v = r.get("hands_shipped")
    if not v:
        return []
    return [n for n in (HAND_NAME_CLEAN.sub("", str(x)).strip() for x in v) if n]


def table3():
    rows = sorted(SIMS, key=lambda r: r["key"])
    body = []
    for r in rows:
        dt = r.get("default_timestep_s")
        names = hands_shipped_names(r)
        body.append([
            subject(r["key"]),
            vocab("contact_model", r.get("contact_model"), r["key"]),
            vocab("solver", r.get("solver"), r["key"]),
            yesno(r.get("differentiable")),
            yesno(r.get("gpu")),
            NA if dt is None else f"{dt:.4g}",
            yesno(r.get("penetration_exposed")),
            str(len(names)) if r.get("hands_shipped") else NA,
        ])
    cols = [("engine", 72, "l"), ("contact model", 78, "l"), ("solver", 68, "l"),
            ("diff.", 24, "c"), ("GPU", 24, "c"), ("dt (s)", 38, "r"),
            ("penetration exposed", 52, "c"), ("hands", 28, "r")]
    cap = (str(len(rows)) + r" simulators and physics engines, with the contact formulation each "
           r"names, whether it exposes interpenetration depth, and how many first-party hand "
           r"models it ships. "
           + emptiness(body, [1, 2, 3, 4, 5, 6, 7], "property columns"))
    shipped = "; ".join(
        r"\emph{%s} %s" % (tex(SUBJECT.get(r["key"], r["key"])), tex(", ".join(hands_shipped_names(r))))
        for r in rows if hands_shipped_names(r))
    note = (r"\emph{contact model} and \emph{solver} are controlled vocabularies: \emph{soft} for "
            r"a compliant or regularised contact, \emph{convex relaxation} for a convexified "
            r"formulation, \emph{complementarity} for an LCP, \emph{hard NCP} for a nonlinear "
            r"complementarity problem, \emph{impulse} for a velocity-level update, and "
            r"\emph{rigid, model unstated} where the source describes collision geometry but "
            r"names no contact law. The sentence each was read from runs to several hundred "
            r"characters and is reproduced in full in Table~\ref{tab:app-contact}, because "
            r"Section~IV's argument turns on its wording. \emph{penetration exposed} is whether "
            r"the engine makes interpenetration depth readable by a user's code without patching "
            r"it. \emph{hands} counts first-party hand models in the parsed snapshot, and they "
            r"are: " + shipped + r".")
    return write_table("table3_simulators.tex", "tab:simulators", cap, cols, body, note=note)


# --- Table IV: reward terms --------------------------------------------------------------------
MARK = {"paper": "P", "code": "C", "both": "B", "code-zero": "Z", None: ""}
FAM_HDR = {"pose": "goal/rot", "objvel": "obj vel", "fingerobj": "fing-obj",
           "handpose": "hand pose", "actrate": "act rate", "effort": "effort", "drop": "drop",
           "contact": "contact", "bonus": "bonus"}


def table4():
    rm = json.loads((R / "corpus/reward_matrix.json").read_text())
    fams = rm["_families"]
    rows = sorted(rm["rows"], key=lambda x: (ROWS.get(x["key"], {}).get("year", 0), x["key"]))
    body, blank, term_cells = [], 0, 0
    for row in rows:
        src = ROWS.get(row["key"], {})
        marks = [MARK[row[f]] for f in fams]
        blank += sum(1 for m in marks if m == "")
        term_cells += len(marks)
        body.append([subject(row["key"]), num(src.get("year"))] + marks + [
            num(src.get("reward_terms")),
            yesno(src.get("code_released")),
            "yes" if src.get("paper_code_mismatch") else ("no" if src.get("code_released") else NA),
        ])
    cols = ([("method", 100, "l"), ("yr", 18, "r")]
            + [(FAM_HDR[f], 26, "c") for f in fams]
            + [("terms", 20, "r"), ("code", 16, "c"), ("mismatch", 34, "c")])
    cap = (r"Reward-term families across the " + str(len(rows)) + r" in-hand reorientation "
           r"methods whose objective could be read term by term. "
           + f"{blank} of the {term_cells} term cells ({100*blank/max(term_cells,1):.0f}\\%) are "
           r"blank, which means the method does not use that family; the only column that carries "
           r"\na is \emph{mismatch}, which no method that released no code can settle.")
    note = (r"A mark is \textbf{P} where the term is in the paper and either no code was released "
            r"or it is absent from the released reward code, \textbf{C} where it is in the "
            r"released code and not in the paper's stated reward, \textbf{B} where it is in both, "
            r"and \textbf{Z} where the released code carries the term with a weight of zero. A "
            r"blank is not the same mark as \na: the objective was read in full for every row in "
            r"this table, so nothing in a term column is unstated. \emph{terms} is the count of "
            r"reward terms the paper states. Marks are read from the per-method source section "
            r"recorded in \texttt{corpus/reward\_matrix.json}.")
    return write_table("table4_rewards.tex", "tab:rewards", cap, cols, body, note=note)


# --- Table V: teleoperation and human-data systems ---------------------------------------------
def table5():
    rows = sorted(TELE, key=lambda r: (r.get("year") or 0, r["key"]))
    body = []
    for r in rows:
        body.append([
            subject(r["key"]),
            vocab("operator_interface", r.get("operator_interface"), r["key"]),
            hand_short(r.get("hand"), 34),
            latency_short(r),
            NA if r.get("rig_cost_usd") is None else thousands(r["rig_cost_usd"]),
            collected(r),
        ])
    cols = [("system", 100, "l"), ("interface", 62, "l"), ("robot hand", 90, "l"),
            ("latency", 58, "l"), ("rig USD", 34, "r"), ("data collected", 50, "l")]
    cap = (str(len(rows)) + r" teleoperation and human-data systems, every corpus row that names "
           r"an operator interface. "
           + emptiness(body, [1, 2, 3, 4, 5], "columns other than the system"))
    note = (r"Two columns rather than one: the interface and hand columns need about 150\,pt "
            r"between them before the hand names start breaking mid-word. \emph{interface} is a "
            r"controlled vocabulary. \emph{latency} is whatever the source measured, reduced to "
            r"its leading figure, and is \na where a paper claims low latency without a number, "
            r"which is the usual case. \emph{rig USD} is the authors' own bill of materials where "
            r"they published one. \emph{data collected} is the released trajectory count and "
            r"hours, and a system built to be an interface rather than a dataset states neither.")
    return write_table("table5_teleop.tex", "tab:teleop", cap, cols, body, note=note)


# --- Table VI: the method table, body version and appendix longtable ---------------------------
def _md_stamp():
    import glob, os
    fs = glob.glob(str(R / "papers/md/*.md"))
    return [len(fs), max((os.path.getmtime(f) for f in fs), default=0)]


def cached(name, fn):
    """Cache a ranking that scans every parsed paper, keyed on the state of papers/md.

    Both rankings read all of papers/md, which is the slow part of a run and cannot change unless
    that directory does. The cache lives outside the repository because it is not a result.
    """
    import tempfile
    p = Path(tempfile.gettempdir()) / "dexmanip_tex_tables_cache.json"
    stamp = _md_stamp()
    try:
        blob = json.loads(p.read_text())
    except Exception:
        blob = {}
    if blob.get("stamp") == stamp and name in blob:
        return [tuple(x) for x in blob[name]]
    val = fn()
    blob["stamp"] = stamp
    blob[name] = val
    try:
        p.write_text(json.dumps(blob))
    except Exception:
        pass
    return val


def mention_counts():
    """Whole-word mentions of each method in the OTHER parsed papers, as make_eval_tables scores
    them. The scoring is that function's, applied to every method row rather than to the
    closed-loop policy subset it selects for the results matrix, because the body table of
    Section V ranks the corpus and not the protocol."""
    import glob
    import os
    texts = {}
    for f in glob.glob(str(R / "papers/md/*.md")):
        k = re.sub(r"\.ocr$", "", os.path.basename(f)[:-3])
        texts[k] = texts.get(k, "") + open(f, errors="ignore").read().lower()
    scored = []
    for r in METHODS:
        name = EV.method_name(r["key"])
        if len(name) < 4:
            continue
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(name.lower()) + r"(?![A-Za-z0-9+-])")
        n = sum(1 for k, t in texts.items() if k != r["key"] and pat.search(t))
        scored.append((n, r["key"], name, "short name" if " " not in name else "title"))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored


def tags(field, short, r, cap=2):
    v = r.get(field) or []
    if not v:
        return NA
    out = [short.get(t, t) for t in v[:cap]]
    return tex(", ".join(out) + ("+" if len(v) > cap else ""))


def sim_short(r):
    """The engine a method ran in, as a name rather than as a sentence.

    `check_numbers.norm_sim` folds the spellings together but keeps whatever qualification the
    row carried, which runs to 185 characters in one case. The leading clause of that, capped at
    three words, is the engine's name; the qualification is in \\texttt{corpus/rows/}. Nothing is
    marked with an ellipsis, because a name is not a truncated sentence.
    """
    v = CN.norm_sim(r.get("sim")) if r.get("sim") else None
    if not v:
        return NA
    lead = re.split(r"[(;,]", str(v))[0].strip()
    return tex(" ".join(lead.split()[:3]) or str(v)[:16])


def method_cells(r, wide=False):
    return [
        subject(r["key"]),
        num(r.get("year")),
        tags("task_family", TASK_SHORT, r),
        tags("paradigm", PARADIGM_SHORT, r),
        hand_short(r.get("hand"), 36 if not wide else 48),
        sim_short(r),
        num(r.get("real_trials")),
        PENETRATION.get(r.get("penetration"), NA),
        yesno(r.get("code_released")),
    ]


METH_BODY_N = 20


def table6():
    scored = cached("mentions_all", mention_counts)[:METH_BODY_N]
    body = [method_cells(ROWS[k]) for _, k, _, _ in scored]
    cols = [("method", 106, "l"), ("yr", 18, "r"), ("task", 46, "l"), ("paradigm", 40, "l"),
            ("hand", 70, "l"), ("simulator", 44, "l"), ("real trials", 24, "r"),
            ("penetration", 40, "l"), ("code", 16, "c")]
    counts = "; ".join(f"{tex(SUBJECT.get(k, k))}~{n}" for n, k, _, _ in scored)
    cap = (r"The " + str(METH_BODY_N) + r" most-mentioned method papers in the corpus, ranked by "
           r"whole-word mentions in the other parsed papers of \texttt{papers/md}. All "
           + str(len(METHODS)) + r" rows, with the DoF, bimanual and unseen-object columns "
           r"restored, are in Table~\ref{tab:app-methods}. "
           + emptiness(body, [2, 3, 4, 5, 6, 7, 8], "columns other than the method and the year"))
    note = (r"A mention count is a count of mentions, not of use; by the rule of Section~VII the "
            r"counts are " + counts + r". \emph{penetration} is \emph{none} where the row's note "
            r"settles that the work does not address interpenetration, and \na where no note "
            r"settles it either way; no row in the corpus reports a penetration number for its "
            r"own trained policy. \emph{task} and \emph{paradigm} print the first two tags of a "
            r"row that carries more, marked with a trailing plus. \emph{simulator} is normalised "
            r"by the same rule \texttt{tools/check\_numbers.py} uses, which folds Isaac Gym "
            r"spellings together and keeps Isaac Lab apart from it.")
    return write_table("table6_methods_top.tex", "tab:methods-top", cap, cols, body, note=note)


def appendix_methods():
    """Every method row, one line each.

    The algorithm column is gone. It carried the corpus `algorithm` string cut at 110 characters,
    which made three rows in four two to four lines tall, took the table to eight pages, and
    ended most of its cells in an ellipsis that told a reader neither the method nor where the
    rest of it was. A table whose job is to let 112 rows be compared on their columns is worth
    more than a paragraph printed 112 times; the field is in \\texttt{corpus/rows/} in full, and
    Section~V describes the algorithms in prose.
    """
    rows = sorted(METHODS, key=lambda r: (str(r.get("year")), r["key"]))
    body = []
    for r in rows:
        body.append([
            subject(r["key"]),
            num(r.get("year")),
            tags("task_family", TASK_SHORT, r, cap=3),
            tags("paradigm", PARADIGM_SHORT, r, cap=3),
            hand_short(r.get("hand"), 40),
            num(r.get("hand_dof")),
            yesno(r.get("bimanual")),
            sim_short(r),
            yesno(r.get("real_robot")),
            num(r.get("real_trials")),
            num(r.get("objects_test_unseen")),
            PENETRATION.get(r.get("penetration"), NA),
            yesno(r.get("code_released")),
        ])
    cols = [("method", 88, "l"), ("yr", 16, "r"), ("task", 52, "l"), ("paradigm", 44, "l"),
            ("hand", 82, "l"), ("DoF", 14, "r"), ("bi", 11, "c"), ("simulator", 48, "l"),
            ("real", 14, "c"), ("trials", 19, "r"), ("unseen", 22, "r"),
            ("penetration", 38, "l"), ("code", 14, "c")]
    idx = list(range(2, 13))
    cap = (r"Every method row in the corpus, " + str(len(rows)) + r" of them, on the columns the "
           r"body version of Table~\ref{tab:methods-top} cuts down to twenty rows. Run across "
           r"both columns in one-column mode. "
           + emptiness(body, idx, "columns other than the method and the year"))
    note = (r"\emph{hand} is the first end effector the row names, without the arm it hangs on, "
            r"and \emph{simulator} is the leading clause of the normalised engine string: both "
            r"are names, so neither is cut and neither carries an ellipsis. The "
            r"\texttt{algorithm} field is not printed. It ran to a paragraph a row, which made "
            r"this table eight pages of ellipses; Section~V describes the algorithms, and "
            r"\texttt{corpus/rows/} holds that field, the full hand string and the full engine "
            r"string at their own length.")
    return write_longtable("appendix_methods_full.tex", "tab:app-methods", cap, cols, body,
                           colsep=2, note=note)


def appendix_contact():
    rows = sorted(SIMS, key=lambda r: r["key"])
    body = [[subject(r["key"]),
             tex(" ".join(str(r.get("contact_model")).split())) if r.get("contact_model") else NA,
             tex(" ".join(str(r.get("solver")).split())) if r.get("solver") else NA]
            for r in rows]
    cols = [("engine", 68, "l"), ("contact model, as the source describes it", 202, "l"),
            ("solver, as the source describes it", 202, "l")]
    cap = (r"The contact-model and solver descriptions behind the controlled vocabulary of "
           r"Table~\ref{tab:simulators}, verbatim from the parsed source and nothing here cut. "
           + emptiness(body, [1, 2], "description columns"))
    note = (r"These cells run to several hundred characters each, which is why the body table "
            r"prints a vocabulary instead: a 480-character cell in a body float is a paragraph "
            r"printed sideways.")
    return write_longtable("appendix_contact_models.tex", "tab:app-contact", cap, cols, body,
                           colsep=2, note=note, extra_labels=["tab:rewards_full"])


def appendix_hands():
    rows = sorted(HANDS, key=BY_JOINTS)
    body = []
    for r in rows:
        body.append([
            subject(r["key"]),
            tex(clip(r.get("actuation") or "", 175)) if r.get("actuation") else NA,
            tex(clip(r.get("force_kind") or "", 130)) if r.get("force_kind") else NA,
            tex(clip(r.get("tactile") or "", 155)) if r.get("tactile") else NA,
            tex(clip(r.get("claim_date") or "", 70)) if r.get("claim_date") else NA,
            tex(clip(r.get("spec_caveat") or "", 125)) if r.get("spec_caveat") else NA,
        ])
    cols = [("hand", 74, "l"), ("actuation, as the source describes it", 110, "l"),
            ("what the force figure is", 86, "l"),
            ("tactile, as the source describes it", 98, "l"),
            ("date of the claim", 48, "l"), ("caveat on the row", 74, "l")]
    cap = (r"The sentences behind the controlled vocabularies of "
           r"Tables~\ref{tab:hands-available} and~\ref{tab:hands-announced}, for all "
           + str(len(rows)) + r" hands. "
           + emptiness(body, [1, 2, 3, 4, 5], "description columns"))
    note = (r"The maker column is not repeated here; Tables~\ref{tab:hands-available} "
            r"and~\ref{tab:hands-announced} carry it, and the width it used goes to the sentences "
            r"this table exists to print. \emph{caveat on the row} is the \texttt{spec\_caveat} "
            r"field, which is where a figure with no reachable source is named as such; it is "
            r"empty for a row that carries no caveat rather than for a row nobody checked. Cells "
            r"are cut at a word boundary where they would otherwise run past the page; "
            r"\texttt{corpus/rows/} holds every field at full length.")
    return write_longtable("appendix_hands_full.tex", "tab:app-hands", cap, cols, body, colsep=2,
                           note=note, extra_labels=["tab:hands_full"])


# --- Table VII: the proposed protocol ----------------------------------------------------------
ENT = {"plusmn": r"$\pm$", "minus": "-", "sect": r"\S", "rho": r"$\rho$", "mdash": "---",
       "ndash": "--", "nbsp": "~", "amp": r"\&", "times": r"$\times$", "le": r"$\le$",
       "ge": r"$\ge$", "#10035": r"$\ast$", "#770": ""}


def md_to_tex(s):
    """Convert one markdown cell from the markdown edition into LaTeX text."""
    s = s.replace("&rho;&#770;", r"$\hat{\rho}$")
    out, i = [], 0
    for m in re.finditer(r"`([^`]*)`|&([a-zA-Z]+|#\d+);", s):
        out.append(tex(s[i:m.start()]))
        if m.group(1) is not None:
            out.append(key_tt(m.group(1)) if "_" in m.group(1)
                       else r"\texttt{%s}" % tex(m.group(1)))
        else:
            e = m.group(2)
            if e not in ENT:
                UNCLASSIFIED.append(("entity", e, s[:40]))
            out.append(ENT.get(e, ""))
        i = m.end()
    out.append(tex(s[i:]))
    return "".join(out)


def protocol_source():
    """The protocol rows as the markdown edition writes them, parsed back out of its own table.

    Reading them from `make_eval_tables.table8()` rather than restating them keeps the appendix
    text and every interpolated trial count identical to the markdown edition's, so the two
    cannot drift.
    """
    md = EV.table8()
    rows = []
    for line in md.splitlines():
        if not line.startswith("|") or set(line) <= set("|- "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] == "axis":
            continue
        rows.append(cells)
    return rows


def table7():
    pairs, matched, unseen, total, old = EV.bill()
    n_ratio = math.ceil(EV.n_for_ratio(0.5, 0.3))
    n_rho = EV.n_for_rho(0.70, 0.05)
    n_obj = EV.n_for_halfwidth(0.10)
    w100 = EV.wilson_halfwidth(0.5, 100) * 100
    body = [
        ["Task success",
         r"fraction of episodes meeting a criterion written before the run, and a graded rubric "
         r"score in $[0,1]$",
         rf"100 real and 200 sim per policy, task and condition for an absolute rate at a "
         rf"{w100:.0f}-point interval; a comparison alone needs {pairs} matched pairs per arm",
         r"raw counts, the criterion verbatim, the rubric, the initial-condition protocol, and an "
         r"interval whose kind is named"],
        ["Robustness",
         r"success under each perturbation axis, and the ratio to the unperturbed anchor",
         rf"40 per axis per policy to rank the axes; {n_ratio} per axis and {n_ratio} at the "
         rf"anchor before any claim that a named axis hurt",
         r"both absolute rates with their Wilson intervals, the axis ranges, and the ratio "
         r"without an interval unless the certifying count was run"],
        ["Unseen objects",
         r"mean over held-out objects of per-object success",
         rf"20 objects at 5 trials to screen; {n_obj} objects for a 10-point claim",
         r"the object list, the per-object rates, a bootstrap interval over objects, and the "
         r"within-object trial count"],
        ["Physical plausibility",
         r"maximum and mean hand-object penetration depth per rollout, and the fraction of frames "
         r"above 2\,mm",
         r"100 rollouts, simulation only",
         r"an interval over rollouts, the sample density, the threshold, the solver's "
         r"depenetration settings, and at least one rendered rollout"],
        ["Sample and wall-clock cost",
         r"environment steps and wall-clock to the checkpoint that produced the headline number",
         r"3 training seeds",
         r"the range over seeds, and the statement that 3 seeds is a range and not an interval"],
        ["Real-robot transfer",
         r"paired real and simulated outcomes on matched initial conditions, their correlation, "
         r"and the rectifier variance against the real variance",
         rf"the 100 real trials paired to 100 sim; about {n_rho} pairs to separate two "
         rf"correlations 0.1 apart",
         r"the correlation with its Fisher-z interval, the variance ratio with its bootstrap "
         r"interval, and which decision the count supports"],
        ["Reproducibility",
         r"the released config and checkpoints against the paper's stated objective",
         r"not a trial count",
         r"the file and line of every disagreement, or an explicit statement that none was found"],
    ]
    cols = [("axis", 62, "l"), ("what is measured", 128, "l"), ("minimum trials", 108, "l"),
            ("reported with it", 170, "l")]
    cap = (r"The proposed evaluation protocol. Two columns rather than one: four columns of "
           r"clauses do not fit 252\,pt without breaking words. No cell is \na, because every "
           r"cell here is a proposal rather than a reading of a source, and the table is the one "
           r"in this paper that no corpus row can fill. The \emph{how} and \emph{why} columns of "
           r"the long form, which carry the design of each measurement and the reason for each "
           r"count, are in Table~\ref{tab:app-protocol}; a paragraph of rationale does not belong "
           rf"in a body float. Every count is derived in Section~VII, and the bill for two "
           rf"policies on three tasks is {matched} matched plus {unseen} unseen real rollouts, "
           rf"against {old} on the independent-arm count the paired design replaces.")
    return write_table("table7_protocol.tex", "tab:protocol", cap, cols, body)


def appendix_protocol():
    rows = protocol_source()
    body = [[md_to_tex(c[0]), md_to_tex(c[2]), md_to_tex(c[5])] for c in rows]
    cols = [("axis", 56, "l"), ("how the measurement is made", 208, "l"),
            ("why the count is what it is", 208, "l")]
    cap = (r"The two columns of the protocol that Table~\ref{tab:protocol} leaves out, verbatim "
           r"from the generator that derives every count in it. No cell is \na. Read with "
           r"Table~\ref{tab:protocol}: the axis names match row for row.")
    return write_longtable("appendix_protocol_long.tex", "tab:app-protocol", cap, cols, body,
                           colsep=2)


# --- Table VIII: the empty results matrix ------------------------------------------------------
AXES_SHORT = ["task success", "robustness", "unseen objects", "plausibility", "cost", "transfer",
              "reproducibility"]
EXAMPLE_SHORT = [r"0.72 $\pm$ 0.09 (100)", r"lighting 0.41 (40), ratio 0.57",
                 r"0.55 [0.41, 0.68], 20 obj", r"3.1 / 0.8 mm, 0.12",
                 r"1.2e9 steps, 46 GPU-h", r"0.61 [0.47, 0.72]",
                 r"\texttt{train.\allowbreak yaml:88}"]


def table8():
    picked = cached("mentions_policy", EV.table9_rows)
    body = [[r"\emph{worked example}"] + EXAMPLE_SHORT]
    for _, k, _, kind in picked:
        body.append([subject(k) + (r"$\ast$" if kind == "title" else "")] + [""] * len(AXES_SHORT))
    cells = len(picked) * len(AXES_SHORT)
    counts = "; ".join(f"{tex(SUBJECT.get(k, k))}~{n}" for n, k, _, _ in picked)
    cols = [("method", 86, "l")] + [(a, 54, "l") for a in AXES_SHORT]
    cap = (r"The matrix, for someone else to fill: the " + str(len(picked)) + r" most-mentioned "
           r"dexterous-hand policy methods against the axes of Table~\ref{tab:protocol}. All "
           + str(cells) + r" cells are empty. An empty cell here is not \na: it is a measurement "
           r"nobody has made, which is the point of the table, and no cell in it has a source to "
           r"be missing.")
    note = (r"The first row is a worked example and every number in it is fabricated. Rows are "
            r"ranked by the rule of Section~VII, on whole-word matches over \texttt{papers/md}: "
            + counts + r". A mention count is a count of mentions, not of use. $\ast$ marks a "
            r"work matched on its title rather than on a short name; a title is matched mostly "
            r"inside reference lists and a short name in running text, so the two kinds of count "
            r"are not comparable. Each column is filled in the units Table~\ref{tab:protocol} "
            r"asks for.")
    return write_table("table8_matrix.tex", "tab:matrix", cap, cols, body, note=note)


# --- Table IX: the predecessor surveys ---------------------------------------------------------
SURVEY_BODY_COLS = ["scope", "bimanual", "hardware", "evaluation"]
UNSUPPORTED = []


def survey_cells(key, row):
    """One survey's cells, with make_survey_table's anchor rule: a cell whose quotation has gone
    from the note prints empty rather than printing an unchecked claim."""
    note = SV.note_text(key)
    spec = SV.SPEC.get(key, {})
    if not spec:
        when = SV.fetched_but_unread(key, note)
        text = (SV.UNREAD % when) if when else SV.UNOBTAINED
        return {c: ("*" + text + "*") for c in SV.COLS}, (1 if when else 0), (0 if when else 1)
    out = {}
    for col in SV.COLS:
        body, anchor = spec[col]
        if anchor in note:
            out[col] = body
        else:
            UNSUPPORTED.append(f"{key}.{col}: anchor gone from the note: {anchor!r}")
            out[col] = ""
    return out, 0, 0


def survey_rows():
    rows = SV.load_rows()
    order = sorted(rows, key=lambda k: (-(rows[k].get("year") or 0), k))
    got, unread, unobtained = [], 0, 0
    for k in order:
        cells, u1, u2 = survey_cells(k, rows[k])
        unread += u1
        unobtained += u2
        got.append((k, rows[k], cells))
    return got, unread, unobtained


def emph_or_tex(s, n=None):
    """A cell that the generator marked *like this* stays italic; anything else is plain text."""
    if s == "":
        return NA
    if s.startswith("*") and s.endswith("*"):
        return r"\emph{%s}" % tex(clip(s[1:-1], n) if n else s[1:-1])
    return tex(clip(s, n) if n else s)


def table9():
    """The survey table, now the only one.

    This printed twice: here cut at 70 characters a cell, and again in the appendix at full
    length over all six columns, a page of the same prose in six columns that no sentence in the
    paper referred to. One table carries the argument, so the cut is lifted here and the appendix
    duplicate is gone.
    """
    got, unread, unobtained = survey_rows()
    body = []
    for k, row, cells in got:
        body.append([subject(k), num(row.get("year"))]
                    + [emph_or_tex(cells[c]) for c in SURVEY_BODY_COLS])
    cols = [("survey", 78, "l"), ("yr", 17, "r"), ("scope", 98, "l"),
            ("bimanual covered", 92, "l"), ("hardware covered", 88, "l"),
            ("evaluation covered", 95, "l")]
    idx = [2, 3, 4, 5]
    empty_cells = sum(1 for row in body for i in idx if row[i].strip() == NA)
    cap = (str(len(body)) + r" existing surveys, one per corpus row of class \texttt{survey}, "
           r"newest first, and what each covers. " + str(empty_cells) + r" of the "
           + str(len(body) * len(idx)) + r" coverage cells print \na, which here means the "
           r"quotation that supported the cell has gone from \texttt{papers/notes/} and the claim "
           r"is no longer checkable rather than that no source stated it.")
    note = (str(unobtained) + r" surveys could not be obtained and " + str(unread) + r" was "
            r"fetched too late to be read into a note; those rows say so in every column rather "
            r"than leaving blanks, because a blank row would read as a survey that covers "
            r"nothing. Every filled cell is read from \texttt{papers/notes/<key>.md} and is "
            r"checked against a quotation from that note by "
            r"\texttt{tools/make\_survey\_table.py}; nothing here is cut. The two columns this "
            r"table does not print, the taxonomy each survey uses and the gaps each names, are "
            r"in those same notes. The columns record what each work covers, not how well, and a "
            r"blank in \emph{bimanual} or \emph{hardware} is a scope decision by its authors "
            r"rather than a failure.")
    return write_table("table9_surveys.tex", "tab:surveys", cap, cols, body, note=note)


def appendix_surveys():
    """The appendix duplicate of Table~\\ref{tab:surveys}, withdrawn.

    It was a full page of the same prose over six columns, no sentence in the paper pointed at
    it, and the body table it repeated now prints its cells at full length. The file stays
    because a section inputs it by name; it emits nothing.
    """
    p = OUT / "appendix_surveys_full.tex"
    p.write_text(
        "% generated by tools/make_tex_tables.py -- do not edit\n"
        "% Withdrawn. This was the full-length duplicate of Table~\\ref{tab:surveys}: the same\n"
        "% fourteen surveys over six columns of prose, a page of it, and nothing in the paper\n"
        "% referred to it. Table~\\ref{tab:surveys} now prints its four coverage columns uncut,\n"
        "% and papers/notes/<key>.md holds the full text of every column including the two that\n"
        "% table does not print. The file is kept because sections/appendix_d_surveys.tex inputs\n"
        "% it by name; it emits nothing.\n")
    return dict(file=p.name, cols=0, width="--", rows=0, pt=0)


# --- the stubs that stand where a placeholder table used to ------------------------------------
# Two sections input a file by a name this generator never wrote, and each fell back to a
# hand-written placeholder that set a one-row table reading "Pending generation": two numbered
# tables and about a page and a half of nothing. The generator writes those names now, as files
# that emit nothing, and the labels the placeholders carried are attached to the real tables by
# `extra_labels` so that a cross reference written against them still resolves.
#
# `methods_full.tex` is the third. It was not a placeholder but an alias that input
# appendix_methods_full.tex, and appendix_a_method.tex inputs that file directly a few lines
# later as well, so the 112-row method table was set twice, end to end: that, and not the row
# count, is most of what made it eight pages. The alias emits nothing now and the direct input
# is the one that sets it.
STUBS = {
    "hands_full.tex": ("tab:hands_full", "appendix_hands_full.tex",
                       "the full hand table with its sources",
                       'set a one-row table reading "Pending generation"'),
    "rewards_full.tex": ("tab:rewards_full", "appendix_contact_models.tex",
                         "the per-paper reward extraction, which has never been generated",
                         'set a one-row table reading "Pending generation"'),
    "methods_full.tex": (None, "appendix_methods_full.tex",
                         "the full method table",
                         "input appendix_methods_full.tex, which the same section inputs again "
                         "by name, so the table was set twice"),
}


def write_stubs():
    out = []
    for name, (label, real, what, was) in STUBS.items():
        note = (f"\\label{{{label}}} is attached to {real} instead, so a reference to it still "
                f"resolves." if label else f"{real} is set by the direct input further down.")
        (OUT / name).write_text(
            "% generated by tools/make_tex_tables.py -- do not edit\n"
            f"% Stands where the hand-written stand-in for {what} used to be. That file\n"
            f"% {was}. This file emits nothing.\n"
            f"% {note}\n")
        out.append(dict(file=name, cols=0, width="--", rows=0, pt=0))
    return out


# --- the probe document, and what the compiler says about it ------------------------------------
PROBE = r"""%% Generated by tools/make_tex_tables.py. Inputs every generated table and nothing else,
%% so an overfull box in the log belongs to a table and not to the prose.
%% Build:  cd tex && TEXINPUTS=.:./sty:: pdflatex -interaction=nonstopmode tables_probe.tex
\documentclass[journal,twoside]{IEEEtran}
\input{preamble}
%% A row label carries \cite. The probe has no bibliography, so \cite is set to a three-digit
%% number here: that is the widest label the survey's 221 entries can produce, which makes the
%% probe's width measurement conservative rather than optimistic.
\renewcommand{\cite}[1]{[199]}
\begin{document}
\title{Table probe}
\author{}
\maketitle
\section{Body tables}
Each table below is flushed onto its own page, so the log attributes every overfull box to the
file that was open when it was set.
%(body)s
\appendices
%(appendix)s
\end{document}
"""


def write_probe(body_files, appendix_files):
    b = "\n".join(r"\input{tables/%s}\clearpage" % f[:-4] for f in body_files)
    a = "\n".join(r"\input{tables/%s}" % f[:-4] for f in appendix_files)
    (R / "tex" / "tables_probe.tex").write_text(PROBE % dict(body=b, appendix=a))


OVERFULL = re.compile(r"Overfull \\hbox \(([\d.]+)pt too wide\)")
OPENFILE = re.compile(r"\(\./tables/([A-Za-z0-9_]+)\.tex")


def compile_probe(threshold=20.0):
    """Run pdflatex on the probe and attribute each overfull box to the table file that was open.

    pdflatex reports an overfull box inside a tabular as the box is set, which is while the
    table's own file is the innermost open file, so the last file the log opened is the table the
    box belongs to."""
    import subprocess
    env = dict(**__import__("os").environ, TEXINPUTS=".:./sty::")
    for _ in range(2):
        p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "tables_probe.tex"],
                           cwd=str(R / "tex"), env=env, capture_output=True, text=True)
    log = (R / "tex" / "tables_probe.log").read_text(errors="ignore")
    counts, current, errors = {}, None, []
    for line in log.splitlines():
        for m in OPENFILE.finditer(line):
            current = m.group(1) + ".tex"
        m = OVERFULL.search(line)
        if m and float(m.group(1)) > threshold:
            counts[current] = counts.get(current, 0) + 1
        if line.startswith("! "):
            errors.append(line.strip())
    pages = re.search(r"Output written on tables_probe\.pdf \((\d+) pages", log)
    return counts, errors, (pages.group(1) if pages else "0"), p.returncode


# --- main --------------------------------------------------------------------------------------
BODY_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    body = [table1(), table2(), table3(), table4(), table5(), table6(), table7(), table8(),
            table9()]
    appendix = [appendix_methods(), appendix_hands(), appendix_contact(), appendix_protocol(),
                appendix_surveys()]
    appendix += write_stubs()
    write_probe([t["file"] for t in body], [t["file"] for t in appendix if t["rows"]])

    counts, errors, pages, rc = compile_probe()
    print(f"probe: {pages} pages, {len(errors)} errors")
    for e in errors[:8]:
        print("  !", e)
    hdr = f"{'table':<8}{'file':<30}{'cols':>5}{'width':>7}{'rows':>6}{'pt':>6}{'overfull>20pt':>15}"
    print(hdr)
    print("-" * len(hdr))
    for name, t in zip(BODY_ORDER, body):
        print(f"{name:<8}{t['file']:<30}{t['cols']:>5}{t['width']:>7}{t['rows']:>6}"
              f"{t['pt']:>6}{counts.get(t['file'], 0):>15}")
    print("-" * len(hdr))
    for t in appendix:
        print(f"{'app':<8}{t['file']:<30}{t['cols']:>5}{'two':>7}{t['rows']:>6}"
              f"{t['pt']:>6}{counts.get(t['file'], 0):>15}")
    unattributed = {k: v for k, v in counts.items() if k not in
                    {t["file"] for t in body + appendix}}
    if unattributed:
        print("overfull boxes outside a table file:", unattributed)
    if UNSUPPORTED:
        print(f"\n{len(UNSUPPORTED)} survey cells lost their anchor:")
        for u in UNSUPPORTED:
            print("  UNSUPPORTED", u)
    if UNCLASSIFIED:
        seen = {}
        for field, key, val in UNCLASSIFIED:
            seen.setdefault(field, []).append((key, val))
        print(f"\nvalues no controlled vocabulary matched ({len(UNCLASSIFIED)}):")
        for field, items in sorted(seen.items()):
            for key, val in items[:12]:
                print(f"  {field:16s} {key:34s} {val}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
