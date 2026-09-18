"""Assemble paper/survey.md from paper/sections/*.md, inserting the generated tables and figures."""
import re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
S, T, F = R / "paper/sections", R / "paper/tables", R / "paper/figures"
HEAD = """# Dexterous Manipulation, Single-Hand and Bimanual

## Machines, simulators, and how policies are trained

A survey of %d works, with an evaluation frame and the gaps it exposes.

*Compiled %s. Every claim traces to a note in `papers/notes/`, every note to a parsed source in
`papers/md/` or `code/md/`, and every source to a hash or commit in `corpus/manifest.json`. The
method is in Appendix A.*

---

"""
def main():
    import json, glob, datetime
    n = len(glob.glob(str(R / "corpus/rows/*.json")))
    parts = [HEAD % (n, datetime.date.today().isoformat())]
    for f in sorted(S.glob("*.md")):
        txt = f.read_text()
        # inline any table referenced as {{table:NAME}}
        for m in re.findall(r"\{\{table:([a-z0-9_]+)\}\}", txt):
            p = T / f"{m}.md"
            txt = txt.replace("{{table:%s}}" % m, p.read_text() if p.exists() else f"*[missing table {m}]*")
        for m in re.findall(r"\{\{figure:([a-z0-9_]+)\}\}", txt):
            p = F / f"{m}.svg"
            txt = txt.replace("{{figure:%s}}" % m, f"![{m}](figures/{m}.svg)" if p.exists() else f"*[missing figure {m}]*")
        parts.append(txt.rstrip() + "\n")
    parts.append("\n---\n\n## Appendix A. Method\n\n" + (R / "paper/METHOD.md").read_text().split("\n", 2)[2])
    out = "\n".join(parts)
    (R / "paper/survey.md").write_text(out)
    words = len(out.split())
    print(f"survey.md: {words} words, {out.count(chr(10))} lines")
    missing = re.findall(r"\*\[missing (table|figure) ([a-z0-9_]+)\]\*", out)
    if missing: print("MISSING:", missing)
    keys = set(re.findall(r"`([a-z][a-z0-9_]{4,})`", out))
    import os
    unknown = [k for k in keys if not os.path.exists(R / f"papers/notes/{k}.md") and "_" in k and re.search(r"_\d{4}$", k)]
    print(f"cited keys: {len(keys)}; citations with no note: {unknown}")
