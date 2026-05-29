# Roadmap (Revised): Insurance Legal Tech Debt Platform

*Version 2.0 — May 2026*

This roadmap updates the original "Insurance Claims Regulatory Automation Platform" plan
by incorporating the legal code smell taxonomy and cost estimates.
It focuses Phase 1 on the **highest-cost, technically tractable smells**:

- Broken Link / Null Reference Clause
- Calculation Rule Drift

and pushes toward a unified **legal tech debt probe** before full productization.

---

## Phase 0.5: Smell Impact Triage (Weeks 0–1)

**Objective**: Use the smell taxonomy and cost model to choose the first detectors
based on economic impact rather than guesswork.

### Deliverables

1. **Smell Impact Brief**
   - Ranked list of policy-layer smells by estimated 10-year cost impact
     (e.g., Calculation Rule Drift, Untested Coverage Path, Coverage Inversion,
     Magic Number Term, Broken Link / Null Reference).[1]
   - Mapping from each smell to cost pools:
     - Premium / claims leakage
     - Litigation / bad faith
     - Compliance / IT rework

2. **Initial Detector Shortlist**
   - Phase 1 detector set:
     - Broken Link / Null Reference Clause
     - Calculation Rule Drift (narrow scope: one exposure base, one LOB)
   - Phase 2 detector candidates:
     - Untested Coverage Path
     - Coverage Inversion + Magic Number Terms
     - Regulatory Drift Map

3. **Updated Success Metrics**
   - Target \$ impact per detector (order-of-magnitude) based on cost model.

### Success Criteria

- ✅ Short document (<5 pages) summarizing top smells and their cost impact.
- ✅ Clear justification for why Broken Links + Calculation Drift are Phase 1 targets.
- ✅ Agreement on which smells are deferred to Phase 2.

---

## Current Scope

This roadmap is currently narrowed to Kentucky homeowners insurance. Do not pursue personal auto, motor vehicle, no-fault, or PIP work unless that scope is explicitly reopened.

## Phase 1: Validation — Broken Links + Calculation Drift (Weeks 1–4)

**Objective**: Prove that detecting **Broken Links** and **Calculation Rule Drift**
for a narrow KY homeowners fixture is technically feasible and delivers
immediate value.

### 1.1 MVP: Dual-Detector Probe

**Inputs**
- ~50 sample insurance policies/forms or synthetic excerpts for KY homeowners.
- NAIC model laws + one state's insurance code (statutory reference).
- A simplified rating specification for one exposure base (e.g., dwelling TIV,
  roof age, construction type, protection class, dwelling TIV, or square footage) with a "filed/expected" formula.

**Process**
- Lightweight parsing to:
  - extract section anchors and definitions
  - extract intra-document references
  - extract external citations (statutes, bulletins, bureau forms)
- Build adjacency and two-hop matrices; tag edges with simple types
  (DEFINES, REFERS_TO, CITES_EXTERNAL).
- Run detectors:
  1. **Broken Link / Null Reference Clause**:
     - internal REFERS_TO edges whose targets do not exist
     - CITES_EXTERNAL edges referencing repealed/unknown authorities
  2. **Calculation Rule Drift**:
     - compare implemented rating formula for one exposure base
       against the "filed/expected" formula
     - flag discrepancies in factors, thresholds, or bases

**Outputs**
- `findings.json` with structured findings for both smells.
- `report.md` summarizing issues by policy and by smell.
- Sample matrices (`section_index.csv`, `adjacency_matrix.csv`, `two_hop_matrix.csv`).

### 1.2 Documentation

- Technical architecture of the **legal debt probe**:
  - parsing, indexing, graph construction, detectors.
- Data flow diagram from corpus → findings → report.
- Accuracy benchmark:
  - precision/recall for broken links and drift on a labeled subset.

### 1.3 Business Validation

- 3–5 interviews with insurance compliance / product / actuarial SMEs:
  - "Have you seen broken statutory references in your policies/forms/rules?"
  - "Have you ever discovered, after the fact, that a rating formula
     drifted from the filed/required version? What did it cost?"
- Back-of-envelope ROI model per detector:
  - Broken Links: avoided market conduct findings, avoided re-filing and reprint costs.
  - Calculation Drift: estimated premium/claims leakage avoided if a drift is caught
    earlier.

### Success Criteria

- ✅ System processes a 50-policy KY fixture in < 10 minutes on a laptop.
- ✅ Finds 80%+ of known broken references on a labeled sample.
- ✅ Detects at least one realistic instance (or synthetic equivalent) of
   Calculation Rule Drift.
- ✅ SMEs confirm both smells are real, recurring pain.
- ✅ Go/no-go: Proceed to Phase 2 (Core Probe & Detectors)?

---

## Phase 2: Core Probe & High-ROI Detectors (Weeks 5–12)

**Objective**: Turn the prototype probe into a reusable engine and
add the next two high-impact detectors.

### 2.1 Core Probe Hardening

- Extract a `probe_corpus(corpus_path) -> Findings` API:
  - plain Python, no external services.
- Define stable data models:
  - `Section`, `Edge`, `Finding`, `SmellType`.
- Add a minimal configuration file for:
  - corpus path
  - jurisdiction
  - enabled detectors

### 2.2 Detector 3: Untested Coverage Path

- Design a simple scenario schema (JSON/YAML) that exercises coverage paths.
- For a given product/state:
  - enumerate combinations of forms, endorsements, and key attributes
  - mark which combinations have no explicit test
- Output: list of "untested coverage paths" for the KY fixture.

### 2.3 Detector 4: Coverage Inversion + Magic Number Terms

- Identify clauses where:
  - broad granting language is followed by many narrow exclusions
  - thresholds like "reasonable time" or "substantial" are used without
    numeric anchors
- Use heuristics + pattern matching, not heavy NLP.
- Output: ranked list of high-risk clauses with:
  - location
  - snippet
  - suggested clarification questions (not legal advice).

### 2.4 Human-Readable Dashboard Prototype

- Basic web or static HTML view (no full product yet):
  - Legal Debt Scorecard by product/state/smell.
  - Drill-down to findings and underlying text.

### Success Criteria

- ✅ Four detectors operational on the KY fixture:
  - Broken Links
  - Calculation Drift
  - Untested Coverage Paths
  - Coverage Inversion / Magic Number Terms
- ✅ Probe API stable enough to reuse in later phases.
- ✅ Simple dashboard demonstrates value to at least one SME.
- ✅ Go/no-go: Proceed to Phase 3 (Pilot) or iterate?

---

## Phase 3: Pilot with Real Corpus (Weeks 13–24)

**Objective**: Run the probe on a real carrier's policy/spec corpus
for one line of business in one or two states.

### 3.1 Deployment for Pilot

- Containerized probe (Docker) with:
  - mounted corpus directory
  - scheduled runs (e.g., nightly)
- Secure handling of customer documents.

### 3.2 Data Pipeline

- Automated ingestion of:
  - carrier policy forms and specs
  - a subset of relevant statutes and bulletins
- Minimal change detection:
  - re-run probe when new filings or forms are added.

### 3.3 SME Workflow

- Provide:
  - Legal Debt Report (policy-layer smells only)
  - Simple UI or static site to explore findings
- Collect feedback on:
  - false positives / negatives
  - most/least useful smells
  - desired next detectors.

### Success Criteria

- ✅ Probe runs regularly on real corpus without manual babysitting.
- ✅ Carrier identifies at least a handful of "we should fix this" findings.
- ✅ Clear evidence of avoided rework / compliance risk.
- ✅ Go/no-go: Invest in full productization (Phase 4)?

---

## Phase 4: Productization & Expansion (Weeks 25–52)

**Objective**: Evolve the probe into a product, add scale/features,
start selling to multiple carriers or software vendors.

### 4.1 Product Hardening

- Performance: handle 10,000+ policies / specs.
- Multi-tenant architecture.
- Audit logging and immutable finding history.

### 4.2 Deeper Tech (Only Where Needed)

- Swap in richer extraction where it clearly earns its keep:
  - spaCy or LLM for better citation/definition extraction.
  - Neo4j for large graphs, when matrix-based approach hits limits.
- Consider structured representations (Akoma Ntoso, LegalRuleML) for
  customers willing to invest in structured corpora.

### 4.3 Go-to-Market & Thought Leadership

- Position as **"Legal Tech Debt Probe for Insurance"**, not generic RegTech.
- GTM assets:
  - case study from pilot
  - ROI calculator based on smell cost estimates
  - whitepaper: "State of Legal Tech Debt in Insurance 2027".

---

## Decision Gates

**After Phase 0.5**:
- Do cost estimates clearly point to Broken Links + Calculation Drift as
  Phase 1 targets?
- → Decision: lock Phase 1 scope or re-rank detectors.

**After Phase 1**:
- Are the dual detectors technically sound and validated by SMEs?
- → Decision: invest in Core Probe & additional detectors?

**After Phase 2**:
- Do the four detectors together tell a coherent "legal debt" story?
- → Decision: run a real pilot?

**After Phase 3**:
- Did the pilot demonstrate concrete value and avoid real risk/rework?
- → Decision: invest in full productization and GTM?

---

[1] See "Insurance Policy Smells" and "Insurance Policy Smells — Cost Estimates" documents
for the underlying taxonomy and cost attribution.
