# GitHub Copilot Instructions

This repository uses shared cross-agent project memory.

Before suggesting or making changes, read `BOOTSTRAP.md` and follow its startup contract. Do not rely on Copilot-only context; project memory must remain visible to Codex, Claude Code, and future agents.

Key reminders:

- Current work is sandbox proof-of-concept development and experimentation.
- Prefer quick, clean, readable implementations over infrastructure.
- Read the relevant project and sandbox documentation before starting work.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- For Sandbox 002 corpus work, read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`, `sandboxes/002-claims-regulatory-automation/corpus/_download_manifest.csv`, and `sandboxes/002-claims-regulatory-automation/corpus/KNOWN-GAPS.md` before procuring or assuming missing sources.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal and handoff records so Codex, Claude Code, GitHub Copilot, and future agents inherit the same project state.
- Preserve the numbered sandbox stage workflow and document lessons.
