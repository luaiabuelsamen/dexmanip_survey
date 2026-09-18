"""Hand-drawn conceptual figures (1, 3, 4, 5) as standalone SVG."""
from pathlib import Path
R = Path(__file__).resolve().parents[1]; OUT = R / "paper/figures"; OUT.mkdir(exist_ok=True)
STYLE = """<style>
 :root{--ink:#111418;--mut:#5b6672;--line:#c3ccd4;--bg:#ffffff;--a:#2f6f9f;--b:#7a5ea8;--c:#a8563e;--d:#3f7d57;--warn:#b5462f;--fill:#eef3f7;--fill2:#f4f1f8}
 @media (prefers-color-scheme:dark){:root{--ink:#e8ecef;--mut:#9aa6b2;--line:#3d4750;--bg:#12161a;--a:#6fb0dc;--b:#b295d8;--c:#dd9376;--d:#7fc09a;--warn:#e88a72;--fill:#1b232a;--fill2:#221e2b}}
 text{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;fill:var(--ink)}
 .t{font-size:15px;font-weight:600}.s{font-size:11.5px;fill:var(--mut)}.l{font-size:11.5px}
 .n{font-size:10px;fill:var(--mut)}.h{font-size:12px;font-weight:600}
 .k{font-size:9px;fill:var(--mut);font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
 .cnt{font-size:13px;font-weight:700;fill:var(--a)}
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
       f'<text class="s" x="24" y="66">Dashed red marks the three stages that make overlap. They do not answer to the same knob.</text>']
    stages=[("broad phase","which pairs might touch"),("narrow phase","contact points and normals"),
            ("constraint assembly","friction cone, limits"),("solver","velocities and impulses"),
            ("integrate","advance state")]
    x,y,bw,bh,gap=28,92,140,46,16
    for i,(s_,sub) in enumerate(stages):
        b.append(box(x+i*(bw+gap),y,bw,bh,s_,sub))
        if i<len(stages)-1: b.append(arrow(x+i*(bw+gap)+bw,y+bh/2,x+(i+1)*(bw+gap)-3,y+bh/2))
    detail={
     0:["PhysX: GPU SAP","MuJoCo: broadphase","Genesis: libccd, islands"],
     1:["MuJoCo: convex, analytic","PhysX: SDF or convex hull","Dojo: primitives vs planes"],
     2:["MuJoCo: soft, elliptic cone","Drake SAP: convex, regularised","Dojo: NCP, hard"],
     3:["MuJoCo: PGS/CG/Newton","PhysX: TGS, fixed iters","Dojo: interior point","ComFree: closed form"],
     4:["semi-implicit Euler","symplectic Euler (Brax)","RK4 (MuJoCo)"]}
    yy=y+bh+30
    for i in range(5):
        cx=x+i*(bw+gap)
        b.append(f'<line class="ed" x1="{cx+bw/2}" y1="{y+bh}" x2="{cx+bw/2}" y2="{yy-6}" stroke-dasharray="2 3"/>')
        for j,d in enumerate(detail[i]):
            b.append(f'<text class="n" x="{cx+bw/2}" y="{yy+j*15}" text-anchor="middle">{d}</text>')
    py=yy+92
    # Three sources, deliberately unordered: no measurement in this corpus ranks
    # them for a hand. Sources: mujoco_convex_contact_2014 Sec. V (mass-independent
    # closed form), contact_models_comparison_2023 Sec. IV-A (conditioning, not
    # stiffness), isaacgym_2021 Table 4 (1/120 s), dojo_2022 Table II (no v-level
    # term), comfree_sim_2026 Sec. III-B/IV-A (states its shipped setting).
    # The 0.5 m/s fingertip speed is an assumption, not a sourced number.
    notes=[["Velocity-level enforcement. Where non-penetration is enforced on velocities, any residual approach velocity is",
            "integrated into overlap of order v&#183;&#916;t. Illustration under an assumption, not a measurement: a fingertip closing at",
            "0.5 m/s &#8212; a speed no source in this survey reports &#8212; at Isaac Gym&#8217;s 1/120 s Shadow Hand step gives about 4 mm before the",
            "next step&#8217;s constraint acts. Engines that enforce the gap at the next configuration carry no such term: Dojo&#8217;s",
            "hard-contact NCP holds its feet above the floor at &#916;t = 0.1, 0.01 and 0.001 s alike."],
           ["The prescribed compliance. A regularised contact rests at a violation equal to the normal load times the compliance",
            "that was chosen for it. It is zero at zero load, and MuJoCo&#8217;s closed form is independent of the object&#8217;s mass. The depth",
            "is a setting, and no engine paper in Table 4 other than ComFree-Sim states the setting it ships."],
           ["Solver truncation. A truncated solve degrades with the conditioning of the problem and with redundancy in the contact",
            "set, not with stiffness, which is prescribed. A grasp guarantees both, being many persistent contacts on a light object."]]
    bh2=42+sum(len(n) for n in notes)*14+80
    b.append(f'<rect class="box2" x="28" y="{py}" width="764" height="{bh2}" rx="4"/>')
    b.append(f'<text class="h" x="44" y="{py+22}">Where penetration comes from: three sources on different knobs. Which one dominates in a hand has not been measured.</text>')
    ly=py+42
    for n in notes:
        for j,ln in enumerate(n):
            pre="&#8226; " if j==0 else "&#160;&#160;&#160;"
            b.append(f'<text class="n" x="44" y="{ly}">{pre}{ln}</text>'); ly+=14
    b.append(f'<line class="ed" x1="44" y1="{ly+2}" x2="776" y2="{ly+2}" stroke-dasharray="2 3"/>')
    ly+=18
    b.append(f'<text class="n" x="44" y="{ly}">Not a source of overlap, but a reason a number is ambiguous: an outer convex hull or decomposition contains the visual mesh, so it</text>')
    ly+=14
    b.append(f'<text class="n" x="44" y="{ly}">blocks contacts and hides overlap measured against that mesh, while an inscribed primitive admits overlap the solver never sees.</text>')
    ly+=14
    b.append(f'<text class="n" x="44" y="{ly}">PhysX 5 uses SDF collision on non-convex bodies and skips the decomposition. A penetration number must name the geometry it used.</text>')
    ly+=18
    b.append(f'<text class="h" style="font-size:10px" x="44" y="{ly}">The depth is computable from the poses and the meshes. IsaacGymEnvs&#8217; IndustReal task already gates its policy update on it at 1 mm.</text>')
    for cx in (410,566,722):
        b.append(arrow(cx,py-30,cx,py-6,warn=True))
    return svg(W,py+bh2+34,"".join(b),"A simulation step and where engines differ")

def fig5():
    # Counts: the 25 corpus papers whose notes place a learned controller on two
    # dexterous hands. Datasets, static grasp-pose synthesis and two-gripper papers
    # are excluded. bidexhands_2022 ships panels 1 and 2; asymdex_2024 uses 3 and 4.
    W,H=820,326
    b=[f'<text class="t" x="24" y="30">Figure 5. Four ways to control two dexterous hands</text>',
       f'<text class="s" x="24" y="50">Counts are the 25 corpus papers that put a learned controller on two dexterous hands. Two are counted twice.</text>']
    panels=[("one policy, both hands","observation of both hands and object|one network, joint action vector",
             "21 of 28","twisting_lids_2024  dexmachina_2025|maniptrans_2025  dexman_2025|gr_dexter_2025  deximit_2026|and 15 more"),
            ("a network per hand","each hand its own network|centralised critic, or own obs. only",
             "4 of 28","bidexhd_2024  artigrasp_2023|dynamic_handover_2023|dydexhandover_2025"),
            ("leader and follower","one hand assigned the dominant role|the other reacts to it",
             "1 of 28","asymdex_2024|dexterous_handover_2025 is not|counted: its giver is a scripted|arm and its row reads bimanual no"),
            ("relative frame","action expressed between the hands|or in the held object's frame",
             "1 of 28","asymdex_2024, the same paper|dexmimicgen_2024 preserves it|offline when generating data,|not in the policy's observation")]
    x,y,bw,bh=28,72,182,188
    for i,(t_,body,cnt,keys) in enumerate(panels):
        px=x+i*(bw+14)
        edge=' stroke-width="2.2" stroke="var(--a)"' if i==0 else ''
        b.append(f'<rect class="box" x="{px}" y="{y}" width="{bw}" height="{bh}" rx="4"{edge}/>')
        b.append(f'<text class="h" x="{px+bw/2}" y="{y+20}" text-anchor="middle">{t_}</text>')
        b.append(f'<text class="cnt" x="{px+bw/2}" y="{y+38}" text-anchor="middle">{cnt}</text>')
        for j,ln in enumerate(body.split("|")):
            b.append(f'<text class="n" x="{px+bw/2}" y="{y+56+j*13}" text-anchor="middle">{ln}</text>')
        cy=y+116
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
        for j,ln in enumerate(keys.split("|")):
            b.append(f'<text class="k" x="{px+bw/2}" y="{y+143+j*12}" text-anchor="middle">{ln}</text>')
    b.append(f'<text class="s" x="24" y="{y+bh+30}">The field is concentrated in the first panel. The two on the right are where the structure of the problem is</text>')
    b.append(f'<text class="s" x="24" y="{y+bh+46}">actually used, and asymdex_2024 is the only corpus paper that puts either one inside a policy.</text>')
    return svg(W,H+40,"".join(b),"Bimanual coordination architectures")

if __name__=="__main__":
    (OUT/"fig3_sim_step.svg").write_text(fig3())
    (OUT/"fig5_bimanual.svg").write_text(fig5())
    for f in sorted(OUT.glob("*.svg")): print(f.name, f.stat().st_size)
