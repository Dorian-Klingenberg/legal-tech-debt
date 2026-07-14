# Sandbox 006 Stage Plan

Status: Current secondary plan; paused at the Stage 002 human review gate
Last updated: 2026-07-13

## Sandbox Goal

Explore the expert drill-down report as an interactive static report/workbench.

The purpose is to learn how a human should inspect and act on findings, not to build hosted infrastructure.

## Stage 001: UX Concept And Design Tool Plan

Status: Complete

Purpose:

Define the interactive report concept, information architecture, and the role of Figma/Canva/static HTML.

Checklist:

- [x] Create Sandbox 006.
- [x] State the no-hosted-anything constraint.
- [x] Separate Sandbox 006 UX exploration from Sandbox 004 report generation.
- [x] Define Figma, Canva, and static HTML roles.
- [x] Add a focused Figma/Canva evaluation brief.
- [x] Add Sandbox 006 playbook for Codex/Figma/Canva/static-or-Blazor iteration.
- [x] Add first concept note from latest Sandbox 004 drill-down reports.
- [x] Identify primary user workflows.
- [x] Define the first-screen information architecture.
- [x] Define finding detail/drill-down anatomy.
- [x] Define internal vs sanitized mode behavior.
- [x] Define reviewer workflow states.
- [x] Define the design questions to test in Figma.
- [x] Define the design questions to test in Canva.
- [x] Define what must be proven in static HTML.

Expected outputs:

- `stages/001-ux-concept/STAGE.md`
- Optional wireframe notes or exported design references.
- A decision about whether to build a Stage 002 static prototype.

## Stage 002: Static HTML Prototype

Status: Implemented; visual and responsive review pending

Purpose:

Build a local static HTML prototype using real or representative Sandbox 004 drill-down data.

Checklist:

- [x] Pick the input data file and variant: `drill_down_entries.json`, combined/internal-first.
- [x] Build a static HTML prototype with no backend.
- [x] Include navigation, filters, and finding detail.
- [x] Include evidence/limitation presentation.
- [x] Include internal/sanitized mode if feasible.
- [x] Add reviewer status controls.
- [ ] Include responsive layout checks.
- [ ] Verify the prototype opens locally.
- [ ] Capture screenshots or notes from review.

Gate:

Do not add a dev server, database, API, or deployment layer.

## Stage 003: Design Tool Comparison

Status: Planned
Document: `stages/003-design-tool-comparison/STAGE.md`

Purpose:

Evaluate what Figma and Canva actually help with.

Checklist:

- [ ] Create or import one Figma frame/wireframe for the report workbench.
- [ ] Create or import one Canva visual direction or stakeholder-facing mockup.
- [ ] Compare against the static HTML prototype.
- [ ] Record which tool improved clarity, speed, polish, or stakeholder communication.
- [ ] Record which tool created friction or duplicate-truth risk.
- [ ] Decide whether either tool belongs in the normal workflow.

Gate:

Design-tool output must be summarized in repo-visible Markdown. Do not rely on private design-tool memory.

## Stage 004: UX Review And Carry-Forward

Status: Planned
Document: `stages/004-ux-review-carry-forward/STAGE.md`

Purpose:

Decide what UX patterns should carry forward into product planning or Sandbox 004 report generation.

Checklist:

- [ ] Review prototype with the owner.
- [ ] List accepted interaction patterns.
- [ ] List rejected interaction patterns.
- [ ] Identify content-model changes needed in Sandbox 004 data.
- [ ] Identify report-generation changes, if any.
- [ ] Decide whether to close Sandbox 006 or continue with a second prototype.
