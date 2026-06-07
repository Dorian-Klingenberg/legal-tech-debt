# Experiment-Backed V&V Evidence Sketch

Status: Sketch

Purpose: record experimental validation or verification evidence when tests alone cannot show whether the implemented behavior satisfies the domain need.

## Template

```yaml
vv_id: EXPVV-000
requirement_or_task_under_test: BACKLOG-000 | REQ-000 | task-contract-path
experiment_type: sandbox_probe | corpus_probe | simulation | playtest | generated_report_review | UI_probe | benchmark | other
source_context:
  - path: path/to/requirement-or-task
  - path: path/to/experiment-setup
setup: >
  What was run, generated, simulated, reviewed, or observed?
expected_behavior: >
  What should happen if the requirement or implementation is valid?
observed_behavior: >
  What actually happened?
result: pass | fail | ambiguous
artifacts_produced:
  - path/to/output
domain_interpretation: >
  What does the result mean in project/domain terms?
surprises:
  - surprise or none
follow_up:
  requirement_candidate: path/to/experiment-requirement-candidate.md | none
  risk: risk-id | none
  defect: issue-or-backlog-id | none
  lesson: path/to/lesson.md | none
human_review_state: proposed | accepted | rejected | needs_more_evidence
```

## Use When

- Deterministic checks pass but the behavior still needs domain proof.
- A simulation/playtest can reveal unintended consequences.
- A corpus probe can show whether a detector generalizes across real sources.
- A generated report must be judged for usefulness and failure modes.
- A hypothesis must be falsified before it becomes a product claim.
