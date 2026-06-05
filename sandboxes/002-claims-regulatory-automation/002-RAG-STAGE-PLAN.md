# Legal RAG Stage Plan

Status: Active planning document
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-06-04 (Stage 002 artifact contract repaired; expanded-corpus run revalidated)
Path decision: `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
Artifact contract: `adr/ADR-004-schema-run-identity-and-id-stability.md`
Contract repair: `adr/ADR-008-stage-002-artifact-contract-repair.md`

Each entry maps 1:1 to a `stages/00N-*/` directory. "Stage" is the single unit of work throughout.

---

## Stage 001: Document The Architecture

Status: **Complete**
Directory: (pre-stages; docs live in `sandboxes/002-claims-regulatory-automation/`)

Question:

> Is the intended build order, substrate boundary, and discovery-first path documented clearly enough that future agents can orient and build without re-deriving decisions?

### Checklist

- [x] `002-RAG-INGESTION-RETRIEVAL-SPEC.md` — technical contract for discovery, instrumentation, and retrieval
- [x] `002-RAG-SUBSYSTEM-PLAN.md` — component plan and layer boundaries
- [x] `002-RAG-STAGE-PLAN.md` — this document; stage build plan
- [x] `adr/ADR-001-rag-substrate-reuses-001-structure.md` — reuse Sandbox 001 data structures
- [x] `adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md` — vector retrieval is expected but deferred
- [x] `adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md` — discovery-and-instrumentation comes before fixture detectors
- [x] `adr/ADR-004-schema-run-identity-and-id-stability.md` — schema version, run identity, and stable-ID requirements
- [x] `adr/ADR-008-stage-002-artifact-contract-repair.md` — repaired implementation drift back to the Stage 002 artifact contract
- [x] `skills/legal-rag-builder/SKILL.md` — agent workflow skill pointing to sandbox 002 docs
- [x] `references/docling-local-stack-boundary.md` — Docling as parser/enrichment adapter only; no vector DB
- [x] `references/rag-substrate-boundary-lesson.md` — findings belong downstream; RAG owns evidence bundles

Done when:

- [x] Future agents can see the intended build order
- [x] RAG substrate boundaries are clear
- [x] Vector retrieval is preserved as expected later work without becoming premature infrastructure
- [x] Discovery-and-instrumentation is clearly the next implementation path

---

## Stage 002: File-Backed Discovery And Instrumentation

Status: **Complete**
Directory: `stages/002-homeowners-discovery-instrumentation/`

Question:

> Can selected Kentucky homeowners corpus files become legal-structure nodes with provenance, parser diagnostics, citations, broader references, conservative graph edges, candidate evidence, and retrieval bundles using local files only?

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

**Contract repair**

- [x] `source_hash` and `content_hash` separated in source records
- [x] source-derived artifacts carry `source_id` and `source_hash`
- [x] candidate evidence uses `candidate_id`
- [x] run manifest carries parser list, schema versions, config snapshot, and parse statistics
- [x] Stage 002 retrieval bundles use future-compatible `hits[]`
- [x] retrieval hits reserve lexical, semantic, graph, citation/reference, metadata, parser penalty, diagnostics, and expanded-context fields
- [x] Stage 003 retrieval bundles validated against the same retrieval-bundle schema
- [x] Contract repair recorded in ADR-008

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

## Stage 003: Retrieval Baseline And Fixture Curation

Status: **Complete**
Directory: `stages/003-retrieval-baseline/`

Question:

> Can exact phrase, lexical search, reference/citation signals, metadata filters, and graph expansion return useful evidence bundles and fixture examples for the five homeowners policy-layer smells?

### Checklist

**Components**

- [x] Exact phrase search over nodes
- [x] Simple lexical scoring (BM25 over local JSONL)
- [x] Metadata filters (source type, smell mapping, effective date)
- [x] Parent/adjacent node expansion
- [x] Citation and authority expansion
- [x] Broader reference expansion
- [x] Retrieval bundle composer
- [x] `src/retrieval/` package — index, searcher, expander, composer modules
- [x] `src/retrieval_runner.py` — CLI runner; smell-specific queries; corpus gap detection

**Outputs**

- [x] `output/retrieval_bundles.json` — updated with retrieval signal metadata (39 bundles on run 18b0dec5)
- [x] `output/retrieval_report.md` — what retrieval modes return for each active smell
- [x] `data/goldsets/goldset-002.1.json` — versioned gold set from Stage 002 real snippets only
- [x] Curated fixture excerpts per active smell (or documented corpus limitation where missing)

**Success criteria**

- [x] Query results include why-retrieved reasons
- [x] Bundles include parent section and adjacent nodes
- [x] Citation/reference expansion includes cited authorities or unresolved records
- [x] Bundles include parser diagnostics or uncertainty when relevant
- [x] Bundles are usable by a detector or reviewer without rereading the entire source
- [x] Every active smell has a candidate fixture example or a documented corpus limitation

---

## Stage 004: Gold Set Evaluation

Status: **Complete**
Directory: `stages/004-gold-set-evaluation/`

Question:

> Which retrieval modes help on real legal/policy questions, and where does the retrieval baseline fall short?

### Checklist

**Gold set construction**

- [x] 11 statute/regulation/DOI items with expected node IDs, 3 test queries each (`goldset-002.2.json`)
- [x] 4 policy/manual clauses — from KNIC SERFF filing (eval-015 to eval-018); additional planned clauses deferred pending broader gold-set expansion against the KFBM/KNIC corpus
- [x] 3 endorsement or form fragments — from KNIC SERFF filing (eval-019 to eval-021); additional planned fragments deferred
- [x] 3 rate/manual fragments — from KNIC SERFF filing (eval-012 to eval-014); additional planned fragments deferred
- [x] Gold set versioned under `data/goldsets/` — 21 items total
- [x] Gold set validator (`stages/005-semantic-retrieval-experiment/data/validate_goldset.py`) — run before any gold set edit
- [x] Gold set validator accepts explicit `--run-dir` and `--goldset`; validated all 21 items against repaired run 18b0dec5

**Retrieval evaluation**

- [x] Exact phrase baseline — 95% recall (20/21 items)
- [x] BM25 baseline — 100% recall (21/21 items)
- [x] Graph-expanded retrieval measured — bundles include parent + siblings + citations
- [x] Failures and missed hits documented (`evaluation_report.md`)
- [x] `src/evaluator.py` — evaluation runner with per-mode stats and semantic decision logic
- [x] `output/evaluation_results.json` + `output/evaluation_report.md`
- [x] Re-evaluated on expanded repaired run 18b0dec5 — phrase 20/21 (95%), BM25 21/21 (100%)

**Success criteria**

- [x] Exact and lexical baselines measured before embeddings
- [x] False positives and missed hits are documented
- [x] Lexical under-recall treated as evidence for later semantic evaluation, not as proof the smell is absent

---

## Stage 005: Semantic Retrieval Experiment

Status: **Complete — architectural finding 2026-06-04**
Directory: `stages/005-semantic-retrieval-experiment/`

Question:

> Do embeddings improve recall for homeowners policy-layer smell research enough to justify vector storage?

### Checklist

- [x] Stage 004 BM25 baseline complete (gate) — 100% recall, no failures
- [x] Node embeddings generated via OpenAI text-embedding-3-small (251 nodes, cached in run dir)
- [x] Cosine similarity search implemented
- [x] Semantic vs. lexical comparison documented — semantic 76%, BM25 100%, hybrid 100%
- [x] Gold set validated (node existence, source match, query term presence) — all 21 items OK
- [x] ADR-002 updated with final conclusion and re-open conditions

**Result:** BM25 is already perfect. Semantic adds nothing on top of BM25 — it rescues zero BM25 misses. The 76% semantic recall reflects gold set queries written in document vocabulary (phrase-matchable), not plain-language paraphrases. A fair semantic evaluation needs paraphrase queries and a multi-carrier corpus. Vector store selection deferred. See ADR-002.

**Re-open conditions — all met 2026-06-04:**

- [x] Second carrier homeowners policy in corpus (KFBM, met 2026-06-03)
- [x] Gold set items written as plain-English reviewer questions — five Smell 5 paraphrase queries approved
- [x] Documented BM25 failure — Smell 5 produces zero findings; lexical cannot surface regulatory-mapping smell in carrier policy language

**Final result:** 14/26 hits (54% recall), Decision: PURSUE. Smell 5 paraphrase items: 0/5 hits with both text-embedding-3-small and text-embedding-3-large. Architectural conclusion: vector similarity cannot detect absence. Smell 5 requires graph-based gap detection. See ADR-010. Vector store selection remains deferred; vector retrieval earns a future role in cross-carrier paraphrase matching.

---

## Stage 006: Deterministic Pattern Detectors

Status: **Complete**
Directory: `stages/006-deterministic-detectors/`

Question:

> Can smell-specific deterministic detectors over Stage 002 nodes emit structured findings with enough precision and provenance to be useful to a reviewer?

### Checklist

- [x] Create `stages/006-deterministic-detectors/` with `STAGE.md`, `.gitignore`, `src/`
- [x] One detector module per active smell:
  - [x] Smell 1 — Overbroad / Non-deterministic Exclusions
  - [x] Smell 2 — Magic Number / Magic Valuation Terms
  - [x] Smell 3 — Coverage Inversion / Contradictory Conditions
  - [x] Smell 4 — Calculation Rule Drift / Unversioned Rate Reference
  - [x] Smell 5 — Regulatory Mapping Smells
- [x] Each detector reads Stage 002 JSONL artifacts via `RunIndex`
- [x] Each detector emits structured `Finding` records: `smell_id`, `node_id`, `source_id`, `evidence_text`, `confidence`, `rationale`, `reviewer_question`, `false_positive_risk`
- [x] Findings are distinct from candidate evidence — they carry confidence, rationale, and reviewer question
- [x] Detector runner CLI — runs all detectors, writes `detector_findings.jsonl` and `detector_report.md`
- [x] False positive risk documented per finding

**Results (run 996e36af, 251 nodes, original corpus):** 17 findings — Smell 2: 13 (MEDIUM), Smell 3: 3 (LOW), Smell 4: 1 (HIGH).

**Results (run 18b0dec5, repaired Stage 002 contract, 353 nodes, 28-source corpus, Smell 5 redesigned):** 35 findings — Smell 1: 1 (LOW), Smell 2: 17 (MEDIUM), Smell 3: 4 (LOW), Smell 4: 1 (HIGH), Smell 5: 12 (7 MEDIUM, 5 LOW, graph-gap detection). ADR-010 records the Smell 5 architecture decision.

**Detector improvement 2026-06-03:** H001/H003 heuristics in smell2.py now suppressed for `kar_regulation`, `krs_statute`, `doi_bulletin`, `doi_guidance` source types. "Reasonable" in regulatory docs is legal standard language, not a claim dispute gate. Detector runner enriches nodes with `source_type` from `source_by_id` before passing to detectors.

**Success criteria**

- [x] Every finding is traceable to a specific node and source
- [x] No finding claims a policy is unlawful — findings surface patterns for reviewer judgment
- [x] Confidence levels are calibrated (not all HIGH)
- [x] Each detector has documented heuristic IDs matching `data/heuristics.md`
- [x] Detectors are independent — one detector failure does not block others

---

## Stage 007: Reviewer Report

Status: **Complete**
Directory: `stages/007-reviewer-report/`

Question:

> Can detector findings, candidate evidence, and retrieval bundles be assembled into a human-readable report that a legal reviewer can act on?

### Checklist

- [x] Create `stages/007-reviewer-report/` with `STAGE.md`, `.gitignore`, `src/`
- [x] Report assembler reads Stage 002 JSONL + Stage 006 `detector_findings.jsonl`
- [x] Per-smell summary section: finding count, confidence distribution
- [x] Per-finding detail: source, node ID, evidence text, heuristic ID, rationale, reviewer question, false positive risk
- [x] Corpus gap section: three gap tiers with affected smells and impact
- [x] Output: single-file dark-theme HTML with Summary, Findings, Corpus Gaps tabs
- [x] Output: `reviewer_report.md` — plain-text version for diff and version control
- [x] Report written into the Stage 002 run directory

**Results (run 996e36af):** 17 findings, 47 candidate evidence items, 3 corpus gap tiers documented.

**Results (run 18b0dec5, repaired Stage 002 contract, after Smell 5 redesign):** 35 findings, 121 candidate evidence items, reviewer report regenerated under `output/007/20260604_130606_18b0dec5/`.

**Success criteria**

- [x] A reviewer unfamiliar with the pipeline can read the report and identify which nodes to inspect
- [x] Every finding links back to source document and node
- [x] Corpus gaps are clearly distinguished from confirmed findings
- [x] Report does not claim legal conclusions — it surfaces patterns for human judgment

---

## Loose Threads (Open, Not Blocking)

- [x] **Smell 5 detector recalibrated** — ADR-010 established graph-based gap detection; H004-H006 now produce 12 Smell 5 findings on run 18b0dec5.
- [x] **Gold set re-evaluated against repaired expanded run 18b0dec5** — phrase 20/21 (95%), BM25 21/21 (100%); semantic remains deferred.
- [x] **Stage 005 reopened 2026-06-04** — all three re-open conditions met. See Stage 005 STAGE.md and ADR-002 for next steps.
- [ ] **EXT MISMATCH files** — KY-KRS-304-12-230 and KY-KRS-304-14 are named `.html` but contain PDF content (same issue as KY-KRS-304-13 which was renamed). Pipeline parses them with warnings. Low priority since they produce nodes, but should be renamed for cleanliness.

---

## Parked Until Earned

- [ ] Retrieval store selection — deferred; ADR-010 shows vector similarity is not appropriate for gap-detection smells, but may still earn a future role for cross-carrier paraphrase matching
- [ ] Chatbot interface
- [ ] Production API
- [ ] Background ingestion service
- [ ] Live regulatory feeds
- [ ] Graph database
- [ ] Docker/deployment scaffolding
- [ ] LLM boundary adjudication in the main pipeline
- [ ] Automated legal conclusions
