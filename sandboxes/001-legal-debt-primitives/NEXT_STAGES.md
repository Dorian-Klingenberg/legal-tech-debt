# Candidate Next Stages

## Completed: 002 Dashboard Mockup

Question answered:

Can the current demo output drive a static dashboard/data drill-down mockup?

Result:

Yes. `stages/002-dashboard-mockup/dashboard.html` embeds the demo output and presents graph, matrix, findings, and drill-down views.

## Completed: 003 Kentucky Insurance Sample

Question answered:

Can the dashboard and matrix outputs handle a larger, more realistic synthetic insurance corpus?

Result:

Yes. `stages/003-kentucky-insurance-sample` contains 60 extracted sections, 197 references, 65 matrix nodes, and a regenerated static dashboard with data-driven graph lanes.

## Active: 004 Typed Edge Study

Question:

Can plain references be classified into edge types so reachability becomes legally meaningful?

Current framework:

- edge taxonomy
- hand-labeling guide
- seed labeling queue
- typed reachability plan
- daily journal entry

## 005: Typed Matrix Prototype

Question:

Can we turn hand-labeled edge types into typed adjacency matrices and typed witness paths?

Evidence to capture:

- one matrix per relationship type
- typed reachability rules
- path examples that plain closure includes but typed closure excludes
- dashboard witness paths annotated with edge types
- lesson on why a legal dependency path needs semantics, not only connectivity

## 006: Matrix Performance Lab

Question:

How much speed can we get from matrix representations before using a graph database or external numerical stack?

Possible progression:

- pure Python list-of-lists boolean multiplication
- optimized Python loops over active columns
- row-as-bitset representation using Python integers
- sparse edge-list multiplication
- optional NumPy/SciPy comparison
- typed-edge matrix composition

Evidence to capture:

- runtime by node count and edge density
- memory use by representation
- correctness compared with baseline closure
- where the implementation becomes too clever to maintain
- lesson on why matrix multiplication speed depends on representation, memory layout, and sparsity

## 007: Edge Type Extraction

Question:

Can relationship types be inferred from source text, or do they require human review?

Possible signal types:

- verbs such as implements, verifies, retains, routes, reopens
- source/target document classes
- missing-target language such as stale, obsolete, retired, legacy
- workflow phrases such as move to, return to, escalate, consult
- evidence phrases such as record, packet, archive, proof

Evidence to capture:

- deterministic extraction rules
- ambiguous examples needing SME review
- precision/recall notes against the hand-labeled seed set
- lesson on why automated semantics needs a review loop

## 008: SME Review Workflow

Question:

What does a legal/compliance reviewer need in order to accept, reject, or annotate a finding?

Evidence to capture:

- finding schema
- review state machine
- reviewer comments
- false-positive categories
- evidence snippets and source anchors
- lesson on why legal meaning requires human review even when structural evidence is machine-generated
