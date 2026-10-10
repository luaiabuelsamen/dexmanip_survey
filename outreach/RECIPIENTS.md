# Recipients: who each letter went to, and how the address was found

One line per letter. Addresses are deliberately not printed here. What matters for auditing this
survey is who was written to, on what basis, and what came back; publishing a consolidated list of
researchers' contact details serves none of that. Every address used was already published by its
owner, in the paper's own PDF or on a page they control, and none was inferred from a name and a
domain. The source column records which, so the choice of recipient is checkable without the
address itself.

All nine letters were sent on 19 September 2026. Each gave until 10 October 2026 to reply and said
that silence would be recorded as silence rather than as agreement.

| key | recipient | how the address was found | reply |
|---|---|---|---|
| `physhoi_2023` | first author, HKUST | the author's own page, wyhuai.github.io/info | **silent**, window closed 2026-10-10 |
| `dexpbt_2023` | a coauthor at NVIDIA, three more in copy | the DeXtreme PDF in this corpus | **silent**; one automatic out-of-office reply, two copied addresses rejected |
| `dexpoint_2022` | senior author at UC San Diego, first author in copy | UCSD CSE faculty profile; the first author's own site | **replied 2026-09-20**, claim withdrawn; see CHANGELOG.md |
| `dextreme_2022` | a coauthor at NVIDIA, three more in copy | the paper's own PDF, page 1 | **silent**; two copied addresses rejected |
| `pddm_2019` | senior author at UC Berkeley | his CV at people.eecs.berkeley.edu | **silent**, window closed 2026-10-10 |
| `penspin_2024` | senior author at UC San Diego | UCSD CSE faculty profile | **silent**, window closed 2026-10-10 |
| `pianomime_2024` | senior author at TU Darmstadt, a coauthor in copy | TU Darmstadt IAS team page; the coauthor's own site | **silent**, window closed 2026-10-10 |
| `unidexgrasp_2023` | corresponding author at Peking University, first author in copy | the project page, pku-epic.github.io/UniDexGrasp | **forwarded to two coauthors 2026-10-02**, copying this survey's author; no answer |
| `visual_dexterity_2022` | senior author at MIT | the paper's own PDF, page 1 | **silent**, window closed 2026-10-10 |

Four of the nine addresses came from a paper already in this corpus. The other five came from a
page the author controls.

## Where a letter went to a coauthor rather than the first author

Four letters went to a senior author because the first author's current address is not published
anywhere this survey could check: Petrenko (DexPBT), Nagabandi (PDDM), Jun Wang (PenSpin) and Cheng
Qian (PianoMime). In each case the recipient is a coauthor of the paper the letter is about, so the
letter reached someone who can answer it, and each letter said so and asked to be forwarded.


## What came back, at the close of the window on 10 October 2026

Of the nine letters: one substantive reply, one acknowledgement without an answer, seven silent.

The reply was from the corresponding author of `dexpoint_2022`, on 20 September. It showed that
three parts of that comparison did not hold, the row left the contradiction class, and the census
went from nine to eight. `CHANGELOG.md` records it.

The acknowledgement was on `unidexgrasp_2023`. On 2 October a copied coauthor forwarded the letter
to two further coauthors, asked them whether they recalled the cause of the difference, and copied
this survey's author on that forward. No answer followed before the window closed. The letter was
read and passed on, and the question in it is open: a forward is neither a confirmation nor a
dispute, so the row is unchanged and the claim is recorded as unanswered rather than as agreed.

Two things qualify the seven silences, and both are recorded in the rows rather than smoothed over.

On `dexpbt_2023` and `dextreme_2022`, which went to the same recipient with three coauthors in
copy, the recipient's mail server rejected two of the three copied addresses. Those two coauthors
never received the letter. The address each letter was addressed to was not among the rejections,
so in both cases the letter did reach a coauthor of the paper it concerns, and a third copied
address was not rejected either. Both bounces are in the sent thread.

On `dexpbt_2023` a copied coauthor's mailer returned an automatic out-of-office message, which
names a week of travel that had already ended when the letter was sent. It is not an answer and is
not counted as one.

Silence is recorded as silence. Nothing in this file or in the paper treats it as agreement, and
every claim the letters asked about rests on a repository at a named commit against the paper's
own table, which any reader can check without the authors' agreement.
