"""Download arXiv PDFs listed in corpus/bib.json and convert each to markdown.

A paper enters the corpus only once its PDF is on disk and its markdown was
produced from that PDF; the manifest records sha256, page count and the
converter version so a quoted passage can be traced to a file.
"""
import argparse, hashlib, json, os, re, sys, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "papers/pdf"; MD = ROOT / "papers/md"; MANIFEST = ROOT / "corpus/manifest.json"

def arxiv_id(entry):
    a = entry.get("arxiv") or ""
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", a)
    return m.group(1) if m else None

def download(url, dest, tries=3):
    for i in range(tries):
        try:
            r = requests.get(url, timeout=60, headers={"User-Agent": "dexmanip-survey/0.1 (academic)"})
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                dest.write_bytes(r.content); return True
            time.sleep(2 + 3 * i)
        except requests.RequestException:
            time.sleep(2 + 3 * i)
    return False

def to_markdown(pdf, md):
    import pymupdf4llm, pymupdf
    doc = pymupdf.open(pdf)
    n = doc.page_count; doc.close()
    try:
        text = pymupdf4llm.to_markdown(str(pdf), show_progress=False, use_ocr=False)
    except Exception:
        d = pymupdf.open(pdf); text = "\n\n".join(f"<!-- page {i+1} -->\n" + pg.get_text() for i, pg in enumerate(d)); d.close()
    if len(text.strip()) < 2000:
        d = pymupdf.open(pdf); text = "\n\n".join(f"<!-- page {i+1} -->\n" + pg.get_text() for i, pg in enumerate(d)); d.close()
    md.write_text(text)
    return n, len(text)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--bib", default=ROOT/"corpus/bib.json")
    ap.add_argument("--only", nargs="*"); ap.add_argument("--sleep", type=float, default=3.0)
    a = ap.parse_args()
    bib = json.loads(Path(a.bib).read_text())
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    for e in bib:
        k = e["key"]
        if a.only and k not in a.only: continue
        pdf, md = PDF / f"{k}.pdf", MD / f"{k}.md"
        if md.exists() and k in manifest and manifest[k].get("md_chars", 0) > 2000: continue
        url = e.get("pdf_url")
        aid = arxiv_id(e)
        if not url and aid: url = f"https://arxiv.org/pdf/{aid}"
        if not url: print(f"[skip] {k}: no pdf source", flush=True); continue
        if not pdf.exists():
            ok = download(url, pdf)
            if not ok: print(f"[fail] {k}: download {url}", flush=True); continue
            time.sleep(a.sleep)
        try:
            pages, chars = to_markdown(pdf, md)
        except Exception as ex:
            print(f"[fail] {k}: convert {ex}", flush=True); continue
        manifest[k] = dict(title=e.get("title"), arxiv=aid, source=url, pages=pages, md_chars=chars,
                           sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), converter="pymupdf4llm",
                           fetched=time.strftime("%Y-%m-%d"))
        MANIFEST.write_text(json.dumps(manifest, indent=1))
        print(f"[ok] {k}: {pages} pages, {chars} chars", flush=True)

if __name__ == "__main__": main()
