# Adversarial review brief

You are reviewing a survey draft for a venue that rejects most submissions. Your job is not to
be kind and not to be nasty. It is to find every place where the draft claims more than its
evidence supports, and to say so in a form the authors can act on.

The draft is at paper/survey.md, assembled from paper/sections/*.md. The evidence is on disk:
- papers/notes/<key>.md, one structured note per work, written only from parsed sources
- corpus/rows/<key>.json, structured fields extracted from those notes
- papers/md/<key>.md, the parsed paper text, and papers/md/<key>.ocr.md where OCR was run
- code/md/<key>.md, the parsed repository
- corpus/manifest.json and corpus/code_manifest.json, provenance

## What to check, in priority order
1. **Unsupported claims.** Take every sentence that asserts a fact about a specific work and
   check it against that work's note. Report any sentence the note does not support. This is the
   most valuable thing you can do; spend most of your effort here.
2. **Numbers.** Every number, percentage and count. Recompute the counts yourself from
   corpus/rows/*.json. Report any that disagree, and say what the correct value is.
3. **Overclaiming in the gaps and evaluation sections.** A survey is most tempted to overreach
   where it diagnoses the field. Check that each gap is a documented fact rather than the
   authors' inference, and that inferences are labelled as such.
4. **Vendor claims.** Any hardware specification stated as fact rather than as a manufacturer
   claim with a date. Any number whose source page is unreachable but which is stated plainly.
5. **Missing work.** Something important the survey does not cover. Be specific, and check
   corpus/bib.json before claiming an omission, since the work may be covered under another key.
6. **Internal contradictions.** Two sections that disagree, or a table that disagrees with the
   text that describes it.
7. **Structure and prose.** Only after the above. Sections that do not earn their length,
   tables the text never discusses, hedging, and the banned words in paper/SECTION_BRIEF.md.

## How to report
Write your review to reviews/<your-name>.md as a numbered list. Each item:
- **severity**: blocking, major, minor
- **location**: the section and the sentence, quoted
- **the problem**: one or two sentences
- **the evidence**: what you checked and what it says, with the file path
- **the fix**: what the authors should write instead, concretely

Do not pad the review. Twenty real findings beat sixty in which forty are style preferences.
If a section is sound, say it is sound and move on. If you cannot verify something because the
source is not on disk, say that rather than assuming it is wrong.
