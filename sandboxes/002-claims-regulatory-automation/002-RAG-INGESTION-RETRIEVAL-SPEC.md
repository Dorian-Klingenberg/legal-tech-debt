# RAG Ingestion and Retrieval Spec

Status: Draft engineering spec
Scope: Sandbox 002 Kentucky homeowners corpus
Created: 2026-06-01
Source notes: `skills/proposals/legal-rag-builder.md`
Planning docs:

- `002-RAG-SUBSYSTEM-PLAN.md`
- `002-RAG-PHASE-PLAN.md`
- `../../skills/legal-rag-builder/adr/ADR-001-rag-substrate-reuses-001-structure.md`
- `../../skills/legal-rag-builder/adr/ADR-002-semantic-vector-retrieval-deferred-not-dropped.md`

## Mission

Build a local-first legal document ingestion and retrieval system for the Sandbox 002 Kentucky homeowners research corpus.

The system should ingest statutes, regulations, DOI bulletins, homeowners policy forms, endorsements, manuals, and filings; preserve legal structure; extract citations and domain references; create graph-linked nodes; and return retrieval bundles suitable for downstream legal tech debt analysis.

This is proof-of-concept infrastructure for research, not a production platform.

## Non-Goals

- Do not build a generic chatbot first.
- Do not start with UI polish.
- Do not use naive fixed-window chunking as the primary strategy.
- Do not rely on pure vector search alone.
- Do not collapse ingestion, retrieval, and legal analysis into one opaque agent prompt.
- Do not add databases, services, queues, containers, or production APIs until a sandbox stage explicitly earns them.

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

For the first implementation stage, use file-backed JSON/JSONL/CSV outputs before choosing a retrieval store. This preserves the sandbox rule against premature infrastructure while still shaping the code around later storage backends.

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

### Phase 1: File-Backed Ingestion Slice

Goal:

> Prove that the corpus can be ingested into legal-structure nodes with provenance, citations, and graph edges using plain local files.

Inputs:

- a small subset from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- 1-2 sources per active smell where practical

Deliverables:

- `stages/003-homeowners-rag-ingestion/STAGE.md`
- `stages/003-homeowners-rag-ingestion/LESSON.md`
- `data/source_manifest_subset.csv`
- `output/sources.jsonl`
- `output/nodes.jsonl`
- `output/citations.jsonl`
- `output/edges.jsonl`
- `output/retrieval_bundles.json`

Success criteria:

- page or source location is preserved where available
- section hierarchy is represented
- KRS and KAR references are extracted
- exact phrase search can return a bundle for at least one smell phrase
- graph expansion includes parent section and cited authority when available

### Phase 2: Retrieval Evaluation

Goal:

> Compare exact phrase, lexical, semantic, and hybrid retrieval on a tiny gold set before adding durable storage.

Deliverables:

- tiny gold set from real corpus excerpts
- 3-5 test queries per selected source group
- comparison report showing where exact, lexical, semantic, and hybrid retrieval help

Decision gate:

- Choose whether retrieval quality requires vector embeddings now.
- Choose whether a local library/index is enough before introducing Qdrant or pgvector.

### Phase 3: Storage Decision

Only after Phases 1-2, decide whether to prototype:

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
- `Node`
- `PageRef`
- `SectionPath`
- `TableBlock`
- `CitationCandidate`
- `Segment`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`

Normalize only after preserving original text.

Domain findings are not part of the RAG substrate. Findings, smell classifications, severity, ROI mapping, reviewer questions, and human-review state belong to downstream detector and reporting layers.

### Segment

- use structure-first segmentation
- use semantic fallback only inside oversized units
- reserve LLM boundary adjudication for malformed or OCR-heavy cases

### Extract

Extract:

- citations
- defined terms
- cross-references
- form IDs
- endorsement IDs
- SERFF tracking numbers
- policy manual identifiers
- statute and regulation references

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

### Source

Fields:

- `source_id`
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
- `source_id`
- `node_type`
- `parent_node_id`
- `ordinal`
- `text`
- `normalized_text`
- `section_path`
- `page_start`
- `page_end`
- `token_count`
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

### Edge

Fields:

- `edge_id`
- `source_id`
- `from_node_id`
- `to_node_id`
- `edge_type`
- `confidence`
- `evidence_text`
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
- `same_topic`
- `derived_from_summary`

### Citation

Fields:

- `citation_id`
- `source_id`
- `node_id`
- `citation_text`
- `citation_type`
- `normalized_citation`
- `resolver_target`
- `confidence`

Citation types:

- `case`
- `statute`
- `regulation`
- `bulletin`
- `form_id`
- `endorsement_id`
- `filing_id`

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

## Citation Extraction

Use Eyecite where it fits formal legal citations.

Add custom extractors for:

- Kentucky statutes: `KRS xxx.xxx-xxx`
- Kentucky regulations: `806 KAR xx:xxx`
- DOI bulletins and advisory opinions
- SERFF tracking numbers
- form numbers
- endorsement numbers
- policy manual identifiers

For each extracted citation:

1. preserve the original citation text
2. normalize the citation
3. classify citation type
4. attempt resolver lookup when a resolver exists
5. create a citation record
6. create an edge from the source node to the authority node or unresolved citation target

## Retrieval Bundle Contract

Return human-readable and machine-usable retrieval bundles.

```json
{
  "query": "...",
  "filters": {},
  "hits": [
    {
      "node_id": "...",
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
      "neighbors": {
        "parent_section": {},
        "adjacent_nodes": [],
        "citations": [],
        "overrides": []
      }
    }
  ]
}
```

## Configuration Knobs

Use explicit config. Initial file-backed defaults:

```yaml
parser:
  engine: docling
  ocr_enabled: false

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
    - doi_bulletin
    - serff
    - form_id
    - endorsement_id

retrieval:
  mode_default: exact_then_lexical
  graph_expand_depth: 1
  include_parent_context: true
  include_cited_authorities: true

storage:
  backend: files
```

## Suggested Package Shape

For the first stage, keep this under the stage directory rather than promoting to shared tooling too early:

```text
stages/003-homeowners-rag-ingestion/
  STAGE.md
  LESSON.md
  data/
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
  tests/
```

If the stage proves reusable, promote the package later.

## Acceptance Tests

Parsing:

- PDF or HTML source becomes structured blocks.
- Source path and provenance are retained.
- Headings, lists, and tables are detected or warnings are emitted.

Chunking:

- numbered exclusions stay intact
- definition clauses remain atomic
- endorsement headers stay attached to body
- no chunk exceeds hard max without warning

Citation extraction:

- KRS references are extracted
- KAR references are extracted
- DOI bulletin/advisory identifiers are extracted where present
- filing/form/endorsement identifiers are captured by custom extractors

Retrieval:

- exact phrase query returns expected clause
- metadata filters exclude wrong smell/source type/company where metadata exists
- retrieval bundle includes parent context
- retrieval bundle includes citations or unresolved citation records where present

Graph:

- parent-child edges are created
- next edges are created between sibling nodes
- reference/citation edges are created
- override/amend edges are recognized only where detectable from explicit text

## Tiny Gold Set

Create a tiny gold set from real corpus documents:

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

## Open Decisions

- When does Phase 1 earn Docling if simple HTML/PDF extraction is enough for the first source subset?
- When does retrieval quality justify embeddings?
- If embeddings are justified, should the first vector experiment use local files, Qdrant, or Postgres plus pgvector?
- Which source subset best covers all five smells without chasing known SERFF gaps?


