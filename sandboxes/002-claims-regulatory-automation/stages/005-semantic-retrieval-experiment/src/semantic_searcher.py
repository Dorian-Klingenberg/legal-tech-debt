"""
Cosine similarity search over cached node embeddings.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from embedder import embed_query, load_embeddings


@dataclass
class SemanticHit:
    node_id: str
    score: float
    rank: int


def cosine_search(
    run_dir: Path,
    query: str,
    top_k: int = 10,
    model: str = "text-embedding-3-small",
) -> list[SemanticHit]:
    node_ids, matrix = load_embeddings(run_dir)
    q_vec = embed_query(query, model=model)

    # Normalise
    q_norm = q_vec / (np.linalg.norm(q_vec) + 1e-10)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-10
    normed = matrix / norms

    scores = normed @ q_norm
    top_idx = np.argsort(-scores)[:top_k]

    return [
        SemanticHit(node_id=node_ids[i], score=float(scores[i]), rank=rank + 1)
        for rank, i in enumerate(top_idx)
    ]
