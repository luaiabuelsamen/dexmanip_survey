# dexmanip-survey

A literature review of learning-based dexterous manipulation, single-hand and bimanual:
simulators, hands and their makers including announced ones, how policies are trained, how they
are evaluated, and where the gaps are. The review is written only from material parsed onto disk.

The survey is `paper/survey.md`. It is assembled by `tools/assemble.py` from `paper/sections/`
with the generated tables and figures inlined, so it should be regenerated rather than edited.

## What it found

Three results came out of opening the repositories and the vendor pages rather than reading the
papers alone.

Ten of the sixty-two method papers that released parseable code contradict their own paper about
the objective that was trained. Thirty-eight disagreements were recorded in total, and the
classification of every one is in the `mismatch_class` field of `corpus/rows/`, including the seven
accusations this survey withdrew after review.

Closed-loop policies do not report interpenetration. Eleven of the ninety-six method rows whose
notes settle it handle it at all, four inside a closed-loop policy, and none reports a penetration
number for its own trained policy's rollouts. The scope of that claim matters. Grasp synthesis and
hand-object reconstruction have reported penetration depth and intersection volume comparatively
for years, so the gap is specific to learned closed-loop control, not to the field. The tooling is
not the obstacle either: NVIDIA's own benchmark repository computes per-environment maximum
interpenetration depth and gates a policy update on a one-millimetre threshold.

Hardware and software have come apart. Thirty-three hands are tabulated, the simulators name five
between them, and of the hands that can actually be bought or built from published designs, seven
appear in no method paper in this corpus.

## Layout

| directory | contents |
|---|---|
| `paper/` | `survey.md`, `sections/`, generated `tables/` and `figures/`, `METHOD.md`, the appendices, and the writing brief |
| `corpus/` | `bib.json` and the per-topic bibliographies, `rows/` with one structured record per work, the manifests with hashes and commits |
| `papers/pdf/`, `papers/md/` | downloaded sources and their parsed markdown, including `.ocr.md` where equations had to be recovered by OCR |
| `papers/notes/` | one structured note per work, written only from the parsed sources, plus the rules that govern them |
| `code/md/` | one markdown per repository: README, file tree, task and reward configs, reward and observation bodies. Clones are deleted after parsing. |
| `reviews/` | the adversarial reviews, the verification round, the claim ledger and the consistency list |
| `tools/` | fetchers, parsers, and the generators for every table and figure |

## Rebuilding

```
. .venv/bin/activate
python tools/merge_bib.py           # per-topic bibliographies into corpus/bib.json
python tools/fetch_papers.py        # PDFs, then markdown, with hashes into the manifest
python tools/fetch_code.py          # shallow clones, parsed, then deleted
python tools/fetch_pages.py         # vendor pages for hands with no paper
python tools/ocr_equations.py KEY   # recover equations that render as images
python tools/check_notes.py         # note quality gate
python tools/make_tables.py tools/make_eval_tables.py tools/make_survey_table.py
python tools/make_figures.py tools/make_diagrams.py tools/make_flow_tree.py
python tools/make_appendices.py
python tools/assemble.py            # paper/survey.md
```

## Reading it critically

Start with `paper/METHOD.md`, which says what the method cannot do. The coverage statistics measure
what this survey's extraction captured, so each is a floor rather than a rate. An audit of the
nulls recovered a stated trial count from fifteen of thirty-four rows that had looked silent, which
moved that headline by nearly thirty points. Six works are behind paywalls and no claim rests on
them. Vendor specifications are manufacturer claims and are dated as such.

## The PDF

`python tools/make_pdf.py` renders `paper/survey.md` to `paper/survey.pdf`. It converts the
markdown to HTML with a print stylesheet, inlines the six figures so the file is self-contained,
drops their dark-mode rules because a printed page has one theme, puts every table of more than
five columns and the two widest figures on real landscape pages, and prints through headless
Chromium. Page numbers are stamped afterwards with PyMuPDF, because Chromium's own footer carries
a URL and a date.
