"""Shallow-clone the code repositories in corpus/bib.json and parse each into one markdown file.

The markdown per repo holds: README, a filtered file tree, every config file that
defines a task/reward/observation (yaml/json under a size cap), and the top-level
docstrings plus function/class signatures of the Python files that mention
reward, observation, action, hand, sim, env, or policy. Enough to say what a method
actually does, without keeping the whole repository on a 9 GB disk.
"""
import ast, json, os, re, shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REPOS = ROOT / "code/repos"; OUT = ROOT / "code/md"; MANIFEST = ROOT / "corpus/code_manifest.json"
KEY = re.compile(r"reward|observ|action|hand|sim|env|policy|retarget|train|task|cfg|config", re.I)
SKIP_DIRS = {".git", "assets", "data", "datasets", "meshes", "urdf", "mjcf", "node_modules", "docs", "images", "img", "media", "__pycache__", "third_party", "checkpoints", "ckpt", "weights", "logs", "wandb"}

def run(cmd, cwd=None, timeout=600):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)

def tree(root, depth=3):
    lines = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts): continue
        if len(rel.parts) > depth: continue
        lines.append(("  " * (len(rel.parts) - 1)) + rel.name + ("/" if p.is_dir() else ""))
    return "\n".join(lines[:600])

def py_summary(path):
    try: src = path.read_text(errors="ignore")
    except Exception: return ""
    if len(src) > 400_000: return ""
    try: mod = ast.parse(src)
    except Exception: return ""
    out = []
    d = ast.get_docstring(mod)
    if d: out.append(f'"""{d[:600]}"""')
    for n in mod.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.append(f"def {n.name}({', '.join(a.arg for a in n.args.args)})")
        elif isinstance(n, ast.ClassDef):
            out.append(f"class {n.name}({', '.join(getattr(b, 'id', getattr(b, 'attr', '?')) for b in n.bases)})")
            cd = ast.get_docstring(n)
            if cd: out.append(f'    """{cd[:300]}"""')
            for m in n.body:
                if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.append(f"    def {m.name}({', '.join(a.arg for a in m.args.args)})")
    # reward / observation function bodies verbatim, capped
    for n in ast.walk(mod):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and re.search(r"reward|compute_obs|observation|_get_obs", n.name, re.I):
            seg = ast.get_source_segment(src, n) or ""
            if seg: out.append("\n```python\n" + seg[:4000] + "\n```")
    return "\n".join(out)

def parse_repo(key, url, dest):
    parts = [f"# {key}\n\nsource: {url}\n"]
    head = run(["git", "rev-parse", "HEAD"], cwd=dest).stdout.strip()
    parts.append(f"commit: {head}\n")
    for name in ["README.md", "readme.md", "README.rst", "README"]:
        p = dest / name
        if p.exists():
            parts.append("## README\n\n" + p.read_text(errors="ignore")[:30000]); break
    parts.append("## File tree (depth 3, assets pruned)\n\n```\n" + tree(dest) + "\n```")
    cfgs, pys = [], []
    for p in dest.rglob("*"):
        rel = p.relative_to(dest)
        if any(part in SKIP_DIRS for part in rel.parts) or not p.is_file(): continue
        if p.suffix in {".yaml", ".yml"} and p.stat().st_size < 40_000 and KEY.search(str(rel)):
            cfgs.append(p)
        elif p.suffix == ".py" and KEY.search(str(rel)) and p.stat().st_size < 400_000:
            pys.append(p)
    parts.append(f"## Config files ({len(cfgs)})\n")
    budget = 250_000
    for p in sorted(cfgs)[:60]:
        t = p.read_text(errors="ignore")
        if budget <= 0: break
        parts.append(f"### {p.relative_to(dest)}\n\n```yaml\n{t[:8000]}\n```"); budget -= min(len(t), 8000)
    parts.append(f"## Python signatures and reward/observation bodies ({len(pys)} files)\n")
    budget = 400_000
    for p in sorted(pys)[:250]:
        s = py_summary(p)
        if not s or budget <= 0: continue
        parts.append(f"### {p.relative_to(dest)}\n\n```\n{s[:12000]}\n```"); budget -= min(len(s), 12000)
    return "\n\n".join(parts), head

def main():
    bib = json.loads((ROOT / "corpus/bib.json").read_text())
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    only = set(sys.argv[1:])
    for e in bib:
        k, url = e["key"], (e.get("github") or "").strip()
        if not url or (only and k not in only): continue
        if k in manifest and (OUT / f"{k}.md").exists(): continue
        dest = REPOS / k
        if not dest.exists():
            r = run(["git", "clone", "--depth", "1", "--filter=blob:limit=512k", "--single-branch", url, str(dest)], timeout=900)
            if r.returncode != 0:
                print(f"[fail] {k}: {r.stderr.strip()[-200:]}", flush=True); shutil.rmtree(dest, ignore_errors=True); continue
        try:
            md, head = parse_repo(k, url, dest)
        except Exception as ex:
            print(f"[fail] {k}: parse {ex}", flush=True); continue
        (OUT / f"{k}.md").write_text(md)
        size = sum(f.stat().st_size for f in dest.rglob("*") if f.is_file())
        manifest[k] = dict(url=url, commit=head, bytes=size, md_chars=len(md))
        shutil.rmtree(dest, ignore_errors=True)  # disk is scarce: keep only the parsed markdown
        MANIFEST.write_text(json.dumps(manifest, indent=1))
        print(f"[ok] {k}: {size//1_000_000} MB, md {len(md)} chars", flush=True)

if __name__ == "__main__": main()
