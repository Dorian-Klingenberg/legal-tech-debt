# Legal Tech Debt Sandboxes

This folder holds small, disposable-but-documented experiments for exploring legal tech debt tooling before committing to a product architecture.

The intent is pre-phase A: learn quickly, capture evidence, and separate what existing technology can already do from what likely needs original engineering.

For shared agent startup instructions, read [../BOOTSTRAP.md](../BOOTSTRAP.md) before beginning work in any sandbox.

## Sandbox Index

| Sandbox | Purpose | Status |
|---|---|---|
| [001-legal-debt-primitives](001-legal-debt-primitives/README.md) | Test basic legal debt detection primitives: citation extraction, dangling references, orphan definitions, circular references, unversioned external authorities, and dependency matrix closure. | Complete; preserved as foundation |
| [002-claims-regulatory-automation](002-claims-regulatory-automation/002-claims-regulatory-automation-README.md) | Apply legal tech debt detection to high-value insurance policy and claims smells using the useful 001 primitives where they fit. | Active |

## Working Rules

- Keep each sandbox independently runnable.
- Prefer tiny sample corpora before real legal data.
- Record assumptions, surprises, and failure modes as findings.
- Treat scripts as probes, not production architecture.
- Promote only proven patterns into future shared tooling.
- Snapshot working states as numbered stages before trying the next idea.
- Keep proof-of-concept work quick, clean, readable, and understandable.
- Do not introduce infrastructure unless a sandbox stage explicitly exists to evaluate it.
