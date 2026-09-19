## Abstract

A hand is dexterous when it can change an object's pose without putting the object down. This
survey covers that problem for one hand and for two: hands, simulators, training, evaluation. It
rests on 221 bibliography entries, 218 of them read into a structured row.

Papers disagree with their own released code. Of 62 method rows whose code could be read against
the paper, 38 record a discrepancy and nine are contradictions, where the code states a different
objective from the paper: `physhoi_2023` zeroes an object-rotation error its own reward table
weights at 0.1. Nobody measures interpenetration on a rollout. Eleven of the 96 method rows whose
notes settle the question address it at all, and not one reports it for the rollouts of its own
trained policy, though IsaacGymEnvs already computes that depth and gates a policy update on it.
Hardware has come apart from published work: 19 of the 33 hand rows appear in no method row, 8 of
them buyable or buildable today.

This survey re-runs no method and ranks nothing. On penetration it supplies a measurement method
and a count, not a threshold, and every coverage statistic here is a floor over what this
extraction captured.