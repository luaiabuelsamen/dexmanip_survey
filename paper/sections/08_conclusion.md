# 8. Conclusion: the seven claims, and what to do next

The binding constraint on this field is not ideas. It is verification. Seven claims survive the
corpus. Each is one sentence here, with the section that carries its evidence and the experiment
that would close it. Nothing is argued in this list: the denominator, the evidence and the
prescription sit in the section named, at the end of it, so that a finding and its consequence are
read together and stated once.

1. Nine of the 62 method rows that released parseable code state, in a named file at a named commit,
   something other than the value their paper prints, and eight further charges have been withdrawn
   since the first draft of that census. Table 11 gives each of the nine as a repository, a commit, a
   file and two values, and none of their authors was written to before this was posted: section 5.6
   says that beside the finding, with the drafted and unsent letters in `outreach/` and the route by
   which a disputed case is corrected (section 5.6 and the technical supplement).

2. No closed-loop policy in the corpus reports interpenetration for the rollouts of its own trained
   policy, and all eleven rows that handle penetration at all sit on the reference side of the
   reference-versus-rollout split (section 7.2, and the contact-handling bar of Figure 6).

3. The evaluation-methodology literature the protocol of section 7.3 is assembled from contains no
   dexterous hand at all: of its seven corpus rows, one runs a parallel-jaw gripper and the other six
   state no hand (section 7.4, Table 8).

4. The generalist and vision-language-action policies that do evaluate on a multi-fingered hand run
   it at a median of 6 actuated degrees of freedom, against 16 across the reinforcement-learning rows
   that state a count, and the two rows that reach the larger band on paper never say whether the
   hand was in the evaluation (section 5.4).

5. Eight hands that can be bought today or built from published designs take zero method rows between
   them, while the corpus's own experiments concentrate on four designs (section 3.4, Figure 2).

6. Twenty-one of the 28 rows that put a learned closed-loop controller on two multi-fingered hands run
   one policy over a concatenated two-hand observation, a choice that has been compared twice with
   opposite outcomes and ablated once (section 6.2, Figure 5).

7. Human data does not port across hands and the map is usually unstated: 33 of the 53 method rows
   that use human data never say how the human motion reached the robot hand (section 5.3, Table 6).

Six of the seven are gaps in the literature. The first is a result about publishing practice, and
this survey's own corrections to it are printed beside it in section 5.6 rather than kept in the
repository.

Three of those claims carry a case worth remembering. A reward table in a paper is a claim about a
document, not about a run, and `physhoi_2023` is the instance to keep in mind: the term its table
weights at 0.1 is set to zero in the file at the commit this survey fetched, and the success
criterion the paper reports is itself position-only. Contact is what separates a hand from a gripper, and the obstacle to measuring it is not the
engines. IsaacGymEnvs ships a task that computes a per-environment maximum interpenetration depth
against meshes and gates the policy update on a 1 mm threshold, and `tactile_genesis_2026` offers
penetration depth on Genesis geometry as a sensor. The tooling sits in the field's own benchmark
repository and the number is still not reported. `dextrack_2025` has the formula and points it at
its inputs. And hardware and software have come apart on a narrower claim than the hand count first
suggests, because 11 of the 19 hands that take no method row are neither sold nor open and take
none for that reason, which is why the fifth claim is eight hands and not nineteen.

What this survey cannot establish is which method is better than which. It re-runs nothing, and
Section 7 argues that the published numbers do not compare. Six works are cited by metadata only,
and a seventh, Ma and Dollar 2011, is on disk but unread; no claim rests on any of them. Every
coverage statistic here counts what this survey's extraction captured rather than what the
literature reported. Each is a floor and not a rate, because every miss converts a reporting paper
into a silent one.

Three things to do next week, cheapest first.

If you are publishing, generate the reward table from the config that trained the reported run,
print it, and cite the commit. State the trial count, state the success predicate, and release the
per-trial outcomes. None of that needs a GPU.

If you are running experiments, measure penetration depth over your evaluation rollouts on a dense
surface sample, and never let that measure become a reward. `toporetarget_2026` shows what the
number looks like when someone takes it seriously, and what the widely used retargeters look like
when nobody does.

If you are choosing hardware, the corpus names four hands and no more. The Allegro carries 35
method rows, the Shadow 21, the Inspire 19 and LEAP 12, and every other hand in Tables 2 and 3
carries eight rows or fewer. An announced hand has no URDF, no datasheet that can be checked, and
no paper in this corpus that used it.
