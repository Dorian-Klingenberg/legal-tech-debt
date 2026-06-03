# Legal RAG Phase Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-06-03
Path decision: `../../skills/legal-rag-builder/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
Artifact contract: `../../skills/legal-rag-builder/adr/ADR-004-schema-run-identity-and-id-stability.md`

## Phase 0: Document The Architecture

Status: In progress

Deliverables:

- `002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- `002-RAG-SUBSYSTEM-PLAN.md`
- `002-RAG-PHASE-PLAN.md`
- ADRs in `adr/`
- `skills/legal-rag-builder/SKILL.md`

Done when:

- future agents can see the intended build order
- RAG substrate boundaries are clear
- vector retrieval is preserved as expected later work without becoming premature infrastructure
- discovery-and-instrumentation is clearly the next implementation path

## Phase 1: File-Backed Discovery And Instrumentation

Question:

> Can selected Kentucky homeowners corpus files become legal-structure nodes with provenance, parser diagnostics, citations, broader references, conservative graph edges, candidate evidence, and retrieval bundles using local files only?

Suggested stage:

```text
stages/002-homeowners-discovery-instrumentation/
```

Inputs:

- small subset of `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- at least one HTML statute or regulation
- at least one DOI PDF
- one policy/rate/manual filing fragment where practical

Components:

- source registry
- parser adapters
- parser instrumentation
- normalized models
- structure-first segmenter
- citation/reference extractor
- graph builder
- candidate evidence scanner
- JSONL/CSV writers

Outputs:

- `schema/` JSON Schemas for every JSON/JSONL artifact type
- `data/heuristics.md`
- `output/run_manifest.json`
- `output/sources.jsonl`
- `output/parser_runs.jsonl`
- `output/blocks.jsonl`
- `output/block_stats.jsonl`
- `output/nodes.jsonl`
- `output/citations.jsonl`
- `output/references.jsonl`
- `output/edges.jsonl`
- `output/table_failures.jsonl`
- `output/parse_warnings.jsonl`
- `output/candidate_evidence.jsonl`
- `output/retrieval_bundles.json`
- `output/discovery_report.md`

Success criteria:

- all JSON/JSONL records carry schema version, run identity, and creation timestamp
- ID generation is deterministic under a fixed parsing strategy
- source provenance survives every transformation
- page or source location is retained where available
- parser uncertainty is visible
- section hierarchy is represented
- KRS and KAR references are extracted
- DOI, SERFF, form, endorsement, manual, current-guideline, and generic-law references are extracted separately from formal citations
- unresolved references are represented as visible targets
- graph edges are reviewable
- candidate evidence for the five active smells is emitted where the selected corpus supports it
- candidate evidence is not presented as final legal findings
- no manual reviewer annotations are written back into the Stage 002 substrate
- no cross-document topic modeling or cluster-level edges are created

## Phase 2: Retrieval Baseline And Fixture Curation

Question:

> Can exact phrase, lexical search, reference/citation signals, metadata filters, and graph expansion return useful evidence bundles and fixture examples for the five homeowners policy-layer smells?

Components:

- exact phrase search
- simple lexical scoring
- metadata filters
- parent/adjacent node expansion
- citation and authority expansion
- broader reference expansion
- retrieval bundle composer
- curated fixture examples

Outputs:

- `output/retrieval_bundles.json`
- `output/retrieval_report.md`
- `data/goldsets/goldset-002.1.json` or equivalent versioned gold set, created from Stage 002 outputs and real snippets only
- curated fixture excerpts or clearly marked synthetic seeds where needed

Success criteria:

- query results include why-retrieved reasons
- bundles include parent section and adjacent nodes
- citation/reference expansion includes cited authorities or unresolved records
- bundles include parser diagnostics or uncertainty when relevant
- bundles are usable by a detector or human reviewer without rereading the entire source
- every active smell has a candidate fixture example or a documented corpus limitation

## Phase 3: Tiny Gold Set And Retrieval Evaluation

Question:

> Which retrieval modes help on real legal/policy questions, and where does semantic retrieval add value?

Gold set:

- 10 statute/regulation sections
- 10 policy/manual clauses
- 5 endorsement or form fragments
- 5 rate/manual fragments

For each record:

- expected node boundaries
- citations present
- parent section
- 3-5 test queries
- expected relevant nodes

Compare:

- exact phrase
- lexical
- graph expansion
- semantic retrieval if embeddings are added
- hybrid retrieval if semantic retrieval proves useful

Success criteria:

- exact and lexical baselines are measured before embeddings
- semantic retrieval is evaluated against a known need
- false positives and missed hits are documented
- lexical under-recall is treated as expected evidence for later semantic evaluation, not as proof that the smell is absent

## Phase 4: Semantic Retrieval Experiment

Question:

> Do embeddings improve recall for homeowners policy-layer smell research enough to justify vector storage?

Build only after Phase 3 identifies queries where exact/lexical/graph retrieval is insufficient.

Possible first implementation:

- local embedding records attached to `Node`
- file-backed or lightweight local index
- no service dependency unless the experiment requires it

Evaluate semantic retrieval for:

- same concept with different wording
- broad exclusion language
- valuation and calculation terms
- coverage/exclusion contradictions
- regulatory mapping language

Success criteria:

- semantic retrieval improves gold-set recall or reviewer usefulness
- provenance and graph expansion remain intact
- embeddings do not replace structure-aware retrieval

## Phase 5: Retrieval Store Decision

Question:

> Which existing retrieval store best supports the proven workload?

Candidates:

- SQLite FTS5 for embedded lexical search and inspectable local experiments
- Qdrant for first-class dense/sparse hybrid retrieval experiments
- Postgres plus pgvector if relational joins, metadata, citations, and graph edges become the dominant need

Decision rule:

- choose Qdrant if hybrid vector retrieval quality is the core experiment
- choose Postgres plus pgvector if structured metadata and relational joins dominate
- stay file-backed or SQLite if the sandbox does not yet need a service

## Parked Until Earned

- chatbot interface
- production API
- background ingestion service
- live regulatory feeds
- graph database
- Docker/deployment scaffolding
- LLM boundary adjudication
- automated legal conclusions
