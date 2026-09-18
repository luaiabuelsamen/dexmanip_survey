#!/usr/bin/env bash
# Build the LaTeX edition. Runs pdflatex, bibtex, pdflatex twice, and reports the first error.
# Takes an optional document name (without .tex); the default is main. `build_tex.sh probe` builds
# the bibliography probe written by tools/make_bib.py --probe.
set -u
cd "$(dirname "$0")/../tex" || exit 1
doc="${1:-main}"
export TEXINPUTS=.:./sty::
export BSTINPUTS=.:./sty::
export BIBINPUTS=.:./sty::
log() { printf '%s\n' "$*"; }
pdflatex -interaction=nonstopmode "$doc.tex" >/tmp/tex1.log 2>&1
bibtex "$doc" >/tmp/bib.log 2>&1
pdflatex -interaction=nonstopmode "$doc.tex" >/tmp/tex2.log 2>&1
pdflatex -interaction=nonstopmode "$doc.tex" >/tmp/tex3.log 2>&1
if [ -f "$doc.pdf" ]; then
  pages=$(pdfinfo "$doc.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
  log "$doc.pdf built${pages:+, $pages pages}"
else
  log "BUILD FAILED"
fi
log "--- errors:"; grep -E "^! " /tmp/tex3.log | head -12
log "--- bibtex warnings: $(grep -ci 'warning' /tmp/bib.log)"
grep -i 'warning' /tmp/bib.log | head -12
log "--- bibtex errors: $(grep -cE "^I couldn't|^Sorry|error message" /tmp/bib.log)"
log "--- undefined citations: $(grep -c 'Citation.*undefined' /tmp/tex3.log)"
grep -o 'Citation .[^ ]* undefined' /tmp/tex3.log | head -10
log "--- undefined references: $(grep -c 'Reference.*undefined' /tmp/tex3.log)"
log "--- overfull hboxes > 20pt: $(grep -cE 'Overfull \\\\hbox \([2-9][0-9]\.|Overfull \\\\hbox \([0-9]{3,}' /tmp/tex3.log)"
