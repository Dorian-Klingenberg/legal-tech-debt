"""In-memory index over a Stage 002 run directory."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def _read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


class RunIndex:
    """Loads all JSONL/JSON artifacts from a run directory and builds lookup indices."""

    def __init__(self, run_dir: Path) -> None:
        self.run_dir = run_dir
        self.manifest: dict = _read_json(run_dir / "run_manifest.json") or {}
        self.nodes: list[dict] = _read_jsonl(run_dir / "nodes.jsonl")
        self.citations: list[dict] = _read_jsonl(run_dir / "citations.jsonl")
        self.references: list[dict] = _read_jsonl(run_dir / "references.jsonl")
        self.edges: list[dict] = _read_jsonl(run_dir / "edges.jsonl")
        self.parser_runs: list[dict] = _read_jsonl(run_dir / "parser_runs.jsonl")
        self.sources: list[dict] = _read_jsonl(run_dir / "sources.jsonl")
        self.evidence: list[dict] = _read_jsonl(run_dir / "candidate_evidence.jsonl")
        self.warnings: list[dict] = _read_jsonl(run_dir / "parse_warnings.jsonl")
        self.run_id: str = self.manifest.get("run_id", "unknown")
        self._build()

    def _build(self) -> None:
        self.node_by_id: dict[str, dict] = {n["node_id"]: n for n in self.nodes}
        self.source_by_id: dict[str, dict] = {s["source_id"]: s for s in self.sources}
        self.pr_by_source: dict[str, dict] = {p["source_id"]: p for p in self.parser_runs}

        self.edges_from: dict[str, list[dict]] = defaultdict(list)
        self.edges_to: dict[str, list[dict]] = defaultdict(list)
        for e in self.edges:
            self.edges_from[e["from_id"]].append(e)
            self.edges_to[e["to_id"]].append(e)

        self.cites_by_node: dict[str, list[dict]] = defaultdict(list)
        for c in self.citations:
            self.cites_by_node[c["node_id"]].append(c)

        self.refs_by_node: dict[str, list[dict]] = defaultdict(list)
        for r in self.references:
            self.refs_by_node[r["node_id"]].append(r)

        self.ev_by_node: dict[str, list[dict]] = defaultdict(list)
        for e in self.evidence:
            self.ev_by_node[e["node_id"]].append(e)

        # Inverted term index for BM25 (content nodes only)
        self._term_index: dict[str, set[str]] = defaultdict(set)
        self._node_terms: dict[str, list[str]] = {}
        for n in self.nodes:
            if n.get("node_type") == "document":
                continue
            text = (n.get("text") or "").lower()
            terms = re.findall(r"\b[a-z]{2,}\b", text)
            self._node_terms[n["node_id"]] = terms
            for t in set(terms):
                self._term_index[t].add(n["node_id"])

    @property
    def content_nodes(self) -> list[dict]:
        return [n for n in self.nodes if n.get("node_type") != "document"]
