# Cover letter template

Adapt the bracketed sections per paper. The per-paper detail (the exact claim, the file and line,
the commit, and what the survey prints if there is no reply) lives in the matching
`outreach/<key>.md` note — attach or paste that note as "the full note" referenced below.

---

Subject: A reading of [PAPER TITLE]'s released code, before we publish

Dear [Dr./Professor SURNAME] and coauthors,

I'm finishing a survey of dexterous manipulation methods that, among other things, checks each
paper's stated reward or training objective against the code the authors released, where code was
released. In going through [PAPER TITLE] ([VENUE, YEAR]), I found what looks like a difference
between [the reward equation / weight / observation channel] your paper describes and what the
released repository ([GITHUB URL], commit [COMMIT]) actually computes. I've attached the specific
claim, the exact file and line, and the wording the survey currently plans to print.

I want to be upfront that this is very possibly a misreading on my part — I am working from a
static snapshot of your repository, not running it, and it is easy to point at the wrong config, an
old commit, or a code path that isn't the one that produced your reported numbers. I am not
alleging anything about your results; I am asking you to check a specific, narrow claim before it
appears in print with your paper's name on it, and to correct me if I have it wrong.

Three things I would appreciate your view on:

1. Is the reading correct — does the file and line I've pointed to say what I think it says?
2. If it does, is there a reason the released configuration differs from what the paper describes
   (a later tuning pass, a different experiment than the one reported, a stripped-down public
   release, etc.) that we should note alongside the observation?
3. However you answer (1) and (2), would you like the wording of the claim changed before we
   publish — either to correct an error, add context, or soften language you feel overstates the
   case?

If you'd like the full note — the paper text, the code excerpt, and the exact sentences the survey
currently plans to print in Sections V and VIII and the appendix — rather than just this summary,
I'm happy to send it; just let me know.

I'd like to give you two to three weeks to respond before we finalize this section, so [DATE ~2-3
WEEKS OUT] if that's workable. If we don't hear back by then, we will note in the survey that we
wrote to you and did not receive a reply — we won't treat silence as agreement with the claim, and
we won't hold a non-reply against you in any way.

For what it's worth: an earlier draft of this section made sixteen such claims across the corpus;
seven were withdrawn after our own adversarial re-reading found them wrong or unfair, and each
withdrawal is recorded in the paper's row alongside the original claim (`mismatch_review` field in
our public data, `corpus/rows/<key>.json`). We would rather drop or correct a claim than publish
one that doesn't hold up, and a reply from you is exactly the kind of check we're asking for.

Thank you for your time, and for releasing the code in the first place — the survey's ability to
check any of this against a paper's own claims exists only because you made that code public.

Best,
[NAME]
[AFFILIATION / CONTACT]

---

Attachment or pasted-in: `outreach/<key>.md`
