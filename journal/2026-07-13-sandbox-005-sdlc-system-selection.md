# 2026-07-13 Sandbox 005 SDLC System Selection

## Session Summary

Resumed Sandbox 005 and compared the current Agile V organization projects,
SwarmForge, and Codex CLI as candidate systems for the Legal Tech Debt
development lifecycle.

The comparison found that they are complementary rather than direct
alternatives:

- Agile V supplies lifecycle assurance concepts and a broad scaffold.
- SwarmForge supplies local multi-agent worktree and handoff mechanics.
- Codex CLI supplies the first practical agent execution and automation layer.
- The repository already contains the project-specific control model that must
  remain canonical, including experiment-derived requirements and
  experiment-backed V&V.

Stage 001 is now complete with a provisional hybrid. Stage 002 is ready but has
not started.

## Research Performed

### Agile V

Reviewed the `Agile-V` organization, including:

- `Agile-V/agile_v_skills` at tag `v3.6.0`, commit
  `a7ae1994ee03f2ff3a7a5986e7c9e5fc71e743f1`;
- `Agile-V/agentic_agile_v` main at commit
  `54eaa5451fcbfe9fa1c59355584deddbf7cef342`;
- task and evidence schemas;
- risk policy and quality-gate workflow;
- repository structure, tests, status claims, releases, tags, license, and
  recent GitHub Actions results.

In a clean WSL temporary clone of `agentic_agile_v`:

- `pytest -q` produced 366 passed and 7 warnings;
- `ruff check src tests` passed;
- `ruff format --check src tests` passed;
- `mypy src` passed;
- whole-package coverage was 44%.

The research also found:

- the README calls the OpenHands path an MVP with phases 0-4 of 12 complete;
- other documents use broader production-ready language;
- the repo-level license is CC BY-SA 4.0 while `pyproject.toml` says MIT;
- five scripts named by the risk policy are absent from `scripts/`;
- the main quality-gate workflow passed, while daily OpenWiki update runs were
  failing on July 9-13.

### SwarmForge

Reviewed `unclebob/swarm-forge`:

- main commit `9acd54d2239fef7e41ddacd8fd30dfb0e69672fe`;
- two-pack, four-pack, six-pack, and adversaries branch heads;
- main scripts, constitution articles, handoff protocol, terminal adapters,
  and tests;
- four-pack topology and role prompts.

Useful mechanics include per-role worktrees, compact commit handoffs,
backend-per-role configuration, and role packs of different sizes.

Current concerns include no detected license, no GitHub Actions workflow, no
requirements/evidence model, unpinned startup procurement in shared role rules,
and defaults centered on Gherkin mutation plus Go/Clojure/Java tooling. The
current WSL environment has Git and tmux but lacks `zsh` and Babashka, so the 24
declared Clojure tests were inspected but not executed.

### Codex CLI

Used the current official Codex manual and CLI documentation to verify:

- custom project agents;
- built-in subagents in the CLI;
- default one-level subagent nesting;
- sandbox and approval controls;
- `codex review`;
- JSONL event output;
- schema-constrained final output from `codex exec`;
- `AGENTS.md` instruction discovery.

Local checks found:

- Windows Codex CLI is installed at version `0.130.0-alpha.5`;
- WSL resolves an inaccessible Windows application path instead of a native
  WSL executable.

No Codex installation or environment configuration was changed in this
session.

## What Changed

- Added
  `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/SDLC-SYSTEM-SELECTION-STUDY.md`.
- Added
  `sandboxes/005-agentic-sdlc-project-manager/stages/002-manual-pilot/STAGE.md`.
- Added `sandboxes/005-agentic-sdlc-project-manager/HANDOFF-2026-07-13.md`.
- Added
  `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/LESSON.md`.
- Updated `sandboxes/005-agentic-sdlc-project-manager/README.md` with the
  provisional selection.
- Updated `sandboxes/005-agentic-sdlc-project-manager/STAGE-PLAN.md` to close
  Stage 001 and make Stage 002 ready.
- Updated
  `sandboxes/005-agentic-sdlc-project-manager/stages/001-stack-concept/STAGE.md`
  with the role set and selection outcome.
- Updated `sandboxes/README.md` so the sandbox index reflects current status.
- Updated `AGENT_CONTEXT.json` so Sandbox 005 is the active sandbox and the
  Stage 002 pilot is the next priority.

## Decisions Made

- Keep the existing repository artifacts as canonical project truth.
- Use selected Agile V concepts, independently authored for this project,
  rather than installing the complete skills library or scaffold.
- Use Codex CLI as the first execution engine.
- Start with lead/specifier, implementer, and fresh-context verifier roles;
  keep researcher optional.
- Use one implementation writer and manual Git worktrees in Stage 002.
- Keep Gherkin conditional on stable user-visible behavior.
- Defer executable SwarmForge adoption to Stage 004.
- Select `S005-PILOT-001`: a synthetic-demo manifest schema, valid fixture,
  invalid fixture, validator, and focused tests. The corpus itself remains out
  of scope for the pilot.
- Do not write an ADR yet. The selection remains provisional until pilot
  evidence exists.

## Licensing And Reuse Boundary

No upstream code, schemas, or role prompts were copied into this repository.

- Agile V's repo-level CC BY-SA 4.0 license conflicts with the scaffold
  package's MIT declaration.
- SwarmForge has no detected license grant at the reviewed commit.

The study uses primary-source facts and independently describes concepts. Any
future code or prompt adoption requires a new license check or permission.

## Validation Performed

- [x] Validated `AGENT_CONTEXT.json` with `python3 -m json.tool`.
- [x] Ran `git diff --check` on the tracked files touched in this session.
- [x] Checked nine touched Markdown files; all relative links resolve.
- [x] Checked all touched files for trailing whitespace; none was found.
- [x] Reviewed the focused diff and status without disturbing unrelated changes.

## Current State

Stage 001 is complete. Stage 002 is ready, not active. No dashboard,
orchestration runtime, production infrastructure, product runtime agent, or
customer-data path was added.

The repository remains heavily dirty from pre-existing user and generated
changes. The Stage 002 preflight explicitly forbids using that dirty root as a
coordinator workspace.

## What Comes Next

- [ ] Isolate or commit the current working state before pilot worktrees are
      created.
- [ ] Install and smoke-test the official Codex CLI natively in WSL.
- [ ] Create project-neutral role prompts and thin Codex adapters.
- [ ] Run `S005-PILOT-001` manually and measure both benefit and ceremony.
- [ ] Update the artifact contract only from pilot evidence.
- [ ] Evaluate SwarmForge separately in Stage 004 after licensing,
      prerequisites, tests, and tool pinning are addressed.
