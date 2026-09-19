## Abstract

A hand is dexterous when it can change an object's pose without putting the object down. This
survey divides that problem the way its sections do: the hands, the simulators they are trained
in, how policies are trained, two hands on one object, and how it is evaluated. It rests on 218
sources read into a structured row, and on their released code. Papers disagree with their own
released code: most method rows whose code could be read against the paper record a discrepancy,
and nine are contradictions, where the code states a different objective from the paper. Nobody
measures interpenetration on a rollout: few of the rows that settle the question address it at
all, and not one reports it for its own trained policy's rollouts, though IsaacGymEnvs already
computes that depth and gates a policy update on it. Hardware has come apart from published work:
most tabulated hands appear in no method row, and several can be bought or built today. This
survey re-runs no method and ranks nothing: on penetration it supplies a measurement method and a
count, not a threshold, and every coverage statistic here is a floor over what this extraction
captured.
