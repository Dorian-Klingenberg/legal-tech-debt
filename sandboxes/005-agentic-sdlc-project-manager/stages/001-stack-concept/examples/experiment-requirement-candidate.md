# Experiment-To-Requirement Candidate Sketch

Status: Sketch

Purpose: capture a surprising or durable experiment observation before deciding whether it becomes a requirement, risk, backlog item, ADR candidate, lesson, or follow-up experiment.

## Template

```yaml
candidate_id: EXPREQ-000
source_experiment:
  path: path/to/experiment-or-output
  run_id: optional-run-id
  observed_at: 2026-06-07T00:00:00-04:00
observation_summary: >
  What happened in the experiment, prototype, playtest, corpus probe, generated
  report, or failed run?
why_it_matters: >
  Why is the observation durable enough to consider for project control?
affected_boundary:
  - product_behavior
  - SDLC_tooling
  - agent_runtime
  - evidence_substrate
  - UX
  - documentation
promotion_decision: requirement | risk | backlog_item | ADR_candidate | lesson | follow_up_experiment | no_promotion_yet
proposed_requirement_or_task: >
  If promoted, state the requirement or task in testable language.
validation_idea: >
  How would we confirm that the promoted requirement is satisfied?
risk_if_ignored: low | medium | high
human_approval_state: proposed | approved | rejected | needs_more_evidence
```

## Promotion Rule

Promote experiment evidence only when it identifies durable behavior, a repeatable risk, a missing capability, a validation need, or a product/design constraint.

Do not promote every interesting surprise. Some surprises should stay as journal notes, lessons, risk records, or follow-up experiments.
