"""Count, across the parsed corpus, which hands / simulators / datasets each paper mentions.

A mention is a regex hit in papers/md/<key>.md or code/md/<key>.md. This is a mention count,
not a usage count: a related-work sentence counts the same as an experiment. The survey quotes
it only as "appears in N of M parsed sources", never as "N papers used it".
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path
R = Path(__file__).resolve().parents[1]
bib = {e["key"]: e for e in json.loads((R / "corpus/bib.json").read_text())}

HANDS = {
 "Shadow": r"shadow\s*(dexterous\s*)?hand|shadowhand", "Allegro": r"allegro",
 "LEAP": r"\bleap\s*hand", "Inspire": r"\binspire\b.{0,20}(hand|rh56|ftp)|rh56",
 "Ability (PSYONIC)": r"psyonic|ability\s*hand", "XHand (RobotEra)": r"xhand",
 "Wonik": r"wonik", "DLR": r"\bdlr\b.{0,15}hand", "Barrett": r"barrett\s*hand",
 "TriFinger": r"trifinger", "ORCA": r"\borca\s*hand", "RUKA": r"\bruka\b",
 "Faive/Mimic": r"faive|mimic\s*robotics", "Unitree Dex": r"dex3|dex5|unitree.{0,12}hand",
 "Sharpa": r"sharpa", "Tesollo": r"tesollo|dg-?5f", "Schunk SVH": r"schunk\s*svh|\bsvh\b",
 "Robotiq (gripper)": r"robotiq", "Franka gripper": r"franka.{0,20}gripper|panda\s*gripper",
 "MANO (human)": r"\bmano\b", "Tesla Optimus": r"optimus", "BrainCo": r"brainco|revo\s*2",
 "LinkerHand": r"linker\s*hand|linkerbot", "PaXini": r"paxini|dexh13",
}
SIMS = {
 "MuJoCo": r"mujoco", "MJX/Warp": r"\bmjx\b|mujoco[\s_-]*warp|mujoco\s*playground",
 "Isaac Gym": r"isaac\s*gym|isaacgym", "Isaac Lab/Orbit": r"isaac\s*lab|isaaclab|\borbit\b.{0,20}sim",
 "Isaac Sim": r"isaac\s*sim|omniverse", "PyBullet/Bullet": r"pybullet|bullet\s*physics",
 "SAPIEN": r"sapien", "ManiSkill": r"maniskill", "Genesis": r"\bgenesis\b",
 "Newton": r"newton\s*(physics|engine)", "Brax": r"\bbrax\b", "RaiSim": r"raisim",
 "Drake": r"\bdrake\b", "Gazebo": r"gazebo", "CoppeliaSim/V-REP": r"coppelia|v-?rep",
 "PhysX": r"physx", "Real robot only": r"",
}
DATA = {
 "GRAB": r"\bgrab\b\s*(dataset|\[)|grab\s*dataset", "DexYCB": r"dex-?ycb", "ARCTIC": r"arctic",
 "TACO": r"\btaco\b", "OakInk": r"oakink", "HOI4D": r"hoi4d", "HOT3D": r"hot3d",
 "GigaHands": r"gigahands", "EgoDex": r"egodex", "H2O": r"\bh2o\b",
 "Open X-Embodiment": r"open\s*x-?embodiment|\brt-?x\b", "DROID": r"\bdroid\b",
 "YCB objects": r"\bycb\b", "ShapeNet": r"shapenet", "Objaverse": r"objaverse",
}
ALGO = {
 "PPO": r"\bppo\b", "SAC": r"\bsac\b", "DDPG": r"\bddpg\b", "TD3": r"\btd3\b",
 "DAgger": r"dagger", "behaviour cloning": r"behavio[u]?r\s*cloning|\bbc\b",
 "diffusion policy": r"diffusion\s*polic", "flow matching": r"flow\s*matching",
 "action chunking": r"action\s*chunk", "transformer policy": r"transformer",
 "teacher-student": r"teacher-?student|privileged\s*(state|information)",
 "domain randomisation": r"domain\s*randomi[sz]", "PBT": r"population-?based\s*training|\bpbt\b",
 "MPC/sampling": r"\bmpc\b|model\s*predictive|predictive\s*sampling",
 "LLM reward": r"\bllm\b.{0,30}reward|reward\s*.{0,10}\bllm\b",
}
def scan(groups):
    out = defaultdict(list)
    for k in bib:
        txt = ""
        for p in (R / f"papers/md/{k}.md", R / f"code/md/{k}.md"):
            if p.exists(): txt += p.read_text(errors="ignore").lower()
        if not txt: continue
        for name, pat in groups.items():
            if pat and re.search(pat, txt, re.I): out[name].append(k)
    return out
if __name__ == "__main__":
    res = {}
    for label, g in [("hands", HANDS), ("simulators", SIMS), ("datasets", DATA), ("algorithms", ALGO)]:
        d = scan(g); res[label] = {n: sorted(ks) for n, ks in sorted(d.items(), key=lambda x: -len(x[1]))}
        print(f"\n== {label} (mentions across parsed sources)")
        for n, ks in res[label].items(): print(f"  {len(ks):3d}  {n}")
    (R / "corpus/stats.json").write_text(json.dumps(res, indent=1))
    print(f"\nparsed sources: {sum(1 for k in bib if (R/f'papers/md/{k}.md').exists() or (R/f'code/md/{k}.md').exists())} of {sum(1 for k in bib if bib[k].get("topic") != "related")}")
