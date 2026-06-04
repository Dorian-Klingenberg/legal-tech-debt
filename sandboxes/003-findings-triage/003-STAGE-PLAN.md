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

**Question:** Can an LLM reliably explain each finding in plain English, assess its false positive risk, and propose a concrete next step — without inventing legal conclusions?

**What it does:**
- Takes each `Finding` record from Stage 006 output
- Sends evidence text + rationale + reviewer question to Claude
- Gets back: plain-English explanation, dispute scenario, false positive assessment, recommended next step
- Writes enriched findings JSONL with LLM annotations alongside original fields
- Human reviewer validates a sample — measure hallucination rate and false positive dismissal rate

**Why this first:** The output of this stage feeds every other stage. Without plain-English explanations, nothing downstream is accessible to a non-technical buyer.

**Key constraint:** LLM output is annotation only — never overwrites the original finding. Original provenance and evidence text stay intact.

---

### Stage 002: Cross-Carrier Pattern Analysis

**Question:** Do the same smells appear in both KNIC and KFBM policy language? Where do they diverge?

**What it does:**
- Groups findings by smell and heuristic across carriers
- Identifies patterns that appear in both carriers (industry-wide) vs. one only (carrier-specific)
- Flags cases where both carriers use the same undefined term (e.g., "actual cash value" without methodology) — that's the strongest signal for systemic risk
- Produces a carrier comparison table per smell

**Why this matters:** A single carrier finding is a filing question. The same finding in two independently-filed carriers is an industry pattern. Industry patterns are what regulators and litigators care about.

---

### Stage 003: Executive Summary Report

**Question:** Can we produce a one-page summary that a CEO or Chief Claims Officer can read in five minutes and understand what risk the findings represent?

**What it does:**
- Takes the enriched findings (Stage 001) and cross-carrier analysis (Stage 002)
- Produces a short executive report: top 3 findings by business risk, estimated dispute exposure per finding type, recommended actions
- Format: clean HTML + PDF-ready markdown; no technical jargon, no node IDs, no JSONL

**Output target:** Something you'd put in front of a potential client to demonstrate value before a sales conversation.

---

## What This Sandbox Does NOT Do

- Does not make legal conclusions — findings are patterns for human judgment
- Does not build a production API or deployment infrastructure
- Does not automate regulatory filings
- Does not expand the corpus (that stays in Sandbox 002)

---

## Prerequisites Before Starting

- [x] Sandbox 002 artifact contract repaired and revalidated on run `18b0dec5`
- [x] Gold set re-evaluated on repaired expanded run — BM25 remains 21/21
- [x] Sandbox 002 closure decision recorded in ADR-009
- [ ] Treat Smell 5 as a known detector-calibration limitation; calibrate before claiming five-smell completeness
- [ ] Perplexity/external LLM feedback on the current reviewer report reviewed and incorporated into Stage 003 design
- [ ] Decision on which Claude model to use for Stage 001 triage (Sonnet vs. Opus; cost vs. quality tradeoff)
- [ ] Prompt design for LLM triage reviewed by a human before running at scale
