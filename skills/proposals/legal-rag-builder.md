# Skill Proposal: legal-rag-builder

Status: captured source notes

Distilled artifacts:

- Repo spec: `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md`
- Draft skill: `skills/legal-rag-builder/SKILL.md`

This file preserves the original proposal and Perplexity brain dump. Do not treat it as the installable skill body.

## Recurring Workflow

Build or extend the local-first legal document ingestion and retrieval system for Sandbox 002.

This workflow will recur whenever an agent needs to work on parsing, normalizing, chunking, citation extraction, graph-linked nodes, retrieval bundles, or evaluation for the Kentucky homeowners corpus.

## Why This Should Be A Skill

The RAG system has several project-specific constraints that generic coding agents are likely to miss:

- Legal structure matters more than fixed token windows.
- Retrieval should return evidence bundles, not orphan chunks.
- Provenance must survive every transformation.
- The first implementation should be deterministic and file-backed before any database or vector service is introduced.
- The active corpus and known gaps already exist under Sandbox 002.
- The system must stay aligned to Kentucky homeowners and the five policy-layer smells unless scope is explicitly reopened.

## Source Of Truth

The skill should point to these repo documents:

- `BOOTSTRAP.md`
- `skills/README.md`
- `skills/SKILL-DEVELOPMENT.md`
- `sandboxes/002-claims-regulatory-automation/002-claims-regulatory-automation-README.md`
- `sandboxes/002-claims-regulatory-automation/002-five-policy-layer-phish.md`
- `sandboxes/002-claims-regulatory-automation/HANDOFF-2026-06-01.md`
- `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`
- `sandboxes/002-claims-regulatory-automation/002-RAG-INGESTION-RETRIEVAL-SPEC.md` once created

## Trigger Examples

- "Build the legal RAG ingestion pipeline for Sandbox 002."
- "Add citation extraction for Kentucky statutes and regulations."
- "Create structural chunks from the homeowners corpus."
- "Make a retrieval bundle for a policy smell query."
- "Compare Qdrant and pgvector for the legal corpus."

## Guardrails

- Do not start with a chatbot or polished UI.
- Do not use naive fixed-window chunking as the primary strategy.
- Do not rely on pure vector search alone.
- Do not collapse ingestion, retrieval, and reasoning into one opaque prompt.
- Do not add Postgres, Qdrant, services, or APIs until a stage explicitly earns that infrastructure.
- Do not procure more SERFF material unless the active task runs into a documented known gap.

## First Validation Task

After the repo-level RAG spec exists, draft the `legal-rag-builder` skill and validate it against this dry-run task:

> Given the Sandbox 002 corpus manifest, propose a file-backed first ingestion stage that preserves source metadata, emits normalized nodes, extracts KRS/KAR citations, and writes a retrieval bundle for one exact-phrase query.

The validation should prove that the skill keeps the agent focused on deterministic ingestion and legal structure before retrieval infrastructure.

## The following is a brain dump from Perplexity, who I was initially having the conversation with about developing this skill with. 

Mission
Build a local-first legal document ingestion and retrieval system for a legal-tech research sandbox. The system must ingest statutes, regulations, bulletins, homeowners policy forms, endorsements, manuals, and filings; preserve legal structure; extract citations; build graph-linked nodes; and support hybrid retrieval for downstream legal analysis.

Non-goals
Do not build a generic chatbot first.

Do not start with UI polish.

Do not use naive fixed-window chunking as the primary strategy.

Do not rely on pure vector search alone.

Do not collapse the whole pipeline into one opaque agent prompt.

Core stack
Recommended baseline:

Parser: Docling

Chunk/index orchestration: LlamaIndex abstractions where helpful

Citation extraction: Eyecite + custom Kentucky citation regexes

Retrieval store: either

Qdrant if hybrid dense+sparse retrieval should be first-class from day one,

or Postgres + pgvector if relational joins, metadata, and a single database are more important early on.

Product requirements
The system must:

ingest PDF, HTML, DOCX, Markdown, and text-like filing artifacts

preserve page numbers and section hierarchy where available

detect legal units: document, section, subsection, clause, list item, definition, table, endorsement

extract formal legal citations and custom domain references

store both node text and structured metadata

create graph edges between nodes and authorities

support exact phrase search, semantic search, metadata filtering, and graph neighbor expansion

return retrieval bundles, not orphan chunks

Domain assumptions
Primary domain is insurance/legal-regulatory text. Legal meaning is often carried by:

headings

numbered subsections

provisos

definition sections

endorsement headers

cross-references

tables

citations

Therefore chunk boundaries must respect legal structure instead of token windows alone.

Architecture
Pipeline
Acquire

input source file or URL

register source metadata

compute source hash for dedup/versioning

Parse

use Docling to convert to structured document representation or Markdown

preserve page references, headings, tables, and reading order if possible

Normalize

canonical intermediate schema:

Document

Block

PageRef

SectionPath

TableBlock

CitationCandidate

Segment

structure-first segmentation

semantic fallback segmentation inside oversize units

optional LLM boundary adjudication only for malformed/OCR-heavy cases

Extract

metadata

citations

defined terms

cross-references

form IDs / endorsement IDs / statute-reg references

Graph build

create nodes and edges

Index

vector embeddings

lexical index / sparse vectors / BM25 equivalent

metadata payloads

graph adjacency

Retrieve

hybrid recall

rerank

graph expansion

package context bundle

Explain

always provide provenance and “why retrieved”

Data model
Sources table
source

source_id

title

source_type

jurisdiction

url

content_hash

effective_date

revision_date

company_name

line_of_business

status

created_at

Document nodes
node

node_id

source_id

node_type (document, section, clause, list_item, definition, table, endorsement, citation)

parent_node_id

ordinal

text

normalized_text

section_path

page_start

page_end

token_count

embedding_status

metadata_json

Edges
edge

edge_id

source_id

from_node_id

to_node_id

edge_type

confidence

evidence_text

metadata_json

Citations
citation

citation_id

source_id

node_id

citation_text

citation_type (case, statute, regulation, bulletin, form_id, endorsement_id, filing_id)

normalized_citation

resolver_target

confidence

Retrieval cache / query logs
query_log

query_id

query_text

filters_json

retrieval_mode

created_at

Node types and edge types
Node types
document

section

subsection

clause

list_item

definition

table

endorsement

citation

summary

Edge types
contains

next

references

defines_term

uses_defined_term

cites_statute

cites_regulation

cites_bulletin

amends

overrides

same_topic

derived_from_summary

Chunking policy
Default chunking rules
Never split a heading from the paragraph that immediately follows it.

Never split a definition term from its definition body.

Never split a numbered list item across chunks unless it is extremely long.

Never split tables into row fragments unless there is a dedicated table serializer.

Keep endorsement titles attached to endorsement body text.

Preserve parent-child relationships rather than adding huge text overlap.

Suggested sizes
Clause/list-item nodes: 150–400 tokens

Section nodes: 400–1200 tokens

Summary nodes: one concise summary per section and one per document

Overlap: minimal, structural only; prefer graph edges over repeated text

Smart chunking algorithm
Pseudo-logic:

detect structural blocks from parser output

group contiguous blocks into legal units

if legal unit <= soft token max, emit node

if unit > soft token max:

split by subsection markers

else split by paragraph boundaries

else apply semantic boundary detection

else use LLM adjudication

create parent section node containing references to child nodes

create summary node for parent section

link all child nodes to parent

Citation extraction
Eyecite usage
Run Eyecite on normalized text blocks to extract formal legal citations.

Custom extractors needed
Add regex/parsers for:

KRS xxx.xxx-xxx

806 KAR xx:xxx

DOI bulletin/advisory formats

SERFF tracking numbers

form numbers

endorsement numbers

policy manual identifiers

Citation resolution
For each extracted citation:

normalize string

classify type

attempt resolver lookup

create citation node if useful

create edge from source clause to authority

Retrieval design
Retrieval modes
Exact phrase

for phrases like “arising out of” or “as announced”

Semantic

embedding-based retrieval for meaning similarity

Metadata-filtered

jurisdiction, company, source_type, filing, date, smell class

Hybrid

combine sparse and dense retrieval using reciprocal rank fusion or equivalent

Graph expansion

after top hits, expand to:

parent section

adjacent clause

cited authority

endorsements that amend base text

Retrieval bundle format
Return:

json
{
  "query": "...",
  "filters": {...},
  "hits": [
    {
      "node_id": "...",
      "score": 0.92,
      "node_type": "clause",
      "text": "...",
      "source": {...},
      "section_path": "...",
      "pages": [12, 13],
      "why_retrieved": ["exact phrase", "semantic similarity", "citation expansion"],
      "neighbors": {
        "parent_section": {...},
        "adjacent_nodes": [...],
        "citations": [...],
        "overrides": [...]
      }
    }
  ]
}
The bundle must be human-readable and machine-usable.

Storage choice guidance
Option A: Qdrant
Choose Qdrant if:

you want built-in hybrid dense+sparse search early,

metadata filtering should be native,

you want cleaner retrieval experimentation.

Implementation notes:

enable hybrid from the beginning in LlamaIndex integration

use payload metadata for jurisdiction, source type, company, dates

use RRF/weighted fusion for sparse+dense results

Option B: Postgres + pgvector
Choose pgvector if:

you want one database,

graph edges and metadata are easier to manage relationally,

you want SQL joins between embeddings and structured legal metadata.

Implementation notes:

keep node, edge, citation, and source relational

store embeddings on node

use HNSW or IVFFlat index as appropriate

combine with Postgres full-text search for hybrid behavior

use SQL filters before or alongside vector ranking

My recommendation
Start with Postgres + pgvector if you value simplicity and one-system control. Start with Qdrant if retrieval quality experimentation is the main goal. Both are valid.

API / internal service contract
Ingest document
POST /ingest

input: file path or URL + metadata

output:

source record

node count

citation count

edge count

parse warnings

Rebuild embeddings
POST /embed/:source_id

embed all nodes missing vectors

Search
POST /search

input:

query text

filters

retrieval mode

top_k

graph expansion depth

output:

retrieval bundle

Explain node
GET /node/:node_id

full node

parent path

incoming/outgoing edges

citations

source provenance

Compare authority
POST /compare

input:

node_id or text block

authority citation

output:

aligned text comparison bundle

Config knobs
Codex should implement config for:

text
parser:
  engine: docling
  ocr_enabled: true

chunking:
  clause_soft_max_tokens: 300
  clause_hard_max_tokens: 450
  section_soft_max_tokens: 900
  semantic_split_enabled: true
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
  mode_default: hybrid
  hybrid_weights:
    sparse: 1.0
    dense: 1.2
  graph_expand_depth: 1
  include_parent_context: true
  include_cited_authorities: true

storage:
  backend: pgvector   # or qdrant
Build order
Tell Codex to build in this order:

project skeleton

source registry + database schema

Docling parser adapter

normalized document schema

structural chunker

citation extractor service with Eyecite

embedding pipeline

vector/lexical retrieval

graph edge builder

retrieval bundle composer

evaluation tests

CLI or minimal API

Do not start with the agent interface. Start with deterministic ingestion and retrieval primitives.

Acceptance tests
Codex should implement tests for:

Parsing
PDF becomes structured blocks

page numbers retained where available

headings/lists/tables detected

Chunking
numbered exclusions stay intact

definition clauses remain atomic

endorsement header stays attached to body

no chunk exceeds hard max without warning

Citation extraction
KRS and KAR references extracted

Eyecite extracts supported legal citations

filing/form identifiers captured by custom extractors

Retrieval
exact phrase query returns expected clause

semantic query finds paraphrased clause

metadata filters exclude wrong jurisdiction/company

hybrid beats dense-only on a curated legal query set

Graph
parent-child edges created

reference edges created

override/amend edges recognized where detectable

Evaluation set
Create a tiny gold set from real documents:

10 statute/reg sections

10 policy clauses

5 endorsements

5 rate/manual fragments

For each, annotate:

expected node boundaries

citations present

parent section

3–5 test queries

expected relevant nodes

This gives measurable chunking and retrieval quality.

Code organization
Suggested package layout:

text
legal_ingest/
  config/
  models/
  parsers/
    docling_adapter.py
  normalize/
  chunking/
    structural.py
    semantic.py
    llm_adjudicator.py
  citations/
    eyecite_adapter.py
    custom_extractors.py
    resolvers.py
  graph/
    builders.py
    traversal.py
  retrieval/
    embeddings.py
    lexical.py
    hybrid.py
    bundle.py
  storage/
    postgres.py
    qdrant.py
  api/
  cli/
  tests/
Developer principles for Codex
Tell Codex:

prefer deterministic code over magical prompting

every output object must carry provenance

no lossy transformations without preserving original text

legal structure beats generic NLP heuristics

graph links are preferable to giant overlap windows

retrieval should return evidence bundles, not just text

every module must be swappable

configuration must be explicit and inspectable

Reading list for Codex implementation
Docling main docs: 
docling-project.github.io/docling

Docling + LlamaIndex integration: 
Docling LlamaIndex integration

LlamaIndex chunking basics: 
Basic Strategies

LlamaIndex metadata filtering: 
Metadata Filtering

Eyecite whitepaper: 
free.law/pdf/eyecite-whitepaper.pdf

Qdrant filtering: 
Qdrant Filtering

Qdrant hybrid queries: 
Qdrant Hybrid Queries

LlamaIndex + Qdrant hybrid: 
Qdrant Hybrid Search

pgvector overview and SQL-join rationale: 
pgvector guide

pgvector deep dive: 
Severalnines pgvector article

Recommendation
The most effective next move is to have me turn this brain dump into a formal engineering handoff document with:

requirements

architecture

schemas

milestones

prompts for Codex

and a phased implementation checklist

That would be the most useful artifact to hand directly to Codex.

