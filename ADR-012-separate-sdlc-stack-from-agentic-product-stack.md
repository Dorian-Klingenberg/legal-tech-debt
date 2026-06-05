# ADR-012: Separate The Development SDLC Stack From The Agentic Product Stack

Date: 2026-06-05
Status: Accepted
Scope: Project architecture, Phase A planning, agent governance

## Context

The project uses multiple AI assistants during development, including Codex, Claude Code, and GitHub Copilot. The eventual product may also include agentic runtime components that ingest documents, retrieve evidence, run analysis, draft reports, or assist human reviewers.

Those are different systems.

The development SDLC stack is the engineering and governance environment used to create the product. The agentic product stack is part of the delivered product. If they are blurred together, the project risks confusing development convenience with product architecture, private assistant memory with product memory, and repository permissions with runtime permissions.

## Decision

Keep the development SDLC stack and the agentic product stack explicitly separate.

The accepted principle is:

> The SDLC stack builds and governs the product. The agentic stack is part of the product being governed.

Development agents may help build, test, review, and document the system. Product agents must be designed, permissioned, tested, logged, and governed as product components.

## Consequences

- Product-agent architecture must not rely on Codex, Claude, Copilot, or chat-session private memory.
- Product-agent memory must live in product artifacts such as corpus records, nodes, edges, candidate evidence, findings, reviewer decisions, reports, and audit logs.
- Development memory must remain repo-visible in startup docs, backlog, ADRs, journals, handoffs, and context files.
- SDLC requirements and product requirements must be written separately.
- SDLC validation and product validation must be measured separately.
- Runtime product agents need narrower permissions than development agents.
- Phase A should include separate concept-of-operations and requirements work for SDLC tooling and product agent runtime.

## Rejected Alternatives

### Treat all agent usage as one shared agent stack

Rejected because development assistants and product agents have different users, permissions, memory, audit requirements, and failure modes.

### Let development agent practices become product architecture by default

Rejected because repository workflow shortcuts are not necessarily acceptable runtime product behavior, especially for customer data, legal review, and auditability.

### Defer the distinction until implementation

Rejected because Phase A will need clear requirements boundaries. Recording the separation now prevents early planning artifacts from mixing SDLC governance with product runtime design.

## Follow-Up Checklist

- [ ] Create an SDLC stack plan during Phase A.
- [ ] Create an agentic product runtime stack plan during Phase A.
- [ ] Decide whether project-level ADRs should move into a root `adr/` directory.
- [ ] Define product-agent permission, memory, and audit-log requirements.
- [ ] Define development-agent permission and handoff requirements.
- [ ] Keep SDLC requirements separate from product runtime requirements.
- [ ] Keep SDLC validation separate from product behavior validation.

## Related Record

See `SDLC-AND-AGENTIC-PRODUCT-STACK-SEPARATION.md` for the longer planning note and checklist.
