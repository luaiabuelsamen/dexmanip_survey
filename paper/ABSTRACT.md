## Abstract

A dexterous hand can change an object's pose without setting it down. This survey examines how
learning-based systems acquire that ability, from hand design and contact simulation to policy
training, bimanual control, and evaluation. Its evidence base contains 218 structured records and
the public code released with the papers. Three findings recur across that evidence. First, nine
of the 62 methods with inspectable code describe a training objective differently in the paper
and repository. Each comparison is tied to a public file and revision; none of their authors was
contacted before posting. Second, no closed-loop policy in the corpus reports interpenetration for
the rollouts of its own trained policy, although existing simulators can compute the quantity.
Third, experiments remain concentrated on four established hands while eight hands that can be
bought or built appear in no method paper in the corpus. The survey does not rerun or rank methods.
Instead, it identifies what current reports can support and proposes a common evaluation protocol.
Because missing information may reflect the extraction as well as the source, all reporting counts
should be read as lower bounds.
