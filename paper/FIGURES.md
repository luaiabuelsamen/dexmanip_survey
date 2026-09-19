# Figures: what each one must show, and how it is drawn

All figures are hand-written SVG in paper/figures/, so they render in any markdown viewer and
carry no dependency. Each has a light and dark variant of its palette via CSS custom properties,
and every number in a figure traces to corpus/rows or corpus/stats.json.

## Figure 1. The field on one page, and the map of the survey
A left-to-right flow with five columns: data sources, embodiment, simulator, training paradigm,
evaluation. Every column head names the section that covers it, so the figure is the table of
contents drawn and the reader can navigate from it; it is the first thing in Section 1 for that
reason. Nodes are sized by how many corpus papers sit in them and carry their count as a label.
Edges show the routes that actually exist in the corpus, drawn only where a paper takes them and
never thinner than prints. The point of the figure is that the routes converge: almost everything
ends in a policy trained in a GPU simulator and distilled to vision.

## Figure 2. Which hands the literature actually runs on
A horizontal bar chart of hands by number of corpus papers whose own experiments use them, split
by whether the hand is open hardware, sold commercially, or announced only. The finding to make
visible: a handful of hands carry nearly all the published work, and none of the announced
humanoid hands carries any.

## Figure 3. One simulation step, and where engines differ
A pipeline diagram: broad-phase, narrow-phase and contact generation, constraint assembly,
solver, integration. Under each stage, the engines that make a materially different choice, with
the choice named. Annotated with the one thing the survey cares about: which stages let
penetration through and which expose it to the user.

## Figure 4. Taxonomy of training paradigms
A tree. Root splits into: learn from reward, learn from demonstration, learn from a reference
trajectory, and do not learn. Each branch subdivides to the level at which papers differ, with
representative corpus keys at the leaves and the count of corpus papers per leaf. Cross-links
drawn as dashed edges where a method belongs to two branches, which most 2024-2026 work does.

## Figure 5. Bimanual coordination architectures
Four panels side by side: one policy over both hands; two policies with shared observation;
leader and follower with role assignment; relative-frame formulation where the action is
expressed between the hands. Each panel labelled with the corpus papers that use it. The panel
borders carry the count, so the reader sees that the field is concentrated in the first.

## Figure 6. What gets reported, and what does not
A matrix of corpus method papers against reported quantities: success rate, trial count,
confidence interval, unseen-object generalisation, penetration or contact quality, wall-clock
cost, released code, released checkpoints. Filled cells only where the note confirms it. This
figure is the evidence for the evaluation section and should be uncomfortable to look at.
