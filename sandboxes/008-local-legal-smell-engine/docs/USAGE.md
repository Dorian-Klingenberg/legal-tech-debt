# Local Engine Usage

The engine uses only the Python standard library at runtime.

## Python API

```python
from legal_smell_engine import DetectorEngine, EvidenceCorpus, Node

corpus = EvidenceCorpus(
    run_id="example-run",
    nodes=[
        Node(
            node_id="node-1",
            source_id="synthetic-policy",
            source_type="serff_form_filing",
            section_path="Loss Settlement",
            text="We pay the actual cash value within a reasonable time.",
        )
    ],
)

findings = DetectorEngine(corpus).run_detectors(["SMELL2"])
for finding in findings:
    print(finding.to_dict())
```

## CLI

From this sandbox directory:

```powershell
$env:PYTHONPATH = (Resolve-Path src).Path
python -m legal_smell_engine --list-smells
python -m legal_smell_engine --text "The premium follows the current manual." --smell SMELL2
python -m legal_smell_engine --nodes fixtures/positive.jsonl --run-id demo-001 --output findings.jsonl --report report.md
```

Node JSONL records use the generic fields `node_id`, `source_id`, `text`,
`source_type`, `section_path`, and `node_type`. Edge JSONL records use
`from_id`, `to_id`, and `edge_type`; pass them with `--edges` when a detector
needs graph evidence.

## Result behavior

Results are JSONL `Finding` records. They include schema version, run identity,
stable smell and heuristic identifiers, source/node provenance, evidence text,
confidence, rationale, reviewer question, false-positive risk, and—when
relevant—missing-evidence and supporting-node fields.

The engine reports review leads. It does not establish legal noncompliance or
provide legal advice.

