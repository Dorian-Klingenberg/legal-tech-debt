import sys
from pathlib import Path

sys.path.insert(0, str(Path("../003-retrieval-baseline/src")))
from retrieval.index import RunIndex

run_dir = Path("../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af")
idx = RunIndex(run_dir)

aerial_nodes = [n for n in idx.nodes if "aerial" in (n.get("text") or "").lower()]
print(f"Nodes containing 'aerial': {len(aerial_nodes)}")
for n in aerial_nodes:
    text = n.get("text") or ""
    i = text.lower().index("aerial")
    print(f"  node_id={n['node_id']} source={n.get('source_id')} type={n.get('node_type')}")
    print(f"  snippet: {repr(text[max(0,i-80):i+150])}")
    print()

# Full text of eval-011 node
print("=== Full text of bdfadc8c3e7aec8ab312 ===")
n = idx.node_by_id["bdfadc8c3e7aec8ab312"]
print(n.get("text"))
