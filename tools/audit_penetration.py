"""Redraw and re-sweep the hand audit of the penetration field, so it can be checked.

The survey's second headline finding is a null: of the 112 method rows, the 85 whose penetration
field says the work does not address it are counted as silence. A null is worth what the search
behind it is worth, and every other field this extraction was audited against had under-counted by
twenty to forty-five percent. This script reproduces the two mechanical halves of the audit whose
verdicts are written up in `reviews/penetration_audit.md`: the draw, and the keyword sweep that
found the passages each verdict was read from.

The draw is `random.Random(20260919).sample(pop, 25)` over the sorted population, so it is fixed
as long as the population is. The population is asserted against the size the write-up records,
because a corpus edit that changes it invalidates the sample rather than shifting it: if the
assertion fires, the audit is stale and has to be redrawn and re-read, not patched.

The sweep is a regex over the whole parsed source for every word the corpus uses for this
quantity, in `papers/md/<key>.md`, its `.ocr.md` where equations were recovered, and
`code/md/<key>.md`. It is deliberately wider than the quantity: it hits collision avoidance,
solver settings and the reference lists, all of which a reader has to rule out by hand. Its
output is a list of passages to read, never a verdict; a verdict is in the write-up beside the
sentence it rests on. What the sweep does settle is that a row reported as silent was searched:
a zero here means the word does not occur in the source at all.
"""
import glob, json, random, re, sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
SEED = 20260919
N_SAMPLE = 25
POPULATION_AT_AUDIT = 85          # method rows with penetration == "not addressed", 2026-09-19

# Every word for the quantity, plus the words that get mistaken for it. Widened once, after the
# first pass over the sample found the near misses that motivate the second group: a tactile
# sensor's indentation depth, an Isaac Gym de-penetration velocity, and self-collision costs in a
# teleoperation retargeter. None is a penetration measurement and all three read like one in a grep.
TERMS = re.compile(
    r"penetrat|interpenetr|intersection|intersect|plausib|contact consist|contact-consist"
    r"|signed distance|sdf|collision|collid|pierc|overlap|simulation displacement"
    r"|volumetric|contact depth|solid intersect",
    re.I)


def population():
    rows = [json.load(open(f)) for f in sorted(glob.glob(str(R / "corpus/rows/*.json")))]
    return sorted(r["key"] for r in rows
                  if r.get("class") == "method" and r.get("penetration") == "not addressed")


def sample(pop):
    return sorted(random.Random(SEED).sample(pop, N_SAMPLE))


def sources(key):
    for rel in (f"papers/md/{key}.md", f"papers/md/{key}.ocr.md", f"code/md/{key}.md"):
        p = R / rel
        if p.exists():
            yield rel, p.read_text(errors="replace")


def main():
    pop = population()
    print(f"population: {len(pop)} method rows whose penetration field says not addressed")
    if len(pop) != POPULATION_AT_AUDIT:
        print(f"STALE: the audit in reviews/penetration_audit.md was drawn from "
              f"{POPULATION_AT_AUDIT} rows, not {len(pop)}. Redraw and re-read it.")
        return 1
    samp = sample(pop)
    print(f"sample: {N_SAMPLE} drawn with random.Random({SEED}).sample over the sorted population\n")
    show = "-v" in sys.argv
    for key in samp:
        seen = []
        for rel, text in sources(key):
            hits = [(i, ln) for i, ln in enumerate(text.splitlines(), 1) if TERMS.search(ln)]
            seen.append(f"{rel.split('/')[0]}={len(hits)}")
            if show:
                for i, ln in hits:
                    print(f"    {rel}:{i}: {ln[:160]}")
        print(f"  {key:<36} {' '.join(seen)}")
    print(f"\nRead the verdicts in reviews/penetration_audit.md. Pass -v for the passages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
