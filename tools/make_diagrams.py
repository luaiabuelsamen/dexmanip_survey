"""Hand-drawn conceptual figures (1, 3, 4, 5) as standalone SVG."""
from pathlib import Path
R = Path(__file__).resolve().parents[1]; OUT = R / "paper/figures"; OUT.mkdir(exist_ok=True)
STYLE = """<style>
 :root{--ink:#111418;--mut:#5b6672;--line:#c3ccd4;--bg:#ffffff;--a:#2f6f9f;--b:#7a5ea8;--c:#a8563e;--d:#3f7d57;--warn:#b5462f;--fill:#eef3f7;--fill2:#f4f1f8}
 @media (prefers-color-scheme:dark){:root{--ink:#e8ecef;--mut:#9aa6b2;--line:#3d4750;--bg:#12161a;--a:#6fb0dc;--b:#b295d8;--c:#dd9376;--d:#7fc09a;--warn:#e88a72;--fill:#1b232a;--fill2:#221e2b}}
 text{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;fill:var(--ink)}
 .t{font-size:15px;font-weight:600}.s{font-size:11.5px;fill:var(--mut)}.l{font-size:11.5px}
 .n{font-size:10px;fill:var(--mut)}.h{font-size:12px;font-weight:600}
 .box{fill:var(--fill);stroke:var(--line);stroke-width:1}
 .box2{fill:var(--fill2);stroke:var(--line);stroke-width:1}
 .ed{stroke:var(--mut);stroke-width:1.2;fill:none}
 .edw{stroke:var(--warn);stroke-width:1.4;fill:none;stroke-dasharray:4 3}
</style>
<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
<path d="M0,0 L7,3 L0,6 z" fill="var(--mut)"/></marker>
<marker id="arw" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
<path d="M0,0 L7,3 L0,6 z" fill="var(--warn)"/></marker></defs>"""
def svg(w,h,body,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}">{STYLE}<rect width="{w}" height="{h}" fill="var(--bg)"/>{body}</svg>')
def box(x,y,w,h,label,sub="",cls="box",fs=11.5):
    o=[f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>']
    lines=label.split("|")
    ty=y+(h-len(lines)*14-(6 if sub else 0))/2+11
    for ln in lines:
        o.append(f'<text class="l" style="font-size:{fs}px" x="{x+w/2}" y="{ty}" text-anchor="middle">{ln}</text>'); ty+=14
    if sub: o.append(f'<text class="n" x="{x+w/2}" y="{ty+2}" text-anchor="middle">{sub}</text>')
    return "".join(o)
def arrow(x1,y1,x2,y2,warn=False):
    m="arw" if warn else "ar"; c="edw" if warn else "ed"
    return f'<path class="{c}" d="M{x1},{y1} L{x2},{y2}" marker-end="url(#{m})"/>'

def fig3():
    W,H=820,430
    b=[f'<text class="t" x="24" y="30">Figure 3. One simulation step, and where engines differ</text>',
       f'<text class="s" x="24" y="50">The stages every rigid-body engine runs. Under each, the choices that separate the engines used for hands.</text>',
       f'<text class="s" x="24" y="66">Dashed red marks where interpenetration is created or hidden from the user.</text>']
    stages=[("broad phase","which pairs might touch"),("narrow phase","contact points and normals"),
            ("constraint assembly","friction cone, limits"),("solver","velocities and impulses"),
            ("integrate","advance state")]
    x,y,bw,bh,gap=28,92,140,46,16
    for i,(s,sub) in enumerate(stages):
        b.append(box(x+i*(bw+gap),y,bw,bh,s,sub))
        if i<len(stages)-1: b.append(arrow(x+i*(bw+gap)+bw,y+bh/2,x+(i+1)*(bw+gap)-3,y+bh/2))
    detail={
     0:["PhysX: GPU SAP","MuJoCo: broadphase","Genesis: GPU tiles"],
     1:["MuJoCo: convex, analytic","PhysX: SDF or convex hull","Dojo: exact, nonconvex"],
     2:["MuJoCo: soft, pyramidal","Drake SAP: convex, regularised","Dojo: NCP, hard"],
     3:["MuJoCo: PGS/CG/Newton","PhysX: TGS, fixed iters","Dojo: interior point","ComFree: closed form"],
     4:["semi-implicit Euler","RK4 (Brax)","implicit (MuJoCo)"]}
    yy=y+bh+30
    for i in range(5):
        cx=x+i*(bw+gap)
        b.append(f'<line class="ed" x1="{cx+bw/2}" y1="{y+bh}" x2="{cx+bw/2}" y2="{yy-6}" stroke-dasharray="2 3"/>')
        for j,d in enumerate(detail[i]):
            b.append(f'<text class="n" x="{cx+bw/2}" y="{yy+j*15}" text-anchor="middle">{d}</text>')
    py=yy+80
    b.append(f'<rect class="box2" x="28" y="{py}" width="764" height="96" rx="4"/>')
    b.append(f'<text class="h" x="44" y="{py+22}">Where penetration comes from</text>')
    notes=["Soft contact admits penetration by construction: the contact force is a function of depth, so depth is never zero.",
           "A fixed iteration budget leaves the constraint unconverged, so a stiff contact under load is resolved as overlap.",
           "Convex decomposition replaces the mesh, so the object the solver sees is not the object the renderer draws.",
           "Only some engines expose the resulting depth to the user; where they do not, a policy can exploit it unobserved."]
    for j,n in enumerate(notes):
        b.append(f'<text class="n" x="44" y="{py+42+j*16}">&#8226; {n}</text>')
    b.append(arrow(430,y+bh+4,430,py-6,warn=True))
    return svg(W,H+80,"".join(b),"A simulation step and where engines differ")

def fig5():
    W,H=820,300
    b=[f'<text class="t" x="24" y="30">Figure 5. Four ways to control two dexterous hands</text>',
       f'<text class="s" x="24" y="50">Counts are surveyed bimanual method papers using each architecture.</text>']
    panels=[("one policy, both hands","observation of both hands and object|one network|joint action vector","most of the corpus"),
            ("two policies, shared observation","each hand its own network|both see the same state","a minority"),
            ("leader and follower","one hand assigned the dominant role|the other reacts to it","AsymDex"),
            ("relative frame","action expressed between the hands|or in the object frame","AsymDex, DexMachina")]
    x,y,bw,bh=28,76,182,140
    for i,(t,body,who) in enumerate(panels):
        px=x+i*(bw+14)
        b.append(f'<rect class="box" x="{px}" y="{y}" width="{bw}" height="{bh}" rx="4"/>')
        b.append(f'<text class="h" x="{px+bw/2}" y="{y+20}" text-anchor="middle">{t}</text>')
        for j,ln in enumerate(body.split("|")):
            b.append(f'<text class="n" x="{px+bw/2}" y="{y+42+j*15}" text-anchor="middle">{ln}</text>')
        cy=y+bh-38
        if i==0:
            b.append(f'<circle cx="{px+50}" cy="{cy}" r="9" class="box2"/><circle cx="{px+132}" cy="{cy}" r="9" class="box2"/>')
            b.append(f'<rect class="box2" x="{px+68}" y="{cy-26}" width="46" height="16" rx="3"/>')
            b.append(arrow(px+59,cy,px+68,cy-14)); b.append(arrow(px+123,cy,px+114,cy-14))
        elif i==1:
            b.append(f'<circle cx="{px+50}" cy="{cy}" r="9" class="box2"/><circle cx="{px+132}" cy="{cy}" r="9" class="box2"/>')
            b.append(f'<rect class="box2" x="{px+28}" y="{cy-28}" width="44" height="14" rx="3"/>')
            b.append(f'<rect class="box2" x="{px+110}" y="{cy-28}" width="44" height="14" rx="3"/>')
            b.append(f'<line class="ed" x1="{px+72}" y1="{cy-21}" x2="{px+110}" y2="{cy-21}" stroke-dasharray="3 3"/>')
        elif i==2:
            b.append(f'<circle cx="{px+50}" cy="{cy}" r="11" class="box2" stroke="var(--a)"/>')
            b.append(f'<circle cx="{px+132}" cy="{cy}" r="8" class="box2"/>')
            b.append(arrow(px+63,cy,px+121,cy))
        else:
            b.append(f'<circle cx="{px+50}" cy="{cy}" r="9" class="box2"/><circle cx="{px+132}" cy="{cy}" r="9" class="box2"/>')
            b.append(f'<line class="ed" x1="{px+59}" y1="{cy}" x2="{px+123}" y2="{cy}" stroke-dasharray="3 2"/>')
            b.append(f'<text class="n" x="{px+91}" y="{cy-6}" text-anchor="middle">&#916;</text>')
    b.append(f'<text class="s" x="24" y="{y+bh+30}">The field is concentrated in the first panel. The two on the right are where the structure of the problem is</text>')
    b.append(f'<text class="s" x="24" y="{y+bh+46}">actually used, and both are represented by a handful of papers.</text>')
    return svg(W,H+40,"".join(b),"Bimanual coordination architectures")

if __name__=="__main__":
    (OUT/"fig3_sim_step.svg").write_text(fig3())
    (OUT/"fig5_bimanual.svg").write_text(fig5())
    for f in sorted(OUT.glob("*.svg")): print(f.name, f.stat().st_size)
