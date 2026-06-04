"""Generate a self-contained HTML report from a Stage 002 pipeline run directory.

Usage (run from the stage root):
    python src/visualizer.py                          # uses output/ directory
    python src/visualizer.py --run-dir output/20260603_164634_caba8e20
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            records.append(json.loads(line))
    return records


def _read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def generate(run_dir: Path) -> Path:
    # Load all artifacts
    manifest   = _read_json(run_dir / "run_manifest.json") or {}
    sources    = _read_jsonl(run_dir / "sources.jsonl")
    parser_runs = _read_jsonl(run_dir / "parser_runs.jsonl")
    nodes      = _read_jsonl(run_dir / "nodes.jsonl")
    citations  = _read_jsonl(run_dir / "citations.jsonl")
    references = _read_jsonl(run_dir / "references.jsonl")
    edges      = _read_jsonl(run_dir / "edges.jsonl")
    evidence   = _read_jsonl(run_dir / "candidate_evidence.jsonl")
    warnings   = _read_jsonl(run_dir / "parse_warnings.jsonl")
    block_stats = _read_jsonl(run_dir / "block_stats.jsonl")

    bundles_raw = _read_json(run_dir / "retrieval_bundles.json") or []
    bundles = bundles_raw if isinstance(bundles_raw, list) else []
    eval_results = _read_json(run_dir / "evaluation_results.json") or {}

    data = {
        "manifest": manifest,
        "sources": sources,
        "parser_runs": parser_runs,
        "nodes": nodes,
        "citations": citations,
        "references": references,
        "edges": edges,
        "evidence": evidence,
        "warnings": warnings,
        "block_stats": block_stats,
        "bundles": bundles,
        "eval": eval_results,
    }

    html = _render(data)
    out_path = run_dir / "report.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"[visualizer] Written: {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

def _render(data: dict) -> str:
    manifest = data["manifest"]
    run_id = manifest.get("run_id", "unknown")
    created_at = manifest.get("created_at", "")
    pipeline = manifest.get("pipeline_version", "")

    data_json = json.dumps(data, ensure_ascii=False, indent=None)

    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stage 002 Report — {run_id[:8]}</title>
<style>
:root {{
  --ink: #e2e8f0; --muted: #7e9ab5; --line: #1e3148; --soft: #0d1a28;
  --panel: #0f1e2e; --page: #080f18; --head-bg: #0b1520;
  --blue: #60a5fa; --teal: #34d4c8; --red: #f87171; --amber: #fbbf24;
  --green: #4ade80; --violet: #c084fc; --orange: #fb923c;
  --s1: #3b0a0a; --s1t: #fca5a5;
  --s2: #3b2800; --s2t: #fcd34d;
  --s3: #1e0a4a; --s3t: #c4b5fd;
  --s4: #0a1e4a; --s4t: #93c5fd;
  --s5: #052e1a; --s5t: #6ee7b7;
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  font-size: 14px; line-height: 1.5; color: var(--ink);
}}
[data-theme="light"] {{
  --ink: #17202a; --muted: #5d6875; --line: #dde3ea; --soft: #f4f7fa;
  --panel: #fff; --page: #eef2f6; --head-bg: #fbfcfe;
  --blue: #1d5fa6; --teal: #0b7a70; --red: #b42318; --amber: #8a5200;
  --green: #2a7230; --violet: #6b4fa3; --orange: #b45309;
  --s1: #fee2e2; --s1t: #991b1b;
  --s2: #fef3c7; --s2t: #78350f;
  --s3: #ede9fe; --s3t: #4c1d95;
  --s4: #dbeafe; --s4t: #1e3a8a;
  --s5: #d1fae5; --s5t: #065f46;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--page); }}

/* ---- header ---- */
.hd {{ background: var(--head-bg); border-bottom: 1px solid var(--line);
       padding: 14px 24px; display: flex; align-items: baseline; gap: 20px; }}
.hd h1 {{ font-size: 16px; font-weight: 600; color: var(--ink); }}
.hd .meta {{ font-size: 12px; color: var(--muted); }}
.hd .meta span {{ margin-right: 16px; }}

/* ---- tabs ---- */
.tabs {{ background: var(--head-bg); border-bottom: 1px solid var(--line);
         padding: 0 24px; display: flex; gap: 0; }}
.tab {{ padding: 10px 18px; cursor: pointer; font-size: 13px; color: var(--muted);
        border-bottom: 2px solid transparent; user-select: none; }}
.tab:hover {{ color: var(--ink); }}
.tab.active {{ color: var(--blue); border-bottom-color: var(--blue); font-weight: 500; }}

/* ---- main ---- */
.main {{ padding: 24px; max-width: 1400px; }}
.panel {{ display: none; }}
.panel.active {{ display: block; }}

/* ---- summary grid ---- */
.stat-grid {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 24px; }}
.stat {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
         padding: 14px 20px; min-width: 130px; }}
.stat .n {{ font-size: 28px; font-weight: 700; color: var(--blue); line-height: 1; }}
.stat .l {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}

/* ---- source cards (summary) ---- */
.source-cards {{ display: flex; flex-direction: column; gap: 10px; }}
.src-card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
             padding: 14px 18px; }}
.src-card .src-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 6px; }}
.src-card .src-id {{ font-weight: 600; font-size: 13px; }}
.src-card .src-counts {{ font-size: 12px; color: var(--muted); display: flex; gap: 14px; margin-top: 4px; }}
.src-card .src-counts span {{ white-space: nowrap; }}
.warn-row {{ font-size: 12px; color: var(--amber); margin-top: 6px; }}

/* ---- document outline ---- */
.outline-table {{ width: 100%; border-collapse: collapse; background: var(--panel);
                  border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
.outline-table th {{ background: #f0f4f8; text-align: left; padding: 8px 12px;
                     font-size: 12px; font-weight: 600; color: var(--muted);
                     border-bottom: 1px solid var(--line); position: sticky; top: 0; }}
.outline-table td {{ padding: 7px 12px; border-bottom: 1px solid var(--line);
                     font-size: 13px; vertical-align: top; }}
.outline-table tr:last-child td {{ border-bottom: none; }}
.outline-table tr.src-row td {{ background: #f7f9fc; font-weight: 600; font-size: 12px;
                                 color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }}
.outline-table tr.node-row:hover td {{ background: #f0f5fb; cursor: pointer; }}
.indent {{ display: inline-block; }}
.node-path {{ color: var(--muted); font-size: 11px; margin-top: 2px; }}
.expandable {{ cursor: pointer; }}
.detail-row td {{ background: #f9fbfd; padding: 10px 16px 14px 40px; }}
.detail-row .node-text {{ font-size: 12px; color: #334; white-space: pre-wrap;
                           max-height: 200px; overflow-y: auto; background: var(--soft);
                           border: 1px solid var(--line); border-radius: 4px;
                           padding: 8px 10px; margin-top: 6px; font-family: monospace; }}
.detail-row .ev-list {{ margin-top: 8px; display: flex; flex-direction: column; gap: 6px; }}

/* ---- evidence ledger ---- */
.ledger-controls {{ display: flex; gap: 10px; margin-bottom: 14px; flex-wrap: wrap; }}
.filter-btn {{ padding: 5px 12px; border: 1px solid var(--line); border-radius: 20px;
               background: var(--panel); cursor: pointer; font-size: 12px; color: var(--muted); }}
.filter-btn.active {{ border-color: var(--blue); background: #e8f0fb; color: var(--blue); font-weight: 500; }}
.ledger-table {{ width: 100%; border-collapse: collapse; background: var(--panel);
                 border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
.ledger-table th {{ background: #f0f4f8; text-align: left; padding: 8px 12px;
                    font-size: 12px; font-weight: 600; color: var(--muted);
                    border-bottom: 1px solid var(--line); position: sticky; top: 0; }}
.ledger-table td {{ padding: 9px 12px; border-bottom: 1px solid var(--line);
                    font-size: 12px; vertical-align: top; }}
.ledger-table tr:last-child td {{ border-bottom: none; }}
.ledger-table tr:hover td {{ background: #f6f9fd; }}
.ev-snippet {{ font-family: monospace; font-size: 11px; color: #334; background: var(--soft);
               border-left: 3px solid var(--line); padding: 4px 8px; margin-top: 4px;
               white-space: pre-wrap; line-height: 1.4; }}
.reviewer-q {{ font-size: 11px; color: var(--muted); margin-top: 4px; font-style: italic; }}

/* ---- citation map ---- */
.cite-source {{ margin-bottom: 20px; }}
.cite-source h3 {{ font-size: 13px; font-weight: 600; margin-bottom: 8px; color: #1a2a3a; }}
.cite-table {{ width: 100%; border-collapse: collapse; background: var(--panel);
               border: 1px solid var(--line); border-radius: 8px; overflow: hidden; margin-bottom: 6px; }}
.cite-table th {{ background: #f0f4f8; text-align: left; padding: 7px 12px;
                  font-size: 11px; font-weight: 600; color: var(--muted);
                  border-bottom: 1px solid var(--line); }}
.cite-table td {{ padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 12px; }}
.cite-table tr:last-child td {{ border-bottom: none; }}

/* ---- warnings ---- */
.warn-table {{ width: 100%; border-collapse: collapse; background: var(--panel);
               border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
.warn-table th {{ background: #fffbeb; text-align: left; padding: 8px 12px;
                  font-size: 12px; font-weight: 600; color: #78350f;
                  border-bottom: 1px solid #fde68a; }}
.warn-table td {{ padding: 8px 12px; border-bottom: 1px solid var(--line); font-size: 12px; }}
.warn-table tr:last-child td {{ border-bottom: none; }}

/* ---- badges ---- */
.badge {{ display: inline-block; padding: 2px 7px; border-radius: 10px;
          font-size: 11px; font-weight: 500; white-space: nowrap; }}
.b-s1 {{ background: var(--s1); color: var(--s1t); }}
.b-s2 {{ background: var(--s2); color: var(--s2t); }}
.b-s3 {{ background: var(--s3); color: var(--s3t); }}
.b-s4 {{ background: var(--s4); color: var(--s4t); }}
.b-s5 {{ background: var(--s5); color: var(--s5t); }}
.b-krs {{ background: #e0f2fe; color: #075985; }}
.b-kar {{ background: #f0fdf4; color: #14532d; }}
.b-doi {{ background: #fdf4ff; color: #701a75; }}
.b-type {{ background: #f1f5f9; color: #475569; }}
.b-conf-high {{ background: #dcfce7; color: #166534; }}
.b-conf-med  {{ background: #fef9c3; color: #854d0e; }}
.b-conf-low  {{ background: #fee2e2; color: #991b1b; }}
.b-warn {{ background: #fffbeb; color: #92400e; }}
.b-ok {{ background: #f0fdf4; color: #166534; }}

/* ---- misc ---- */
.empty {{ color: var(--muted); font-style: italic; font-size: 13px; padding: 16px 0; }}
.section-title {{ font-size: 15px; font-weight: 600; margin-bottom: 14px; color: var(--ink); }}
.theme-toggle {{ margin-left: auto; padding: 5px 12px; border: 1px solid var(--line);
                 border-radius: 6px; background: transparent; color: var(--muted);
                 cursor: pointer; font-size: 12px; }}
.theme-toggle:hover {{ color: var(--ink); border-color: var(--muted); }}
</style>
</head>
<body>

<div class="hd">
  <h1>Stage 002 — Discovery &amp; Instrumentation</h1>
  <div class="meta">
    <span>Run <code>{run_id[:8]}</code></span>
    <span>{created_at[:19].replace("T", " ")} UTC</span>
    <span>Pipeline {pipeline}</span>
  </div>
  <button class="theme-toggle" id="theme-toggle">Light mode</button>
</div>

<div class="tabs">
  <div class="tab active" data-tab="summary">Summary</div>
  <div class="tab" data-tab="outline">Document Outline</div>
  <div class="tab" data-tab="ledger">Evidence Ledger</div>
  <div class="tab" data-tab="citations">Citations</div>
  <div class="tab" data-tab="warnings">Warnings</div>
  <div class="tab" data-tab="bundles">Retrieval Bundles</div>
  <div class="tab" data-tab="evaluation">Evaluation</div>
</div>

<div class="main">

  <div class="panel active" id="tab-summary"></div>
  <div class="panel" id="tab-outline"></div>
  <div class="panel" id="tab-ledger"></div>
  <div class="panel" id="tab-citations"></div>
  <div class="panel" id="tab-warnings"></div>
  <div class="panel" id="tab-bundles"></div>
  <div class="panel" id="tab-evaluation"></div>

</div>

<script>
const DATA = {data_json};

const SMELL_NAMES = {{
  1: "Overbroad Exclusions",
  2: "Magic Valuation Terms",
  3: "Coverage Inversion",
  4: "Calculation Rule Drift",
  5: "Regulatory Mapping",
}};

const SMELL_CLASS = {{ 1:"b-s1", 2:"b-s2", 3:"b-s3", 4:"b-s4", 5:"b-s5" }};

function badge(cls, text) {{
  return `<span class="badge ${{cls}}">${{text}}</span>`;
}}

function smellBadge(sid) {{
  return badge(SMELL_CLASS[sid] || "b-type", `Smell ${{sid}}: ${{SMELL_NAMES[sid] || ""}}`);
}}

function confBadge(c) {{
  if (c === "high") return badge("b-conf-high", "high");
  if (c === "medium") return badge("b-conf-med", "medium");
  return badge("b-conf-low", "low");
}}

function citeBadge(t) {{
  if (t === "krs_statute") return badge("b-krs", "KRS");
  if (t === "kar_regulation") return badge("b-kar", "KAR");
  return badge("b-doi", t);
}}

// ---- Tab switching ----
document.querySelectorAll(".tab").forEach(tab => {{
  tab.addEventListener("click", () => {{
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.querySelectorAll(".panel").forEach(p => p.classList.remove("active"));
    tab.classList.add("active");
    document.getElementById("tab-" + tab.dataset.tab).classList.add("active");
  }});
}});

// ---- Summary ----
function renderSummary() {{
  const m = DATA.manifest;
  const ev = DATA.evidence;
  const bySmell = {{}};
  ev.forEach(e => {{ bySmell[e.smell_id] = (bySmell[e.smell_id] || 0) + 1; }});

  const warns = DATA.warnings;
  const prBySource = {{}};
  DATA.parser_runs.forEach(p => prBySource[p.source_id] = p);
  const bsBySource = {{}};
  DATA.block_stats.forEach(b => bsBySource[b.source_id] = b);
  const nodesBySource = {{}};
  DATA.nodes.forEach(n => {{ nodesBySource[n.source_id] = (nodesBySource[n.source_id] || 0) + 1; }});
  const evBySource = {{}};
  ev.forEach(e => {{ evBySource[e.source_id] = (evBySource[e.source_id] || 0) + 1; }});
  const citesBySource = {{}};
  DATA.citations.forEach(c => {{ citesBySource[c.source_id] = (citesBySource[c.source_id] || 0) + 1; }});
  const warnsBySource = {{}};
  warns.forEach(w => {{ warnsBySource[w.source_id] = (warnsBySource[w.source_id] || 0) + 1; }});

  let html = `<div class="stat-grid">
    ${{stat(DATA.nodes.length, "Nodes")}}
    ${{stat(DATA.citations.length, "Citations")}}
    ${{stat(DATA.references.length, "References")}}
    ${{stat(DATA.edges.length, "Edges")}}
    ${{stat(ev.length, "Candidate Evidence")}}
    ${{stat(DATA.block_stats.reduce((a,b) => a + b.total_blocks, 0), "Blocks")}}
    ${{stat(warns.length, "Parse Warnings")}}
  </div>`;

  // Smell breakdown
  html += `<div class="section-title">Candidate Evidence by Smell</div>`;
  html += `<div class="stat-grid">`;
  for (let i = 1; i <= 5; i++) {{
    const n = bySmell[i] || 0;
    html += `<div class="stat"><div class="n" style="font-size:22px">${{n}}</div>
      <div class="l">${{badge(SMELL_CLASS[i], `Smell ${{i}}`)}} ${{SMELL_NAMES[i]}}</div></div>`;
  }}
  html += `</div>`;

  // Source cards
  html += `<div class="section-title" style="margin-top:20px">Sources</div>`;
  html += `<div class="source-cards">`;
  DATA.sources.forEach(s => {{
    const pr = prBySource[s.source_id] || {{}};
    const bs = bsBySource[s.source_id] || {{}};
    const evCount = evBySource[s.source_id] || 0;
    const cCount = citesBySource[s.source_id] || 0;
    const wCount = warnsBySource[s.source_id] || 0;
    const extBadge = s.extension_matches_type ? badge("b-ok","ext ok") : badge("b-warn","ext mismatch");
    const stBadge = badge("b-type", s.source_type);
    const confBadgeHtml = confBadge(pr.status === "success" ? "high" : pr.status === "partial" ? "medium" : "low");
    html += `<div class="src-card">
      <div class="src-header">
        <span class="src-id">${{s.source_id}}</span>
        ${{stBadge}} ${{extBadge}} ${{confBadgeHtml}}
        ${{evCount > 0 ? `<span style="margin-left:4px">${{badge("b-s" + (Object.keys(bySmell).find(k => evBySource[s.source_id] > 0) || 1), evCount + " evidence")}}</span>` : ""}}
      </div>
      <div class="src-counts">
        <span>📄 ${{bs.total_blocks || 0}} blocks</span>
        <span>🧱 ${{nodesBySource[s.source_id] || 0}} nodes</span>
        <span>⚖️ ${{cCount}} citations</span>
        <span>🔍 ${{evCount}} evidence</span>
        <span>⏱ ${{pr.duration_seconds != null ? pr.duration_seconds.toFixed(1) + "s" : "—"}}</span>
      </div>
      ${{wCount > 0 ? `<div class="warn-row">⚠ ${{wCount}} parse warning(s)</div>` : ""}}
    </div>`;
  }});
  html += `</div>`;

  document.getElementById("tab-summary").innerHTML = html;
}}

function stat(n, label) {{
  return `<div class="stat"><div class="n">${{n}}</div><div class="l">${{label}}</div></div>`;
}}

// ---- Document Outline ----
function renderOutline() {{
  const evByNode = {{}};
  DATA.evidence.forEach(e => {{
    if (!evByNode[e.node_id]) evByNode[e.node_id] = [];
    evByNode[e.node_id].push(e);
  }});
  const citesByNode = {{}};
  DATA.citations.forEach(c => {{
    if (!citesByNode[c.node_id]) citesByNode[c.node_id] = [];
    citesByNode[c.node_id].push(c);
  }});

  // Group non-document nodes by source
  const srcOrder = DATA.sources.map(s => s.source_id);
  const nodesBySource = {{}};
  DATA.nodes.forEach(n => {{
    if (n.node_type === "document") return;
    if (!nodesBySource[n.source_id]) nodesBySource[n.source_id] = [];
    nodesBySource[n.source_id].push(n);
  }});

  let rows = `<table class="outline-table">
    <thead><tr>
      <th style="width:45%">Section</th>
      <th style="width:8%">Type</th>
      <th style="width:7%">Depth</th>
      <th style="width:10%">Citations</th>
      <th style="width:30%">Evidence</th>
    </tr></thead><tbody id="outline-body">`;

  srcOrder.forEach(sid => {{
    const snodes = nodesBySource[sid] || [];
    const src = DATA.sources.find(s => s.source_id === sid) || {{}};
    rows += `<tr class="src-row"><td colspan="5">${{sid}} — ${{src.source_type || ""}}</td></tr>`;

    snodes.forEach(n => {{
      const ev = evByNode[n.node_id] || [];
      const cites = citesByNode[n.node_id] || [];
      const indent = Math.max(0, (n.depth || 1) - 1) * 16;
      const evHtml = ev.map(e => smellBadge(e.smell_id)).join(" ");
      const citesHtml = cites.length > 0 ? `${{cites.length}} ${{badge("b-type","cite")}}` : `<span style="color:var(--muted)">—</span>`;
      const shortPath = (n.section_path || "").split(" > ").slice(-1)[0] || n.node_id;
      rows += `<tr class="node-row expandable" data-nid="${{n.node_id}}">
        <td><span class="indent" style="width:${{indent}}px;display:inline-block"></span>${{shortPath}}</td>
        <td>${{badge("b-type", n.node_type)}}</td>
        <td style="color:var(--muted);text-align:center">${{n.depth || "—"}}</td>
        <td>${{citesHtml}}</td>
        <td>${{evHtml || '<span style="color:var(--muted)">—</span>'}}</td>
      </tr>
      <tr class="detail-row" id="detail-${{n.node_id}}" style="display:none">
        <td colspan="5">
          <div style="font-size:11px;color:var(--muted);margin-bottom:4px">
            ${{n.section_path || ""}} &nbsp;·&nbsp; node_id: <code>${{n.node_id}}</code>
          </div>
          <div class="node-text">${{(n.text || "").substring(0, 800)}}${{(n.text||"").length > 800 ? "…" : ""}}</div>
          ${{ev.length > 0 ? `<div class="ev-list">${{ev.map(e => `
            <div>${{smellBadge(e.smell_id)}} ${{badge("b-type", e.heuristic_id)}} ${{confBadge(e.parser_confidence)}}
              <div class="ev-snippet">${{e.evidence_text}}</div>
              <div class="reviewer-q">🔎 ${{e.reviewer_question}}</div>
            </div>`).join("")}}</div>` : ""}}
        </td>
      </tr>`;
    }});
  }});

  rows += `</tbody></table>`;
  document.getElementById("tab-outline").innerHTML = rows;

  // Expand/collapse
  document.getElementById("outline-body").addEventListener("click", e => {{
    const row = e.target.closest("tr.node-row");
    if (!row) return;
    const nid = row.dataset.nid;
    const det = document.getElementById("detail-" + nid);
    if (det) det.style.display = det.style.display === "none" ? "table-row" : "none";
  }});
}}

// ---- Evidence Ledger ----
function renderLedger() {{
  let activeFilter = 0;

  function buildLedger(filter) {{
    const ev = filter === 0 ? DATA.evidence : DATA.evidence.filter(e => e.smell_id === filter);
    const nodeMap = {{}};
    DATA.nodes.forEach(n => nodeMap[n.node_id] = n);

    let html = `<div class="ledger-controls">
      <button class="filter-btn ${{filter===0?"active":""}}" data-f="0">All (${{DATA.evidence.length}})</button>`;
    for (let i = 1; i <= 5; i++) {{
      const n = DATA.evidence.filter(e => e.smell_id === i).length;
      html += `<button class="filter-btn ${{filter===i?"active":""}}" data-f="${{i}}">
        ${{badge(SMELL_CLASS[i], `S${{i}}`)}} ${{SMELL_NAMES[i]}} (${{n}})</button>`;
    }}
    html += `</div>`;

    if (ev.length === 0) {{
      html += `<div class="empty">No candidate evidence for this smell in this corpus slice.</div>`;
    }} else {{
      html += `<table class="ledger-table"><thead><tr>
        <th>Smell</th><th>Heuristic</th><th>Source</th><th>Section</th>
        <th>Confidence</th><th>Evidence &amp; Reviewer Question</th>
      </tr></thead><tbody>`;
      ev.forEach(e => {{
        const node = nodeMap[e.node_id] || {{}};
        const shortSection = (node.section_path || e.node_id).split(" > ").slice(-1)[0];
        html += `<tr>
          <td>${{smellBadge(e.smell_id)}}</td>
          <td>${{badge("b-type", e.heuristic_id)}}</td>
          <td style="font-size:11px;font-weight:500">${{e.source_id}}</td>
          <td style="font-size:11px;max-width:200px;word-break:break-word">${{shortSection}}</td>
          <td>${{confBadge(e.parser_confidence)}}</td>
          <td>
            <div class="ev-snippet">${{e.evidence_text}}</div>
            <div class="reviewer-q">🔎 ${{e.reviewer_question}}</div>
          </td>
        </tr>`;
      }});
      html += `</tbody></table>`;
    }}

    document.getElementById("tab-ledger").innerHTML = html;

    document.querySelectorAll(".filter-btn").forEach(btn => {{
      btn.addEventListener("click", () => buildLedger(parseInt(btn.dataset.f)));
    }});
  }}

  buildLedger(0);
}}

// ---- Citations ----
function renderCitations() {{
  const srcOrder = DATA.sources.map(s => s.source_id);
  const citesBySource = {{}};
  DATA.citations.forEach(c => {{
    if (!citesBySource[c.source_id]) citesBySource[c.source_id] = [];
    citesBySource[c.source_id].push(c);
  }});

  let html = "";
  srcOrder.forEach(sid => {{
    const cites = citesBySource[sid] || [];
    const src = DATA.sources.find(s => s.source_id === sid) || {{}};
    html += `<div class="cite-source">
      <h3>${{sid}} <span style="font-weight:400;color:var(--muted);font-size:12px">(${{src.source_type || ""}})</span></h3>`;
    if (cites.length === 0) {{
      html += `<div class="empty">No citations extracted.</div>`;
    }} else {{
      html += `<table class="cite-table"><thead><tr>
        <th>Type</th><th>Normalized</th><th>Raw Text</th><th>Resolved</th>
      </tr></thead><tbody>`;
      cites.forEach(c => {{
        const typeLabel = c.citation_type === "krs_statute" ? badge("b-krs","KRS") : badge("b-kar","KAR");
        html += `<tr>
          <td>${{typeLabel}}</td>
          <td style="font-family:monospace;font-size:11px">${{c.normalized || "—"}}</td>
          <td style="font-size:11px;color:var(--muted)">${{(c.raw_text||"").substring(0,80)}}</td>
          <td>${{c.resolved ? badge("b-ok","yes") : badge("b-warn","no")}}</td>
        </tr>`;
      }});
      html += `</tbody></table>`;
    }}
    html += `</div>`;
  }});

  document.getElementById("tab-citations").innerHTML = html;
}}

// ---- Warnings ----
function renderWarnings() {{
  const w = DATA.warnings;
  if (w.length === 0) {{
    document.getElementById("tab-warnings").innerHTML = `<div class="empty">No parse warnings in this run.</div>`;
    return;
  }}
  let html = `<table class="warn-table"><thead><tr>
    <th>Type</th><th>Source</th><th>Description</th>
  </tr></thead><tbody>`;
  w.forEach(wn => {{
    html += `<tr>
      <td>${{badge("b-warn", wn.warning_type)}}</td>
      <td style="font-weight:500">${{wn.source_id}}</td>
      <td>${{wn.description}}</td>
    </tr>`;
  }});
  html += `</tbody></table>`;
  document.getElementById("tab-warnings").innerHTML = html;
}}

// ---- Retrieval Bundles ----
function renderBundles() {{
  const bundles = DATA.bundles || [];
  if (bundles.length === 0) {{
    document.getElementById("tab-bundles").innerHTML =
      `<div class="empty">No retrieval bundles in this run directory. Run <code>python src/retrieval_runner.py</code> first.</div>`;
    return;
  }}

  // Group by smell_id extracted from why_retrieved
  const bySmell = {{}};
  bundles.forEach(b => {{
    const firstHit = (b.hits && b.hits[0]) || b;
    const why = firstHit.why_retrieved || b.why_retrieved || [];
    const filters = b.filters || {{}};
    const smellMatch = (why || []).join(" ").match(/smell_id=([0-9])/);
    const filterSmell = filters.smell_id ? parseInt(filters.smell_id) : 0;
    const sid = filterSmell || (smellMatch ? parseInt(smellMatch[1]) : 0);
    if (!bySmell[sid]) bySmell[sid] = [];
    bySmell[sid].push(b);
  }});

  const nodeMap = {{}};
  DATA.nodes.forEach(n => nodeMap[n.node_id] = n);

  let html = `<div class="section-title">${{bundles.length}} Retrieval Bundle(s)</div>`;

  const smellOrder = [1,2,3,4,5,0];
  smellOrder.forEach(sid => {{
    const items = bySmell[sid] || [];
    if (!items.length) return;
    const label = sid > 0 ? `Smell ${{sid}}: ${{SMELL_NAMES[sid]}}` : "Unassigned";
    const cls = sid > 0 ? SMELL_CLASS[sid] : "b-type";
    html += `<div style="margin-bottom:20px">
      <div class="section-title" style="font-size:13px;margin-bottom:10px">
        ${{badge(cls, label)}} — ${{items.length}} bundle(s)
      </div>`;

    items.forEach(b => {{
      const firstHit = (b.hits && b.hits[0]) || b;
      const source = firstHit.source || {{}};
      const diagnostics = firstHit.parser_diagnostics || {{}};
      const context = firstHit.expanded_context || {{}};
      const parent = context.parent_section || {{}};
      const citationIds = context.citations || b.citation_ids || [];
      const why = firstHit.why_retrieved || b.why_retrieved || [];
      const shortSection = (firstHit.section_path || b.section_path || "").split(" > ").slice(-1)[0] || firstHit.node_id || b.hit_node_id;
      const signalStr = Object.entries(firstHit.signal_scores || b.signal_scores || {{}})
        .map(([k,v]) => `${{k}}=${{v}}`).join(", ");
      html += `<div class="src-card" style="margin-bottom:8px">
        <div class="src-header">
          <span class="src-id" style="font-size:12px">${{source.source_id || b.source_id || ""}}</span>
          ${{badge("b-type", source.source_type || b.source_type || "?")}}
          ${{diagnostics.reading_order_confidence !== undefined ? badge("b-type", "parser " + diagnostics.reading_order_confidence) : confBadge(b.parser_confidence)}}
          ${{citationIds.length ? badge("b-krs", citationIds.length + " cite(s)") : ""}}
        </div>
        <div style="font-size:12px;color:var(--muted);margin:4px 0">${{shortSection}}</div>
        <div style="font-size:11px;color:var(--muted);margin-bottom:6px">
          Query: <code>${{b.query_text || b.query || ""}}</code> &nbsp;·&nbsp; signals: ${{signalStr}}
        </div>
        <div class="ev-snippet">${{(firstHit.text || b.hit_text || "").substring(0,300)}}</div>
        ${{why.length ? `<div style="margin-top:6px;font-size:11px;color:var(--muted)">
          Why: ${{why.map(w => `<span style="display:inline-block;margin-right:8px">• ${{w}}</span>`).join("")}}
        </div>` : ""}}
        ${{parent.text ? `<div style="margin-top:6px;font-size:11px;color:var(--muted)">Parent: <em>${{parent.text.substring(0,120)}}</em></div>` : ""}}
      </div>`;
    }});
    html += `</div>`;
  }});

  document.getElementById("tab-bundles").innerHTML = html;
}}

// ---- Theme toggle ----
document.getElementById("theme-toggle").addEventListener("click", () => {{
  const html = document.documentElement;
  const isDark = html.getAttribute("data-theme") !== "light";
  html.setAttribute("data-theme", isDark ? "light" : "dark");
  document.getElementById("theme-toggle").textContent = isDark ? "Dark mode" : "Light mode";
}});

// ---- Evaluation ----
function renderEvaluation() {{
  const ev = DATA.eval || {{}};
  if (!ev.item_results) {{
    document.getElementById("tab-evaluation").innerHTML =
      `<div class="empty">No evaluation results. Run <code>python src/evaluator.py</code> first.</div>`;
    return;
  }}

  const modeStats = ev.mode_stats || [];
  const items = ev.item_results || [];

  // Header stats
  let html = `<div class="stat-grid">`;
  modeStats.forEach(ms => {{
    html += `<div class="stat">
      <div class="n" style="font-size:22px">${{(ms.recall * 100).toFixed(0)}}%</div>
      <div class="l">${{ms.mode}} recall (${{ms.items_hit}}/${{ms.items_evaluated}})</div>
    </div>`;
  }});
  if (ev.semantic_decision) {{
    const dec = ev.semantic_decision;
    const decColor = dec.startsWith("DEFER") ? "var(--green)" : dec.startsWith("PURSUE") ? "var(--red)" : "var(--amber)";
    html += `<div class="stat" style="min-width:260px">
      <div class="n" style="font-size:13px;color:${{decColor}}">${{dec.split(" — ")[0]}}</div>
      <div class="l">Semantic retrieval decision</div>
    </div>`;
  }}
  html += `</div>`;

  // Rationale
  if (ev.semantic_rationale) {{
    html += `<div style="background:var(--panel);border:1px solid var(--line);border-radius:8px;
                         padding:14px 18px;margin-bottom:20px;font-size:13px;line-height:1.6">
      ${{ev.semantic_rationale}}
    </div>`;
  }}

  // Item table
  html += `<div class="section-title">Item Results</div>
    <table class="ledger-table"><thead><tr>
      <th>Item</th><th>Smell</th><th>Source</th><th>Phrase</th><th>BM25 Rank</th><th>Notes</th>
    </tr></thead><tbody>`;

  items.forEach(r => {{
    const hitIcon = r.any_hit ? badge("b-conf-high", "HIT") : badge("b-conf-low", "MISS");
    const phraseCell = r.missed_by_phrase ? badge("b-conf-low","miss") : badge("b-conf-high","hit");
    const bm25Cell = r.missed_by_bm25
      ? badge("b-conf-low","miss")
      : badge("b-conf-high", r.best_rank ? `rank ${{r.best_rank}}` : "hit");
    const notesHtml = (r.notes || []).map(n => `<div style="font-size:11px;color:var(--muted)">${{n}}</div>`).join("");
    html += `<tr>
      <td style="font-weight:500">${{r.item_id}} ${{hitIcon}}</td>
      <td>${{smellBadge(r.smell_id)}}</td>
      <td style="font-size:11px">${{r.source_id}}<br><span style="color:var(--muted)">${{r.tier}}</span></td>
      <td>${{phraseCell}}</td>
      <td>${{bm25Cell}}</td>
      <td style="font-size:11px">${{r.fixture_summary.substring(0,80)}}${{notesHtml}}</td>
    </tr>`;
  }});
  html += `</tbody></table>`;

  // Corpus gaps
  const gapCount = ev.corpus_gap_count || 0;
  if (gapCount > 0) {{
    html += `<div style="margin-top:20px;padding:12px 16px;background:var(--s2);border-radius:8px;
                          border:1px solid var(--line);font-size:13px">
      <strong style="color:var(--s2t)">${{gapCount}} corpus gap tier(s)</strong> — policy/manual clauses,
      endorsement fragments, and rate/manual fragments could not be evaluated.
      Add carrier form sources to unlock full evaluation coverage.
    </div>`;
  }}

  document.getElementById("tab-evaluation").innerHTML = html;
}}

// Boot
renderSummary();
renderOutline();
renderLedger();
renderCitations();
renderWarnings();
renderBundles();
renderEvaluation();
</script>
</body>
</html>
"""


def main() -> None:
    stage_root = Path(__file__).parent.parent

    parser = argparse.ArgumentParser(description="Stage 002 HTML report generator")
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=stage_root / "output",
        help="Path to a pipeline run output directory (default: output/)",
    )
    args = parser.parse_args()
    generate(args.run_dir)


if __name__ == "__main__":
    main()
