# Evidence Bundle Sketch

Status: Sketch

Purpose: record what changed, what was validated, what evidence was produced, and what remains uncertain after a task.

## Template

```yaml
task_id: BACKLOG-000
title: Task title
completed_by: Codex | Claude Code | GitHub Copilot | human | mixed
completed_at: 2026-06-07T00:00:00-04:00
implementation_summary: >
  Concise summary of what changed.
changed_files:
  - path/to/file
tests_run:
  - command: pytest path/to/tests
    result: pass | fail | not_run
    notes: concrete counts or reason not run
validation_outputs:
  - path: path/to/output
    description: What this output proves or fails to prove
experimental_probes_run:
  - probe_id: optional
    path: path/to/experiment-vv-evidence.md
    result: pass | fail | ambiguous | not_run
generated_artifacts:
  - path/to/artifact
screenshots_or_visual_checks:
  - path/to/screenshot-or-report
risks_accepted:
  - risk_id: optional
    note: Accepted risk and owner approval, if any
known_limitations:
  - limitation
next_recommended_action:
  - action
human_approval_state: not_required | pending | approved | rejected
```

## Notes

- Evidence bundles are task-local records, not canonical project truth.
- Generated dashboards should read evidence bundles, but dashboards must not replace them.
- If validation was not run, the bundle should say why.
