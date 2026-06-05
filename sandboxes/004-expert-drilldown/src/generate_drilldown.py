"""Sandbox 004: Expert Drill-Down Report Generator

Reads drill_down_entries.json and produces a dark-themed HTML report.

Usage:
    python src/generate_drilldown.py                    # all carriers -> drilldown_report.html
    python src/generate_drilldown.py --carrier KFBM     # KFBM only   -> drilldown_KFBM.html
    python src/generate_drilldown.py --carrier KNIC     # KNIC only   -> drilldown_KNIC.html
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from html import escape

SANDBOX_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE    = SANDBOX_ROOT / "data" / "drill_down_entries.json"
OUTPUT_DIR   = SANDBOX_ROOT / "output"

# ---------------------------------------------------------------------------
# CSS — dark theme
# ---------------------------------------------------------------------------

CSS = """
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 15px;
    line-height: 1.6;
    color: #c9d1d9;
    background: #0d1117;
  }

  /* ── Layout ───────────────────────────────────────────────────────── */
  .page-header {
    background: #010409;
    color: #e6edf3;
    padding: 28px 40px 24px;
    border-bottom: 3px solid #da3633;
  }
  .page-header h1 { font-size: 1.4rem; font-weight: 600; letter-spacing: -0.01em; }
  .page-header .subtitle { font-size: 0.85rem; color: #8b949e; margin-top: 4px; }

  .page-body { max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }

  /* ── Finding card ─────────────────────────────────────────────────── */
  .finding-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    margin-bottom: 40px;
    overflow: hidden;
  }

  .finding-header {
    padding: 20px 28px 16px;
    border-bottom: 1px solid #21262d;
    display: flex;
    align-items: flex-start;
    gap: 20px;
  }

  .badge-col { display: flex; flex-direction: column; gap: 6px; min-width: 120px; }

  .badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    white-space: nowrap;
  }
  .badge-high     { background: #3d0c0c; color: #f85149; border: 1px solid #6e1a1a; }
  .badge-medium   { background: #2d1f00; color: #d29922; border: 1px solid #5a3e00; }
  .badge-low      { background: #0c2a0c; color: #3fb950; border: 1px solid #1a4e1a; }
  .badge-heuristic{ background: #0d1f3c; color: #58a6ff; border: 1px solid #1a3a6e; }
  .badge-carrier  { background: #1a1a2e; color: #a5b4fc; border: 1px solid #2e3a5e; }
  .badge-industry { background: #0c2a1a; color: #3fb950; border: 1px solid #1a4e2a; }

  .finding-meta { flex: 1; }
  .finding-meta h2 { font-size: 1.1rem; font-weight: 600; color: #e6edf3; margin-bottom: 4px; }
  .finding-meta .source-line { font-size: 0.82rem; color: #8b949e; }
  .finding-meta .section-line {
    font-size: 0.82rem;
    color: #6e7681;
    margin-top: 2px;
    font-family: "SF Mono", "Fira Code", monospace;
  }

  /* ── Evidence block ───────────────────────────────────────────────── */
  .evidence-block {
    margin: 0;
    padding: 16px 28px;
    background: #0d1117;
    border-bottom: 1px solid #21262d;
  }
  .evidence-block .label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #6e7681;
    margin-bottom: 6px;
  }
  .verbatim {
    font-family: "SF Mono", "Fira Code", "Courier New", monospace;
    font-size: 0.88rem;
    color: #f85149;
    background: #1a0a0a;
    border-left: 3px solid #da3633;
    padding: 10px 14px;
    border-radius: 0 4px 4px 0;
  }
  .context-text {
    font-size: 0.85rem;
    color: #8b949e;
    margin-top: 10px;
    font-style: italic;
    line-height: 1.5;
  }

  /* ── Gap statement ────────────────────────────────────────────────── */
  .gap-block {
    padding: 16px 28px;
    border-bottom: 1px solid #21262d;
    background: #1a1200;
    border-left: 4px solid #9e6a03;
  }
  .gap-block .label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #9e6a03;
    margin-bottom: 6px;
  }
  .gap-block p { font-size: 0.9rem; color: #c9d1d9; line-height: 1.65; }

  /* ── Three-panel reader sections ──────────────────────────────────── */
  .reader-panels {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: 1px solid #21262d;
  }

  .panel {
    padding: 20px 24px 24px;
    border-right: 1px solid #21262d;
  }
  .panel:last-child { border-right: none; }

  .panel-heading {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 2px solid #21262d;
  }
  .panel-icon { font-size: 1rem; }
  .panel-title { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; }

  .panel-compliance .panel-title { color: #58a6ff; }
  .panel-compliance .panel-heading { border-color: #1a3a6e; }

  .panel-claims .panel-title { color: #d29922; }
  .panel-claims .panel-heading { border-color: #5a3e00; }

  .panel-policy .panel-title { color: #3fb950; }
  .panel-policy .panel-heading { border-color: #1a4e2a; }

  .panel p, .panel li { font-size: 0.85rem; color: #c9d1d9; line-height: 1.6; }
  .panel ul { list-style: none; padding: 0; }
  .panel ul li { padding: 6px 0; border-bottom: 1px solid #21262d; }
  .panel ul li:last-child { border-bottom: none; }

  .citation-item { margin-bottom: 10px; }
  .citation-ref {
    font-family: "SF Mono", "Fira Code", monospace;
    font-size: 0.78rem;
    font-weight: 600;
    color: #58a6ff;
    display: block;
    margin-bottom: 2px;
  }
  .citation-summary { font-size: 0.82rem; color: #8b949e; line-height: 1.5; }

  .question-block {
    margin-top: 14px;
    padding: 10px 12px;
    background: #0d1f3c;
    border-radius: 4px;
    border-left: 3px solid #388bfd;
    font-size: 0.82rem;
    color: #a5c4f3;
    font-style: italic;
  }

  .scenario-block {
    margin-top: 10px;
    padding: 10px 12px;
    background: #1a1000;
    border-radius: 4px;
    border-left: 3px solid #9e6a03;
    font-size: 0.82rem;
    color: #c9a84c;
    line-height: 1.55;
  }

  .risk-tag {
    display: inline-block;
    margin-top: 10px;
    margin-right: 6px;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    background: #2d1f00;
    color: #d29922;
    border: 1px solid #5a3e00;
  }
  .risk-tag-high {
    background: #3d0c0c;
    color: #f85149;
    border-color: #6e1a1a;
  }

  .redline-block { margin-top: 10px; }
  .redline-label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #8b949e; margin-bottom: 4px; }
  .redline-old {
    font-family: "SF Mono", "Fira Code", monospace;
    font-size: 0.8rem;
    color: #f85149;
    background: #1a0a0a;
    border-left: 3px solid #6e1a1a;
    padding: 8px 10px;
    border-radius: 0 3px 3px 0;
    text-decoration: line-through;
    opacity: 0.8;
    margin-bottom: 6px;
  }
  .redline-new {
    font-family: "SF Mono", "Fira Code", monospace;
    font-size: 0.8rem;
    color: #3fb950;
    background: #0c2a0c;
    border-left: 3px solid #1a4e2a;
    padding: 8px 10px;
    border-radius: 0 3px 3px 0;
    margin-bottom: 8px;
  }
  .refiling-note {
    margin-top: 10px;
    font-size: 0.78rem;
    color: #c9d1d9;
    background: #1c2128;
    padding: 8px 10px;
    border-radius: 4px;
    border: 1px solid #30363d;
  }
  .refiling-note strong { color: #e6edf3; }

  .disclaimer {
    margin-top: 14px;
    font-size: 0.74rem;
    color: #6e7681;
    font-style: italic;
    border-top: 1px dashed #30363d;
    padding-top: 10px;
  }

  /* ── Nav bar ──────────────────────────────────────────────────────── */
  .report-nav {
    font-size: 0.8rem;
    color: #8b949e;
    margin-bottom: 24px;
    padding: 12px 16px;
    background: #161b22;
    border-radius: 6px;
    border: 1px solid #30363d;
  }
  .report-nav strong { color: #c9d1d9; }
  .nav-item {
    display: inline-block;
    margin-right: 16px;
    padding: 2px 0;
    color: #8b949e;
    cursor: pointer;
  }
  .nav-item:hover { color: #f85149; }
  .nav-active { color: #58a6ff; font-weight: 600; }
"""

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def _badge(text: str, cls: str) -> str:
    return f'<span class="badge {cls}">{escape(text)}</span>'

def _severity_badge(level: str) -> str:
    cls = {"HIGH": "badge-high", "MEDIUM": "badge-medium", "LOW": "badge-low"}.get(level.upper(), "badge-low")
    return _badge(f"{level} severity", cls)

def _confidence_badge(level: str) -> str:
    cls = {"HIGH": "badge-high", "MEDIUM": "badge-medium", "LOW": "badge-low"}.get(level.upper(), "badge-low")
    return _badge(f"{level} confidence", cls)


def _render_entry(e: dict, sanitize: bool = False) -> str:
    """Render one drill-down entry to HTML.

    sanitize: when True, use paraphrased_evidence / paraphrased_context instead of
    verbatim carrier text. Safe for commercial distribution (BACKLOG-022).
    """
    eid = escape(e.get("entry_id", ""))

    # ── Header badges ──
    severity   = e.get("severity", "")
    confidence = e.get("confidence", "")
    heuristic  = e.get("heuristic_id", "")

    # Carrier display — single or multi
    if "carriers" in e:
        carrier_text = " + ".join(e["carriers"])
        scope_text = e.get("scope", "Industry-wide")
    else:
        carrier_text = e.get("carrier", "")
        scope_text = e.get("scope", "Carrier-specific")

    badges = "\n".join([
        _severity_badge(severity),
        _confidence_badge(confidence),
        _badge(heuristic, "badge-heuristic"),
        _badge(carrier_text, "badge-carrier"),
    ])
    if "industry" in scope_text.lower():
        badges += "\n" + _badge("Industry-wide", "badge-industry")

    # ── Title / source ──
    title   = escape(e.get("title", heuristic))
    source  = escape(e.get("source_description", e.get("source_id", "")))
    section = escape(e.get("section_path", ""))

    # ── Evidence — verbatim (internal) or paraphrased (commercial/sanitized) ──
    if sanitize:
        # Use top-level paraphrased fields; fall back to primary_instance if needed
        raw_verbatim = (
            e.get("paraphrased_evidence")
            or e.get("primary_instance", {}).get("verbatim_evidence", "")
        )
        raw_context = e.get("paraphrased_context", "")
    else:
        raw_verbatim = (
            e.get("verbatim_evidence")
            or e.get("primary_instance", {}).get("verbatim_evidence", "")
        )
        raw_context = e.get("verbatim_context", e.get("context", ""))

    verbatim = escape(raw_verbatim)
    context  = escape(raw_context)

    # ── Gap statement ──
    gap = escape(e.get("gap_statement", ""))

    # ── Compliance panel ──
    comp = e.get("compliance_section", {})
    citations_html = ""
    for c in comp.get("regulatory_citations", []):
        citations_html += f"""
      <div class="citation-item">
        <span class="citation-ref">{escape(c.get('citation',''))}</span>
        <span class="citation-summary">{escape(c.get('summary',''))}</span>
      </div>"""
    comp_question = escape(comp.get("compliance_question", ""))
    question_html = f'<div class="question-block">{comp_question}</div>' if comp_question else ""

    # ── Claims panel ──
    claims = e.get("claims_section", {})
    claims_narrative = escape(claims.get("exposure_narrative", ""))
    dispute = escape(claims.get("dispute_scenario", ""))
    bad_faith = claims.get("bad_faith_risk", "")
    scenario_html = f'<div class="scenario-block"><strong>Dispute scenario:</strong> {dispute}</div>' if dispute else ""
    bf_level = "HIGH" if "HIGH" in bad_faith.upper() else ("MEDIUM" if "MEDIUM" in bad_faith.upper() else "LOW")
    risk_cls = "risk-tag risk-tag-high" if bf_level == "HIGH" else "risk-tag"
    risk_tag = f'<span class="{risk_cls}">Bad-faith risk: {escape(bf_level)}</span>'

    # ── Policy panel ──
    policy = e.get("policy_designer_section", {})
    if sanitize:
        current_lang = escape(
            policy.get("paraphrased_current_language")
            or policy.get("current_language", "")
        )
    else:
        current_lang = escape(policy.get("current_language", ""))
    suggested_lang = escape(policy.get("suggested_language", ""))
    remediation   = escape(policy.get("remediation_note", ""))
    refiling      = escape(policy.get("refiling_note", ""))
    refiling_req  = policy.get("doi_refiling_required", False)
    disclaimer    = escape(policy.get("disclaimer", ""))

    redline_html = ""
    if current_lang or suggested_lang:
        redline_html = f"""
      <div class="redline-block">
        <div class="redline-label">Current language</div>
        <div class="redline-old">{current_lang}</div>
        <div class="redline-label">Suggested language</div>
        <div class="redline-new">{suggested_lang}</div>
      </div>"""

    refiling_badge = "Yes" if refiling_req else "No"
    refiling_html = f'<div class="refiling-note"><strong>DOI refiling required: {refiling_badge}.</strong> {refiling}</div>' if refiling else ""
    remediation_html = f'<div class="refiling-note" style="margin-top:8px;">{remediation}</div>' if remediation else ""
    disclaimer_html = f'<div class="disclaimer">{disclaimer}</div>' if disclaimer else ""

    return f"""
  <div class="finding-card" id="{eid}">

    <div class="finding-header">
      <div class="badge-col">
        {badges}
      </div>
      <div class="finding-meta">
        <h2>{title}</h2>
        <div class="source-line">{source}</div>
        <div class="section-line">{section}</div>
      </div>
    </div>

    <div class="evidence-block">
      <div class="label">Verbatim triggering language</div>
      <div class="verbatim">{verbatim}</div>
      {"<div class='context-text'>" + context + "</div>" if context else ""}
    </div>

    <div class="gap-block">
      <div class="label">The gap</div>
      <p>{gap}</p>
    </div>

    <div class="reader-panels">

      <div class="panel panel-compliance">
        <div class="panel-heading">
          <span class="panel-icon">⚖️</span>
          <span class="panel-title">Compliance &amp; Coverage Counsel</span>
        </div>
        {citations_html}
        {question_html}
      </div>

      <div class="panel panel-claims">
        <div class="panel-heading">
          <span class="panel-icon">📋</span>
          <span class="panel-title">Claims Professional</span>
        </div>
        <p>{claims_narrative}</p>
        {scenario_html}
        {risk_tag}
      </div>

      <div class="panel panel-policy">
        <div class="panel-heading">
          <span class="panel-icon">✏️</span>
          <span class="panel-title">Policy Designer / Filing Specialist</span>
        </div>
        {redline_html}
        {refiling_html}
        {remediation_html}
        {disclaimer_html}
      </div>

    </div>

  </div>"""


# ---------------------------------------------------------------------------
# Carrier filter
# ---------------------------------------------------------------------------

def _entry_matches_carrier(entry: dict, carrier: str) -> bool:
    """Return True if this entry belongs to the target carrier."""
    if "carriers" in entry:
        return carrier.upper() in [c.upper() for c in entry["carriers"]]
    return entry.get("carrier", "").upper() == carrier.upper()


# ---------------------------------------------------------------------------
# Report assembly
# ---------------------------------------------------------------------------

def build_report(entries: list[dict], carrier: str | None, sanitize: bool = False) -> str:
    if carrier:
        title = f"Kentucky Homeowners Insurance — Expert Drill-Down Report — {carrier.upper()}"
        subtitle = f"Confidential · {carrier.upper()} Filings Only · Not Legal Advice · Findings require review by qualified coverage counsel"
    else:
        title = "Kentucky Homeowners Insurance — Expert Drill-Down Report"
        subtitle = "Confidential · Internal Use · Not Legal Advice · Findings require review by qualified coverage counsel"

    nav_items = "".join(
        f'<span class="nav-item nav-active">{escape(e.get("entry_id",""))} — {escape(e.get("heuristic_id",""))}</span>'
        for e in entries
    )

    cards = "\n".join(_render_entry(e, sanitize=sanitize) for e in entries)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="page-header">
  <h1>{escape(title)}</h1>
  <div class="subtitle">{escape(subtitle)}</div>
</div>

<div class="page-body">

  <div class="report-nav">
    <strong>Confirmed findings:</strong>
    {nav_items}
  </div>

{cards}

</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate expert drill-down HTML report")
    parser.add_argument(
        "--carrier",
        default=None,
        metavar="CARRIER",
        help="Filter to a single carrier (e.g. KFBM, KNIC). Omit for all carriers.",
    )
    parser.add_argument(
        "--sanitize",
        action="store_true",
        help=(
            "Commercial/sanitize mode: replace verbatim carrier policy text with "
            "paraphrased descriptions. Required for external distribution (BACKLOG-022). "
            "Uses paraphrased_evidence, paraphrased_context, and paraphrased_current_language fields."
        ),
    )
    args = parser.parse_args()

    if not DATA_FILE.exists():
        sys.exit(f"Data file not found: {DATA_FILE}")

    with open(DATA_FILE, encoding="utf-8") as fh:
        data = json.load(fh)

    entries: list[dict] = data.get("entries", [])

    carrier = args.carrier.upper() if args.carrier else None
    if carrier:
        entries = [e for e in entries if _entry_matches_carrier(e, carrier)]
        if not entries:
            sys.exit(f"No entries found for carrier '{carrier}'.")
        suffix = f"_{carrier}"
    else:
        suffix = ""

    sanitize_suffix = "_sanitized" if args.sanitize else ""
    out_name = f"drilldown{suffix}{sanitize_suffix}.html"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / out_name

    html = build_report(entries, carrier, sanitize=args.sanitize)
    out_path.write_text(html, encoding="utf-8")

    mode = "sanitized/commercial" if args.sanitize else "internal"
    print(f"[drilldown] {len(entries)} entries, {mode} mode -> {out_path}")


if __name__ == "__main__":
    main()
