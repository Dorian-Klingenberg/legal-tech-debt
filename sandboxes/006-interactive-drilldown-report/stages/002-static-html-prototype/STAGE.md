# Stage 002: Static HTML Prototype

Status: Implemented; paused at human visual/responsive review gate
Started: 2026-06-05

## Purpose

Build the first local static HTML workbench for the interactive drill-down report concept.

This stage tests whether real Sandbox 004 drill-down data can support a useful review interaction without a backend, hosted surface, database, build tool, or Blazor project.

## Input

Primary input:

- `sandboxes/004-expert-drilldown/data/drill_down_entries.json`

Secondary input, not yet required:

- `sandboxes/004-expert-drilldown/data/case_library.json`

## Output

Generated review artifact:

- `sandboxes/006-interactive-drilldown-report/output/workbench.html`

Generator:

- `sandboxes/006-interactive-drilldown-report/stages/002-static-html-prototype/src/build_workbench.py`

## Prototype Scope

Included:

- portfolio metrics,
- carrier, smell, severity, status, and search filters,
- persistent-on-screen finding list,
- selected finding detail,
- internal vs sanitized evidence toggle,
- role tabs,
- local reviewer status control,
- source trace and limitation/disclaimer panel.

Not included:

- persisted reviewer status,
- case/dollar-anchor panels,
- Figma or Canva design import,
- Blazor component model,
- backend API,
- hosted deployment.

## Stage 002 Checklist

- [x] Pick the input data file and variant: `drill_down_entries.json`, combined/internal-first.
- [x] Use plain static HTML/CSS/JavaScript with no build tool.
- [x] Create a generator so the HTML can be refreshed from the real data.
- [x] Include navigation, filters, and finding detail.
- [x] Include evidence/limitation presentation.
- [x] Include internal/sanitized mode.
- [x] Include reviewer workflow states.
- [ ] Include responsive layout checks.
- [ ] Verify the prototype opens locally.
- [ ] Capture screenshots or review notes.

## Validation Notes

Completed on 2026-06-05:

- Generator ran successfully and wrote `output/workbench.html` with 3 entries.
- Embedded JSON payload parsed successfully from the generated HTML.
- Extracted JavaScript passed `node --check`.
- `git diff --check` passed for the Stage 001/002 files and generated HTML.

Not completed:

- In-app browser visual verification. Direct `file://` navigation to the generated HTML was blocked by the browser URL policy. Do not treat this as a prototype failure; the next human or agent should open the local file directly or use an approved local-review path.

## Open Questions For Stage 003

- Does Figma produce a clearer split-pane or multi-panel layout than this first HTML pass?
- Can Canva improve professional polish without turning the workbench into a presentation deck?
- Should source trace be a bottom panel, right rail, drawer, or inline section?
- Should reviewer status sit near the finding title, suggested fix, or list row?
- Should sanitized mode be a whole-report mode or a per-section mode?
