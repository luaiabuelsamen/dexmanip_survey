#!/usr/bin/env python3
"""Turn the survey's inline citation keys into LaTeX citations.

The markdown edition cites a work by writing its corpus key in backticks: `dextrack_2025`. It also
writes file names, config fields and function names in backticks: `corpus/rows`,
`compute_humanoid_reward`, `interpen_thresh: 0.001`. The difference is not visible in the markup,
only in corpus/bib.json, so citeify() rewrites a span only when the span is a key that the
bibliography actually defines. Everything else is left in backticks for the section converter to
set as \\texttt{}, which is what it is: a name in the code, not a citation.

A run of keys separated by nothing but a comma and a space is one citation in the prose, so the
citations are merged into a single \\cite{a,b,c}; a run joined by "and" is two sentences' worth of
emphasis and is left as two \\cite commands.

citeify() must run before code spans become \\texttt{}, and is safe to run twice: a \\cite it has
already written has no backticks left to match.

Usage as a filter:  python tools/mdtex_cite.py < section.md > section.tex.part
Self-test:          python tools/mdtex_cite.py --selftest
"""
import json
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
BIB_JSON = R / "corpus/bib.json"

_KEYS = None
_FENCE = re.compile(r"(?ms)^```.*?^```[ \t]*$")
_SPAN = re.compile(r"`([^`\n]+)`")
_MERGE = re.compile(r"\\cite\{([^{}]+)\}, \\cite\{([^{}]+)\}")


def corpus_keys():
    """The set of keys the bibliography defines. Anything outside it is not a citation."""
    global _KEYS
    if _KEYS is None:
        _KEYS = {e["key"] for e in json.loads(BIB_JSON.read_text())}
    return _KEYS


def citeify(text, keys=None):
    """Rewrite every backticked corpus key in `text` as \\cite{key}, and merge comma-separated runs.

    Code spans that are not bibliography keys are returned untouched, backticks included.
    """
    keys = corpus_keys() if keys is None else keys

    # A fenced block is quoted source, not prose: a key inside it is being shown, not cited.
    blocks = []

    def stash(m):
        blocks.append(m.group(0))
        return "\x00FENCE%d\x00" % (len(blocks) - 1)

    out = _FENCE.sub(stash, text)
    out = _SPAN.sub(lambda m: r"\cite{%s}" % m.group(1) if m.group(1) in keys else m.group(0), out)
    while True:
        merged = _MERGE.sub(r"\\cite{\1,\2}", out)
        if merged == out:
            break
        out = merged
    for i, b in enumerate(blocks):
        out = out.replace("\x00FENCE%d\x00" % i, b)
    return out


def _selftest():
    keys = {"dextrack_2025", "hora_2022", "dexpbt_2023", "leap_hand_v2_adv_2025"}
    cases = [
        ("tracking `dextrack_2025` is", r"tracking \cite{dextrack_2025} is"),
        ("`compute_humanoid_reward` and `corpus/rows` stay",
         "`compute_humanoid_reward` and `corpus/rows` stay"),
        ("three: `hora_2022`, `dexpbt_2023`, `dextrack_2025`.",
         r"three: \cite{hora_2022,dexpbt_2023,dextrack_2025}."),
        ("`hora_2022` and `dexpbt_2023`", r"\cite{hora_2022} and \cite{dexpbt_2023}"),
        ("`hora_2022`, `interpen_thresh: 0.001`", r"\cite{hora_2022}, `interpen_thresh: 0.001`"),
        ("`not_a_key_2025`", "`not_a_key_2025`"),
        ("```\n`dextrack_2025`\n```\n`hora_2022`",
         "```\n`dextrack_2025`\n```\n" + r"\cite{hora_2022}"),
    ]
    bad = 0
    for src, want in cases:
        got = citeify(src, keys)
        if got != want:
            bad += 1
            print("FAIL\n  in   %r\n  want %r\n  got  %r" % (src, want, got))
    # idempotent
    once = citeify(cases[2][0], keys)
    if citeify(once, keys) != once:
        bad += 1
        print("FAIL not idempotent: %r" % citeify(once, keys))
    print("%d of %d cases pass, %d keys in corpus/bib.json"
          % (len(cases) + 1 - bad, len(cases) + 1, len(corpus_keys())))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    sys.stdout.write(citeify(sys.stdin.read()))
