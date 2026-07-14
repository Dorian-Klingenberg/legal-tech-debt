# Backlog Implementation Plan

Date: 2026-06-05
Audience: Claude Code, Codex, GitHub Copilot, and future agents
Status: Historical implementation brief; superseded by completed backlog records and active sandbox stage plans

> This file preserves the June 5 execution briefs that led to the completed work in `BACKLOG.md`. It is not a current queue and must not be used to reopen BACKLOG-019, BACKLOG-015, BACKLOG-020, BACKLOG-011, BACKLOG-022, or BACKLOG-023. Current work starts at `README.md`, `AGENT_CONTEXT.json`, and the active sandbox stage document.

## Historical Disposition Checklist

- [x] Reconcile every brief with its final status in `BACKLOG.md`.
- [x] Move current sandbox work into dedicated stage plans.
- [x] Mark this June 5 brief as superseded rather than an active queue.

## Purpose

This file turns the open backlog into detailed, constrained implementation briefs. It is intended especially for Claude Code, where the best results come from a tight file allowlist, exact next steps, and explicit forbidden actions.

## Claude Startup Contract

Before working any item:

0. Read `CLAUDE_CONSTRAINTS.md` before any exploration, file reads, planning, or edits.
1. Read `BOOTSTRAP.md`.
2. Read `AGENT_CONTEXT.json`.
3. Read `AGENT_OPERATING_MODEL.md`.
4. Read `CLAUDE.md`.
5. Read `BACKLOG.md`.
6. Read this file.
7. Read the item-specific files listed below.
8. Read `skills/project-coding-preferences/SKILL.md` before code changes.
9. If creating or updating journals, handoffs, lessons, or context, read `skills/project-memory-artifacts/SKILL.md`.

## Global Constraints

- Current preserved Stage 002 run: `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/`
- Current canonical detector findings: `sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl`
- Keep work local-first: plain Python, JSON/JSONL/Markdown, no services, no databases, no vector store, no production scaffolding.
- Do not expand beyond Kentucky homeowners unless the backlog item explicitly requires a public external comparison or public case lookup.
- Do not make legal conclusions. Produce evidence, candidate findings, reviewer questions, and source-traceable notes.
- Do not rewrite Stage 002 ingestion outputs unless the item explicitly requires a Stage 002 rerun.
- For focused detector changes, extend Stage 006 in place and write updated Stage 006 outputs for the preserved run. If the work becomes a broader experiment or new output layer, stop and create a new numbered stage plan instead.
- Journals go under top-level `journal/`. Handoffs stay near the sandbox or component they resume.

## Validation Commands

Use these as the default validation anchors when the relevant layer changes.

```powershell
cd sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors
python src/detector_runner.py --run-dir ../../output/002/20260604_130606_18b0dec5
```

```powershell
git diff --check
git status --short
```

When detector outputs change, report:

- total findings,
- findings by smell,
- new or removed finding count,
- run directory,
- and any findings intentionally treated as review leads rather than confirmed defects.

## Priority 1: BACKLOG-019 - Missing State Amendatory Detector

Goal: detect a filing package that appears to use a multi-state master jacket but lacks a Kentucky amendatory or Kentucky special provisions form in the attachment/form set.

Why this is first: it is binary, high-value, and aligned with the Sandbox 004 product principle that the product audits internal filing completeness.

Read first:

- `BACKLOG.md`, section `BACKLOG-019`
- `sandboxes/004-expert-drilldown/HANDOFF-2026-06-04.md`
- `sandboxes/004-expert-drilldown/README.md`
- `sandboxes/002-claims-regulatory-automation/adr/ADR-010-smell5-retrieval-architecture-gap-detection.md`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detectors/smell5.py`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/models.py`
- `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md`
- `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`

Likely files to edit:

- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detectors/smell5.py`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py` only if registration or shared filtering is needed
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/STAGE.md`
- `BACKLOG.md`
- `journal/YYYY-MM-DD-*.md`

Implementation shape:

- Add a new Smell 5 heuristic, probably `SMELL5-H007`, for missing Kentucky amendatory.
- Use source/package evidence only. Do not infer from ISO comparison.
- Search Stage 002 nodes and source metadata for:
  - form schedule / attachment list / forms list / endorsements list,
  - multi-state cues such as "state amendatory", "special provisions", "for use in", "all states", "state exceptions", "Kentucky amendatory", "KY amendatory",
  - Kentucky-specific expected terms such as "Kentucky", "KY", "amendatory", "special provisions", "mandatory endorsement".
- Emit a finding only when both sides are supported:
  - a source/package appears to contain a multi-state or state-variable form set,
  - and no Kentucky amendatory/special-provisions payload is found in the same source package or related attachment list.
- Prefer one consolidated source-level finding with `supporting_nodes` rather than many repetitive node findings.

Acceptance criteria:

- The detector does not fire on KRS/KAR/DOI reference nodes.
- Evidence text shows the master/multi-state or state-variable cue.
- Reviewer question asks for the missing Kentucky amendatory/special provisions form or filing attachment.
- False-positive risk names the main benign explanation: Kentucky provisions may be embedded in a proprietary base form or a separate filing not in the current corpus.
- If no finding is supported by the current corpus, document that result clearly rather than forcing a finding.

Forbidden actions:

- Do not procure new SERFF filings unless the user explicitly asks.
- Do not claim Kentucky law requires a specific amendatory unless a source in the corpus supports it.
- Do not add a vector or LLM dependency.

## Priority 2: BACKLOG-015 - Heuristic-Specific Case And Bad-Faith Closure Library

Goal: replace broad ROI examples with public cases, enforcement actions, or documented bad-faith closures tied to the exact heuristics in the confirmed findings.

Read first:

- `BACKLOG.md`, section `BACKLOG-015`
- `sandboxes/003-findings-triage/stages/003-executive-report/data/dollar_anchors.json`
- `sandboxes/003-findings-triage/stages/003-executive-report/output/executive_summary.md`
- `sandboxes/003-findings-triage/stages/001-llm-triage/validation/human-review-notes.md`
- `sandboxes/004-expert-drilldown/data/drill_down_entries.json`

Suggested artifact targets:

- `sandboxes/004-expert-drilldown/research/heuristic-case-library.md`
- Optional machine-readable companion: `sandboxes/004-expert-drilldown/data/case_library.json`

Implementation shape:

- Research one heuristic at a time.
- Use public records only.
- For each heuristic, record case/action name, jurisdiction, year, source URL or citation, specific language gap, outcome, and connection to the heuristic.
- If no public case is found for a heuristic, record "not found yet" with search terms used.
- Do not invent or stretch cases to fit.

Priority heuristic order:

1. `SMELL2-H003` / reclassified Smell 4: undisclosed ACV or replacement-cost methodology.
2. `SMELL4-H001`: unversioned manual reference.
3. `SMELL5-H004`: rate-setting nodes with no regulatory citation.
4. `SMELL2-H001`: undefined "reasonable time" in roof/windstorm settlement.
5. `SMELL5-H005`: mandatory coverage assertion with no regulatory citation.
6. `SMELL5-H006`: loss-settlement methodology with no regulatory citation.

Acceptance criteria:

- Every entry has a public source.
- Every entry states the exact heuristic connection in one sentence.
- Weak matches are labeled weak, not promoted.
- No confidential claim data is used.

## Priority 3: BACKLOG-020 - Tighten Broken Definitions Loop Detector

Goal: detect terms used as defined terms in policy body text but missing from the Definitions Section.

Read first:

- `BACKLOG.md`, section `BACKLOG-020`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detectors/smell2.py`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/models.py`
- `sandboxes/003-findings-triage/stages/001-llm-triage/validation/human-review-notes.md`

Likely files to edit:

- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detectors/smell2.py`
- Possibly `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py` if `idx` is needed
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/STAGE.md`
- `BACKLOG.md`

Implementation shape:

- Add a new heuristic, likely `SMELL2-H004`, instead of replacing existing H003 immediately.
- Extract candidate defined terms from quotes, bold markers if present in parsed text, and definition-style capitalization only when evidence is strong.
- Build a same-source Definitions Section term set from nodes whose section path or text indicates definitions.
- Flag body terms absent from that same-source Definitions Section.
- Keep confidence LOW or MEDIUM unless the source has a clear Definitions Section and the term clearly appears as a defined term.

Acceptance criteria:

- Does not flag ordinary capitalized words.
- Does not flag terms when no Definitions Section is present in the current source.
- Preserves source/node provenance and reviewer question.

## Priority 4: BACKLOG-007 - KRS/KAR Definitional Cross-Reference Check

Goal: downweight or annotate Smell 2 findings when a flagged term is defined in Kentucky statutes or regulations already in the corpus.

Read first:

- `BACKLOG.md`, section `BACKLOG-007`
- `sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl`
- `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/nodes.jsonl`
- `sandboxes/002-claims-regulatory-automation/output/002/20260604_130606_18b0dec5/edges.jsonl`
- `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md`

Implementation shape:

- Start with an audit script or report before changing detector behavior.
- Check terms: `reasonable time`, `actual cash value`, `replacement cost`, `market value`, `depreciation`.
- Search only regulatory source nodes first.
- If definitions exist, create a post-detection enrichment or detector adjustment proposal.

Acceptance criteria:

- Produces a short Markdown audit with exact source/node IDs.
- Does not suppress findings automatically without a clear definition match.
- Records whether the term is truly defined or merely used.

## Priority 5: BACKLOG-011 - Filter Section Headers And Structure Nodes

Goal: prevent detector findings from firing on section headers, table-of-contents nodes, and document-title-only nodes.

Read first:

- `BACKLOG.md`, section `BACKLOG-011`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py`
- `sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl`

Likely files to edit:

- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/src/detector_runner.py`
- `sandboxes/002-claims-regulatory-automation/stages/006-deterministic-detectors/STAGE.md`
- `BACKLOG.md`

Implementation shape:

- Add a conservative pre-filter in `detector_runner.py`.
- Filter out nodes with very short substantive text after stripping section path/title repetition.
- Suggested threshold: 50 to 75 non-title characters.
- Log how many carrier nodes were skipped.

Acceptance criteria:

- Re-run Stage 006 and report before/after finding counts.
- Confirm no high-confidence finding is removed without review.
- If the filter removes a legitimate short provision, lower the threshold or make the filter more specific.

## Priority 6: BACKLOG-003 - Kentucky Growers SERFF Recheck

Goal: confirm whether Kentucky Growers filings are available in SERFF Filing Access.

Read first:

- `BACKLOG.md`, section `BACKLOG-003`
- `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md`
- `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md`

Implementation shape:

- Search SERFF Filing Access for Kentucky, TOI 04.0 and 04.1, company terms "Growers" and "Kentucky Growers".
- Record exact date, search terms, and result.
- If SERFF is down, update the gap record with a dated "site unavailable" note and stop.
- If still no results, propose closing the gap as unavailable in SFA.

Acceptance criteria:

- `KNOWN-GAPS.md` reflects the exact search outcome.
- No new source files are added unless a real filing is found and the user has approved procurement.

## Priority 7: BACKLOG-002 - Corpus File Extension Mismatches

Goal: rename corpus files that contain PDF content but have `.html` extensions.

Read first:

- `BACKLOG.md`, section `BACKLOG-002`
- `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`
- `corpus/kentucky-homeowners-policy-smells/CORPUS-SOURCES.md`

Files involved:

- `corpus/kentucky-homeowners-policy-smells/sources/KY-KRS-304-12-230.html`
- `corpus/kentucky-homeowners-policy-smells/sources/KY-KRS-304-14.html`

Implementation shape:

- Rename to `.pdf`.
- Update `_download_manifest.csv`.
- Update any corpus source index references.
- Re-run Stage 002 only if the change is intended to refresh outputs. Otherwise document that output refresh is deferred.

Acceptance criteria:

- No references to the old source paths remain in active corpus indexes.
- The repo records whether Stage 002 was rerun or deliberately not rerun.

## Priority 8: BACKLOG-009 - Candidate New Smell: Non-Deterministic Underwriting Criteria

Goal: determine whether this candidate smell already exists in the taxonomy or needs a proposed taxonomy entry.

Read first:

- `BACKLOG.md`, section `BACKLOG-009`
- `legal_code_smell_taxonomy.md`
- `insurance_policy_smells.md`
- `insurance_claims_smells.md`
- `sandboxes/003-findings-triage/stages/001-llm-triage/validation/human-review-notes.md`

Implementation shape:

- Search taxonomy docs for underwriting, eligibility, subjective criteria, non-deterministic criteria, discretion, and vague standards.
- If an existing smell covers it, update `BACKLOG.md` with the mapping.
- If not, draft a candidate taxonomy entry for human review.
- Do not build detectors yet.

Acceptance criteria:

- The result is a taxonomy mapping or a clearly labeled candidate smell proposal.
- Scope stays underwriting-layer, not claims-layer.

## Gated Items

Do not hand these to Claude as implementation tasks yet unless the gating condition is explicitly resolved.

- `BACKLOG-005`: blocked on owner SE coursework, SE expert RAG corpus, and Gherkin/BDD setup.
- `BACKLOG-006`: gated by validation design for node language-context classification.
- `BACKLOG-012`: practically dependent on the same context-classification design as `BACKLOG-006`.

## End-Of-Session Requirements For Claude

At the end of any backlog item:

- Update `BACKLOG.md` with current status and evidence.
- Update the relevant stage doc or sandbox doc if behavior changed.
- Write a top-level journal entry under `journal/`.
- Write or update a handoff if work is partial, blocked, or changes the next resume point.
- Run `git diff --check`.
- Report validation commands, counts, and any commands not run.
