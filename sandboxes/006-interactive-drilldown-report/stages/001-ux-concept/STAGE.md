# Stage 001: UX Concept And Design Tool Plan

Status: Complete
Started: 2026-06-05
Completed: 2026-06-05

## Purpose

Define the interactive report/workbench concept before building a prototype.

The owner clarified that "drill-down report" means an interactive report that is pleasant to inspect and work with, not only a generated static memo. The review artifact can still be static HTML; the important shift is from document output to product surface.

## Core Constraint

No hosted product work in this sandbox.

Allowed outputs:

- static HTML,
- local CSS/JS/assets,
- exported design images,
- Figma or Canva links/exports documented in Markdown,
- repo-visible UX notes.

Not allowed by default:

- backend service,
- database,
- authentication,
- deployment,
- cloud hosting,
- live ingestion,
- production dashboard architecture.

## Initial UX Hypothesis

The interactive drill-down report should be a workbench with three levels:

1. **Portfolio view:** what findings exist, how severe they are, and which carriers/smells/workflows they affect.
2. **Finding view:** one selected finding with evidence, reasoning, business impact, limitations, and suggested fix.
3. **Trace view:** source path, supporting nodes, cases, regulatory anchors, procurement/copyright limitations, and sanitized/internal presentation boundary.

## Candidate Navigation

- Carrier filter: all, KFBM, KNIC, future carrier labels.
- Smell filter: policy-layer smell category.
- Severity/confidence filter.
- Mode: internal evidence vs sanitized commercial view.
- Role tabs: executive, compliance, claims, product/forms, engineering/ops.
- Status controls: needs review, accepted, rejected, needs source, needs counsel.

## Candidate Finding Anatomy

Each finding detail view should include:

- headline,
- carrier/source context,
- severity/confidence,
- one-sentence product risk,
- evidence summary,
- sanitized/internal evidence toggle,
- why it matters,
- expected fix direction,
- source trace,
- known limitations,
- related cases or dollar anchors,
- reviewer decision/status.

## Primary Reviewer Workflows

The first prototype should support four reviewer workflows:

- **Triage the portfolio:** scan all findings, understand severity/confidence, and decide which issue deserves attention first.
- **Inspect one finding:** keep the finding list visible while reading gap statement, evidence summary, role analysis, and suggested fix.
- **Trace the source:** separate "what the report says" from "where it came from" by exposing source ID, section path, context, limitations, and case/dollar anchors.
- **Record review posture:** mark a finding as needs review, accepted, rejected, needs source, or needs counsel.

The prototype does not need persistent storage. Status controls can be local browser state only.

## First-Screen Wireframe

Use a dense workbench layout:

```text
+------------------------------------------------------------------------------+
| Header: Interactive Drill-Down Workbench                                      |
| Mode toggle: Internal / Sanitized                                             |
+-------------------------------+----------------------------------------------+
| Portfolio strip               | Filter bar                                   |
| - finding count               | carrier | smell | severity | confidence      |
| - severity/confidence summary | status | search                              |
+-------------------------------+----------------------------------------------+
| Finding list                  | Selected finding detail                      |
| - headline                    | - headline and badges                        |
| - carrier                     | - gap statement                              |
| - smell / heuristic           | - evidence summary                           |
| - severity/confidence         | - role tabs                                  |
| - status                      | - suggested fix/action                       |
|                               | - source trace / limitations panel           |
+-------------------------------+----------------------------------------------+
```

The finding list must remain visible while drilling down. The first screen should answer, "what exists, what is risky, and where should I click first?"

## Finding-Detail Wireframe

```text
+------------------------------------------------------------------------------+
| Finding headline                                  severity | confidence | mode |
+------------------------------------------------------------------------------+
| Gap statement                                                                 |
+-----------------------------------+------------------------------------------+
| Evidence summary                  | Reviewer status                          |
| Internal/sanitized mode note      | action priority / needs source / counsel |
+-----------------------------------+------------------------------------------+
| Role tabs: Executive | Compliance | Claims | Product/Forms | Ops              |
| - implication                                                                  |
| - risk / operational impact                                                    |
| - recommended action                                                           |
+------------------------------------------------------------------------------+
| Source trace / limitations / related cases                                     |
+------------------------------------------------------------------------------+
```

The role tab content should be short enough to scan. Source trace can be collapsible but should not be hidden behind decorative treatment.

## Internal vs Sanitized Behavior

- Internal mode may show verbatim evidence when present and should label that text as internal analysis material.
- Sanitized mode must prefer `paraphrased_evidence` and `paraphrased_context`.
- Sanitized mode should visibly warn that source trace remains available internally but commercial output should avoid carrier/ISO verbatim text.
- Switching modes should change evidence presentation without changing the selected finding.

## Reviewer Status States

Use these prototype states:

- needs review
- accepted
- rejected
- needs source
- needs counsel

These are workflow labels only. They are not legal conclusions and do not need persistence in Stage 002.

## Figma Evaluation Questions

- Does a side-nav plus detail panel work better than stacked cards?
- What should remain visible while drilling down?
- How dense can the workbench be before it feels exhausting?
- Which visual hierarchy best separates evidence, interpretation, and action?
- How should internal/sanitized mode switching appear?

## Canva Evaluation Questions

- What visual language makes this feel like a serious professional review artifact?
- Can Canva help produce a polished executive summary or cover/overview frame?
- Can Canva help explore branding without committing the HTML prototype to a final design system?
- Which presentation treatments should be copied into static HTML, and which are just slide-deck polish?

## Static HTML Proof Questions

- Can the experience be reviewed locally without hosting?
- Can real Sandbox 004 data drive the prototype?
- Can filters and drill-down interactions work with plain local JavaScript?
- Can internal vs sanitized mode stay clear?
- Can the report remain attractive without becoming a marketing page?

## Stage 002 Decision

Use `sandboxes/004-expert-drilldown/data/drill_down_entries.json` directly for the first prototype. Do not create a smaller hand-authored fixture unless the real data blocks implementation.

Use plain static HTML/CSS/JavaScript. Do not add a build tool, package manager, Blazor project, backend, or dev server for the first pass.

`case_library.json` is valid and may be loaded later for case/dollar-anchor panels, but it is not required for the first interaction proof.

## Stage 001 Checklist

- [x] Record UX concept.
- [x] Record no-hosting constraint.
- [x] Record Figma/Canva/static HTML roles.
- [x] Add `DESIGN-TOOL-EVALUATION.md` for a time-boxed Figma/Canva trial.
- [x] Add `PLAYBOOK.md` for the working loop and Blazor/static HTML decision rule.
- [x] Add `REPORT-CONCEPT.md` based on the latest Sandbox 004 drill-down reports.
- [x] Draft a first-screen wireframe note.
- [x] Draft one finding-detail wireframe note.
- [x] Decide whether to prototype from `drill_down_entries.json` or a smaller hand-authored fixture.
- [x] Decide whether Stage 002 should use plain HTML/CSS/JS or a tiny local build tool.
