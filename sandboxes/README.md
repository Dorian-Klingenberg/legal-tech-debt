# Legal Tech Debt Sandboxes

This folder holds small, disposable-but-documented experiments for exploring legal tech debt tooling before committing to a product architecture.

The intent is pre-phase A: learn quickly, capture evidence, and separate what existing technology can already do from what likely needs original engineering.

For shared agent startup instructions, read [../BOOTSTRAP.md](../BOOTSTRAP.md) before beginning work in any sandbox.

## Sandbox Index

| Sandbox | Purpose | Status |
|---|---|---|
| [001-legal-debt-primitives](001-legal-debt-primitives/README.md) | Test basic legal debt detection primitives: citation extraction, dangling references, orphan definitions, circular references, unversioned external authorities, and dependency matrix closure. | Complete; preserved as foundation |
| [002-claims-regulatory-automation](002-claims-regulatory-automation/002-claims-regulatory-automation-README.md) | Apply legal tech debt detection to high-value Kentucky homeowners policy-layer smells using the useful 001 primitives where they fit. | Complete; preserved as evidence substrate |
| [003-findings-triage](003-findings-triage/003-STAGE-PLAN.md) | Turn Sandbox 002 structured findings into business-actionable triage, cross-carrier analysis, and executive-facing output. | Complete; sales instrument built and hardened |
| [004-expert-drilldown](004-expert-drilldown/README.md) | Build the expert drill-down report proof of concept: finding-level technical brief with evidence, role-specific analysis, and suggested fixes. | Complete; paid-service PoC preserved |
| [005-agentic-sdlc-project-manager](005-agentic-sdlc-project-manager/README.md) | Explore the development SDLC/project-manager stack: Agile V, Gherkin/BDD, Clean AI discipline, SwarmForge-style agent roles, verification evidence, and repo-native status surfaces. | Active; Stage 001 selection complete, Stage 002 pilot ready |
| [006-interactive-drilldown-report](006-interactive-drilldown-report/README.md) | Explore the expert drill-down report as an interactive static HTML workbench, with Figma/Canva used as design aids rather than hosted product infrastructure. | Stage 002 implemented; paused at human visual/responsive review gate |
| [007-policy-smell-detector-strategies](007-policy-smell-detector-strategies/README.md) | Develop detection strategies for five high-value policy-layer smells beyond the five operationalized Sandbox 002 smells. Build Phase 1 MVP detectors (Circular Definition, Rule Duplication, Hardcoded Jurisdiction Logic, Null Reference Clause) and Phase 2+ strategies leveraging Sandbox 002 graph architecture. | Active; Stage 001 complete, Phase 1 MVP ready for prototype implementation |

## Working Rules

- Keep each sandbox independently runnable.
- Prefer tiny sample corpora before real legal data.
- Record assumptions, surprises, and failure modes as findings.
- Treat scripts as probes, not production architecture.
- Promote only proven patterns into future shared tooling.
- Snapshot working states as numbered stages before trying the next idea.
- Keep proof-of-concept work quick, clean, readable, and understandable.
- Do not introduce infrastructure unless a sandbox stage explicitly exists to evaluate it.
