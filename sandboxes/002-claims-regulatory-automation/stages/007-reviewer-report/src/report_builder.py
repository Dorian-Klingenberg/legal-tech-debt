"""
Stage 007: Reviewer Report Builder

Assembles detector findings, candidate evidence, retrieval bundles, and corpus
gap information into a human-readable report for a legal reviewer.

Outputs (written under the sandbox-level Stage 007 output directory):
  - reviewer_report.html  — single-file dark-theme HTML
  - reviewer_report.md    — plain-text version for diff and version control

Usage:
    python src/report_builder.py --run-dir ../../output/002/<run_key>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

_STAGE_003_SRC = (
    Path(__file__).resolve().parent.parent.parent
    / "003-retrieval-baseline" / "src"
)
if str(_STAGE_003_SRC) not in sys.path:
    sys.path.insert(0, str(_STAGE_003_SRC))

from retrieval.index import RunIndex  # type: ignore
from paths import stage_output_dir  # type: ignore

SMELL_NAMES = {
    1: "Overbroad / Non-deterministic Exclusions",
    2: "Magic Number / Magic Valuation Terms",
    3: "Coverage Inversion / Contradictory Conditions",
    4: "Calculation Rule Drift / Unversioned Rate Reference",
    5: "Regulatory Mapping Smells",
}

SMELL_COLORS = {1: "s1", 2: "s2", 3: "s3", 4: "s4", 5: "s5"}

CORPUS_GAPS = [
    {
        "tier": "policy_form_coverage",
        "smells": [1, 2, 3, 5],
        "description": "Carrier form evidence is present through SERFF filings, but full unredacted base HO-3 coverage is still partial.",
        "impact": "Policy-language detectors can run, but reviewer confidence still depends on checking whether the parsed forms represent the full operative form set.",
    },
    {
        "tier": "manual_serff_sources",
        "smells": [4, 5],
        "description": "Several manual SERFF sources remain known gaps; they are not blockers unless an active experiment needs their exact pages.",
        "impact": "Calculation-drift and regulatory-mapping review should treat missing manual attachments as coverage limits, not as negative evidence.",
    },
    {
        "tier": "detector_and_source_coverage",
        "smells": [2, 3, 5],
        "description": "All five detector families are implemented. The current run has no Smell 3 findings after regulatory-layer false positives were removed; H007 and Smell 2 H004 also have no findings because their required package/base-form inputs are absent.",
        "impact": "Zero findings for a heuristic are scoped to the current sources and detector preconditions. They are not proof that the issue class is absent from the market.",
    },
]


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def build(run_dir: Path) -> None:
    print(f"[report-builder] Loading data from {run_dir}...")
    idx = RunIndex(run_dir)
    s006_dir = stage_output_dir("006", run_dir)
    findings = _read_jsonl(s006_dir / "detector_findings.jsonl")
    evidence = _read_jsonl(run_dir / "candidate_evidence.jsonl")

    if not findings:
        print("[report-builder] WARNING: no detector_findings.jsonl found. Run Stage 006 first.")

    by_smell: dict[int, list[dict]] = defaultdict(list)
    for f in findings:
        by_smell[f["smell_id"]].append(f)

    ev_by_smell: dict[int, list[dict]] = defaultdict(list)
    for e in evidence:
        ev_by_smell[e["smell_id"]].append(e)

    print(f"[report-builder] {len(findings)} findings, {len(evidence)} candidate evidence items")

    _write_md(run_dir, idx, findings, by_smell, ev_by_smell)
    _write_html(run_dir, idx, findings, by_smell, ev_by_smell)


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def _write_md(run_dir: Path, idx: RunIndex, findings: list[dict],
              by_smell: dict, ev_by_smell: dict) -> None:
    conf_counts = defaultdict(int)
    for f in findings:
        conf_counts[f["confidence"]] += 1

    lines = [
        "# Reviewer Report — Sandbox 002 Kentucky Homeowners",
        "",
        f"Run: `{idx.run_id}`  ",
        f"Generated: {datetime.now(timezone.utc).isoformat()}  ",
        f"Sources: {len(idx.sources)}  |  Content nodes: {len(idx.content_nodes)}  |  Findings: {len(findings)}",
        "",
        "> **Note:** This report surfaces patterns for reviewer judgment. "
        "It does not claim any policy is unlawful. All findings require human review.",
        "",
        "## Finding Summary",
        "",
        f"| Confidence | Count |",
        f"|---|---|",
        f"| HIGH | {conf_counts['HIGH']} |",
        f"| MEDIUM | {conf_counts['MEDIUM']} |",
        f"| LOW | {conf_counts['LOW']} |",
        f"| **Total** | **{len(findings)}** |",
        "",
        "| Smell | Name | Findings |",
        "|---|---|---|",
    ]
    for sid in sorted(SMELL_NAMES):
        lines.append(f"| {sid} | {SMELL_NAMES[sid]} | {len(by_smell.get(sid, []))} |")

    lines += ["", "## Corpus Coverage", ""]
    for src in idx.sources:
        node_count = sum(1 for n in idx.content_nodes if n.get("source_id") == src["source_id"])
        lines.append(f"- **{src['source_id']}** ({src.get('source_type', '?')}) — {node_count} nodes")

    lines += ["", "## Corpus Gaps", ""]
    for gap in CORPUS_GAPS:
        smells_str = ", ".join(f"Smell {s}" for s in gap["smells"])
        lines += [
            f"### {gap['tier']}",
            f"Affects: {smells_str}  ",
            f"{gap['description']}  ",
            f"Impact: {gap['impact']}",
            "",
        ]

    lines += ["## Findings By Smell", ""]
    for sid in sorted(SMELL_NAMES):
        fs = by_smell.get(sid, [])
        lines += [f"### Smell {sid}: {SMELL_NAMES[sid]}", ""]
        if not fs:
            ev_count = len(ev_by_smell.get(sid, []))
            lines += [
                f"No detector findings.  ",
                f"Candidate evidence items from Stage 002: {ev_count}  ",
                "This may reflect a corpus gap rather than absence of the smell.",
                "",
            ]
            continue
        for f in sorted(fs, key=lambda x: ("HIGH", "MEDIUM", "LOW").index(x["confidence"])):
            node = idx.node_by_id.get(f["node_id"], {})
            lines += [
                f"#### [{f['confidence']}] `{f['heuristic_id']}` — {f['source_id']}",
                "",
                f"**Node:** `{f['node_id']}`  ",
                f"**Section:** {f.get('section_path') or node.get('section_path') or '—'}",
                "",
                f"**Evidence:**",
                f"> {f['evidence_text'].replace(chr(10), ' ')}",
                "",
                f"**Rationale:** {f['rationale']}",
                "",
                f"**Reviewer question:** {f['reviewer_question']}",
                "",
                f"**False positive risk:** {f['false_positive_risk']}",
                "",
                "---",
                "",
            ]

    out = stage_output_dir("007", run_dir) / "reviewer_report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"[report-builder] Written -> {out}")


# ---------------------------------------------------------------------------
# HTML report
# ---------------------------------------------------------------------------

def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def _confidence_badge(conf: str) -> str:
    color = {"HIGH": "var(--red)", "MEDIUM": "var(--amber)", "LOW": "var(--muted)"}.get(conf, "var(--muted)")
    return f'<span style="color:{color};font-weight:600;font-size:11px">{conf}</span>'


def _write_html(run_dir: Path, idx: RunIndex, findings: list[dict],
                by_smell: dict, ev_by_smell: dict) -> None:
    conf_counts = defaultdict(int)
    for f in findings:
        conf_counts[f["confidence"]] += 1

    run_id = idx.run_id
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # --- Summary tab ---
    summary_stats = f"""
<div class="stat-grid">
  <div class="stat"><div class="n">{len(idx.sources)}</div><div class="l">Sources</div></div>
  <div class="stat"><div class="n">{len(idx.content_nodes)}</div><div class="l">Content nodes</div></div>
  <div class="stat"><div class="n" style="color:var(--red)">{conf_counts['HIGH']}</div><div class="l">HIGH findings</div></div>
  <div class="stat"><div class="n" style="color:var(--amber)">{conf_counts['MEDIUM']}</div><div class="l">MEDIUM findings</div></div>
  <div class="stat"><div class="n" style="color:var(--muted)">{conf_counts['LOW']}</div><div class="l">LOW findings</div></div>
  <div class="stat"><div class="n">{len(findings)}</div><div class="l">Total findings</div></div>
</div>
<p style="color:var(--muted);font-size:12px;margin-bottom:20px">
  This report surfaces patterns for reviewer judgment. It does not claim any policy is unlawful.
  All findings require human review.
</p>
<h3 style="margin-bottom:12px;font-size:14px">By Smell</h3>
<table class="outline-table" style="margin-bottom:24px">
<thead><tr><th>Smell</th><th>Name</th><th>Findings</th><th>HIGH</th><th>MEDIUM</th><th>LOW</th></tr></thead>
<tbody>"""
    for sid in sorted(SMELL_NAMES):
        fs = by_smell.get(sid, [])
        h = sum(1 for f in fs if f["confidence"] == "HIGH")
        m = sum(1 for f in fs if f["confidence"] == "MEDIUM")
        lo = sum(1 for f in fs if f["confidence"] == "LOW")
        sc = SMELL_COLORS[sid]
        summary_stats += f'<tr><td><span class="badge {sc}">{sid}</span></td><td>{_esc(SMELL_NAMES[sid])}</td>'
        summary_stats += f'<td><b>{len(fs)}</b></td>'
        summary_stats += f'<td style="color:var(--red)">{h}</td><td style="color:var(--amber)">{m}</td><td style="color:var(--muted)">{lo}</td></tr>'
    summary_stats += "</tbody></table>"

    summary_stats += '<h3 style="margin-bottom:12px;font-size:14px">Corpus Coverage</h3><div class="source-cards">'
    for src in idx.sources:
        node_count = sum(1 for n in idx.content_nodes if n.get("source_id") == src["source_id"])
        src_id = _esc(src["source_id"])
        src_type = _esc(src.get("source_type", ""))
        summary_stats += f'<div class="src-card"><div class="src-header"><span class="src-id">{src_id}</span><span style="color:var(--muted);font-size:11px">{src_type}</span></div>'
        summary_stats += f'<div class="src-counts"><span>{node_count} nodes</span></div></div>'
    summary_stats += "</div>"

    # --- Gaps tab ---
    gaps_html = '<h3 style="margin-bottom:16px;font-size:14px">Known Corpus Gaps</h3>'
    for gap in CORPUS_GAPS:
        smells_str = " ".join(f'<span class="badge {SMELL_COLORS[s]}">{s}</span>' for s in gap["smells"])
        gaps_html += f"""<div class="src-card" style="margin-bottom:12px">
  <div class="src-header"><span class="src-id">{_esc(gap['tier'])}</span>{smells_str}</div>
  <div style="font-size:12px;margin-top:6px;color:var(--ink)">{_esc(gap['description'])}</div>
  <div style="font-size:12px;margin-top:4px;color:var(--amber)">Impact: {_esc(gap['impact'])}</div>
</div>"""

    # --- Findings tab ---
    findings_html = ""
    for sid in sorted(SMELL_NAMES):
        fs = by_smell.get(sid, [])
        sc = SMELL_COLORS[sid]
        findings_html += f'<div class="smell-section" style="margin-bottom:32px">'
        findings_html += f'<h3 style="font-size:14px;margin-bottom:12px"><span class="badge {sc}">{sid}</span> {_esc(SMELL_NAMES[sid])}</h3>'

        if not fs:
            ev_count = len(ev_by_smell.get(sid, []))
            findings_html += f'<p style="color:var(--muted);font-size:12px">No detector findings. {ev_count} candidate evidence item(s) from Stage 002. May reflect a corpus gap.</p>'
        else:
            for f in sorted(fs, key=lambda x: ("HIGH", "MEDIUM", "LOW").index(x["confidence"])):
                node = idx.node_by_id.get(f["node_id"], {})
                section = _esc(f.get("section_path") or node.get("section_path") or "—")
                evtext = _esc(f["evidence_text"].replace("\n", " "))
                findings_html += f"""<div class="src-card" style="margin-bottom:10px">
  <div class="src-header">
    {_confidence_badge(f['confidence'])}
    <span style="font-size:12px;color:var(--blue);font-family:monospace">{_esc(f['heuristic_id'])}</span>
    <span style="font-size:12px;color:var(--muted)">{_esc(f['source_id'])}</span>
    <span style="font-size:11px;color:var(--muted);margin-left:auto">{_esc(f['finding_id'])}</span>
  </div>
  <div style="font-size:11px;color:var(--muted);margin-bottom:6px">Node: <code>{_esc(f['node_id'])}</code> &nbsp; Section: {section}</div>
  <div class="ev-snippet">{evtext}</div>
  <div style="margin-top:10px;display:grid;gap:6px">
    <div style="font-size:12px"><b style="color:var(--muted)">Rationale:</b> {_esc(f['rationale'])}</div>
    <div style="font-size:12px"><b style="color:var(--teal)">Reviewer question:</b> {_esc(f['reviewer_question'])}</div>
    <div style="font-size:12px"><b style="color:var(--muted)">False positive risk:</b> {_esc(f['false_positive_risk'])}</div>
  </div>
</div>"""
        findings_html += "</div>"

    html = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reviewer Report — {_esc(run_id[:8])}</title>
<style>
:root {{
  --ink: #e2e8f0; --muted: #7e9ab5; --line: #1e3148; --soft: #0d1a28;
  --panel: #0f1e2e; --page: #080f18; --head-bg: #0b1520;
  --blue: #60a5fa; --teal: #34d4c8; --red: #f87171; --amber: #fbbf24;
  --green: #4ade80; --violet: #c084fc; --orange: #fb923c;
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  font-size: 14px; line-height: 1.5; color: var(--ink);
}}
[data-theme="light"] {{
  --ink: #17202a; --muted: #5d6875; --line: #dde3ea; --soft: #f4f7fa;
  --panel: #fff; --page: #eef2f6; --head-bg: #fbfcfe;
  --blue: #1d5fa6; --teal: #0b7a70; --red: #b42318; --amber: #8a5200;
  --green: #2a7230; --violet: #6b4fa3; --orange: #b45309;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--page); }}
.hd {{ background: var(--head-bg); border-bottom: 1px solid var(--line);
       padding: 14px 24px; display: flex; align-items: baseline; gap: 20px; }}
.hd h1 {{ font-size: 16px; font-weight: 600; color: var(--ink); }}
.hd .meta {{ font-size: 12px; color: var(--muted); }}
.hd .meta span {{ margin-right: 16px; }}
.theme-btn {{ margin-left: auto; padding: 4px 12px; border: 1px solid var(--line);
              border-radius: 4px; background: transparent; color: var(--muted);
              cursor: pointer; font-size: 12px; }}
.tabs {{ background: var(--head-bg); border-bottom: 1px solid var(--line);
         padding: 0 24px; display: flex; gap: 0; }}
.tab {{ padding: 10px 18px; cursor: pointer; font-size: 13px; color: var(--muted);
        border-bottom: 2px solid transparent; user-select: none; }}
.tab:hover {{ color: var(--ink); }}
.tab.active {{ color: var(--blue); border-bottom-color: var(--blue); font-weight: 500; }}
.main {{ padding: 24px; max-width: 1200px; }}
.panel {{ display: none; }}
.panel.active {{ display: block; }}
.stat-grid {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 24px; }}
.stat {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
         padding: 14px 20px; min-width: 130px; }}
.stat .n {{ font-size: 28px; font-weight: 700; color: var(--blue); line-height: 1; }}
.stat .l {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}
.src-card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
             padding: 14px 18px; }}
.src-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 4px; flex-wrap: wrap; }}
.src-id {{ font-weight: 600; font-size: 13px; }}
.src-counts {{ font-size: 12px; color: var(--muted); display: flex; gap: 14px; margin-top: 4px; }}
.source-cards {{ display: flex; flex-direction: column; gap: 10px; }}
.outline-table {{ width: 100%; border-collapse: collapse; background: var(--panel);
                  border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
.outline-table th {{ background: var(--soft); text-align: left; padding: 8px 12px;
                     font-size: 12px; font-weight: 600; color: var(--muted);
                     border-bottom: 1px solid var(--line); }}
.outline-table td {{ padding: 7px 12px; border-bottom: 1px solid var(--line);
                     font-size: 13px; vertical-align: top; }}
.outline-table tr:last-child td {{ border-bottom: none; }}
.ev-snippet {{ font-family: monospace; font-size: 11px; color: var(--ink);
               background: var(--soft); border-left: 3px solid var(--line);
               padding: 6px 10px; margin-top: 4px; white-space: pre-wrap; line-height: 1.4; }}
.badge {{ display: inline-block; padding: 2px 8px; border-radius: 4px;
          font-size: 11px; font-weight: 600; }}
.s1 {{ background: #3b0a0a; color: #fca5a5; }}
.s2 {{ background: #3b2800; color: #fcd34d; }}
.s3 {{ background: #1e0a4a; color: #c4b5fd; }}
.s4 {{ background: #0a1e4a; color: #93c5fd; }}
.s5 {{ background: #052e1a; color: #6ee7b7; }}
code {{ font-family: monospace; font-size: 11px; background: var(--soft);
        padding: 1px 5px; border-radius: 3px; color: var(--blue); }}
</style>
</head>
<body>
<div class="hd">
  <h1>Reviewer Report</h1>
  <div class="meta">
    <span>Run <b>{_esc(run_id[:8])}</b></span>
    <span>{_esc(generated)}</span>
    <span>{len(findings)} findings</span>
  </div>
  <button class="theme-btn" onclick="document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'light':'dark'">Toggle theme</button>
</div>
<div class="tabs">
  <div class="tab active" onclick="show('summary',this)">Summary</div>
  <div class="tab" onclick="show('findings',this)">Findings</div>
  <div class="tab" onclick="show('gaps',this)">Corpus Gaps</div>
</div>
<div class="main">
  <div id="summary" class="panel active">{summary_stats}</div>
  <div id="findings" class="panel">{findings_html}</div>
  <div id="gaps" class="panel">{gaps_html}</div>
</div>
<script>
function show(id, el) {{
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  el.classList.add('active');
}}
</script>
</body>
</html>"""

    out = stage_output_dir("007", run_dir) / "reviewer_report.html"
    out.write_text(html, encoding="utf-8")
    print(f"[report-builder] Written -> {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build reviewer report from Stage 006 findings")
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()
    build(args.run_dir)
