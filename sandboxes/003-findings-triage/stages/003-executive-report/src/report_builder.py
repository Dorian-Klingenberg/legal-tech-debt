"""Stage 003: Executive summary report.

Combines Stage 001 enriched findings, Stage 002 cross-carrier analysis, and
human review verdicts to produce a markdown report written for a CEO or Chief
Claims Officer prospect audience.

Tone: "Here is what we found in your industry" — analyst perspective, not a
compliance fix-it list.

Usage:
    python report_builder.py
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------------------------------
# Markdown safety
# ---------------------------------------------------------------------------

# Dollar signs act as LaTeX math delimiters in many markdown renderers
# (GitHub, Obsidian, VS Code with math extensions, most PDF converters).
# Any two $-signs that can be parsed as a matching pair render the content
# between them as a math expression — spaces drop out, letters go italic.
# This has surfaced multiple times in this report (BACKLOG-016).
#
# _safe_dollar() replaces bare $<number> patterns with a renderer-safe form.
# Apply to the complete report string before writing — covers LLM prose and
# deterministic sections equally.

_DOLLAR_RE = re.compile(r'\$(\d[\d,./KMBkmbillion]*)')


def _safe_dollar(text: str) -> str:
    """Replace $<amount> with <amount> USD throughout a markdown string.

    Removes the $ sign that triggers math-delimiter rendering in LaTeX-aware
    markdown renderers.  Single isolated $ signs before non-numeric chars are
    left untouched (they cannot form a math pair with another $ sign).
    """
    return _DOLLAR_RE.sub(r'\1', text)


REPO_ROOT = Path(__file__).resolve().parents[5]
load_dotenv(REPO_ROOT / ".env")

ENRICHED_FINDINGS = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/001-llm-triage/output/enriched_findings.jsonl"
)
DOLLAR_ANCHORS = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/003-executive-report/data/dollar_anchors.json"
)
CARRIER_COMPARISON = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/002-cross-carrier/output/carrier_comparison.json"
)
REVIEW_VERDICTS = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/002-cross-carrier/data/review_verdicts.json"
)
OUTPUT_MD = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/003-executive-report/output/executive_summary.md"
)
OUTPUT_MD_ANON = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/003-executive-report/output/executive_summary_anon.md"
)

# Carrier label maps.  Identity map = internal report; anonymized map = external/prospect report.
CARRIER_LABELS_INTERNAL: dict[str, str] = {"KNIC": "KNIC", "KFBM": "KFBM"}
CARRIER_LABELS_ANON: dict[str, str] = {"KNIC": "Carrier A", "KFBM": "Carrier B"}

MODEL = "gpt-4o"
MAX_TOKENS = 1200


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_findings(path: Path) -> list[dict]:
    findings = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                findings.append(json.loads(line))
    return findings


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def apply_verdicts(
    findings: list[dict],
    verdicts_data: dict,
    carrier_labels: dict[str, str],
) -> list[dict]:
    verdicts = {v["finding_id"]: v for v in verdicts_data["verdicts"]}
    confirmed = []
    for f in findings:
        v = verdicts.get(f["finding_id"], {})
        status = v.get("status", "confirmed")
        if status not in ("confirmed", "downgraded"):
            continue
        f = dict(f)
        f["_revised_severity"] = v.get("revised_severity") or f.get("judgment", {}).get("business_severity", "")
        raw_carrier = "KNIC" if "KNIC" in f.get("source_id", "") else "KFBM"
        f["_carrier"] = carrier_labels.get(raw_carrier, raw_carrier)
        confirmed.append(f)
    return confirmed


# ---------------------------------------------------------------------------
# LLM narrative generation
# ---------------------------------------------------------------------------

def call_llm(client: OpenAI, system: str, user: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return response.choices[0].message.content.strip()


NARRATIVE_SYSTEM = """\
You are a senior insurance industry analyst writing a briefing for a CEO or Chief Claims Officer at a homeowners insurance carrier.
Tone: authoritative, clear, peer-to-peer — not alarmist, not salesy. You are presenting industry research findings, not auditing the reader's company.
Write in plain English. No jargon, no legal conclusions. No bullet points unless specifically asked.
Do not invent dollar figures, case citations, or statistics not provided in the context.
Do not mention specific carrier names (KNIC, KFBM) — refer to them as 'the carriers analyzed' or 'carriers in this study.'"""


def write_executive_intro(client: OpenAI, comparison: dict, confirmed: list[dict]) -> str:
    industry_wide = sum(
        s["industry_wide_patterns"] for s in comparison["smells"]
    )
    total_confirmed = comparison["confirmed_findings"]
    smell_names = [s["smell_name"] for s in comparison["smells"]]

    prompt = f"""\
Write a 3-paragraph executive introduction for a briefing titled "Kentucky Homeowners Insurance: Policy Language Risk Patterns."

Context:
- We analyzed homeowners insurance policy filings, rate manuals, and endorsements from two Kentucky carriers
- We identified {total_confirmed} confirmed findings across {len(smell_names)} risk categories: {', '.join(smell_names)}
- {industry_wide} of those patterns appear in both carriers independently — making them industry patterns, not isolated filing errors
- The analysis covers policy form language, rate rule filings, and endorsements submitted to the Kentucky DOI

Paragraph 1: Frame what the research is and why it matters for a CCO or CEO. Make it clear this is industry-wide analysis, not a compliance audit.
Paragraph 2: Summarize the key finding in one or two sentences — what stands out most across carriers.
Paragraph 3: One sentence on what this means for a carrier that wants to get ahead of the risk.

Do not mention specific carrier names. Do not invent dollar figures."""

    return call_llm(client, NARRATIVE_SYSTEM, prompt)


def write_pattern_narrative(client: OpenAI, smell: dict, pattern: dict, findings_for_pattern: list[dict], anchors: list[dict] | None = None) -> str:
    sample_plain = next(
        (f.get("triage", {}).get("plain_english", "") for f in findings_for_pattern if f.get("triage", {}).get("plain_english")),
        ""
    )
    sample_dispute = next(
        (f.get("triage", {}).get("dispute_scenario", "") for f in findings_for_pattern if f.get("triage", {}).get("dispute_scenario")),
        ""
    )
    label = "both carriers analyzed" if pattern["industry_wide"] else "one of the carriers analyzed"
    terms = ", ".join(f'"{t}"' for t in pattern["terms_flagged"][:3]) if pattern["terms_flagged"] else "undefined valuation terms"

    heuristic_descriptions = {
        "SMELL2-H001": "undefined timing language ('reasonable time') in loss settlement conditions — controls whether a claim is paid at replacement cost or actual cash value",
        "SMELL2-H003": "undefined valuation terms ('actual cash value', 'replacement cost') used in loss settlement without a calculation methodology or external reference",
        "SMELL5-H004": "carrier rate-setting and premium-computation filings with no traceable citation to a Kentucky statute (KRS), administrative regulation (KAR), or DOI bulletin — the regulatory authority for these rate rules is unverifiable from the filing",
        "SMELL5-H005": "mandatory coverage language asserting that certain coverages are required, with no regulatory citation to establish what authority mandates them",
        "SMELL5-H006": "loss settlement methodology sections with no traceable regulatory citation for the settlement approach used",
    }
    heuristic_desc = heuristic_descriptions.get(
        pattern["heuristic_id"],
        f"policy language pattern under {pattern['heuristic_id']}"
    )

    anchor_block = ""
    if anchors:
        anchor_lines = []
        for a in anchors:
            anchor_lines.append(f"- {a['label']} ({a['dollar_figure']}): {a['description']}")
        anchor_block = "\nPublic cost examples you may reference (do not invent additional figures):\n" + "\n".join(anchor_lines)

    prompt = f"""\
Write 2 short paragraphs (3-4 sentences each) describing this insurance policy risk pattern for a CEO or CCO audience.

Pattern: {pattern['heuristic_id']} under "{smell['smell_name']}"
What this pattern detects: {heuristic_desc}
Appears in: {label}
KNIC findings: {pattern['knic_count']}, KFBM findings: {pattern['kfbm_count']}

Plain-English description of one example finding:
{sample_plain}

Example claim dispute scenario:
{sample_dispute}
{anchor_block}
Paragraph 1: What the pattern is and where it appears in policy documents. Be precise about what is missing or undefined. Do not mention carrier names.
Paragraph 2: What the practical risk is — what dispute, regulatory exposure, or claims challenge does this gap create? Where public cost examples are provided above, weave one or two into the paragraph naturally to ground the risk in real events. Do not present them as hypotheticals.

Keep it grounded. No legal conclusions. No invented figures beyond those provided."""

    return call_llm(client, NARRATIVE_SYSTEM, prompt)


def write_closing(client: OpenAI, comparison: dict) -> str:
    industry_wide_count = sum(s["industry_wide_patterns"] for s in comparison["smells"])
    prompt = f"""\
Write a 2-paragraph closing section for the briefing titled "What Forward-Looking Carriers Are Doing."

Context:
- {industry_wide_count} of the risk patterns identified appear across multiple independently-filed carriers — suggesting industry-wide drafting conventions rather than isolated errors
- The patterns involve undefined valuation terms (actual cash value, replacement cost), unanchored rate methodology, and undefined timing language in loss settlement conditions
- These are addressable through policy language revisions, explicit methodology citations, and regulatory cross-referencing

Paragraph 1: What a carrier that takes these findings seriously does next — framed as proactive risk management, not remediation of violations.
Paragraph 2: One or two sentences on the broader value of systematic policy language review as a practice.

Tone: peer-to-peer. This is what smart carriers do, not what they are required to do."""

    return call_llm(client, NARRATIVE_SYSTEM, prompt)


# ---------------------------------------------------------------------------
# Report assembly
# ---------------------------------------------------------------------------

def severity_sort_key(f: dict) -> int:
    return {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(f.get("_revised_severity", "LOW"), 3)


def build_findings_table(
    confirmed: list[dict],
    comparison: dict,
    carrier_labels: dict[str, str],
) -> str:
    """One row per pattern (smell + heuristic), not per individual finding."""
    from collections import defaultdict
    pattern_map: dict[tuple, list] = defaultdict(list)
    for f in confirmed:
        key = (f["smell_id"], f["heuristic_id"])
        pattern_map[key].append(f)

    rows = []
    for smell in comparison["smells"]:
        for pattern in smell["patterns"]:
            key = (smell["smell_id"], pattern["heuristic_id"])
            findings = pattern_map.get(key, [])
            if not findings:
                continue
            carriers = sorted({f["_carrier"] for f in findings})
            carrier_str = "Both carriers" if len(carriers) > 1 else f"{carriers[0]} only"
            severities = [f["_revised_severity"] for f in findings]
            top_severity = "HIGH" if "HIGH" in severities else ("MEDIUM" if "MEDIUM" in severities else "LOW")
            terms = ", ".join(f'"{t}"' for t in pattern["terms_flagged"][:2]) if pattern["terms_flagged"] else "—"
            scope = "Industry-wide" if pattern["industry_wide"] else "Carrier-specific"
            rows.append((top_severity, smell["smell_name"], pattern["heuristic_id"], carrier_str, scope, terms, len(findings)))

    lines = [
        "| Severity | Risk Category | Pattern | Carriers | Scope | Terms Flagged | # Findings |",
        "|---|---|---|---|---|---|---|",
    ]
    for severity, smell_name, heuristic, carrier_str, scope, terms, count in rows:
        lines.append(f"| {severity} | {smell_name} | {heuristic} | {carrier_str} | {scope} | {terms} | {count} |")
    return "\n".join(lines)


def build_risk_context_section(anchors_data: dict) -> str:
    lines = [
        "## Risk Context: What This Costs When It Goes Wrong",
        "",
        "*The patterns identified in this analysis are not theoretical. "
        "The following public events illustrate the cost range when similar gaps are not caught early.*",
        "",
    ]
    for smell_data in anchors_data["smells"].values():
        lines += [f"**{smell_data['smell_name']}**", ""]
        for anchor in smell_data["anchors"]:
            # Strip dollar amounts from the label into the description line
            # to avoid markdown math-delimiter rendering issues with $ inside bold
            label = anchor["label"]
            lines.append(f"- **{label}** — {anchor['description']}")
        lines.append("")

    pf = anchors_data.get("portfolio_framing", {})
    if pf:
        lines += [
            "**Portfolio-Level Exposure Framing**",
            "",
            f"{pf.get('description', '')}",
            "",
        ]
        for r in pf.get("ranges", []):
            lines.append(
                f"- *{r['category']}:* {r['annual_estimate']} estimated annual impact "
                f"({r['ten_year_range']} over ten years)"
            )
        lines += [
            "",
            f"> {pf.get('conservative_pitch', '')}",
            "",
        ]
    return "\n".join(lines)


def build_report(
    intro: str,
    comparison: dict,
    confirmed: list[dict],
    pattern_narratives: dict,
    closing: str,
    anchors_data: dict | None = None,
    carrier_labels: dict[str, str] | None = None,
) -> str:
    if carrier_labels is None:
        carrier_labels = CARRIER_LABELS_INTERNAL
    date_str = datetime.now(timezone.utc).strftime("%B %Y")
    lines = [
        "# Kentucky Homeowners Insurance: Policy Language Risk Patterns",
        "",
        f"*Industry Analysis — {date_str}*  ",
        f"*Based on review of homeowners policy filings, rate manuals, and endorsements from two Kentucky carriers*",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        intro,
        "",
        "---",
        "",
        "## Industry-Wide Patterns",
        "",
        "*Patterns appearing in both carriers independently carry the strongest signal — they reflect industry drafting conventions, not isolated filing choices.*",
        "",
    ]

    for smell in comparison["smells"]:
        iw_patterns = [p for p in smell["patterns"] if p["industry_wide"]]
        if not iw_patterns:
            continue

        lines += [
            f"### {smell['smell_name']}",
            "",
        ]

        for pattern in iw_patterns:
            pattern_key = f"{smell['smell_id']}_{pattern['heuristic_id']}"
            narrative = pattern_narratives.get(pattern_key, "")
            terms = ", ".join(f'"{t}"' for t in pattern["terms_flagged"][:3]) if pattern["terms_flagged"] else ""
            carrier_count = f"({pattern['knic_count']} + {pattern['kfbm_count']} findings across both carriers)"

            lines += [
                f"**{pattern['heuristic_id']}** {carrier_count}",
                "",
            ]
            if terms:
                lines += [f"*Language flagged: {terms}*", ""]
            if narrative:
                lines += [narrative, ""]

    lines += [
        "---",
        "",
        "## Carrier-Specific Patterns",
        "",
        "*Patterns appearing in only one carrier may reflect a specific drafting choice or filing vintage. Worth monitoring but lower systemic significance than industry-wide patterns.*",
        "",
    ]

    for smell in comparison["smells"]:
        cs_patterns = [p for p in smell["patterns"] if not p["industry_wide"]]
        if not cs_patterns:
            continue
        lines += [f"**{smell['smell_name']}**", ""]
        for pattern in cs_patterns:
            count = pattern["knic_count"] + pattern["kfbm_count"]
            carrier = carrier_labels.get(pattern["only_carrier"], pattern["only_carrier"])
            terms = ", ".join(f'"{t}"' for t in pattern["terms_flagged"][:3]) if pattern["terms_flagged"] else "—"
            lines.append(
                f"- **{pattern['heuristic_id']}** — {carrier}, {count} finding(s). Terms: {terms}"
            )
        lines.append("")

    # Risk context section — dollar anchors before the findings table
    if anchors_data:
        lines += [
            "---",
            "",
            build_risk_context_section(anchors_data),
        ]

    lines += [
        "---",
        "",
        "## Confirmed Findings",
        "",
        f"*{comparison['confirmed_findings']} confirmed findings after human review of {comparison['total_input_findings']} detector outputs.*",
        "",
        build_findings_table(confirmed, comparison, carrier_labels),
        "",
        "---",
        "",
        "## What Forward-Looking Carriers Are Doing",
        "",
        closing,
        "",
        "---",
        "",
        "## Methodology Note",
        "",
        "This analysis uses deterministic pattern detection over parsed policy documents, "
        "followed by LLM-assisted annotation and human expert review. Findings represent "
        "patterns that warrant review by a compliance team or coverage attorney — they are "
        "not legal conclusions and should not be acted on without qualified professional judgment. "
        "The corpus covers two Kentucky homeowners carriers; patterns may or may not generalize "
        "to other carriers or states.",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Build executive summary report")
    parser.add_argument(
        "--anonymize",
        action="store_true",
        help="Replace carrier names with generic labels (Carrier A, Carrier B) for external/prospect distribution.",
    )
    args = parser.parse_args()

    carrier_labels = CARRIER_LABELS_ANON if args.anonymize else CARRIER_LABELS_INTERNAL
    output_path = OUTPUT_MD_ANON if args.anonymize else OUTPUT_MD

    if args.anonymize:
        print("[report-builder] Anonymize mode ON — carrier names will be replaced with generic labels.")
        print(f"[report-builder] Label map: {carrier_labels}")

    for p in (ENRICHED_FINDINGS, CARRIER_COMPARISON, REVIEW_VERDICTS, DOLLAR_ANCHORS):
        if not p.exists():
            sys.exit(f"Required input not found: {p}")

    findings = load_findings(ENRICHED_FINDINGS)
    comparison = load_json(CARRIER_COMPARISON)
    verdicts_data = load_json(REVIEW_VERDICTS)
    anchors_data = load_json(DOLLAR_ANCHORS)
    confirmed = apply_verdicts(findings, verdicts_data, carrier_labels)

    client = OpenAI()

    print("Writing executive intro...")
    intro = write_executive_intro(client, comparison, confirmed)

    print("Writing pattern narratives...")
    pattern_narratives = {}
    # Build a lookup: finding_id → finding
    finding_by_id = {f["finding_id"]: f for f in confirmed}

    for smell in comparison["smells"]:
        for pattern in smell["patterns"]:
            if not pattern["industry_wide"]:
                continue
            fids = (
                [p["finding_id"] for p in pattern["knic_findings"]]
                + [p["finding_id"] for p in pattern["kfbm_findings"]]
            )
            findings_for_pattern = [finding_by_id[fid] for fid in fids if fid in finding_by_id]
            key = f"{smell['smell_id']}_{pattern['heuristic_id']}"
            print(f"  {key}...")
            smell_anchors = anchors_data.get("smells", {}).get(str(smell["smell_id"]), {}).get("anchors")
            pattern_narratives[key] = write_pattern_narrative(
                client, smell, pattern, findings_for_pattern, anchors=smell_anchors
            )

    print("Writing closing...")
    closing = write_closing(client, comparison)

    report = build_report(
        intro, comparison, confirmed, pattern_narratives, closing,
        anchors_data=anchors_data,
        carrier_labels=carrier_labels,
    )

    # Sanitize dollar signs before writing — prevents math-delimiter rendering
    # corruption in LaTeX-aware markdown renderers (BACKLOG-016).
    report = _safe_dollar(report)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(report)

    print(f"\nReport: {output_path}")
    print(f"Length: {len(report.splitlines())} lines")


if __name__ == "__main__":
    main()
