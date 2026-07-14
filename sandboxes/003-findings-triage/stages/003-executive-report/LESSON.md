# Stage 003 Executive Report Lessons

Stage: 003-executive-report
First lesson recorded: 2026-06-04 (session 4)

---

## Lesson 1: Dollar Signs in Markdown Output Cause Math-Delimiter Rendering Corruption

### Problem

Dollar signs (`$`) inside markdown strings are treated as LaTeX math delimiters by renderers that support math mode (GitHub, Obsidian, many PDF converters, VS Code preview with math extensions). Any two `$` signs that can be parsed as a matching pair — even across prose in the same sentence or bullet point — will render the content between them as a math expression: spaces drop out, letters render in italic math font, special characters transform.

This surfaced twice in the same report:

1. **Bold label strings** (first occurrence, session 3): `**Label ($2.575M):**` — dollar sign inside bold triggers math mode, corrupting the label text.
2. **Blockquote and range strings** (second occurrence, session 4): `$1M ... $100K ... $60K–$90K` in a blockquote; `$20M–$200M` etc. in portfolio bullet points.

### Why It Mattered

The corruption is invisible in plain text editors but breaks the report in every markdown renderer the prospect is likely to use. In the blockquote case, the rendered text read: "preventing a 1Mremediationorlitigationevent,expectedvalueis100K" — the entire ROI pitch was garbled.

### Pattern or Solution

**Never use bare `$` signs in markdown output strings that will be rendered.** Two safe alternatives:

1. **Remove the dollar sign and suffix with USD for ranges:** `$20M–$200M` → `20M–200M USD`
2. **Reword amounts in prose:** `$1M remediation event` → `1M-dollar remediation event`

Single `$` signs in isolated prose sentences are usually safe (no matching pair forms). Paired `$` signs — ranges, two amounts in one sentence, amounts inside parentheses next to other amounts — always need to be defused.

**Fix must go in the source data, not just the output.** If the dollar-sign strings live in a data file (`dollar_anchors.json`) and the report is regenerated from that data, fixing only the output file is not enough — the next build re-introduces the bug. Fix the data file too.

**Defensive fix:** Add a `_safe_dollar()` sanitizer in the report builder that strips bare `$` from numeric strings before they enter markdown output. Apply at every interpolation point. This is BACKLOG-016.

### Evidence

- Session 3: first instance caught by human reviewer on the bold label strings.
- Session 4: second instance reported by user — the blockquote ROI pitch was fully garbled.
- Both instances fixed by removing dollar signs from the affected strings.
- `dollar_anchors.json` updated so future builds generate clean output.

### Limitations

This is a renderer-specific issue. Plain text tools and some markdown parsers do not render math mode and will display `$` correctly. The fix only matters for rendered output (HTML, PDF, GitHub preview, Obsidian, etc.). Do not apply aggressively to data files that are never rendered as markdown.

### What to Reuse Next Time

When building any report generator that interpolates numeric strings into markdown:
- [ ] Check all output strings for paired `$` signs before first use
- [ ] Fix dollar signs in source data files, not just rendered output
- [ ] Add a `_safe_dollar()` sanitizer at interpolation points in the builder
- [ ] Test the output in a markdown renderer before considering the report complete — plain text review is not sufficient

---

## Lesson 2: Edit LLM Report Output Directly — Do Not Re-Run for Prose Improvements

### Problem

LLM-generated prose in report sections contained boilerplate openers and closers ("rapidly evolving landscape," "cannot be understated," "showcasing a proactive stance"). The obvious fix seemed to be tightening the prompts and re-running the LLM.

### Why Direct Edit Was Better

Re-running the LLM:
- Costs money (API calls for all narrative sections)
- Is non-deterministic — the new output may fix the boilerplate but introduce new problems
- Risks destabilizing prose that was already calibrated (e.g., the pattern narratives with correctly framed heuristic descriptions and properly sourced dollar figures took iteration to get right)

The LLM output is a first draft. Once human-reviewed and approved, treat it as a document, not as a generated artifact to be regenerated. Apply targeted edits directly.

### Pattern

For prose quality improvements on an already-reviewed LLM report:
1. Identify the specific phrases to replace (make a list before editing)
2. Write exact replacement strings for each
3. Apply via direct file edit or a one-shot replacement script
4. Verify each replacement landed; delete the script after use

### Evidence

12 targeted replacements applied in one pass in session 4. All landed correctly. Report quality improved without any LLM API calls or risk of destabilizing the calibrated content.

### Limitations

This only works when the output file is a stable artifact (not regenerated on every pipeline run). If the report builder regenerates prose on every run, the edits will be overwritten. In that case, the prompts must be improved instead. The Sandbox 003 report builder calls the LLM on each run — the edited `executive_summary.md` is therefore a snapshot, and a fresh `python report_builder.py` run would overwrite the editorial changes with new LLM output.

### What to Reuse Next Time

- [ ] Treat LLM report output as a first draft, not a generated artifact
- [ ] Accumulate a list of prohibited phrases for the system prompt (session 3 lesson: add explicit "do not use" list to prevent recurrence on next generation)
- [ ] If the report will be regenerated frequently, improve the prompts. If it is a stable deliverable, edit directly.

---

## Lesson 3: Executive Summary vs. Expert Drill-Down Are Different Products, Not Different Formats

### Problem

The executive summary was initially conceived as the primary deliverable and the drill-down as a "detailed version" of the same document.

### Clarification

They are not the same product at different detail levels. They serve different readers with different jobs:

- **Executive summary** — CEO/CCO. Job: decide whether to engage. Needs: pattern-level framing, industry context, cost exposure, no filing detail. Produced once per carrier cohort.
- **Expert drill-down** — Compliance officer, claims professional, policy designer. Job: fix the problem. Needs: verbatim evidence, exact section path, regulatory grounding, suggested fix language. Produced per carrier per engagement.

The executive summary is the sales instrument. The drill-down is the paid service. Building them with the same architecture or the same pipeline is wrong — they have different sources, different outputs, different regeneration cadences, and different audiences.

### What to Reuse Next Time

When designing report outputs for a multi-audience system:
- [ ] Name the reader and their job before deciding what the report contains
- [ ] Decide early whether the output is a sales tool or a service deliverable — they have different quality/cost tradeoffs
- [ ] Build sales tools to be reusable across prospects; build service deliverables to be specific to the engagement
