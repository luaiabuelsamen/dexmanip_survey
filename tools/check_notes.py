"""Flag notes that are short, missing the sources line, or contain no citation of a table/section."""
import re, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1] / "papers/notes"
bad = []
for f in sorted(R.glob("*.md")):
    if f.stem in {"TEMPLATE", "HOWTO", "HOWTO_METHOD"}: continue
    t = f.read_text(); n = t.count("\n")
    issues = []
    if n < 22: issues.append(f"short({n})")
    if "sources:" not in t.lower(): issues.append("no-sources-line")
    if not re.search(r"(Tab|Fig|Sec|§|papers/md|code/md)", t): issues.append("no-citation")
    if issues: bad.append((f.stem, ",".join(issues)))
print(f"{len(list(R.glob('*.md')))-3} notes; {len(bad)} flagged")
for k, i in bad: print(" ", k, i)
