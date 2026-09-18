#!/usr/bin/env python3
"""Generate tex/refs.bib from corpus/bib.json, one BibTeX entry per bibliography key.

What the entry types mean here, which is a claim about the sources and not a formatting choice:

  @inproceedings / @article  a work that appeared at a venue. If it is also on arXiv it carries
                             eprint/archivePrefix/primaryClass, because the version this survey
                             parsed is the arXiv one and a reader should be able to fetch it.
  @misc with howpublished    a preprint that has no venue. It has not been refereed and the entry
                             says so by naming arXiv as the only place it appeared.
  @misc with a note          a vendor product page, a company announcement, a blog post or a
                             software release page. The note says what kind of source it is and
                             when it was fetched. These are manufacturer claims with no review and
                             no method section, and the bibliography must not dress them up as
                             papers.
  @incollection              one book chapter, which none of the four rules above covers.

The six works whose full text was never obtained keep their entry and carry a note saying so, so
that a reader who follows a citation to one of them learns that no claim rests on its contents.

Usage:
    python tools/make_bib.py             # write tex/refs.bib, print the tally
    python tools/make_bib.py --probe     # also write tex/probe_bib.tex, a 20-citation probe
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

R = Path(__file__).resolve().parents[1]
BIB_JSON = R / "corpus/bib.json"
PAGES_MANIFEST = R / "corpus/pages_manifest.json"
PAPER_MANIFEST = R / "corpus/manifest.json"
MD_DIR = R / "papers/md"
ROWS_DIR = R / "corpus/rows"
OUT_BIB = R / "tex/refs.bib"
OUT_PROBE = R / "tex/probe_bib.tex"

# --- venue keywords ---------------------------------------------------------------------------
# The survey's own rule: these words in a venue string mean a refereed venue of that kind.
# Conference..Humanoids and Transactions..Review are the survey's list; "Symposium" and
# "Magazine" are added here because two venues in the corpus are one of those and nothing else.
INPROC_WORDS = ("Conference", "CoRL", "ICRA", "IROS", "RSS", "NeurIPS", "ICLR", "ICML",
                "CVPR", "ECCV", "ICCV", "AAAI", "Humanoids", "Symposium")
ARTICLE_WORDS = ("Transactions", "Journal", "Letters", "Science", "Review", "Magazine")

# Venue strings in corpus/bib.json use abbreviations that contain none of those words. Expanding
# them before the keyword test is what keeps a T-RO paper an @article instead of falling through
# to @misc. Every expansion used is reported at the end of a run.
ABBREV = {
    "RA-L": "Robotics and Automation Letters",
    "T-RO": "Transactions on Robotics",
    "IJRR": "International Journal of Robotics Research",
    "3DV": "International Conference on 3D Vision",
    "ICAR": "International Conference on Advanced Robotics",
    "RO-MAN": "International Conference on Robot and Human Interactive Communication",
    "SSCI": "Symposium Series on Computational Intelligence",
    "Autonomous Robots": "Autonomous Robots Journal",
    "Frontiers in Robotics and AI": "Frontiers in Robotics and AI Journal",
    "Nature Communications": "Nature Communications Journal",
    "Software Impacts": "Software Impacts Journal",
}

# Venue strings that name a source that is not a paper, and the phrase the note uses for it.
PAGE_KINDS = {
    "commercial product": "vendor product page",
    "company announcement": "company announcement",
    "company announcement (unreleased)": "company announcement, hand not released",
    "company announcement and USPTO patents (unreleased)":
        "company announcement and USPTO patent filings, hand not released",
    "open-hardware project": "open-hardware project page",
    "software release": "software release page",
    "software release (GTC 2025)": "software release announcement, NVIDIA GTC 2025",
    "software release (Linux Foundation)": "software release announcement, Linux Foundation",
    "software (pybullet.org)": "software documentation page",
    "Figure AI blog (Feb 2025)": "company blog post, February 2025",
    "NVIDIA GEAR release (Dec 2025)": "company press release, December 2025",
}

# corpus/bib.json tags five entries [SOURCE UNAVAILABLE] in their `why`. paper/METHOD.md,
# "Sources that could not be obtained", names six: the sixth is Roa and Suarez 2015, whose row
# records the fetched source as a 434-byte Springer interstitial with no article text. The tag is
# missing from its bib entry, so it is named here rather than silently dropped from the count.
UNOBTAINABLE_EXTRA = {"roa_suarez_grasp_quality_2015"}

# Non-ASCII that appears in the corpus, written as BibTeX-safe LaTeX so the .bib does not depend
# on inputenc being loaded by whatever document cites it.
ACCENTS = {
    "á": r"{\'a}", "é": r"{\'e}", "í": r"{\'i}", "ó": r"{\'o}", "ú": r"{\'u}",
    "à": r"{\`a}", "è": r"{\`e}", "ä": r"{\"a}", "ö": r"{\"o}", "ü": r"{\"u}",
    "ñ": r"{\~n}", "ç": r"{\c c}", "å": r"{\aa}", "ø": r"{\o}", "–": "--", "—": "---",
    "’": "'", "‘": "`", "“": "``", "”": "''", "×": r"$\times$", "°": r"$^\circ$",
}
SPECIALS = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%",
    "$": r"\$", "#": r"\#", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def tex_escape(s):
    """Escape every LaTeX special character in a field value."""
    out = []
    for ch in str(s):
        if ch in SPECIALS:
            out.append(SPECIALS[ch])
        elif ch in ACCENTS:
            out.append(ACCENTS[ch])
        elif ord(ch) > 127:
            out.append("?")  # reported by the caller; nothing in the corpus reaches this today
        else:
            out.append(ch)
    return "".join(out)


def authors_field(authors):
    """Turn the corpus' short author string into a BibTeX author list.

    The corpus stores surnames only ("Okamura, Smith, Cutkosky", "Ma & Dollar", "Liu et al.").
    BibTeX reads a comma as "Last, First" and an ampersand as part of a name, so both have to
    become " and ". "et al." becomes "and others", which is what makes BibTeX print "et al.".
    A multi-word element is an organisation ("Boston Dynamics") and is braced so that BibTeX does
    not initialise it into "B. Dynamics".
    """
    s = authors.strip()
    et_al = bool(re.search(r"\bet\s+al\.?$", s))
    s = re.sub(r"\s*\bet\s+al\.?$", "", s).strip(" ,")
    parts = [p.strip() for p in re.split(r"\s*(?:,|&|/|\band\b)\s*", s) if p.strip()]
    names = []
    for p in parts:
        p = tex_escape(p)
        names.append("{%s}" % p if len(p.split()) > 1 else p)
    if et_al:
        names.append("others")
    return " and ".join(names)


def expand_venue(venue):
    """Expand the abbreviations the keyword test cannot see. Returns (expanded, used)."""
    out, used = venue, []
    for ab, full in ABBREV.items():
        if re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(ab), out):
            out = out.replace(ab, full)
            used.append(ab)
    return out, used


def arxiv_only(venue):
    """True when the venue string says nothing but 'arXiv', a year and an author's affiliation."""
    s = re.sub(r"\([^)]*\)", " ", venue)
    s = re.sub(r"\b(19|20|21)\d{2}\b", " ", s)
    s = re.sub(r"[^A-Za-z]+", " ", s).strip().lower()
    return s == "arxiv"


def keyword_type(expanded):
    if any(w in expanded for w in INPROC_WORDS):
        return "inproceedings"
    if any(w in expanded for w in ARTICLE_WORDS):
        return "article"
    return None


def venue_field(venue, year):
    """The venue as it should print: the arXiv clause removed, and the year removed only when it is
    the same year the entry already carries. A venue year that differs is the year the work actually
    appeared at that venue, against an arXiv year in the year field, and it is kept. Returns
    (venue, volume, number)."""
    s = re.sub(r";\s*arXiv[^;]*$", "", venue)
    s = re.sub(r"\(\s*arXiv[^)]*\)", "", s)
    s = re.sub(r"^\s*arXiv\s*/\s*", "", s)
    s = re.sub(r"\b%d\b" % int(year), " ", s)
    s = re.sub(r"\s{2,}", " ", s).strip(" ,;/")
    vol = num = None
    m = re.search(r"\s(\d{1,4})\((\d{1,3})\)$", s)
    if m:
        vol, num = m.group(1), m.group(2)
        s = s[: m.start()].strip()
    else:
        # a trailing bare number is a volume, unless it is a year the venue states because the work
        # appeared there in a different year than the one in the year field.
        m = re.search(r"\s(?!(?:19|20|21)\d{2}$)(\d{1,4})$", s)
        if m:
            vol = m.group(1)
            s = s[: m.start()].strip()
    return s, vol, num


def primary_classes():
    """arXiv primary class per key, read off the side stamp in the parsed PDF where it survived
    the conversion ("arXiv:2502.09614v2 [cs.RO]"). Returns {key: (class, 'stamp'|'venue')}."""
    out = {}
    rx = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})v?\d*\s*\[?\s*([a-z-]+\.[A-Z]{2})")
    for key in [e["key"] for e in load_bib() if e["arxiv"]]:
        cls = None
        for p in (MD_DIR / f"{key}.md", MD_DIR / f"{key}.ocr.md"):
            if not p.exists():
                continue
            m = rx.search(p.read_text(errors="replace")[:200000])
            if m:
                cls = m.group(2)
                break
        if cls:
            out[key] = (cls, "stamp")
    return out


VISION_VENUES = ("CVPR", "ECCV", "ICCV", "3DV", "SIGGRAPH")


def default_class(entry):
    """The class to assume when the stamp did not survive the PDF conversion. A vision-conference
    paper is cs.CV, everything else in this corpus is cs.RO. This is an assumption, not a reading,
    and the run reports how many entries it covers."""
    return "cs.CV" if any(v in entry["venue"] for v in VISION_VENUES) else "cs.RO"


_BIB = None


def load_bib():
    global _BIB
    if _BIB is None:
        _BIB = json.loads(BIB_JSON.read_text())
    return _BIB


def source_note(entry, pages, papers):
    """The note for a source that is not a paper: what it is, where from, when fetched."""
    kind = PAGE_KINDS.get(entry["venue"])
    fallback = kind is None
    if fallback:
        kind = entry["venue"].strip().rstrip(".")
    bits = [kind[0].upper() + kind[1:]]
    urls = (pages.get(entry["key"]) or {}).get("urls") or []
    url = urls[0] if urls else (entry.get("pdf_url") or entry.get("github") or "")
    host = urlparse(url).netloc.replace("www.", "") if url else ""
    if host:
        bits.append(host)
    fetched = (pages.get(entry["key"]) or {}).get("fetched") or \
              (papers.get(entry["key"]) or {}).get("fetched")
    bits.append("fetched %s" % fetched if fetched else "no fetch date recorded")
    return ", ".join(bits), url, fallback


def build():
    bib = load_bib()
    pages = json.loads(PAGES_MANIFEST.read_text())
    papers = json.loads(PAPER_MANIFEST.read_text())
    stamped = primary_classes()

    unobtainable = {e["key"] for e in bib if "SOURCE UNAVAILABLE" in (e.get("why") or "")}
    unobtainable |= UNOBTAINABLE_EXTRA

    # Rows that record the fetched source as a stub but that are not in the unobtainable set:
    # printed rather than absorbed, so the disagreement between the corpus and METHOD.md is visible.
    thin = set()
    for p in sorted(ROWS_DIR.glob("*.json")):
        row = json.loads(p.read_text())
        if re.search(r"SOURCE (THIN|UNAVAILABLE)|no page body", row.get("note_gaps") or ""):
            thin.add(row["key"])

    entries, tally, report = [], Counter(), defaultdict(list)
    for e in sorted(bib, key=lambda x: x["key"]):
        key, arxiv = e["key"], e["arxiv"]
        expanded, used = expand_venue(e["venue"])
        fields = [("author", authors_field(e["authors"])),
                  ("title", "{%s}" % tex_escape(e["title"]))]
        notes = []

        if "LNCIS" in e["venue"] or re.search(r"\bbook chapter\b", e["venue"], re.I):
            etype = "incollection"
            report["outside the four rules"].append("%s (%s)" % (key, e["venue"]))
        else:
            etype = keyword_type(expanded)
            if etype and used:
                report["classified via an abbreviation"].append(
                    "%s (%s -> %s)" % (key, e["venue"], etype))
            if etype is None:
                if arxiv_only(e["venue"]):
                    etype = "preprint" if arxiv else None
                    if etype is None:
                        report["unclassified"].append("%s (venue %r, no arXiv id)"
                                                      % (key, e["venue"]))
                        etype = "misc"
                else:
                    etype = "page"

        if etype == "inproceedings":
            venue, vol, num = venue_field(e["venue"], e["year"])
            fields.append(("booktitle", tex_escape(venue)))
        elif etype == "article":
            venue, vol, num = venue_field(e["venue"], e["year"])
            fields.append(("journal", tex_escape(venue)))
            if vol:
                fields.append(("volume", vol))
            if num:
                fields.append(("number", num))
        elif etype == "incollection":
            venue, _, _ = venue_field(e["venue"], e["year"])
            fields.append(("booktitle", tex_escape(venue)))
            fields.append(("publisher", "Springer"))
        elif etype == "preprint":
            fields.append(("howpublished", "arXiv:%s" % arxiv))
        elif etype == "page":
            note, url, fallback = source_note(e, pages, papers)
            if fallback:
                report["source kind taken verbatim from the venue string"].append(
                    "%s (%r)" % (key, e["venue"]))
            if url:
                fields.append(("howpublished", r"\url{%s}" % url.rstrip(",")))
            notes.append(note)

        fields.append(("year", str(e["year"])))

        if arxiv:
            cls, how = stamped.get(key, (default_class(e), "venue"))
            report["primary class from the arXiv stamp" if how == "stamp"
                   else "primary class assumed from the venue"].append(key)
            fields += [("eprint", arxiv), ("archivePrefix", "arXiv"), ("primaryClass", cls)]

        if key in unobtainable:
            notes.insert(0, "Full text not obtained; cited by metadata only")
        if notes:
            fields.append(("note", tex_escape("; ".join(notes))))

        bibtype = "misc" if etype in ("preprint", "page", "misc") else etype
        tally[{"preprint": "misc (arXiv preprint)", "page": "misc (page, not a paper)",
               "misc": "misc (unclassified)"}.get(etype, "@" + etype)] += 1
        width = max(len(f) for f, _ in fields)
        body = ",\n".join("  %-*s = {%s}" % (width, f, v) for f, v in fields)
        entries.append("@%s{%s,\n%s\n}" % (bibtype, key, body))

    head = ["% tex/refs.bib -- generated by tools/make_bib.py from corpus/bib.json. Do not edit.",
            "% entries: " + str(len(entries)),
            "% command: python tools/make_bib.py",
            "% commit:  " + git_commit(),
            "% titles are double-braced so BibTeX keeps their capitalisation.",
            "% 'and others' in an author list is the corpus' 'et al.'.",
            "% a note on an entry says either what kind of source it is and when it was fetched,",
            "% or that the full text was never obtained and the work is cited by metadata only.",
            ""]
    OUT_BIB.parent.mkdir(parents=True, exist_ok=True)
    OUT_BIB.write_text("\n".join(head) + "\n\n".join(entries) + "\n")
    return tally, report, unobtainable, thin


def git_commit():
    try:
        return subprocess.run(["git", "-C", str(R), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, timeout=10).stdout.strip() or "?"
    except Exception:
        return "?"


PROBE = r"""%% tex/probe_bib.tex -- generated by tools/make_bib.py --probe
%% A compile probe for refs.bib: twenty entries across the seven topics and every entry type the
%% bibliography uses. Built with tools/build_tex.sh probe_bib. bibtex must report no warnings.
\documentclass[journal]{IEEEtran}
\usepackage{url}
\begin{document}
\title{Bibliography probe}
\author{tools/make\_bib.py}
\maketitle
%s
\bibliographystyle{IEEEtran}
\bibliography{refs}
\end{document}
"""


def write_probe():
    """Twenty entries, spread over the seven topics and chosen so that every entry type and the
    unobtainable notes are exercised."""
    bib = {e["key"]: e for e in load_bib()}
    text = OUT_BIB.read_text()
    types = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),", text):
        types[m.group(2)] = m.group(1)
    has_eprint = {m.group(1) for m in re.finditer(r"@\w+\{([^,]+),(?:[^@]*?)eprint", text)}

    def flavour(k):
        t = types.get(k, "?")
        if t == "misc":
            return "preprint" if k in has_eprint else "page"
        return t

    chosen = []
    # one of each flavour first, then round-robin over topics until twenty.
    for want in ("inproceedings", "article", "preprint", "page", "incollection"):
        for k in sorted(types):
            if flavour(k) == want and k not in chosen:
                chosen.append(k)
                break
    for k in sorted({"okamura_overview_2000", "raisim_2018", "dlr_hand_ii_2001",
                     "roa_suarez_grasp_quality_2015"}):
        if k in types and k not in chosen:
            chosen.append(k)
    by_topic = defaultdict(list)
    for k in sorted(types):
        by_topic[bib[k]["topic"]].append(k)
    topics = sorted(by_topic)
    i = 0
    while len(chosen) < 20:
        t = topics[i % len(topics)]
        pool = [k for k in by_topic[t] if k not in chosen]
        if pool:
            chosen.append(pool[(i // len(topics)) % len(pool)])
        i += 1
        if i > 500:
            break
    chosen = chosen[:20]
    lines = ["Twenty entries across the seven topics and every entry type this bibliography",
             "uses, cited so that bibtex has to resolve each one:"]
    for k in chosen:
        lines.append(r"\cite{%s} (%s, %s);" % (k, flavour(k), bib[k]["topic"]))
    lines[-1] = lines[-1][:-1] + "."
    OUT_PROBE.write_text(PROBE % "\n".join(lines))
    return chosen


def main():
    tally, report, unobtainable, thin = build()
    print("wrote %s" % OUT_BIB.relative_to(R))
    print("\nentries by type")
    for t, n in sorted(tally.items(), key=lambda x: -x[1]):
        print("  %-28s %3d" % (t, n))
    print("  %-28s %3d" % ("total", sum(tally.values())))

    print("\nfull text not obtained (note carried): %d" % len(unobtainable))
    for k in sorted(unobtainable):
        print("  %s" % k)
    extra = thin - unobtainable
    if extra:
        print("  a row records a stub source for these, but corpus/bib.json does not tag them and")
        print("  METHOD.md does not name them, so they carry no such note: %s" % ", ".join(sorted(extra)))

    for label in ("unclassified", "outside the four rules",
                  "classified via an abbreviation",
                  "source kind taken verbatim from the venue string"):
        items = report.get(label) or []
        print("\n%s: %d" % (label, len(items)))
        for it in items:
            print("  %s" % it)
    print("\narXiv primary class: %d read from the parsed PDF's stamp, %d assumed from the venue"
          % (len(report.get("primary class from the arXiv stamp") or []),
             len(report.get("primary class assumed from the venue") or [])))

    if "--probe" in sys.argv:
        chosen = write_probe()
        print("\nwrote %s citing %d entries" % (OUT_PROBE.relative_to(R), len(chosen)))


if __name__ == "__main__":
    main()
