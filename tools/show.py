"""Print the bib entry, manifest provenance and file sizes for one or more keys."""
import json, sys, os
from pathlib import Path
R = Path(__file__).resolve().parents[1]
bib = {e["key"]: e for e in json.loads((R/"corpus/bib.json").read_text())}
man = json.loads((R/"corpus/manifest.json").read_text()) if (R/"corpus/manifest.json").exists() else {}
cman = json.loads((R/"corpus/code_manifest.json").read_text()) if (R/"corpus/code_manifest.json").exists() else {}
for k in sys.argv[1:]:
    e = bib.get(k); print("="*80); print(json.dumps(e, indent=1))
    print("paper md:", (R/f"papers/md/{k}.md").exists() and os.path.getsize(R/f"papers/md/{k}.md"), "| provenance:", man.get(k))
    print("code md:", (R/f"code/md/{k}.md").exists() and os.path.getsize(R/f"code/md/{k}.md"), "| provenance:", cman.get(k))
