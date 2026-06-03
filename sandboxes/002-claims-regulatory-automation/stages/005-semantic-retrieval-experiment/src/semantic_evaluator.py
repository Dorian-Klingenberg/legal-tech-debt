"""
Semantic retrieval evaluation against goldset-002.2.json.

Adds a 'semantic' retrieval mode alongside phrase and BM25 from Stage 004.
Writes semantic_evaluation_results.json and semantic_evaluation_report.md
into the Stage 002 run directory.

Usage:
    python src/semantic_evaluator.py --run-dir ../002-homeowners-discovery-instrumentation/output/<run_id>
    python src/semantic_evaluator.py --run-dir <path> --goldset <path> --top-k 10
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

# Cross-stage: Stage 003 src for RunIndex (via Stage 002 path in composer)
_STAGE_003_SRC = (
    Path(__file__).parent.parent.parent
    / "003-retrieval-baseline" / "src"
)
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

from retrieval.index import RunIndex  # type: ignore  # noqa: E402

from embedder import embed_run  # noqa: E402
from semantic_searcher import cosine_search  # noqa: E402

DEFAULT_GOLDSET = (
    Path(__file__).parent.parent.parent
    / "004-gold-set-evaluation" / "data" / "goldsets" / "goldset-002.2.json"
)
DEFAULT_TOP_K = 10


@dataclass
class ItemResult:
    item_id: str
    smell_id: int
    tier: str
    expected_node_id: str
    fixture_summary: str
    semantic_hit: bool
    best_rank: int | None
    best_score: float | None
    queries_tried: list[str]


@dataclass
class EvaluationReport:
    run_id: str
    goldset_id: str
    top_k: int
    model: str
    total_items: int
    semantic_hits: int
    semantic_recall: float
    decision: str
    decision_rationale: str
    items: list[ItemResult]
    created_at: str


def _evaluate_item(item: dict, run_dir: Path, top_k: int, model: str) -> ItemResult:
    expected_id = item["expected_node_id"]
    queries = item.get("test_queries", [])
    best_rank = None
    best_score = None

    for query in queries:
        hits = cosine_search(run_dir, query, top_k=top_k, model=model)
        for h in hits:
            if h.node_id == expected_id:
                if best_rank is None or h.rank < best_rank:
                    best_rank = h.rank
                    best_score = h.score
                break

    return ItemResult(
        item_id=item["item_id"],
        smell_id=item["smell_id"],
        tier=item["tier"],
        expected_node_id=expected_id,
        fixture_summary=item.get("fixture_summary", ""),
        semantic_hit=best_rank is not None,
        best_rank=best_rank,
        best_score=round(best_score, 4) if best_score is not None else None,
        queries_tried=queries,
    )


def _semantic_decision(results: list[ItemResult]) -> tuple[str, str]:
    hit_rate = sum(1 for r in results if r.semantic_hit) / max(len(results), 1)
    if hit_rate >= 0.95:
        return "DEFER", f"Semantic recall {hit_rate:.0%} — lexical is sufficient; defer vector store."
    if hit_rate >= 0.80:
        return "INVESTIGATE", f"Semantic recall {hit_rate:.0%} — marginal gains; investigate hybrid before committing to a store."
    return "PURSUE", f"Semantic recall {hit_rate:.0%} — meaningful gap; semantic retrieval earns a vector store experiment."


def evaluate(run_dir: Path, goldset_path: Path, top_k: int = 10, model: str = "text-embedding-3-small") -> EvaluationReport:
    print(f"[semantic-eval] Ensuring embeddings exist in {run_dir}...")
    embed_run(run_dir, model=model)

    idx = RunIndex(run_dir)

    goldset = json.loads(goldset_path.read_text(encoding="utf-8"))
    items = goldset["items"]
    print(f"[semantic-eval] {len(items)} gold set items")

    results = []
    for item in items:
        r = _evaluate_item(item, run_dir, top_k=top_k, model=model)
        hit_str = f"rank={r.best_rank} score={r.best_score}" if r.semantic_hit else "MISS"
        print(f"[semantic-eval]   {r.item_id} [{hit_str}] {r.fixture_summary[:60]}")
        results.append(r)

    hits = sum(1 for r in results if r.semantic_hit)
    recall = hits / max(len(results), 1)
    decision, rationale = _semantic_decision(results)

    report = EvaluationReport(
        run_id=idx.run_id,
        goldset_id=goldset["goldset_id"],
        top_k=top_k,
        model=model,
        total_items=len(results),
        semantic_hits=hits,
        semantic_recall=round(recall, 4),
        decision=decision,
        decision_rationale=rationale,
        items=results,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    # Write JSON results
    results_path = run_dir / "semantic_evaluation_results.json"
    results_path.write_text(
        json.dumps(asdict(report), indent=2, default=str),
        encoding="utf-8",
    )
    print(f"[semantic-eval] Written results -> {results_path}")

    # Write markdown report
    _write_report(report, run_dir / "semantic_evaluation_report.md", run_dir)
    print(f"[semantic-eval] Written report -> {run_dir / 'semantic_evaluation_report.md'}")

    return report


def _write_report(report: EvaluationReport, path: Path, run_dir: Path) -> None:
    idx = RunIndex(run_dir)
    lines = [
        f"# Semantic Retrieval Evaluation Report",
        f"",
        f"Run: `{report.run_id}`  ",
        f"Gold set: `{report.goldset_id}`  ",
        f"Model: `{report.model}`  ",
        f"Top-K: {report.top_k}  ",
        f"Generated: {report.created_at}",
        f"",
        f"## Summary",
        f"",
        f"| Mode | Recall | Items |",
        f"|---|---|---|",
        f"| Semantic (cosine@{report.top_k}) | {report.semantic_recall:.0%} | {report.semantic_hits}/{report.total_items} |",
        f"",
        f"**Decision: {report.decision}** — {report.decision_rationale}",
        f"",
        f"## Per-Item Results",
        f"",
        f"| Item | Tier | Smell | Hit | Rank | Score | Summary |",
        f"|---|---|---|---|---|---|---|",
    ]
    for r in report.items:
        hit = "yes" if r.semantic_hit else "**MISS**"
        rank = str(r.best_rank) if r.best_rank else "—"
        score = f"{r.best_score:.4f}" if r.best_score else "—"
        summary = r.fixture_summary[:60]
        lines.append(f"| {r.item_id} | {r.tier} | {r.smell_id} | {hit} | {rank} | {score} | {summary} |")

    misses = [r for r in report.items if not r.semantic_hit]
    if misses:
        lines += [
            f"",
            f"## Missed Items",
            f"",
        ]
        for r in misses:
            node = idx.node_by_id.get(r.expected_node_id, {})
            node_text = (node.get("text") or "")[:300]
            lines += [
                f"### {r.item_id} — {r.fixture_summary}",
                f"",
                f"- Expected node: `{r.expected_node_id}`",
                f"- Queries tried: {r.queries_tried}",
                f"- Node text (first 300 chars): {node_text!r}",
                f"",
            ]

    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic retrieval evaluation")
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--goldset", type=Path, default=DEFAULT_GOLDSET)
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--model", default="text-embedding-3-small")
    args = parser.parse_args()

    report = evaluate(args.run_dir, args.goldset, top_k=args.top_k, model=args.model)

    print()
    print("=" * 60)
    print("SEMANTIC EVALUATION SUMMARY")
    print("=" * 60)
    print(f"  semantic : {report.semantic_hits}/{report.total_items} items hit ({report.semantic_recall:.0%} recall)")
    print(f"")
    print(f"  Decision: {report.decision} -- {report.decision_rationale}")
    print("=" * 60)
