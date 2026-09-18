# dexmanip-survey

A literature review of learning-based dexterous manipulation, single-hand and
bimanual: simulators, hands and their makers (released and announced), how
policies are trained (RL, imitation, hybrids, foundation policies), how they
are evaluated, and where the gaps are.

The review is written only from material that is on disk in parsed form.

| directory | contents |
|---|---|
| `corpus/` | `bib_<topic>.json` per-topic bibliographies, merged into `bib.json`; `manifest.json` (PDF sha256, pages, converter) and `code_manifest.json` (repo, commit) |
| `papers/pdf/` | downloaded PDFs (arXiv unless `pdf_url` says otherwise) |
| `papers/md/` | one markdown per paper, converted with pymupdf4llm from the PDF beside it |
| `papers/notes/` | one structured note per paper, written from `papers/md/` and `code/md/` only |
| `code/md/` | one markdown per repository: README, file tree, task/reward configs, reward and observation function bodies. Clones are deleted after parsing. |
| `paper/` | the survey (`survey.md`), figures, tables |
| `reviews/` | adversarial reviews of the survey and the responses to them |
| `tools/` | `fetch_papers.py`, `fetch_code.py`, `merge_bib.py` |

```
. .venv/bin/activate
python tools/merge_bib.py
python tools/fetch_papers.py
python tools/fetch_code.py
```
