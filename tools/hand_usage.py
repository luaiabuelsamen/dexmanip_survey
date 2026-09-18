"""The one rule for whether a tabulated hand appears in a method paper's own experiments.

The survey states this partition in four places, so it is computed once here and imported. A hand
counts as used when its pattern matches the `hand` field of any method row. Obtainable means the
row's release status is sold or open-source, or open_hardware is true.
"""
import json, glob, re
from pathlib import Path
R = Path(__file__).resolve().parents[1]
PAT = {
 'leap_hand_2023':'leap','leap_hand_v2_adv_2025':'leap v2|leap hand v2','shadow_dexterous_hand_2005':'shadow|adroit',
 'shadow_dex_ee_2024':'dex-?ee','allegro_hand_v4_2016':'allegro','inspire_rh56dfx_2023':'inspire',
 'psyonic_ability_hand_2021':'psyonic|ability hand','robotera_xhand1_2024':'xhand','sharpa_wave_2026':'sharpa',
 'wuji_hand_2025':'wuji','unitree_dex5_2025':'dex5|unitree.{0,12}hand','faive_hand_2023':'faive|mimic',
 'orca_hand_2025':'orca','ruka_2025':'ruka','ruka_v2_2026':'ruka v2','bidexhand_2025':'bidexhand',
 'dexhand_open_source_2023':'dexhand','pisa_iit_softhand_2014':'pisa|softhand','ilda_hand_2021':'ilda',
 'tesollo_dg5f_2024':'tesollo|dg-?5f','brainco_revo2_2025':'brainco|revo','linkerbot_l20_2025':'linker',
 'paxini_dexh13_2024':'paxini|dexh13','agibot_omnihand_2025':'agibot|omnihand','tesla_optimus_hand_2025':'optimus',
 'figure_03_hand_2025':'figure ?03','onex_neo_hand_2026':r'\bneo\b','sanctuary_phoenix_hand_2024':'phoenix',
 'boston_dynamics_atlas_hand_2026':r'\batlas\b','xiaomi_cyberone_hand_2026':'cyberone',
 'proception_prohand_2026':'prohand','daxo_muscle_v0_2025':'daxo','clone_robotics_hand_2024':'clone',
}
OBTAINABLE = {"sold", "open-source"}

def partition():
    rows = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
    m = [r for r in rows if r.get("class") == "method"]
    hands = [r for r in rows if r.get("class") == "hand"]
    hay = " | ".join(str(r.get("hand") or "") for r in m).lower()
    used, unused = [], []
    for h in hands:
        p = PAT.get(h["key"])
        (used if (p and re.search(p, hay)) else unused).append(h)
    ob = [h for h in unused if h.get("release_status") in OBTAINABLE or h.get("open_hardware") is True]
    return dict(hands=len(hands), used=len(used), unused=len(unused),
                unused_obtainable=len(ob), unused_unobtainable=len(unused) - len(ob),
                unused_obtainable_keys=[h["key"] for h in ob])

if __name__ == "__main__":
    p = partition()
    for k, v in p.items(): print(f"  {k}: {v}")
