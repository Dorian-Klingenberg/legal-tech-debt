# Task Contract Sketch

Status: Sketch

Purpose: define the minimum fields needed before an agent starts implementation.

## Template

```yaml
task_id: BACKLOG-000
title: Short imperative title
owner_or_agent: Codex | Claude Code | GitHub Copilot | human | mixed
origin: conversation | experiment | backlog | ADR | external_requirement | mixed
source_evidence:
  - path_or_reference: path/to/source.md
    note: Why this source matters
objective: >
  One paragraph describing what should be true when the task is complete.
scope:
  in:
    - File, module, behavior, or artifact in scope
  out:
    - Explicit non-goal
allowed_files:
  - path/or/glob
requirements_or_acceptance:
  - Requirement or acceptance criterion
gherkin_feature: path/to/feature.feature | none
risk_class: low | medium | high
validation_plan:
  deterministic:
    - command or check
  experimental:
    - probe or scenario, if needed
  semantic:
    - LLM-as-judge rubric, if justified
expected_evidence_bundle: path/to/evidence-bundle.md
human_approval:
  required: true | false
  reason: Why human approval is or is not needed
handoff_or_journal_required: true | false
```

## Notes

- `origin` is mandatory so the control surface can distinguish conversation-driven tasks from experiment-derived work.
- `source_evidence` should point to the conversation summary, journal, sandbox output, generated report, failing run, screenshot, or external requirement that justifies the task.
- Experimental validation is optional. Use it when tests alone cannot show domain behavior.
