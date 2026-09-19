One JSON object per paper, written to corpus/rows/<key>.json by an extraction agent reading
papers/notes/<key>.md ONLY. Every field is what the paper itself did, never what it cites.
Use null when the note says "not stated" or does not settle it. Never guess.

{
 "key": str,
 "year": int,
 "class": one of ["method","benchmark","dataset","simulator","hand","sensor","survey","eval-protocol"],
 "task_family": one or more of ["reorient","grasp","functional/tool","track-human-ref","bimanual-coord",
                "handover","music","locomanipulation","other"] or null,
 "paradigm": one or more of ["RL","BC","diffusion","flow","RL+demo","distillation","VLA","MPC",
             "trajopt","grasp-synthesis","teleop-system","data-collection","world-model"] or null,
 "algorithm": str or null,                 // e.g. "PPO", "MAPPO", "CVAE+L1", "flow matching"
 "hand": str or null,                      // the robot hand the paper's own experiments use
 "hand_dof": int or null,                  // actuated DoF of that hand, if the note states it
 "bimanual": true/false/null,              // the paper's own experiments use two hands
 "arm": str or null,
 "sim": str or null,                       // the simulator its own experiments run in
 "n_envs": int or null,
 "real_robot": true/false/null,
 "real_trials": int or null,               // total real trials behind the headline number
 "sim_episodes": int or null,
 "success_criterion": str or null,         // verbatim if short, e.g. "rotation within 0.1 rad"
 "headline_metric": str or null,
 "headline_value": str or null,            // include units and the table it came from
 "objects_train": int or null,
 "objects_test_unseen": int or null,
 "human_data": str or null,                // dataset name or "none"
 "penetration": one of ["penalised","measured","constrained","not addressed",null],
 "reward_terms": int or null,              // count of terms in the paper's stated reward
 "code_released": true/false/null,
 "paper_code_mismatch": str or null,       // one sentence, or null if none found
 "note_gaps": str or null,                 // what the note flagged as unreadable in the source
 "mismatch_class": str or null,            // contradiction, parse-limitation, code-absent,
                                           // version-skew, internal-inconsistency
 "mismatch_confidence": str or null,       // high, medium, low
 "mismatch_review": str or null,           // what a re-reading changed, beside the charge it changed
 "mismatch_artifact": object or null       // required on every `contradiction` row: the public
                                           // artefact the claim is a claim about. Keys: repo,
                                           // commit (both copied from corpus/code_manifest.json),
                                           // file (its path inside that repository), locator
                                           // (the function, key or config block inside the file),
                                           // paper (the value the paper prints, with its table or
                                           // equation), code (what the file at that commit
                                           // contains). Backticks mark code spans; the table
                                           // generators set them in monospace. The two values are
                                           // the two halves of paper_code_mismatch and add
                                           // nothing to it: the field exists so the comparison
                                           // can be printed as a statement about a named
                                           // artefact that a reader can check, rather than as a
                                           // statement about what anyone did.
}
