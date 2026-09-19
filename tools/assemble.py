"""Assemble paper/survey.md from paper/sections/*.md, inserting the generated tables and figures.

Three things this script is responsible for beyond concatenation.

The byline. The markdown edition carries the same author and address as the LaTeX edition,
because Section 5.6 offers nine named research groups a correction route and that route is the
address: an edition without it strands the disclosure.

The front-matter count. "Works" is not one number. The corpus holds one count of bibliography
entries, a smaller count of entries that were read into a structured row, and a smaller count
again of entries with a parsed source on disk. The header states the first two and names the
eight row classes, because a survey whose argument is that a number needs its denominator cannot
open with a bare integer. The numbers are counted here at assembly time, never typed in.

The abstract. paper/ABSTRACT.md is inserted directly after the title block, before Section 1.

Author comments. An HTML comment in a section is a note to whoever is writing that section. It is
not part of the manuscript and is stripped here, so a to-do list cannot ship inside the document.
"""
import re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
S, T, F = R / "paper/sections", R / "paper/tables", R / "paper/figures"

# The row classes, in the order the front matter lists them, with the words the prose uses for
# each. A class appearing in the rows and missing here is still counted, under its own name.
CLASS_LABELS = [("method", "method papers"), ("hand", "hands"), ("simulator", "simulators"),
                ("dataset", "datasets"), ("benchmark", "benchmarks"), ("survey", "surveys"),
                ("sensor", "tactile sensors"), ("eval-protocol", "evaluation protocols")]

HEAD = """# Learning Dexterous Manipulation

## Hands, simulators, training, and evaluation

Luai Abuelsamen, `luai_abuelsamen@berkeley.edu`. Corrections go to that address, which is the
route section 5.6 names; the corpus is available from the author and is not yet deposited.

A survey of %d bibliography entries, %d of which carry a structured row read from a note: %s.
"Method row" throughout means one of the %d, and every headline count here has one of those eight
classes as its denominator.

*Compiled %s. Every claim traces to a note in `papers/notes/`, every note to a parsed source in
`papers/md/` or `code/md/`, and every source to a hash or commit in `corpus/manifest.json`. The
method is in Appendix A.*

---

"""

def expand(txt):
    """Inline the generated tables and figures a section or appendix references, and drop any
    HTML comment. A missing table or figure is reported in the text rather than skipped."""
    for m in re.findall(r"\{\{table:([a-z0-9_]+)\}\}", txt):
        p = T / f"{m}.md"
        txt = txt.replace("{{table:%s}}" % m, p.read_text() if p.exists() else f"*[missing table {m}]*")
    for m in re.findall(r"\{\{figure:([a-z0-9_]+)\}\}", txt):
        p = F / f"{m}.svg"
        txt = txt.replace("{{figure:%s}}" % m, f"![{m}](figures/{m}.svg)" if p.exists() else f"*[missing figure {m}]*")
    txt, n = re.subn(r"[ \t]*<!--.*?-->[ \t]*\n?", "", txt, flags=re.S)
    return txt, n

def counts():
    """The three front-matter numbers, counted from the corpus rather than stated."""
    import json, glob
    bib = json.loads((R / "corpus/bib.json").read_text())
    # Entries with topic "related" are prior work cited from outside the dexterous-manipulation
    # corpus. They carry no row and enter no count, so they are not part of this total.
    entries = sum(1 for e in bib if e.get("topic") != "related")
    rows = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
    seen = {}
    for r in rows:
        seen[r.get("class")] = seen.get(r.get("class"), 0) + 1
    named = [(c, lab) for c, lab in CLASS_LABELS if c in seen]
    named += [(c, c) for c in sorted(seen) if c not in dict(CLASS_LABELS)]
    parts = [f"{seen[c]} {lab}" for c, lab in named]
    breakdown = ", ".join(parts[:-1]) + " and " + parts[-1]
    return entries, len(rows), breakdown, seen.get("method", 0)

def main():
    import datetime
    entries, nrows, breakdown, nmethod = counts()
    parts = [HEAD % (entries, nrows, breakdown, nmethod, datetime.date.today().isoformat())]
    parts.append((R / "paper/ABSTRACT.md").read_text().rstrip() + "\n\n---\n")
    stripped = 0
    for f in sorted(S.glob("*.md")):
        txt, n = expand(f.read_text())
        stripped += n
        parts.append(txt.rstrip() + "\n")
    parts.append("\n---\n\n## Appendix A. Method\n\n" + (R / "paper/METHOD.md").read_text().split("\n", 2)[2])
    # The reader-facing article keeps only the hardware and engine reference tables. The detailed
    # discrepancy catalogue, predecessor audit, and protocol derivations are a supplement in both
    # editions so the Markdown build cannot silently grow a different paper from the LaTeX build.
    for letter in ("B",):
        p = R / f"paper/APPENDIX_{letter}.md"
        if p.exists():
            txt, n = expand(p.read_text()); stripped += n
        else:
            txt, n = f"*[missing appendix {letter}]*\n", 0
        parts.append("\n---\n\n" + txt)
    out = "\n".join(parts)
    (R / "paper/survey.md").write_text(out)
    supplement = ["# Learning Dexterous Manipulation: Technical Supplement\n"]
    supplement.append("Detailed evidence for the paper--code comparisons, predecessor-survey "
                      "coding, and evaluation-protocol calculations.\n")
    for letter in ("C", "D", "E"):
        p = R / f"paper/APPENDIX_{letter}.md"
        if p.exists():
            txt, n = expand(p.read_text()); stripped += n
        else:
            txt = f"*[missing appendix {letter}]*\n"
        supplement.append("\n---\n\n" + txt.rstrip() + "\n")
    (R / "paper/supplement.md").write_text("\n".join(supplement))
    words = len(out.split())
    print(f"survey.md: {words} words, {out.count(chr(10))} lines")
    print(f"front matter: {entries} entries, {nrows} rows ({breakdown})")
    print(f"author comments stripped: {stripped}")
    em = out.count("—")
    if em: print(f"em-dashes in the assembled document: {em} (the brief forbids them)")
    missing = re.findall(r"\*\[missing (table|figure|appendix) ([A-Za-z0-9_]+)\]\*", out)
    if missing: print("MISSING:", missing)
    keys = set(re.findall(r"`([a-z][a-z0-9_]{4,})`", out))
    import os, json as _json
    # Entries with topic "related" are prior work cited from outside the corpus. No source for them
    # was parsed, so they have no note by construction and are not a missing-note report.
    related = {e["key"] for e in _json.loads((R / "corpus/bib.json").read_text())
               if e.get("topic") == "related"}
    unknown = [k for k in keys if not os.path.exists(R / f"papers/notes/{k}.md") and "_" in k
               and re.search(r"_\d{4}$", k) and k not in related]
    print(f"cited keys: {len(keys)}; citations with no note: {unknown}; "
          f"related-work citations, which have none by design: {len(keys & related)}")

if __name__ == "__main__":
    main()
