# Roadmap: Sandbox 002 Kentucky Homeowners Policy-Layer Smells

Version: 3.0
Status: Active roadmap
Controlling scope: `002-five-policy-layer-phish.md`

## Current Scope

Sandbox 002 is focused on Kentucky homeowners insurance and the five policy-layer smells documented in `002-five-policy-layer-phish.md`.

The active smells are:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

Do not pursue personal auto, motor vehicle, no-fault, PIP, broad claims platforms, live regulatory feeds, PAS integration, or production infrastructure unless the user explicitly reopens that scope.

## Stage 001: Foundation Import

Status: Complete bridge stage
Location: `stages/001-foundation-import`

Purpose:

- import the useful Sandbox 001 probe shape
- confirm it runs against a tiny homeowners-oriented fixture
- preserve the fast local workflow for later stages

What it proves:

- plain Python is enough for the current sandbox style
- Markdown fixtures and JSON/Markdown/CSV outputs are reviewable
- section/reference extraction remains useful as a supporting primitive

What it does not prove:

- it does not implement the five active homeowners smells
- it does not validate real Kentucky filings
- it does not justify infrastructure

## Stage 002: Homeowners Five-Smell Fixture

Status: Next recommended stage
Suggested location: `stages/002-homeowners-policy-layer-smells`

Objective:

Build one small Kentucky homeowners fixture that contains realistic examples for all five policy-layer smells.

Inputs:

- selected Kentucky homeowners source excerpts from `corpus/_download_manifest.csv`
- known source gaps from `corpus/KNOWN-GAPS.md`
- a source manifest with access dates, URLs, filing metadata, and effective dates where available
- synthetic defect copies that preserve source traceability without treating fixtures as legal advice

Deliverables:

- `data/raw/` for untouched source files or source notes
- `data/processed/corpus/` for cleaned Markdown excerpts
- `data/processed/source_manifest.csv`
- one fixture example per active smell
- one lightweight ROI note per fixture example, using `002-ROI-CASES-FIVE-SMELLS.md`
- `STAGE.md` documenting scope and limitations
- `LESSON.md` documenting what the fixture taught

Success criteria:

- every active smell has at least one reviewable fixture example
- every fixture example can be traced to a source or clearly marked synthetic seed
- every fixture example identifies the relevant cost pool and reviewer question
- no auto/no-fault/PIP material is included except as explicitly noted homeowners context
- manual SERFF gaps are not chased unless a fixture cannot be supported from the current corpus
- the stage remains runnable and understandable on a laptop

## Stage 003: Deterministic Pattern Detectors

Status: Planned

Objective:

Adapt the imported probe into lightweight detectors for the five active smells.

Detector approach:

- regex and phrase lists for known trigger language
- simple section and endorsement indexing
- simple reference/citation checks
- small clause relationship graph where it helps coverage inversion
- no heavy NLP unless a detector cannot be made useful without it

Expected outputs:

- `output/findings.json`
- `output/report.md`
- `output/section_index.csv`
- optional matrix outputs only when they explain a smell

Success criteria:

- the probe flags at least one fixture example for each active smell
- findings include location, smell type, evidence text, cost pool, why it matters, and reviewer questions
- false-positive limitations are explicit
- the code stays small enough for future agents to read quickly

## Stage 004: Reviewer Report

Status: Planned

Objective:

Turn detector output into a practical review artifact for a policy, claims, compliance, or product reviewer.

Deliverables:

- smell-by-smell summary
- source traceability
- concise reviewer questions
- explicit non-legal-advice limitation
- list of missing sources or human-review blockers

Success criteria:

- a reviewer can understand why each finding was flagged without reading the code
- the report distinguishes detected text risk from legal conclusions
- the report makes clear which findings need human review

## Stage 005: Optional Visual Drill-Down

Status: Parked until the report earns it

Objective:

Create a static, local visual drill-down only if Stage 004 shows that a visual surface would make the findings easier to review.

Allowed if earned:

- static HTML generated from local outputs
- simple tables and links from findings to source excerpts
- no server, database, scheduled job, or product shell

## Parked Work

These ideas may be useful later, but they are not part of active Sandbox 002 work:

- live statute or regulatory feed ingestion
- Neo4j or other graph database
- Docker or deployment packaging
- PAS or claim system integration
- broad claim decision audit trails
- multi-carrier pilots
- production citation validation
- LLM extraction pipelines
- go-to-market platform planning

## Decision Gate

Before adding any new tool, stage, or detector, ask:

> Does this directly help evaluate one of the five Kentucky homeowners policy-layer smells?

If the answer is no, leave it parked.
