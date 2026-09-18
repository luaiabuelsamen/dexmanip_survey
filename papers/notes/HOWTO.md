Rules for writing a note (papers/notes/<key>.md):
1. Read only papers/md/<key>.md and code/md/<key>.md (if present). Nothing from memory enters a note. If you know something the file does not say, leave it out.
2. Start with `python tools/show.py <key>` for the bib entry and provenance; put the sha256 prefix (8 chars) and commit (8 chars) in the sources line.
3. Long markdowns: do not cat the whole file. grep -n for "^#" to get the section map, then sed -n ranges for abstract, method, experiments, tables, limitations. Tables are often flattened: read them carefully; if a number is ambiguous say so.
4. Every number in the note must carry where it came from (table/figure/section). Quote reward terms and metric definitions verbatim when they exist.
5. Code: quote the reward/observation function or task config that actually implements the paper's claim, with the file path. Note any mismatch between paper and code.
6. If the source is a vendor page or blog (no paper), the note records only what the page says, and marks the entry "source: vendor page; specs are manufacturer claims, not measurements". If the page fetch was blocked (HTTP 403, Cloudflare, empty), say "SOURCE THIN" at the top and list what the bib `specs` field claims separately as unverified.
7. Follow papers/notes/TEMPLATE.md. Length: 60-150 lines for a paper, 25-60 for a vendor page. No filler.
