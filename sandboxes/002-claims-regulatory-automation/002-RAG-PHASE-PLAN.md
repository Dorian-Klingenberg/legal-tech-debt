# Legal RAG Phase Plan

Status: Historical phase plan; superseded by `002-RAG-STAGE-PLAN.md` and `CLOSURE.md`
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-07-13 (historical status and completed reopen gates reconciled)
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

Status: **Complete**

Question:

> Can selected Kentucky homeowners corpus files become legal-structure nodes with provenance, parser diagnostics, citations, broader references, conservative graph edges, candidate evidence, and retrieval bundles using local files only?

Suggested stage:

```text
stages/002-homeowners-discovery-instrumentation/
```

### Checklist

**Setup**

- [x] Create `stages/002-homeowners-discovery-instrumentation/` directory
- [x] Choose 5–10 source files from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- [x] Create `data/source_manifest_subset.csv` listing selected sources with smell mappings
- [x] Create `STAGE.md` documenting scope, selected sources, and limitations
- [x] Create `data/heuristics.md` documenting heuristic rule IDs, purposes, and failure modes

**Schema**

- [x] Create `schema/` directory with JSON Schemas for every contract artifact:
  - [x] `schema/run_manifest.schema.json`
  - [x] `schema/source.schema.json`
  - [x] `schema/parser_run.schema.json`
  - [x] `schema/block.schema.json`
  - [x] `schema/block_stats.schema.json`
  - [x] `schema/node.schema.json`
  - [x] `schema/citation.schema.json`
  - [x] `schema/reference.schema.json`
  - [x] `schema/edge.schema.json`
  - [x] `schema/table_failure.schema.json`
  - [x] `schema/parse_warning.schema.json`
  - [x] `schema/candidate_evidence.schema.json`
  - [x] `schema/retrieval_bundle.schema.json`

**Components**

- [x] Source registry — reads manifest rows, emits stable `Source` records with hash and metadata
- [x] Parser adapters — HTML parser (statute/regulation pages) and PDF parser (DOI bulletins, SERFF filing)
- [x] Parser instrumentation — emits block stats, table failures, parse warnings, and reading-order uncertainty
- [x] Normalizer — converts parser output to project-owned models (not leaking parser objects)
- [x] Structure-first segmenter — creates legal nodes from headings, sections, subsections, clauses, definitions, tables
- [x] Citation extractor — formal KRS and KAR citations into `citations.jsonl`
- [x] Reference extractor — DOI bulletins, SERFF tracking numbers, form IDs, endorsement IDs, manual references, generic law references into `references.jsonl`
- [x] Graph builder — typed edges: `contains`, `next`, `references`, `cites_statute`, `cites_regulation`, `cites_bulletin`, `defines_term`, `uses_defined_term`, `amends`, `overrides`, `unresolved_reference`
- [x] Candidate evidence scanner — exact and lexical scans for five active smells over nodes
- [x] JSONL writers — UTF-8 JSONL, one object per line, every record carries `schema_version`, `run_id`, `created_at`

**Outputs**

- [x] `output/run_manifest.json`
- [x] `output/sources.jsonl`
- [x] `output/parser_runs.jsonl`
- [x] `output/blocks.jsonl`
- [x] `output/block_stats.jsonl`
- [x] `output/nodes.jsonl`
- [x] `output/citations.jsonl`
- [x] `output/references.jsonl`
- [x] `output/edges.jsonl`
- [x] `output/table_failures.jsonl`
- [x] `output/parse_warnings.jsonl`
- [x] `output/candidate_evidence.jsonl`
- [x] `output/retrieval_bundles.json`
- [x] `output/discovery_report.md`
- [x] `LESSON.md` documenting what the discovery pass taught
- [x] `src/visualizer.py` — self-contained HTML report generator (Summary, Document Outline, Evidence Ledger, Citations, Warnings tabs)
- [x] Timestamped run subdirectories (`output/YYYYMMDD_HHMMSS_<run_id[:8]>/`); `output/` gitignored

**Success criteria**

- [x] All JSON/JSONL records carry `schema_version`, `run_id`, and `created_at`
- [x] `source_id` is stable; `node_id` is deterministic under a fixed parsing strategy
- [x] Source provenance survives every transformation
- [x] Page or source location is retained where available
- [x] Parser uncertainty is visible through block stats, table failures, and parse warnings
- [x] Section hierarchy is represented in nodes and `contains` edges
- [x] KRS and KAR references are extracted as formal citations
- [x] DOI, SERFF, form, endorsement, manual, current-guideline, and generic-law references are extracted separately from formal citations
- [x] Unresolved references are represented as visible targets
- [x] Graph edges are conservative and reviewable (no edge without explicit text or structural evidence)
- [x] Candidate evidence for the five active smells is emitted where the corpus supports it
- [x] Candidate evidence is not presented as final legal findings
- [x] No manual reviewer annotations written back into the substrate
- [x] No cross-document topic modeling or cluster-level edges

---

## Phase 2: Retrieval Baseline And Fixture Curation

Status: **Complete**

Question:

> Can exact phrase, lexical search, reference/citation signals, metadata filters, and graph expansion return useful evidence bundles and fixture examples for the five homeowners policy-layer smells?

### Checklist

**Components**

- [x] Exact phrase search over nodes
- [x] Simple lexical scoring (BM25 or equivalent over local JSONL)
- [x] Metadata filters (source type, smell mapping, effective date)
- [x] Parent/adjacent node expansion
- [x] Citation and authority expansion
- [x] Broader reference expansion
- [x] Retrieval bundle composer

**Outputs**

- [x] `output/retrieval_bundles.json` — updated with retrieval signal metadata (23 bundles)
- [x] `output/retrieval_report.md` — what retrieval modes return for each active smell
- [x] `data/goldsets/goldset-002.1.json` — versioned gold set from Stage 002 real snippets only
- [x] Curated fixture excerpts per active smell (or documented corpus limitation where missing)
- [x] `src/retrieval/` package — index, searcher, expander, composer modules
- [x] `src/retrieval_runner.py` — CLI runner; smell-specific queries; corpus gap detection

**Success criteria**

- [x] Query results include why-retrieved reasons
- [x] Bundles include parent section and adjacent nodes
- [x] Citation/reference expansion includes cited authorities or unresolved records
- [x] Bundles include parser diagnostics or uncertainty when relevant
- [x] Bundles are usable by a detector or reviewer without rereading the entire source
- [x] Every active smell has a candidate fixture example or a documented corpus limitation

---

## Phase 3: Tiny Gold Set And Retrieval Evaluation

Status: **Complete** (statute/regulation/DOI + partial policy/endorsement/rate tiers from SERFF filing)

Question:

> Which retrieval modes help on real legal/policy questions, and where does semantic retrieval add value?

### Checklist

**Gold set construction**

- [x] 11 statute/regulation/DOI items with expected node IDs, 3 test queries each (`goldset-002.2.json`)
- [x] 4 policy/manual clauses — from KNIC SERFF filing (eval-015 to eval-018); 6 more blocked (needs base HO-3 form)
- [x] 3 endorsement or form fragments — from KNIC SERFF filing (eval-019 to eval-021); 2 more blocked
- [x] 3 rate/manual fragments — from KNIC SERFF filing (eval-012 to eval-014); 2 more blocked
- [x] Gold set versioned under `data/goldsets/` — 21 items total

**Retrieval comparison**

- [x] Exact phrase baseline measured — 90% recall (19/21 items)
- [x] Lexical baseline measured — 95% recall (20/21 items)
- [x] Graph-expanded retrieval measured — bundles include parent + siblings + citations
- [x] Failures and missed hits documented (`evaluation_report.md`)
- [x] Decision: does semantic retrieval have a concrete question to answer? — **INVESTIGATE** (eval-011 aerial imagery missed by both modes)
- [x] `src/evaluator.py` — evaluation runner with per-mode stats and semantic decision logic
- [x] `output/evaluation_results.json` + `output/evaluation_report.md`
- [x] Evaluation tab added to `report.html`

**Success criteria**

- [x] Exact and lexical baselines measured before embeddings
- [x] Semantic retrieval is evaluated against a known need (not a general want)
- [x] False positives and missed hits are documented
- [x] Lexical under-recall treated as evidence for later semantic evaluation, not as proof the smell is absent

---

## Phase 4: Semantic Retrieval Experiment

Status: **Complete — deferred by result** (BM25 100%; semantic adds nothing on current corpus/queries)

Question:

> Do embeddings improve recall for homeowners policy-layer smell research enough to justify vector storage?

### Checklist

- [x] Phase 3 retrieval evaluation complete and specific failures identified (gate) — BM25 100%, no failures
- [x] Node embeddings generated via OpenAI text-embedding-3-small (251 nodes, cached in run dir)
- [x] Cosine similarity search implemented (`stages/005-semantic-retrieval-experiment/`)
- [x] Semantic vs. lexical comparison documented — semantic 76%, BM25 100%, hybrid 100%
- [x] Gold set validated (node existence, source match, query term presence) — all 21 items OK
- [x] ADR-002 updated with final conclusion and re-open conditions

**Result:** Semantic retrieval adds nothing on top of BM25 for this corpus and query set. Gold set queries were written using document vocabulary, making them phrase-matchable. A fair semantic evaluation requires paraphrase queries and multi-carrier corpus. See ADR-002 for re-open conditions.

**What would re-open Phase 4:**

- [x] Second carrier homeowners policy in corpus (KFBM)
- [x] Gold set items written as plain-English reviewer questions (five Smell 5 paraphrase queries)
- [x] At least one documented BM25 failure (Smell 5 absence-pattern query)

---

## Phase 5: Retrieval Store Decision

Status: **Parked** — gate not met; BM25 is sufficient; revisit when Phase 4 re-open conditions are satisfied

Question:

> Which existing retrieval store best supports the proven workload?

### Checklist

- [x] Phase 4 semantic retrieval evaluation complete; result did not justify a retrieval store
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
