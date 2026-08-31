"""Validate the isolated Stage 003 smell packet shape."""
from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_SPEC_MARKERS = (
    "Definition",
    "Evidence",
    "Positive",
    "Negative",
    "Insufficiency",
    "Provenance",
)
REQUIRED_CASE_KEYS = {"case_id", "label", "nodes", "edges", "expected"}
REQUIRED_LABELS = {"positive", "negative", "insufficient"}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: case must be an object")
        rows.append(value)
    return rows


def validate(root: Path) -> dict:
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    smells = manifest["smells"]
    if len(smells) != 20 or len({item["smell_id"] for item in smells}) != 20:
        raise ValueError("manifest must contain 20 unique smell IDs")

    counts = {"low": 0, "medium": 0, "high": 0}
    packet_reports = []
    for item in smells:
        complexity = item["complexity"]
        counts[complexity] += 1
        packet = root / manifest["packet_root"] / item["packet"]
        spec = (packet / "SPEC.md").read_text(encoding="utf-8")
        missing_markers = [marker for marker in REQUIRED_SPEC_MARKERS if marker.lower() not in spec.lower()]
        if missing_markers:
            raise ValueError(f"{item['smell_id']}: SPEC.md missing {missing_markers}")

        case_counts = {}
        case_ids = set()
        for label in REQUIRED_LABELS:
            rows = load_jsonl(packet / f"{label}.jsonl")
            if not rows:
                raise ValueError(f"{item['smell_id']}: {label}.jsonl is empty")
            case_counts[label] = len(rows)
            for row in rows:
                missing = REQUIRED_CASE_KEYS - row.keys()
                if missing:
                    raise ValueError(f"{item['smell_id']}: {label} case missing {sorted(missing)}")
                if row["label"] != label:
                    raise ValueError(f"{item['smell_id']}: {label} case has label {row['label']!r}")
                if not row["case_id"] or row["case_id"] in case_ids:
                    raise ValueError(f"{item['smell_id']}: case IDs must be non-empty and unique")
                case_ids.add(row["case_id"])
                expected = row["expected"]
                if expected.get("smell_id") != item["smell_id"]:
                    raise ValueError(f"{item['smell_id']}: expected.smell_id mismatch")
                node_ids = {node.get("node_id") for node in row["nodes"]}
                if None in node_ids or len(node_ids) != len(row["nodes"]):
                    raise ValueError(f"{item['smell_id']}: node IDs must be present and unique per case")
                if any(not node.get("kind") or not isinstance(node.get("text"), str) for node in row["nodes"]):
                    raise ValueError(f"{item['smell_id']}: every node needs kind and text")
                edge_keys = set()
                for edge in row["edges"]:
                    if edge.get("source") not in node_ids or edge.get("target") not in node_ids:
                        raise ValueError(f"{item['smell_id']}: edge endpoint is not a case node")
                    if not edge.get("type"):
                        raise ValueError(f"{item['smell_id']}: every edge needs a non-empty type")
                    edge_key = (edge["source"], edge["target"], edge["type"])
                    if edge_key in edge_keys:
                        raise ValueError(f"{item['smell_id']}: duplicate semantic edge {edge_key}")
                    edge_keys.add(edge_key)
        packet_reports.append({"smell_id": item["smell_id"], "complexity": complexity, "cases": case_counts})

    if counts != {"low": 8, "medium": 8, "high": 4}:
        raise ValueError(f"unexpected complexity distribution: {counts}")
    return {"status": "ok", "benchmark_id": manifest["benchmark_id"], "smell_count": 20, "complexity_counts": counts, "packets": packet_reports}


if __name__ == "__main__":
    stage_root = Path(__file__).resolve().parents[1]
    try:
        print(json.dumps(validate(stage_root), indent=2))
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
