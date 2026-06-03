"""
Validate goldset-002.2.json against the actual run output.
For each item: node exists, source matches, at least one query term appears in node text.
"""
import json, sys, re
from pathlib import Path

sys.path.insert(0, str(Path("../003-retrieval-baseline/src")))
from retrieval.index import RunIndex

run_dir = Path("../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af")
goldset_path = Path("../004-gold-set-evaluation/data/goldsets/goldset-002.2.json")

idx = RunIndex(run_dir)
goldset = json.loads(goldset_path.read_text(encoding="utf-8"))

issues = []
print(f"Validating {len(goldset['items'])} items against run {idx.run_id[:8]}\n")
print(f"{'item':<12} {'node_exists':<13} {'source_ok':<12} {'query_match':<13} {'node_text_preview'}")
print("-" * 90)

for item in goldset["items"]:
    iid = item["item_id"]
    expected_id = item["expected_node_id"]
    expected_source = item["source_id"]
    queries = item.get("test_queries", [])

    node = idx.node_by_id.get(expected_id)
    node_exists = node is not None
    source_ok = node.get("source_id") == expected_source if node else False
    text = (node.get("text") or "") if node else ""
    text_lower = text.lower()

    # Check if any query term (or significant word from it) appears in node text
    query_match = any(
        any(word.lower() in text_lower for word in q.split() if len(word) > 3)
        for q in queries
    )

    preview = repr(text[:80]) if text else "EMPTY"
    flag = "" if (node_exists and source_ok and query_match) else " <-- ISSUE"

    print(f"{iid:<12} {str(node_exists):<13} {str(source_ok):<12} {str(query_match):<13} {preview}{flag}")

    if not node_exists:
        issues.append(f"{iid}: node {expected_id} not found in run")
    elif not source_ok:
        issues.append(f"{iid}: expected source {expected_source}, got {node.get('source_id')}")
    elif not query_match:
        issues.append(f"{iid}: none of {queries} match node text (text: {repr(text[:120])})")

print()
if issues:
    print(f"ISSUES ({len(issues)}):")
    for iss in issues:
        print(f"  - {iss}")
else:
    print("All items OK.")
