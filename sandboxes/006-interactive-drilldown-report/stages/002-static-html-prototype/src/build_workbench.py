from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SANDBOX = ROOT / "sandboxes" / "006-interactive-drilldown-report"
INPUT = ROOT / "sandboxes" / "004-expert-drilldown" / "data" / "drill_down_entries.json"
OUTPUT = SANDBOX / "output" / "workbench.html"


def build() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    payload = {
        "schema_version": data.get("schema_version"),
        "created_at": data.get("created_at"),
        "source_path": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
        "entries": entries,
    }
    encoded = html.escape(json.dumps(payload, ensure_ascii=False), quote=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(encoded), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(entries)} entries")


def render(encoded_payload: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Interactive Drill-Down Workbench</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f8;
      --panel: #ffffff;
      --ink: #1d252d;
      --muted: #5f6c79;
      --line: #d9dee4;
      --accent: #0f766e;
      --accent-2: #8b5cf6;
      --warn: #b45309;
      --danger: #b91c1c;
      --good: #166534;
      --shadow: 0 1px 2px rgba(20, 30, 40, 0.08);
      font-family: "Segoe UI", Arial, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-size: 15px;
      line-height: 1.45;
    }}
    button, input, select {{
      font: inherit;
    }}
    .app {{
      min-height: 100vh;
      display: grid;
      grid-template-rows: auto auto 1fr;
    }}
    header {{
      background: #17202a;
      color: #fff;
      padding: 18px 24px;
      display: flex;
      gap: 18px;
      justify-content: space-between;
      align-items: center;
    }}
    header h1 {{
      margin: 0;
      font-size: 21px;
      font-weight: 650;
      letter-spacing: 0;
    }}
    header p {{
      margin: 4px 0 0;
      color: #cbd5df;
      max-width: 900px;
      font-size: 13px;
    }}
    .mode-toggle {{
      display: inline-grid;
      grid-template-columns: 1fr 1fr;
      background: rgba(255,255,255,.1);
      border: 1px solid rgba(255,255,255,.22);
      border-radius: 6px;
      padding: 3px;
      min-width: 230px;
    }}
    .mode-toggle button {{
      border: 0;
      color: #d7dee7;
      background: transparent;
      border-radius: 4px;
      padding: 7px 12px;
      cursor: pointer;
    }}
    .mode-toggle button.active {{
      background: #fff;
      color: #17202a;
    }}
    .toolbar {{
      display: grid;
      grid-template-columns: minmax(240px, .72fr) minmax(420px, 1.28fr);
      gap: 14px;
      padding: 14px 16px;
      border-bottom: 1px solid var(--line);
      background: #eef2f5;
    }}
    .metrics, .filters, .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 6px;
      box-shadow: var(--shadow);
    }}
    .metrics {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1px;
      overflow: hidden;
    }}
    .metric {{
      padding: 12px;
      background: #fff;
      min-height: 70px;
    }}
    .metric span {{
      display: block;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    .metric strong {{
      display: block;
      margin-top: 4px;
      font-size: 22px;
    }}
    .filters {{
      padding: 12px;
      display: grid;
      grid-template-columns: repeat(5, minmax(110px, 1fr));
      gap: 10px;
      align-content: start;
    }}
    label {{
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    select, input {{
      width: 100%;
      color: var(--ink);
      background: #fff;
      border: 1px solid #c9d1da;
      border-radius: 5px;
      min-height: 34px;
      padding: 6px 8px;
      text-transform: none;
      letter-spacing: 0;
    }}
    .workspace {{
      display: grid;
      grid-template-columns: minmax(300px, 410px) minmax(0, 1fr);
      gap: 14px;
      padding: 14px 16px 18px;
      min-height: 0;
    }}
    .list {{
      overflow: auto;
      min-height: 0;
      padding: 8px;
    }}
    .finding-button {{
      width: 100%;
      border: 1px solid var(--line);
      background: #fff;
      text-align: left;
      border-radius: 6px;
      padding: 12px;
      margin: 0 0 8px;
      cursor: pointer;
      display: grid;
      gap: 8px;
    }}
    .finding-button.active {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(15, 118, 110, .14);
    }}
    .finding-title {{
      font-weight: 700;
      font-size: 14px;
    }}
    .meta-row, .badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      min-height: 22px;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: #f8fafc;
      color: #324251;
      font-size: 12px;
      font-weight: 650;
    }}
    .badge.high {{ color: var(--danger); border-color: #fecaca; background: #fff1f2; }}
    .badge.medium {{ color: var(--warn); border-color: #fed7aa; background: #fff7ed; }}
    .badge.good {{ color: var(--good); border-color: #bbf7d0; background: #f0fdf4; }}
    .badge.mode {{ color: #5b21b6; border-color: #ddd6fe; background: #f5f3ff; }}
    .detail {{
      min-width: 0;
      overflow: auto;
    }}
    .detail-inner {{
      padding: 18px;
      display: grid;
      gap: 14px;
    }}
    .detail h2 {{
      margin: 0;
      font-size: 23px;
      letter-spacing: 0;
    }}
    .detail h3 {{
      margin: 0 0 8px;
      font-size: 15px;
      letter-spacing: 0;
    }}
    .subtle {{
      color: var(--muted);
      font-size: 13px;
    }}
    .section {{
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      padding: 14px;
    }}
    .split {{
      display: grid;
      grid-template-columns: minmax(0, 1.05fr) minmax(240px, .95fr);
      gap: 12px;
    }}
    .tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 10px;
    }}
    .tabs button {{
      border: 1px solid var(--line);
      background: #f8fafc;
      border-radius: 5px;
      padding: 7px 9px;
      cursor: pointer;
      color: #334155;
    }}
    .tabs button.active {{
      border-color: var(--accent);
      color: #064e3b;
      background: #ecfdf5;
    }}
    .role-body {{
      display: grid;
      gap: 10px;
    }}
    .field {{
      display: grid;
      gap: 3px;
    }}
    .field span {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    .field p {{
      margin: 0;
    }}
    details {{
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px 12px;
      background: #fbfcfd;
    }}
    summary {{
      cursor: pointer;
      font-weight: 700;
    }}
    .trace-list {{
      margin: 10px 0 0;
      padding-left: 18px;
    }}
    .empty {{
      padding: 30px;
      color: var(--muted);
      text-align: center;
    }}
    @media (max-width: 980px) {{
      header, .toolbar, .workspace, .split {{
        grid-template-columns: 1fr;
      }}
      header {{
        align-items: stretch;
      }}
      .mode-toggle {{
        width: 100%;
      }}
      .filters {{
        grid-template-columns: repeat(2, minmax(140px, 1fr));
      }}
    }}
    @media (max-width: 620px) {{
      .metrics, .filters {{
        grid-template-columns: 1fr;
      }}
      .workspace {{
        padding: 10px;
      }}
    }}
  </style>
</head>
<body>
  <div class="app">
    <header>
      <div>
        <h1>Interactive Drill-Down Workbench</h1>
        <p>Local static prototype driven by Sandbox 004 drill-down entries. It explores review flow, source trace, role views, and internal versus sanitized presentation.</p>
      </div>
      <div class="mode-toggle" aria-label="Evidence mode">
        <button type="button" data-mode="internal" class="active">Internal</button>
        <button type="button" data-mode="sanitized">Sanitized</button>
      </div>
    </header>

    <section class="toolbar" aria-label="Portfolio controls">
      <div class="metrics" id="metrics"></div>
      <div class="filters">
        <label>Carrier<select id="carrierFilter"></select></label>
        <label>Smell<select id="smellFilter"></select></label>
        <label>Severity<select id="severityFilter"></select></label>
        <label>Status<select id="statusFilter"></select></label>
        <label>Search<input id="searchInput" type="search" placeholder="finding, source, gap"></label>
      </div>
    </section>

    <main class="workspace">
      <section class="panel list" id="findingList" aria-label="Findings"></section>
      <section class="panel detail" id="findingDetail" aria-label="Finding detail"></section>
    </main>
  </div>

  <script id="workbench-data" type="application/json">{encoded_payload}</script>
  <script>
    const payload = JSON.parse(document.getElementById('workbench-data').textContent);
    const entries = payload.entries || [];
    const statuses = ['needs review', 'accepted', 'rejected', 'needs source', 'needs counsel'];
    const state = {{
      mode: 'internal',
      selected: entries[0]?.entry_id || null,
      role: 'executive',
      statuses: Object.fromEntries(entries.map(entry => [entry.entry_id, 'needs review']))
    }};

    const els = {{
      metrics: document.getElementById('metrics'),
      list: document.getElementById('findingList'),
      detail: document.getElementById('findingDetail'),
      carrier: document.getElementById('carrierFilter'),
      smell: document.getElementById('smellFilter'),
      severity: document.getElementById('severityFilter'),
      status: document.getElementById('statusFilter'),
      search: document.getElementById('searchInput')
    }};

    function asArray(value) {{
      if (Array.isArray(value)) return value;
      if (value === undefined || value === null || value === '') return [];
      return [value];
    }}

    function carriers(entry) {{
      return asArray(entry.carriers || entry.carrier);
    }}

    function title(entry) {{
      return entry.smell_name || entry.heuristic_id || entry.entry_id;
    }}

    function severityClass(value) {{
      const lower = String(value || '').toLowerCase();
      if (lower.includes('high')) return 'high';
      if (lower.includes('medium')) return 'medium';
      if (lower.includes('low')) return 'good';
      return '';
    }}

    function text(value) {{
      if (value === undefined || value === null || value === '') return 'Not stated.';
      if (Array.isArray(value)) return value.join(' ');
      if (typeof value === 'object') return JSON.stringify(value);
      return String(value);
    }}

    function escapeHtml(value) {{
      return text(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
    }}

    function optionList(select, values, label) {{
      select.innerHTML = [`<option value="">All ${{label}}</option>`]
        .concat(values.map(value => `<option value="${{escapeHtml(value)}}">${{escapeHtml(value)}}</option>`))
        .join('');
    }}

    function initFilters() {{
      optionList(els.carrier, [...new Set(entries.flatMap(carriers))].sort(), 'carriers');
      optionList(els.smell, [...new Set(entries.map(entry => entry.heuristic_id).filter(Boolean))].sort(), 'smells');
      optionList(els.severity, [...new Set(entries.map(entry => entry.severity).filter(Boolean))].sort(), 'severities');
      optionList(els.status, statuses, 'statuses');
    }}

    function filteredEntries() {{
      const carrier = els.carrier.value;
      const smell = els.smell.value;
      const severity = els.severity.value;
      const status = els.status.value;
      const needle = els.search.value.trim().toLowerCase();
      return entries.filter(entry => {{
        const haystack = [
          entry.entry_id,
          entry.heuristic_id,
          entry.smell_name,
          entry.source_id,
          entry.source_description,
          entry.section_path,
          entry.gap_statement,
          entry.paraphrased_evidence,
          entry.verbatim_evidence
        ].map(text).join(' ').toLowerCase();
        return (!carrier || carriers(entry).includes(carrier))
          && (!smell || entry.heuristic_id === smell)
          && (!severity || entry.severity === severity)
          && (!status || state.statuses[entry.entry_id] === status)
          && (!needle || haystack.includes(needle));
      }});
    }}

    function renderMetrics(filtered) {{
      const high = filtered.filter(entry => String(entry.severity).toUpperCase() === 'HIGH').length;
      const carriersCount = new Set(filtered.flatMap(carriers)).size;
      els.metrics.innerHTML = `
        <div class="metric"><span>Visible findings</span><strong>${{filtered.length}}</strong></div>
        <div class="metric"><span>High severity</span><strong>${{high}}</strong></div>
        <div class="metric"><span>Carriers</span><strong>${{carriersCount}}</strong></div>
      `;
    }}

    function renderList(filtered) {{
      if (!filtered.length) {{
        els.list.innerHTML = '<div class="empty">No findings match these filters.</div>';
        return;
      }}
      if (!filtered.some(entry => entry.entry_id === state.selected)) {{
        state.selected = filtered[0].entry_id;
      }}
      els.list.innerHTML = filtered.map(entry => `
        <button type="button" class="finding-button ${{entry.entry_id === state.selected ? 'active' : ''}}" data-entry="${{escapeHtml(entry.entry_id)}}">
          <div class="finding-title">${{escapeHtml(title(entry))}}</div>
          <div class="meta-row">
            <span class="badge">${{escapeHtml(carriers(entry).join(' + ') || 'All carriers')}}</span>
            <span class="badge">${{escapeHtml(entry.heuristic_id)}}</span>
          </div>
          <div class="badges">
            <span class="badge ${{severityClass(entry.severity)}}">${{escapeHtml(entry.severity)}}</span>
            <span class="badge">${{escapeHtml(entry.confidence)}} confidence</span>
            <span class="badge mode">${{escapeHtml(state.statuses[entry.entry_id])}}</span>
          </div>
          <div class="subtle">${{escapeHtml(entry.gap_statement).slice(0, 170)}}${{text(entry.gap_statement).length > 170 ? '...' : ''}}</div>
        </button>
      `).join('');
    }}

    function sectionText(section, key) {{
      return section && section[key] ? section[key] : '';
    }}

    function roleContent(entry, role) {{
      if (role === 'executive') {{
        return [
          ['Why it matters', entry.gap_statement],
          ['Scope', entry.scope],
          ['Action direction', entry.policy_designer_section?.remediation_note]
        ];
      }}
      if (role === 'compliance') {{
        return [
          ['Compliance question', sectionText(entry.compliance_section, 'compliance_question')],
          ['Regulatory grounding', (entry.compliance_section?.regulatory_citations || []).map(c => `${{c.citation}}: ${{c.summary}}`).join(' ')],
          ['Refiling note', entry.policy_designer_section?.refiling_note]
        ];
      }}
      if (role === 'claims') {{
        return [
          ['Exposure narrative', sectionText(entry.claims_section, 'exposure_narrative')],
          ['Dispute scenario', sectionText(entry.claims_section, 'dispute_scenario')],
          ['Risk', sectionText(entry.claims_section, 'bad_faith_risk')]
        ];
      }}
      if (role === 'product') {{
        return [
          ['Fix type', entry.policy_designer_section?.fix_type],
          ['Suggested language or template', entry.policy_designer_section?.suggested_language || entry.policy_designer_section?.template],
          ['Remediation note', entry.policy_designer_section?.remediation_note]
        ];
      }}
      return [
        ['Operational note', 'Use this view to decide what source, filing, or review task must happen next.'],
        ['Source availability', entry.source_id || entry.primary_instance?.source_id],
        ['Limitations', entry.policy_designer_section?.disclaimer]
      ];
    }}

    function renderRole(entry) {{
      return roleContent(entry, state.role).map(([label, value]) => `
        <div class="field"><span>${{escapeHtml(label)}}</span><p>${{escapeHtml(value)}}</p></div>
      `).join('');
    }}

    function evidence(entry) {{
      if (state.mode === 'sanitized') {{
        return {{
          label: 'Sanitized evidence',
          body: entry.paraphrased_evidence || entry.gap_statement,
          context: entry.paraphrased_context || 'Sanitized context not provided.',
          note: 'Commercial-facing mode uses paraphrased evidence. Do not treat this as the raw source text.'
        }};
      }}
      return {{
        label: 'Internal evidence',
        body: entry.verbatim_evidence || entry.primary_instance?.verbatim_evidence || entry.paraphrased_evidence,
        context: entry.verbatim_context || entry.paraphrased_context || 'Internal context not provided.',
        note: 'Internal mode may contain source text for analysis. Keep commercial exports sanitized.'
      }};
    }}

    function traceItems(entry) {{
      const items = [];
      if (entry.source_id) items.push(`Source: ${{entry.source_id}}`);
      if (entry.source_description) items.push(`Description: ${{entry.source_description}}`);
      if (entry.section_path) items.push(`Section: ${{entry.section_path}}`);
      if (entry.primary_instance) {{
        items.push(`Primary instance: ${{entry.primary_instance.carrier || ''}} ${{entry.primary_instance.source_id || ''}} ${{entry.primary_instance.section_path || ''}}`);
      }}
      for (const instance of entry.supporting_instances || []) {{
        items.push(`Supporting instance: ${{instance.carrier || ''}} ${{instance.source_id || ''}} ${{instance.section_path || ''}}`);
      }}
      return items;
    }}

    function renderDetail() {{
      const entry = entries.find(item => item.entry_id === state.selected);
      if (!entry) {{
        els.detail.innerHTML = '<div class="empty">Select a finding.</div>';
        return;
      }}
      const ev = evidence(entry);
      const trace = traceItems(entry);
      els.detail.innerHTML = `
        <div class="detail-inner">
          <div>
            <div class="badges">
              <span class="badge">${{escapeHtml(carriers(entry).join(' + ') || 'All carriers')}}</span>
              <span class="badge">${{escapeHtml(entry.heuristic_id)}}</span>
              <span class="badge ${{severityClass(entry.severity)}}">${{escapeHtml(entry.severity)}}</span>
              <span class="badge">${{escapeHtml(entry.confidence)}} confidence</span>
              <span class="badge mode">${{state.mode === 'internal' ? 'Internal evidence' : 'Sanitized evidence'}}</span>
            </div>
            <h2>${{escapeHtml(title(entry))}}</h2>
            <p class="subtle">${{escapeHtml(entry.entry_id)}} | Data source: ${{escapeHtml(payload.source_path)}} | Generated snapshot from ${{escapeHtml(payload.created_at || 'unknown date')}}</p>
          </div>

          <div class="split">
            <section class="section">
              <h3>Gap Statement</h3>
              <p>${{escapeHtml(entry.gap_statement)}}</p>
            </section>
            <section class="section">
              <h3>Reviewer Status</h3>
              <label>Status
                <select id="detailStatus">
                  ${{statuses.map(status => `<option value="${{status}}" ${{state.statuses[entry.entry_id] === status ? 'selected' : ''}}>${{status}}</option>`).join('')}}
                </select>
              </label>
              <p class="subtle">Prototype state only. This does not persist after refresh.</p>
            </section>
          </div>

          <section class="section">
            <h3>${{escapeHtml(ev.label)}}</h3>
            <p>${{escapeHtml(ev.body)}}</p>
            <details>
              <summary>Context and mode note</summary>
              <p>${{escapeHtml(ev.context)}}</p>
              <p class="subtle">${{escapeHtml(ev.note)}}</p>
            </details>
          </section>

          <section class="section">
            <div class="tabs">
              ${{[
                ['executive', 'Executive'],
                ['compliance', 'Compliance'],
                ['claims', 'Claims'],
                ['product', 'Product/Forms'],
                ['ops', 'Ops']
              ].map(([id, label]) => `<button type="button" data-role="${{id}}" class="${{state.role === id ? 'active' : ''}}">${{label}}</button>`).join('')}}
            </div>
            <div class="role-body">${{renderRole(entry)}}</div>
          </section>

          <section class="section">
            <h3>Source Trace And Limitations</h3>
            <ul class="trace-list">
              ${{trace.map(item => `<li>${{escapeHtml(item)}}</li>`).join('') || '<li>No source trace fields present.</li>'}}
            </ul>
            <details>
              <summary>Suggested fix / disclaimer</summary>
              <p>${{escapeHtml(entry.policy_designer_section?.suggested_language || entry.policy_designer_section?.template || entry.policy_designer_section?.remediation_note)}}</p>
              <p class="subtle">${{escapeHtml(entry.policy_designer_section?.disclaimer)}}</p>
            </details>
          </section>
        </div>
      `;
      document.getElementById('detailStatus')?.addEventListener('change', event => {{
        state.statuses[entry.entry_id] = event.target.value;
        render();
      }});
      els.detail.querySelectorAll('[data-role]').forEach(button => {{
        button.addEventListener('click', () => {{
          state.role = button.dataset.role;
          renderDetail();
        }});
      }});
    }}

    function render() {{
      const filtered = filteredEntries();
      renderMetrics(filtered);
      renderList(filtered);
      renderDetail();
      els.list.querySelectorAll('[data-entry]').forEach(button => {{
        button.addEventListener('click', () => {{
          state.selected = button.dataset.entry;
          render();
        }});
      }});
    }}

    document.querySelectorAll('[data-mode]').forEach(button => {{
      button.addEventListener('click', () => {{
        state.mode = button.dataset.mode;
        document.querySelectorAll('[data-mode]').forEach(item => item.classList.toggle('active', item.dataset.mode === state.mode));
        renderDetail();
      }});
    }});
    [els.carrier, els.smell, els.severity, els.status, els.search].forEach(input => input.addEventListener('input', render));

    initFilters();
    render();
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    build()
