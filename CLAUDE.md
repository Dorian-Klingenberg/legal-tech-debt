# Claude Code Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. Do not rely only on Claude-specific memory; project instructions must stay visible to Codex, GitHub Copilot, and other future agents too.

Key reminders:

- The current work is sandbox research and proof-of-concept experimentation.
- Avoid production infrastructure unless a stage explicitly evaluates it.
- Read the relevant project and sandbox documentation before starting.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- For Sandbox 002 corpus work, read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`, `sandboxes/002-claims-regulatory-automation/corpus/_download_manifest.csv`, and `sandboxes/002-claims-regulatory-automation/corpus/KNOWN-GAPS.md` before procuring or assuming missing sources.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal and handoff records so Codex, GitHub Copilot, Claude Code, and future agents inherit the same project state.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep outputs readable and document what each experiment teaches.
- Before starting substantive work, read `SECRET_SCAN_REPORT.md` if it exists and remind the user to review or resolve any open secret-scan findings.
