# Sandbox 006: Interactive Drill-Down Report

Status: Current secondary UX lane; paused at the Stage 002 human review gate
Started: 2026-06-05
Scope: Product UX, interactive report/workbench, static HTML review artifact

## Purpose

This sandbox explores what the expert drill-down report should feel like as an interactive product surface.

Sandbox 004 proved that the project can generate expert drill-down content: finding evidence, role-specific interpretation, suggested fixes, sanitization, and carrier-specific variants. Sandbox 006 asks a different question:

> What should a human actually work with when they review, filter, inspect, and act on those findings?

The output should remain local and reviewable. Do not build a hosted app, backend service, account system, deployment layer, or production dashboard. Static HTML, local assets, exported design frames, and repo-visible notes are enough.

## Relationship To Sandbox 004

Sandbox 004 is the content and report-generation proof of concept.

Sandbox 006 is the interaction and presentation proof of concept.

Use Sandbox 004 artifacts as input examples, especially:

- `sandboxes/004-expert-drilldown/data/drill_down_entries.json`
- `sandboxes/004-expert-drilldown/data/case_library.json`
- generated internal/sanitized HTML variants under `sandboxes/004-expert-drilldown/output/`

Do not rewrite Sandbox 004 unless a specific carry-back item is accepted.

## Scope

In scope:

- Interactive finding navigation.
- Filtering by carrier, smell, severity, confidence, status, and role.
- Evidence expansion/collapse.
- Internal vs sanitized presentation modes.
- Limitation and procurement-risk notes.
- Reviewer workflow states such as needs review, accepted, rejected, needs source, needs counsel.
- Role views for compliance, claims, product/forms, engineering/ops, and executive readers.
- Static HTML prototypes that can be opened locally.
- Figma and Canva exploration as design aids.

Out of scope:

- Hosted infrastructure.
- User accounts.
- Backend APIs.
- Databases.
- Live corpus ingestion.
- Production authentication or authorization.
- Replacing the Stage 004 evidence pipeline.
- Commercial distribution without copyright-safe sanitization.

## Design Tool Roles

### Figma

Use Figma for:

- layout and interaction prototyping,
- component structure,
- information architecture,
- visual hierarchy,
- state diagrams,
- responsive frame exploration,
- handoff notes for local static HTML.

Figma is not the source of truth for findings, evidence, or decisions. Any design learning that matters must be summarized in repo-visible Markdown.

### Canva

Use Canva for:

- polished visual direction,
- stakeholder-facing mockups,
- brand exploration,
- report cover/summary concepts,
- slide-style narrative framing,
- exportable images or visual treatments that can inform the static prototype.

Canva is not the implementation surface and not the canonical report data store. Use it when visual polish and presentation language are the question.

### Static HTML

Use static HTML for:

- reviewable interactive prototypes,
- local UX validation,
- preserved design snapshots,
- testing whether the experience works with real report data.

Static HTML is the preferred review artifact because it stays repo-visible, runnable without hosting, and close enough to product UI to expose workflow issues.

## UX Questions

- What is the first screen a reviewer should see?
- Should the primary unit be finding, carrier, smell, role, or risk?
- How should internal evidence differ from sanitized commercial output?
- How much legal/source detail should be visible by default?
- What does "drill down" mean in interaction terms: expand, compare, trace, annotate, or assign?
- What workflow states does a finding need?
- What should make a reviewer feel confident enough to act?
- What should make uncertainty impossible to miss?

## Success Criteria

- A human can quickly understand the portfolio of findings.
- A human can drill into one finding without losing orientation.
- Source limitations and confidence boundaries are visible.
- Internal/sanitized modes are clearly separated.
- The prototype feels like a workbench, not a static memo.
- The artifact is local, static, and reviewable.

## Starting Point

Stage 001 is complete. Stage 002 generated `output/workbench.html` and passed structural JavaScript/data checks. The next step is a human visual and responsive review; do not start Stage 003 design-tool comparison until that review identifies a question worth testing.

Use [PLAYBOOK.md](PLAYBOOK.md) for the agreed exploration loop: discuss functionality with Codex, optionally build static HTML or client-side Blazor for real interaction, use Figma/Canva for focused design passes, then bring useful design learning back into repo-visible notes and local artifacts.

Use [DOCUMENTATION-MAP.md](DOCUMENTATION-MAP.md) for the current reading order and [HANDOFF-2026-07-13.md](HANDOFF-2026-07-13.md) for the exact review gate.
