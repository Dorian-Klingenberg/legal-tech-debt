# Detection Strategy Matrix: Five Policy Layer Smells

**Generated**: 2026-07-14
**Source**: Five parallel background agents analyzed 5 high-value policy-layer smells from `insurance_policy_smells.md`
**Corpus**: Kentucky homeowners insurance (32 sources in corpus; 28 ingested in Sandbox 002)

---

## Evidence Status

This is a Stage 001 strategy inventory, not a detector evaluation. Corpus
examples below are candidate signals unless explicitly stated otherwise.
Projected counts and precision are Stage 002 success targets, not achieved
results. The current corpus cannot establish Spec-Code Divergence because it
contains no paired PAS or configuration artifact.

All teaching examples in the accompanying [lesson catalog](lessons/README.md)
are synthetic. Real corpus evidence is identified by source ID and paraphrased.

---

## Executive Summary

All five agents completed analysis and identified **25 total detection strategies** (5 per smell). Key findings:

| Smell | Strategies | Complexity Range | Corpus Evidence Status | Recommended Start |
|---|---|---|---|---|
| **Circular Definition** | 5 | Low–High | Literal term-echo candidate | Strategy #1 (literal self-ref) + #4 (package completeness) |
| **Rule Duplication** | 5 | Low–High | Lineage, delta, and fan-out candidates | Strategy #3 (cross-ref fan-out) + #1 (similarity hashing) |
| **Hardcoded Jurisdiction Logic** | 5 | Low–High | Uncited state-rule candidates | Strategy #1 (citation audit) + #2 (graph gaps) |
| **Null Reference Clause** | 5 | Low–High | No validated instance; temporal evidence dependency identified | Strategy #1 (citation resolution) + #3 (temporal validity) |
| **Spec-Code Divergence** | 5 | Medium–High | None established; no paired system artifact | Strategy #2 (trace-back contract) — needs system data |

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

**Observed Candidate Signal:**
- KFBM `134870230-UW-MANUAL`: a definition repeats the term being defined before adding thresholds and exceptions. This is a literal-match candidate, not a validated defect.

**Integration Path:** Reuse definition extraction and stable provenance, but add
term nodes or explicit `definition_depends_on` edges. The current Sandbox 002
`defines_term` edges are node-to-self extraction markers; running cycle scoring
over them would falsely mark every extracted definition as circular.

---

### 2. Rule Duplication

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Textual Similarity Hashing** | MinHash/SimHash fingerprinting | Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Normalized Clause Comparison** | Structure-aware normalization | Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#3: Cross-Reference Fan-Out** | Multi-form paragraph replacement | Low-Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#4: Lineage / Version Drift** | Form-family diffing | Medium | Kentucky corpus NOW | Phase 2 |
| **#5: Exclusion / Condition Inventory** | Clause cataloging by business meaning | High | Kentucky corpus NOW | Phase 3+ |

**Observed Candidate Signals:**
- KFBM `134503212-HO-FORM-MARKUP` and ISO `HO-04-93-1000`: structurally similar roof endorsements with a seven-year condition in the KFBM markup; exact edition lineage and intent remain unvalidated. The redacted `134503212-HO-FORM` public-view artifact is not the comparison source.
- KNIC `132500003-HO-04-95`: one replacement paragraph fans out across five named forms; this proves fan-out, not five independent copies
- KFBM `134827992`: one endorsement applies appraisal and duties-after-loss changes across six forms; this is a fan-out lead, not a duplicate-cluster finding

**Integration Path:** Define a versioned Sandbox 007 clause artifact with
`normalized_text` and `clause_fingerprint`, reusing Sandbox 002's provenance
principles. Do not silently add fields to the closed Stage 002 schema or emit
new findings into preserved Stage 006 output.

---

### 3. Hardcoded Jurisdiction Logic

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Citation Audit** | Lexical scan for rules + citation presence | Low | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#2: Regulatory Traceability Gap** | Graph-based gap detection | High | **Matches Sandbox 002 Phish 5 arch** | Phase 2 |
| **#3: State-Scoped Rule Header** | Section title + imperative mining | Low-Medium | Kentucky corpus NOW | **Phase 1 (MVP)** |
| **#4: Jurisdictional Parameter-to-Authority** | Parameter crosswalk to citations | Medium | Kentucky corpus NOW | Phase 2 |
| **#5: Filing-Package Reconciliation** | Package-level legal anchor validation | Medium-High | Kentucky corpus NOW | Phase 2 |

**Observed Candidate Signals:**
- KNIC `127064322`: a state-requirements section contains endorsement instructions without a nearby KRS/KAR citation; authority may exist elsewhere in the filing package
- KFBM `134870729-RATE-MANUAL`: a mandatory endorsement instruction appears without a nearby authority citation
- KFBM manuals: rating and underwriting rules provide candidates for package-level traceability review

**Integration Path:** Reuse Phish 5 H001–H003 lexical concepts in a Sandbox 007
prototype and use typed graph gaps where lexical matching cannot establish a
missing authority relationship.

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

**Corpus Evidence:** No explicit reference has yet been validated as retired,
withdrawn, or inapplicable for the relevant policy interval. A missing local
match or `resolved: false` value is an evidence gap, not a Null Reference
finding.

---

### 5. Spec-Code Divergence

| Strategy | Method | Complexity | Applicability | Recommended Phase |
|---|---|---|---|---|
| **#1: Structural Clause-to-Rule Diff** | Policy clauses vs. system rules diff | High | Requires PAS/system artifacts | Phase 3+ |
| **#2: Trace-Back Coverage Matrix** | Policy-to-system bidirectional audit | Medium | Synthetic contract design only until paired artifacts exist | Phase 2 design / Phase 3 audit |
| **#3: Scenario Replay / Golden-Path** | Test-coverage audit + executable scenarios | High | Requires system access | Phase 3+ |
| **#4: Version-Sync Lineage Drift** | Filing/spec/config version alignment | Medium | Synthetic schema/fixture design; real comparison needs system data | Phase 2 design / Phase 3 audit |
| **#5: Outcome-Based Divergence Mining** | Claim outcome clustering audit | High | Requires operational claim data | Phase 4+ |

**Integration Path:** Strategy #2 (trace-back) and #4 (version-sync) can reuse
Sandbox 002's provenance principles to define a synthetic paired-artifact
contract. Real detection still requires a system-side comparator. Strategies
#1, #3, and #5 additionally require configuration, execution, or outcome data.

**Key Insight:** Sandbox 002 provides policy-side provenance only. No
Spec-Code Divergence instance can be claimed until a version-aligned system-side
comparator exists.

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
   - Citation extraction and current-corpus resolution mechanics, plus synthetic authority-lifecycle fixtures
   - Low-Medium complexity; real null-status validation remains Phase 2
   - Expected to produce: resolved, unresolved-evidence, and synthetic temporal-status cases without claiming a real Null Reference instance

### Phase 2: Extended Detectors (Leverage Sandbox 002 graph)

- Circular Definition (#2 + #3): Graph cycle detection with typed edges
- Rule Duplication (#4 + #5): Lineage drift + condition inventory
- Hardcoded Jurisdiction Logic (#2 + #4 + #5): Graph gaps + parameter crosswalk + package reconciliation
- Null Reference Clause (#2 + #3 + #4 + #5): Supersession + temporal + cross-ref triangulation + live-authority graph
- Spec-Code Divergence (#2 + #4): design a synthetic trace-back contract and version-sync schema; do not claim real detector coverage

### Phase 3+: System-Integration Detectors

- Spec-Code Divergence: Structural diff, scenario replay, outcome mining (requires PAS/claims data)
- Advanced Circular Definition: Semantic equivalence loops (requires richer corpus)

---

## Quick Integration Checklist

- [ ] Phase 1 MVP detectors: 4 smells with ~12 strategies total
- [ ] Define a versioned Sandbox 007 clause artifact with normalized text and fingerprints
- [ ] Reuse H004 extraction concepts for literal term-echo scoring and add term-level `definition_depends_on` edges
- [ ] Create citation resolution pipeline for H001–H003 and Phish 5
- [ ] Implement state-scoped header mining in rate/manual text
- [ ] Cluster identical clauses via similarity hashing
- [ ] Emit duplicate-cluster findings in Sandbox 007; integrate with closed Sandbox 002 output only after an explicit reopen decision
- [ ] Document candidate corpus signals, evidence status, and false-positive handling

---

## Success Metrics

**Phase 1 (MVP):**
- Detect ≥3 Circular Definition instances in KFBM manuals
- Detect ≥5 Rule Duplication clusters (KFBM/KNIC/ISO)
- Detect ≥4 Hardcoded Jurisdiction Logic instances
- Resolve ≥2 explicit citation fixtures and correctly distinguish live, unresolved-evidence, and synthetic retired-authority cases; do not claim a real Null Reference without authoritative lifecycle data

**Phase 2 (Extended):**
- Implement graph-based detectors for the 4 policy-corpus smells
- Define and validate a synthetic paired-artifact contract for Spec-Code Divergence
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
2. **False-positive tuning** (evaluate candidate corpus signals and labeled negative cases)
3. **ROI prioritization** (rank by detectability, false-positive risk, and business impact)
4. **Sandbox 007 artifact design** (define versioned prototype outputs; integrate with closed Sandbox 002 only after an explicit reopen decision)
