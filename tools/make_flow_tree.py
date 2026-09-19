"""Figures 1 and 4: the field on one page, and the taxonomy of training paradigms.
Counts are recomputed from corpus/rows/*.json at draw time, never typed in."""
import json, glob, re
from collections import Counter
from pathlib import Path
R = Path(__file__).resolve().parents[1]; OUT = R / "paper/figures"
ROWS = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
M = [r for r in ROWS if r.get("class") == "method"]
N = len(M)
STYLE = """<style>
 :root{--ink:#111418;--mut:#5b6672;--line:#c3ccd4;--bg:#ffffff;--a:#2f6f9f;--b:#7a5ea8;--c:#a8563e;--d:#3f7d57;--warn:#b5462f;--fill:#eef3f7;--fill2:#f4f1f8}
 @media (prefers-color-scheme:dark){:root{--ink:#e8ecef;--mut:#9aa6b2;--line:#3d4750;--bg:#12161a;--a:#6fb0dc;--b:#b295d8;--c:#dd9376;--d:#7fc09a;--warn:#e88a72;--fill:#1b232a;--fill2:#221e2b}}
 text{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;fill:var(--ink)}
 .t{font-size:17px;font-weight:600}.s{font-size:12.5px;fill:var(--mut)}.l{font-size:12.5px}
 .n{font-size:11px;fill:var(--mut)}.h{font-size:13px;font-weight:600}
 .k{font-size:10.5px;fill:var(--mut);font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
 .box{fill:var(--fill);stroke:var(--line);stroke-width:1}
 .ghost{fill:none;stroke:var(--line);stroke-width:1;stroke-dasharray:3 3}
 .ed{stroke:var(--mut);fill:none}
 .rule{stroke:var(--line);fill:none;stroke-width:1}.tree{stroke:var(--line);fill:none;stroke-width:1.2}
 .xl{fill:none;stroke:var(--mut);stroke-width:1.1;stroke-dasharray:5 4;opacity:.75}
 .xt{fill:none;stroke:var(--mut);stroke-width:1.1;stroke-dasharray:6 3 2 3;opacity:.85}
 .xw{font-size:9.5px;fill:var(--mut);font-style:italic}
</style>"""
def svg(w,h,body,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}">{STYLE}<rect width="{w}" height="{h}" fill="var(--bg)"/>{body}</svg>')
def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def norm_sim(s):
    """Normalise a sim field to the buckets Figure 1 draws.

    This is the rule tools/make_tikz_figures.py uses, word for word, because the two editions
    draw one figure and a bucket that differs between them prints two counts for one quantity.
    The order matters: a field that names an engine and then says the version is not stated is
    that engine, not a reporting gap.
    """
    s=(s or "").lower()
    if any(k in s for k in ("isaac lab","isaaclab","isaac sim","isaacsim","orbit")): return "Isaac Lab or Sim"
    if "isaac" in s: return "Isaac Gym"
    if "mjx" in s or "mujoco" in s: return "MuJoCo"
    if "sapien" in s or "maniskill" in s: return "SAPIEN"
    if not s or "not stated" in s: return "not stated"
    if s in ("none","no simulator"): return "no simulator"
    return "other"

def wrap(text, width):
    """Greedy wrap on word boundaries: SVG text does not wrap itself."""
    lines, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur: lines.append(cur)
    return lines

def fig1():
    """Figure 1, the map of the survey: five columns from data source to evaluation.

    The column heads carry the section that covers them, so the figure is the table of contents
    drawn and a reader can navigate from it. A node is a predicate over the method rows and its
    count is that predicate applied; an edge is the rows that satisfy both of the nodes it joins,
    so a route no paper takes is not drawn at all. Edges used to run between every adjacent pair
    at a width taken from the two boxes, which drew routes the corpus does not contain. The
    columns, the nodes and the edge rule are the same here as in tools/make_tikz_figures.py, so
    the two editions draw one figure.
    """
    def human(r):
        v = str(r.get("human_data") or "").lower()
        return bool(r.get("human_data")) and v not in ("none", "no")
    def nodem(r): return str(r.get("human_data") or "").lower() in ("none", "no")
    HANDLED = ("penalised", "measured", "constrained")
    sims = [k for k, _ in Counter(norm_sim(r.get("sim")) for r in M).most_common(6)]
    pars = [k for k, _ in Counter(p for r in M for p in (r.get("paradigm") or [])).most_common(6)]
    cols = [
        ("data source", "Sec. 5.3",
         [("human data named", human, 0), ("no demonstrations", nodem, 0),
          ("not stated", lambda r: not human(r) and not nodem(r), 1)]),
        ("embodiment", "Sec. 3, 6",
         [("one hand", lambda r: r.get("bimanual") is False, 0),
          ("two hands", lambda r: r.get("bimanual") is True, 0),
          ("not stated", lambda r: r.get("bimanual") is None, 1)]),
        ("simulator", "Sec. 4",
         [(k, (lambda k: lambda r: norm_sim(r.get("sim")) == k)(k),
           1 if k == "not stated" else 0) for k in sims]),
        ("training paradigm", "Sec. 5",
         [(k, (lambda k: lambda r: k in (r.get("paradigm") or []))(k), 0) for k in pars]),
        ("evaluation", "Sec. 7",
         [("real robot", lambda r: r.get("real_robot") is True, 0),
          ("simulation only", lambda r: r.get("real_robot") is not True, 0),
          ("penetration addressed", lambda r: r.get("penetration") in HANDLED, 2),
          ("penetration silent", lambda r: r.get("penetration") == "not addressed", 2)]),
    ]
    count = {(ci, name): sum(1 for r in M if pred(r))
             for ci, (_, _, items) in enumerate(cols) for name, pred, _ in items}
    # --- geometry ------------------------------------------------------------------------
    # The five columns are 950 by about 475, the 2:1 the LaTeX edition sets at 180 by 91 mm.
    # The whole drawing stays under the 1000-unit viewBox that tools/make_pdf.py treats as
    # wide, because a figure this shape reads on the portrait page beside the text that
    # introduces it and does not need a landscape page of its own.
    x0, cw, gap, top = 20, 146, 55, 148
    h0, kh, vgap = 28.0, 144.0, 9.0
    mx = max(count.values()) or 1
    stack = {ci: sum(max(h0, h0 + kh * count[(ci, n)] / mx) for n, _, _ in items)
             + vgap * (len(items) - 1) for ci, (_, _, items) in enumerate(cols)}
    tall = max(stack.values())
    geo, mid = {}, {}
    for ci, (cname, sec, items) in enumerate(cols):
        x = x0 + ci * (cw + gap)
        y = top + (tall - stack[ci]) / 2          # every column on one midline
        for name, _, kind in items:
            v = count[(ci, name)]
            h = max(h0, h0 + kh * v / mx)
            geo[(ci, name)] = (x, y, h, kind, v); mid[(ci, name)] = y + h / 2
            y += h + vgap
    W, H = x0 * 2 + 5 * cw + 4 * gap, int(top + tall + 96)
    b = ['<text class="t" x="24" y="30">Figure 1. The field on one page, and the map of this survey</text>',
         f'<text class="s" x="24" y="52">Every node is a count over the {N} method papers in the corpus, and every column head names the'
         ' section that covers it.</text>',
         '<text class="s" x="24" y="70">Dashed nodes are reporting gaps, not choices. A paradigm count may include a paper twice, because'
         ' a method may use several.</text>',
         '<text class="s" x="24" y="88">Recomputed from corpus/rows at draw time.</text>']
    # --- the routes the corpus contains, under the nodes -------------------------------------
    edges = []
    for ci in range(len(cols) - 1):
        for a, pa, _ in cols[ci][2]:
            for bb, pb, _ in cols[ci + 1][2]:
                n = sum(1 for r in M if pa(r) and pb(r))
                if n: edges.append((ci, a, bb, n))
    mxe = max(n for *_, n in edges) or 1
    def anchors(key, others, ci_other):
        x, ytop, h, _, _ = geo[key]
        order = sorted(others, key=lambda o: mid[(ci_other, o)])
        span = 0.80 * h
        return {o: ytop + (h - span) / 2 + span * (i + 0.5) / len(order)
                for i, o in enumerate(order)}
    outa, ina = {}, {}
    for ci in range(len(cols) - 1):
        for a, _, _ in cols[ci][2]:
            t = [bb for c, aa, bb, _ in edges if c == ci and aa == a]
            if t: outa[(ci, a)] = anchors((ci, a), t, ci + 1)
        for bb, _, _ in cols[ci + 1][2]:
            s = [a for c, a, b2, _ in edges if c == ci and b2 == bb]
            if s: ina[(ci + 1, bb)] = anchors((ci + 1, bb), s, ci)
    for ci, a, bb, n in sorted(edges, key=lambda e: e[3]):
        x = geo[(ci, a)][0] + cw; y1 = outa[(ci, a)][bb]
        x2 = geo[(ci + 1, bb)][0]; y2 = ina[(ci + 1, bb)][a]
        sw = 1.2 + 4.4 * n / mxe          # the thinnest route still prints
        op = 0.45 + 0.5 * n / mxe
        b.append(f'<path class="ed" d="M{x},{y1:.0f} C{x + 34},{y1:.0f} {x2 - 34},{y2:.0f} '
                 f'{x2},{y2:.0f}" stroke-width="{sw:.1f}" opacity="{op:.2f}"/>')
    # --- the column heads and the nodes ------------------------------------------------------
    for ci, (cname, sec, items) in enumerate(cols):
        x = x0 + ci * (cw + gap)
        b.append(f'<text class="h" x="{x + cw / 2:.0f}" y="{top - 44}" text-anchor="middle">{esc(cname)}</text>')
        b.append(f'<text class="n" x="{x + cw / 2:.0f}" y="{top - 26}" text-anchor="middle">{sec}</text>')
        b.append(f'<path class="rule" d="M{x},{top - 16} L{x + cw},{top - 16}"/>')
        for name, _, _ in items:
            xx, ytop, h, kind, v = geo[(ci, name)]
            cls = "ghost" if kind == 1 else "box"
            fill = ' fill="var(--fill2)" stroke="var(--b)"' if kind == 2 else ''
            b.append(f'<rect class="{cls}" x="{xx}" y="{ytop:.0f}" width="{cw}" height="{h:.0f}" rx="3"{fill}/>')
            lines = wrap(name, 15)
            y = ytop + h / 2 - 6 * (len(lines) - 1) + 4
            for ln in lines:
                b.append(f'<text class="l" x="{xx + 9}" y="{y:.0f}">{esc(ln)}</text>'); y += 14
            b.append(f'<text class="n" x="{xx + cw - 9}" y="{ytop + h / 2 + 4:.0f}" text-anchor="end">{v}</text>')
    cap = top + tall + 26
    b.append(f'<text class="s" x="24" y="{cap:.0f}">The routes converge. The heaviest single path is no demonstrations, one hand, Isaac Gym, reinforcement learning, real robot.</text>')
    b.append(f'<text class="s" x="24" y="{cap + 18:.0f}">Whatever enters on the left, almost everything leaves through a GPU simulator and arrives at a real robot without contact</text>')
    b.append(f'<text class="s" x="24" y="{cap + 36:.0f}">quality ever being measured.</text>')
    return svg(W, H, "".join(b), "The field on one page, and the map of this survey")

def fig4():
    """Figure 4. Every leaf predicate must test the property its label names.

    Leaves that once read a paradigm tag and then asserted an algorithm, a simulator
    or a student modality the tag does not carry have been either re-predicated
    (PPO and the GPU simulator are read from `algorithm` and `sim`) or renamed to
    what the tag selects. Membership lists that the prose also states are defined
    once here, next to the section that states them, so figure and text cannot drift.

    The footer says the branches are not exclusive, so the overlaps are drawn. Six dashed
    curves run in the right-hand gutter, each labelled with the one word that names what
    crosses: a leaf or a branch on one side, a leaf or a branch on the other. They are drawn
    before the nodes, so a node occludes any curve that passes under it. The smoothing edge
    is a theorem rather than a pipeline and carries a different dash.
    """
    par=Counter(p for r in M for p in (r.get("paradigm") or []))
    tf=Counter(t for r in M for t in (r.get("task_family") or []))
    BY={r["key"]:r for r in M}
    def tags(r): return set(r.get("paradigm") or [])
    def is_ppo(r): return bool(re.search(r"\bppo\b",(r.get("algorithm") or ""),re.I))
    def is_gpu_sim(r): return bool(re.search(r"isaac|genesis",(r.get("sim") or ""),re.I))
    def reward_learner(r): return bool(tags(r) & {"RL","RL+demo"})
    def sel(pred):
        ks=[r["key"] for r in M if pred(r)]; return ks,len(ks)
    def named(*keys):
        """A leaf whose membership the prose names. Keys absent from the method rows
        are dropped and the count says so, rather than being asserted anyway."""
        ks=[k for k in keys if k in BY]; return ks,len(ks)
    # Sec. 5.7, the four variants: the papers that distil a privileged teacher into a
    # vision student. "To vision" is true of these five and of no other distillation row.
    VISION_STUDENT=("hora_2022","visual_dexterity_2022","rotateit_2023","robot_synesthesia_2023","viserdex_2026")
    # Sec. 5.7 again: the generators that need no reinforcement learning. dex1b_2025 is
    # classed as a dataset row, so it is outside the 112 method papers this figure counts.
    SYNTHETIC_GEN=("dexmimicgen_2024","dex1b_2025","deximit_2026")
    # Sec. 5.3.3, the rows trained from human video with no teleoperation at any stage.
    VIDEO_ONLY=("dexmv_2021","videodex_2022","dexvip_2022","okami_2024","human2sim2robot_2025",
                "hudor_2024","wm_dex_human_videos_2025")
    # Wearable and hand-held capture rigs: the operator's own hand is the interface.
    WEARABLE_RIG=("dexcap_2024","dexumi_2025","dexwild_2025","umi_2024")
    branches=[
      ("a reward function",len([r for r in M if reward_learner(r)]),"var(--a)",[
        ("PPO in a GPU-parallel simulator, no distillation stage",
         *sel(lambda r:reward_learner(r) and is_ppo(r) and is_gpu_sim(r) and "distillation" not in tags(r)),0),
        ("plus teacher-student distillation",
         *sel(lambda r:reward_learner(r) and is_ppo(r) and is_gpu_sim(r) and "distillation" in tags(r)),0),
        ("of which the student is a vision policy",*named(*VISION_STUDENT),1),
        ("reward written by a language model",*named("eureka_2023","dreureka_2024"),0),
        ("seeded by demonstrations (the RL+demo tag)",*sel(lambda r:"RL+demo" in tags(r)),0),
      ]),
      ("a human demonstration",len([r for r in M if tags(r) & {"BC","diffusion","flow"}]),"var(--d)",[
        ("teleoperated on the target robot",*sel(lambda r:"teleop-system" in tags(r)),0),
        ("wearable or hand-held rig, no robot in the loop",*named(*WEARABLE_RIG),0),
        ("egocentric video, no robot at all",*named(*VIDEO_ONLY),0),
        ("synthetic demonstration generation",*named(*SYNTHETIC_GEN),0),
      ]),
      ("a human reference, tracked with physics",tf.get("track-human-ref",0),"var(--b)",[
        ("whole reference including fingers",*named("dextrack_2025","maniptrans_2025","dexmachina_2025","toporetarget_2026"),0),
        ("wrist only, fingers learned",*named("objdex_2024"),0),
        ("object trajectory only",*named("human2sim2robot_2025"),0),
        ("reference as soft guidance",*named("dexplore_2025"),0),
        ("no retargeting, reference already on the embodiment",*named("physhoi_2023","omnigrasp_2024"),0),
        ("whole-body humanoid, hands carried with the body",*named("dexman_2025","humanplus_2024","omnih2o_2024"),0),
      ]),
      # The branch is the three papers that learn no policy at all, not the trajopt and MPC
      # tags: eight further rows carry one of those tags inside a learned pipeline.
      ("no learned policy",3,"var(--c)",[
        ("sampled plan, learned model",*named("pddm_2019"),0),
        ("sampled plan, given model",*named("mjpc_2022"),0),
        ("smoothed analytic contact model",*named("pang_global_planning_2022"),0),
      ])]
    rowh=26; H=150+sum(rowh*(len(l)+1.6) for _,_,_,l in branches)
    BW=322                      # branch box width, set by the longest branch name at 11.5px
    LX=210+BW+35                # the leaf column starts clear of the branch boxes
    def textw(s,px): return len(s)*px
    right=LX
    for _,_,_,leaves in branches:
        for lname,ks,_,ann in leaves:
            ind=18 if ann else 0
            keys=", ".join(k.replace("_"," ").replace(" 20"," ") for k in ks[:5])
            if len(ks)>5: keys+=f", and {len(ks)-5} more"
            right=max(right, LX+ind+textw(lname,5.9), LX+ind+textw(keys,5.45))
    STUB=right+26               # the cross-link gutter starts clear of every leaf line
    W=int(STUB+215)
    b=[f'<text class="t" x="24" y="28">Figure 4. What supervises a dexterous policy</text>',
       f'<text class="s" x="24" y="48">Four kinds of supervision, subdivided to the level at which the {N} method papers actually differ.</text>',
       f'<text class="s" x="24" y="64">Every leaf count is the rows its stated predicate selects, recomputed from corpus/rows; a paper may appear more than once.</text>']
    rx,bx,lx=40,210,LX; y=110
    banchor={}; lanchor={}
    b.append(f'<rect class="box" x="{rx-16}" y="{y+ (H-150)/2 - 26}" width="150" height="52" rx="4"/>')
    b.append(f'<text class="l" x="{rx+59}" y="{y+(H-150)/2-8}" text-anchor="middle">supervision for a</text>')
    b.append(f'<text class="l" x="{rx+59}" y="{y+(H-150)/2+6}" text-anchor="middle">dexterous policy</text>')
    b.append(f'<text class="n" x="{rx+59}" y="{y+(H-150)/2+20}" text-anchor="middle">{N} method papers</text>')
    rootx, rooty = rx+134, y+(H-150)/2
    for bi,(bname,bcount,colr,leaves) in enumerate(branches):
        by=y+8
        bh=rowh*len(leaves)
        shown=len({k for _,ks,_,ann in leaves for k in ks if not ann})
        b.append(f'<rect class="box" x="{bx}" y="{by}" width="{BW}" height="{bh}" rx="4" stroke="{colr}"/>')
        b.append(f'<text class="h" x="{bx+10}" y="{by+18}" fill="{colr}">{esc(bname)}</text>')
        b.append(f'<text class="n" x="{bx+BW-10}" y="{by+18}" text-anchor="end">{bcount}</text>')
        if shown<bcount:
            b.append(f'<text class="n" x="{bx+BW-10}" y="{by+32}" text-anchor="end">{shown} of {bcount} in a leaf</text>')
        b.append(f'<path class="tree" d="M{rootx},{rooty} C{rootx+30},{rooty} {bx-30},{by+bh/2} {bx},{by+bh/2}" stroke="{colr}" opacity=".6"/>')
        banchor[bi]=by+bh/2
        ly=by+8
        for leaf_i,(lname,ks,cnt,ann) in enumerate(leaves):
            ind=18 if ann else 0
            label=("— "+lname) if ann else lname
            b.append(f'<text class="l" x="{lx+ind}" y="{ly+12}">{esc(label)}</text>')
            b.append(f'<text class="n" x="{lx-12}" y="{ly+12}" text-anchor="end">{cnt}</text>')
            if not ann:
                b.append(f'<path class="tree" d="M{bx+BW},{by+bh/2} C{bx+BW+15},{by+bh/2} {lx-40},{ly+9} {lx-28},{ly+9}" stroke="{colr}" opacity=".45"/>')
            shownk=", ".join(k.replace("_"," ").replace(" 20"," ") for k in ks[:5])
            if len(ks)>5: shownk+=f", and {len(ks)-5} more"
            b.append(f'<text class="k" x="{lx+ind}" y="{ly+23}">{esc(shownk)}</text>')
            lanchor[(bi,leaf_i)]=ly+9
            ly+=rowh
        y=by+bh+18
    # The overlaps the footer claims, drawn. Each entry is source, target, the one word for
    # what crosses, and whether the edge is a theorem rather than a pipeline. A branch index
    # alone anchors on the branch box; a pair anchors on that branch's leaf.
    CROSS=[((0,1), 1,      "distil",   False),
           ((0,0), (1,3),  "generate", False),
           ((1,2), 2,      "retarget", False),
           (2,     1,      "distil",   False),
           (3,     (0,0),  "smooth",   True),
           ((1,0), (0,4),  "seed",     False)]
    def ay(a): return banchor[a] if isinstance(a,int) else lanchor[a]
    links=[]; placed=[]
    for i,(src,dst,word,thm) in enumerate(CROSS):
        y1,y2=ay(src),ay(dst)
        lane=STUB+40+i*30
        apex=STUB+0.75*(lane-STUB)
        cls="xt" if thm else "xl"
        links.append(f'<path class="{cls}" d="M{STUB},{y1:.0f} C{lane},{y1:.0f} {lane},{y2:.0f} {STUB},{y2:.0f}"/>')
        links.append(f'<path class="{cls}" d="M{STUB+9},{y2-4:.0f} L{STUB},{y2:.0f} L{STUB+9},{y2+4:.0f}" stroke-dasharray="none"/>')
        lyw=(y1+y2)/2+3
        while any(abs(lyw-py)<12 and abs(apex-px)<46 for px,py in placed): lyw+=12
        placed.append((apex,lyw))
        links.append(f'<text class="xw" x="{apex+7:.0f}" y="{lyw:.0f}">{word}</text>')
    b=b[:3]+links+b[3:]
    b.append(f'<text class="s" x="24" y="{y+14}">The branches are not exclusive, and the dashed curves on the right are the overlaps. Most work after 2024 trains</text>')
    b.append(f'<text class="s" x="24" y="{y+30}">with a reward in simulation and ships something shaped like an imitation policy, so it belongs to the first branch and</text>')
    b.append(f'<text class="s" x="24" y="{y+46}">the second at once. Eight further rows carry a trajectory-optimisation or MPC tag inside a learned pipeline and are</text>')
    b.append(f'<text class="s" x="24" y="{y+62}">counted on the branch that learns. The double-dashed smoothing edge is the one overlap that is a theorem rather than</text>')
    b.append(f'<text class="s" x="24" y="{y+78}">a pipeline: `pang_global_planning_2022` proves that a policy gradient and an analytic log-barrier relaxation compute</text>')
    b.append(f'<text class="s" x="24" y="{y+94}">the same local model of contact.</text>')
    return svg(W,y+116,"".join(b),"Taxonomy of training paradigms")

if __name__=="__main__":
    (OUT/"fig1_field.svg").write_text(fig1())
    (OUT/"fig4_taxonomy.svg").write_text(fig4())
    for f in ["fig1_field.svg","fig4_taxonomy.svg"]: print(f,(OUT/f).stat().st_size)
