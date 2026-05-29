# Sandbox 001 Closure

Closed: 2026-05-29
Status: Complete as foundational research

## Decision

Sandbox 001 is complete. It should now be treated as a preserved foundation, not the active forward-development lane.

Future insurance policy and claims work should continue in `sandboxes/002-claims-regulatory-automation` unless the explicit task is to revisit a primitive from 001.

## Why We Are Closing 001

Sandbox 001 answered its original research question well enough for the project to move on:

> How far can lightweight parsing plus graph/matrix checks get before heavier tools are needed?

The answer is:

- far enough to extract useful section anchors and references from small corpora
- far enough to detect intentional structural defects
- far enough to produce reviewable JSON, Markdown, CSV, and static dashboard evidence
- far enough to show that plain graph reachability becomes semantically noisy on richer insurance-like text
- not far enough to justify production infrastructure, graph databases, external NLP stacks, or live regulatory feeds at this stage

The later project research has also narrowed the product direction. The highest-value lane is now insurance policy and claims legal tech debt, especially high-cost smells such as broken/null references, calculation rule drift, coverage inversion, magic-number terms, non-deterministic language, and regulatory drift in claim handling.

That domain focus belongs in Sandbox 002.

## What 001 Proved

The sandbox produced a working plain-Python probe that can:

- extract section anchors from Markdown corpora
- extract internal section references
- represent references as graph edges
- detect dangling references
- detect simple circular references
- detect orphan definitions
- detect unversioned external authorities
- emit `findings.json` and `report.md`
- emit `section_index.csv`, `adjacency_matrix.csv`, `two_hop_matrix.csv`, `transitive_closure.csv`, and `dependency_roots.json`
- drive a static dashboard with graph, matrix, findings, and drill-down views

The staged workflow also worked. Stages 001 through 004 captured experiments, outputs, lessons, and next questions clearly enough for later agents to reconstruct the project state.

## What 001 Taught

The major lesson is that a reference is not yet a relationship.

The Kentucky-style fixture in Stage 003 made the graph large enough to expose the weakness of plain reachability. Stage 004 showed that legal dependency paths need typed edge semantics before matrix closure can be trusted as legal/compliance meaning.

Stage 004 should be preserved as a useful semantic study, but it should not block Sandbox 002. Typed matrices should return only when a concrete insurance detector needs them.

## What Carries Forward to 002

Carry these forward:

- plain-Python probe structure
- Markdown corpus layout
- section/reference extraction patterns
- dangling/null-reference detector concept
- graph edge list representation
- matrix output pattern where it helps explain impact
- static HTML dashboard pattern
- JSON/CSV/Markdown evidence outputs
- staged experiment workflow
- lesson-documentation style
- typed-edge concept as a review aid
- human-review framing

Adapt these for insurance:

- finding schema
- severity language
- detector names
- edge types
- dashboard labels and workflows
- corpus fixtures

## What Does Not Carry Forward Yet

Do not carry these forward as mandatory architecture:

- graph databases
- live regulatory feed ingestion
- containers or deployment infrastructure
- PAS integration
- LLM extraction pipelines
- full typed-matrix implementation
- production citation parsing

Those may become useful later, but 002 should earn each dependency through a concrete insurance policy or claims experiment.

## Final State

001 remains valuable as evidence, reference code, and method. It is no longer the main place to add new product-facing work.

The active project lane is now:

> Sandbox 002: insurance policy and claims legal tech debt experiments using the proven 001 primitives where they help.
