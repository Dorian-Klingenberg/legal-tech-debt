"""Stage 003 retrieval baseline runner.

Runs smell-specific queries (exact phrase + BM25) over a Stage 002 pipeline run
directory, expands hits via the graph, composes retrieval bundles, and writes
outputs back into that run directory.

Usage (run from the stage root):
    python src/retrieval_runner.py --run-dir ../002-homeowners-discovery-instrumentation/output/20260603_180716_996e36af
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

_SRC = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from retrieval.composer import compose
from retrieval.index import RunIndex
from retrieval.searcher import SearchHit, bm25_search, phrase_search
from paths import stage_output_dir

# ---------------------------------------------------------------------------
# Smell query definitions
# Each smell has a list of (query_text, search_mode) tuples.
# "phrase" = exact phrase search; "bm25" = lexical scoring.
# ---------------------------------------------------------------------------

SMELL_QUERIES: dict[int, list[tuple[str, str]]] = {
    1: [
        ("including but not limited to", "phrase"),
        ("arising from or related to", "phrase"),
        ("directly or indirectly", "phrase"),
        ("any loss or damage", "phrase"),
        ("all losses", "bm25"),
        ("exclude", "bm25"),
    ],
    2: [
        ("reasonable", "bm25"),
        ("actual cash value", "phrase"),
        ("replacement cost value", "phrase"),
        ("replacement cost", "bm25"),
        ("current manual", "phrase"),
        ("current guidelines", "phrase"),
        ("fair market value", "phrase"),
    ],
    3: [
        ("all risk", "phrase"),
        ("all direct physical loss", "phrase"),
        ("subject to all terms", "phrase"),
        ("except as provided", "phrase"),
        ("coverage is provided", "bm25"),
        ("insuring agreement", "bm25"),
    ],
    4: [
        ("underwriting guidelines", "phrase"),
        ("rating guidelines", "phrase"),
        ("as amended", "phrase"),
        ("from time to time", "phrase"),
        ("current edition", "phrase"),
        ("manual", "bm25"),
        ("rate manual", "phrase"),
    ],
    5: [
        ("as required by law", "phrase"),
        ("as required by state law", "phrase"),
        ("as permitted by law", "phrase"),
        ("pursuant to applicable law", "phrase"),
        ("in accordance with applicable law", "phrase"),
        ("applicable law", "bm25"),
    ],
}

SMELL_NAMES = {
    1: "Overbroad / Non-deterministic Exclusions",
    2: "Magic Number / Magic Valuation Terms",
    3: "Coverage Inversion / Contradictory Conditions",
    4: "Calculation Rule Drift / Unversioned Rate Reference",
    5: "Regulatory Mapping Smells",
}

# Expected source types that carry each smell (for corpus gap documentation)
SMELL_SOURCE_TYPES = {
    1: ["serff_form_filing"],
    2: ["serff_form_filing", "serff_rate_rule_filing", "doi_bulletin", "kar_regulation"],
    3: ["serff_form_filing"],
    4: ["serff_rate_rule_filing"],
    5: ["serff_form_filing", "serff_correspondence", "serff_rate_rule_filing"],
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(run_dir: Path) -> None:
    print(f"[retrieval_runner] Loading index from {run_dir}...")
    index = RunIndex(run_dir)
    run_id = index.run_id

    print(f"[retrieval_runner] {len(index.content_nodes)} content nodes, "
          f"{len(index.citations)} citations, {len(index.references)} references")

    present_source_types = {
        index.source_by_id.get(n["source_id"], {}).get("source_type", "")
        for n in index.content_nodes
    }

    all_bundles: dict[str, dict] = {}   # bundle_id -> bundle dict
    smell_results: dict[int, list[dict]] = {i: [] for i in range(1, 6)}
    corpus_gaps: list[dict] = []

    for smell_id, queries in SMELL_QUERIES.items():
        print(f"\n[retrieval_runner] Smell {smell_id}: {SMELL_NAMES[smell_id]}")

        # Check if corpus can support this smell
        expected = SMELL_SOURCE_TYPES[smell_id]
        covered = [t for t in expected if t in present_source_types]
        if not covered:
            gap_msg = (
                f"Smell {smell_id} requires source types {expected}; "
                f"corpus only contains {sorted(present_source_types)}."
            )
            print(f"[retrieval_runner]   CORPUS GAP: {gap_msg}")
            corpus_gaps.append({
                "smell_id": smell_id,
                "smell_name": SMELL_NAMES[smell_id],
                "requires_source_types": expected,
                "present_source_types": sorted(present_source_types),
                "gap_note": gap_msg,
            })

        seen_nodes: set[str] = set()

        for query, mode in queries:
            if mode == "phrase":
                hits = phrase_search(index, query)
            else:
                hits = bm25_search(index, query, top_k=5)

            for hit in hits:
                if hit.node_id in seen_nodes:
                    continue
                seen_nodes.add(hit.node_id)

                bundle = compose(index, hit, run_id, smell_id=smell_id)
                if bundle is None:
                    continue

                bd = dataclasses.asdict(bundle)
                all_bundles[bundle.bundle_id] = bd
                first_hit = bundle.hits[0] if bundle.hits else {}
                source = first_hit.get("source", {})
                smell_results[smell_id].append({
                    "bundle_id": bundle.bundle_id,
                    "query": query,
                    "mode": mode,
                    "source_id": source.get("source_id", ""),
                    "source_type": source.get("source_type", ""),
                    "section_path": first_hit.get("section_path", ""),
                    "parser_confidence": first_hit.get("parser_diagnostics", {}).get("reading_order_confidence", ""),
                    "hit_text_excerpt": (first_hit.get("text") or "")[:200],
                    "why_retrieved": first_hit.get("why_retrieved", []),
                    "citation_count": len(first_hit.get("expanded_context", {}).get("citations", [])),
                    "reference_count": len(first_hit.get("expanded_context", {}).get("references", [])),
                })
                print(f"[retrieval_runner]   [{mode}] {query!r} -> {source.get('source_id', '')} / "
                      f"{first_hit.get('section_path', '').split(' > ')[-1][:60]}")

        if not smell_results[smell_id]:
            print(f"[retrieval_runner]   No hits.")

    # Write retrieval bundles
    out_dir = stage_output_dir("003", run_dir)
    bundles_path = out_dir / "retrieval_bundles.json"
    bundles_path.write_text(
        json.dumps(list(all_bundles.values()), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n[retrieval_runner] Written {len(all_bundles)} bundles -> {bundles_path}")

    # Write retrieval report
    report = _build_report(smell_results, corpus_gaps, index, run_id)
    report_path = out_dir / "retrieval_report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"[retrieval_runner] Written report -> {report_path}")

    print("\n" + "=" * 60)
    print("RETRIEVAL SUMMARY")
    print("=" * 60)
    for sid in range(1, 6):
        n = len(smell_results[sid])
        gap = " [CORPUS GAP]" if any(g["smell_id"] == sid for g in corpus_gaps) else ""
        print(f"  Smell {sid}: {n} bundle(s){gap}")
    print(f"  Total bundles: {len(all_bundles)}")
    print("=" * 60)


def _build_report(
    smell_results: dict[int, list[dict]],
    corpus_gaps: list[dict],
    index: RunIndex,
    run_id: str,
) -> str:
    lines = [
        "# Stage 002 Retrieval Report",
        "",
        f"Run ID: `{run_id}`",
        f"Created: {_now()}",
        "",
        "This report documents what exact-phrase and lexical retrieval modes return",
        "for each of the five active homeowners policy-layer smells.",
        "",
        "---",
        "",
        "## Corpus Summary",
        "",
    ]

    src_types = {}
    for s in index.sources:
        st = s.get("source_type", "unknown")
        src_types[st] = src_types.get(st, 0) + 1
    for st, count in sorted(src_types.items()):
        lines.append(f"- {count}× `{st}`")
    lines.append("")

    if corpus_gaps:
        lines += [
            "## Corpus Gaps",
            "",
            "The following smells cannot be meaningfully evaluated because the required",
            "source types are not present in this corpus slice:",
            "",
        ]
        for g in corpus_gaps:
            lines.append(f"- **Smell {g['smell_id']}** ({g['smell_name']}): "
                         f"requires `{'`, `'.join(g['requires_source_types'])}` — not present")
        lines += ["", "---", ""]

    lines += ["## Results by Smell", ""]

    for sid in range(1, 6):
        results = smell_results[sid]
        gap = next((g for g in corpus_gaps if g["smell_id"] == sid), None)
        lines.append(f"### Smell {sid}: {SMELL_NAMES[sid]}")
        lines.append("")

        if gap:
            lines.append(f"> **Corpus gap**: {gap['gap_note']}")
            lines.append("")

        if not results:
            lines.append("No retrieval hits in this corpus slice.")
            lines.append("")
            continue

        lines.append(f"{len(results)} bundle(s) retrieved.")
        lines.append("")

        by_query: dict[str, list[dict]] = {}
        for r in results:
            by_query.setdefault(r["query"], []).append(r)

        for query, hits in by_query.items():
            mode = hits[0]["mode"]
            lines.append(f"**Query** (`{mode}`): `{query}`")
            lines.append("")
            for h in hits:
                path_short = h["section_path"].split(" > ")[-1][:80]
                lines.append(f"- `{h['source_id']}` / {path_short}")
                lines.append(f"  - Source type: `{h['source_type']}`  "
                             f"Parser confidence: `{h['parser_confidence']}`")
                if h["citation_count"]:
                    lines.append(f"  - {h['citation_count']} citation(s) attached")
                if h["reference_count"]:
                    lines.append(f"  - {h['reference_count']} broader reference(s) attached")
                lines.append(f"  - *{h['hit_text_excerpt'][:160].replace(chr(10), ' ')}*")
                lines.append("")

    lines += [
        "---",
        "",
        "## Retrieval Mode Assessment",
        "",
        "| Mode | Strengths | Weaknesses |",
        "|---|---|---|",
        "| Exact phrase | High precision; zero false positives for legal terms | Misses paraphrases and variant spellings |",
        "| BM25 lexical | Catches term co-occurrence; handles varied phrasing | High false-positive rate on common legal words (\"reasonable\", \"manual\") |",
        "| Graph expansion | Attaches parent section and sibling nodes for context | Only intra-document edges exist in Stage 002 |",
        "| Metadata filter | Source-type scoping reduces noise immediately | Requires carrier form sources not yet in corpus |",
        "",
        "---",
        "",
        "_This report is generated output. Do not edit manually._",
        "_Retrieval bundles are not legal findings._",
    ]

    return "\n".join(lines) + "\n"


def main() -> None:
    # Default points at Stage 002's most recent output — override with --run-dir
    _stage_002 = Path(__file__).parent.parent.parent / "002-homeowners-discovery-instrumentation"
    parser = argparse.ArgumentParser(description="Stage 003 retrieval runner")
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=_stage_002 / "output",
        help="Stage 002 pipeline run output directory",
    )
    args = parser.parse_args()
    run(args.run_dir)


if __name__ == "__main__":
    main()
