# Discovery, Instrumentation, And Retrieval Spec

Status: Draft engineering spec
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Updated: 2026-06-03
Source notes: `skills/proposals/legal-rag-builder.md`
Planning docs:

- `002-RAG-SUBSYSTEM-PLAN.md`
- `002-RAG-PHASE-PLAN.md`
- `../../skills/legal-rag-builder/adr/ADR-001-rag-substrate-reuses-001-structure.md`
- `../../skills/legal-rag-builder/adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md`
- `../../skills/legal-rag-builder/adr/ADR-003-discovery-instrumentation-before-fixture-detectors.md`
- `../../skills/legal-rag-builder/adr/ADR-004-schema-run-identity-and-id-stability.md`

## Mission

Build a local-first legal discovery, instrumentation, and retrieval evidence substrate for the Sandbox 002 Kentucky homeowners research corpus.

The system should ingest statutes, regulations, DOI bulletins, homeowners policy forms, endorsements, manuals, and filings; preserve legal structure; record parser/reference uncertainty; extract citations and broader domain references; create graph-linked nodes; return retrieval bundles; and surface source-traceable candidate evidence for the five active smells.

This is proof-of-concept infrastructure for research, not a production platform.

## Non-Goals

- Do not build a generic chatbot first.
- Do not start with UI polish.
- Do not use naive fixed-window chunking as the primary strategy.
- Do not rely on pure vector search alone.
- Do not collapse ingestion, retrieval, and legal analysis into one opaque agent prompt.
- Do not add databases, services, queues, containers, or production APIs until a sandbox stage explicitly earns them.
- Do not treat parser output as truth without diagnostics.
- Do not treat all references as legal citations.
- Do not let lexical candidate scans become the final discovery ceiling.

## Active Domain

The active domain remains Kentucky homeowners insurance and the five Sandbox 002 policy-layer smells:

1. Overbroad / Non-deterministic Exclusions
2. Magic Number / Magic Valuation Terms
3. Coverage Inversion / Contradictory Conditions
4. Calculation Rule Drift / Unversioned Rate Reference
5. Regulatory Mapping Smells

Use the existing corpus:

- `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`
- one source directory per smell under `corpus/`

Do not procure more SERFF material unless the active task runs into a documented known gap.

## Design Principles

- Legal structure beats generic NLP heuristics.
- Every output object must carry provenance.
- Preserve original text before any lossy normalization.
- Graph links are preferable to large overlapping chunks.
- Retrieval should return evidence bundles, not orphan text fragments.
- Parser provenance, parse-quality signals, table failures, reading-order uncertainty, and partial reference normalization are evidence-layer records, not debugging leftovers.
- Citations and broader references must be separate records.
- Prefer deterministic code over broad prompting.
- Make each module swappable, but do not over-abstract before the first stage proves the need.
- Keep configuration explicit and inspectable.

## Recommended Stack

The first implementation should reuse the proven Sandbox 001 representation style: local records, graph edges, missing/unresolved targets, matrices where useful, and JSON/CSV/Markdown evidence outputs.

The target architecture may eventually use:

- Parser: Docling
- Chunk/index orchestration: LlamaIndex abstractions where useful
- Citation extraction: Eyecite plus custom Kentucky and insurance filing extractors
- Retrieval store: SQLite FTS5, Qdrant, or Postgres plus pgvector, depending on the experiment

For the first implementation stage, use file-backed JSON/JSONL/CSV outputs before choosing a retrieval store. This preserves the sandbox rule against premature infrastructure while still shaping the code around later lexical, semantic, graph, citation/reference, and metadata retrieval.

Semantic/vector retrieval remains expected, not dropped. It should be added after the node, citation, edge, and retrieval-bundle contracts are stable and a tiny gold set shows which semantic queries exact/lexical/graph retrieval cannot satisfy.

### Local Docling Boundary

Docling 2.93.0 and related Docling model packages were verified in the local Python environment on 2026-06-02. See `../../skills/legal-rag-builder/references/docling-local-stack-boundary.md`.

Treat Docling as a parser or optional enrichment adapter. It can convert messy documents and may use local cached document models, OCR, table extraction, and VLM-style parsing/enrichment features. It does not replace the project-owned normalizer, legal metadata, citation extraction, typed graph, sparse/lexical indexes, vector store decision, retrieval bundles, smell detectors, or reviewer state.

No general local LLM runtime or vector database was verified for this repo at that time. Future stages must re-verify and document any embedding library, local model runtime, or retrieval store they introduce.

## Phased Build Plan

### Phase 0: Spec and Skill

Deliverables:

- this spec
- `skills/legal-rag-builder/SKILL.md`
- registry update in `skills/registry.csv`

Success criteria:

- future agents know the RAG work exists
- the skill points to repo docs instead of carrying all project knowledge
- no implementation infrastructure is introduced

### Phase 1: File-Backed Discovery And Instrumentation Slice

Goal:

> Prove that selected corpus files can become legal-structure nodes with provenance, parser diagnostics, citations, broader references, conservative graph edges, candidate evidence, and future-compatible retrieval bundles using plain local files.

Inputs:

- a small subset from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- 1-2 sources per active smell where practical
- target 5-10 unique source files total; exceeding that requires a stage note explaining why the tiny slice was insufficient

Deliverables:

- `stages/002-homeowners-discovery-instrumentation/STAGE.md`
- `stages/002-homeowners-discovery-instrumentation/LESSON.md`
- `schema/sources.schema.json`
- `schema/parser_runs.schema.json`
- `schema/blocks.schema.json`
- `schema/block_stats.schema.json`
- `schema/nodes.schema.json`
- `schema/citations.schema.json`
- `schema/references.schema.json`
- `schema/edges.schema.json`
- `schema/table_failures.schema.json`
- `schema/parse_warnings.schema.json`
- `schema/candidate_evidence.schema.json`
- `schema/retrieval_bundle.schema.json`
- `data/source_manifest_subset.csv`
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

- every JSON/JSONL artifact carries schema version, run identity, and creation timestamp
- schema files exist for all Stage 002 artifact types
- page or source location is preserved where available
- parser provenance and parser uncertainty are visible
- section hierarchy is represented
- KRS and KAR references are extracted
- broader DOI, SERFF, form, endorsement, manual, and current-guideline references are extracted separately from citations
- exact phrase search can return a bundle for at least one smell phrase
- graph expansion includes parent section and cited authority when available
- transparent heuristic rules are documented in `data/heuristics.md`

### Phase 2: Retrieval Baseline And Fixture Curation

Goal:

> Use exact phrase, lexical, citation/reference, metadata, and graph expansion to return useful evidence bundles and curate fixture examples before adding embeddings or durable storage.

Deliverables:

- curated fixture excerpts from candidate evidence
- tiny gold set from real corpus excerpts
- 3-5 test queries per selected source group
- comparison report showing where exact, lexical, citation/reference, metadata, and graph-expanded retrieval help or fail

Decision gate:

- Record what exact/lexical/citation/reference/graph retrieval misses.
- Choose whether those misses justify a semantic retrieval experiment.

### Phase 3: Semantic Retrieval Evaluation

Only after Phases 1-2 show specific retrieval failures, compare semantic or hybrid retrieval on the tiny gold set.

Decision gate:

- Choose whether retrieval quality requires embeddings now.
- Choose whether a local file-backed or embedded-local index is enough before introducing Qdrant or pgvector.

### Phase 4: Storage Decision

Only after Phases 1-3, decide whether to prototype:

- Qdrant, if hybrid dense/sparse retrieval experimentation is the main need
- Postgres plus pgvector, if relational joins, metadata, citations, and graph edges are the main need

This should be a separate stage with an explicit question and rollback-friendly implementation.

## Pipeline

### Acquire

- read a source file path or URL from manifest
- register source metadata
- compute content hash for deduplication and versioning
- preserve raw path and access metadata

### Parse

- convert source into structured blocks or Markdown
- preserve page references, headings, tables, and reading order where possible
- record parser warnings instead of hiding them

### Normalize

Canonical intermediate concepts:

- `Source`
- `Document`
- `Block`
- `ParserRun`
- `BlockStats`
- `Node`
- `PageRef`
- `SectionPath`
- `TableBlock`
- `CitationCandidate`
- `Segment`
- `Citation`
- `Reference`
- `Edge`
- `TableFailure`
- `ParseWarning`
- `CandidateEvidence`
- `RetrievalBundle`

Normalize only after preserving original text.

Domain findings are not part of the discovery/RAG substrate. Candidate evidence is allowed; final findings, smell classifications, severity, ROI mapping, reviewer decisions, and human-review state belong to downstream detector and reporting layers.

### Segment

- use structure-first segmentation
- use semantic fallback only inside oversized units
- do not use LLM boundary adjudication in the Stage 002 main pipeline; park it for a later explicitly approved experiment if malformed or OCR-heavy sources require it

### Extract

Extract:

- citations
- broader references
- defined terms
- cross-references
- form IDs
- endorsement IDs
- SERFF tracking numbers
- policy manual identifiers
- statute and regulation references

Keep formal legal citations in `citations.jsonl`. Keep DOI bulletins, SERFF tracking numbers, form IDs, endorsement IDs, manual IDs, current-guideline references, generic law references, and internal cross-references in `references.jsonl` unless they are also formal legal citations.

### Build Graph

Create nodes and edges that preserve:

- containment
- order
- citations
- defined-term relationships
- amendments or overrides where detectable
- source derivation

### Retrieve

Support:

- exact phrase search
- lexical search
- semantic search when embeddings exist
- metadata filtering
- graph neighbor expansion

Return retrieval bundles with provenance and "why retrieved" reasons.

## Data Model

### Schema And Run Identity

Every JSON/JSONL artifact emitted by Stage 002 must include:

- `schema_version`
- `run_id`
- `created_at`
- `source_hash` or `content_hash` where applicable

Definitions:

- `source_hash`: hash of canonical document identity inputs, such as jurisdiction, title, citation or filing ID, and effective date.
- `content_hash`: hash of the actual file bytes or normalized text.

`sources.jsonl` should include both `source_hash` and `content_hash`. Node-like records must carry `source_id` plus at least `source_hash`; `content_hash` is optional when it is not cheap to compute.

Stage 002 should use artifact-specific JSON Schemas under `schema/`. Stage 003 and later stages must conform to these schemas or explicitly version and document any extension. Do not silently add fields that downstream stages depend on.

Each Stage 002 run must also emit `output/run_manifest.json` with:

- `run_id`
- `timestamp`
- `corpus_root`
- `sources_count`
- `parsers_used`
- `schema_versions`
- `config_snapshot`
- high-level parse stats, such as the percentage of blocks with low reading-order confidence

### ID Stability

`source_id` should either be assigned manually and recorded in `sources.jsonl`, or generated as a stable hash of normalized document identity fields such as jurisdiction, title, URL or filing ID, and effective date, with a short readable suffix.

`source_id` must remain stable across runs as long as the underlying document identity does not change.

`node_id` should be generated deterministically from `source_id`, structural path, and parser block ID or equivalent stable block locator. Node IDs are intended to be stable across reparses under a fixed parsing strategy.

If a parser configuration or segmentation strategy changes in a way that invalidates node IDs, record that change with a new `schema_version`, `run_mode`, and migration note.

### Source

Fields:

- `source_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_hash`
- `title`
- `source_type`
- `jurisdiction`
- `url`
- `downloaded_path`
- `content_hash`
- `effective_date`
- `revision_date`
- `company_name`
- `line_of_business`
- `status`
- `created_at`
- `metadata`

### Node

Fields:

- `node_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `node_type`
- `parent_node_id`
- `ordinal`
- `text`
- `retrievable_text`
- `normalized_text`
- `section_path`
- `page_start`
- `page_end`
- `parser_block_ids`
- `normalization_steps`
- `token_count`
- `char_count`
- `stable_anchor`
- `embedding_status`
- `metadata`

Allowed node types:

- `document`
- `section`
- `subsection`
- `clause`
- `list_item`
- `definition`
- `table`
- `endorsement`
- `citation`
- `summary`

### Block

Fields:

- `block_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `parser_run_id`
- `parser_block_id`
- `parser_block_type`
- `text`
- `page`
- `char_span`
- `token_span`
- `section_path`
- `layout_confidence`
- `ocr_confidence`
- `reading_order_confidence`
- `table_confidence`
- `normalization_steps`
- `metadata`

Parser uncertainty fields are part of the evidence layer. They must not be stripped or collapsed away before Stage 003.

### BlockStats

Fields:

- `block_stats_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `parser_run_id`
- `blocks_count`
- `blocks_by_type`
- `low_layout_confidence_count`
- `low_reading_order_confidence_count`
- `ocr_blocks_count`
- `table_blocks_count`
- `metadata`

### Edge

Fields:

- `edge_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `from_node_id`
- `to_node_id`
- `edge_type`
- `confidence`
- `evidence`
- `metadata`

Allowed edge types:

- `contains`
- `next`
- `references`
- `defines_term`
- `uses_defined_term`
- `cites_statute`
- `cites_regulation`
- `cites_bulletin`
- `amends`
- `overrides`
- `has_schedule`
- `has_declaration_reference`
- `incorporates_by_reference`
- `state_amendment_to`
- `version_of`
- `has_exception`
- `has_condition`
- `has_sublimit`
- `applies_to_coverage_part`
- `has_notice_period`
- `unresolved_reference`
- `same_topic`
- `derived_from_summary`

Every edge must be supported by explicit text evidence such as a reference string, heading, or clause, recorded in `edges.jsonl.evidence`. Do not add inferred legal relationships without text support.

### Citation

Fields:

- `citation_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `node_id`
- `citation_text`
- `citation_type`
- `normalized_citation`
- `resolver_target`
- `confidence`
- `citation_confidence`

Citation types:

- `case`
- `statute`
- `regulation`
- `bulletin`
- `legal_authority`

### Reference

Fields:

- `reference_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `node_id`
- `reference_text`
- `reference_type`
- `normalized_reference`
- `resolver_target`
- `reference_target_id`
- `confidence`
- `reference_confidence`
- `normalization_status`
- `metadata`

Reference types:

- `krs_reference`
- `kar_reference`
- `doi_bulletin`
- `serff_tracking_number`
- `form_id`
- `endorsement_id`
- `manual_reference`
- `current_guideline_reference`
- `state_amendatory_reference`
- `declarations_reference`
- `schedule_reference`
- `defined_term_reference`
- `incorporation_by_reference`
- `generic_state_law_reference`
- `internal_cross_reference`
- `coverage_part_reference`
- `notice_period_reference`
- `unresolved_reference`

`citations.jsonl` is for formal legal citations. `references.jsonl` is for broader domain references and incorporation patterns that matter for the five smells.

### ParserRun

Fields:

- `parser_run_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `parser_name`
- `parser_version`
- `parser_config`
- `started_at`
- `completed_at`
- `input_path`
- `document_format`
- `scope`
- `output_format`
- `status`
- `failure_reason`
- `warnings_count`
- `table_failures_count`
- `reading_order_confidence`
- `metadata`

### TableFailure

Fields:

- `table_failure_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `parser_run_id`
- `block_id`
- `page`
- `failure_type`
- `message`
- `evidence`
- `confidence`
- `metadata`

Failure types:

- `mis_detected`
- `partial`
- `merged_columns`
- `header_lost`
- `row_order_uncertain`
- `cell_text_lost`
- `unknown`

### ParseWarning

Fields:

- `parse_warning_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `parser_run_id`
- `block_id`
- `warning_type`
- `message`
- `severity`
- `evidence`
- `metadata`

### Parse Failure Policy

A completely failed parse must never silently drop a source from Stage 002.

Record a failed parse by setting `parser_runs.jsonl.status` to `failed` and filling `failure_reason`. If the failure has block-level evidence, also emit `parse_warnings.jsonl` or `table_failures.jsonl` records as appropriate.

Do not add a separate `parse_failures.jsonl` artifact in Stage 002 unless the first implementation proves `parser_runs.jsonl` cannot carry enough failure detail.

### CandidateEvidence

Fields:

- `candidate_id`
- `schema_version`
- `run_id`
- `created_at`
- `source_id`
- `source_hash`
- `node_id`
- `candidate_type`
- `smell`
- `evidence_text`
- `why_flagged`
- `heuristic_rule_id`
- `heuristic_version`
- `evidence_span`
- `supporting_node_ids`
- `retrieval_reasons`
- `parser_confidence`
- `reference_confidence`
- `machinery_confidence`
- `cost_pool`
- `reviewer_question`
- `status`
- `metadata`

Candidate evidence is not a final finding. It should be reviewable, source-traceable, and honest about extraction uncertainty.

`status` in `candidate_evidence.jsonl` describes workflow state, not legal confidence. `machinery_confidence` describes pipeline confidence in the candidate generation process, not the underlying legal conclusion.

## Chunking Policy

Default rules:

- Never split a heading from the paragraph that immediately follows it.
- Never split a definition term from its definition body.
- Never split a numbered list item across chunks unless it is extremely long.
- Never split tables into row fragments unless there is a dedicated table serializer.
- Keep endorsement titles attached to endorsement body text.
- Preserve parent-child relationships rather than adding large text overlap.

Suggested sizes:

- clause/list-item nodes: 150-400 tokens
- section nodes: 400-1200 tokens
- summaries: one concise summary per section and one per document, only when useful
- overlap: minimal and structural; prefer graph edges

Pseudo-logic:

```text
detect structural blocks from parser output
group contiguous blocks into legal units
if legal unit <= soft token max:
  emit node
else if unit can split by subsection markers:
  split by subsection
else if unit can split by paragraph boundaries:
  split by paragraph
else if semantic splitting is enabled:
  apply semantic boundary detection
else:
  emit oversized node with warning
create parent section node
link child nodes to parent
create next edges between siblings
```

## Citation And Reference Extraction

Use Eyecite where it fits formal legal citations.

Add custom citation extractors for:

- Kentucky statutes: `KRS xxx.xxx-xxx`
- Kentucky regulations: `806 KAR xx:xxx`

Add custom reference extractors for:

- DOI bulletins and advisory opinions
- SERFF tracking numbers
- form numbers
- endorsement numbers
- policy manual identifiers
- coverage part references
- notice period references
- generic references such as "as required by law" or "current company guidelines"

For each extracted citation:

1. preserve the original citation text
2. normalize the citation
3. classify citation type
4. attempt resolver lookup when a resolver exists
5. create a citation record
6. create an edge from the source node to the authority node or unresolved citation target

For each extracted reference:

1. preserve the original reference text
2. normalize the reference where possible
3. classify reference type
4. record normalization status and confidence
5. create a reference record
6. create a conservative edge only when the relationship is supported by explicit text

## Retrieval Bundle Contract

Return human-readable and machine-usable retrieval bundles.

```json
{
  "schema_version": "retrieval_bundle.002.1.0",
  "run_id": "20260603T120000Z-stage002",
  "created_at": "2026-06-03T12:00:00Z",
  "bundle_id": "...",
  "query_text": "...",
  "task_description": "...",
  "filters": {},
  "hits": [
    {
      "node_id": "...",
      "rank": 1,
      "score": 0.92,
      "node_type": "clause",
      "text": "...",
      "source": {
        "source_id": "...",
        "title": "...",
        "source_type": "...",
        "url": "..."
      },
      "section_path": "...",
      "pages": [12, 13],
      "why_retrieved": ["exact phrase", "citation expansion"],
      "candidate_ids": [],
      "signal_scores": {
        "exact": 1.0,
        "lexical": 0.72,
        "graph": 0.4,
        "citation": 0.2,
        "reference": 0.2,
        "metadata": 0.1,
        "semantic": null,
        "parser_penalty": 0.0
      },
      "parser_diagnostics": {
        "parser_run_id": "...",
        "reading_order_confidence": 0.9,
        "warnings": []
      },
      "expanded_context": {
        "parent_section": {},
        "adjacent_nodes": [],
        "citations": [],
        "references": [],
        "overrides": []
      }
    }
  ]
}
```

`retrieval_bundles.json` is one record per retrieval task or query. Hits are node-centric: each hit must reference at least one `node_id` and may reference tightly associated `candidate_id` values. Semantic scores should remain `null` until a semantic retrieval stage explicitly implements and validates them.

## Heuristic Rule Governance

Stage 002 candidate generation may use transparent heuristics only.

Document each heuristic in `data/heuristics.md` with:

- `heuristic_rule_id`
- `heuristic_version`
- active smell
- purpose
- input records consumed
- trigger language or structural signal
- expected false positives
- expected false negatives
- downstream consumer

Heuristic rules may produce candidate evidence. They do not produce final detector findings.

## Stage 002 Guardrails

- No new edge type without at least one text-supported example and an identified consumer in Stage 003 or later.
- No new schema field without an identified downstream consumer, such as retrieval, detectors, reporting, or parser-uncertainty instrumentation.
- No semantic retrieval implementation before a tiny retrieval gold set exists and documented misses show where lexical, reference/citation, metadata, or graph retrieval fails.
- No detector logic inside Stage 002 beyond transparent, documented heuristics.
- No manual reviewer annotations written back into the Stage 002 substrate; reviewer state belongs in separate later artifacts.
- No cross-document topic modeling or cluster-level graph edges in Stage 002.

## LLM Usage Constraints

Stage 002 is intended to be deterministic.

LLMs may be used only for one-off experiments or helper notes, not the main pipeline. Any LLM-assisted output must go into separate artifacts such as `llm_assisted_notes.jsonl` and must not mutate the standard Stage 002 outputs.

## JSONL Conventions

JSON Lines artifacts must be:

- UTF-8 encoded
- one JSON object per line
- no trailing commas
- tolerant of a final line with or without a trailing newline

## Configuration Knobs

Use explicit config. Initial file-backed defaults:

```yaml
parser:
  engine: docling
  ocr_enabled: false
  emit_parser_runs: true
  emit_block_stats: true
  emit_table_failures: true
  config_snapshot: true

chunking:
  clause_soft_max_tokens: 300
  clause_hard_max_tokens: 450
  section_soft_max_tokens: 900
  semantic_split_enabled: false
  llm_boundary_adjudication: false

citation_extraction:
  eyecite_enabled: true
  custom_extractors:
    - krs
    - kar

reference_extraction:
  custom_extractors:
    - doi_bulletin
    - serff
    - form_id
    - endorsement_id
    - manual_id
    - current_guideline
    - coverage_part
    - notice_period
    - generic_law_reference

retrieval:
  mode_default: exact_then_lexical
  graph_expand_depth: 1
  include_parent_context: true
  include_cited_authorities: true
  future_signals:
    - semantic
    - graph
    - citation
    - reference
    - metadata

storage:
  backend: files

schemas:
  schema_version: "002.1.0"
  require_schema_validation: true
```

## Suggested Package Shape

For the first stage, keep this under the stage directory rather than promoting to shared tooling too early:

```text
stages/002-homeowners-discovery-instrumentation/
  STAGE.md
  LESSON.md
  schema/
  data/
    heuristics.md
    source_manifest_subset.csv
  src/
    legal_ingest/
      config/
      models/
      parsers/
      normalize/
      chunking/
      citations/
      graph/
      retrieval/
      storage/
      cli/
  output/
    run_manifest.json
  tests/
```

If the stage proves reusable, promote the package later.

## Minimum Schema Outlines

Stage 002 implementation should create full JSON Schemas, but these three artifacts are especially load-bearing.

The three inline outlines below are normative minimums. The remaining schemas under `schema/` must at least cover the required fields named in this Stage 002 spec.

If an artifact is not listed under `schema/`, it is experimental and not part of the Stage 002 contract. Experimental artifacts must not become Stage 003+ dependencies without being added to `schema/` and versioned.

`nodes.schema.json` must require at least:

- `schema_version`
- `run_id`
- `created_at`
- `node_id`
- `source_id`
- `node_type`
- `section_path`
- `page_start`
- `page_end`
- `parser_block_ids`
- `text`

`candidate_evidence.schema.json` must require at least:

- `schema_version`
- `run_id`
- `created_at`
- `candidate_id`
- `source_id`
- `node_id`
- `smell`
- `candidate_type`
- `evidence_text`
- `why_flagged`
- `heuristic_rule_id`
- `heuristic_version`
- `status`

`retrieval_bundle.schema.json` must require at least:

- `schema_version`
- `run_id`
- `created_at`
- `bundle_id`
- `hits`

Each retrieval hit must require:

- `node_id`
- `signal_scores`

`signal_scores` must include:

- `exact`
- `lexical`
- `graph`
- `citation`
- `reference`
- `metadata`
- `semantic`
- `parser_penalty`

## Acceptance Tests

Parsing:

- PDF or HTML source becomes structured blocks.
- Source path and provenance are retained.
- Headings, lists, and tables are detected or warnings are emitted.
- parser run records are emitted
- block stats are emitted
- table failures and reading-order uncertainty are visible
- failed parses produce `parser_runs.jsonl.status = failed` and a `failure_reason`; sources are not silently dropped
- JSONL files are UTF-8 encoded with one JSON object per line

Chunking:

- numbered exclusions stay intact
- definition clauses remain atomic
- endorsement headers stay attached to body
- no chunk exceeds hard max without warning

Citation extraction:

- KRS references are extracted
- KAR references are extracted
- formal legal citations are recorded in `citations.jsonl`
- DOI bulletin/advisory identifiers are extracted where present into `references.jsonl`
- filing/form/endorsement/manual identifiers are captured by custom reference extractors
- partial or failed normalization is visible

Retrieval:

- exact phrase query returns expected clause
- metadata filters exclude wrong smell/source type/company where metadata exists
- retrieval bundle includes parent context
- retrieval bundle includes citations, broader references, parser diagnostics, or unresolved records where present
- retrieval bundle schema has slots for semantic, graph, citation, reference, and metadata signals even when semantic scores are null

Graph:

- parent-child edges are created
- next edges are created between sibling nodes
- reference/citation edges are created
- override/amend edges are recognized only where detectable from explicit text

Candidate evidence:

- lexical candidate scans emit candidate evidence for the five active smells where the selected corpus supports them
- each candidate includes source, node, why flagged, heuristic rule ID/version, machinery confidence, cost pool, and reviewer question
- candidates are not presented as final findings

Schema and run identity:

- all JSON/JSONL records include `schema_version`, `run_id`, and `created_at`
- `run_manifest.json` records corpus root, parsers used, schema versions, config snapshot, and high-level parse stats
- schema validation catches unplanned field drift
- standard Stage 002 outputs are not mutated by any LLM-assisted helper notes

## Tiny Gold Set

Create a tiny versioned gold set from real corpus documents:

- 10 statute/regulation sections
- 10 policy or manual clauses
- 5 endorsement or form fragments
- 5 rate/manual fragments

For each record, annotate:

- expected node boundaries
- citations present
- parent section
- 3-5 test queries
- expected relevant nodes

Gold-set rules:

- use real snippets only, not synthetic clauses
- cover all five active smells at least minimally where the corpus supports them
- store as a versioned artifact such as `data/goldsets/goldset-002.1.json`
- record expected node IDs and the schema version used to create the gold set

## Open Decisions

- When does Phase 1 earn Docling if simple HTML/PDF extraction is enough for the first source subset?
- When does retrieval quality justify embeddings?
- If embeddings are justified, should the first vector experiment use local files, Qdrant, or Postgres plus pgvector?
- Which source subset best covers all five smells without chasing known SERFF gaps?
- Are deterministic node IDs stable enough under the chosen parser strategy, or do we need a stronger structural-path alignment pass?
- Which heuristic rules belong in Stage 002 candidate generation versus Stage 004 detectors?


