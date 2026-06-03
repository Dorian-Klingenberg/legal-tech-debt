import sys, json
from pathlib import Path

sys.path.insert(0, str(Path("../003-retrieval-baseline/src")))
sys.path.insert(0, "src")

from retrieval.index import RunIndex
from embedder import _load_env
_load_env()
from semantic_searcher import cosine_search

run_dir = Path("../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af")
idx = RunIndex(run_dir)

node_id = "bdfadc8c3e7aec8ab312"
node = idx.node_by_id.get(node_id, {})
print("=== eval-011 node ===")
print("node_type:", node.get("node_type"))
print("heading:", repr(node.get("heading")))
print("text:", repr((node.get("text") or "")[:800]))
print("source_id:", node.get("source_id"))
print()

queries = ["aerial imagery", "property inspection", "available information", "aerial", "inspection"]
for q in queries:
    hits = cosine_search(run_dir, q, top_k=15)
    target_rank = next((h.rank for h in hits if h.node_id == node_id), None)
    top3 = [(h.rank, h.score, idx.node_by_id.get(h.node_id, {}).get("heading", "")[:40]) for h in hits[:3]]
    print(f"Query: {q!r}")
    print(f"  Target rank: {target_rank}")
    print(f"  Top 3: {top3}")
    print()
