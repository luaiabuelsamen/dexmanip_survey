"""Fetch the non-PDF sources (vendor spec pages, blog posts, DOI landing pages) for entries that have no arXiv id, and save them as markdown so hand specs are quoted from a file on disk, not from memory."""
import json, re, time
from pathlib import Path
import requests, html2text
ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "papers/md"; MAN = ROOT / "corpus/pages_manifest.json"
bib = json.loads((ROOT / "corpus/bib.json").read_text())
man = json.loads(MAN.read_text()) if MAN.exists() else {}
h = html2text.HTML2Text(); h.ignore_images = True; h.body_width = 0
for e in bib:
    k = e["key"]
    if e.get("arxiv") or (MD / f"{k}.md").exists(): continue
    urls = [u for u in [e.get("pdf_url")] + re.findall(r"https?://[^\s)\]]+", e.get("why", "") + " " + e.get("specs", "")) if u]
    if not urls: continue
    parts = [f"# {e['title']}\n\nsource entry: {k}\n"]
    for u in dict.fromkeys(urls):
        try:
            r = requests.get(u, timeout=40, headers={"User-Agent": "Mozilla/5.0 (X11; Linux) dexmanip-survey/0.1"})
            ct = r.headers.get("content-type", "")
            if r.status_code != 200: parts.append(f"## {u}\n\nHTTP {r.status_code}\n"); continue
            if "pdf" in ct or r.content[:4] == b"%PDF":
                pdf = ROOT / "papers/pdf" / f"{k}.pdf"; pdf.write_bytes(r.content)
                import pymupdf; d = pymupdf.open(pdf); txt = "\n".join(p.get_text() for p in d); d.close()
                parts.append(f"## {u} (PDF)\n\n{txt[:120000]}")
            else:
                parts.append(f"## {u}\n\n{h.handle(r.text)[:60000]}")
        except Exception as ex:
            parts.append(f"## {u}\n\nfetch error: {ex}\n")
        time.sleep(1)
    (MD / f"{k}.md").write_text("\n\n".join(parts))
    man[k] = dict(urls=urls, fetched=time.strftime("%Y-%m-%d"), chars=sum(len(p) for p in parts))
    MAN.write_text(json.dumps(man, indent=1)); print(f"[ok] {k}: {len(urls)} urls", flush=True)
