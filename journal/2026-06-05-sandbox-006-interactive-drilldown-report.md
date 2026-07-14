# 2026-06-05 — Sandbox 006 Interactive Drill-Down Report

## Summary

Opened Sandbox 006 to explore the expert drill-down report as an interactive product surface.

The owner clarified that "drill-down report" means an interactive report/workbench that is pleasant to inspect and work with, not just a generated static memo. The review artifact can still be static HTML; the sandbox should not build hosted infrastructure.

## What Changed

- Created `sandboxes/006-interactive-drilldown-report/README.md`.
- Created `sandboxes/006-interactive-drilldown-report/STAGE-PLAN.md`.
- Created `sandboxes/006-interactive-drilldown-report/stages/001-ux-concept/STAGE.md`.
- Created `sandboxes/006-interactive-drilldown-report/PLAYBOOK.md`.
- Added Sandbox 006 to `sandboxes/README.md`.
- Added Sandbox 006 to `AGENT_CONTEXT.json` as an active project thread.

## Decision Context

Sandbox 004 proved the drill-down content model and report-generation path. Sandbox 006 is separate because it asks a UX question:

> What should the expert drill-down report feel like when a human reviews, filters, inspects, and acts on findings?

The sandbox explicitly allows Figma and Canva as design aids:

- Figma for interaction, layout, information architecture, component structure, and responsive frames.
- Canva for polished visual direction, stakeholder-facing mockups, branding, and presentation framing.
- Static HTML for local review and preserved interactive prototypes.

Figma and Canva are not sources of truth. Design learning that matters must be summarized in repo-visible Markdown.

The owner also clarified the intended tool pipeline:

1. Discuss functionality with Codex and optionally create a local behavior prototype.
2. Use static HTML for simple interactions or client-side Blazor when stateful interaction gets JavaScript-heavy.
3. Feed a tight Codex-written brief to Figma/Canva for visual and UX exploration.
4. Bring useful design learning back into repo-visible notes and local review artifacts.

## Constraints

- No hosted app.
- No backend.
- No database.
- No deployment layer.
- No replacement of Sandbox 004 evidence/report generation.
- Static HTML remains the preferred review artifact.

## Current State

Stage 001 is active. It records:

- UX concept,
- no-hosting constraint,
- Figma/Canva/static HTML roles,
- candidate navigation,
- finding anatomy,
- and design questions for the first prototype.

## Next Useful Work

Draft:

- a first-screen wireframe note,
- a finding-detail wireframe note,
- and a decision on whether Stage 002 should prototype from `drill_down_entries.json` or a smaller fixture.

## Validation

Ran focused `git diff --check` on the new sandbox docs, `sandboxes/README.md`, `AGENT_CONTEXT.json`, and this journal entry. It passed with only existing CRLF normalization warnings.

## Later Update: Stage 001 Closed, Stage 002 Started

Closed Stage 001 by making the UX concept concrete enough to prototype:

- defined primary reviewer workflows,
- added first-screen and finding-detail wireframe notes,
- specified internal vs sanitized evidence behavior,
- defined prototype reviewer status states,
- chose `drill_down_entries.json` as the first prototype data source,
- chose plain static HTML/CSS/JavaScript with no build tool for Stage 002.

Started Stage 002 and created the first local static workbench:

- added `sandboxes/006-interactive-drilldown-report/stages/002-static-html-prototype/STAGE.md`,
- added `sandboxes/006-interactive-drilldown-report/stages/002-static-html-prototype/src/build_workbench.py`,
- generated `sandboxes/006-interactive-drilldown-report/output/workbench.html`.

The first prototype includes portfolio metrics, filters, finding list, finding detail, internal/sanitized evidence mode, role tabs, reviewer status controls, source trace, and suggested-fix/disclaimer display.

Validation performed:

- generator wrote `workbench.html` with 3 entries,
- embedded JSON payload parsed successfully,
- extracted JavaScript passed `node --check`,
- focused `git diff --check` passed.

Validation not performed:

- in-app browser visual verification. Direct `file://` navigation was blocked by the browser URL policy. The prototype still needs a human local open or approved review path before Stage 002 is closed.

Next useful work:

- Owner can use Stage 003 to test the same concept in Figma and Canva.
- Compare design-tool output against `output/workbench.html`.
- Record which design choices should carry back into the HTML prototype and which should be rejected.
