"""Assemble RetrievalBundle records from search hits and graph expansions."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

# Stage 002 src/ provides models.py and ids.py
_STAGE_002_SRC = (
    Path(__file__).parent.parent.parent.parent
    / "002-homeowners-discovery-instrumentation" / "src"
)
if str(_STAGE_002_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_002_SRC))

import ids as id_gen
from models import SCHEMA_VERSION, RetrievalBundle

from .expander import expand
from .index import RunIndex
from .searcher import SearchHit


def compose(
    index: RunIndex,
    hit: SearchHit,
    run_id: str,
    smell_id: int | None = None,
) -> RetrievalBundle | None:
    now = datetime.now(timezone.utc).isoformat()
    n = index.node_by_id.get(hit.node_id)
    if not n:
        return None

    exp = expand(index, hit.node_id)

    doc_nodes = {nd["source_id"]: nd for nd in index.nodes if nd.get("node_type") == "document"}
    doc = doc_nodes.get(n["source_id"])
    src = index.source_by_id.get(n["source_id"], {})

    why: list[str] = [f"{hit.match_type} match on {hit.matched_query!r} (score={hit.score})"]
    why.extend(exp.notes)
    if smell_id:
        why.append(f"smell_id={smell_id}")

    signal_scores = {
        "exact": hit.score if hit.match_type == "phrase" else 0.0,
        "lexical": hit.score if hit.match_type == "bm25" else 0.0,
        "graph": 1.0 if (exp.parent_node_id or exp.adjacent_node_ids) else 0.0,
        "citation": 1.0 if exp.citation_ids else 0.0,
        "reference": 1.0 if exp.reference_ids else 0.0,
        "metadata": 1.0 if src else 0.0,
        "semantic": None,
        "parser_penalty": 0.0 if exp.parser_confidence == "high" else 0.25 if exp.parser_confidence == "medium" else 0.5,
    }

    hit_record = {
        "node_id": hit.node_id,
        "rank": hit.rank,
        "score": hit.score,
        "node_type": n.get("node_type", ""),
        "text": (n.get("retrievable_text") or n.get("text") or "")[:500],
        "source": {
            "source_id": n["source_id"],
            "source_hash": n.get("source_hash", ""),
            "title": doc["title"] if doc else n["source_id"],
            "source_type": src.get("source_type", ""),
            "url": src.get("url", ""),
        },
        "section_path": n.get("section_path", ""),
        "pages": [n["page_number"]] if n.get("page_number") is not None else [],
        "why_retrieved": why,
        "candidate_ids": [],
        "signal_scores": signal_scores,
        "parser_diagnostics": {
            "parser_run_id": index.pr_by_source.get(n["source_id"], {}).get("parser_run_id", ""),
            "reading_order_confidence": 1.0 if exp.parser_confidence == "high" else 0.75,
            "warnings": [],
        },
        "expanded_context": {
            "parent_section": {
                "node_id": exp.parent_node_id,
                "text": exp.parent_text,
            } if exp.parent_node_id else None,
            "adjacent_nodes": exp.adjacent_node_ids,
            "citations": exp.citation_ids,
            "references": exp.reference_ids,
            "overrides": [],
        },
    }

    return RetrievalBundle(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        bundle_id=id_gen.bundle_id(hit.matched_query, hit.node_id),
        query_text=hit.matched_query,
        task_description="Stage 003 retrieval baseline bundle",
        filters={"smell_id": smell_id} if smell_id else {},
        hits=[hit_record],
    )
