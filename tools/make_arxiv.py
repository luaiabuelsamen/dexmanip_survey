#!/usr/bin/env python3
"""Assemble, lint and test-compile the arXiv submission package.

arXiv compiles from source, not from a PDF, and it compiles in a directory that contains
nothing but what was uploaded: no repository, no ``TEXINPUTS``, no ``bibtex`` run. This script
builds that directory and then proves it by compiling a copy of it outside the repository.

What the checks mean
--------------------
``portable``   Every path the document reads resolves inside the package, relative to the
               package root. A path that resolves only because the repository is on disk, or
               only because ``tools/build_tex.sh`` exported ``TEXINPUTS=.:./sty``, is a failure:
               arXiv exports neither.
``bibliography`` arXiv does not run bibtex. The reference list a reader sees comes from the
               uploaded ``.bbl`` alone, so the ``.bbl`` must exist, must be newer than the
               ``.bib`` it was made from, and must carry a ``\\bibitem`` for every key the
               sources cite. A missing ``.bbl`` does not error: the bibliography silently
               vanishes and every citation prints as a question mark.
``compile``    A copy of the package, in a scratch directory outside the repository, compiled
               with two ``pdflatex`` passes and no ``bibtex``, must produce the same page count
               as the repository's own build, a populated reference list, and no undefined
               citation. That is close to what arXiv's own toolchain does.

The reference page count is a fresh compile of the same sources, in the repository's own way
(``TEXINPUTS=.:./sty``), not the page count of the committed ``tex/main.pdf``. Those are the same
number only when nobody has edited a section since the last build, and the difference between
"the package is broken" and "the paper changed an hour ago" is worth keeping separate. The
committed PDF's page count is reported too, with whether it is stale.

Everything is read from a snapshot of ``tex/`` taken once at the start, so a package assembled
while somebody else is editing the tree is still internally consistent: the sources, the figures
and the reference build are all the same instant of the paper.

Usage
-----
    python tools/make_arxiv.py              # assemble, lint, and verify by compiling
    python tools/make_arxiv.py --no-verify  # assemble and lint only
    python tools/make_arxiv.py --out /tmp/pkg --scratch /tmp/scratch
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEX = REPO / "tex"

# arXiv's limit on a source package. It also warns above ~10 MB; we report both.
ARXIV_LIMIT_BYTES = 50 * 1024 * 1024
ARXIV_SOFT_BYTES = 10 * 1024 * 1024

# Raster and vector formats arXiv's AutoTeX accepts from a pdflatex submission.
GRAPHICS_OK = {".pdf", ".png", ".jpg", ".jpeg", ".eps", ".ps"}
GRAPHICS_BAD = {".gif", ".tif", ".tiff", ".bmp", ".svg", ".webp", ".psd"}

# Packages known to be in arXiv's TeX Live. The list is not a whitelist of everything arXiv
# has; it is what this document loads, checked one by one. Anything this document starts
# loading that is not here gets reported so a human looks it up rather than finding out at
# submission time.
ARXIV_TEXLIVE_KNOWN = {
    "amsmath", "amssymb", "array", "balance", "booktabs", "caption", "fontenc",
    "graphicx", "hyperref", "inputenc", "longtable", "microtype", "multirow",
    "subcaption", "tabularx", "tikz", "url", "xcolor",
}

# Packages that need a toolchain arXiv will not give a pdflatex submission.
PACKAGES_FORBIDDEN = {
    "fontspec": "XeLaTeX/LuaLaTeX only; pdflatex submissions cannot load it",
    "unicode-math": "XeLaTeX/LuaLaTeX only",
    "minted": "requires --shell-escape, which arXiv does not enable",
    "svg": "requires --shell-escape to call Inkscape",
    "epstopdf": "shells out to convert EPS; arXiv converts EPS itself",
    "pythontex": "requires --shell-escape",
    "gnuplottex": "requires --shell-escape",
    "bibentry": "interacts badly with a precompiled .bbl",
}

FONT_SUFFIXES = {".ttf", ".otf", ".pfb", ".pfa", ".tfm", ".vf", ".ttc"}

# Names never uploaded, whatever the dependency walk says. figs/extracted is 367 MB of raw
# figure regions rendered out of the source PDFs; the paper reproduces only what figs/selected holds.
EXCLUDE_DIRS = {"extracted"}
EXCLUDE_GLOBS = ("probe*", "*.aux", "*.log", "*.blg", "*.out", "*.fls",
                 "*.fdb_latexmk", "*.synctex.gz", "*.toc", "*.lof", "*.lot")

SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
          "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
          "eighteen", "nineteen", "twenty")


def num(n: int) -> str:
    """Spell small counts, so a generated sentence does not read "The 1 reproduced plate"."""
    return _WORDS[n] if 0 <= n < len(_WORDS) else str(n)


def strip_comments(text: str) -> str:
    """Drop TeX comments so a commented-out \\input is not mistaken for a dependency."""
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


class Package:
    def __init__(self, root: Path = TEX, main: str = "main.tex"):
        self.root = root
        self.main = main
        self.tex_files: list[str] = []       # relative to root, in discovery order
        self.graphics: dict[str, str] = {}   # relative path -> file that referenced it
        self.problems: list[str] = []        # hard failures
        self.notes: list[str] = []           # things a human should read
        self.fixes: list[str] = []           # what this script changed to make it portable
        self.cite_keys: set[str] = set()
        self.packages: set[str] = set()
        self.bbl_items = 0

    # -- dependency walk ---------------------------------------------------------------

    def _resolve_tex(self, target: str) -> str | None:
        for cand in (target, target + ".tex"):
            if (self.root / cand).is_file():
                return cand
        return None

    def _resolve_graphic(self, target: str) -> str | None:
        p = self.root / target
        if p.is_file():
            return target
        for ext in (".pdf", ".png", ".jpg", ".jpeg", ".eps"):
            if (self.root / (target + ext)).is_file():
                return target + ext
        return None

    def walk(self) -> None:
        seen: set[str] = set()

        def visit(rel: str) -> None:
            if rel in seen:
                return
            seen.add(rel)
            self.tex_files.append(rel)
            raw = (self.root / rel).read_text(encoding="utf-8", errors="replace")
            body = strip_comments(raw)

            if "\\write18" in body or "\\immediate\\write18" in body:
                self.problems.append(f"{rel}: uses \\write18 (shell escape); arXiv forbids it")

            for m in re.finditer(r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", body):
                for name in m.group(1).split(","):
                    name = name.strip()
                    if name:
                        self.packages.add(name)

            for m in re.finditer(r"\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", body):
                for key in m.group(1).split(","):
                    key = key.strip()
                    if key:
                        self.cite_keys.add(key)

            # \IfFileExists{f}{...} guards a generated table; the tested file is a dependency
            # even though the \input inside the true branch is usually picked up anyway.
            for m in re.finditer(r"\\IfFileExists\s*\{([^}]*)\}", body):
                got = self._resolve_tex(m.group(1).strip())
                if got:
                    visit(got)

            for m in re.finditer(r"\\(?:input|include)\s*\{([^}]*)\}", body):
                target = m.group(1).strip()
                if target.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", target):
                    self.problems.append(f"{rel}: absolute path in \\input: {target}")
                    continue
                got = self._resolve_tex(target)
                if got:
                    visit(got)
                else:
                    self.problems.append(f"{rel}: \\input{{{target}}} does not resolve")

            for m in re.finditer(
                r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", body
            ):
                target = m.group(1).strip()
                if target.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", target):
                    self.problems.append(
                        f"{rel}: absolute path in \\includegraphics: {target}"
                    )
                    continue
                got = self._resolve_graphic(target)
                if got:
                    self.graphics[got] = rel
                else:
                    self.problems.append(
                        f"{rel}: \\includegraphics{{{target}}} does not resolve"
                    )

        visit(self.main)

    # -- assembly ----------------------------------------------------------------------

    def assemble(self, out: Path) -> list[str]:
        """Copy the package into `out` and return its file list, relative, sorted."""
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)

        def put(src: Path, rel: str) -> None:
            dst = out / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        for rel in self.tex_files:
            self._check_name(rel)
            put(self.root / rel, rel)
        for rel in self.graphics:
            self._check_name(rel)
            suffix = Path(rel).suffix.lower()
            if suffix in GRAPHICS_BAD:
                self.problems.append(
                    f"{rel}: arXiv will not accept {suffix}; convert to PDF or PNG"
                )
            elif suffix not in GRAPHICS_OK:
                self.notes.append(f"{rel}: unusual graphics extension {suffix}; check arXiv takes it")
            put(self.root / rel, rel)

        # The vendored class and style, twice. sty/ is where the repository keeps them and
        # where tools/build_tex.sh looks (it exports TEXINPUTS=.:./sty). arXiv exports no
        # TEXINPUTS, and kpathsea's default `.` is not recursive, so a class that exists only
        # in sty/ is not found and the build dies on line 4 of main.tex. The copy at the
        # package root is the one TeX actually reads, and because `.` precedes the system tree
        # it also pins the class version: the pagination cannot drift onto whatever IEEEtran
        # arXiv's TeX Live happens to ship.
        for name in ("IEEEtran.cls", "IEEEtran.bst"):
            src = self.root / "sty" / name
            if not src.is_file():
                self.problems.append(f"sty/{name} missing from the repository; cannot vendor it")
                continue
            put(src, f"sty/{name}")
            put(src, name)
            self.fixes.append(
                f"copied sty/{name} to the package root, because arXiv sets no TEXINPUTS "
                f"and TeX does not search subdirectories"
            )

        bbl = self.root / "main.bbl"
        if bbl.is_file():
            put(bbl, "main.bbl")
        else:
            self.problems.append("main.bbl missing; run tools/build_tex.sh first")

        bib = self.root / "refs.bib"
        if bib.is_file():
            put(bib, "refs.bib")
        else:
            self.notes.append("refs.bib missing; arXiv does not need it, but the source should carry it")

        files = sorted(
            str(p.relative_to(out)) for p in out.rglob("*") if p.is_file()
        )
        return files

    def _check_name(self, rel: str) -> None:
        for part in Path(rel).parts:
            if not SAFE_NAME.match(part):
                self.problems.append(
                    f"{rel}: path component {part!r} has a space or an unusual character; "
                    f"arXiv's unpacking and TeX's own parser both choke on these"
                )

    # -- lint --------------------------------------------------------------------------

    def lint(self, out: Path, files: list[str]) -> None:
        for name in sorted(self.packages):
            if name in PACKAGES_FORBIDDEN:
                self.problems.append(f"\\usepackage{{{name}}}: {PACKAGES_FORBIDDEN[name]}")
            elif name not in ARXIV_TEXLIVE_KNOWN:
                self.notes.append(
                    f"\\usepackage{{{name}}} is not on this script's checked list; "
                    f"confirm it is in arXiv's TeX Live or vendor the .sty"
                )

        for rel in files:
            if Path(rel).suffix.lower() in FONT_SUFFIXES:
                self.problems.append(f"{rel}: font file in the package; arXiv rejects these")

        for bad in EXCLUDE_DIRS:
            if (out / "figs" / bad).exists():
                self.problems.append(f"figs/{bad} leaked into the package")
        for rel in files:
            base = Path(rel).name
            for pat in EXCLUDE_GLOBS:
                if Path(base).match(pat):
                    self.problems.append(f"{rel}: excluded by pattern {pat} but present")

        # Exactly one top-level \documentclass, so arXiv's AutoTeX cannot pick the wrong file.
        roots = [
            rel for rel in files
            if rel.endswith(".tex")
            and "\\documentclass" in strip_comments((out / rel).read_text(
                encoding="utf-8", errors="replace"))
        ]
        if roots != [self.main]:
            self.problems.append(
                f"expected {self.main} to be the only file with \\documentclass, found {roots}"
            )

        # The bibliography arXiv will show is the .bbl and nothing else.
        bbl_path = out / "main.bbl"
        if bbl_path.is_file():
            bbl = bbl_path.read_text(encoding="utf-8", errors="replace")
            if "\\begin{thebibliography}" not in bbl:
                self.problems.append("main.bbl has no thebibliography environment")
            items = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", bbl))
            missing = sorted(self.cite_keys - items)
            if missing:
                self.problems.append(
                    f"{len(missing)} cited keys have no \\bibitem in main.bbl: "
                    f"{', '.join(missing[:8])}"
                )
            bib_path = self.root / "refs.bib"
            if bib_path.is_file() and bib_path.stat().st_mtime > (self.root / "main.bbl").stat().st_mtime:
                self.problems.append(
                    "refs.bib is newer than main.bbl; the .bbl is stale, rerun tools/build_tex.sh"
                )
            self.bbl_items = len(items)
            self.notes.append(f"main.bbl carries {len(items)} \\bibitem entries for "
                              f"{len(self.cite_keys)} cited keys")

        total = sum((out / f).stat().st_size for f in files)
        if total > ARXIV_LIMIT_BYTES:
            self.problems.append(f"package is {total/1e6:.1f} MB, over arXiv's 50 MB limit")
        elif total > ARXIV_SOFT_BYTES:
            self.notes.append(f"package is {total/1e6:.1f} MB; arXiv asks about anything over 10 MB")


# -- the test that matters ------------------------------------------------------------------

SNAPSHOT_IGNORE = shutil.ignore_patterns(
    "extracted", "probe*", "_probe*", "tables_probe*", "__pycache__",
    "*.aux", "*.log", "*.blg", "*.out", "*.fls", "*.fdb_latexmk", "*.synctex.gz", "*.pdf",
)


def snapshot_tex(scratch_root: Path) -> Path:
    """Copy tex/ once, minus the 367 MB figure catalogue and every build by-product.

    Taken so that the package, its lint and the reference build all describe one instant of a
    tree that another process may be editing.
    """
    scratch_root.mkdir(parents=True, exist_ok=True)
    dst = scratch_root / "tex_snapshot"
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(TEX, dst, ignore=SNAPSHOT_IGNORE)
    bbl = TEX / "main.bbl"
    if bbl.is_file():
        shutil.copy2(bbl, dst / "main.bbl")
    return dst


def pdf_pages(pdf: Path) -> int | None:
    if not pdf.is_file():
        return None
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"(?m)^Pages:\s+(\d+)", info.stdout)
    return int(m.group(1)) if m else None


def _compile(tree: Path, texinputs: str | None) -> dict:
    """Two pdflatex passes, no bibtex, shell escape off. Returns what the log and PDF say."""
    env = {k: v for k, v in os.environ.items()
           if k not in ("TEXINPUTS", "BIBINPUTS", "BSTINPUTS", "TEXMFHOME", "TEXMFVAR")}
    if texinputs:
        env["TEXINPUTS"] = texinputs
        env["BSTINPUTS"] = texinputs
    env["TEXMFOUTPUT"] = str(tree)
    passes = []
    for _ in (1, 2):
        proc = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-no-shell-escape", "main.tex"],
            cwd=tree, env=env, capture_output=True, text=True, timeout=900,
        )
        passes.append(proc.returncode)
    logf = tree / "main.log"
    log = logf.read_text(encoding="utf-8", errors="replace") if logf.is_file() else ""
    pdf = tree / "main.pdf"
    out = {
        "dir": str(tree),
        "passes": passes,
        "pdf": pdf.is_file(),
        "pages": pdf_pages(pdf),
        "undefined_citations": len(re.findall(r"Citation `[^']*' (?:on page [^ ]+ )?undefined", log)),
        "undefined_references": len(re.findall(r"Reference `[^']*' (?:on page [^ ]+ )?undefined", log)),
        "errors": re.findall(r"(?m)^! .*$", log)[:10],
        "rerun_wanted": "Rerun to get cross-references right" in log,
        "shell_escape": "runsystem" in log,
        "class_read": "sty/IEEEtran.cls" if "(sty/IEEEtran.cls" in log
                      else ("./IEEEtran.cls" if "(./IEEEtran.cls" in log else "system or none"),
        "bibliography_entries": 0,
        "bibliography_heading_found": False,
        "bibliography_contiguous": False,
        "text": "",
    }
    if pdf.is_file():
        txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        out["text"] = txt
        # A populated bibliography, measured where a reader sees it: the numbered entries printed
        # after the reference-list heading, not every bracketed number in the document. IEEEtran
        # sets that heading in letterspaced small caps, so pdftotext extracts it as "R EFERENCES"
        # and a plain "REFERENCES" test never matches; the first version of this check silently
        # fell back to the whole document and counted every inline citation instead. It happened
        # to return the right number, which is how a bug like that survives. The count is checked
        # against the .bbl's own \bibitem count in lint(), and against 1..N being contiguous here.
        heads = list(re.finditer(r"(?mi)^\s*R\s*EFERENCES\s*$", txt))
        if not heads:
            out["bibliography_heading_found"] = False
        else:
            out["bibliography_heading_found"] = True
            tail = txt[heads[-1].end():]
            nums = [int(m.group(1)) for m in re.finditer(r"(?m)^\[(\d{1,4})\]", tail)]
            out["bibliography_entries"] = len(set(nums))
            out["bibliography_contiguous"] = bool(nums) and sorted(set(nums)) == list(
                range(1, max(nums) + 1))
    return out


def verify(out: Path, snapshot: Path, scratch_root: Path) -> dict:
    """Compile the package outside the repository, and the same sources the repository's way.

    The package build gets no TEXINPUTS and no repository: that is arXiv. The reference build
    gets the repository's own ``TEXINPUTS=.:./sty`` and the whole snapshot around it. Equal page
    counts and identical extracted text mean the package is the paper, not a subset of it.
    """
    work = Path(tempfile.mkdtemp(prefix="arxiv_verify_", dir=scratch_root))
    tree = work / "package"
    shutil.copytree(out, tree)
    pkg = _compile(tree, texinputs=None)
    ref = _compile(snapshot, texinputs=".:./sty:")
    pkg["reference_pages"] = ref["pages"]
    pkg["reference_errors"] = len(ref["errors"])
    pkg["reference_bibliography_entries"] = ref["bibliography_entries"]
    pkg["text_matches_reference"] = bool(pkg["text"]) and pkg["text"] == ref["text"]
    pkg["committed_pdf_pages"] = pdf_pages(TEX / "main.pdf")
    return pkg


# -- the two documents the submission form and the last five minutes need -------------------


def plain_abstract(path: Path) -> str:
    """The abstract as arXiv's form takes it: no LaTeX, no comments, one paragraph."""
    text = strip_comments(path.read_text(encoding="utf-8"))
    text = re.sub(r"\\(?:emph|textit|textbf|texttt|text|key|path)\{([^}]*)\}", r"\1", text)
    text = re.sub(r"~\\ref\{[^}]*\}", "", text)
    text = re.sub(r"\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\{[^}]*\}", "", text)
    text = text.replace("~", " ").replace("\\%", "%").replace("\\&", "&")
    text = text.replace("\\,", " ").replace("\\ ", " ").replace("--", "-")
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    text = re.sub(r"[{}]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def write_submission(out: Path, pkg: Package, build_files: int, build_size: int,
                     total_files: int, total_size: int,
                     pages: int | None, bib_entries: int,
                     n_figs: int, n_plates: int) -> str:
    abstract = plain_abstract(pkg.root / "sections" / "abstract.tex")
    title = ("Dexterous Manipulation, Single-Hand and Bimanual: "
             "Machines, Simulators, and How Policies Are Trained")
    today = _dt.date.today().isoformat()
    body = f"""# arXiv submission metadata

Generated by `tools/make_arxiv.py` on {today}. Every field below is what to paste into the
corresponding box on arXiv's submission form. Copy, do not retype.

## Title

{title}

## Authors

Luai Abuelsamen

## Abstract

arXiv's abstract box takes plain text: no LaTeX commands, no math mode, no citation keys. This
is the paper's abstract with the markup removed, {len(abstract)} characters, against arXiv's
1920-character limit. It says the same thing as `tex/sections/abstract.tex`; if that file
changes, regenerate this one rather than editing it here, because a form abstract that has
drifted from the paper's is the single most common thing a reader notices and an author cannot
fix without replacing the submission.

{abstract}

## Primary category

cs.RO (Robotics)

That is the right primary. The paper is a robotics survey: hands, simulators, and the training
of manipulation policies. Its audit method is the contribution, but its audience reads cs.RO.

## Cross-lists

- cs.LG (Machine Learning) -- the survey's largest section is how policies are trained, and the
  reward-function audit is a claim about learning code, not about hardware.
- cs.AI (Artificial Intelligence) -- broad but conventional for a learning-heavy robotics survey,
  and it is where readers who follow embodied-agent work look.

Two cross-lists is the usual ceiling; a third reads as fishing and moderators sometimes strip it.
cs.CV is deliberately not requested: the paper discusses visual observation but contributes
nothing to vision.

## Comments field

{pages} pages, {bib_entries} references. Survey with an audit component; the corpus of
structured rows, extraction notes and parsed repositories that every count is computed from is
public and will be deposited with a DOI.

(If the Zenodo deposit has a DOI by the time you submit, put it in this field as well as in the
paper: `Corpus and build: doi:10.5281/zenodo.XXXXXXX`. If it does not yet, leave that sentence
as a promise and do not invent a number.)

## Licence

CC BY 4.0 (Creative Commons Attribution 4.0 International).

**This choice is irreversible.** The licence is attached to the version at the moment it is
announced, and arXiv does not change the licence on an announced version -- not on request and
not by replacing the paper. A later version can be submitted under a different licence, but v1
keeps this one, permanently and publicly. Read the selector at the form rather than clicking
through it; the default it lands on is arXiv's own non-exclusive licence to distribute, not this.

It is the deliberate choice here for two reasons. The survey argues that claims should be
checkable against reusable artefacts, and a preprint under arXiv's default licence cannot itself
be redistributed or built on -- which would leave the paper's own argument resting on a
restriction it asks others not to impose. And the paper depends on other people having made this
choice: `figs/selected/bimanual_grasp_penetration.png` is in the paper only because its authors
released it CC BY 4.0, and it carries the attribution that licence asks for. It is the only plate
left: the two that would have rested on an author's permission were redrawn or dropped, because
this paper is posted without asking anyone for anything, and `tex/PERMISSIONS.md` records the
position each closed at. Taking reuse and then withholding it is not a position this paper can
hold.

## Files in this package

{build_files} files the build reads, {build_size/1e6:.2f} MB. With `SUBMISSION.md`,
`CHECKLIST.md` and `MANIFEST.txt`, {total_files} files and {total_size/1e6:.2f} MB, against
arXiv's 50 MB limit -- about {ARXIV_LIMIT_BYTES/total_size:.0f} times the headroom needed.

The package is self-contained: it compiles with `pdflatex main.tex` twice and no `bibtex`, in a
directory with no repository around it and no `TEXINPUTS` set. That is what arXiv does.

- `main.tex` -- the only file with a `\\documentclass`, so AutoTeX cannot pick the wrong root.
- `preamble.tex`, `sections/`, `tables/`, `figs/*.tex` -- the document: {num(n_figs)} numbered
  figures, of which {num(n_figs - n_plates)} are TikZ the document draws itself.
- `figs/selected/` -- every bitmap the paper reproduces, and there
  {'is only one' if n_plates == 1 else f'are {num(n_plates)}'}:
  {', '.join(sorted(pkg.graphics)) or 'none'}.
- `IEEEtran.cls`, `IEEEtran.bst` at the package root **and** in `sty/`. The root copies are the
  ones TeX finds: arXiv sets no `TEXINPUTS`, and kpathsea's default `.` is not recursive, so a
  class present only in `sty/` is not found and the build dies at `\\documentclass`. The `sty/`
  copies keep the repository's own layout and build script working inside the package. Vendoring
  the class rather than trusting arXiv's TeX Live also pins the version, so the pagination
  cannot shift under the paper.
- `main.bbl` -- **the bibliography**. arXiv does not run bibtex. Without this file the reference
  list does not error, it silently disappears and every citation renders as a question mark.
- `refs.bib` -- not needed to compile; included so the source is complete and the `.bbl` can be
  regenerated by anyone who downloads it.

Not in the package, deliberately: `tex/figs/extracted/` (367 MB of raw figure regions rendered
out of the source PDFs, none of it referenced), the probe documents `probe45.tex`,
`probe_bib.tex`, `probe_s89_appendices.tex`, `tables_probe.tex` and their output, every build
by-product (`.aux`, `.log`, `.blg`, `.out`), and `tex/main.pdf`.

`SUBMISSION.md`, `CHECKLIST.md` and `MANIFEST.txt` are metadata for the person submitting. arXiv
ignores files it does not recognise as TeX, so leaving them in is harmless, and they travel with
the source others can download. Delete them before upload if you would rather they did not.

## Things worth knowing before you paste

- The second `pdflatex` pass still prints "Label(s) may have changed. Rerun to get
  cross-references right." A third pass clears the warning and changes nothing: same {pages}
  pages, and the extracted text of the two PDFs is identical. arXiv iterates until the build is
  stable, so this is not a problem; it is recorded here so nobody reads the warning in arXiv's
  log and replaces a correct submission over it.
- The running head prints `Survey draft, \\today`, so it will carry arXiv's compile date. That is
  cosmetic, but if the word "draft" should not appear on a posted preprint, change
  `\\markboth` in `main.tex` before you build the package.
- No `00README.XXX` is included. It would let you name the top-level file explicitly, but
  `main.tex` is already the only candidate, and a malformed directive file is a way to fail a
  submission for no gain.
- The paper says the archived release "will carry a DOI"
  (`sections/appendix_a_method.tex`). If the Zenodo deposit exists at submission time, cite it;
  if it does not, that sentence is still true and needs no edit.
"""
    (out / "SUBMISSION.md").write_text(body, encoding="utf-8")
    return abstract


def write_checklist(out: Path, pages: int | None, bib_entries: int,
                    n_figs: int, n_plates: int, plate_names: list[str]) -> None:
    names = ", ".join(Path(p).name for p in plate_names)
    if n_plates == 1:
        plate_phrase = f"one bitmap plate, `{names}`"
        plate_list = f"the one bitmap the paper reproduces, `{names}`"
    elif n_plates:
        plate_phrase = f"{num(n_plates)} bitmap plates ({names})"
        plate_list = f"the {num(n_plates)} bitmaps the paper reproduces: {names}"
    else:
        plate_phrase = "no bitmaps at all"
        plate_list = "nothing, because the paper reproduces no bitmap"
    body = f"""# Five minutes before you click submit

In order. Each one is a way a submission has actually gone wrong, not a way one could in
principle. Work down the list against the package in this directory and the form on screen.

1. **`main.bbl` is present and current.** Rebuild the package first --
   `python tools/make_arxiv.py` -- because the only package worth checking is one assembled from
   the sources you are about to submit, and it takes a minute. Then open `main.bbl`: it must
   contain `\\begin{{thebibliography}}` and {bib_entries} `\\bibitem` lines. arXiv does not
   run bibtex. A package without a `.bbl` compiles cleanly and posts with no reference list at all
   and every citation printed as `[?]`, and the first thing anyone will notice is that the
   survey cites nothing. If `refs.bib` has been touched since the `.bbl` was written, the `.bbl`
   is stale: rerun `tools/build_tex.sh` and rebuild this package.

2. **The abstract in the form matches the abstract in the paper.** Paste from the "Abstract"
   section of `SUBMISSION.md`, which was generated from `tex/sections/abstract.tex`. Do not
   retype and do not tighten it in the box. The listing abstract and the PDF abstract are read
   side by side, they are what search indexes, and a mismatch cannot be fixed without
   submitting a new version.

3. **The licence selector says CC BY 4.0.** Not "arXiv's non-exclusive licence to distribute",
   which is the default the form lands on if you click through. This is irreversible: arXiv will
   not downgrade or change a licence after announcement. Read the radio button, then read it
   again.

4. **The corpus DOI is cited, if it exists yet.** If the Zenodo deposit is live, its DOI belongs
   in the comments field and in the paper (`sections/appendix_a_method.tex` promises it). If it
   is not live, leave the promise and do not paste a DOI that resolves to a draft: a dead DOI in
   a survey about checkable artefacts is worse than no DOI.

5. **Every figure renders in arXiv's preview.** Open the generated PDF arXiv shows you before
   announcement and look at all {pages} pages, not the first two. The paper has {num(n_figs)}
   numbered figures: {num(n_figs - n_plates)} TikZ diagrams the document draws itself, and
   {plate_phrase}. A missing bitmap shows as a grey box or an empty float, and TikZ that hit a
   version difference shows as a diagram with its labels piled at the origin. Check Figure 1 in
   particular: it is the map of the paper and the widest float in it.

6. **The page count matches.** arXiv's build should give {pages} pages, which is what a fresh
   compile of these sources gives here. Compare against a current `tools/build_tex.sh`, not
   against whatever `tex/main.pdf` happens to hold: that file is only as new as the last build. A
   different number from arXiv means it resolved a different class or package version than the
   vendored one, and the layout has moved under you. Check the reference list and the full-width
   floats before accepting it.

7. **Every reproduced plate still has the permission it claims.** `tex/PERMISSIONS.md` is the
   register. Check it against {plate_list}. Posting is publishing, and a plate whose permission
   email has not come back is not cleared by the deadline arriving. No email is outstanding: every
   plate that needed one has already taken the fallback, redrawn in the paper's own style or
   dropped, because the prose usually made the point anyway.

8. **The primary category is cs.RO** and the cross-lists are the two in `SUBMISSION.md`. A
   primary set to cs.LG on a robotics survey gets it read by the wrong people, and moderators
   reclassify slowly.

9. **You are submitting the source, not the PDF.** The upload is this directory's contents.
   If arXiv shows one file and offers to post it as-is, you uploaded `main.pdf` by mistake and
   the source-based build everything above assumes is not what will be compiled.

10. **`IEEEtran.cls` is at the top level of the upload, not only in `sty/`.** It is there in both
    places and must stay that way. arXiv sets no `TEXINPUTS`, and TeX does not search
    subdirectories, so a package carrying the class only in `sty/` fails at `\\documentclass` with
    "File `IEEEtran.cls' not found" and produces no PDF at all. Tested: removing the top-level
    copy from this package kills the build outright.
"""
    (out / "CHECKLIST.md").write_text(body, encoding="utf-8")


def provenance() -> dict:
    """Commit, working-tree state and command line, so a package can be tied to a source state."""
    def git(*args: str) -> str:
        try:
            return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                                  text=True, timeout=60).stdout.strip()
        except Exception:
            return ""
    dirty = [l for l in git("status", "--porcelain").splitlines() if l.strip()]
    return {
        "commit": git("rev-parse", "HEAD"),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "dirty_paths": len(dirty),
        "command": "python " + " ".join([os.path.relpath(sys.argv[0], REPO), *sys.argv[1:]]),
        "built_at": _dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }


def write_manifest(out: Path, files: list[str], size: int, prov: dict) -> None:
    lines = [
        "# arXiv package manifest",
        f"# {len(files)} files, {size} bytes ({size/1e6:.2f} MB)",
        f"# built by {prov['command']} at {prov['built_at']}",
        f"# from commit {prov['commit'][:12] or 'unknown'} on {prov['branch'] or '?'}"
        + (f", working tree dirty in {prov['dirty_paths']} paths" if prov["dirty_paths"] else ", clean"),
        "# sizes in bytes; dist/arxiv_build.json carries a sha256 for each of these",
        "",
    ]
    for rel in files:
        lines.append(f"{(out / rel).stat().st_size:>9}  {rel}")
    (out / "MANIFEST.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(REPO / "dist" / "arxiv"),
                    help="package directory to write (default dist/arxiv)")
    ap.add_argument("--scratch", default=None,
                    help="directory outside the repository for the verification compile")
    ap.add_argument("--no-verify", action="store_true",
                    help="assemble and lint, but do not compile a copy")
    ap.add_argument("--keep-scratch", action="store_true",
                    help="leave the verification compile directory in place")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    if out.is_relative_to(TEX):
        print("refusing to write the package inside tex/", file=sys.stderr)
        return 2

    scratch = Path(args.scratch) if args.scratch else Path(
        tempfile.gettempdir()) / "arxiv_verify"
    if scratch.resolve().is_relative_to(REPO):
        print("the scratch directory must be outside the repository", file=sys.stderr)
        return 2

    snapshot = snapshot_tex(scratch)
    pkg = Package(root=snapshot)
    pkg.walk()
    files = pkg.assemble(out)
    pkg.lint(out, files)
    size = sum((out / f).stat().st_size for f in files)

    # tex/main.pdf is the committed build. If a source is newer than it, it is not the paper this
    # package contains, and its page count is not the number to check against.
    committed = TEX / "main.pdf"
    if committed.is_file():
        newer = [rel for rel in pkg.tex_files + list(pkg.graphics)
                 if (TEX / rel).is_file()
                 and (TEX / rel).stat().st_mtime > committed.stat().st_mtime]
        if newer:
            pkg.notes.append(
                f"tex/main.pdf is stale: {len(newer)} packaged source"
                f"{'' if len(newer) == 1 else 's'} newer than it "
                f"({', '.join(sorted(newer)[:4])}{'...' if len(newer) > 4 else ''}). The page "
                f"count checked below is a fresh build of these sources, not that PDF's. "
                f"Rerun tools/build_tex.sh before quoting a page count anywhere."
            )

    bbl_items = pkg.bbl_items
    result = None
    if not args.no_verify:
        result = verify(out, snapshot, scratch)

    pages = result["pages"] if result else pdf_pages(committed)
    bib_entries = result["bibliography_entries"] if result else len(pkg.cite_keys)

    # The three metadata files report the package's own file count and size, which they change by
    # existing. Write, remeasure, rewrite, until the listing stops moving; it takes two or three
    # rounds. Without the loop the counts in SUBMISSION.md are the counts from before it existed.
    prov = provenance()
    fig_labels = set()
    for rel in pkg.tex_files:
        fig_labels |= set(re.findall(
            r"\\label\{(fig:[^}]*)\}",
            strip_comments((out / rel).read_text(encoding="utf-8", errors="replace"))))
    n_figs, n_plates = len(fig_labels), len(pkg.graphics)
    plate_names = sorted(pkg.graphics)

    build_files, build_size = len(files), size
    listing: list[tuple[str, int]] = []
    for _ in range(6):
        total = sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file())
        total_size = sum((out / f).stat().st_size for f in total)
        write_submission(out, pkg, build_files, build_size, len(total), total_size,
                         pages, bib_entries, n_figs, n_plates)
        write_checklist(out, pages, bib_entries, n_figs, n_plates, plate_names)
        write_manifest(out, total, total_size, prov)
        now = sorted((f, (out / f).stat().st_size)
                     for f in (str(p.relative_to(out)) for p in out.rglob("*") if p.is_file()))
        if now == listing:
            break
        listing = now
    else:
        pkg.notes.append("the metadata files' own size/count figures did not settle; "
                         "SUBMISSION.md may be a few bytes out")

    files = [f for f, _ in listing]
    size = sum(s for _, s in listing)

    # The record: what was built, from what, and what the compile test found. Written beside the
    # package rather than inside it, because it is provenance and not part of the paper.
    record = {
        "provenance": prov,
        "package": str(out),
        "files": len(files),
        "build_files": build_files,
        "bytes": size,
        "arxiv_limit_bytes": ARXIV_LIMIT_BYTES,
        "pages": pages,
        "bibliography_entries": bib_entries,
        "figures": n_figs,
        "bitmap_plates": plate_names,
        "sha256": {rel: _sha256(out / rel) for rel in files},
        "verification": {k: v for k, v in (result or {}).items() if k != "text"},
        "problems": pkg.problems,
        "notes": pkg.notes,
        "portability_fixes": sorted(set(pkg.fixes)),
    }
    (out.parent / "arxiv_build.json").write_text(
        json.dumps(record, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    print(f"package      {out}")
    print(f"files        {len(files)}  ({build_files} the build reads, "
          f"{len(files) - build_files} metadata)")
    print(f"size         {size} bytes ({size/1e6:.2f} MB), arXiv limit 50 MB "
          f"-- {ARXIV_LIMIT_BYTES/size:.0f}x headroom")
    print(f"tex sources  {len(pkg.tex_files)}   graphics {len(pkg.graphics)}   "
          f"cited keys {len(pkg.cite_keys)}")

    if result:
        ok = (result["pdf"] and result["pages"] == result["reference_pages"]
              and result["undefined_citations"] == 0
              and result["bibliography_heading_found"]
              and result["bibliography_contiguous"]
              and result["bibliography_entries"] == bbl_items
              and result["text_matches_reference"] and not result["errors"])
        print(f"\nscratch compile in {result['dir']}")
        print(f"  two pdflatex passes, no bibtex, no TEXINPUTS, outside the repository")
        print(f"  pdf produced            {result['pdf']}")
        print(f"  pages                   {result['pages']}  "
              f"(fresh reference build of the same sources: {result['reference_pages']}; "
              f"committed tex/main.pdf: {result['committed_pdf_pages']})")
        print(f"  text identical to ref   {result['text_matches_reference']}")
        print(f"  bibliography entries    {result['bibliography_entries']} rendered after the "
              f"reference heading, numbered 1..N contiguously: "
              f"{result['bibliography_contiguous']}; main.bbl has {bbl_items} \\bibitem")
        print(f"  undefined citations     {result['undefined_citations']}")
        print(f"  undefined references    {result['undefined_references']}")
        print(f"  IEEEtran.cls read from  {result['class_read']}")
        print(f"  rerun still requested   {result['rerun_wanted']}  "
              f"(a third pass changes nothing; arXiv iterates to stable)")
        print(f"  shell escape used       {result['shell_escape']}")
        print(f"  latex errors            {len(result['errors'])}")
        for e in result["errors"]:
            print(f"    {e}")
        print(f"  VERDICT                 {'PASS' if ok else 'FAIL'}")
        if not args.keep_scratch:
            shutil.rmtree(Path(result["dir"]).parent, ignore_errors=True)

    if pkg.fixes:
        print("\nmade portable by:")
        for f in sorted(set(pkg.fixes)):
            print(f"  - {f}")
    if pkg.notes:
        print("\nnotes:")
        for n in pkg.notes:
            print(f"  - {n}")
    if pkg.problems:
        print("\nPROBLEMS:")
        for p in pkg.problems:
            print(f"  - {p}")
        return 1
    print("\nchecks clean: no absolute paths, no odd filenames, no forbidden package, no font "
          "file, no shell escape, one \\documentclass, bbl covers every cited key, "
          "figs/extracted excluded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
