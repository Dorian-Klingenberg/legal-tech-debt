import json
from pathlib import Path

run_dir = Path("../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af")
s4 = json.loads((run_dir / "evaluation_results.json").read_text(encoding="utf-8"))
s5 = json.loads((run_dir / "semantic_evaluation_results.json").read_text(encoding="utf-8"))

items4 = {i["item_id"]: i for i in s4["item_results"]}
items5 = {i["item_id"]: i for i in s5["items"]}

print(f"{'item_id':<14} {'phrase':<7} {'bm25':<7} {'semantic':<10} hybrid")
print("-" * 55)
hybrid_hits = 0
for iid in sorted(items4.keys(), key=lambda x: int(x.split("-")[1])):
    i4 = items4[iid]
    i5 = items5.get(iid, {})
    ph = not i4["missed_by_phrase"]
    bm = not i4["missed_by_bm25"]
    se = i5.get("semantic_hit", False)
    hybrid = ph or bm or se
    if hybrid:
        hybrid_hits += 1
    row = f"{iid:<14} {str(ph):<7} {str(bm):<7} {str(se):<10} {'HIT' if hybrid else 'MISS'}"
    print(row)

total = len(items4)
phrase_hits = sum(1 for i in items4.values() if not i["missed_by_phrase"])
bm25_hits = sum(1 for i in items4.values() if not i["missed_by_bm25"])
sem_hits = sum(1 for i in items5.values() if i.get("semantic_hit"))
print()
print(f"Phrase:   {phrase_hits}/{total} = {phrase_hits/total:.0%}")
print(f"BM25:     {bm25_hits}/{total} = {bm25_hits/total:.0%}")
print(f"Semantic: {sem_hits}/{total} = {sem_hits/total:.0%}")
print(f"Hybrid:   {hybrid_hits}/{total} = {hybrid_hits/total:.0%}")

# What does semantic add that BM25 misses?
bm25_misses = {iid for iid, i in items4.items() if i["missed_by_bm25"]}
sem_only_hits = {iid for iid, i in items5.items() if i.get("semantic_hit") and iid in bm25_misses}
print()
print(f"Semantic rescues (BM25 miss -> semantic hit): {sorted(sem_only_hits)}")

# What does semantic miss that BM25 hits?
bm25_hits_ids = {iid for iid, i in items4.items() if not i["missed_by_bm25"]}
sem_misses = {iid for iid, i in items5.items() if not i.get("semantic_hit")}
bm25_only = sem_misses & bm25_hits_ids
print(f"BM25-only hits (semantic misses these): {sorted(bm25_only)}")
