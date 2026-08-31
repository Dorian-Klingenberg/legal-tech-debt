from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from .contracts import Finding


def render_markdown(findings: Iterable[Finding], run_id: str) -> str:
    rows = list(findings)
    by_smell = Counter((finding.smell_id, finding.smell_name) for finding in rows)
    by_confidence = Counter(finding.confidence for finding in rows)
    lines = [
        "# Local Legal Smell Findings",
        "",
        f"Run: `{run_id}`",
        f"Total findings: {len(rows)}",
        f"HIGH: {by_confidence['HIGH']}  MEDIUM: {by_confidence['MEDIUM']}  LOW: {by_confidence['LOW']}",
        "",
        "## Summary",
        "",
        "| Smell | Name | Findings |",
        "|---:|---|---:|",
    ]
    for (smell_id, smell_name), count in sorted(by_smell.items()):
        lines.append(f"| {smell_id} | {smell_name} | {count} |")
    lines.extend(["", "## Findings", ""])
    for finding in rows:
        lines.extend(
            [
                f"### {finding.finding_id} — {finding.smell_name} [{finding.confidence}]",
                "",
                f"- **Heuristic:** `{finding.heuristic_id}`",
                f"- **Source:** `{finding.source_id}`",
                f"- **Node:** `{finding.node_id}`",
                f"- **Section:** {finding.section_path or '—'}",
                f"- **Evidence:** {finding.evidence_text.replace(chr(10), ' ')}",
                f"- **Rationale:** {finding.rationale}",
                f"- **Reviewer question:** {finding.reviewer_question}",
                f"- **False-positive risk:** {finding.false_positive_risk}",
            ]
        )
        if finding.missing_evidence:
            lines.append(f"- **Missing evidence:** {'; '.join(finding.missing_evidence)}")
        lines.extend(["", "---", ""])
    return "\n".join(lines)

