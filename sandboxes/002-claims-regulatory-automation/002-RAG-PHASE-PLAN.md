# Legal RAG Phase Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-06-03 (checklists added; ADR/references paths updated)
Path decision: `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
Artifact contract: `adr/ADR-004-schema-run-identity-and-id-stability.md`

---

## Phase 0: Document The Architecture

Status: **Complete**

Question:

> Is the intended build order, substrate boundary, and discovery-first path documented clearly enough that future agents can orient and build without re-deriving decisions?

### Checklist

- [x] `002-RAG-INGESTION-RETRIEVAL-SPEC.md` — technical contract for discovery, instrumentation, and retrieval
- [x] `002-RAG-SUBSYSTEM-PLAN.md` — component plan and layer boundaries
- [x] `002-RAG-PHASE-PLAN.md` — this document; phased build plan
- [x] `adr/ADR-001-rag-substrate-reuses-001-structure.md` — reuse Sandbox 001 data structures
- [x] `adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md` — vector retrieval is expected but deferred
- [x] `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md` — discovery-and-instrumentation comes before fixture detectors
- [x] `adr/ADR-004-schema-run-identity-and-id-stability.md` — schema version, run identity, and stable-ID requirements
- [x] `skills/legal-rag-builder/SKILL.md` — agent workflow skill pointing to sandbox 002 docs
- [x] `references/docling-local-stack-boundary.md` — Docling as parser/enrichment adapter only; no vector DB
- [x] `references/rag-substrate-boundary-lesson.md` — findings belong downstream; RAG owns evidence bundles

Done when:

- [x] Future agents can see the intended build order
- [x] RAG substrate boundaries are clear
- [x] Vector retrieval is preserved as expected later work without becoming premature infrastructure
- [x] Discovery-and-instrumentation is clearly the next implementation path

---

## Phase 1: File-Backed Discovery And Instrumentation

Status: **Not started**

Question:

> Can selected Kentucky homeowners corpus files become legal-structure nodes with provenance, parser diagnostics, citations, broader references, conservative graph edges, candidate evidence, and retrieval bundles using local files only?

Suggested stage:

```text
stages/002-homeowners-discovery-instrumentation/
```

### Checklist

**Setup**

- [ ] Create `stages/002-homeowners-discovery-instrumentation/` directory
- [ ] Choose 5–10 source files from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- [ ] Create `data/source_manifest_subset.csv` listing selected sources with smell mappings
- [ ] Create `STAGE.md` documenting scope, selected sources, and limitations
- [ ] Create `data/heuristics.md` documenting heuristic rule IDs, purposes, and failure modes

**Schema**

- [ ] Create `schema/` directory with JSON Schemas for every contract artifact:
  - [ ] `schema/run_manifest.schema.json`
  - [ ] `schema/source.schema.json`
  - [ ] `schema/parser_run.schema.json`
  - [ ] `schema/block.schema.json`
  - [ ] `schema/block_stats.schema.json`
  - [ ] `schema/node.schema.json`
  - [ ] `schema/citation.schema.json`
  - [ ] `schema/reference.schema.json`
  - [ ] `schema/edge.schema.json`
  - [ ] `schema/table_failure.schema.json`
  - [ ] `schema/parse_warning.schema.json`
  - [ ] `schema/candidate_evidence.schema.json`
  - [ ] `schema/retrieval_bundle.schema.json`

**Components**

- [ ] Source registry — reads manifest rows, emits stable `Source` records with hash and metadata
- [ ] Parser adapters — HTML parser (statute/regulation pages) and PDF parser (DOI bulletins, SERFF filing)
- [ ] Parser instrumentation — emits block stats, table failures, parse warnings, and reading-order uncertainty
- [ ] Normalizer — converts parser output to project-owned models (not leaking parser objects)
- [ ] Structure-first segmenter — creates legal nodes from headings, sections, subsections, clauses, definitions, tables
- [ ] Citation extractor — formal KRS and KAR citations into `citations.jsonl`
- [ ] Reference extractor — DOI bulletins, SERFF tracking numbers, form IDs, endorsement IDs, manual references, generic law references into `references.jsonl`
- [ ] Graph builder — typed edges: `contains`, `next`, `references`, `cites_statute`, `cites_regulation`, `cites_bulletin`, `defines_term`, `uses_defined_term`, `amends`, `overrides`, `unresolved_reference`
- [ ] Candidate evidence scanner — exact and lexical scans for five active smells over nodes
- [ ] JSONL writers — UTF-8 JSONL, one object per line, every record carries `schema_version`, `run_id`, `created_at`

**Outputs**

- [ ] `output/run_manifest.json`
- [ ] `output/sources.jsonl`
- [ ] `output/parser_runs.jsonl`
- [ ] `output/blocks.jsonl`
- [ ] `output/block_stats.jsonl`
- [ ] `output/nodes.jsonl`
- [ ] `output/citations.jsonl`
- [ ] `output/references.jsonl`
- [ ] `output/edges.jsonl`
- [ ] `output/table_failures.jsonl`
- [ ] `output/parse_warnings.jsonl`
- [ ] `output/candidate_evidence.jsonl`
- [ ] `output/retrieval_bundles.json`
- [ ] `output/discovery_report.md`
- [ ] `LESSON.md` documenting what the discovery pass taught

**Success criteria**

- [ ] All JSON/JSONL records carry `schema_version`, `run_id`, and `created_at`
- [ ] `source_id` is stable; `node_id` is deterministic under a fixed parsing strategy
- [ ] Source provenance survives every transformation
- [ ] Page or source location is retained where available
- [ ] Parser uncertainty is visible through block stats, table failures, and parse warnings
- [ ] Section hierarchy is represented in nodes and `contains` edges
- [ ] KRS and KAR references are extracted as formal citations
- [ ] DOI, SERFF, form, endorsement, manual, current-guideline, and generic-law references are extracted separately from formal citations
- [ ] Unresolved references are represented as visible targets
- [ ] Graph edges are conservative and reviewable (no edge without explicit text or structural evidence)
- [ ] Candidate evidence for the five active smells is emitted where the corpus supports it
- [ ] Candidate evidence is not presented as final legal findings
- [ ] No manual reviewer annotations written back into the substrate
- [ ] No cross-document topic modeling or cluster-level edges

---

## Phase 2: Retrieval Baseline And Fixture Curation

Status: **Not started** — depends on Phase 1 outputs

Question:

> Can exact phrase, lexical search, reference/citation signals, metadata filters, and graph expansion return useful evidence bundles and fixture examples for the five homeowners policy-layer smells?

### Checklist

**Components**

- [ ] Exact phrase search over nodes
- [ ] Simple lexical scoring (BM25 or equivalent over local JSONL)
- [ ] Metadata filters (source type, smell mapping, effective date)
- [ ] Parent/adjacent node expansion
- [ ] Citation and authority expansion
- [ ] Broader reference expansion
- [ ] Retrieval bundle composer

**Outputs**

- [ ] `output/retrieval_bundles.json` — updated with retrieval signal metadata
- [ ] `output/retrieval_report.md` — what retrieval modes return for each active smell
- [ ] `data/goldsets/goldset-002.1.json` — versioned gold set from Stage 002 real snippets only
- [ ] Curated fixture excerpts per active smell (or documented corpus limitation where missing)

**Success criteria**

- [ ] Query results include why-retrieved reasons
- [ ] Bundles include parent section and adjacent nodes
- [ ] Citation/reference expansion includes cited authorities or unresolved records
- [ ] Bundles include parser diagnostics or uncertainty when relevant
- [ ] Bundles are usable by a detector or reviewer without rereading the entire source
- [ ] Every active smell has a candidate fixture example or a documented corpus limitation

---

## Phase 3: Tiny Gold Set And Retrieval Evaluation

Status: **Not started** — depends on Phase 2 gold set

Question:

> Which retrieval modes help on real legal/policy questions, and where does semantic retrieval add value?

### Checklist

**Gold set construction**

- [ ] 10 statute/regulation sections with expected node boundaries, citations, parent section, 3–5 test queries, and expected relevant nodes
- [ ] 10 policy/manual clauses (same fields)
- [ ] 5 endorsement or form fragments (same fields)
- [ ] 5 rate/manual fragments (same fields)
- [ ] Gold set versioned under `data/goldsets/`

**Retrieval comparison**

- [ ] Exact phrase baseline measured
- [ ] Lexical baseline measured
- [ ] Graph-expanded retrieval measured
- [ ] Failures and missed hits documented
- [ ] Decision: does semantic retrieval have a concrete question to answer?

**Success criteria**

- [ ] Exact and lexical baselines measured before embeddings
- [ ] Semantic retrieval is evaluated against a known need (not a general want)
- [ ] False positives and missed hits are documented
- [ ] Lexical under-recall treated as evidence for later semantic evaluation, not as proof the smell is absent

---

## Phase 4: Semantic Retrieval Experiment

Status: **Parked** — build only after Phase 3 identifies queries where exact/lexical/graph retrieval is insufficient

Question:

> Do embeddings improve recall for homeowners policy-layer smell research enough to justify vector storage?

### Checklist

- [ ] Phase 3 retrieval evaluation complete and specific failures identified (gate)
- [ ] Local embedding records attached to `Node` records
- [ ] File-backed or lightweight local index (no service dependency unless required)
- [ ] Same concept with different wording — tested against gold set
- [ ] Broad exclusion language — tested against gold set
- [ ] Valuation and calculation terms — tested against gold set
- [ ] Coverage/exclusion contradictions — tested against gold set
- [ ] Regulatory mapping language — tested against gold set
- [ ] Semantic vs. lexical comparison documented

**Success criteria**

- [ ] Semantic retrieval improves gold-set recall or reviewer usefulness
- [ ] Provenance and graph expansion remain intact
- [ ] Embeddings do not replace structure-aware retrieval

---

## Phase 5: Retrieval Store Decision

Status: **Parked** — decide only after Phase 4 proves what the workload actually needs

Question:

> Which existing retrieval store best supports the proven workload?

### Checklist

- [ ] Phase 4 semantic retrieval evaluation complete (gate)
- [ ] Workload characterization: is hybrid vector quality or relational metadata/joins the dominant need?
- [ ] ADR drafted for store selection before implementation
- [ ] Store selected from candidates:
  - [ ] SQLite FTS5 — embedded lexical search, local, no service
  - [ ] Qdrant — dense/sparse hybrid retrieval
  - [ ] Postgres + pgvector — relational joins, metadata, citations, graph edges

Decision rule:

- Choose Qdrant if hybrid vector retrieval quality is the core experiment
- Choose Postgres plus pgvector if structured metadata and relational joins dominate
- Stay file-backed or SQLite if the sandbox does not yet need a service

---

## Parked Until Earned

- [ ] Chatbot interface
- [ ] Production API
- [ ] Background ingestion service
- [ ] Live regulatory feeds
- [ ] Graph database
- [ ] Docker/deployment scaffolding
- [ ] LLM boundary adjudication in the main pipeline
- [ ] Automated legal conclusions
