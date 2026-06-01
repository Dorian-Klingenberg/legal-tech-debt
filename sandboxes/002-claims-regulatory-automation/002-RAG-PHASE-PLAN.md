# Legal RAG Phase Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01

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

## Phase 1: File-Backed Structural Ingestion

Question:

> Can real Kentucky homeowners corpus files become legal-structure nodes with provenance, citations, references, and graph edges using local files only?

Suggested stage:

```text
stages/003-homeowners-rag-ingestion/
```

Inputs:

- small subset of `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- at least one HTML statute or regulation
- at least one DOI PDF
- one policy/rate/manual filing fragment where practical

Components:

- source registry
- parser adapters
- normalized models
- structure-first segmenter
- citation/reference extractor
- graph builder
- JSONL/CSV writers

Outputs:

- `output/sources.jsonl`
- `output/nodes.jsonl`
- `output/citations.jsonl`
- `output/edges.jsonl`
- `output/parse_warnings.jsonl`
- `output/report.md`

Success criteria:

- source provenance survives every transformation
- page or source location is retained where available
- section hierarchy is represented
- KRS and KAR references are extracted
- unresolved references are represented as visible targets
- graph edges are reviewable

## Phase 2: Retrieval Bundle Prototype

Question:

> Can exact phrase, lexical search, and graph expansion return useful evidence bundles for the five homeowners policy-layer smells?

Components:

- exact phrase search
- simple lexical scoring
- metadata filters
- parent/adjacent node expansion
- citation and authority expansion
- retrieval bundle composer

Outputs:

- `output/retrieval_bundles.json`
- `output/retrieval_report.md`

Success criteria:

- query results include why-retrieved reasons
- bundles include parent section and adjacent nodes
- citation expansion includes cited authorities or unresolved citation records
- bundles are usable by a detector or human reviewer without rereading the entire source

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
