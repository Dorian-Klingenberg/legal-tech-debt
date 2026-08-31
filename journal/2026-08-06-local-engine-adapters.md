# 2026-08-06 — Local Engine Integration Adapters

## Session Summary

After completing the local engine, added the requested direct Codex and future
agent/deployment surfaces as thin adapters around the tested Python contract.

## What Changed

- Created and forward-tested the repo-visible `local-legal-smell-review` skill.
- Registered the skill as active in `skills/registry.csv`.
- Added an optional MCP FastMCP adapter exposing `review_legal_smells`.
- Added an optional Azure Functions HTTP adapter.
- Added an Azure Functions Python v2 `function_app.py` scaffold and
  `requirements.txt`.
- Added Microsoft Foundry integration guidance through MCP or HTTP.
- Added Sandbox 008 Stage 002 documentation.
- Created ADR-003 with adapter decisions, sources, and follow-up gates.

## Validation

- Skill validator passed.
- Forward-test reviewed the synthetic positive fixture without editing files.
- Local engine and adapter tests passed: 7 tests.
- Azure host entrypoint syntax parsed locally; Azure Functions runtime was not installed.
- MCP SDK installation/live transport was not run.
- Azure Functions Core Tools and a real Foundry connection were not run.
- No cloud resource or hosted endpoint was created.

## Current State

- [x] Local Python API and CLI.
- [x] Five deterministic detector families.
- [x] JSONL and Markdown outputs.
- [x] Repo-visible Codex skill.
- [x] Optional MCP and Azure adapters.
- [x] Foundry integration guidance.
- [x] ADR-003 created.
- [ ] Calibrate generic S1/S2 count deltas against Stage 006.
- [ ] Validate live MCP, Azure Functions, and Foundry surfaces in an explicitly
      authorized deployment experiment.
