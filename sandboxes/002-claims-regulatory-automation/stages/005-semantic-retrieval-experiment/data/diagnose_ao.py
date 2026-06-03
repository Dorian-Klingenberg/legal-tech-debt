import sys, json
from pathlib import Path

sys.path.insert(0, str(Path("../003-retrieval-baseline/src")))
from retrieval.index import RunIndex

run_dir = Path("../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af")
idx = RunIndex(run_dir)

nodes = [n for n in idx.nodes if n.get("source_id") == "KY-DOI-AO-2023-08"]
print(f"{len(nodes)} nodes from KY-DOI-AO-2023-08")
for n in nodes:
    text = n.get("text") or ""
    has_aerial = "aerial" in text.lower()
    nid = n["node_id"]
    ntype = n.get("node_type")
    heading = repr((n.get("heading") or "")[:40])
    print(f"  {nid} type={ntype} heading={heading} aerial={has_aerial} len={len(text)}")
    if has_aerial:
        idx2 = text.lower().index("aerial")
        print(f"    snippet: {repr(text[max(0,idx2-50):idx2+100])}")

# Also grep all blocks for aerial
print()
blocks = [b for b in idx.nodes if "aerial" in (b.get("text") or "").lower()]
print(f"Nodes containing 'aerial': {len(blocks)}")
