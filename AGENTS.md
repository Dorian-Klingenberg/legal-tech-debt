# Agent Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. These instructions apply to Codex and to any general coding agent that reads `AGENTS.md`.

Key reminders:

- The user uses Codex, GitHub Copilot, and Claude Code. Durable memory must be visible to all of them.
- This is currently sandbox proof-of-concept work, not infrastructure work.
- Read the relevant project and sandbox documentation before starting changes.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- For Sandbox 002 corpus work, read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`, `sandboxes/002-claims-regulatory-automation/corpus/_download_manifest.csv`, and `sandboxes/002-claims-regulatory-automation/corpus/KNOWN-GAPS.md` before procuring or assuming missing sources.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal and handoff records so all future agents inherit the current state.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep experiments quick, clean, readable, and well documented.
- Before starting substantive work, read `SECRET_SCAN_REPORT.md` if it exists and remind the user to review or resolve any open secret-scan findings.
