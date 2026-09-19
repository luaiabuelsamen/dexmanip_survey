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
# Small counts read as words in a sentence and as figures in a table. The generated paragraphs are
# sentences, so they spell a count under ten.
WORD = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
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

# A replacement here is plain text, never LaTeX. tex() escapes the cell after these run, so a
# control space (`Univ.\ Pisa`) came out of the escaper as `Univ.\textbackslash{} Pisa` and printed
# a literal backslash in the Pisa/IIT maker cell.
MAKER_ABBREV = [
    (r"\bUniversity of ([A-Z][a-z]+)", r"Univ. \1"), (r"\bUniversity\b", "Univ."),
    (r"\bInstitute of Technology\b", "Inst. Tech."), (r"\bInstitute\b", "Inst."),
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


# --- where each table goes ------------------------------------------------------------------------
# One test decides it: does a reader read the table to follow the argument, or consult it to look a
# value up? What is read stays in the paper. What is consulted is reference material, and this
# survey's reference material is the repository, which carries every row as structured JSON under
# `corpus/rows/` and every table as markdown under `paper/tables/`. A survey that argues for
# checkable artefacts should point at its artefact rather than print it.
#
# Kept in the body: the proposed protocol and the empty results matrix, which are this survey's own
# contribution and are read, not consulted; the comparison to the predecessor surveys, which is the
# survey's positioning and belongs where the reader meets it rather than on page 39; and the
# task-family table, which is written by sections/02_taxonomy.tex rather than here.
#
# Kept in an appendix: the two hand tables and the simulator table. Sections III and IV reason over
# their individual cells -- which column is emptiest, which cell is blank and why -- so the prose
# does not stand up without them on the page.
#
# Withdrawn to the repository: everything else. Each entry says why, and the file is still written,
# as a comment that emits nothing, because a section inputs it by name.
WITHDRAWN = {
    "table4_rewards.tex":
        "the reward-term matrix. Consulted, not read, and the paper-against-code finding it "
        "carries is now made by a figure. paper/tables/table5_rewards.md",
    "table5_teleop.tex":
        "the teleoperation systems. A lookup table from beginning to end; Section V's argument is "
        "in its prose. paper/tables/table6_teleop.md",
    "table6_methods_top.tex":
        "the twenty most-mentioned methods. A ranked extract of a tabulation that is wholly "
        "reference material. paper/tables/table7_methods.md",
    "appendix_methods_full.tex":
        "all 112 method rows. Eight pages of a table nobody reads through. corpus/rows/",
    "appendix_hands_full.tex":
        "the source sentence behind every hand specification. Six pages of verbatim quotation, "
        "which is what the corpus is for. corpus/rows/ and papers/notes/",
    "appendix_contact_models.tex":
        "the contact-model and solver text behind the simulator vocabulary, verbatim. "
        "corpus/rows/ and papers/notes/",
    "appendix_protocol_long.tex":
        "the design of each protocol measurement and the reason for each count. Appendix E "
        "derives every one of them in prose. tools/make_eval_tables.py",
    "appendix_surveys_full.tex":
        "the full-length duplicate of the survey table, which no sentence in the paper referred "
        "to. paper/tables/table10_surveys.md",
}


def write_withdrawn(fname):
    """A table that is not in the paper: the file still exists, and emits nothing.

    The generator still builds the table above this call, so its column design, its emptiness
    count and its width assertion are all still exercised on every run and the table can be put
    back by deleting one line of WITHDRAWN.
    """
    why = WITHDRAWN[fname]
    (OUT / fname).write_text(
        "% generated by tools/make_tex_tables.py -- do not edit\n"
        f"% Withdrawn from the paper: {why}\n"
        "% Reference material belongs in the repository, not in the body of a survey that argues\n"
        "% for checkable artefacts. Appendix A says where the tabulation lives and how to read it.\n"
        "% This file emits nothing; it exists because a section inputs it by name.\n")
    return dict(file=fname, cols=0, width="--", rows=0, pt=0, withdrawn=True)


# --- the table writer ----------------------------------------------------------------------------
ALIGN = {"l": r">{\raggedright\arraybackslash\hspace{0pt}}p{%s}",
         "r": r">{\raggedleft\arraybackslash}p{%s}",
         "c": r">{\centering\arraybackslash}p{%s}"}


# --- what goes in the float, and what does not --------------------------------------------------
# Every table in this paper used to carry three text elements: a caption of about 44 words, the
# table, and a second paragraph under it at \scriptsize. The exemplar surveys carry one. So the
# caption is a label of at most 20 words, which says what the table shows and how many of its cells
# are empty and stops, and the paragraph that used to sit under the rules is written to its own
# file and set as body prose in the section that owns the table. It is the same words at the same
# size as the argument they belong to, in the place a reader meets them while reading rather than
# in six-point type under a float they have already turned away from.
CAPTION_WORDS = 20


def caption_words(caption):
    """The words a reader counts on the page, which is what the style measurement counted.

    A cross-reference sets one word, the number, so `\\ref{tab:protocol}` counts once and its key
    is not three words of punctuation. A label sets nothing. A glyph macro sets a mark rather than
    a word and counts for nothing, since the caption that carries the key to a three-level encoding
    is not made longer by the three marks in it.
    """
    t = re.sub(r"\\(eq)?ref\{[^}]*\}", " 1 ", caption)
    t = re.sub(r"\\label\{[^}]*\}", " ", t)
    t = re.sub(r"\\[a-zA-Z@]+", " ", t)
    t = re.sub(r"[{}$~\\&%_^]", " ", t)
    return len([w for w in re.split(r"[\s/]+", t) if re.search(r"[A-Za-z0-9]", w)])


def write_note(fname, note):
    """The table's explanatory paragraph, as body prose for the section that owns the table."""
    if not note:
        return None
    out = fname[:-4] + "_note.tex"
    (OUT / out).write_text(
        "% generated by tools/make_tex_tables.py -- do not edit\n"
        f"% The paragraph that belongs to tables/{fname}: what the columns mean and how they were\n"
        "% read. It is body prose, input by the section that owns the table, and not a second\n"
        "% block of small type inside the float.\n"
        + note + "\n")
    return out


# A zebra tint is a wide-table device: it keeps the eye on one row across many narrow columns, and
# Firoozi et al.'s is the one zebra in the corpus and the most legible wide table in it. Below seven
# columns it is ink for nothing, so it is switched on by column count rather than by habit.
ZEBRA_FROM_COLS = 7


def body_lines(body, ncols, zebra):
    """Body rows, with bold spanning rows where the rows group and a tint on alternate data rows.

    A row is either a list of cells or a `("group", label)` pair. A group row is the taxonomy the
    rows fall into, set bold across the table, as the contact-models comparison sets it. The tint
    alternates over data rows only, so a group row does not shift the stripes.
    """
    lines, n = [], 0
    for row in body:
        if isinstance(row, tuple) and row and row[0] == "group":
            lines.append(r"\addlinespace[2pt]" if n else "")
            lines.append(r"\multicolumn{%d}{@{}l}{\textbf{%s}} \\[1pt]" % (ncols, row[1]))
            continue
        n += 1
        tint = r"\rowcolor{wash} " if (zebra and n % 2 == 0) else ""
        lines.append(tint + " & ".join(row) + r" \\")
    return [l for l in lines if l != ""]


def data_rows(body):
    """The rows that carry data, i.e. everything that is not a group heading."""
    return [r for r in body if not (isinstance(r, tuple) and r and r[0] == "group")]


def write_table(fname, label, caption, cols, body, wide=True, env=None, colsep=3,
                size=r"\footnotesize", pos="!t", note=None, zebra=None, preamble=()):
    """One table file. `cols` is a list of (header, width in pt, alignment).

    Width discipline: the sum of the column widths plus 2*colsep per column must not exceed the
    text measure, 252 pt in one column and 516 pt in two. The sum is asserted here rather than
    discovered in the log, so a column added without taking width from another fails at generation
    time instead of silently overflowing the page.

    Caption discipline: the caption is asserted at or under 20 words, here rather than in a review.
    """
    measure = 516.0 if wide else 252.0
    total = sum(w for _, w, _ in cols) + 2 * colsep * len(cols)
    assert total <= measure, f"{fname}: {total:.0f} pt of column over a {measure:.0f} pt measure"
    words = caption_words(caption)
    assert words <= CAPTION_WORDS, f"{fname}: caption of {words} words over {CAPTION_WORDS}"
    if zebra is None:
        zebra = len(cols) >= ZEBRA_FROM_COLS
    env = env or ("table*" if wide else "table")
    spec = "".join(ALIGN[a] % f"{w:g}pt" for _, w, a in cols)
    head = " & ".join(r"\hdr{%s}" % h for h, _, _ in cols)
    lines = [
        f"% generated by tools/make_tex_tables.py -- do not edit",
        *preamble,
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
    lines += body_lines(body, len(cols), zebra)
    lines += [r"\bottomrule", r"\end{tabular}"]
    lines += [rf"\end{{{env}}}", ""]
    if fname in WITHDRAWN:
        return write_withdrawn(fname)
    (OUT / fname).write_text("\n".join(lines))
    return dict(file=fname, cols=len(cols), width="two" if wide else "one",
                rows=len(data_rows(body)), pt=round(total), caption_words=words,
                zebra=zebra, note=write_note(fname, note))


def write_longtable(fname, label, caption, cols, body, colsep=3, size=r"\scriptsize", note=None,
                    extra_labels=(), zebra=None):
    """An appendix longtable, run across both columns by switching to one-column mode."""
    total = sum(w for _, w, _ in cols) + 2 * colsep * len(cols)
    assert total <= 516.0, f"{fname}: {total:.0f} pt over a 516 pt measure"
    words = caption_words(caption)
    assert words <= CAPTION_WORDS, f"{fname}: caption of {words} words over {CAPTION_WORDS}"
    if zebra is None:
        zebra = len(cols) >= ZEBRA_FROM_COLS
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
    lines += body_lines(body, len(cols), zebra)
    lines += [r"\end{longtable}"]
    lines += [r"\twocolumn", r"\normalsize", ""]
    if fname in WITHDRAWN:
        return write_withdrawn(fname)
    (OUT / fname).write_text("\n".join(lines))
    return dict(file=fname, cols=len(cols), width="two (longtable, one-column mode)",
                rows=len(data_rows(body)), pt=round(total), caption_words=words, zebra=zebra,
                note=write_note(fname, note))


def emptiness(body, idx, kind):
    """How many of the counted cells are \\na, as a clause a caption can carry.

    The count stays in the caption, because how much of a table no source filled is part of what
    the table shows. What the counted columns are, and why the others are left out of the count,
    is in the paragraph the section carries.
    """
    cells = [row[i] for row in data_rows(body) for i in idx]
    n = sum(1 for c in cells if c.strip() == NA)
    return f"{n} of {len(cells)} {kind} cells are empty."


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
    cap = (r"Hands that can be obtained, sorted by joint count. "
           + emptiness(body, HAND_SPEC_IDX, "specification"))
    note = (r"Table~\ref{tab:hands-available} holds the hands that can be had: sold, open-source, "
            r"or with no release status stated. A row whose joint count no source states sorts "
            r"last rather than being ranked by a number nobody stated. Its empty-cell count covers "
            r"the eight specification columns, DoF through price; the hand, maker, open-hardware, "
            r"status and usage columns are left out of it because they are never blank and "
            r"counting them would dilute the finding. \emph{force N} is not a ranking: read "
            r"\emph{force kind} first, because pull-out resistance, pinch force, a fingertip "
            r"normal force under an indenter and an unlabelled vendor number are different "
            r"measurements. \emph{uses} counts the method rows whose own experiments run on that "
            r"hand.")
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
    cap = (r"Hands announced, prototyped or held internally, which cannot be obtained. "
           + emptiness(body, HAND_SPEC_IDX, "specification"))
    note = (r"Table~\ref{tab:hands-announced} carries the columns of "
            r"Table~\ref{tab:hands-available} plus the date of the claim and the class of artefact "
            r"it was read off, over the same eight specification columns. Its empty share is far "
            r"higher, and that is the finding of the table rather than a defect of it: an "
            r"unreleased hand is announced without a specification. \emph{evidence} is "
            r"\emph{datasheet} for a paper, datasheet or vendor specification page, \emph{video} "
            r"for a demonstration reel, \emph{press} for a press release or a third-party tracker. "
            r"\emph{claim date} prints \emph{undated} where the source page carries no date of its "
            r"own; a fetch date is not a claim date.")
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
    cap = (str(len(rows)) + r" simulators and physics engines, by contact formulation and "
           r"penetration exposure. " + emptiness(body, [1, 2, 3, 4, 5, 6, 7], "property"))
    shipped = "; ".join(
        r"\emph{%s} %s" % (tex(SUBJECT.get(r["key"], r["key"])), tex(", ".join(hands_shipped_names(r))))
        for r in rows if hands_shipped_names(r))
    note = (r"Table~\ref{tab:simulators} prints, for each engine, the contact formulation it names, "
            r"whether it exposes interpenetration depth and how many first-party hand models it "
            r"ships; its empty-cell count is over the seven property columns. "
            r"\emph{contact model} and \emph{solver} are controlled vocabularies: \emph{soft} for "
            r"a compliant or regularised contact, \emph{convex relaxation} for a convexified "
            r"formulation, \emph{complementarity} for an LCP, \emph{hard NCP} for a nonlinear "
            r"complementarity problem, \emph{impulse} for a velocity-level update, and "
            r"\emph{rigid, model unstated} where the source describes collision geometry but "
            r"names no contact law. The sentence each was read from runs to several hundred "
            r"characters; \texttt{corpus/rows/} carries each one verbatim, because "
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
    cap = (r"Reward-term families in the " + str(len(rows)) + r" methods whose objective was read "
           r"term by term. " + f"{blank} of {term_cells} term cells blank.")
    note = (r"The rows are the in-hand reorientation methods whose objective could be read term by "
            r"term. A blank term cell means the method does not use that family, and \emph{mismatch} is "
            r"the only column that carries \na, because no method that released no code can settle "
            r"it. A mark is \textbf{P} where the term is in the paper and either no code was released "
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
    cap = (str(len(rows)) + r" teleoperation and human-data systems, one per operator interface. "
           + emptiness(body, [1, 2, 3, 4, 5], "non-name"))
    note = (r"Table~\ref{tab:teleop} holds every corpus row that names an operator interface, and "
            r"counts empty cells over every column but the system name. "
            r"\emph{interface} is a "
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
    cap = (r"The " + str(METH_BODY_N) + r" most-mentioned method papers, by mentions in the other "
           r"parsed papers. " + emptiness(body, [2, 3, 4, 5, 6, 7, 8], "non-name"))
    note = (r"The ranking is on whole-word mentions in \path{papers/md}. All " + str(len(METHODS))
            + r" rows, with the DoF, bimanual and unseen-object columns restored, are in "
            r"Table~\ref{tab:app-methods}, and the empty-cell count here is over every column but "
            r"the method and the year. "
            r"A mention count is a count of mentions, not of use; by the rule of Section~VII the "
            r"counts are " + counts + r". \emph{penetration} is \emph{none} where the row's note "
            r"settles that the work does not address interpenetration, and \na where no note "
            r"settles it either way; no row in the corpus reports a penetration number for its "
            r"own trained policy. \emph{task} and \emph{paradigm} print the first two tags of a "
            r"row that carries more, marked with a trailing plus. \emph{simulator} is normalised "
            r"by the same rule \texttt{tools/check\_numbers.py} uses, which folds Isaac Gym "
            r"spellings together and keeps Isaac Lab apart from it.")
    return write_table("table6_methods_top.tex", "tab:methods-top", cap, cols, body, note=note)


# --- Table X: the nine artefact comparisons ------------------------------------------------------
# The finding this table carries is the one the survey publishes without having written to anybody
# first, so it is set as a claim about artefacts and nothing else: a repository, the commit that was
# fetched, the file inside it, the value the paper prints and the value the file contains. Every
# cell comes from the row's `mismatch_artifact` field, and the repository and commit inside that
# field are copied from corpus/code_manifest.json, so the table cannot name a commit the corpus did
# not fetch. Nothing here is a statement about what an author did.
def code_spans(s):
    """Backtick spans in a corpus string, set in monospace and breakable at their punctuation."""
    out, parts = [], str(s).split("`")
    for i, p in enumerate(parts):
        if i % 2 == 0:
            out.append(tex(p))
        else:
            body = tex(p)
            # A shipped identifier is long and has no hyphen, so it needs its own break points:
            # after each separator, and at every camelCase boundary. Without the second one
            # `actionDeltaPenaltyScale` sets 50 pt wider than its column.
            body = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", r"\\allowbreak{}", body)
            for ch in ("_", "/", "."):
                body = body.replace(tex(ch), tex(ch) + r"\allowbreak{}")
            out.append(r"\texttt{" + body + "}")
    return "".join(out)


def path_tt(p):
    """A path inside a repository, breakable at every separator so a long one wraps in its cell."""
    return code_spans("`" + str(p) + "`")


def repo_cell(art):
    """The repository, as owner/name, with the short commit under it."""
    slug = re.sub(r"^https?://github\.com/", "", art["repo"]).rstrip("/")
    owner, _, name = slug.partition("/")
    return (r"\texttt{%s/}\allowbreak{}\texttt{%s}\newline\texttt{%s}"
            % (tex(owner), tex(name), tex(art["commit"][:10])))


def table10():
    rows = [r for r in METHODS if r.get("mismatch_class") == "contradiction"]
    rows.sort(key=lambda r: (r.get("year") or 0, r["key"]))
    missing = [r["key"] for r in rows if not r.get("mismatch_artifact")]
    assert not missing, f"contradiction rows with no mismatch_artifact: {missing}"
    body = []
    for r in rows:
        a = r["mismatch_artifact"]
        body.append([
            subject(r["key"]),
            repo_cell(a),
            path_tt(a["file"]) + r"\newline " + code_spans("`" + a["locator"] + "`"),
            code_spans(a["paper"]),
            code_spans(a["code"]),
        ])
    # The method column is wide enough for the longest name to set unhyphenated: at 46 pt the
    # probe broke PianoMime as "Pi-anoMime", which is a name a reader has to reassemble.
    cols = [("method", 58, "l"), ("repository, fetched commit", 86, "l"),
            ("file in it, and where", 98, "l"), ("what the paper prints", 114, "l"),
            ("what that file contains", 114, "l")]
    cap = (r"The " + str(len(rows)) + r" rows where a paper and its released repository state "
           r"different values, each at the commit this survey fetched.")
    note = (r"Table~\ref{tab:codegap} is the whole of the paper-against-code finding, in the form "
            r"the finding is made: a public repository, the commit \texttt{tools/fetch\_code.py} "
            r"cloned, the file inside it, and the two values. \emph{file in it, and where} gives "
            r"the path as that repository spells it and, beneath it, the function, configuration "
            r"key or branch the value sits in. \emph{what the paper prints} names the table or "
            r"equation the value was read from. \emph{what that file contains} is what is in the "
            r"parsed copy under \path{code/md}, which is the same snapshot every other claim in "
            r"this survey about that repository is made from. The commit is the one in "
            r"\texttt{corpus/code\_manifest.json}, printed to ten characters; the rows print the "
            r"comparison and Appendix~\ref{app:rewards} prints each row's full text, its "
            r"confidence and any review note. No cell states a cause, and none is a claim about "
            r"what the work's authors did: a reader with a browser settles every line of this "
            r"table without asking anyone.")
    return write_table("table10_codegap.tex", "tab:codegap", cap, cols, body, note=note,
                       size=r"\scriptsize")



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
    cap = (r"Every method row in the corpus, on the columns Table~\ref{tab:methods-top} cuts. "
           + emptiness(body, idx, "non-name"))
    note = (r"All " + str(len(ROWS)) + r" method rows are here, and the empty-cell count is over "
            r"every column but the method and the year. "
            r"\emph{hand} is the first end effector the row names, without the arm it hangs on, "
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
    cap = (r"The descriptions behind the vocabulary of Table~\ref{tab:simulators}, verbatim and "
           r"uncut. " + emptiness(body, [1, 2], "description"))
    note = (r"These cells run to several hundred characters each, which is why the body table "
            r"prints a vocabulary instead: a 480-character cell in a body float is a paragraph "
            r"printed sideways.")
    return write_longtable("appendix_contact_models.tex", "tab:app-contact", cap, cols, body,
                           colsep=2, note=note)


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
    cap = (r"The sentences behind the vocabularies of Tables~\ref{tab:hands-available} "
           r"and~\ref{tab:hands-announced}, all " + str(len(rows)) + r" hands. "
           + emptiness(body, [1, 2, 3, 4, 5], "description"))
    note = (r"The maker column is not repeated here; Tables~\ref{tab:hands-available} "
            r"and~\ref{tab:hands-announced} carry it, and the width it used goes to the sentences "
            r"this table exists to print. \emph{caveat on the row} is the \texttt{spec\_caveat} "
            r"field, which is where a figure with no reachable source is named as such; it is "
            r"empty for a row that carries no caveat rather than for a row nobody checked. Cells "
            r"are cut at a word boundary where they would otherwise run past the page; "
            r"\texttt{corpus/rows/} holds every field at full length.")
    return write_longtable("appendix_hands_full.tex", "tab:app-hands", cap, cols, body, colsep=2,
                           note=note)


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
    cap = (r"The proposed evaluation protocol, and this survey's own contribution. No cell is "
           r"empty: every cell is a proposal.")
    # No note under this table. What used to be here was a typographic aside, a pointer to the
    # long form in the appendix, and the bill: and Section VII's own prose derives the bill in
    # sentences, "342 real rollouts on the matched set and 600 on the unseen-object set, 942 in
    # all", against 1200 on the independent-arm count. The paragraph said nothing the section did
    # not, so it is deleted rather than moved. The assertion keeps it that way.
    body_prose = (R / "tex/sections/07_evaluation.tex").read_text()
    for n in (matched, unseen, total, old):
        assert str(n) in body_prose, f"Section VII no longer states the bill figure {n}"
    return write_table("table7_protocol.tex", "tab:protocol", cap, cols, body)


def appendix_protocol():
    rows = protocol_source()
    body = [[md_to_tex(c[0]), md_to_tex(c[2]), md_to_tex(c[5])] for c in rows]
    cols = [("axis", 56, "l"), ("how the measurement is made", 208, "l"),
            ("why the count is what it is", 208, "l")]
    cap = (r"The two columns Table~\ref{tab:protocol} leaves out, verbatim. No cell is empty; the "
           r"axes match row for row.")
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
    body = [("group", "A worked example. Every number in this row is fabricated"),
            [r"\emph{worked example}"] + EXAMPLE_SHORT,
            ("group", "The %d most-mentioned methods. No cell below has been measured"
                      % len(picked))]
    for _, k, _, kind in picked:
        body.append([subject(k) + (r"$\ast$" if kind == "title" else "")] + [""] * len(AXES_SHORT))
    cells = len(picked) * len(AXES_SHORT)
    counts = "; ".join(f"{tex(SUBJECT.get(k, k))}~{n}" for n, k, _, _ in picked)
    cols = [("method", 86, "l")] + [(a, 54, "l") for a in AXES_SHORT]
    # "All 84 cells are empty" printed directly above the filled worked example reads as false to a
    # reader who looks at the table before the text, so the caption says which 84 and what the
    # first row is.
    cap = (r"The matrix, for someone else to fill: " + str(len(picked)) + r" methods against "
           r"Table~\ref{tab:protocol}. All " + str(cells) + r" method cells empty; row one "
           r"fabricated.")
    # The section already states the ranking rule, the whole-word correction, the $\ast$ mark and
    # the fabricated first row, in its own prose. The one thing it cannot state without the
    # generator is the counts themselves, so they are written as a sentence the section inputs
    # where it promises them, and the rest of the old note is deleted as duplication.
    (OUT / "table8_matrix_counts.tex").write_text(
        "% generated by tools/make_tex_tables.py -- do not edit\n"
        "% The mention counts behind the ranking of tables/table8_matrix.tex, as a sentence for the\n"
        "% body of Section VII, which is where the ranking rule they follow from is stated.\n"
        "The counts, on whole-word matches over \\path{papers/md}, are " + counts + ".\n")
    return write_table("table8_matrix.tex", "tab:matrix", cap, cols, body)


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


# The three-level encoding, as the Isaac Sim review sets it: a tick, a hollow circle and a cross.
# That matrix decoded at a glance where the nine-engines review's grid of ++/+/-/-- at 6 pt did
# not, and the difference is that a shape is read without being decoded while a sign has to be
# looked up. The macros are defined in the table's own file, guarded, so the paper's preamble does
# not carry a command used by one table.
GLYPH_DEFS = [
    r"\providecommand{\cvyes}{\textcolor{accent}{$\checkmark$}}",
    r"\providecommand{\cvpart}{\textcolor{accent}{$\circ$}}",
    r"\providecommand{\cvno}{\textcolor{black!40}{$\times$}}",
]
GLYPH = {"full": r"\cvyes", "part": r"\cvpart", "none": r"\cvno", None: NA}
SURVEY_MATRIX_COLS = [("scope", "dexterous scope"), ("taxonomy", "taxonomy"),
                      ("bimanual", "bimanual"), ("hardware", "hardware"),
                      ("evaluation", "evaluation"), ("gaps", "gaps named")]


def table9():
    """The comparison to prior surveys, as a matrix on page 2 or 3 rather than prose on page 39.

    None of the sixteen surveys this paper was measured against carries a comparison-to-prior-work
    table; four of them do the comparison in prose and one buries it in a subsection of a
    212-page document. This survey has the comparison, over fourteen works on one set of columns,
    and it was prose in an appendix while the generator emitted nothing. So it is set here as the
    matrix it always was: fourteen rows, the repository's own six columns, three levels a reader
    decodes without a key, and the prose kept in Appendix~D, which is what a glyph is checked
    against.

    The rows group by what the predecessor is, which is a taxonomy and not a column: surveys of the
    field, simulator and contact-model studies, and the four works whose sources this survey never
    read. The third group is the honest part of the positioning and it is bold across the table
    rather than a footnote to it.
    """
    rows = SV.load_rows()
    sim_keys = SV.sim_bib_keys()
    order = sorted(rows, key=lambda k: (-(rows[k].get("year") or 0), k))
    grouped, unread, unobtained = {g: [] for g, _ in SV.GROUPS}, 0, 0
    for k in order:
        note = SV.note_text(k)
        spec = SV.SPEC.get(k, {})
        if not spec:
            if SV.fetched_but_unread(k, note):
                unread += 1
            else:
                unobtained += 1
            grouped["unread"].append([subject(k), num(rows[k].get("year"))]
                                     + [NA] * len(SURVEY_MATRIX_COLS))
            continue
        cells = []
        for col, _ in SURVEY_MATRIX_COLS:
            lv = SV.level(k, col, note)
            if lv is None:
                UNSUPPORTED.append(f"{k}.{col}: anchor gone from the note, so no level is printed")
            cells.append(GLYPH[lv])
        grouped["engine" if k in sim_keys else "field"].append(
            [subject(k), num(rows[k].get("year"))] + cells)
    body = []
    for g, title in SV.GROUPS:
        if not grouped[g]:
            continue
        body.append(("group", title))
        body += grouped[g]
    cols = ([("survey", 120, "l"), ("yr", 18, "r")]
            + [(h, 57, "c") for _, h in SURVEY_MATRIX_COLS])
    idx = list(range(2, 2 + len(SURVEY_MATRIX_COLS)))
    cap = (r"What " + str(len(data_rows(body))) + r" predecessor surveys cover: \cvyes\ covered, "
           r"\cvpart\ partly, \cvno\ not. " + emptiness(body, idx, "coverage"))
    note = (r"A cell is a level and not a score: \cvyes\ where the work gives the topic a "
            r"structure of its own, a section, a table or a measurement it defines; \cvpart\ where "
            r"the topic is there without one, a subsection with no analysis, a handful of "
            r"mentions, or a metric named and never defined; \cvno\ where it is absent or put "
            r"outside the work's scope. Each level coarsens one sentence read from "
            r"\path{papers/notes/<key>.md}, and it is printed only while the quotation behind that "
            r"sentence is still in the note, so a glyph cannot outlive its evidence. The sentences "
            r"themselves are Appendix~\ref{app:surveys} and "
            r"\path{paper/tables/table10_surveys.md}. " + WORD[unobtained].capitalize() + r" of the fourteen "
            r"sources could not be obtained and " + WORD[unread] + r" is on disk and has never "
            r"been read, which is why their cells are empty; they are grouped as such rather than "
            r"scored, because this survey knows nothing of them beyond a title and a DOI. The "
            r"\emph{gaps named} column is uniform by design: every predecessor names gaps, and "
            r"what none of them attaches to a gap is a measurement.")
    t = write_table("table9_surveys.tex", "tab:surveys", cap, cols, body, colsep=2, note=note,
                    preamble=GLYPH_DEFS)
    # The level and the sentence it coarsens, printed side by side, so the coarsening can be
    # audited against the prose without opening two files.
    t["levels"] = [(k, col, SV.level(k, col, SV.note_text(k)), SV.SPEC[k][col][0])
                   for k in order if SV.SPEC.get(k) for col, _ in SURVEY_MATRIX_COLS]
    return t


def appendix_surveys():
    """The full-length duplicate of the survey table. Withdrawn; see WITHDRAWN."""
    return write_withdrawn("appendix_surveys_full.tex")


# --- the stubs that stand where a placeholder table used to ------------------------------------
# Four sections input a file by a name this generator never wrote. Each fell back to a hand-written
# stand-in: two set a one-row table reading "Pending generation", which took a table number and
# most of a page each, and one input the 112-row method table a second time, end to end. The
# generator writes those names now, as files that emit nothing.
STUBS = {
    "hands_full.tex": "the full hand table with its sources",
    "rewards_full.tex": "the per-paper reward extraction, which was never generated",
    "methods_full.tex": "the full method table, which this file used to input a second time",
}
# `surveys.tex` used to be a fifth stub, standing in for the survey table in Appendix D and
# emitting nothing. The survey table is Table IX now, set in Section I, so the stub has nothing to
# stand in for and the file is gone.


def write_stubs():
    out = []
    for name, what in STUBS.items():
        (OUT / name).write_text(
            "% generated by tools/make_tex_tables.py -- do not edit\n"
            f"% Stands where the hand-written stand-in for {what} used to be. That file set a\n"
            '% one-row table reading "Pending generation", or input a table a second time. The\n'
            "% tabulation itself is in the repository now; Appendix A says where. This file\n"
            "% emits nothing, and exists because a section inputs it by name.\n")
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


def write_probe(body_files, appendix_files, notes=()):
    b = "\n".join(r"\input{tables/%s}\clearpage" % f[:-4] for f in body_files)
    a = "\n".join(r"\input{tables/%s}" % f[:-4] for f in appendix_files)
    n = "\n\n".join(r"\input{tables/%s}" % f[:-4] for f in notes)
    if n:
        a += "\n\section{The paragraphs the floats no longer carry}\n" + n
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
BODY_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    body = [table1(), table2(), table3(), table4(), table5(), table6(), table7(), table8(),
            table9(), table10()]
    appendix = [appendix_methods(), appendix_hands(), appendix_contact(), appendix_protocol(),
                appendix_surveys()]
    appendix += write_stubs()
    notes = [t["note"] for t in body + appendix if t.get("note")]
    write_probe([t["file"] for t in body], [t["file"] for t in appendix if t["rows"]], notes)

    counts, errors, pages, rc = compile_probe()
    print(f"probe: {pages} pages, {len(errors)} errors")
    for e in errors[:8]:
        print("  !", e)
    hdr = (f"{'table':<6}{'file':<30}{'cols':>5}{'rows':>5}{'pt':>5}{'cap words':>10}"
           f"{'zebra':>7}{'note':>6}{'overfull>20pt':>14}")
    print(hdr)
    print("-" * len(hdr))
    for name, t in list(zip(BODY_ORDER, body)) + [("app", t) for t in appendix]:
        print(f"{name:<6}{t['file']:<30}{t['cols']:>5}{t['rows']:>5}{t['pt']:>5}"
              f"{t.get('caption_words', '--'):>10}{('yes' if t.get('zebra') else 'no'):>7}"
              f"{('yes' if t.get('note') else 'no'):>6}{counts.get(t['file'], 0):>14}")
    unattributed = {k: v for k, v in counts.items() if k not in
                    {t["file"] for t in body + appendix}}
    if unattributed:
        print("overfull boxes outside a table file:", unattributed)
    levels = next((t["levels"] for t in body if t.get("levels")), [])
    if levels:
        print(f"\nthe {len(levels)} coverage levels, each beside the sentence it coarsens:")
        for key, col, lv, prose in levels:
            print(f"  {key:34s} {col:11s} {str(lv):5s} {prose[:78]}")
    for pb in SV.level_problems():
        print("  LEVEL", pb)
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
