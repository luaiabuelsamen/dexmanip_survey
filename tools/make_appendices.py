"""Generate Appendix B and Appendix C from the corpus.

`paper/OUTLINE.md` promises both and neither existed. Both are generated here rather than
written, for the same reason the body tables are: an appendix is where a reader goes to check a
number, so it cannot contain a value no note confirmed.

Appendix B, the full hand table with its sources. Table 2 and Table 3 truncate cells to keep the
body readable, and they split the hands by whether one can be bought. Appendix B prints every
hand row once, at full width, and adds the provenance columns the body tables leave out: what
kind of source the specification came from, the URL it was fetched from, whether a PDF or page
is in the manifest with a hash, and the note that was read.

Appendix C, the per-paper reward term extraction. Table 5 is a presence matrix over nine term
families for one task family. Appendix C is the underlying extraction for every method row that
records a reward at all: how many terms the paper states, their names as the paper names them,
where in the note the reward was read from, and the full text of any disagreement between the
paper and the released code with its classification. The classifications are what Sec. 5.8 and
Sec. 8.1 count, so this is where a reader checks that count.

Usage: python3 tools/make_appendices.py
Writes: paper/APPENDIX_B.md, paper/APPENDIX_C.md
"""
import glob
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
EM = " "


def cell(v):
    """A value with no width limit. An appendix exists so nothing has to be cut."""
    if v is None or v == "" or v == []:
        return EM
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, list):
        v = ", ".join(str(x) for x in v)
    return str(v).replace("|", "/").replace("\n", " ").strip()


def table(rows, cols, headers, note):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    empty = total = 0
    for r in rows:
        vals = [cell(r.get(c)) for c in cols]
        vals[0] = f"`{vals[0]}`"
        empty += sum(1 for v in vals if v == EM)
        total += len(vals)
        out.append("| " + " | ".join(vals) + " |")
    pct = 100 * empty // max(total, 1)
    out.append(f"\n*{len(rows)} rows. {empty} of {total} cells ({pct} percent) are values no "
               f"source stated. {note}*")
    return "\n".join(out)


def load():
    rows = {}
    for f in glob.glob(str(R / "corpus/rows/*.json")):
        r = json.load(open(f))
        rows[r["key"]] = r
    bib = {e["key"]: e for e in json.loads((R / "corpus/bib.json").read_text())}
    man = json.loads((R / "corpus/manifest.json").read_text())
    return rows, bib, man


def source_url(key, bib):
    e = bib.get(key) or {}
    for field in ("pdf_url", "github"):
        if e.get(field):
            return e[field]
    if e.get("arxiv"):
        return f"arXiv:{e['arxiv']}"
    return None


def provenance(key, man):
    """One clause saying whether a parsed source with a hash exists for this entry."""
    m = man.get(key) or {}
    if not m:
        return "no manifest entry"
    if not m.get("sha256"):
        return "fetched, no hash recorded"
    pages = m.get("pages")
    return "%s, %s, fetched %s" % (
        (f"{pages} pp" if pages else "page"), m["sha256"][:8], m.get("fetched") or "undated")


def used_by_map():
    """Reuse tools/make_tables.py's hand-to-method patterns rather than restating them.

    That module owns the mapping and documents why each pattern exists. If it is mid-edit or
    fails to import, the column is dropped rather than guessed.
    """
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("_mt", R / "tools/make_tables.py")
        mt = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mt)
        methods = [r for r in mt.ROWS.values() if r.get("class") == "method"]
        return {k: mt.used_by(k, methods, cap=99) for k in mt.USES}
    except Exception as exc:  # noqa: BLE001
        print("  (used_by column dropped:", exc, ")")
        return None


def appendix_b(rows, bib, man):
    hands = [r for r in rows.values() if r.get("class") == "hand"]
    hands.sort(key=lambda r: (str(r.get("release_status")), -(r.get("dof") or 0), r["key"]))
    used = used_by_map()
    for h in hands:
        h["_url"] = source_url(h["key"], bib)
        h["_prov"] = provenance(h["key"], man)
        h["_note"] = f"papers/notes/{h['key']}.md" if (R / f"papers/notes/{h['key']}.md").exists() else None
        if used is not None:
            h["_used"] = used.get(h["key"], "0")

    spec_cols = ["key", "maker", "dof", "actuated_dof", "actuation", "weight_g",
                 "fingertip_force_n", "payload", "tactile", "control_rate", "price_usd",
                 "bom_cost_usd", "open_hardware", "license", "sim_model", "release_status"]
    spec_head = ["hand", "maker", "DoF", "act. DoF", "actuation", "weight g", "tip force N",
                 "payload", "tactile", "control rate", "price USD", "BOM USD", "open HW",
                 "licence", "sim model", "status"]
    prov_cols = ["key", "source_quality", "claim_date", "spec_caveat", "_url", "_prov", "_note"]
    prov_head = ["hand", "source quality", "claim date", "caveat recorded in the row",
                 "source URL", "parsed source in the manifest", "note"]
    if used is not None:
        prov_cols.append("_used")
        prov_head.append("corpus method rows running it")

    parts = ["## Appendix B. The full hand table with its sources", "",
             "Table 2 and Table 3 split these rows by whether the hand can be bought, and truncate "
             "their cells to stay readable. This appendix prints every hand row once and at full "
             "width. Nothing here is a measurement by this survey. Every specification is a "
             "manufacturer claim, a figure in a paper, or a figure in a press article, and the "
             "`source quality` column in B.2 says which. Cells reproduce the text stored in the "
             "row, with the source's own punctuation and wording.", "",
             "### B.1 Specifications as the source states them", "",
             table(hands, spec_cols, spec_head,
                   "A blank price is a hand with no public list price rather than a free hand."),
             "", "### B.2 Where each specification came from", "",
             table(hands, prov_cols, prov_head,
                   "`parsed source in the manifest` gives page count, the first eight characters "
                   "of the sha256 of the stored copy, and the date it was fetched. A hand with no "
                   "manifest entry was recorded from a page that could not be stored, and its row "
                   "should be read as a claim with no retrievable source.")]
    (R / "paper/APPENDIX_B.md").write_text("\n".join(parts) + "\n")
    return len(hands)


def appendix_c(rows):
    rm = json.loads((R / "corpus/reward_matrix.json").read_text())
    src = {r["key"]: r.get("src") for r in rm["rows"]}
    marks = {r["key"]: r for r in rm["rows"]}

    meth = [r for r in rows.values() if r.get("class") == "method"]
    # Every method row carrying reward evidence of any kind: a term count, term names, a
    # position in the reward-term matrix, or a recorded paper/code disagreement. The column that
    # marks the matrix is named after the matrix and not after a table number: the LaTeX edition
    # tabulates the matrix in the repository, so "in Table 5" named nothing a reader could find.
    keep = [r for r in meth if r.get("reward_terms") or r.get("reward_term_names")
            or r["key"] in marks or r.get("paper_code_mismatch")]
    keep.sort(key=lambda r: (r.get("year") or 0, r["key"]))
    for r in keep:
        r["_src"] = src.get(r["key"])
        r["_t5"] = "yes" if r["key"] in marks else None
        r["_names"] = ", ".join(r.get("reward_term_names") or []) or None

    cols = ["key", "year", "paradigm", "reward_terms", "_names", "_src", "_t5", "code_released",
            "mismatch_class", "mismatch_confidence"]
    head = ["method", "yr", "paradigm", "terms stated", "term names as the paper names them",
            "where the reward was read", "in reward matrix", "code released", "paper/code class",
            "confidence"]

    classes = {}
    for r in keep:
        if r.get("mismatch_class"):
            classes.setdefault(r["mismatch_class"], []).append(r)

    parts = ["## Appendix C. Per-paper reward term extraction", "",
             "Table 5 marks nine recurring term families across the in-hand reorientation "
             "methods. This appendix is the extraction underneath it, over every method row that "
             "records a reward at all. `terms stated` counts the terms the paper itself names. "
             "`where the reward was read` gives the section of the paper or the file in the "
             "released code that the note quotes. A row with a `paper/code class` is one where "
             "the two disagree, and C.2 prints the disagreement in full. Cells and entries "
             "reproduce the text stored in the row, with the source's own punctuation and "
             "wording.", "",
             "### C.1 The extraction", "",
             table(keep, cols, head,
                   "A blank `terms stated` with a filled `term names` column is a paper that "
                   "names its terms without numbering them. `in reward matrix` marks the rows "
                   "that are also in the reward-term matrix, which covers in-hand reorientation "
                   "only."), ""]

    parts += ["### C.2 Paper against released code, in full", "",
              "Each entry below is the disagreement text stored in the row, unedited. The class "
              "is what Sec. 5.8 and Sec. 8.1 count. `contradiction` means the paper states one "
              "value and the shipped code demonstrably states another. `parse-limitation` means "
              "this survey's own parse could not settle it and the accusation is withdrawn. "
              "`code-absent` means the described component is not in the released repository. "
              "`version-skew` means the repository is a later generation than the paper. "
              "`internal-inconsistency` means the paper disagrees with itself and no code is "
              "implicated. Every `contradiction` entry carries an `Artefact` line: the "
              "repository, the commit `corpus/code_manifest.json` records, the file inside it "
              "and where in that file the value sits, so the entry can be checked without "
              "asking anyone. None of those authors was written to before this survey was "
              "posted; section 5.6 says so beside the finding, the letters that were drafted "
              "and not sent are in `outreach/` in the corpus, which is available from the "
              "author at the address in the byline, and the route by which a disputed entry "
              "is corrected is stated there too.", ""]
    order = ["contradiction", "internal-inconsistency", "version-skew", "code-absent",
             "parse-limitation"]
    for cls in order + [c for c in sorted(classes) if c not in order]:
        group = classes.get(cls) or []
        if not group:
            continue
        parts.append(f"**{cls}, {len(group)} rows.**")
        parts.append("")
        for r in group:
            conf = r.get("mismatch_confidence") or "confidence not recorded"
            parts.append(f"- `{r['key']}` ({conf}). {cell(r.get('paper_code_mismatch'))}")
            a = r.get("mismatch_artifact")
            if a:
                parts.append(
                    "  Artefact: `%s` at `%s`, `%s` (`%s`)."
                    % (a["repo"].replace("https://github.com/", ""), a["commit"][:10],
                       a["file"], a["locator"]))
            if r.get("mismatch_review"):
                parts.append(f"  Review: {cell(r['mismatch_review'])}")
        parts.append("")

    unclassed = [r for r in keep if r.get("paper_code_mismatch") and not r.get("mismatch_class")]
    if unclassed:
        parts.append("**not yet classified, %d rows.**" % len(unclassed))
        parts.append("")
        for r in unclassed:
            parts.append(f"- `{r['key']}`. {cell(r.get('paper_code_mismatch'))}")
        parts.append("")

    (R / "paper/APPENDIX_C.md").write_text("\n".join(parts) + "\n")
    return len(keep), {c: len(v) for c, v in sorted(classes.items())}, len(unclassed)


def main():
    rows, bib, man = load()
    n_hands = appendix_b(rows, bib, man)
    n_rew, classes, n_unclassed = appendix_c(rows)
    print(f"APPENDIX_B.md: {n_hands} hand rows")
    print(f"APPENDIX_C.md: {n_rew} method rows with reward evidence, "
          f"{n_unclassed} disagreements not yet classified")
    print("  paper/code classes:", classes)


if __name__ == "__main__":
    main()
