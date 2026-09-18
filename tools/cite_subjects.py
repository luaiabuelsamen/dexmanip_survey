#!/usr/bin/env python3
"""Build the citation-key to subject-name map used by the LaTeX style pass on tex/sections/.

A citation that stands as the grammatical subject of a sentence ("[2] draws the same line")
reads as a number doing the acting. IEEE style wants a noun phrase as the subject with the
citation attached to it ("Bicchi [2] draws the same line"). This module answers one question,
reproducibly, for every key in corpus/bib.json: what noun phrase names that work?

The name is chosen in this order.

1. The work's own short name, taken from the title before its first colon, when that prefix
   reads as a name rather than as the opening of a sentence: at most three words, every word
   name-like (capitalised, all-caps, or carrying a digit), and no function words. This is what
   gives DexTrack, AnyRotate, RoboPianist, Isaac Gym, DIGIT, GR00T N1. A title with no colon
   that is itself a name by the same test counts too, which is MuJoCo Playground.
2. For a product page, a company announcement or a software release with no such title prefix,
   the maker's name from the authors field, stripped of corporate suffixes: Figure, Unitree.
3. Otherwise the author surname, with "et al." kept when the authors field carries it:
   "Handa et al.", "Bicchi".

OVERRIDES holds the entries where those rules produce a name the field does not use, each with
the reason. Everything else is derived, so a reviewer can re-run this file and check the map.

Usage:
    python3 tools/cite_subjects.py              # print the map, one key per line
    python3 tools/cite_subjects.py --json       # print it as JSON
    python3 tools/cite_subjects.py --source     # print the rule that produced each name
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_JSON = os.path.join(REPO, "corpus", "bib.json")

# Words that give away a title prefix as prose rather than a name.
FUNCTION_WORDS = {
    "a", "an", "the", "and", "or", "of", "for", "with", "in", "into", "on", "to", "toward",
    "towards", "from", "via", "without", "beyond", "as", "at", "by", "is", "are", "no", "not",
    "this", "that", "its", "their", "our", "we", "learning", "scaling", "benchmarking",
    "evaluating", "solving", "planning", "closing", "crossing", "rethinking", "digitizing",
    "getting", "measuring", "adaptive", "robotic", "simulation", "contact", "hands", "reliable",
}

# Corporate suffixes dropped from a maker's name, so that "Figure AI" is cited as "Figure".
MAKER_SUFFIXES = {
    "ai", "robotics", "robots", "technologies", "technology", "tech", "company", "inc",
    "corporation", "corp", "labs", "lab", "research",
}

# Venues that mean the entry is a product page, an announcement or a code release rather than a
# paper with an author list.
NON_PAPER_VENUE = re.compile(
    r"commercial product|company announcement|open-hardware|software release|software \(|blog",
    re.IGNORECASE,
)

# Names the derivation gets wrong. Each line says why the derived name is not the one the field
# uses. Keys not listed here are derived by the rules above.
OVERRIDES = {
    # Title has no colon, but the release is universally cited by its repository name.
    "bidexhands_2022": "Bi-DexHands",
    # The survey's prose calls the second-generation dataset OakInk-V2 throughout; the title
    # shouts OAKINK2.
    "oakink2_2024": "OakInk-V2",
    # "THE COLOSSEUM" survives the rules only as shouted prose; the benchmark's own prose name.
    "colosseum_2024": "The Colosseum",
    # Title is "Benchmarking in Manipulation Research: ..."; the object set is the YCB set.
    "ycb_2015": "YCB",
    # Title is a sentence ("Digitizing Touch with ..."); the fingertip is DIGIT 360.
    "digit360_2024": "DIGIT 360",
    # "GR-Dexter Technical Report" is a report title, not a colon-prefixed name.
    "gr_dexter_2025": "GR-Dexter",
    # Greek-letter model names are set as maths in the prose, matching the rest of the survey.
    "pi0_2024": r"$\pi_0$",
    "pi05_2025": r"$\pi_{0.5}$",
    "pistar06_2025": r"$\pi^{*}_{0.6}$",
    # dm_control needs LaTeX escaping and is set as code in the prose.
    "dm_control_2020": r"\texttt{dm\_control}",
    # The citation key names the work and the field uses that name, but the title carries no
    # colon prefix to derive it from.
    "hora_2022": "Hora",
    "rotateit_2023": "RotateIt",
    "penspin_2024": "PenSpin",
    "dapg_2017": "DAPG",
    "pddm_2019": "PDDM",
    "bidexhd_2024": "BiDexHD",
    "hato_visuotactile_2024": "HATO",
    "resdex_2024": "ResDex",
    "simpler_2024": "SIMPLER",
    "umi_2024": "UMI",
    "aloha_act_2023": "ALOHA",
    "bimangrasp_2024": "BimanGrasp",
    "bidex_teleop_2024": "Bidex",
    # The paper is "Learning Dexterous In-Hand Manipulation"; the field cites the lab.
    "openai_dexterity_2018": "OpenAI",
    "openai_rubiks_cube_2019": "OpenAI",
    # Physical Intelligence and the Gemini Robotics team are the authors of record; the model
    # names are handled above for pi0 and below by title for Gemini Robotics.
    "helix_2025": "Helix",
}


def words(text: str) -> list[str]:
    return [w for w in re.split(r"\s+", text.strip()) if w]


def name_like(word: str) -> bool:
    """True when a title word reads as part of a name rather than as prose."""
    bare = word.strip("(),.'’\"")
    if not bare:
        return False
    if bare.lower() in FUNCTION_WORDS:
        return False
    if bare.isupper():                      # GRAB, LIBERO, TACO
        return True
    if any(c.isdigit() for c in bare):      # GR00T, HOT3D, pi0, Dex5-1
        return True
    if bare[0].isupper() and any(c.isupper() for c in bare[1:]):   # DexArt, RoboPianist
        return True
    if bare[0].isupper():                   # Isaac, Gym, Eureka, Newton, Sparsh
        return True
    if "_" in bare:                         # dm_control
        return True
    return False


def title_short_name(title: str) -> str | None:
    """The work's own short name: the title prefix before a colon, when it reads as a name."""
    if ":" not in title:
        return None
    prefix = title.split(":", 1)[0].strip()
    ws = words(prefix)
    if not ws or len(ws) > 3:
        return None
    if not all(name_like(w) for w in ws):
        return None
    return " ".join(ws)


def whole_title_name(title: str) -> str | None:
    """A title that is itself a name: three words or fewer, every word name-like."""
    if ":" in title:
        return None
    ws = words(re.sub(r"\(.*?\)", "", title))
    if not ws or len(ws) > 3:
        return None
    if not all(name_like(w) for w in ws):
        return None
    return " ".join(ws)


def product_name(title: str) -> str | None:
    """The leading name-like run of a product title: "Allegro Hand V4 (Wonik Robotics)"."""
    kept = []
    for w in words(re.split(r"[(:/,]", title)[0]):
        if name_like(w):
            kept.append(w)
        else:
            break
        if len(kept) == 3:
            break
    if not kept:
        return None
    return " ".join(kept)


def maker_name(authors: str) -> str | None:
    """The maker behind a product page, trimmed of corporate suffixes: "Figure AI" -> "Figure"."""
    first = re.split(r"\s+(?:and|/|&)\s+|,", authors)[0]
    first = re.sub(r"\(.*?\)", "", first).strip()
    ws = words(first)
    while len(ws) > 1 and ws[-1].strip(".").lower() in MAKER_SUFFIXES:
        ws.pop()
    return " ".join(ws) if ws else None


def author_name(authors: str) -> str:
    """Author surname, keeping "et al." and joining a two-author entry with "and"."""
    a = authors.strip()
    if re.search(r"\bet al\.?", a):
        surname = re.split(r"\s*,\s*|\s+et al", a)[0].strip()
        return f"{surname} et al."
    parts = [p.strip() for p in re.split(r"\s*(?:,|&|\band\b)\s*", a) if p.strip()]
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return f"{parts[0]} et al."


def build_map(entries: list[dict]) -> dict[str, tuple[str, str]]:
    """key -> (name, which rule produced it)."""
    out: dict[str, tuple[str, str]] = {}
    for e in entries:
        key = e["key"]
        title = (e.get("title") or "").strip()
        authors = (e.get("authors") or "").strip()
        venue = (e.get("venue") or "").strip()
        if key in OVERRIDES:
            out[key] = (OVERRIDES[key], "override")
            continue
        short = title_short_name(title) or whole_title_name(title)
        if short:
            out[key] = (short, "title")
            continue
        if NON_PAPER_VENUE.search(venue):
            prod = product_name(title)
            mk = maker_name(authors)
            if prod and mk and prod.split()[0].lower() == mk.split()[0].lower():
                out[key] = (prod, "product")
            elif prod and (len(words(prod)) >= 2 or any(c.isupper() for c in prod[1:]) or any(c.isdigit() for c in prod)):
                out[key] = (prod, "product")
            elif mk:
                out[key] = (mk, "maker")
            else:
                out[key] = (author_name(authors), "author")
            continue
        out[key] = (author_name(authors), "author")
    return out


def load(path: str = BIB_JSON) -> list[dict]:
    with open(path) as fh:
        return json.load(fh)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--bib", default=BIB_JSON)
    ap.add_argument("--json", action="store_true", help="print the map as JSON")
    ap.add_argument("--source", action="store_true", help="print the rule behind each name")
    ap.add_argument("--keys", nargs="*", help="print only these keys")
    args = ap.parse_args(argv)

    entries = load(args.bib)
    m = build_map(entries)
    if args.keys:
        m = {k: v for k, v in m.items() if k in set(args.keys)}
    if args.json:
        print(json.dumps({k: v[0] for k, v in sorted(m.items())}, indent=1))
        return 0
    width = max(len(k) for k in m) if m else 0
    for k in sorted(m):
        name, how = m[k]
        line = f"{k:<{width}}  {name}"
        if args.source:
            line += f"   [{how}]"
        print(line)
    print(f"# {len(m)} keys", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
