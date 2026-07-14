"""
Embed Stage 002 nodes via OpenAI text-embedding-3-small and cache to a .npy + index file.

Usage:
    python src/embedder.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
    python src/embedder.py --run-dir <path> --model text-embedding-3-small --batch-size 64
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

def _load_env() -> None:
    """Load .env from repo root into os.environ if not already set."""
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

import openai  # noqa: E402  (after env load)

# Cross-stage: Stage 003 src for RunIndex (which itself imports Stage 002 src)
_STAGE_003_SRC = (
    Path(__file__).parent.parent.parent
    / "003-retrieval-baseline" / "src"
)
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

from retrieval.index import RunIndex  # type: ignore  # noqa: E402
from paths import stage_output_dir  # type: ignore  # noqa: E402

EMBED_INDEX_FILE = "semantic_embed_index.json"
EMBED_MATRIX_FILE = "semantic_embeddings.npy"


def _batched(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def embed_run(run_dir: Path, model: str = "text-embedding-3-small", batch_size: int = 64) -> None:
    out_dir = stage_output_dir("005", run_dir)
    index_path = out_dir / EMBED_INDEX_FILE
    matrix_path = out_dir / EMBED_MATRIX_FILE

    if index_path.exists() and matrix_path.exists():
        print(f"[embedder] Cache exists — skipping. Delete {EMBED_INDEX_FILE} to re-embed.")
        return

    print(f"[embedder] Loading index from {run_dir}...")
    idx = RunIndex(run_dir)
    nodes = idx.content_nodes
    print(f"[embedder] {len(nodes)} content nodes to embed")

    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    node_ids = []
    all_embeddings = []

    for batch_num, batch in enumerate(_batched(nodes, batch_size)):
        texts = [
            (n.get("heading") or "") + " " + (n.get("text") or "")
            for n in batch
        ]
        texts = [t.strip()[:8000] for t in texts]  # API token limit guard

        print(f"[embedder] Batch {batch_num + 1}: {len(texts)} nodes...", end=" ", flush=True)
        t0 = time.monotonic()

        response = client.embeddings.create(input=texts, model=model)
        vecs = [r.embedding for r in response.data]

        elapsed = time.monotonic() - t0
        print(f"{elapsed:.1f}s")

        node_ids.extend(n["node_id"] for n in batch)
        all_embeddings.extend(vecs)

        # Small pause to stay well under rate limits
        if batch_num > 0 and batch_num % 5 == 0:
            time.sleep(1)

    matrix = np.array(all_embeddings, dtype=np.float32)
    np.save(matrix_path, matrix)

    embed_index = {
        "model": model,
        "run_id": idx.run_id,
        "node_count": len(node_ids),
        "dim": matrix.shape[1],
        "node_ids": node_ids,
    }
    index_path.write_text(json.dumps(embed_index, indent=2), encoding="utf-8")

    print(f"[embedder] Saved {len(node_ids)} embeddings ({matrix.shape}) -> {out_dir}")


def load_embeddings(run_dir: Path) -> tuple[list[str], np.ndarray]:
    """Return (node_ids, matrix) from cached files in the stage 005 output dir."""
    out_dir = stage_output_dir("005", run_dir)
    index_path = out_dir / EMBED_INDEX_FILE
    matrix_path = out_dir / EMBED_MATRIX_FILE
    if not index_path.exists() or not matrix_path.exists():
        raise FileNotFoundError(f"No embedding cache in {out_dir}. Run embedder.py first.")
    embed_index = json.loads(index_path.read_text(encoding="utf-8"))
    matrix = np.load(matrix_path)
    return embed_index["node_ids"], matrix


def embed_query(query: str, model: str = "text-embedding-3-small") -> np.ndarray:
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.embeddings.create(input=[query], model=model)
    return np.array(response.data[0].embedding, dtype=np.float32)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Embed Stage 002 nodes via OpenAI")
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--model", default="text-embedding-3-small")
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()
    embed_run(args.run_dir, model=args.model, batch_size=args.batch_size)
