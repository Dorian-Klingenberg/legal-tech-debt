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

    return RetrievalBundle(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        bundle_id=id_gen.bundle_id(hit.matched_query, hit.node_id),
        query=hit.matched_query,
        hit_node_id=hit.node_id,
        source_id=n["source_id"],
        source_title=doc["title"] if doc else n["source_id"],
        source_type=src.get("source_type", ""),
        section_path=n.get("section_path", ""),
        why_retrieved=why,
        hit_text=(n.get("retrievable_text") or n.get("text") or "")[:500],
        parent_node_id=exp.parent_node_id,
        parent_text=exp.parent_text,
        adjacent_node_ids=exp.adjacent_node_ids,
        citation_ids=exp.citation_ids,
        reference_ids=exp.reference_ids,
        parser_run_id=index.pr_by_source.get(n["source_id"], {}).get("parser_run_id", ""),
        parser_confidence=exp.parser_confidence,
        signal_scores={hit.match_type: hit.score},
    )
