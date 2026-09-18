# 9. Conclusion

The binding constraint on this field is not ideas. It is verification. Thirty-seven of the 61
method papers that released code disagree with their own paper about the objective that was
trained, and the 45 that released nothing cannot be checked at all. A reward table in a paper is a
claim about a document, not about a run. `physhoi_2023` is the case to remember, because the term
its table weights at 0.1 is set to zero in the code, and its own success criterion could not have
detected that.

The second finding is that the quantity most specific to dexterous manipulation is the one nobody
measures. Contact is what separates a hand from a gripper. Eleven of 110 method rows address
interpenetration, seven of those do it offline in a grasp synthesiser or a trajectory optimiser,
and not one reports a penetration number for its own trained policy's rollouts. `dextrack_2025` has
the formula and points it at its inputs.

The third is that hardware and software have come apart. Tables 2 and 3 hold 33 hands, the
simulators ship six between them, and 19 of the 33 appear in no method row. The generalist policies
that were meant to absorb all of this mostly do not use hands, with five of 16 VLA rows reporting
no dexterous-hand result at all.

What this survey cannot establish is which method is better than which. It re-runs nothing, and
Section 7 argues the published numbers do not compare. Five works are paywalled and no claim here
rests on them. Six papers' reward weights defeated our converter while remaining legible to a human
with the PDF, so that count measures our pipeline as much as it measures them. The failure-mode
count in Section 8.10 is a floor set by a note template, not a rate.

Three things to do next week, cheapest first.

If you are publishing, generate the reward table from the config that trained the reported run,
print it, and cite the commit. State the trial count, state the success predicate, and release the
per-trial outcomes. None of that needs a GPU.

If you are running experiments, measure penetration depth over your evaluation rollouts on a dense
surface sample, and never let that measure become a reward. `toporetarget_2026` shows what the
number looks like when someone takes it seriously, and what the widely used retargeters look like
when nobody does.

If you are choosing hardware, pick from the six hands a simulator already ships. An announced hand
has no URDF, no datasheet that can be checked, and no paper in this corpus that used it.
