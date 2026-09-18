# Writing brief, binding on every section

Audience: a researcher who knows robot learning and is choosing a hand, a simulator and a
training recipe, or is reviewing someone who has. Assume they know what PPO and behaviour
cloning are. Do not explain them.

## Evidence rules
1. Every factual claim about a specific work cites its key in backticks, e.g. `dextrack_2025`,
   and must be supported by that paper's note in papers/notes/. If the note does not support it,
   the sentence does not go in.
2. Numbers come from corpus/rows/*.json or from a note that names the table the number is in.
   Quote the condition with the number: which hand, how many trials, simulation or real.
3. Where a source could not be obtained, say so rather than describing the work from memory.
   The five paywalled works are listed in paper/METHOD.md and may be cited by metadata only.
4. Where paper and released code disagree, say both and name the file. These disagreements are
   a finding of this survey, not an aside.
5. Vendor specifications are manufacturer claims. Write them as claims, with the date.
6. Never write "many works" or "several papers" without a count you can defend from the rows.

## Prose rules
One idea per sentence. Around 20 words. No em-dashes, no parentheticals, no arrows, no
semicolons joining clauses. State the fact, then the consequence, as two sentences.
Do not use the words: novel, seminal, paradigm-shifting, leverage, delve, landscape, realm,
crucial, pivotal, tapestry, testament, underscore, showcase.
Do not open a section by announcing what the section will do. Start with the content.
Do not close a section with a summary of itself.
Tables and figures are referenced by number in the text, and each is discussed, not merely
pointed at. A table the text never discusses should be cut.

## Voice
The survey has a point of view and states it. When the evidence supports a judgement, make the
judgement in plain words and show the evidence. When the evidence is thin, say the evidence is
thin. Do not hedge every sentence, and do not overclaim to compensate.

## Length
Section 1: 800 words. Section 2: 900. Section 3: 2200. Section 4: 2200. Section 5: 3500.
Section 6: 1600. Section 7: 2000. Section 8: 1400. Section 9: 400.
These are targets, not limits. Going 20 percent over for substance is fine. Padding is not.
