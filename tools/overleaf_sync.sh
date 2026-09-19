#!/usr/bin/env bash
# Sync the LaTeX edition with the Overleaf project.
#
# Overleaf's layout is not the repository's layout. tools/make_arxiv.py flattens
# tex/ to the project root and copies sty/IEEEtran.{cls,bst} up to the root,
# because Overleaf, like arXiv, sets no TEXINPUTS and TeX does not search
# subdirectories. So Overleaf/<path> maps to tex/<path>, with two exceptions
# that this script filters: the root IEEEtran.{cls,bst}, whose real home is
# tex/sty/, and main.bbl, which is generated from refs.bib.
#
#   push    rebuild the verified package and send it to Overleaf
#   pull    bring Overleaf's edits back into tex/
#   status  show whether the two have diverged
#
# Credentials are read from the same file the Overleaf MCP server uses.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MIRROR="$REPO/.overleaf-mirror"
BUILD="$REPO/.overleaf-build"   # make_arxiv.py writes arxiv_build.json beside --out
CONF="${OVERLEAF_PROJECTS_CONFIG:-$HOME/.config/overleaf-mcp/projects.json}"
PROJECT="${1:-}"; shift || true

read_conf() {
  python3 - "$CONF" "$1" <<'PY'
import json, sys
conf, key = sys.argv[1], sys.argv[2]
try:
    d = json.load(open(conf))["projects"]["default"]
except Exception as e:
    sys.exit(f"cannot read {conf}: {e}")
v = d.get(key, "")
if not v or v.startswith("PASTE_"):
    sys.exit(f"{key} is not set in {conf}")
print(v)
PY
}

remote_url() {
  local tok pid
  tok="$(read_conf gitToken)"; pid="$(read_conf projectId)"
  printf 'https://git:%s@git.overleaf.com/%s' "$tok" "$pid"
}

# Never let the token reach the terminal or the mirror's stored config.
scrub() { sed -E 's#https://git:[^@]*@#https://#g; s/olp_[A-Za-z0-9]+/<token>/g'; }

ensure_mirror() {
  if [ ! -d "$MIRROR/.git" ]; then
    echo "cloning Overleaf project into ${MIRROR#$REPO/} ..."
    git clone --quiet "$(remote_url)" "$MIRROR" 2>&1 | scrub
  fi
  # Keep the token out of .git/config; supply it per-invocation instead.
  git -C "$MIRROR" remote set-url origin "https://git.overleaf.com/$(read_conf projectId)"
}

git_ol() {
  git -C "$MIRROR" -c "credential.helper=!f(){ echo username=git; echo password=$(read_conf gitToken); };f" "$@"
}

case "$PROJECT" in
  push)
    ensure_mirror
    git_ol fetch --quiet origin main
    git_ol checkout --quiet main
    git_ol reset --hard --quiet origin/main
    echo "building verified package ..."
    trap 'rm -rf "$BUILD"' EXIT
    if ! python3 "$REPO/tools/make_arxiv.py" --out "$BUILD/pkg" "$@"; then
      echo
      echo "package build failed; Overleaf not touched. Fix the problems above" >&2
      echo "(a stale .bbl usually just needs tools/build_tex.sh) and rerun." >&2
      exit 1
    fi
    # Replace tracked content, preserving .git; drop arXiv-only metadata.
    git -C "$MIRROR" rm -rq --ignore-unmatch .
    rsync -ac --exclude='CHECKLIST.md' --exclude='MANIFEST.txt' \
             --exclude='SUBMISSION.md' "$BUILD/pkg/" "$MIRROR/"
    git -C "$MIRROR" add -A
    if git -C "$MIRROR" diff --cached --quiet; then
      echo "Overleaf already matches tex/; nothing to push."
      exit 0
    fi
    git -C "$MIRROR" diff --cached --stat | tail -3
    git -C "$MIRROR" commit -q -m "Sync from repository ($(git -C "$REPO" rev-parse --short HEAD))"
    git_ol push --quiet origin main 2>&1 | scrub
    echo "pushed to Overleaf."
    ;;

  pull)
    ensure_mirror
    git_ol fetch --quiet origin main
    git_ol checkout --quiet main
    git_ol reset --hard --quiet origin/main
    # Overleaf/<path> -> tex/<path>. No --delete: a file absent from the
    # package (figs/extracted, probe files) must survive the copy.
    # -c compares checksums, not mtimes: rewriting an identical file with a fresh
    # timestamp would make the staleness checks in make_arxiv.py and build_tex.sh
    # report a rebuild that is not needed.
    rsync -ac --exclude='.git' --exclude='/IEEEtran.cls' --exclude='/IEEEtran.bst' \
             --exclude='main.bbl' --exclude='CHECKLIST.md' --exclude='MANIFEST.txt' \
             --exclude='SUBMISSION.md' "$MIRROR/" "$REPO/tex/"
    echo "Overleaf edits copied into tex/. Review before committing:"
    git -C "$REPO" diff --stat -- tex | tail -15
    ;;

  status)
    ensure_mirror
    git_ol fetch --quiet origin main
    echo "Overleaf HEAD : $(git_ol log -1 --format='%h %ad %s' --date=short origin/main)"
    echo "repository    : $(git -C "$REPO" log -1 --format='%h %ad %s' --date=short)"
    echo "uncommitted in tex/: $(git -C "$REPO" status --porcelain -- tex | wc -l) file(s)"
    ;;

  *)
    sed -n '2,13p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'
    exit 1
    ;;
esac
