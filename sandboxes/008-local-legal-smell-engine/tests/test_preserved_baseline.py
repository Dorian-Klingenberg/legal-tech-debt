from __future__ import annotations

import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from legal_smell_engine.contracts import Edge, EvidenceCorpus, Node  # noqa: E402
from legal_smell_engine.engine import DetectorEngine  # noqa: E402


RUN_DIR = REPO / "sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5"
EXPECTED_STAGE006 = {1: 1, 2: 17, 3: 0, 4: 1, 5: 12}
CARRIER_TYPES = {"serff_form_filing", "serff_rate_rule_filing", "serff_correspondence"}


def jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class PreservedBaselineTests(unittest.TestCase):
    def test_stage006_baseline_is_available_and_generic_engine_runs(self) -> None:
        self.assertTrue(RUN_DIR.exists())
        baseline = jsonl(REPO / "sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl")
        baseline_counts = Counter(item["smell_id"] for item in baseline)
        self.assertEqual({smell_id: baseline_counts.get(smell_id, 0) for smell_id in EXPECTED_STAGE006}, EXPECTED_STAGE006)
        self.assertEqual(31, len(baseline))

        source_types = {item["source_id"]: item.get("source_type", "") for item in jsonl(RUN_DIR / "sources.jsonl")}
        nodes = [
            Node.from_dict({**item, "source_type": source_types.get(item.get("source_id", ""), "")})
            for item in jsonl(RUN_DIR / "nodes.jsonl")
        ]
        nodes = [node for node in nodes if node.source_type in CARRIER_TYPES]
        edges = [Edge.from_dict(item) for item in jsonl(RUN_DIR / "edges.jsonl")]
        findings = DetectorEngine(EvidenceCorpus("stage006-port", nodes, edges)).run_detectors(
            ["SMELL1", "SMELL2", "SMELL3", "SMELL4", "SMELL5"]
        )
        actual_counts = Counter(finding.smell_id for finding in findings)
        print(f"preserved_stage006={dict(baseline_counts)} generic_port={dict(actual_counts)} total={len(findings)}")
        self.assertTrue(findings)
        self.assertTrue(all(finding.source_id and finding.node_id for finding in findings))


if __name__ == "__main__":
    unittest.main()
