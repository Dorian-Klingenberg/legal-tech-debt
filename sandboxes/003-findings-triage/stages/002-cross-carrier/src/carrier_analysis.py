"""Stage 002: Cross-carrier pattern analysis.

Loads enriched findings (Stage 001) and human review verdicts, filters to
confirmed findings, groups by smell and heuristic across carriers, and labels
each pattern as industry-wide or carrier-specific.

Usage:
    python carrier_analysis.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]

ENRICHED_FINDINGS = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/001-llm-triage/output/enriched_findings.jsonl"
)
REVIEW_VERDICTS = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/002-cross-carrier/data/review_verdicts.json"
)
OUTPUT_JSON = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/002-cross-carrier/output/carrier_comparison.json"
)
OUTPUT_MD = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/002-cross-carrier/output/carrier_comparison.md"
)


def carrier_from_source(source_id: str) -> str:
    if "KNIC" in source_id:
        return "KNIC"
    if "KFBM" in source_id:
        return "KFBM"
    return "UNKNOWN"


def load_findings(path: Path) -> list[dict]:
    findings = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                findings.append(json.loads(line))
    return findings


def load_verdicts(path: Path) -> dict[str, dict]:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return {v["finding_id"]: v for v in data["verdicts"]}


def apply_verdicts(findings: list[dict], verdicts: dict[str, dict]) -> list[dict]:
    confirmed = []
    for f in findings:
        fid = f["finding_id"]
        verdict = verdicts.get(fid, {})
        status = verdict.get("status", "confirmed")
        if status not in ("confirmed", "downgraded"):
            continue
        f = dict(f)
        revised = verdict.get("revised_severity")
        if revised:
            f["_revised_severity"] = revised
        else:
            f["_revised_severity"] = f.get("judgment", {}).get("business_severity", "")
        f["_review_status"] = status
        f["_review_reason"] = verdict.get("reason", "")
        f["_carrier"] = carrier_from_source(f.get("source_id", ""))
        confirmed.append(f)
    return confirmed


def group_findings(confirmed: list[dict]) -> dict:
    """Group by smell_id → heuristic_id → carrier → list of findings."""
    groups: dict[int, dict] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    smell_names: dict[int, str] = {}
    for f in confirmed:
        sid = f["smell_id"]
        hid = f["heuristic_id"]
        carrier = f["_carrier"]
        smell_names[sid] = f.get("smell_name", "")
        groups[sid][hid][carrier].append(f)
    return groups, smell_names


def build_output(confirmed: list[dict], groups: dict, smell_names: dict) -> dict:
    smell_summaries = []
    for smell_id in sorted(groups.keys()):
        heuristics = groups[smell_id]
        smell_name = smell_names[smell_id]
        patterns = []
        for heuristic_id in sorted(heuristics.keys()):
            carriers = heuristics[heuristic_id]
            knic = carriers.get("KNIC", [])
            kfbm = carriers.get("KFBM", [])
            industry_wide = bool(knic and kfbm)
            pattern_label = "industry-wide" if industry_wide else "carrier-specific"
            only_carrier = None
            if not industry_wide:
                only_carrier = "KNIC" if knic else "KFBM"

            # Collect unique terms/concepts flagged
            terms = set()
            for f in knic + kfbm:
                r = f.get("rationale", "")
                # Pull quoted terms from rationale if present
                import re
                quoted = re.findall(r"'([^']+)'", r)
                terms.update(quoted[:2])  # cap at 2 per finding to avoid noise

            patterns.append({
                "heuristic_id": heuristic_id,
                "pattern_label": pattern_label,
                "industry_wide": industry_wide,
                "only_carrier": only_carrier,
                "knic_count": len(knic),
                "kfbm_count": len(kfbm),
                "terms_flagged": sorted(terms),
                "knic_findings": [
                    {
                        "finding_id": f["finding_id"],
                        "section_path": f.get("section_path", ""),
                        "revised_severity": f["_revised_severity"],
                        "verdict": f.get("judgment", {}).get("triage_verdict", ""),
                    }
                    for f in knic
                ],
                "kfbm_findings": [
                    {
                        "finding_id": f["finding_id"],
                        "section_path": f.get("section_path", ""),
                        "revised_severity": f["_revised_severity"],
                        "verdict": f.get("judgment", {}).get("triage_verdict", ""),
                    }
                    for f in kfbm
                ],
            })

        smell_summaries.append({
            "smell_id": smell_id,
            "smell_name": smell_name,
            "confirmed_findings": sum(
                len(c) for h in heuristics.values() for c in h.values()
            ),
            "industry_wide_patterns": sum(1 for p in patterns if p["industry_wide"]),
            "carrier_specific_patterns": sum(1 for p in patterns if not p["industry_wide"]),
            "patterns": patterns,
        })

    return {
        "schema_version": "1.0.0",
        "stage": "003-002-cross-carrier",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "findings_source": str(ENRICHED_FINDINGS),
        "review_verdicts_source": str(REVIEW_VERDICTS),
        "total_input_findings": 35,
        "confirmed_findings": len(confirmed),
        "smells": smell_summaries,
    }


def build_markdown(output: dict) -> str:
    lines = [
        "# Stage 002: Cross-Carrier Pattern Analysis",
        "",
        f"Run: {output['run_at'][:10]}  ",
        f"Confirmed findings: {output['confirmed_findings']} of {output['total_input_findings']} total  ",
        "",
        "---",
        "",
    ]

    for smell in output["smells"]:
        lines += [
            f"## Smell {smell['smell_id']}: {smell['smell_name']}",
            "",
            f"**Confirmed findings:** {smell['confirmed_findings']}  ",
            f"**Industry-wide patterns:** {smell['industry_wide_patterns']}  ",
            f"**Carrier-specific patterns:** {smell['carrier_specific_patterns']}  ",
            "",
        ]

        # Comparison table
        lines += [
            "| Heuristic | Pattern | KNIC | KFBM | Terms Flagged |",
            "|---|---|---|---|---|",
        ]
        for p in smell["patterns"]:
            label = "**industry-wide**" if p["industry_wide"] else f"carrier-specific ({p['only_carrier']})"
            terms = ", ".join(p["terms_flagged"][:3]) if p["terms_flagged"] else "—"
            lines.append(
                f"| {p['heuristic_id']} | {label} | {p['knic_count']} | {p['kfbm_count']} | {terms} |"
            )

        lines.append("")

        # Industry-wide callout
        iw = [p for p in smell["patterns"] if p["industry_wide"]]
        if iw:
            lines += ["**Industry-wide patterns (strongest signal):**", ""]
            for p in iw:
                terms_str = f" — terms: {', '.join(p['terms_flagged'][:3])}" if p["terms_flagged"] else ""
                lines.append(f"- **{p['heuristic_id']}**{terms_str}: {p['knic_count']} KNIC finding(s), {p['kfbm_count']} KFBM finding(s)")
            lines.append("")

        cs = [p for p in smell["patterns"] if not p["industry_wide"]]
        if cs:
            lines += ["**Carrier-specific patterns:**", ""]
            for p in cs:
                terms_str = f" — terms: {', '.join(p['terms_flagged'][:3])}" if p["terms_flagged"] else ""
                lines.append(f"- **{p['heuristic_id']}** ({p['only_carrier']} only){terms_str}: {p['knic_count'] + p['kfbm_count']} finding(s)")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    if not ENRICHED_FINDINGS.exists():
        sys.exit(f"Enriched findings not found: {ENRICHED_FINDINGS}")
    if not REVIEW_VERDICTS.exists():
        sys.exit(f"Review verdicts not found: {REVIEW_VERDICTS}")

    findings = load_findings(ENRICHED_FINDINGS)
    verdicts = load_verdicts(REVIEW_VERDICTS)
    confirmed = apply_verdicts(findings, verdicts)
    groups, smell_names = group_findings(confirmed)
    output = build_output(confirmed, groups, smell_names)

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(output, fh, indent=2, ensure_ascii=False)

    md = build_markdown(output)
    with open(OUTPUT_MD, "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"Confirmed findings: {output['confirmed_findings']} of {output['total_input_findings']}")
    print(f"Smells with confirmed findings: {len(output['smells'])}")
    for smell in output["smells"]:
        iw = smell["industry_wide_patterns"]
        cs = smell["carrier_specific_patterns"]
        print(f"  Smell {smell['smell_id']}: {smell['confirmed_findings']} findings — {iw} industry-wide, {cs} carrier-specific")
    print(f"\nJSON:     {OUTPUT_JSON}")
    print(f"Markdown: {OUTPUT_MD}")


if __name__ == "__main__":
    main()
