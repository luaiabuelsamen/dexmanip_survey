# 8. Conclusion: the seven claims, and what to do next

This corpus describes a field that has converged. Most of it trains with reinforcement learning
on privileged state in a GPU simulator and distills the result into a vision-only student; a
second branch, growing faster, learns from teleoperated demonstration instead; and almost all
of it runs on four hands. What the field cannot currently do is compare its own results, and
most of the seven claims below follow from that. Each is one sentence, with the section that
carries its evidence and the experiment that would close it. Nothing is argued here: the
denominator, the evidence and the prescription sit in the section named, so that a finding and
its consequence are read together and stated once.

1. Eight hands that can be bought today or built from published designs take zero papers
   between them, while the corpus's own experiments concentrate on four designs (section 3.4,
   Figure 2).

2. Human data does not port across hands and the map is usually unstated: 33 of the 53 method
   papers that use human data never say how the human motion reached the robot hand (section
   5.3, Table 6).

3. Twenty-one of the 28 papers that put a learned closed-loop controller on two multi-fingered
   hands run one policy over a concatenated two-hand observation, a choice that has been
   compared twice with opposite outcomes and ablated once (section 6.2, Figure 5).

4. The generalist and vision-language-action policies that do evaluate on a multi-fingered
   hand run it at a median of 6 actuated degrees of freedom, against 16 across the
   reinforcement-learning papers that state a count, and the two papers that reach the larger
   band on paper never say whether the hand was in the evaluation (section 5.4).

5. The evaluation-methodology literature the protocol of section 7.3 is assembled from
   contains no dexterous hand at all: of its seven papers in this corpus, one runs a parallel-jaw
   gripper and the other six state no hand (section 7.4, Table 8).

6. Eight of the 63 papers that released parseable code state, in a named file at a named
   commit, something other than the value their paper prints. Table 11 gives each one as a repository, a
   commit, a file and two values, and all of their authors were written to before this was
   posted: section 5.6 says that beside the finding, with the letters in `outreach/` and the
   route by which a disputed case is corrected (section 5.6 and Appendix C).

7. Penetration is almost never measured where it would matter. No paper here reports how far
   its hand sank into the object, measured in the physics its own policy ran in. The one that
   does report a volume for a pose its own policy reached measures it outside the simulator, on
   meshes the simulator never used, and reports zero inside it. On the reference-versus-rollout
   split that frames this survey, every paper that handles penetration at all is still measuring a
   reference (section 7.2, and the contact-handling bar of Figure 6).

Six of the seven are gaps in the literature. The sixth is a result about publishing practice,
and this survey's own corrections to it are printed beside it in section 5.6 rather than kept
in the repository.

Three of those claims carry a case worth remembering. Hardware and software have come apart on
a narrower claim than the hand count first suggests: 11 of the 19 hands that take no paper
are neither sold nor open and take none for that reason, which is why the first claim is eight
hands and not nineteen. A reward table in a paper is a claim about a document rather than about
a run, and `physhoi_2023` is the instance to keep in mind, since the term its table weights at
0.1 is set to zero in the file at the commit this survey fetched and the success criterion the
paper reports is itself position-only. And the obstacle to measuring contact is not the
engines: IsaacGymEnvs ships a task that computes a per-environment maximum interpenetration
depth and gates the policy update on a one-millimetre threshold, so the tooling sits in the
field's own benchmark repository while the number goes unreported.

What this survey cannot establish is which method is better than which. It re-runs nothing, and
Section 7 argues that the published numbers do not compare. Six works are cited by metadata only,
and a seventh, Ma and Dollar 2011, is on disk but unread; no claim rests on any of them. Every
coverage figure here is a floor rather than a rate, for the reason Appendix A sets out.

Three things to do next week, cheapest first.

If you are publishing, generate the reward table from the config that trained the reported run,
print it, and cite the commit. State the trial count, state the success predicate, and release the
per-trial outcomes. None of that needs a GPU.

If you are running experiments, measure penetration depth over your evaluation rollouts on a dense
surface sample, and never let that measure become a reward. `toporetarget_2026` shows what the
number looks like when it is reported carefully, and what the widely used retargeters look like
when it is not.

If you are choosing hardware, the corpus names four hands and no more: the Allegro, the Shadow,
the Inspire RH56 family and LEAP, in that order, with the Allegro alone carrying 35 of the 113
papers. Every other hand in Tables 2 and 3 carries eight papers or fewer. An announced hand has no
URDF, no datasheet that can be checked, and no paper in this corpus that used it.
