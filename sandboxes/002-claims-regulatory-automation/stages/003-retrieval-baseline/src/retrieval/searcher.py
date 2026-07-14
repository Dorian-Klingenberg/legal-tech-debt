"""Exact phrase search, BM25 lexical search, and metadata filtering."""
from __future__ import annotations

import math
import re
from dataclasses import dataclass

from .index import RunIndex


@dataclass
class SearchHit:
    node_id: str
    score: float
    match_type: str        # "phrase" | "bm25"
    matched_query: str
    context_snippet: str   # ~160 chars around the match
    rank: int = 1


def phrase_search(
    index: RunIndex,
    query: str,
    source_type: str | None = None,
) -> list[SearchHit]:
    """Return one hit per node that contains the exact phrase (case-insensitive)."""
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    hits: list[SearchHit] = []
    for n in index.content_nodes:
        if source_type and index.source_by_id.get(n["source_id"], {}).get("source_type") != source_type:
            continue
        text = n.get("text") or ""
        m = pattern.search(text)
        if m:
            start = max(0, m.start() - 80)
            end = min(len(text), m.end() + 80)
            hits.append(SearchHit(
                node_id=n["node_id"],
                score=1.0,
                match_type="phrase",
                matched_query=query,
                context_snippet=text[start:end].strip(),
                rank=len(hits) + 1,
            ))
    return hits


def bm25_search(
    index: RunIndex,
    query: str,
    top_k: int = 10,
    source_type: str | None = None,
) -> list[SearchHit]:
    """BM25 scoring over content nodes. Returns top_k results."""
    k1, b = 1.5, 0.75
    query_terms = re.findall(r"\b[a-z]{2,}\b", query.lower())
    if not query_terms or not index._node_terms:
        return []

    N = len(index._node_terms)
    avg_dl = sum(len(t) for t in index._node_terms.values()) / N

    scores: dict[str, float] = {}
    for term in query_terms:
        df = len(index._term_index.get(term, set()))
        if df == 0:
            continue
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
        for nid in index._term_index.get(term, set()):
            tf = index._node_terms[nid].count(term)
            dl = len(index._node_terms[nid])
            tf_norm = tf * (k1 + 1) / (tf + k1 * (1 - b + b * dl / avg_dl))
            scores[nid] = scores.get(nid, 0.0) + idf * tf_norm

    hits: list[SearchHit] = []
    for nid, score in sorted(scores.items(), key=lambda x: -x[1]):
        n = index.node_by_id.get(nid)
        if not n:
            continue
        if source_type and index.source_by_id.get(n["source_id"], {}).get("source_type") != source_type:
            continue
        text = n.get("text") or ""
        hits.append(SearchHit(
            node_id=nid,
            score=round(score, 4),
            match_type="bm25",
            matched_query=query,
            context_snippet=text[:160].strip(),
            rank=len(hits) + 1,
        ))
        if len(hits) >= top_k:
            break
    return hits


def metadata_filter(
    index: RunIndex,
    source_types: list[str] | None = None,
    smell_ids: list[int] | None = None,
) -> list[dict]:
    """Return nodes matching source_type and/or smell_id filters."""
    results = []
    for n in index.content_nodes:
        src = index.source_by_id.get(n["source_id"], {})
        if source_types and src.get("source_type") not in source_types:
            continue
        if smell_ids:
            node_smells = {e["smell_id"] for e in index.ev_by_node.get(n["node_id"], [])}
            if not node_smells.intersection(smell_ids):
                continue
        results.append(n)
    return results
