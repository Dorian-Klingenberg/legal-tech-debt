# SDLC And Agentic Product Stack Separation

Date: 2026-06-05
Status: Planning note for Phase A and later architecture work

## Purpose

The project will eventually have two different technology stacks:

- Development SDLC stack: the engineering system used to plan, build, test, trace, release, govern, and maintain the product.
- Agentic product stack: the runtime system inside the product that ingests documents, retrieves evidence, runs detectors, drafts reports, and assists reviewers.

These stacks are related, but they must not collapse into one another.

Core principle:

> The SDLC stack builds and governs the product. The agentic stack is part of the product being governed.

## Separation Rules

### 1. Separate Architecture Surfaces

Keep separate architecture records for:

- product architecture
- agent runtime architecture
- SDLC/tooling architecture
- data/evidence architecture
- security/compliance architecture

Do not let "we use agents while developing" imply that those development agents are part of the product runtime.

### 2. Separate Requirements

Product requirements describe what the delivered product must do for users.

Examples:

- Every finding must include source text and provenance.
- Reviewer reports must distinguish candidate evidence from legal conclusions.
- Product agents must not leak customer corpus data across tenants.

SDLC requirements describe how the engineering process must produce trustworthy software.

Examples:

- Detector changes must run regression validation on preserved corpus runs.
- Requirements must trace to Gherkin scenarios and test evidence during Phase A.
- Release candidates must pass schema, provenance, and report-render validation gates.

### 3. Separate Validation

Product validation asks whether the product behavior is useful, traceable, and safe.

Examples:

- false positive / false negative review
- finding provenance review
- reviewer usefulness
- report correctness
- source traceability

SDLC validation asks whether engineering controls were followed.

Examples:

- unit and integration tests
- schema validation
- CI gates
- requirements traceability
- release readiness checks
- auditability of changes

### 4. Separate Agent Roles

Development agents help build the system:

- Codex
- Claude Code
- GitHub Copilot

Product agents are product components:

- ingestion assistant
- retrieval assistant
- reviewer assistant
- report drafter
- workflow assistant

Development agents may have repository access. Product agents should have constrained runtime permissions, explicit memory boundaries, logged tool calls, and customer-data isolation.

### 5. Separate Memory

Development memory lives in repo-visible project records:

- `BOOTSTRAP.md`
- `AGENT_CONTEXT.json`
- `AGENT_OPERATING_MODEL.md`
- `BACKLOG.md`
- ADRs
- handoffs
- top-level `journal/`

Product memory lives in product artifacts:

- source corpus records
- parser runs
- nodes and edges
- candidate evidence
- detector findings
- reviewer decisions
- report drafts
- product audit logs

Product behavior must never depend on private Codex, Claude, Copilot, or chat-session memory.

### 6. Separate Permissions

Development agents can be granted repository permissions appropriate to the current task.

Product agents should default to narrow runtime permissions:

- read approved tenant corpus
- write structured product artifacts
- call approved retrieval and analysis tools
- log evidence and decisions
- avoid arbitrary filesystem access
- avoid unapproved external network calls
- avoid cross-tenant memory

### 7. Separate ADR Streams Or Tags

During Phase A, use either separate ADR folders or explicit ADR scope tags.

Possible folders:

```text
adr/sdlc/
adr/product/
adr/agent-runtime/
adr/data-evidence/
adr/security/
```

Possible scope tags:

```text
Scope: SDLC
Scope: Product Agent Runtime
Scope: Evidence Substrate
Scope: Security / Governance
```

The important point is that an SDLC decision should not silently become a product-runtime decision, and a product-agent design should not silently alter engineering governance.

## Phase A Implications

Phase A should explicitly define:

- SDLC stack concept of operations
- product agent runtime concept of operations
- requirements traceability model
- Gherkin/BDD acceptance criteria strategy
- product evidence and audit-log model
- agent permission and memory model
- release and validation gates

## Checklist For Later

- [ ] Decide whether root ADRs should live in `adr/` folders or use root-level project ADR files.
- [ ] Draft SDLC stack plan.
- [ ] Draft product agent runtime stack plan.
- [ ] Define requirements categories: product, SDLC, data/evidence, security, agent runtime.
- [ ] Define traceability between requirements, Gherkin scenarios, tests, and evidence artifacts.
- [ ] Define product-agent permission model.
- [ ] Define development-agent permission model.
- [ ] Define audit-log requirements for product agent actions.
- [ ] Define customer/tenant memory boundaries for product runtime.
