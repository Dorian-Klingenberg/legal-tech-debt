# Detection Strategy Matrix: Five Policy Layer Smells

**Generated**: 2026-07-14
**Source**: Five parallel background agents analyzed 5 high-value policy-layer smells from `insurance_policy_smells.md`
**Corpus**: Kentucky homeowners insurance (32 sources in corpus; 28 ingested in Sandbox 002)

---

## Executive Summary

All five agents completed analysis and identified **25 total detection strategies** (5 per smell). Key findings:

| Smell | Strategies | Complexity Range | Real Corpus Examples | Recommended Start |
|---|---|---|---|---|
| **Circular Definition** | 5 | Low–High | KFBM UW manual self-ref | Strategy #1 (literal self-ref) + #4 (package completeness) |
| **Rule Duplication** | 5 | Low–High | KFBM/KNIC/ISO duplicates | Strategy #3 (cross-ref fan-out) + #1 (similarity hashing) |
| **Hardcoded Jurisdiction Logic** | 5 | Low–High | KNIC/KFBM missing citations | Strategy #1 (citation audit) + #2 (graph gaps) |
| **Null Reference Clause** | 5 | Low–High | Superseded bulletins | Strategy #1 (citation resolution) + #3 (temporal validity) |
| **Spec-Code Divergence** | 5 | Medium–High | Policy-system mismatches | Strategy #2 (trace-back matrix) — needs system data |

---

## Detailed Strategy Matrix

### 1. Circular Definition

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Literal self-reference detector** | Regex + normalized term echo | Low | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Two-node definition graph cycle** | Graph 2-cycle detection | Medium | Limited (missing base forms) | Phase 2 |
| **#3: Typed definition-edge cycle** | Typed graph + witness paths | High | **Best long-term design** | Phase 3 |
| **#4: Package-completeness + broken-def** | Definitions reconciliation | Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#5: Semantic equivalence loop** | NLP/embedding semantic analysis | High | Future (needs richer corpus) | Phase 4+ |

**Real Corpus Example:**
- KFBM `134870230-UW-MANUAL`: **"a claim is defined as any type of claim"**

**Integration Path:** Extend SMELL2-H004 definition extraction with self-loop scoring.

---

### 2. Rule Duplication

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Textual Similarity Hashing** | MinHash/SimHash fingerprinting | Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Normalized Clause Comparison** | Structure-aware normalization | Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#3: Cross-Reference Fan-Out** | Multi-form paragraph replacement | Low-Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#4: Lineage / Version Drift** | Form-family diffing | Medium | Kentucky corpus NOW | Phase 2 |
| **#5: Exclusion / Condition Inventory** | Clause cataloging by business meaning | High | Kentucky corpus NOW | Phase 3+ |

**Real Corpus Examples:**
- KFBM `134503212` vs. ISO `HO-04-93-1000-ROOF-ACV`: Nearly identical with **7-year roof divergence**
- KNIC `132500003-HO-04-95`: **One replacement** across HO 00 03 / 00 05 / 05 24 / 17 31 / 17 32
- KFBM `134827992`: **Appraisal/duties-after-loss** rewritten across 6 HO forms

**Integration Path:** Add `normalized_text` + `clause_fingerprint` to Stage 002 parsing; emit duplicate-cluster findings.

---

### 3. Hardcoded Jurisdiction Logic

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Citation Audit** | Lexical scan for rules + citation presence | Low | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Regulatory Traceability Gap** | Graph-based gap detection | High | **Matches Sandbox 002 Phish 5 arch** | Phase 2 |
| **#3: State-Scoped Rule Header** | Section title + imperative mining | Low-Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#4: Jurisdictional Parameter-to-Authority** | Parameter crosswalk to citations | Medium | Kentucky corpus NOW | Phase 2 |
| **#5: Filing-Package Reconciliation** | Package-level legal anchor validation | Medium-High | Kentucky corpus NOW | Phase 2 |

**Real Corpus Examples:**
- KNIC `127064322`: **"Special State Requirements"** with no KRS/KAR citation
- KFBM `134870729-RATE-MANUAL`: **"The policy must be endorsed…"** without authority
- KFBM manuals: Rating/underwriting factors missing statute/reg cross-references

**Integration Path:** Extend Phish 5 H001–H003 lexical logic into rating/manual text; use graph gaps where lexical fails.

---

### 4. Null Reference Clause

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Regulatory Citation Resolution** | Exact citation validation + authority match | Low-Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Supersession / Archive Check** | Bulletin lineage validation | Medium | Requires KY DOI archive | Phase 2 |
| **#3: Temporal Validity Comparison** | Effective-date overlap test | Medium | Requires timeline metadata | Phase 2 |
| **#4: Filing-Package Cross-Reference** | Cross-document resolution | Medium-High | Kentucky corpus NOW | Phase 2 |
| **#5: Graph-Based Missing-Live-Authority** | Regulatory edge gap detection | High | **Matches Sandbox 002 Phish 5 upgrade** | Phase 3+ |

**Integration Path:** Citation resolution (#1) → supersession check (#2) → temporal comparison (#3). Strategy #5 is the eventual Phish 5 graph-gap architecture.

**Data Dependencies:** KY DOI bulletin archive, SERFF metadata, official KRS/KAR database.

---

### 5. Spec-Code Divergence

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Structural Clause-to-Rule Diff** | Policy clauses vs. system rules diff | High | Requires PAS/system artifacts | Phase 3+ |
| **#2: Trace-Back Coverage Matrix** | Policy-to-system bidirectional audit | Medium | **Recommended** — extends Sandbox 002 | Phase 2 |
| **#3: Scenario Replay / Golden-Path** | Test-coverage audit + executable scenarios | High | Requires system access | Phase 3+ |
| **#4: Version-Sync Lineage Drift** | Filing/spec/config version alignment | Medium | Aligns with Sandbox 002 versioning | Phase 2 |
| **#5: Outcome-Based Divergence Mining** | Claim outcome clustering audit | High | Requires operational claim data | Phase 4+ |

**Integration Path:** Strategy #2 (trace-back) and #4 (version-sync) extend naturally from Sandbox 002's provenance layer. Strategies #1, #3, #5 require system-level data.

**Key Insight:** Sandbox 002 provides policy-side provenance; system-side comparators would be needed for full spec-code divergence detection.

---

## Phased Implementation Roadmap

### Phase 1: MVP Detectors (Can run on Kentucky corpus NOW)

**Recommended smell/strategy combinations:**

1. **Circular Definition (#1 + #4)**
   - Literal self-reference + package-completeness check
   - Low complexity, high signal
   - Expected to find: Self-referential definition patterns in manuals

2. **Rule Duplication (#1 + #2 + #3)**
   - Similarity hashing + normalized comparison + cross-ref fan-out
   - Medium complexity, high signal
   - Expected to find: Duplicated roof ACV, appraisal conditions, latent defect clauses

3. **Hardcoded Jurisdiction Logic (#1 + #3)**
   - Citation audit + state-scoped header mining
   - Low complexity, high signal
   - Expected to find: "Special state requirements," "must be endorsed" patterns without citations

4. **Null Reference Clause (#1)**
   - Citation resolution only (can expand with archive check in Phase 2)
   - Low-Medium complexity, medium signal
   - Expected to find: Named DOI bulletins and SERFF references that can be validated

### Phase 2: Extended Detectors (Leverage Sandbox 002 graph)

- Circular Definition (#2 + #3): Graph cycle detection with typed edges
- Rule Duplication (#4 + #5): Lineage drift + condition inventory
- Hardcoded Jurisdiction Logic (#2 + #4 + #5): Graph gaps + parameter crosswalk + package reconciliation
- Null Reference Clause (#2 + #3 + #4 + #5): Supersession + temporal + cross-ref triangulation + live-authority graph
- Spec-Code Divergence (#2 + #4): Trace-back matrix + version-sync lineage

### Phase 3+: System-Integration Detectors

- Spec-Code Divergence: Structural diff, scenario replay, outcome mining (requires PAS/claims data)
- Advanced Circular Definition: Semantic equivalence loops (requires richer corpus)

---

## Quick Integration Checklist

- [ ] Phase 1 MVP detectors: 4 smells with ~12 strategies total
- [ ] Add normalized_text + clause_fingerprint to Stage 002 parsing
- [ ] Extend H004 definition extraction with self-loop scoring
- [ ] Create citation resolution pipeline for H001–H003 and Phish 5
- [ ] Implement state-scoped header mining in rate/manual text
- [ ] Cluster identical clauses via similarity hashing
- [ ] Stage 006 emits duplicate-cluster findings
- [ ] Document real corpus examples and false-positive handling

---

## Success Metrics

**Phase 1 (MVP):**
- Detect ≥3 Circular Definition instances in KFBM manuals
- Detect ≥5 Rule Duplication clusters (KFBM/KNIC/ISO)
- Detect ≥4 Hardcoded Jurisdiction Logic instances
- Detect ≥2 Null Reference Clause citations

**Phase 2 (Extended):**
- Implement graph-based detectors for all 5 smells
- Cross-validate findings across Phish 1–5 existing detectors
- Document false-positive handling and confidence scoring

**Phase 3+ (System-Integration):**
- Implement spec-code divergence matrix audit
- Compare policy corpus findings against PAS/claims outcomes
- Identify patterns not detectable from policy documents alone

---

## Notes for Next Implementation Phase

This matrix is ready for:
1. **Prototype implementation** (assign to agent tasked with building Phase 1 detectors)
2. **False-positive tuning** (integrate real corpus signals into detection logic)
3. **ROI prioritization** (rank by detectability, false-positive risk, and business impact)
4. **Stage 002 integration** (extend existing detector pipeline)
