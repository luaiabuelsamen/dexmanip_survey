"""Recompute the survey's load-bearing statistics from corpus/rows, then check the prose.

Two kinds of check.
  FACTS   the corpus value for each quantity the survey quotes more than once.
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
def cnt(f, rows=None): return sum(1 for r in (rows if rows is not None else M) if f(r))
def norm_sim(s):
    s = (s or "").lower()
    if any(k in s for k in ("isaac lab", "isaaclab", "isaac sim", "orbit")): return "isaaclab"
    if "isaac" in s: return "isaacgym"
    if "mjx" in s or "mujoco" in s: return "mujoco"
    return s
VLA = [r for r in M if "VLA" in (r.get("paradigm") or [])]

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
 "isaacgym_rows": cnt(lambda r: norm_sim(r.get("sim")) == "isaacgym"),
 "isaaclab_rows": cnt(lambda r: norm_sim(r.get("sim")) == "isaaclab"),
 "leap_rows": cnt(lambda r: re.search(r"leap", str(r.get("hand") or ""), re.I)),
 "vla_rows": len(VLA),
 "vla_settled": cnt(lambda r: r.get("dexterous_hand_evaluated") is not None, VLA),
 "vla_dexterous": cnt(lambda r: r.get("dexterous_hand_evaluated") is True, VLA),
 "hands": cnt(lambda r: r.get("class") == "hand", ROWS),
 "bimanual_true": cnt(lambda r: r.get("bimanual") is True),
}
WORD = {w: i for i, w in enumerate(
 "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
 "sixteen seventeen eighteen nineteen twenty".split())}
WORD.update({"twenty-one":21,"twenty-two":22,"twenty-five":25,"twenty-eight":28,"thirty-three":33,
 "thirty-five":35,"thirty-six":36,"thirty-seven":37,"thirty-eight":38,"forty-six":46,"fifty":50,
 "sixty-one":61,"sixty-two":62,"eighty-five":85,"eighty-nine":89,"ninety-six":96})
NUM = r"(\d{1,4}|[A-Za-z]+(?:-[a-z]+)?)"

# Each entry: fact key, regex. The regex must be specific to that quantity.
CLAIMS = [
 ("contradictions", rf"{NUM}\s+(?:are\s+)?(?:true\s+|hard\s+|real\s+)?contradictions?\b"),
 ("contradictions", rf"{NUM}\s+of\s+(?:the\s+)?\d+\s+(?:method\s+)?(?:papers|rows)\s+that\s+released\s+(?:parseable\s+)?code\s+contradict"),
 ("disagreements", rf"{NUM}\s+(?:recorded\s+)?(?:paper[ \-]?(?:versus|and|vs)?[ \-]?code\s+)?disagreements?\b(?!\s+that\s+are)"),
 ("parse_limitation", rf"{NUM}\s+are\s+limitations\s+of\s+(?:this|the)\s+survey"),
 ("code_released", rf"{NUM}\s+(?:of\s+(?:the\s+)?\d+\s+)?(?:method\s+)?rows?\s+released\s+code"),
 ("pen_handled", rf"{NUM}\s+of\s+the\s+\d+\s+(?:method\s+)?rows\s+whose\s+notes\s+settle"),
 ("vla_dexterous", rf"{NUM}\s+of\s+the\s+\w+\s+generalist\s+policies\s+that\s+settle"),
 ("hands", rf"Tables?\s+2\s+and\s+3\s+hold\s+{NUM}\s+hands"),
 ("leap_rows", rf"LEAP\s+(?:Hand\s+)?(?:in|for|carries)\s+{NUM}\s+(?:method\s+)?rows"),
]

def to_int(tok):
    if tok is None: return None
    if str(tok).isdigit(): return int(tok)
    return WORD.get(str(tok).lower())

def main():
    text = (R / "paper/survey.md").read_text()
    print("=== facts recomputed from corpus/rows ===")
    for k, v in FACTS.items(): print(f"  {v:>5}  {k}")
    print("\n=== claims in the prose ===")
    bad = 0
    seen = {}
    for key, pat in CLAIMS:
        want = FACTS[key]
        for m in re.finditer(pat, text, re.I):
            got = to_int(m.group(1))
            if got is None: continue
            seen.setdefault(key, set()).add(got)
            if got != want:
                bad += 1
                ctx = text[max(0, m.start()-100):m.end()+50].replace("\n", " ")
                print(f"  WRONG  {key}: prose {got}, corpus {want}\n         ...{ctx}...")
    for key, vals in sorted(seen.items()):
        if len(vals) > 1:
            bad += 1
            print(f"  SPLIT  {key}: prose uses {sorted(vals)} for one quantity; corpus says {FACTS[key]}")
    print(f"\n{bad} problems")
    return 1 if bad else 0

if __name__ == "__main__": sys.exit(main())
