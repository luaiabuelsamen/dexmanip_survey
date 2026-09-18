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
 .t{font-size:15px;font-weight:600}.s{font-size:11px;fill:var(--mut)}.l{font-size:11px}
 .n{font-size:9.5px;fill:var(--mut)}.h{font-size:11.5px;font-weight:600}
 .k{font-size:9px;fill:var(--mut);font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
 .box{fill:var(--fill);stroke:var(--line);stroke-width:1}
 .ghost{fill:none;stroke:var(--line);stroke-width:1;stroke-dasharray:3 3}
 .ed{stroke:var(--mut);fill:none;opacity:.55}.tree{stroke:var(--line);fill:none;stroke-width:1.2}
</style>"""
def svg(w,h,body,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}">{STYLE}<rect width="{w}" height="{h}" fill="var(--bg)"/>{body}</svg>')
def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def norm_sim(s):
    s=(s or "").lower()
    if not s or "not stated" in s: return "not stated"
    if "isaac lab" in s or "isaaclab" in s or "isaac sim" in s or "orbit" in s: return "Isaac Lab / Sim"
    if "isaac" in s: return "Isaac Gym"
    if "mjx" in s or "mujoco" in s: return "MuJoCo"
    if "sapien" in s or "maniskill" in s: return "SAPIEN"
    if "bullet" in s: return "PyBullet"
    if "raisim" in s: return "RaiSim"
    if "drake" in s: return "Drake"
    if "genesis" in s: return "Genesis"
    if s in ("none","no simulator","n/a"): return "no simulator"
    return "other"

def fig1():
    human=sum(1 for r in M if r.get("human_data") and str(r["human_data"]).lower() not in ("none","no","null"))
    nodem=sum(1 for r in M if str(r.get("human_data") or "").lower() in ("none","no"))
    hns=N-human-nodem
    one=sum(1 for r in M if r.get("bimanual") is False); two=sum(1 for r in M if r.get("bimanual") is True)
    sims=Counter(norm_sim(r.get("sim")) for r in M)
    par=Counter(p for r in M for p in (r.get("paradigm") or []))
    real=sum(1 for r in M if r.get("real_robot") is True); simonly=N-real
    pen=Counter(str(r.get("penetration")) for r in M)
    penany=sum(pen[k] for k in ("penalised","measured","constrained"))
    cols=[("data source",[("human data named",human,False),("no demonstrations",nodem,False),("not stated",hns,True)]),
          ("embodiment",[("one hand",one,False),("two hands",two,False),("not stated",N-one-two,True)]),
          ("simulator",[(k,v,k=="not stated") for k,v in sims.most_common(7)]),
          ("training paradigm",[(k,v,False) for k,v in par.most_common(7)]),
          ("evaluation",[("real robot",real,False),("simulation only",simonly,False),
                         ("penetration addressed",penany,False),("penetration not addressed",pen.get("not addressed",0),False)])]
    W,H=900,560; x0,cw,gap=28,150,32
    b=[f'<text class="t" x="24" y="28">Figure 1. The field on one page</text>',
       f'<text class="s" x="24" y="48">Every node is a count over the {N} method papers in the corpus. Dashed nodes are reporting gaps, not choices.</text>',
       f'<text class="s" x="24" y="64">Paradigm counts exceed {N} because a method may use several. Recomputed from corpus/rows at draw time.</text>']
    top=92; maxv=max(v for _,items in cols for _,v,_ in items) or 1
    pos={}
    for ci,(cname,items) in enumerate(cols):
        cx=x0+ci*(cw+gap)
        b.append(f'<text class="h" x="{cx+cw/2}" y="{top-12}" text-anchor="middle">{cname}</text>')
        y=top
        for name,v,ghost in items:
            h=max(24,int(16+56*v/maxv))
            cls="ghost" if ghost else "box"
            fill=' fill="var(--warn)" fill-opacity="0.18" stroke="var(--warn)"' if "not addressed" in name else ""
            b.append(f'<rect class="{cls}" x="{cx}" y="{y}" width="{cw}" height="{h}" rx="3"{fill}/>')
            b.append(f'<text class="l" x="{cx+8}" y="{y+15}">{esc(name)}</text>')
            b.append(f'<text class="n" x="{cx+cw-8}" y="{y+15}" text-anchor="end">{v}</text>')
            pos[(ci,name)]=(cx,y+h/2,cw,h); y+=h+9
        cols[ci]=(cname,items)
    for ci in range(4):
        for (c,n),(x,yy,w,h) in list(pos.items()):
            if c!=ci: continue
            for (c2,n2),(x2,y2,w2,h2) in list(pos.items()):
                if c2!=ci+1: continue
                sw=max(.4,min(3.2,(h*h2)/900))
                b.append(f'<path class="ed" d="M{x+w},{yy} C{x+w+16},{yy} {x2-16},{y2} {x2},{y2}" stroke-width="{sw:.1f}"/>')
    cap=top+330
    b.append(f'<text class="s" x="24" y="{cap}">The routes converge. The heaviest single path is no demonstrations, one hand, Isaac Gym,</text>')
    b.append(f'<text class="s" x="24" y="{cap+16}">reinforcement learning, real robot. Whatever enters on the left, almost everything leaves through a</text>')
    b.append(f'<text class="s" x="24" y="{cap+32}">GPU simulator and arrives at a real robot without contact quality ever being measured.</text>')
    return svg(W,H,"".join(b),"The field on one page")

def fig4():
    par=Counter(p for r in M for p in (r.get("paradigm") or []))
    tf=Counter(t for r in M for t in (r.get("task_family") or []))
    def keys_with(pred,lim=7):
        ks=[r["key"] for r in M if pred(r)]; return ks[:lim],len(ks)
    branches=[
      ("a reward function",par.get("RL",0),"var(--a)",[
        ("PPO in a GPU simulator, privileged state",*keys_with(lambda r:"RL" in (r.get("paradigm") or []) and "distillation" not in (r.get("paradigm") or []))),
        ("plus teacher-student distillation to vision",*keys_with(lambda r:"distillation" in (r.get("paradigm") or []))),
        ("reward written by a language model",*keys_with(lambda r:r["key"] in ("eureka_2023","dreureka_2024"))),
        ("seeded by demonstrations",*keys_with(lambda r:"RL+demo" in (r.get("paradigm") or []))),
      ]),
      ("a human demonstration",par.get("BC",0)+par.get("diffusion",0)+par.get("flow",0),"var(--d)",[
        ("teleoperated on the target robot",*keys_with(lambda r:"teleop-system" in (r.get("paradigm") or []))),
        ("wearable rig, no robot in the loop",*keys_with(lambda r:r["key"] in ("dexcap_2024","dexumi_2025","dexwild_2025"))),
        ("egocentric video, no robot at all",*keys_with(lambda r:r["key"] in ("videodex_2022","dexvip_2022","okami_2024","egozero_2025","egomimic_2024","hudor_2024","wm_dex_human_videos_2025"))),
        ("synthetic demonstration generation",*keys_with(lambda r:"data-collection" in (r.get("paradigm") or []))),
      ]),
      ("a human reference, tracked with physics",tf.get("track-human-ref",0),"var(--b)",[
        ("whole reference including fingers",*keys_with(lambda r:r["key"] in ("dextrack_2025","maniptrans_2025","dexmachina_2025","toporetarget_2026"))),
        ("wrist only, fingers learned",*keys_with(lambda r:r["key"]=="objdex_2024")),
        ("object trajectory only",*keys_with(lambda r:r["key"] in ("pgdm_2023","human2sim2robot_2025"))),
        ("reference as soft guidance",*keys_with(lambda r:r["key"] in ("dexplore_2025","physhoi_2023","omnigrasp_2024"))),
      ]),
      ("no learned policy",par.get("trajopt",0)+par.get("MPC",0),"var(--c)",[
        ("sampled plan, learned model",*keys_with(lambda r:r["key"]=="pddm_2019")),
        ("sampled plan, given model",*keys_with(lambda r:r["key"]=="mjpc_2022")),
        ("smoothed analytic contact model",*keys_with(lambda r:r["key"]=="pang_global_planning_2022")),
      ])]
    W=980; rowh=26; H=150+sum(rowh*(len(l)+1.6) for _,_,_,l in branches)
    b=[f'<text class="t" x="24" y="28">Figure 4. What supervises a dexterous policy</text>',
       f'<text class="s" x="24" y="48">Four kinds of supervision, subdivided to the level at which the {N} method papers actually differ.</text>',
       f'<text class="s" x="24" y="64">Counts are recomputed from corpus/rows and a paper may appear under more than one branch.</text>']
    rx,bx,lx=40,210,470; y=110
    b.append(f'<rect class="box" x="{rx-16}" y="{y+ (H-150)/2 - 26}" width="150" height="52" rx="4"/>')
    b.append(f'<text class="l" x="{rx+59}" y="{y+(H-150)/2-8}" text-anchor="middle">supervision for a</text>')
    b.append(f'<text class="l" x="{rx+59}" y="{y+(H-150)/2+6}" text-anchor="middle">dexterous policy</text>')
    b.append(f'<text class="n" x="{rx+59}" y="{y+(H-150)/2+20}" text-anchor="middle">{N} method papers</text>')
    rootx, rooty = rx+134, y+(H-150)/2
    for bi,(bname,bcount,colr,leaves) in enumerate(branches):
        by=y+8
        bh=rowh*len(leaves)
        b.append(f'<rect class="box" x="{bx}" y="{by}" width="235" height="{bh}" rx="4" stroke="{colr}"/>')
        b.append(f'<text class="h" x="{bx+10}" y="{by+18}" fill="{colr}">{esc(bname)}</text>')
        b.append(f'<text class="n" x="{bx+225}" y="{by+18}" text-anchor="end">{bcount}</text>')
        b.append(f'<path class="tree" d="M{rootx},{rooty} C{rootx+30},{rooty} {bx-30},{by+bh/2} {bx},{by+bh/2}" stroke="{colr}" opacity=".6"/>')
        ly=by+8
        for lname,ks,cnt in leaves:
            b.append(f'<text class="l" x="{lx}" y="{ly+12}">{esc(lname)}</text>')
            b.append(f'<text class="n" x="{lx-12}" y="{ly+12}" text-anchor="end">{cnt}</text>')
            b.append(f'<path class="tree" d="M{bx+235},{by+bh/2} C{bx+250},{by+bh/2} {lx-40},{ly+9} {lx-28},{ly+9}" stroke="{colr}" opacity=".45"/>')
            b.append(f'<text class="k" x="{lx}" y="{ly+23}">{esc(", ".join(k.replace("_"," ").replace(" 20"," ") for k in ks[:5]))}</text>')
            ly+=rowh
        y=by+bh+18
    b.append(f'<text class="s" x="24" y="{y+14}">The branches are not exclusive. Most work after 2024 trains with a reward in simulation and ships something</text>')
    b.append(f'<text class="s" x="24" y="{y+30}">shaped like an imitation policy, so it belongs to the first branch and the second at once.</text>')
    return svg(W,y+52,"".join(b),"Taxonomy of training paradigms")

if __name__=="__main__":
    (OUT/"fig1_field.svg").write_text(fig1())
    (OUT/"fig4_taxonomy.svg").write_text(fig4())
    for f in ["fig1_field.svg","fig4_taxonomy.svg"]: print(f,(OUT/f).stat().st_size)
