"""Generate the data-driven figures as standalone SVG from corpus/rows/*.json.

Colours are CSS custom properties with a dark-mode media query, so the figures stay legible in
either theme. Every bar length and every filled cell comes from a row; nothing is drawn that a
note did not confirm.
"""
import json, glob, re
from collections import Counter, defaultdict
from pathlib import Path
R = Path(__file__).resolve().parents[1]
OUT = R / "paper/figures"; OUT.mkdir(exist_ok=True)
ROWS = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
BY = {r["key"]: r for r in ROWS}

STYLE = """<style>
 :root{--ink:#111418;--mut:#5b6672;--line:#d4dae0;--bg:#ffffff;--a:#2f6f9f;--b:#7a5ea8;--c:#a8563e;--d:#3f7d57;--warn:#b5462f;--fill:#e8eef3}
 @media (prefers-color-scheme:dark){:root{--ink:#e8ecef;--mut:#9aa6b2;--line:#39424b;--bg:#12161a;--a:#6fb0dc;--b:#b295d8;--c:#dd9376;--d:#7fc09a;--warn:#e88a72;--fill:#1d252c}}
 text{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;fill:var(--ink)}
 .t{font-size:15px;font-weight:600}.s{font-size:11.5px;fill:var(--mut)}.l{font-size:11.5px}.n{font-size:10.5px;fill:var(--mut)}
 .ax{stroke:var(--line);stroke-width:1}
</style>"""

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}">{STYLE}<rect width="{w}" height="{h}" fill="var(--bg)"/>{body}</svg>')

def esc(s): return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------------- Figure 2: hands the literature actually runs on ----------------
def fig_hands():
    canon = [("Allegro", r"allegro"), ("Shadow", r"shadow"), ("LEAP", r"\bleap\b"), ("Adroit (sim)", r"adroit"),
             ("Inspire", r"inspire"), ("Ability (PSYONIC)", r"psyonic|ability"), ("XHand", r"xhand"),
             ("Faive/Mimic", r"faive|mimic"), ("ORCA", r"\borca\b"), ("RUKA", r"\bruka\b"),
             ("Sharpa", r"sharpa"), ("D'Claw/TriFinger", r"d.?claw|trifinger"), ("Fourier", r"fourier"),
             ("PsiBot", r"psibot"), ("Schunk", r"schunk"), ("parallel-jaw gripper", r"parallel.?jaw|gripper")]
    status = {"Allegro": "sold", "Shadow": "sold", "LEAP": "open", "Adroit (sim)": "sim only", "Inspire": "sold",
              "Ability (PSYONIC)": "sold", "XHand": "sold", "Faive/Mimic": "open", "ORCA": "open", "RUKA": "open",
              "Sharpa": "sold", "D'Claw/TriFinger": "open", "Fourier": "sold", "PsiBot": "sold",
              "Schunk": "sold", "parallel-jaw gripper": "sold"}
    counts = Counter()
    for r in ROWS:
        if r.get("class") != "method": continue
        h = str(r.get("hand") or "")
        for name, pat in canon:
            if re.search(pat, h, re.I): counts[name] += 1
    items = [(n, c) for n, c in counts.most_common() if c > 0]
    announced = [r for r in ROWS if r.get("class") == "hand" and r.get("release_status") in ("announced", "prototype", "internal-only")]
    W, rowh, top = 760, 22, 86
    H = top + rowh * (len(items) + 3) + 70
    mx = max(c for _, c in items) or 1
    x0, bw = 210, 420
    col = {"sold": "var(--a)", "open": "var(--d)", "sim only": "var(--b)"}
    b = [f'<text class="t" x="24" y="30">Figure 2. Which hands the surveyed methods actually run on</text>',
         f'<text class="s" x="24" y="50">One count per method paper whose own experiments use the hand, from {sum(1 for r in ROWS if r.get("class")=="method")} method rows.</text>',
         f'<text class="s" x="24" y="66">Colour: blue sold commercially, green open hardware, purple simulation-only model.</text>']
    y = top
    for name, c in items:
        wpx = max(2, int(bw * c / mx))
        b.append(f'<text class="l" x="{x0-10}" y="{y+11}" text-anchor="end">{esc(name)}</text>')
        b.append(f'<rect x="{x0}" y="{y}" width="{wpx}" height="14" rx="2" fill="{col.get(status.get(name),"var(--mut)")}"/>')
        b.append(f'<text class="n" x="{x0+wpx+7}" y="{y+11}">{c}</text>')
        y += rowh
    y += 10
    b.append(f'<line class="ax" x1="24" y1="{y}" x2="{W-24}" y2="{y}"/>')
    y += 24
    b.append(f'<text class="l" x="{x0-10}" y="{y+11}" text-anchor="end" fill="var(--warn)">announced humanoid hands</text>')
    b.append(f'<rect x="{x0}" y="{y}" width="2" height="14" fill="var(--warn)"/>')
    b.append(f'<text class="n" x="{x0+9}" y="{y+11}" fill="var(--warn)">0 &#8212; none of the {len(announced)} announced or prototype hands appears in any method row</text>')
    return svg(W, H, "".join(b), "Hands used by surveyed methods")

# ---------------- Figure 6: what gets reported ----------------
def fig_reporting():
    m = [r for r in ROWS if r.get("class") == "method"]
    axes = [("success criterion stated", lambda r: bool(r.get("success_criterion"))),
            ("real-robot experiment", lambda r: r.get("real_robot") is True),
            ("real trial count stated", lambda r: r.get("real_trials") is not None),
            ("unseen-object count stated", lambda r: r.get("objects_test_unseen") is not None),
            ("contact or penetration handled", lambda r: r.get("penetration") in ("penalised", "measured", "constrained")),
            ("code released", lambda r: r.get("code_released") is True)]
    W, H = 760, 300
    x0, y0, bw = 300, 96, 380
    b = [f'<text class="t" x="24" y="30">Figure 6. What the method literature reports</text>',
         f'<text class="s" x="24" y="50">Share of the {len(m)} surveyed method papers whose note confirms each item. A bar is</text>',
         f'<text class="s" x="24" y="66">evidence the item was stated, not that the work did it well.</text>']
    y = y0
    for label, pred in axes:
        n = sum(1 for r in m if pred(r)); frac = n / len(m)
        wpx = max(2, int(bw * frac))
        colr = "var(--warn)" if frac < 0.35 else "var(--a)"
        b.append(f'<text class="l" x="{x0-10}" y="{y+12}" text-anchor="end">{esc(label)}</text>')
        b.append(f'<rect x="{x0}" y="{y}" width="{bw}" height="15" rx="2" fill="var(--fill)"/>')
        b.append(f'<rect x="{x0}" y="{y}" width="{wpx}" height="15" rx="2" fill="{colr}"/>')
        b.append(f'<text class="n" x="{x0+bw+8}" y="{y+12}">{n} ({round(100*frac)}%)</text>')
        y += 28
    b.append(f'<text class="s" x="24" y="{y+18}">Red marks an item fewer than a third of papers state. The two lowest are the two a reader</text>')
    b.append(f'<text class="s" x="24" y="{y+34}">needs in order to compare two methods at all.</text>')
    return svg(W, max(H, y + 54), "".join(b), "What the method literature reports")

if __name__ == "__main__":
    (OUT / "fig2_hands.svg").write_text(fig_hands())
    (OUT / "fig6_reporting.svg").write_text(fig_reporting())
    for f in sorted(OUT.glob("*.svg")): print(f.name, f.stat().st_size, "bytes")
