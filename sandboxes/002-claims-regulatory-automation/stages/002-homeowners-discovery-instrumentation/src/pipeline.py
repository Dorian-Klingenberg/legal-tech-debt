"""Stage 002 discovery-and-instrumentation pipeline.

Usage (run from the stage root directory):
    python src/pipeline.py

Or with explicit paths:
    python src/pipeline.py --manifest data/source_manifest_subset.csv --output output/

Reads selected corpus sources, runs parsers, builds nodes, extracts citations
and references, builds graph edges, scans for candidate evidence, and writes
all JSONL/JSON outputs.

No LLM. No vector store. No final legal findings.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure src/ is on the path regardless of working directory
_SRC = Path(__file__).parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import ids as id_gen
from extractors.citations import extract_citations
from extractors.references import extract_references
from graph_builder import build_edges
from models import PIPELINE_VERSION, SCHEMA_VERSION, RetrievalBundle, RunManifest
from parsers import html_parser, pdf_parser
from segmenter import build_nodes
from source_registry import load_sources
from evidence_scanner import scan as scan_evidence
from writers import write_json, write_jsonl


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(manifest_path: Path, output_base: Path) -> None:
    run_id = id_gen.run_id()
    now = _now()

    # Each run gets its own timestamped subdirectory: output/YYYYMMDD_HHMMSS_<run_id[:8]>/
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_dir = output_base / f"{ts}_{run_id[:8]}"

    print(f"[pipeline] run_id={run_id}")
    print(f"[pipeline] manifest={manifest_path}")
    print(f"[pipeline] output={output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load sources ---
    print("\n[pipeline] Loading sources...")
    sources = load_sources(manifest_path, run_id)
    print(f"[pipeline] {len(sources)} sources loaded")

    # --- Parse each source ---
    all_parser_runs = []
    all_blocks = []
    all_block_stats = []
    all_table_failures = []
    all_parse_warnings = []
    all_nodes = []
    all_citations = []
    all_references = []
    all_edges = []

    # Index source metadata
    source_by_id = {s.source_id: s for s in sources}

    for source in sources:
        path = Path(source.downloaded_path)
        ftype = source.detected_file_type
        ext_ok = source.extension_matches_type
        print(f"\n[pipeline] Parsing {source.source_id} ({ftype}, {'ext ok' if ext_ok else 'EXT MISMATCH'})...")

        if ftype == "html":
            pr, blocks, stats, tfs, warns = html_parser.parse(source.source_id, source.source_hash, path, run_id)
        else:
            # pdf or unknown — route to Docling
            pr, blocks, stats, tfs, warns = pdf_parser.parse(
                source.source_id, source.source_hash, path, run_id, extension_mismatch=not ext_ok
            )

        print(f"[pipeline]   {pr.status}: {pr.block_count} blocks, {pr.warning_count} warnings, {pr.table_failure_count} table failures ({pr.duration_seconds:.1f}s)")

        all_parser_runs.append(pr)
        all_blocks.extend(blocks)
        all_block_stats.append(stats)
        all_table_failures.extend(tfs)
        all_parse_warnings.extend(warns)

        # Build nodes
        nodes = build_nodes(source.source_id, source.source_hash, source.title, blocks, run_id)
        print(f"[pipeline]   {len(nodes)} nodes")
        all_nodes.extend(nodes)

        # Extract citations and references
        cites = extract_citations(nodes, run_id)
        refs = extract_references(nodes, run_id)
        print(f"[pipeline]   {len(cites)} citations, {len(refs)} references")
        all_citations.extend(cites)
        all_references.extend(refs)

        # Build graph edges
        edges = build_edges(nodes, cites, refs, run_id)
        print(f"[pipeline]   {len(edges)} edges")
        all_edges.extend(edges)

    # --- Candidate evidence ---
    print("\n[pipeline] Scanning for candidate evidence...")
    evidence = scan_evidence(all_nodes, all_parser_runs, run_id)
    print(f"[pipeline] {len(evidence)} candidate evidence items")

    by_smell = {}
    for e in evidence:
        by_smell.setdefault(e.smell_id, []).append(e)
    for sid in sorted(by_smell):
        print(f"[pipeline]   Smell {sid}: {len(by_smell[sid])} items")

    # --- Retrieval bundles ---
    print("\n[pipeline] Building retrieval bundles...")
    bundles = _build_bundles(evidence, all_nodes, all_citations, all_references, all_parser_runs, sources, run_id)
    print(f"[pipeline] {len(bundles)} retrieval bundles")

    # --- Run manifest ---
    manifest = RunManifest(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        pipeline_version=PIPELINE_VERSION,
        corpus_root=str(Path("corpus") / "kentucky-homeowners-policy-smells"),
        subset_manifest=str(manifest_path),
        source_ids=[s.source_id for s in sources],
        output_dir=str(output_dir),
        total_sources=len(sources),
        parsers_used=sorted({pr.parser_name for pr in all_parser_runs}),
        schema_versions={
            "run_manifest": SCHEMA_VERSION,
            "source": SCHEMA_VERSION,
            "parser_run": SCHEMA_VERSION,
            "block": SCHEMA_VERSION,
            "block_stats": SCHEMA_VERSION,
            "node": SCHEMA_VERSION,
            "citation": SCHEMA_VERSION,
            "reference": SCHEMA_VERSION,
            "edge": SCHEMA_VERSION,
            "table_failure": SCHEMA_VERSION,
            "parse_warning": SCHEMA_VERSION,
            "candidate_evidence": SCHEMA_VERSION,
            "retrieval_bundle": SCHEMA_VERSION,
        },
        config_snapshot={
            "storage_backend": "files",
            "semantic_split_enabled": False,
            "llm_boundary_adjudication": False,
            "graph_expand_depth": 1,
            "parser_strategy": "html_bs4_kar_v1 for HTML; docling_2.93.0 for PDF or unknown/PDF-magic files",
        },
        parse_stats={
            "blocks_count": len(all_blocks),
            "nodes_count": len(all_nodes),
            "citations_count": len(all_citations),
            "references_count": len(all_references),
            "edges_count": len(all_edges),
            "table_failures_count": len(all_table_failures),
            "parse_warnings_count": len(all_parse_warnings),
            "partial_parser_runs_count": sum(1 for pr in all_parser_runs if pr.status == "partial"),
            "failed_parser_runs_count": sum(1 for pr in all_parser_runs if pr.status == "failed"),
        },
    )

    # --- Write outputs ---
    print("\n[pipeline] Writing outputs...")
    write_json(manifest, output_dir / "run_manifest.json")
    write_jsonl(sources, output_dir / "sources.jsonl")
    write_jsonl(all_parser_runs, output_dir / "parser_runs.jsonl")
    write_jsonl(all_blocks, output_dir / "blocks.jsonl")
    write_jsonl(all_block_stats, output_dir / "block_stats.jsonl")
    write_jsonl(all_nodes, output_dir / "nodes.jsonl")
    write_jsonl(all_citations, output_dir / "citations.jsonl")
    write_jsonl(all_references, output_dir / "references.jsonl")
    write_jsonl(all_edges, output_dir / "edges.jsonl")
    write_jsonl(all_table_failures, output_dir / "table_failures.jsonl")
    write_jsonl(all_parse_warnings, output_dir / "parse_warnings.jsonl")
    write_jsonl(evidence, output_dir / "candidate_evidence.jsonl")
    write_json([b.__dict__ if hasattr(b, '__dict__') else b for b in bundles], output_dir / "retrieval_bundles.json")

    # --- Discovery report ---
    report = _build_report(manifest, sources, all_parser_runs, all_block_stats, all_nodes,
                           all_citations, all_references, all_edges, all_table_failures,
                           all_parse_warnings, evidence, bundles)
    (output_dir / "discovery_report.md").write_text(report, encoding="utf-8")
    print(f"[pipeline] Written to {output_dir}/")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Sources:           {len(sources)}")
    print(f"  Blocks:            {len(all_blocks)}")
    print(f"  Nodes:             {len(all_nodes)}")
    print(f"  Citations:         {len(all_citations)}")
    print(f"  References:        {len(all_references)}")
    print(f"  Edges:             {len(all_edges)}")
    print(f"  Table failures:    {len(all_table_failures)}")
    print(f"  Parse warnings:    {len(all_parse_warnings)}")
    print(f"  Candidate evidence:{len(evidence)}")
    print(f"  Retrieval bundles: {len(bundles)}")
    print(f"\n  run_id: {run_id}")
    print("=" * 60)


def _build_bundles(
    evidence,
    nodes,
    citations,
    references,
    parser_runs,
    sources,
    run_id: str,
) -> list[RetrievalBundle]:
    """Build one retrieval bundle per candidate evidence item."""
    now = _now()
    node_by_id = {n.node_id: n for n in nodes}
    cites_by_node = {}
    for c in citations:
        cites_by_node.setdefault(c.node_id, []).append(c.citation_id)
    refs_by_node = {}
    for r in references:
        refs_by_node.setdefault(r.node_id, []).append(r.reference_id)
    pr_by_source = {pr.source_id: pr for pr in parser_runs}
    source_by_id = {s.source_id: s for s in sources}

    bundles: list[RetrievalBundle] = []
    seen_bundles: set[str] = set()

    for ev in evidence:
        nid = ev.node_id
        node = node_by_id.get(nid)
        if not node:
            continue

        query = f"smell:{ev.smell_id} heuristic:{ev.heuristic_id}"
        bid = id_gen.bundle_id(query, nid)
        if bid in seen_bundles:
            continue
        seen_bundles.add(bid)

        parent = node_by_id.get(node.parent_node_id) if node.parent_node_id else None
        # Find adjacent siblings
        siblings = [
            n.node_id for n in nodes
            if n.parent_node_id == node.parent_node_id
            and n.node_id != nid
            and n.source_id == node.source_id
        ][:2]

        pr = pr_by_source.get(node.source_id)
        pconf = "high" if (pr and pr.status == "success") else ("medium" if pr else "low")

        doc_nodes = {n.source_id: n for n in nodes if n.node_type == "document"}
        doc = doc_nodes.get(node.source_id)
        source = source_by_id.get(node.source_id)

        signal_scores = {
            "exact": 0.0,
            "lexical": 1.0,
            "graph": 1.0 if (parent or siblings) else 0.0,
            "citation": 1.0 if cites_by_node.get(nid) else 0.0,
            "reference": 1.0 if refs_by_node.get(nid) else 0.0,
            "metadata": 1.0 if source else 0.0,
            "semantic": None,
            "parser_penalty": 0.0 if pconf == "high" else 0.25 if pconf == "medium" else 0.5,
        }

        hit = {
            "node_id": nid,
            "rank": 1,
            "score": 1.0,
            "node_type": node.node_type,
            "text": node.retrievable_text[:500],
            "source": {
                "source_id": node.source_id,
                "source_hash": node.source_hash,
                "title": source.title if source else (doc.title if doc else node.source_id),
                "source_type": source.source_type if source else "",
                "url": source.url if source else "",
            },
            "section_path": node.section_path,
            "pages": [node.page_number] if node.page_number is not None else [],
            "why_retrieved": [ev.why_flagged, f"heuristic={ev.heuristic_id}"],
            "candidate_ids": [ev.candidate_id],
            "signal_scores": signal_scores,
            "parser_diagnostics": {
                "parser_run_id": pr.parser_run_id if pr else "",
                "reading_order_confidence": 0.75 if (pr and pr.reading_order_uncertain) else 1.0,
                "warnings": [],
            },
            "expanded_context": {
                "parent_section": {
                    "node_id": parent.node_id,
                    "text": parent.retrievable_text[:300],
                } if parent else None,
                "adjacent_nodes": siblings,
                "citations": cites_by_node.get(nid, []),
                "references": refs_by_node.get(nid, []),
                "overrides": [],
            },
        }

        bundles.append(RetrievalBundle(
            schema_version=SCHEMA_VERSION,
            run_id=run_id,
            created_at=now,
            bundle_id=bid,
            query_text=query,
            task_description="Stage 002 candidate-evidence retrieval bundle",
            filters={"smell_id": ev.smell_id, "heuristic_id": ev.heuristic_id},
            hits=[hit],
        ))

    return bundles


def _build_report(manifest, sources, parser_runs, block_stats, nodes,
                  citations, references, edges, table_failures, warnings,
                  evidence, bundles) -> str:
    lines = [
        "# Stage 002 Discovery Report",
        "",
        f"Run ID: `{manifest.run_id}`",
        f"Created: {manifest.created_at}",
        f"Pipeline: {manifest.pipeline_version}",
        "",
        "---",
        "",
        "## Sources",
        "",
        f"{len(sources)} sources processed.",
        "",
        "| source_id | type | detected | ext_ok | blocks | nodes |",
        "|---|---|---|---|---:|---:|",
    ]

    block_by_source = {bs.source_id: bs.total_blocks for bs in block_stats}
    node_by_source = {}
    for n in nodes:
        node_by_source[n.source_id] = node_by_source.get(n.source_id, 0) + 1
    pr_by_source = {pr.source_id: pr for pr in parser_runs}

    for s in sources:
        pr = pr_by_source.get(s.source_id)
        status = pr.status if pr else "—"
        lines.append(
            f"| {s.source_id} | {s.source_type} | {s.detected_file_type} | "
            f"{'✓' if s.extension_matches_type else '✗'} | "
            f"{block_by_source.get(s.source_id, 0)} | "
            f"{node_by_source.get(s.source_id, 0)} |"
        )

    lines += [
        "",
        "## Parser Summary",
        "",
    ]
    for pr in parser_runs:
        lines.append(f"- **{pr.source_id}**: {pr.parser_name}, status={pr.status}, "
                     f"{pr.block_count} blocks, {pr.warning_count} warnings, "
                     f"{pr.table_failure_count} table failures, {pr.duration_seconds:.1f}s")

    lines += [
        "",
        "## Counts",
        "",
        f"- Blocks: {sum(b.total_blocks for b in block_stats)}",
        f"- Nodes: {len(nodes)}",
        f"- Citations: {len(citations)}",
        f"- References: {len(references)}",
        f"- Edges: {len(edges)}",
        f"- Table failures: {len(table_failures)}",
        f"- Parse warnings: {len(warnings)}",
        f"- Candidate evidence: {len(evidence)}",
        f"- Retrieval bundles: {len(bundles)}",
        "",
        "## Candidate Evidence by Smell",
        "",
    ]

    by_smell: dict[int, list] = {}
    for e in evidence:
        by_smell.setdefault(e.smell_id, []).append(e)

    smell_names = {
        1: "Overbroad / Non-deterministic Exclusions",
        2: "Magic Number / Magic Valuation Terms",
        3: "Coverage Inversion / Contradictory Conditions",
        4: "Calculation Rule Drift / Unversioned Rate Reference",
        5: "Regulatory Mapping Smells",
    }

    for sid in range(1, 6):
        items = by_smell.get(sid, [])
        lines.append(f"### Smell {sid}: {smell_names[sid]}")
        lines.append("")
        if not items:
            lines.append("No candidate evidence found in this corpus slice.")
        else:
            lines.append(f"{len(items)} candidate evidence items.")
            lines.append("")
            for e in items[:5]:  # show first 5
                node = next((n for n in nodes if n.node_id == e.node_id), None)
                path = node.section_path if node else e.node_id
                lines.append(f"- **{e.heuristic_id}** in `{e.source_id}` at `{path}`")
                lines.append(f"  - {e.why_flagged}")
                lines.append(f"  - Evidence: _{e.evidence_text[:120].replace(chr(10), ' ')}_")
                lines.append(f"  - Parser confidence: {e.parser_confidence}")
                lines.append(f"  - Reviewer question: {e.reviewer_question}")
                lines.append("")
            if len(items) > 5:
                lines.append(f"  _(+ {len(items) - 5} more — see candidate_evidence.jsonl)_")
        lines.append("")

    lines += [
        "## Parse Warnings",
        "",
    ]
    if not warnings:
        lines.append("No parse warnings.")
    else:
        for w in warnings:
            lines.append(f"- **{w.warning_type}** in `{w.source_id}`: {w.description}")

    lines += [
        "",
        "## Table Failures",
        "",
    ]
    if not table_failures:
        lines.append("No table failures.")
    else:
        for tf in table_failures:
            lines.append(f"- **{tf.failure_type}** in `{tf.source_id}` (page {tf.page_number}): {tf.description}")

    lines += [
        "",
        "## Known Gaps",
        "",
        "- Smell 4 coverage is sparse. The KNIC SERFF rate/rule filing (KY-SERFF-KNIC-127064322, ~988 KB) was not included in this slice.",
        "- No endorsement-level or schedule-level parsing in this slice.",
        "- KRS statute pages were saved as PDFs with .html extensions; Docling parsed them but structural fidelity depends on PDF content quality.",
        "- No cross-document edges. Each source is processed independently.",
        "",
        "---",
        "",
        "_This report is generated output. Do not edit manually._",
        "_Candidate evidence items are not legal findings._",
    ]

    return "\n".join(lines) + "\n"


def main() -> None:
    # Default paths relative to the stage root (one level above src/)
    stage_root = Path(__file__).parent.parent

    parser = argparse.ArgumentParser(description="Stage 002 discovery pipeline")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=stage_root / "data" / "source_manifest_subset.csv",
        help="Path to source_manifest_subset.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=stage_root / "output",
        help="Base output directory; each run creates a timestamped subdirectory inside it",
    )
    args = parser.parse_args()
    run(args.manifest, args.output)  # args.output is the base; run() creates the timestamped subfolder


if __name__ == "__main__":
    main()
