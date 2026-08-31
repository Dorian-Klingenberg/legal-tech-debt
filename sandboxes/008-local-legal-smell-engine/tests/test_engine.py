from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from legal_smell_engine.contracts import Edge, EvidenceCorpus, Node  # noqa: E402
from legal_smell_engine.cli import main  # noqa: E402
from legal_smell_engine.adapters.azure_function import review_json_payload  # noqa: E402
from legal_smell_engine.adapters.mcp_server import review_payload  # noqa: E402
from legal_smell_engine.engine import DetectorEngine  # noqa: E402
from legal_smell_engine.report import render_markdown  # noqa: E402


def fixture_nodes(name: str) -> list[Node]:
    path = ROOT / "fixtures" / name
    return [Node.from_dict(json.loads(line)) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class EngineTests(unittest.TestCase):
    def test_positive_fixture_produces_findings_across_all_five_smells(self) -> None:
        corpus = EvidenceCorpus("fixture-positive", fixture_nodes("positive.jsonl"))
        findings = DetectorEngine(corpus, created_at="2026-08-06T00:00:00+00:00").run_detectors(
            ["SMELL1", "SMELL2", "SMELL3", "SMELL4", "SMELL5"]
        )
        self.assertTrue({finding.smell_id for finding in findings} >= {1, 2, 3, 4, 5})
        self.assertTrue(all(finding.schema_version == "1.0.0" for finding in findings))
        self.assertTrue(all(finding.evidence_text for finding in findings))

    def test_negative_fixture_has_no_findings(self) -> None:
        corpus = EvidenceCorpus("fixture-negative", fixture_nodes("negative.jsonl"))
        findings = DetectorEngine(corpus).run_detectors(["SMELL1", "SMELL2", "SMELL3", "SMELL4", "SMELL5"])
        self.assertEqual([], findings)

    def test_regulatory_edge_suppresses_graph_gap(self) -> None:
        nodes = [
            Node(
                node_id="rate-1",
                source_id="filing-1",
                source_type="serff_rate_rule_filing",
                section_path="Rate",
                text="The base premium follows the rate revision procedure.",
            ),
            Node(node_id="authority-1", source_id="KRS-1", text="Authority"),
        ]
        edges = [Edge("rate-1", "authority-1", "cites_statute")]
        findings = DetectorEngine(EvidenceCorpus("graph-clean", nodes, edges)).run_detectors(["SMELL5"])
        self.assertFalse(any(finding.heuristic_id == "SMELL5-H004" for finding in findings))

    def test_report_is_markdown(self) -> None:
        corpus = EvidenceCorpus("fixture-report", fixture_nodes("positive.jsonl"))
        findings = DetectorEngine(corpus).run_detectors(["SMELL2"])
        report = render_markdown(findings, corpus.run_id)
        self.assertIn("# Local Legal Smell Findings", report)
        self.assertIn("SMELL2-H001", report)

    def test_cli_writes_jsonl_and_markdown(self) -> None:
        with TemporaryDirectory() as temporary:
            output = Path(temporary) / "findings.jsonl"
            report = Path(temporary) / "report.md"
            result = main(
                [
                    "--text",
                    "The premium follows the current manual.",
                    "--run-id",
                    "cli-test",
                    "--smell",
                    "SMELL2",
                    "--output",
                    str(output),
                    "--report",
                    str(report),
                ]
            )
            self.assertEqual(0, result)
            self.assertTrue(output.exists())
            self.assertTrue(report.exists())
            self.assertIn("SMELL2-H002", output.read_text(encoding="utf-8"))
            self.assertIn("# Local Legal Smell Findings", report.read_text(encoding="utf-8"))

    def test_optional_adapters_share_the_core_contract(self) -> None:
        nodes = [
            {
                "node_id": "adapter-1",
                "source_id": "synthetic-policy",
                "source_type": "serff_form_filing",
                "section_path": "Loss Settlement",
                "text": "We pay actual cash value within a reasonable time.",
            }
        ]
        mcp_findings = review_payload(nodes, run_id="adapter-test", smell_ids=["SMELL2"])
        azure_response = review_json_payload({"nodes": nodes, "run_id": "adapter-test", "smell_ids": ["SMELL2"]})
        self.assertTrue(mcp_findings)
        self.assertEqual(mcp_findings, azure_response["findings"])


if __name__ == "__main__":
    unittest.main()
