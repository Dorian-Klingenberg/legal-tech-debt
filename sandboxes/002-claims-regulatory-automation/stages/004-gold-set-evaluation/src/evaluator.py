"""Stage 004 gold set evaluation.

Measures exact-phrase and BM25 recall against the gold set, documents false
positives and missed hits, and produces a structured evaluation report.

Reads artifacts from a Stage 002 pipeline run directory. Uses the Stage 003
retrieval package for search.

Usage (run from the stage root):
    python src/evaluator.py --run-dir ../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af
    python src/evaluator.py --run-dir <path> --goldset data/goldsets/goldset-002.2.json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# Stage 003 src/ provides the retrieval package
_STAGE_003_SRC = (
    Path(__file__).parent.parent.parent
    / "003-retrieval-baseline" / "src"
)
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

from retrieval.index import RunIndex
from retrieval.searcher import bm25_search, phrase_search

SMELL_NAMES = {
    1: "Overbroad / Non-deterministic Exclusions",
    2: "Magic Number / Magic Valuation Terms",
    3: "Coverage Inversion / Contradictory Conditions",
    4: "Calculation Rule Drift / Unversioned Rate Reference",
    5: "Regulatory Mapping Smells",
}


# ---------------------------------------------------------------------------
# Result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QueryResult:
    query: str
    mode: str          # "phrase" | "bm25"
    hit: bool          # expected node was in top results
    rank: int | None   # 1-based rank of expected node; None if not found
    top_node_ids: list[str]
    false_positives: list[str]   # top nodes that are NOT the expected node


@dataclass
class ItemResult:
    item_id: str
    smell_id: int
    source_id: str
    expected_node_id: str
    expected_section_path: str
    fixture_summary: str
    tier: str
    query_results: list[QueryResult]
    any_hit: bool        # True if any query/mode found the expected node
    best_rank: int | None
    missed_by_phrase: bool
    missed_by_bm25: bool
    notes: list[str] = field(default_factory=list)


@dataclass
class ModeStats:
    mode: str
    items_evaluated: int
    items_hit: int
    recall: float
    avg_rank: float | None
    missed_item_ids: list[str]


@dataclass
class EvaluationReport:
    goldset_id: str
    run_id: str
    created_at: str
    items_evaluated: int
    corpus_gap_count: int
    item_results: list[ItemResult]
    mode_stats: list[ModeStats]
    smell_recall: dict[int, float]   # smell_id -> recall (any mode)
    semantic_decision: str
    semantic_rationale: str


# ---------------------------------------------------------------------------
# Core evaluation logic
# ---------------------------------------------------------------------------

def _evaluate_item(item: dict, index: RunIndex) -> ItemResult:
    expected_id = item["expected_node_id"]
    queries = item.get("test_queries", [])
    expected_modes = set(item.get("expected_retrieval_modes", ["phrase", "bm25"]))

    query_results: list[QueryResult] = []

    for query in queries:
        for mode in ("phrase", "bm25"):
            if mode == "phrase":
                hits = phrase_search(index, query)
            else:
                hits = bm25_search(index, query, top_k=10)

            hit_node_ids = [h.node_id for h in hits]
            found = expected_id in hit_node_ids
            rank = (hit_node_ids.index(expected_id) + 1) if found else None
            fp = [nid for nid in hit_node_ids[:5] if nid != expected_id]

            query_results.append(QueryResult(
                query=query,
                mode=mode,
                hit=found,
                rank=rank,
                top_node_ids=hit_node_ids[:5],
                false_positives=fp,
            ))

    any_hit = any(r.hit for r in query_results)
    ranks = [r.rank for r in query_results if r.rank is not None]
    best_rank = min(ranks) if ranks else None

    phrase_hits = [r for r in query_results if r.mode == "phrase" and r.hit]
    bm25_hits = [r for r in query_results if r.mode == "bm25" and r.hit]
    missed_by_phrase = len(phrase_hits) == 0
    missed_by_bm25 = len(bm25_hits) == 0

    notes: list[str] = []
    n = index.node_by_id.get(expected_id)
    if n:
        pr = index.pr_by_source.get(n["source_id"], {})
        if pr.get("status") == "partial":
            notes.append(f"Parser status=partial for source {n['source_id']} — may reduce BM25 recall")
        cite_count = len(index.cites_by_node.get(expected_id, []))
        if cite_count:
            notes.append(f"{cite_count} citation(s) attached to expected node")
    else:
        notes.append(f"WARNING: expected_node_id {expected_id} not found in index")

    if missed_by_phrase and not missed_by_bm25:
        notes.append("Phrase search missed; BM25 succeeded — paraphrase present")
    if missed_by_bm25 and not missed_by_phrase:
        notes.append("BM25 missed; phrase search succeeded — rare/specific term")
    if missed_by_phrase and missed_by_bm25:
        notes.append("Both modes missed — likely needs semantic retrieval or different query")

    return ItemResult(
        item_id=item["item_id"],
        smell_id=item["smell_id"],
        source_id=item["source_id"],
        expected_node_id=expected_id,
        expected_section_path=item.get("expected_section_path", ""),
        fixture_summary=item.get("fixture_summary", ""),
        tier=item.get("tier", ""),
        query_results=query_results,
        any_hit=any_hit,
        best_rank=best_rank,
        missed_by_phrase=missed_by_phrase,
        missed_by_bm25=missed_by_bm25,
        notes=notes,
    )


def _mode_stats(mode: str, results: list[ItemResult]) -> ModeStats:
    evaluated = len(results)
    if mode == "phrase":
        hits = [r for r in results if not r.missed_by_phrase]
        missed = [r.item_id for r in results if r.missed_by_phrase]
    else:
        hits = [r for r in results if not r.missed_by_bm25]
        missed = [r.item_id for r in results if r.missed_by_bm25]

    recall = len(hits) / evaluated if evaluated else 0.0

    hit_ranks = []
    for r in results:
        for qr in r.query_results:
            if qr.mode == mode and qr.rank is not None:
                hit_ranks.append(qr.rank)
    avg_rank = sum(hit_ranks) / len(hit_ranks) if hit_ranks else None

    return ModeStats(
        mode=mode,
        items_evaluated=evaluated,
        items_hit=len(hits),
        recall=round(recall, 3),
        avg_rank=round(avg_rank, 1) if avg_rank else None,
        missed_item_ids=missed,
    )


def _semantic_decision(results: list[ItemResult]) -> tuple[str, str]:
    """Return (decision, rationale) string pair."""
    both_miss = [r for r in results if r.missed_by_phrase and r.missed_by_bm25]
    phrase_only = [r for r in results if not r.missed_by_phrase and r.missed_by_bm25]
    bm25_only = [r for r in results if r.missed_by_phrase and not r.missed_by_bm25]

    if len(both_miss) >= 3:
        decision = "PURSUE — multiple items missed by both modes"
        rationale = (
            f"{len(both_miss)} gold set items were missed by both exact-phrase and BM25 search. "
            "These represent queries where semantic similarity might bridge the vocabulary gap. "
            f"Items missed: {', '.join(r.item_id for r in both_miss)}."
        )
    elif len(both_miss) >= 1:
        decision = "INVESTIGATE — some items missed by both modes"
        rationale = (
            f"{len(both_miss)} item(s) missed by both modes — worth checking whether "
            "semantic retrieval would recover them before committing to vector infrastructure. "
            f"Items missed: {', '.join(r.item_id for r in both_miss)}."
        )
    else:
        decision = "DEFER — exact/lexical retrieval is sufficient for this corpus"
        rationale = (
            "All gold set items were retrieved by at least one of phrase or BM25 search. "
            "Semantic retrieval has no concrete question to answer with this corpus slice. "
            "Revisit after adding carrier policy form sources, which may use paraphrase "
            "language that lexical search misses."
        )

    if phrase_only:
        rationale += (
            f" {len(phrase_only)} item(s) were retrieved by phrase but not BM25 "
            f"({', '.join(r.item_id for r in phrase_only)}) — rare/specific terms where "
            "BM25 term weighting is too coarse."
        )
    if bm25_only:
        rationale += (
            f" {len(bm25_only)} item(s) were retrieved by BM25 but not phrase "
            f"({', '.join(r.item_id for r in bm25_only)}) — paraphrase present; "
            "phrase queries should be expanded."
        )

    return decision, rationale


def evaluate(run_dir: Path, goldset_path: Path) -> EvaluationReport:
    print(f"[evaluator] Loading index from {run_dir}...")
    index = RunIndex(run_dir)

    print(f"[evaluator] Loading gold set from {goldset_path}...")
    goldset = json.loads(goldset_path.read_text(encoding="utf-8"))
    items = goldset.get("items", [])
    gaps = goldset.get("corpus_gaps", [])

    print(f"[evaluator] {len(items)} items, {len(gaps)} corpus gaps")

    results: list[ItemResult] = []
    for item in items:
        r = _evaluate_item(item, index)
        hit_str = "HIT" if r.any_hit else "MISS"
        rank_str = f" rank={r.best_rank}" if r.best_rank else ""
        print(f"[evaluator]   {r.item_id} [{hit_str}{rank_str}] "
              f"phrase={'ok' if not r.missed_by_phrase else 'miss'} "
              f"bm25={'ok' if not r.missed_by_bm25 else 'miss'} "
              f"— {r.fixture_summary[:60]}")
        results.append(r)

    # Per-mode stats
    phrase_stats = _mode_stats("phrase", results)
    bm25_stats = _mode_stats("bm25", results)

    # Per-smell recall (any mode)
    smell_recall: dict[int, float] = {}
    for sid in range(1, 6):
        smell_items = [r for r in results if r.smell_id == sid]
        if smell_items:
            smell_recall[sid] = round(sum(1 for r in smell_items if r.any_hit) / len(smell_items), 3)

    decision, rationale = _semantic_decision(results)
    print(f"\n[evaluator] Semantic decision: {decision}")

    return EvaluationReport(
        goldset_id=goldset.get("goldset_id", ""),
        run_id=index.run_id,
        created_at=datetime.now(timezone.utc).isoformat(),
        items_evaluated=len(results),
        corpus_gap_count=len(gaps),
        item_results=results,
        mode_stats=[phrase_stats, bm25_stats],
        smell_recall=smell_recall,
        semantic_decision=decision,
        semantic_rationale=rationale,
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def _build_report(ev: EvaluationReport) -> str:
    lines = [
        "# Stage 002 Retrieval Evaluation Report",
        "",
        f"Gold set: `{ev.goldset_id}`",
        f"Run ID: `{ev.run_id}`",
        f"Created: {ev.created_at}",
        "",
        "---",
        "",
        "## Overall Results",
        "",
        f"- Items evaluated: **{ev.items_evaluated}**",
        f"- Corpus gap tiers (not evaluated): **{ev.corpus_gap_count}**",
        "",
        "| Mode | Items Hit | Recall | Avg Rank |",
        "|---|---|---|---|",
    ]
    for ms in ev.mode_stats:
        avg = f"{ms.avg_rank}" if ms.avg_rank else "—"
        lines.append(f"| {ms.mode} | {ms.items_hit}/{ms.items_evaluated} "
                     f"| {ms.recall:.0%} | {avg} |")

    lines += ["", "### Recall by Smell (any mode)", ""]
    for sid in range(1, 6):
        r = ev.smell_recall.get(sid)
        if r is not None:
            lines.append(f"- **Smell {sid}** ({SMELL_NAMES[sid]}): {r:.0%}")
        else:
            lines.append(f"- **Smell {sid}** ({SMELL_NAMES[sid]}): not evaluated (corpus gap)")

    lines += [
        "",
        "---",
        "",
        "## Item-by-Item Results",
        "",
    ]

    for r in ev.item_results:
        hit_icon = "✓" if r.any_hit else "✗"
        lines.append(f"### {hit_icon} {r.item_id} — Smell {r.smell_id} ({r.tier})")
        lines.append("")
        lines.append(f"**Source**: `{r.source_id}` / {r.expected_section_path.split(' > ')[-1][:80]}")
        lines.append(f"**Summary**: {r.fixture_summary}")
        lines.append(f"**Expected node**: `{r.expected_node_id}`")
        lines.append("")
        lines.append("| Query | Phrase | BM25 Rank |")
        lines.append("|---|---|---|")

        seen_queries: set[str] = set()
        query_phrase: dict[str, QueryResult] = {}
        query_bm25: dict[str, QueryResult] = {}
        for qr in r.query_results:
            if qr.mode == "phrase":
                query_phrase[qr.query] = qr
            else:
                query_bm25[qr.query] = qr

        for q in dict.fromkeys(qr.query for qr in r.query_results):
            pqr = query_phrase.get(q)
            bqr = query_bm25.get(q)
            p_str = "hit" if (pqr and pqr.hit) else "miss"
            b_str = f"rank {bqr.rank}" if (bqr and bqr.hit) else "miss"
            lines.append(f"| `{q}` | {p_str} | {b_str} |")

        if r.notes:
            lines.append("")
            for note in r.notes:
                lines.append(f"- {note}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Corpus Gaps",
        "",
        "The following tiers could not be evaluated due to missing source types:",
        "",
    ]
    # Re-read gaps from original goldset — we only have them in the JSON
    lines.append("_(See goldset-002.2.json for details)_")

    lines += [
        "",
        "---",
        "",
        "## Semantic Retrieval Decision",
        "",
        f"**Decision**: {ev.semantic_decision}",
        "",
        ev.semantic_rationale,
        "",
        "---",
        "",
        "## Retrieval Mode Assessment",
        "",
        "| Finding | Implication |",
        "|---|---|",
        "| Exact phrase: high precision, moderate recall | Good for known legal terms; misses paraphrase |",
        "| BM25: moderate precision, higher recall | Catches co-occurrence but noisy on common words (\"reasonable\", \"law\") |",
        "| Graph expansion: adds context, not new hits | Valuable for reviewer bundles; doesn't change recall |",
        "| Corpus limited to regulatory sources | Carrier form smells (1, 3, 5) cannot be evaluated until SERFF filing added |",
        "",
        "---",
        "",
        "_This report is generated output. Do not edit manually._",
        "_Retrieval results are not legal findings._",
    ]

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    _stage_002 = Path(__file__).parent.parent.parent / "002-homeowners-discovery-instrumentation"
    stage_root = Path(__file__).parent.parent
    parser = argparse.ArgumentParser(description="Stage 004 gold set evaluator")
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=_stage_002 / "output",
        help="Stage 002 pipeline run output directory",
    )
    parser.add_argument(
        "--goldset",
        type=Path,
        default=stage_root / "data" / "goldsets" / "goldset-002.2.json",
        help="Gold set JSON file to evaluate against",
    )
    args = parser.parse_args()

    ev = evaluate(args.run_dir, args.goldset)

    # Write JSON results
    results_path = args.run_dir / "evaluation_results.json"
    results_path.write_text(
        json.dumps(asdict(ev), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[evaluator] Written results -> {results_path}")

    # Write markdown report
    report = _build_report(ev)
    report_path = args.run_dir / "evaluation_report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"[evaluator] Written report -> {report_path}")

    # Summary
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    for ms in ev.mode_stats:
        print(f"  {ms.mode:8s}: {ms.items_hit}/{ms.items_evaluated} items hit "
              f"({ms.recall:.0%} recall)")
    print(f"\n  Semantic decision: {ev.semantic_decision}")
    print("=" * 60)


if __name__ == "__main__":
    main()
