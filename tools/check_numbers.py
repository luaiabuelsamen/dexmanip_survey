"""Recompute the survey's load-bearing statistics from corpus/rows, then check the prose.

Three kinds of check.
  FACTS   the corpus value for each quantity the survey quotes more than once.
  SHAPE   the definitions the prose states in words and the corpus cannot express as a field.
          Section 6's bimanual denominator is the case: it is the `bimanual: true` rows less four
          named exclusion lists, and its four architecture buckets partition the result. Both are
          encoded here as key lists, so a row added to the corpus or a flag flipped in it breaks
          this check instead of silently moving a number the prose still prints.
  CLAIMS  a regex per quantity, specific enough that every match is that quantity and not a
          sub-denominator the survey has legitimately narrowed. For each, the checker reports
          every distinct value the prose uses, flags any that disagrees with the corpus, and
          flags the case where the prose uses two different values for one quantity, which is
          the failure mode of a document written in parallel.
Run before committing paper/survey.md.
"""
import json, glob, re, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
ROWS = [json.load(open(f)) for f in glob.glob(str(R / "corpus/rows/*.json"))]
M = [r for r in ROWS if r.get("class") == "method"]
BY_KEY = {r["key"]: r for r in M}
def cnt(f, rows=None): return sum(1 for r in (rows if rows is not None else M) if f(r))
def has(pat, r, field="hand"): return bool(re.search(pat, str(r.get(field) or ""), re.I))
def keys(pat, field="hand"): return {r["key"] for r in M if has(pat, r, field)}
def norm_sim(s):
    s = (s or "").lower()
    if any(k in s for k in ("isaac lab", "isaaclab", "isaac sim", "isaacsim", "orbit")): return "isaaclab"
    if "isaac" in s: return "isaacgym"
    if "mjx" in s or "mujoco" in s: return "mujoco"
    return s
VLA = [r for r in M if "VLA" in (r.get("paradigm") or [])]
import importlib.util as _il
_sp=_il.spec_from_file_location("hand_usage", str(R/"tools/hand_usage.py")); _hu=_il.module_from_spec(_sp); _sp.loader.exec_module(_hu)
HU=_hu.partition()
RL = [r for r in M if set(r.get("paradigm") or []) & {"RL", "RL+demo"}]
RL_DOF = [r for r in RL if r.get("hand_dof") is not None]

# --- Section 6's denominator, stated as the prose states it -------------------------------------
# "the method rows whose notes place a learned closed-loop controller on two multi-fingered hands.
#  It is the 53 less those 16; less two static grasp-synthesis methods; less three systems with no
#  learned policy; and less four rows where no learned policy holds both hands."
BIMANUAL_ALL = {r["key"] for r in M if r.get("bimanual") is True}
BI_EXCLUDE = {
 "no dexterous hand on the robot": """aloha_act_2023 rdt1b_2024 egomimic_2024 h_rdt_2025 umi_2024
    pi0_2024 pi05_2025 pistar06_2025 diffusion_policy_2023 gemini_robotics_2025
    gemini_robotics_15_2025 helix_2025 groot_n16_2025 ace_teleop_2024 dp3_2024
    open_television_2024""".split(),
 "static grasp synthesis": "bimangrasp_2024 bidexgrasp_2026".split(),
 "no learned policy": "castro_sap_contact_2021 dexteleop0_2026 pang_global_planning_2022".split(),
 "no learned policy over both hands": "omnih2o_2024 okami_2024 dexdeform_2023 omnigrasp_2024".split(),
}
BI_EXCLUDED = {k for v in BI_EXCLUDE.values() for k in v}
BIMANUAL_28 = BIMANUAL_ALL - BI_EXCLUDED
# Section 6.2: "Every row of the 28 is assigned to exactly one of them, read from its note."
BI_ARCH = {
 "arch_single": """dexmachina_2025 dexman_2025 maniptrans_2025 objdex_2024 humanplus_2024
    dexpbt_2023 twisting_lids_2024 eureka_2023 pianomime_2024 humanoid_sim2real_recipe_2025
    bidex_teleop_2024 dexcap_2024 dexwild_2025 dexmimicgen_2024 hato_visuotactile_2024
    humanoid_policy_human_policy_2025 gr_dexter_2025 groot_n1_2025 dexora_2026 metis_2025
    egoscale_2026""".split(),
 "arch_per_hand": "artigrasp_2023 dynamic_handover_2023 dydexhandover_2025 bidexhd_2024".split(),
 "arch_leader_follower": "asymdex_2024".split(),
 "arch_unstated": "bunny_visionpro_2024 deximit_2026".split(),
}

FACTS = {
 "method_rows": len(M),
 "code_released": cnt(lambda r: r.get("code_released") is True),
 "code_withheld": cnt(lambda r: r.get("code_released") is False),
 "disagreements": cnt(lambda r: r.get("paper_code_mismatch")),
 "contradictions": cnt(lambda r: r.get("mismatch_class") == "contradiction"),
 "parse_limitation": cnt(lambda r: r.get("mismatch_class") == "parse-limitation"),
 "code_absent": cnt(lambda r: r.get("mismatch_class") == "code-absent"),
 "version_skew": cnt(lambda r: r.get("mismatch_class") == "version-skew"),
 "internal_inconsistency": cnt(lambda r: r.get("mismatch_class") == "internal-inconsistency"),
 "pen_settled": cnt(lambda r: r.get("penetration") is not None),
 "pen_handled": cnt(lambda r: r.get("penetration") in ("penalised", "measured", "constrained")),
 "real_robot": cnt(lambda r: r.get("real_robot") is True),
 "states_trials": cnt(lambda r: r.get("real_trials") is not None),
 "states_criterion": cnt(lambda r: bool(r.get("success_criterion"))),
 "states_unseen": cnt(lambda r: r.get("objects_test_unseen") is not None),
 "states_envs": cnt(lambda r: r.get("n_envs") is not None),
 "isaacgym_rows": cnt(lambda r: norm_sim(r.get("sim")) == "isaacgym"),
 "isaaclab_rows": cnt(lambda r: norm_sim(r.get("sim")) == "isaaclab"),
 "hand_named": cnt(lambda r: bool(r.get("hand"))),
 "allegro_rows": len(keys("allegro")),
 "shadow_rows": len(keys("shadow")),
 "inspire_rows": len(keys("inspire")),
 "leap_rows": len(keys("leap")),
 "big_five_rows": len(keys("allegro") | keys("shadow") | keys("adroit")
                      | keys("leap") | keys("inspire")),
 "reorient_rows": cnt(lambda r: "reorient" in str(r.get("task_family"))),
 "rl_rows": len(RL),
 "rl_dof_stated": len(RL_DOF),
 "rl_dof_ge16": sum(1 for r in RL_DOF if r["hand_dof"] >= 16),
 "vla_rows": len(VLA),
 "vla_settled": cnt(lambda r: r.get("dexterous_hand_evaluated") is not None, VLA),
 "vla_dexterous": cnt(lambda r: r.get("dexterous_hand_evaluated") is True, VLA),
 "vla_no_hand": cnt(lambda r: r.get("dexterous_hand_evaluated") is False, VLA),
 "vla_unsettled": cnt(lambda r: r.get("dexterous_hand_evaluated") is None, VLA),
 "vla_dof_stated": cnt(lambda r: r.get("dexterous_hand_evaluated") is True
                       and r.get("hand_dof") is not None, VLA),
 "hands": cnt(lambda r: r.get("class") == "hand", ROWS),
 "bimanual_true": cnt(lambda r: r.get("bimanual") is True),
 "hands_unused": HU["unused"],
 "hands_unused_obtainable": HU["unused_obtainable"],
 "hands_unused_unobtainable": HU["unused_unobtainable"],
 # Hand rows only: the DIGIT sensor also carries open_hardware and is not one of the 33.
 "open_hw_hands": cnt(lambda r: r.get("class") == "hand"
                      and r.get("open_hardware") is True, ROWS),
 "open_hw_available": cnt(lambda r: r.get("class") == "hand"
                          and r.get("open_hardware") is True
                          and r.get("release_status") in ("sold", "open-source"), ROWS),
 "bimanual_learned": len(BIMANUAL_28),
}
FACTS.update({k: len(v) for k, v in BI_ARCH.items()})

_U = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
      "fifteen sixteen seventeen eighteen nineteen").split()
_T = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
      "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
WORD = {w: i for i, w in enumerate(_U)}
for _t, _tv in _T.items():
    WORD[_t] = _tv
    for _i, _u in enumerate(_U[1:10], 1): WORD[f"{_t}-{_u}"] = _tv + _i
NUM = r"(\d{1,4}|[A-Za-z]+(?:-[a-z]+)?)"
def P(s):
    """Prose is hard-wrapped, so every literal space in a pattern must match a newline too."""
    return s.replace(" ", r"\s+")

# Each entry is (fact key, regex) or (fact key for group 1, fact key for group 2, regex).
# The regex must be specific to that quantity. Two-group entries check a number and the
# denominator it is quoted against in the same sentence, which is where sections drift apart.
CLAIMS = [
 # --- paper versus code -------------------------------------------------------------------------
 ("contradictions", rf"{NUM}\s+(?:are\s+)?(?:true\s+|hard\s+|real\s+)?contradictions?\b"),
 ("contradictions", rf"{NUM}\s+of\s+(?:the\s+)?\d+\s+(?:method\s+)?(?:papers|rows)\s+that\s+released\s+(?:parseable\s+)?code\s+contradict"),
 ("disagreements", rf"{NUM}\s+(?:recorded\s+)?(?:paper[ \-]?(?:versus|and|vs)?[ \-]?code\s+)?disagreements?\b(?!\s+that\s+are)"),
 ("disagreements", P(rf"{NUM} of the 112 method rows record a discrepancy")),
 ("disagreements", P(rf"{NUM} of the 112 method rows record a disagreement")),
 ("disagreements", P(rf"{NUM} of those record a disagreement")),
 ("disagreements", P(rf"and {NUM} carry a recorded discrepancy")),
 ("disagreements", P(rf"{NUM} of the 112 rows record a disagreement")),
 ("disagreements", P(rf"{NUM} of those record a discrepancy")),
 ("disagreements", P(rf"[Aa]ll {NUM} released code")),
 ("parse_limitation", rf"{NUM}\s+are\s+limitations\s+of\s+(?:this|the)\s+survey"),
 ("parse_limitation", P(rf"{NUM} are limits of this survey's own parse")),
 ("code_absent", P(rf"{NUM} released code without the described")),
 ("version_skew", P(rf"{NUM} are version skew\b")),
 ("version_skew", P(rf"{NUM} version skews?\b")),
 ("internal_inconsistency", P(rf"{NUM} are a paper disagreeing with itself")),
 ("code_released", rf"{NUM}\s+(?:of\s+(?:the\s+)?\d+\s+)?(?:method\s+)?rows?\s+released\s+code"),
 ("code_released", P(rf"{NUM} method papers released code")),
 ("code_released", P(rf"the {NUM} rows that released anything")),
 ("code_released", "code_withheld", P(rf"{NUM} released code and {NUM} did not")),
 ("code_withheld", P(rf"{NUM} method rows released nothing")),
 # --- penetration -------------------------------------------------------------------------------
 ("pen_handled", rf"{NUM}\s+of\s+the\s+\d+\s+(?:method\s+)?rows\s+whose\s+notes\s+settle"),
 ("pen_handled", "pen_settled", P(rf"{NUM} of the {NUM} method rows whose notes settle")),
 ("pen_handled", "pen_settled", P(rf"{NUM} of the {NUM} rows whose contact handling the note settled")),
 ("pen_handled", P(rf"{NUM} method rows handle interpenetration")),
 # --- coverage, after the section 7.1 null audit -------------------------------------------------
 ("states_trials", P(rf"only {NUM} state how many real trials")),
 ("states_trials", P(rf"{NUM} state how many real trials produced")),
 ("states_unseen", P(rf"only {NUM} state how many unseen objects were tested")),
 ("states_unseen", P(rf"{NUM} rows state a count of unseen test objects")),
 ("states_unseen", P(rf"[Oo]nly {NUM} rows state a count and the median")),
 ("states_criterion", P(rf"{NUM} state how a rollout is scored")),
 ("states_criterion", P(rf"the count rose from 79 to {NUM}")),
 ("states_envs", P(rf"only {NUM} rows state an environment count")),
 ("states_envs", P(rf"{NUM} of 112 rows state a parallel environment count")),
 ("real_robot", P(rf"{NUM} report a real-robot experiment")),
 ("real_robot", P(rf"of the {NUM} papers with a real robot")),
 # --- hands -------------------------------------------------------------------------------------
 ("hands", rf"Tables?\s+2\s+and\s+3\s+hold\s+{NUM}\s+hands"),
 ("hands_unused", rf"{NUM}\s+(?:of\s+the\s+\d+\s+)?hands?(?:\s+rows?)?\s+(?:in\s+Tables?\s+2\s+and\s+3\s+)?appear\s+in\s+no\s+method\s+row"),
 ("hands_unused_obtainable", rf"{NUM}\s+documented\s+hands\s+that\s+can\s+be\s+bought"),
 ("hands_unused_obtainable", rf"leaves\s+{NUM}\s+hands\s+that\s+can\s+be\s+bought"),
 # The four sentences that carry the hand partition. They were unregistered while the partition
 # was wrong in all four of them, which is how a substring bug survived into print.
 ("hands_unused_obtainable", P(rf"{NUM} of those can be bought today or built from published")),
 ("hands_unused_obtainable",
  rf"{NUM}\s+hands\s+that\s+can\s+be\s+bought\s+(?:today\s+)?or\s+built\s+from\s+published"),
 ("hands_unused_obtainable", P(rf"the {NUM} hands (?:of|named just above|named in) the paragraph")),
 ("hands_unused_unobtainable", P(rf"{NUM} of those are neither sold nor open")),
 # Open hardware. The seven rows and the six of them that are purchasable or released are
 # read out of the corpus in two sentences and were unchecked.
 ("open_hw_available", rf"{NUM}\s+rows\s+in\s+Table\s*\d?\s+are\s+open\s+hardware"),
 ("open_hw_hands", P(rf"of the {NUM} state a dollar cost")),
 # The Isaac family split. isaacgym_rows was the quantity that was one too high, unmatched by any
 # pattern, while three sentences and a figure node printed it.
 ("isaacgym_rows", P(rf"{NUM} run in Isaac Gym")),
 ("isaacgym_rows", P(rf"{NUM} of the 112 method papers in this corpus run on it")),
 ("isaaclab_rows", P(rf"against {NUM} on its successors Isaac Lab")),
 ("method_rows", P(rf"all {NUM} method rows")),
 ("method_rows", P(rf"the {NUM} method rows in the corpus")),
 ("method_rows", P(rf"the {NUM} method papers in this corpus")),
 ("method_rows", P(rf"the {NUM} method papers actually differ")),
 ("method_rows", P(rf"Of {NUM} method rows,")),
 ("hands", P(rf"of the {NUM} hands in Tables 2 and 3")),
 ("hand_named", P(rf"Of 112 method rows, {NUM} name a hand")),
 ("hand_named", P(rf"The {NUM} method rows that name their own hand")),
 ("hand_named", P(rf"of the {NUM} method rows that name a hand")),
 ("hand_named", P(rf"of the {NUM} hand-naming method rows")),
 ("allegro_rows", P(rf"The Allegro accounts for {NUM}")),
 ("allegro_rows", P(rf"Allegro appears in {NUM},")),
 ("allegro_rows", P(rf"It appears in {NUM} of the 112 method rows")),
 ("shadow_rows", P(rf"Shadow for {NUM},")),
 ("shadow_rows", P(rf"Shadow in {NUM},")),
 ("shadow_rows", P(rf"Shadow at {NUM} and \d+")),
 ("inspire_rows", P(rf"family for {NUM},")),
 ("inspire_rows", P(rf"Inspire in {NUM} and LEAP")),
 ("leap_rows", rf"LEAP\s+(?:Hand\s+)?(?:in|for|carries)\s+{NUM}\s+(?:method\s+)?rows"),
 ("leap_rows", P(rf"and LEAP for {NUM}\b")),
 ("leap_rows", P(rf"and LEAP in {NUM}\b")),
 ("leap_rows", P(rf"LEAP at {NUM} and \d+")),
 ("leap_rows", "hand_named", P(rf"{NUM} of the {NUM} hand-naming method rows use an open-hardware")),
 ("big_five_rows", "hand_named", P(rf"{NUM} of the {NUM} name an Allegro")),
 ("reorient_rows", P(rf"In-hand reorientation has {NUM} rows")),
 ("reorient_rows", P(rf"of the {NUM} reorientation rows")),
 # --- generalist and reinforcement-learning hand sizes --------------------------------------------
 ("vla_rows", P(rf"{NUM} method rows carry the `VLA` tag")),
 ("vla_rows", P(rf"{NUM} rows carry the generalist tag")),
 ("vla_settled", P(rf"{NUM} of them settle whether")),
 ("vla_dexterous", rf"{NUM}\s+of\s+the\s+\w+\s+generalist\s+policies\s+that\s+settle"),
 ("vla_dexterous", "vla_settled", P(rf"{NUM} of those {NUM} did")),
 ("vla_dexterous", "vla_dof_stated", P(rf"Of the {NUM}, {NUM} state the hand's degrees")),
 ("vla_dof_stated", "vla_dexterous", P(rf"{NUM} of the {NUM} state a hand size")),
 ("vla_no_hand", P(rf"{NUM} report no hand result at all")),
 ("vla_no_hand", P(rf"The {NUM} with no hand result")),
 ("vla_unsettled", P(rf"the remaining {NUM} (?:do not|never) say")),
 ("vla_unsettled", P(rf"The remaining {NUM} do not say")),
 ("rl_rows", P(rf"{NUM} of the 112 method rows learn from a reward")),
 ("rl_rows", "rl_dof_stated", P(rf"Of the {NUM} reward-learning rows, {NUM} state a count")),
 ("rl_dof_stated", P(rf"over the {NUM} reinforcement-learning rows that state one")),
 ("rl_dof_ge16", P(rf"{NUM} of those are 16 or above")),
 # --- bimanual: section 6 defines the denominator, every other section follows it -----------------
 ("bimanual_true", P(rf"{NUM} corpus method rows record `bimanual: true`")),
 ("bimanual_true", P(rf"{NUM} of the 112 method rows record two hands on the robot")),
 ("bimanual_learned", P(rf"denominator for this section is {NUM}")),
 ("bimanual_learned", P(rf"to the {NUM} rows whose notes place a learned")),
 ("bimanual_learned", P(rf"Every row of the {NUM} is assigned")),
 ("bimanual_learned", P(rf"of the {NUM} rows that Section 6 counts")),
 ("bimanual_learned", P(rf"outside the {NUM} by class")),
 ("bimanual_learned", P(rf"so outside the {NUM},")),
 ("bimanual_learned", P(rf"one of the rows the {NUM} excludes")),
 ("bimanual_learned", P(rf"of the {NUM} (?:put one policy|give each hand|assigns? explicit|have no real robot)")),
 ("arch_single", "bimanual_learned", P(rf"{NUM} of the {NUM} put one policy over both hands")),
 ("arch_single", "bimanual_learned", P(rf"{NUM} of the {NUM} rows that Section 6 counts")),
 ("arch_per_hand", "bimanual_learned", P(rf"{NUM} of the {NUM} give each hand its own network")),
 ("arch_leader_follower", "bimanual_learned", P(rf"{NUM} of the {NUM} assigns? explicit leader")),
 ("arch_unstated", P(rf"{NUM} rows do not say which they are")),
]

# --- reconciliations that are not quantities -----------------------------------------------------
# A withdrawn claim and a changed table mark cannot be caught by recounting rows, so each is pinned
# as a phrase. FORBIDDEN is prose the corpus or the generated tables refute. REQUIRED_IN is prose a
# section has to carry, so that a frame named in section 1 stays vocabulary the body actually uses.
FORBIDDEN = [
 (r"[Ss]imulators\s+would\s+have\s+to\s+expose\s+penetration",
  "withdrawn in section 4.2: released code already computes penetration outside the reward"),
 (r"are\s+blank\s+in\s+it",
  "Table 5 prints `code (0)` in those three cells since the fourth mark was added"),
]
REQUIRED_IN = {
 "paper/tables/table5_rewards.md": [
   (r"code \(0\)", "the fourth mark section 5.2.2 describes"),
 ],
 "paper/sections/01_introduction.md": [
   (r"reference-versus-rollout", "where the frame is named"),
 ],
 "paper/sections/07_evaluation.md": [
   (r"reference-versus-rollout", "sections 7.3 and 7.7 are where the frame does its work"),
   (r"does not supply a threshold",
    "section 1 promises a threshold, a method and a count; section 7 has to say which are delivered"),
 ],
 "paper/sections/08_conclusion.md": [
   (r"reference-versus-rollout", "the second of the seven claims is the gap the frame names"),
   (r"none\s+of\s+their\s+authors\s+was\s+written\s+to",
    "claim 1 carries the disclosure it rests on"),
 ],
 # The paper-against-code finding is published without a reply from anyone it names. The paragraph
 # that says so, what a fetched commit can and cannot show, and how a disputed case is corrected is
 # what makes that publishable, so it is pinned in both editions rather than left to survive an
 # edit. Its four parts are checked separately: an edit may reword any of them, but not drop one.
 "paper/sections/05_training.md": [
   (r"reference-versus-rollout", "section 5.4 is the frame's clearest instance"),
   (r"were\s+not\s+contacted\s+before\s+this\s+survey\s+was\s+posted",
    "the nine were not written to"),
   (r"in\s+`outreach/`\s+in\s+the\s+repository,\s+unsent",
    "the letters are in the repository, and named"),
   (r"not\s+the\s+code\s+that\s+produced\s+a\s+paper's\s+numbers",
    "a fetched commit may postdate, precede or diverge from the code behind the numbers"),
   (r"says\s+exactly\s+that\s+about\s+itself",
    "one corpus paper's own README makes the same point"),
   (r"correctable\s+in\s+public", "the route by which a disputed case is corrected"),
 ],
 "tex/sections/05_training.tex": [
   (r"were\s+not\s+contacted\s+before\s+this\s+survey\s+was\s+posted",
    "the nine were not written to"),
   (r"in\s+the\s+repository,\s+unsent",
    "the letters are in the repository, and named"),
   (r"not\s+the\s+code\s+that\s+produced\s+a\s+paper's\s+numbers",
    "a fetched commit may postdate, precede or diverge from the code behind the numbers"),
   (r"says\s+exactly\s+that\s+about\s+itself",
    "one corpus paper's own README makes the same point"),
   (r"correctable\s+in\s+public", "the route by which a disputed case is corrected"),
 ],
}

def text_problems(text):
    out = []
    for pat, why in FORBIDDEN:
        for m in re.finditer(pat, text):
            ctx = text[max(0, m.start()-90):m.end()+40].replace("\n", " ")
            out.append(f"survey.md still says {m.group(0)!r} ({why})\n         ...{ctx}...")
    for rel, rules in REQUIRED_IN.items():
        f = R / rel
        body = f.read_text() if f.exists() else ""
        if not body: out.append(f"{rel} is missing")
        for pat, why in rules:
            if not re.search(pat, body):
                out.append(f"{rel} no longer carries /{pat}/ ({why})")
    return out

def to_int(tok):
    if tok is None: return None
    if str(tok).isdigit(): return int(tok)
    return WORD.get(str(tok).lower())

def artefact_problems():
    """Every contradiction row must name the public artefact its claim is a claim about.

    The finding is published without having written to any of the accused authors, so what stands
    in for a reply is that a reader can check the claim: a repository, the commit the corpus
    fetched, the file inside it, and the two values. A row classed `contradiction` without that
    locator, or with a commit the code manifest did not fetch, or naming a file that is not in the
    parsed copy of that repository, is a claim nobody can settle, and it breaks this check rather
    than reaching the page.
    """
    out = []
    man = json.loads((R / "corpus/code_manifest.json").read_text())
    for r in sorted([x for x in M if x.get("mismatch_class") == "contradiction"],
                    key=lambda x: x["key"]):
        k = r["key"]
        a = r.get("mismatch_artifact")
        if not a:
            out.append(f"`{k}` is a contradiction with no mismatch_artifact")
            continue
        for f in ("repo", "commit", "file", "locator", "paper", "code"):
            if not a.get(f):
                out.append(f"`{k}` mismatch_artifact has no {f}")
        m = man.get(k) or {}
        if a.get("repo") != m.get("url"):
            out.append(f"`{k}` names repo {a.get('repo')}, the manifest fetched {m.get('url')}")
        if a.get("commit") != m.get("commit"):
            out.append(f"`{k}` names commit {a.get('commit')}, the manifest fetched {m.get('commit')}")
        md = R / "code/md" / f"{k}.md"
        if a.get("file") and md.exists() and a["file"].split("/")[-1] not in md.read_text():
            out.append(f"`{k}` names {a['file']}, which is not in code/md/{k}.md")
    return out


def shape_problems():
    """Check the definitions the prose states in words against the corpus rows they name."""
    out = []
    for reason, ks in BI_EXCLUDE.items():
        for k in ks:
            if k not in BY_KEY: out.append(f"section 6 excludes `{k}` ({reason}), which is not a method row")
            elif BY_KEY[k].get("bimanual") is not True:
                out.append(f"section 6 excludes `{k}` ({reason}) from the bimanual rows, "
                           f"but its `bimanual` field is {BY_KEY[k].get('bimanual')!r}")
    dupes = sorted(k for k in BI_EXCLUDED if sum(k in v for v in BI_EXCLUDE.values()) > 1)
    for k in dupes: out.append(f"section 6 excludes `{k}` under two reasons at once")
    assigned = [k for ks in BI_ARCH.values() for k in ks]
    for k in sorted(set(assigned)):
        if assigned.count(k) > 1: out.append(f"section 6.2 assigns `{k}` to two architectures")
    for k in sorted(set(assigned) - BIMANUAL_28):
        out.append(f"section 6.2 assigns an architecture to `{k}`, which is not one of the {len(BIMANUAL_28)}")
    for k in sorted(BIMANUAL_28 - set(assigned)):
        out.append(f"section 6.2 assigns no architecture to `{k}`, which is one of the {len(BIMANUAL_28)}")
    return out

# --- the emptiness each printed table claims, against the section that reads cells out of it ------
# Nine tables left the paper and three moved to an appendix, and the prose that read cells out of
# them kept quoting the repository tabulation's wider column set: Section III quoted 61 and 39 per
# cent against captions saying 58 and 42, and Section IV-B quoted 165 cells and 45 per cent against
# a printed table of 105 cells and 38. Both editions carry their own tables, with their own column
# sets and so their own percentages, so each edition is pinned to its own generated file. The check
# is deliberately one-directional: the share a table's own caption states has to appear in the prose
# that argues from it. It says nothing about the other numbers in that paragraph, which may
# legitimately describe the repository tabulation, as long as they are labelled as such.
CAPTION_OWNERS = [
 ("latex", "tex/tables/table1_hands_available.tex", "tex/sections/03_hands.tex",
  "Table IV, the hands that can be obtained"),
 ("latex", "tex/tables/table2_hands_announced.tex", "tex/sections/03_hands.tex",
  "Table V, the hands announced"),
 ("latex", "tex/tables/table3_simulators.tex", "tex/sections/04_simulators.tex",
  "Table VI, the simulators"),
 ("markdown", "paper/tables/table2_hands_available.md", "paper/sections/03_hands.md",
  "Table 2, the hands that can be obtained"),
 ("markdown", "paper/tables/table3_hands_announced.md", "paper/sections/03_hands.md",
  "Table 3, the hands announced"),
 ("markdown", "paper/tables/table4_simulators.md", "paper/sections/04_simulators.md",
  "Table 4, the simulators"),
]

def caption_problems():
    """Every printed table's own empty-cell share, checked against the section that argues from it.

    A caption states "N of M cells". The share that follows from N and M is what the section has to
    quote, because a reader compares the sentence with the caption on the facing page. Both the
    truncated and the rounded percentage are accepted, since the two generators differ.
    """
    out = []
    for edition, tbl, prose, what in CAPTION_OWNERS:
        tp, pp = R / tbl, R / prose
        if not tp.exists() or not pp.exists():
            out.append(f"{what}: {tbl if not tp.exists() else prose} is missing")
            continue
        m = re.search(r"(\d+)\s+of\s+(?:the\s+)?(\d+)", tp.read_text())
        if not m:
            out.append(f"{what}: its caption no longer states an N of M cell count ({tbl})")
            continue
        n, d = int(m.group(1)), int(m.group(2))
        want = {int(100 * n / d), round(100 * n / d)}
        body = re.sub(r"\s+", " ", pp.read_text())
        if not any(re.search(rf"\b{p}\s*(?:percent|%)", body) for p in want):
            out.append(f"{what}: its caption says {n} of {d} cells, which is "
                       f"{'/'.join(str(p) for p in sorted(want))} percent, and no sentence of "
                       f"{prose} states that share")
    return out


# --- the two hand-matching pattern sets, against each other --------------------------------------
# The hand partition is decided by tools/hand_usage.py and the `uses` column by tools/make_tables.py,
# each with its own regular expression per hand. They disagreed once, on `dexhand` matching the
# substring `bi-dexhands`, and the survey printed 18 unused where the table printed 19. The sets
# stay separate because the figure and the partition ask slightly different questions of some rows,
# so what is checked here is the only thing that has to hold: that they place every hand on the same
# side of used and unused. A pattern edited in one file and not the other breaks this check rather
# than a printed number.
def pattern_problems():
    out = []
    try:
        import importlib.util as _i
        sp = _i.spec_from_file_location("make_tables", str(R / "tools/make_tables.py"))
        mt = _i.module_from_spec(sp); sp.loader.exec_module(mt)
    except Exception as e:                                    # a generator that will not import is
        return [f"tools/make_tables.py could not be imported to compare pattern sets: {e}"]
    hands = [r for r in ROWS if r.get("class") == "hand"]
    fields = [str(r.get("hand") or "").lower() for r in M]
    def used(pat): return bool(pat) and any(re.search(pat, f) for f in fields)
    for h in hands:
        a, b = used(_hu.PAT.get(h["key"])), used(mt.USES.get(h["key"]))
        if a != b:
            out.append(f"`{h['key']}` is {'used' if a else 'unused'} by tools/hand_usage.py and "
                       f"{'used' if b else 'unused'} by tools/make_tables.py, so the partition the "
                       f"prose states and the `uses` column the table prints disagree")
    return out


def strip_tex(t):
    """Reduce LaTeX source to running prose so the same patterns match both editions."""
    t = re.sub(r"(?m)^\s*%.*$", " ", t)                    # comments
    t = re.sub(r"\\(cite|ref|label|input)\{[^}]*\}", " ", t)  # references
    t = re.sub(r"\\(texttt|textbf|emph|textit)\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\[a-zA-Z@]+\s*", " ", t)                 # any remaining command
    t = t.replace("\\_", "_").replace("\\%", "%").replace("\\&", "&").replace("~", " ")
    t = re.sub(r"[{}]", " ", t)
    return re.sub(r"\s+", " ", t)

def main():
    # Both editions are checked. The checker previously read only paper/survey.md, so a clean
    # report said nothing at all about the LaTeX edition, which is the one being submitted.
    sources = [("markdown", R / "paper/survey.md")]
    tex = sorted((R / "tex/sections").glob("*.tex"))
    if tex:
        sources.append(("latex", None))
    text = (R / "paper/survey.md").read_text()
    tex_text = "\n".join(f.read_text() for f in tex)
    print("=== facts recomputed from corpus/rows ===")
    for k, v in FACTS.items(): print(f"  {v:>5}  {k}")
    bad = 0
    print("\n=== the artefact behind every contradiction ===")
    ap = artefact_problems()
    for p in ap:
        bad += 1
        print(f"  ARTEFACT  {p}")
    if not ap:
        print(f"  {FACTS['contradictions']} contradiction rows, each with a repository, the "
              f"commit the manifest fetched, a file in the parsed copy, and both values")
    print("\n=== definitions the prose states in words ===")
    for p in shape_problems():
        bad += 1
        print(f"  SHAPE  {p}")
    print(f"  section 6: {FACTS['bimanual_true']} bimanual rows less {len(BI_EXCLUDED)} named "
          f"exclusions is {FACTS['bimanual_learned']}, split "
          + " / ".join(f"{len(v)} {k.replace('arch_', '')}" for k, v in BI_ARCH.items()))
    print("\n=== phrases the reconciliation pinned ===")
    tp = text_problems(text)
    for t in tp:
        bad += 1
        print(f"  TEXT   {t}")
    if not tp: print(f"  {len(FORBIDDEN)} withdrawn phrases absent, "
                     f"{sum(len(v) for v in REQUIRED_IN.values())} required phrases present")
    print("\n=== the two hand-matching pattern sets against each other ===")
    pp = pattern_problems()
    for q in pp:
        bad += 1
        print(f"  PATTERN  {q}")
    if not pp:
        print(f"  {len([r for r in ROWS if r.get('class') == 'hand'])} hands placed the same side "
              f"of used and unused by both generators")
    print("\n=== each printed table's emptiness against the section that argues from it ===")
    cp = caption_problems()
    for c in cp:
        bad += 1
        print(f"  CAPTION  {c}")
    if not cp: print(f"  {len(CAPTION_OWNERS)} table captions agree with their own section")
    print("\n=== claims in the prose ===")
    matched_any = set()
    for edition, body in (("markdown", text), ("latex", strip_tex(tex_text))):
        seen = {}
        for entry in CLAIMS:
            pat = entry[-1]
            for m in re.finditer(pat, body, re.I):
                for grp, key in enumerate(entry[:-1], 1):
                    want = FACTS[key]
                    got = to_int(m.group(grp))
                    if got is None: continue
                    seen.setdefault(key, set()).add(got)
                    if got != want:
                        bad += 1
                        ctx = body[max(0, m.start()-100):m.end()+50].replace("\n", " ")
                        print(f"  WRONG  [{edition}] {key}: prose {got}, corpus {want}\n         ...{ctx}...")
        for key, vals in sorted(seen.items()):
            if len(vals) > 1:
                bad += 1
                print(f"  SPLIT  [{edition}] {key}: prose uses {sorted(vals)} for one quantity; "
                      f"corpus says {FACTS[key]}")
        matched_any |= set(seen)
    unchecked = sorted(set(FACTS) - matched_any)
    if unchecked: print(f"  note: no prose in either edition matched {', '.join(unchecked)}")
    print(f"\n{bad} problems")
    return 1 if bad else 0

if __name__ == "__main__": sys.exit(main())
