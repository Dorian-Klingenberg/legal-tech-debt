from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


RUN_DATA_RE = re.compile(
    r"(?s)    const runData = .*?;\n\n    const nodeGeometry"
)


def build_run_data(stage_dir: Path) -> dict[str, object]:
    findings_path = stage_dir / "output" / "findings.json"
    roots_path = stage_dir / "output" / "dependency_roots.json"

    findings_payload = json.loads(findings_path.read_text(encoding="utf-8"))
    roots_payload = json.loads(roots_path.read_text(encoding="utf-8"))

    return {
        "sections": [
            {
                "id": section["id"],
                "title": section["title"],
                "document": section["document"],
                "line": section["line"],
                "body": section["body"].strip(),
            }
            for section in findings_payload["sections"]
        ],
        "references": findings_payload["references"],
        "findings": findings_payload["findings"],
        "cycleNodes": roots_payload["cycle_nodes"],
        "rootsByNode": {
            node_key: [root["key"] for root in roots]
            for node_key, roots in roots_payload["roots_by_node"].items()
        },
    }


def embed(stage_dir: Path) -> None:
    dashboard_path = stage_dir / "dashboard.html"
    html = dashboard_path.read_text(encoding="utf-8")
    run_data = build_run_data(stage_dir)
    js = json.dumps(run_data, indent=6)
    replacement = f"    const runData = {js};\n\n    const nodeGeometry"
    updated, count = RUN_DATA_RE.subn(lambda _match: replacement, html, count=1)
    if count != 1:
        raise RuntimeError("Could not find exactly one runData block in dashboard.html")
    dashboard_path.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed probe output into a static dashboard.html file.")
    parser.add_argument("stage_dir", type=Path, help="Stage directory containing output/ and dashboard.html.")
    args = parser.parse_args()
    embed(args.stage_dir.resolve())


if __name__ == "__main__":
    main()
