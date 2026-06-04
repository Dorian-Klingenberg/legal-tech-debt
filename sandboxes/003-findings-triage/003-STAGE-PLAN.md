# Sandbox 003: Findings Triage And Intelligence

Status: **Planning — next active lane**
Scope: Take structured findings from Sandbox 002 and make them business-actionable
Created: 2026-06-03
Depends on: Sandbox 002 repaired run `output/002/20260604_130606_18b0dec5/`, Stage 006 findings JSONL, and Stage 007 reviewer report

---

## The Problem This Sandbox Solves

Sandbox 002 produces structured `Finding` records — each one has a node, evidence text, confidence level, rationale, and a reviewer question. That output is technically correct but not yet useful to a non-technical audience. A claims officer, coverage counsel, or CEO cannot directly act on a JSONL file.

This sandbox turns findings into decisions.

---

## Guiding Question

> Can we take the structured findings from Sandbox 002 and produce output that a claims professional or executive can act on without understanding the pipeline that generated it?

---

## Proposed Stages

### Stage 001: LLM-Assisted Finding Triage

**Question:** Can an LLM reliably explain each finding in plain English, assess its false positive risk, assign business severity, suggest a remediation direction, and propose a concrete next step — without inventing legal conclusions?

**What it does:**
- Takes each `Finding` record from Stage 006 output
- Sends evidence text + rationale + reviewer question to Claude
- Gets back:
  - plain-English explanation of the issue
  - dispute scenario (what goes wrong if this is not addressed)
  - false positive assessment
  - business severity signal — maps finding to claim frequency, litigation sensitivity, and regulatory exposure, not just technical confidence level
  - remediation direction — concrete suggested next step (e.g., add a definition, anchor a version reference, replace open-ended timing language), not just a reviewer question
- Writes enriched findings JSONL with LLM annotations alongside original fields
- Human reviewer validates a sample — measure hallucination rate and false positive dismissal rate

**Why this first:** The output of this stage feeds every other stage. Without plain-English explanations and business-severity framing, nothing downstream is accessible to a non-technical buyer.

**Key constraint:** LLM output is annotation only — never overwrites the original finding. Original provenance and evidence text stay intact.

---

### Stage 002: Cross-Carrier Pattern Analysis

**Question:** Do the same smells appear in both KNIC and KFBM policy language? Where do they diverge?

**What it does:**
- Groups findings by smell and heuristic across carriers
- Explicitly labels each pattern as **industry-wide** (appears in both KNIC and KFBM) or **carrier-specific** (one carrier only) — industry-wide patterns are the strongest signal for systemic risk and the most compelling evidence for a buyer
- Flags cases where both carriers use the same undefined term (e.g., "actual cash value" without methodology)
- Produces a carrier comparison table per smell

**Why this matters:** A single carrier finding is a filing question. The same finding in two independently-filed carriers is an industry pattern. Industry patterns are what regulators and litigators care about, and what makes a sales conversation more than an anecdote.

---

### Stage 003: Executive Summary Report

**Question:** Can we produce a one-page summary that a CEO or Chief Claims Officer can read in five minutes and understand what risk the findings represent?

**What it does:**
- Takes the enriched findings (Stage 001) and cross-carrier analysis (Stage 002)
- Produces a short executive report framed around **decisions and actions**, not a findings list:
  - top findings by business severity (claim frequency, litigation sensitivity, regulatory exposure)
  - dollar anchors where available (e.g., ACV/RCV payment swings, published dispute settlements)
  - industry-wide vs. carrier-specific pattern distinction
  - recommended actions per finding — what a compliance team or filing lawyer should do next
- Format: clean HTML + PDF-ready markdown; no technical jargon, no node IDs, no JSONL
- Tone: written for a CEO or Chief Claims Officer who will hand it to a team, not read it themselves

**Output target:** Something you'd put in front of a potential client to demonstrate value before a sales conversation. The `business_owner_prospects_report.md` and `KNIC_real_world_examples_and_costs_report.md` in Sandbox 002 are reference prototypes for the tone and structure this report should achieve.

---

## What This Sandbox Does NOT Do

- Does not make legal conclusions — findings are patterns for human judgment
- Does not build a production API or deployment infrastructure
- Does not automate regulatory filings
- Does not expand the corpus (that stays in Sandbox 002)
- Does not design workflow integration (dashboards, issue tracking, sign-off flows, document management hooks) — that is a product-design question for a later lane

---

## Prerequisites Before Starting

- [x] Sandbox 002 artifact contract repaired and revalidated on run `18b0dec5`
- [x] Gold set re-evaluated on repaired expanded run — BM25 remains 21/21
- [x] Sandbox 002 closure decision recorded in ADR-009
- [ ] Treat Smell 5 as a known detector-calibration limitation; calibrate before claiming five-smell completeness
- [x] Perplexity/external LLM feedback on the current reviewer report reviewed and incorporated into Stage 003 design — key outputs: add business severity + remediation direction to Stage 001 annotations; label industry-wide vs. carrier-specific in Stage 002; frame Stage 003 report around decisions and actions with dollar anchors
- [ ] Decision on which Claude model to use for Stage 001 triage (Sonnet vs. Opus; cost vs. quality tradeoff)
- [ ] Prompt design for LLM triage reviewed by a human before running at scale
