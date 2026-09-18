"""Merge corpus/bib_<topic>.json into corpus/bib.json, deduplicating on arXiv id and normalised title."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / "corpus"
def norm(t): return re.sub(r"[^a-z0-9]", "", (t or "").lower())
seen_arxiv, seen_title, out = {}, {}, []
for f in sorted(ROOT.glob("bib_*.json")):
    if f.name == "bib_smoke.json": continue
    try: entries = json.loads(f.read_text())
    except Exception as ex: print(f"[bad json] {f.name}: {ex}"); continue
    for e in entries:
        aid = re.sub(r"v\d+$", "", (e.get("arxiv") or "").strip()) or None
        e["arxiv"] = aid
        t = norm(e.get("title"))
        dup = (aid and aid in seen_arxiv) or (t and t in seen_title)
        if dup:
            prev = seen_arxiv.get(aid) or seen_title.get(t)
            prev.setdefault("also_topics", []).append(e.get("topic"))
            if not prev.get("github") and e.get("github"): prev["github"] = e["github"]
            continue
        keys = {x["key"] for x in out}
        if e["key"] in keys: e["key"] = e["key"] + "_" + (e.get("topic") or "x")
        out.append(e)
        if aid: seen_arxiv[aid] = e
        if t: seen_title[t] = e
    print(f"{f.name}: {len(entries)} entries")
Path(ROOT / "bib.json").write_text(json.dumps(out, indent=1))
print(f"merged: {len(out)}; with arxiv: {sum(1 for e in out if e['arxiv'])}; with github: {sum(1 for e in out if e.get('github'))}; verified: {sum(1 for e in out if e.get('verified'))}")
