# <key> — <title> (<authors>, <venue> <year>)

sources: papers/md/<key>.md [sha from corpus/manifest.json] ; code/md/<key>.md [commit] (or "no code")

## One-line contribution
## Setting
- hand(s): (model, DoF, vendor) ; arm: ; single/bimanual:
- simulator / physics: (engine, timestep, contact model if stated, #envs)
- observation: (state / vision / tactile; what exactly)
- action space: (joint targets / torques / delta; control rate)
- objects / data: (dataset, #objects, #trajectories)
## Method
- paradigm: (RL / IL / hybrid / MPC / VLA) ; algorithm:
- reward or loss (quote the terms from the paper or code; cite line/section):
- key trick(s):
## Evaluation
- metrics (exact definitions):
- headline numbers (with the table/figure they come from):
- baselines beaten:
- real robot? (which hand, #trials, success rate)
## Limitations stated by the authors
## Quotable claims (verbatim, with section)
## Notes for the survey (which sections this feeds; contradictions with other notes)
