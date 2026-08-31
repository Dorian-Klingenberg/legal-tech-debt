from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .contracts import Edge, EvidenceCorpus, Finding, Node


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_corpus(nodes_path: Path, edges_path: Path | None, run_id: str) -> EvidenceCorpus:
    nodes = [Node.from_dict(value) for value in read_jsonl(nodes_path)]
    edges = [Edge.from_dict(value) for value in read_jsonl(edges_path)] if edges_path else []
    return EvidenceCorpus(run_id=run_id, nodes=nodes, edges=edges)


def write_findings(findings: Iterable[Finding], path: Path | None = None) -> None:
    lines = [json.dumps(finding.to_dict(), ensure_ascii=False) for finding in findings]
    output = "\n".join(lines) + ("\n" if lines else "")
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output, encoding="utf-8")
    else:
        print(output, end="")

