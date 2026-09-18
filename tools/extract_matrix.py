"""Pull a coarse per-paper matrix out of the notes: paradigm, hand, simulator, bimanual,
real-robot, and whether interpenetration is addressed. Regex over notes, so it is a screening
tool: every cell that reaches the survey is confirmed by reading the note."""
import json, re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
bib = {e["key"]: e for e in json.loads((R / "corpus/bib.json").read_text())}
rows = []
for f in sorted((R / "papers/notes").glob("*.md")):
    k = f.stem
    if k in {"TEMPLATE", "HOWTO", "HOWTO_METHOD"} or k not in bib: continue
    t = f.read_text(errors="ignore"); lo = t.lower()
    def has(p): return bool(re.search(p, lo))
    para = []
    if has(r"\bppo\b|reinforcement learning|\brl\b"): para.append("RL")
    if has(r"behaviou?r cloning|imitation|diffusion polic|action chunk|flow matching"): para.append("IL")
    if has(r"vision-language-action|\bvla\b"): para.append("VLA")
    if has(r"model predictive|trajectory optimi|sampling-based mpc"): para.append("MPC")
    hands = [h for h, p in [("Shadow", r"shadow"), ("Allegro", r"allegro"), ("LEAP", r"leap hand"),
             ("Inspire", r"inspire"), ("Ability", r"psyonic|ability hand"), ("XHand", r"xhand"),
             ("gripper", r"parallel.?jaw|gripper"), ("TriFinger", r"trifinger")] if has(p)]
    sims = [s for s, p in [("MuJoCo", r"mujoco"), ("IsaacGym", r"isaac ?gym"), ("IsaacLab", r"isaac ?lab"),
            ("SAPIEN/ManiSkill", r"sapien|maniskill"), ("PyBullet", r"pybullet"), ("Genesis", r"genesis")] if has(p)]
    pen = "penalised" if has(r"penetration penalt|penali[sz]e.{0,20}penetration") else \
          "measured" if has(r"penetration (depth|volume|is measured)|interpenetration.{0,30}(measur|report|metric)") else \
          "not addressed" if has(r"not addressed|does not address") else "unclear"
    rows.append(dict(key=k, topic=bib[k].get("topic"), year=bib[k].get("year"),
                     paradigm="+".join(para) or "-", hands="/".join(hands) or "-",
                     sims="/".join(sims) or "-",
                     bimanual="yes" if has(r"bimanual|two hands|both hands") else "no",
                     real="yes" if has(r"real.?robot|real.?world experiment") else "no",
                     penetration=pen))
(R / "corpus/matrix.json").write_text(json.dumps(rows, indent=1))
from collections import Counter
print(len(rows), "rows")
for field in ["paradigm", "penetration", "bimanual", "real"]:
    print(f"\n{field}:", dict(Counter(r[field] for r in rows).most_common(8)))
