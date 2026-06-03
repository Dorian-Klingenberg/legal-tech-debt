# Agent Instructions

This repository uses shared cross-agent project memory.

Before doing any work, read `BOOTSTRAP.md` and follow its startup contract. These instructions apply to Codex and to any general coding agent that reads `AGENTS.md`.

Key reminders:

- The user uses Codex, GitHub Copilot, and Claude Code. Durable memory must be visible to all of them.
- This is currently sandbox proof-of-concept work, not infrastructure work.
- Read the relevant project and sandbox documentation before starting changes.
- For Sandbox 002, align active work to the five Kentucky homeowners policy-layer smells in `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`.
- Current Sandbox 002 path: build Stage 002 discovery-and-instrumentation before detector findings. Emit parser diagnostics, legal nodes, citations, broader references, conservative graph edges, retrieval bundles, and candidate evidence first.
- Defer vector infrastructure, but design the evidence substrate as if hybrid retrieval will eventually exist. Treat parser/reference uncertainty as part of the evidence layer.
- Stage 002 JSON/JSONL artifacts should carry schema version, run identity, creation timestamp, and stable source/node IDs under a fixed parsing strategy.
- For Sandbox 002 corpus work, read `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`, `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`, and `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` before procuring or assuming missing sources.
- For Sandbox 002 RAG parser/model work, read `skills/legal-rag-builder/references/docling-local-stack-boundary.md`; Docling is a parser/enrichment adapter, not a vector database or verified general local LLM runtime.
- Treat manual SERFF sources as known gaps, not automatic blockers. Chase them only when an active experiment needs them.
- At major pause points, update shared journal, handoff, lesson, and context records so all future agents inherit the current state. Use `skills/project-memory-artifacts/SKILL.md` for that workflow.
- For project skill work, read `skills/README.md`, `skills/SKILL-DEVELOPMENT.md`, and `skills/registry.csv`. Skills must remain visible to Codex, GitHub Copilot, and Claude Code, not only installed into one assistant's private skill store.
- Keep experiments quick, clean, readable, and well documented.
- Before starting substantive work, read `SECRET_SCAN_REPORT.md` if it exists and remind the user to review or resolve any open secret-scan findings.

