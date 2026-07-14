"""
Smell 5 model diagnostic: compare text-embedding-3-small vs text-embedding-3-large
on the five paraphrase gold set items (eval-022 through eval-026).

For each query:
  - Shows cosine score of the expected node under both models
  - Shows top-5 nodes returned by each model
  - Indicates whether the expected node appears in top-10

Usage:
    python src/smell5_model_diagnostic.py --run-dir ../../output/002/20260604_130606_18b0dec5
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np

# Env + path setup (same pattern as embedder.py)
def _load_env() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent.parent.parent
    env_path = repo_root / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

_load_env()

import openai  # noqa: E402

_STAGE_003_SRC = Path(__file__).parent.parent.parent / "003-retrieval-baseline" / "src"
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

from retrieval.index import RunIndex  # type: ignore
from paths import stage_output_dir  # type: ignore

PARAPHRASE_ITEMS = ["eval-022", "eval-023", "eval-024", "eval-025", "eval-026"]
MODELS = ["text-embedding-3-small", "text-embedding-3-large"]
TOP_K = 10

GOLDSET_PATH = (
    Path(__file__).parent.parent.parent
    / "004-gold-set-evaluation" / "data" / "goldsets" / "goldset-002.2.json"
)


def embed_texts(texts: list[str], model: str) -> np.ndarray:
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.embeddings.create(input=texts, model=model)
    return np.array([r.embedding for r in response.data], dtype=np.float32)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))


def run_diagnostic(run_dir: Path) -> None:
    idx = RunIndex(run_dir)
    nodes = idx.content_nodes
    node_by_id = {n["node_id"]: n for n in nodes}

    goldset = json.loads(GOLDSET_PATH.read_text(encoding="utf-8"))
    items = {it["item_id"]: it for it in goldset["items"]}

    paraphrase_items = [items[i] for i in PARAPHRASE_ITEMS]

    # Build corpus texts once
    node_ids = [n["node_id"] for n in nodes]
    corpus_texts = [
        ((n.get("heading") or "") + " " + (n.get("text") or "")).strip()[:8000]
        for n in nodes
    ]

    print(f"\nCorpus: {len(nodes)} nodes from run {idx.run_id}")
    print(f"Paraphrase items: {PARAPHRASE_ITEMS}\n")

    for model in MODELS:
        print("=" * 70)
        print(f"MODEL: {model}")
        print("=" * 70)

        print(f"  Embedding {len(nodes)} corpus nodes...", end=" ", flush=True)
        corpus_matrix = embed_texts(corpus_texts, model)
        print("done")

        for item in paraphrase_items:
            query = item["test_queries"][0]
            expected_id = item["expected_node_id"]
            expected_node = node_by_id.get(expected_id, {})
            expected_text = (
                (expected_node.get("heading") or "") + " " +
                (expected_node.get("text") or "")
            ).strip()[:120]

            print(f"\n  [{item['item_id']}] {item['fixture_summary'][:70]}")
            print(f"  Query: \"{query}\"")
            print(f"  Expected node: {expected_id} | {expected_text!r}")

            q_vec = embed_texts([query], model)[0]
            scores = [(node_ids[i], cosine(q_vec, corpus_matrix[i])) for i in range(len(node_ids))]
            scores.sort(key=lambda x: x[1], reverse=True)

            expected_rank = next(
                (rank + 1 for rank, (nid, _) in enumerate(scores) if nid == expected_id),
                None
            )
            expected_score = next((s for nid, s in scores if nid == expected_id), None)

            hit_str = f"rank={expected_rank}, score={expected_score:.4f}" if expected_rank and expected_rank <= TOP_K else \
                      f"NOT IN TOP-{TOP_K} (rank={expected_rank}, score={expected_score:.4f})" if expected_rank else "NOT FOUND"
            print(f"  Expected node result: {hit_str}")

            print(f"  Top 5 returned:")
            for rank, (nid, score) in enumerate(scores[:5], 1):
                n = node_by_id.get(nid, {})
                snippet = ((n.get("heading") or "") + " " + (n.get("text") or "")).strip()[:80]
                marker = " <-- TARGET" if nid == expected_id else ""
                print(f"    {rank}. [{score:.4f}] {nid[:12]}... {snippet!r}{marker}")

    print("\n" + "=" * 70)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()
    run_diagnostic(args.run_dir)
