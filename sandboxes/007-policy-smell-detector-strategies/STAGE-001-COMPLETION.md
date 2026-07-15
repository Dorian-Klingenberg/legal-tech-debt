# Stage 001 Completion: Detection Strategy Development

**Completed**: 2026-07-14
**Status**: Complete — ready for Phase 1 MVP implementation (Stage 002)

## What Was Done

Five parallel background agents analyzed five policy-layer smells and developed **25 detection strategies** (5 per smell).

### Agents and Smells

| Agent | Smell | Strategies | Status |
|---|---|---|---|
| agent-circular-definition | Circular Definition | 5 | ✅ Complete |
| agent-rule-duplication | Rule Duplication | 5 | ✅ Complete |
| agent-hardcoded-jurisdiction | Hardcoded Jurisdiction Logic | 5 | ✅ Complete |
| agent-null-reference | Null Reference Clause | 5 | ✅ Complete |
| agent-spec-code-divergence | Spec-Code Divergence | 5 | ✅ Complete |
| **Total** | **5 smells** | **25 strategies** | ✅ **Complete** |

---

## Key Findings

### Candidate Corpus Signals And Evidence Boundaries

Stage 001 was a strategy-development pass, not a detector evaluation. Direct
inspection supports candidate signals for Circular Definition, Rule
Duplication, and Hardcoded Jurisdiction Logic. Null Reference Clause still
requires live-authority and temporal validation. Spec-Code Divergence cannot be
established because the corpus has no paired PAS or configuration artifact.

#### Circular Definition
- **KFBM `134870230-UW-MANUAL.pdf`**: a definition repeats the term being defined before adding thresholds and exceptions; this is a lexical candidate, not a validated defect
- **Sandbox 001 lesson reused**: Edge typing is critical; plain cycles miss context

#### Rule Duplication
- **KFBM `134503212-HO-FORM-MARKUP.pdf` vs. ISO `HO-04-93-1000-ROOF-ACV-ENDORSEMENT.pdf`**: structurally similar roof loss-settlement forms with a seven-year condition in the KFBM markup; exact edition lineage and intent remain unvalidated. The redacted `134503212-HO-FORM.pdf` public-view artifact is not the comparison source.
- **KNIC `132500003-HO-04-95.pdf`**: one replacement paragraph applies across **HO 00 03, HO 00 05, HO 05 24, HO 17 31, HO 17 32**; this proves fan-out, not inconsistent independent copies
- **KFBM `134827992-ENDORSEMENT.pdf`**: one endorsement applies appraisal and duties-after-loss changes across **six HO forms**; this is a maintenance-surface lead, not a duplicate-cluster result

#### Hardcoded Jurisdiction Logic
- **KNIC `127064322`**: a state-requirements section uses mandatory and endorsement instructions without a nearby KRS/KAR citation; package-level authority resolution remains open
- **KFBM `134870729-RATE-MANUAL-HOP2-1`**: a mandatory endorsement instruction and an external construction-cost index appear without nearby Kentucky authority references
- **KFBM underwriting/rate manuals**: rating factors and premium computation rules provide package-level traceability candidates, not noncompliance findings

#### Null Reference Clause
- **No validated instance yet**: the current extractor does not resolve official authority identity, supersession, or effective intervals
- **Known version gaps**: corpus and SERFF acquisition records show why archive and temporal metadata are required, but missing or superseded source material is not itself a Null Reference Clause

#### Spec-Code Divergence
- No instance can be established from the policy-only corpus because no PAS/configuration comparator is present
- Stage 001 produced five comparison strategies and identified the missing paired-artifact contract for future system-integration phases

---

## Phase 1 MVP: Immediate Implementation Readiness

Four smells with ~12 recommended strategies are ready for Phase 1 MVP implementation (Stage 002):

### Implementation-Ready Strategies

1. **Circular Definition**
   - Strategy #1: **Literal self-reference detector** (Low complexity)
   - Strategy #4: **Package-completeness + broken-definition-loop** (Medium complexity)
   - **Candidate signal expectation**: HIGH (one literal-match candidate inspected; evaluation pending)

2. **Rule Duplication**
   - Strategy #1: **Textual Similarity Hashing** (Medium complexity)
   - Strategy #2: **Normalized Clause Comparison** (Medium complexity)
   - Strategy #3: **Cross-Reference Fan-Out Detector** (Low-Medium complexity)
   - **Candidate signal expectation**: HIGH (lineage, delta, and fan-out candidates inspected; cluster validation pending)

3. **Hardcoded Jurisdiction Logic**
   - Strategy #1: **Citation Audit** (Low complexity)
   - Strategy #3: **State-Scoped Rule Header Mining** (Low-Medium complexity)
   - **Candidate signal expectation**: HIGH (multiple state-scoped rule candidates inspected; package resolution pending)

4. **Null Reference Clause**
   - Strategy #1: **Regulatory Citation Resolution** (Low-Medium complexity)
   - **Candidate signal expectation**: MEDIUM (reference records exist, but no null-reference instance is validated)

---

## Phase 2 & 3: Extended and System-Integration

All agents identified phase-2 and phase-3 strategies leveraging:
- **Sandbox 002's graph architecture** (typed edges, gap detection)
- **Sandbox 001's lessons** (edge typing, witness paths, cycle detection)
- **System-level data** (PAS rules, claim outcomes, filing timelines)

### Phase 2 Integration Points with Sandbox 002

| Strategy Family | Alignment with Sandbox 002 |
|---|---|
| Graph-based cycle detection | Extends Sandbox 001 circular-reference logic to **definition edges** |
| Regulatory traceability gaps | Extends Phish 5 (H001–H003) to **graph-based live-authority detection** |
| Filing-package reconciliation | Uses Sandbox 002's **package-level evidence model** |
| Version-sync lineage | Aligns with Sandbox 002's **stable IDs and version awareness** |

---

## Blockers & Constraints

✅ **No known blocker to beginning Phase 1 prototype work.** No precision,
recall, or finding-count target has yet been validated.

The Circular Definition, Rule Duplication, and Hardcoded Jurisdiction Logic
prototypes can begin on the current Kentucky homeowners corpus without new
procurement or system artifacts. Null Reference Phase 1 is limited to citation
extraction, current-corpus resolution mechanics, and synthetic lifecycle
fixtures. Validating a real Null Reference finding requires authoritative
current and archival status data in a later step.

⚠️ **Constraints for Phase 2+:**
- Phase 2 needs a versioned Sandbox 007 artifact contract; integrating into closed Sandbox 002 outputs requires an explicit reopen decision
- Phase 3 real Spec-Code comparison requires PAS/configuration artifacts not currently available; claims data is a later outcome-evidence layer

---

## Integration with Sandbox 002

**Potential integration (Sandbox 007 → Sandbox 002):**
- Phase 1–2 prototypes should emit versioned Sandbox 007 findings first
- Feeding new detectors into the preserved **Sandbox 002 Stage 006 detector pipeline** requires an explicit Sandbox 002 reopen decision

**Downward leverage (Sandbox 002 → Sandbox 007):**
- Reuse Sandbox 002's existing **source/node/edge substrate**
- Define versioned Sandbox 007 clause artifacts with **clause fingerprinting** and **normalized text**, reusing Sandbox 002 provenance without silently extending its closed schema
- Leverage Stage 006 **finding emission and confidence scoring**

---

## Success Metrics (Phase 1 MVP Expectations)

**Baseline expectations for Stage 002 prototype:**

| Smell | Target Detections | Success Threshold | Observed Evidence Boundary |
|---|---|---|---|
| Circular Definition | ≥3 instances | ≥80% precision | One literal term-echo candidate; defect status unvalidated |
| Rule Duplication | ≥5 clusters | ≥80% precision | Structural, delta, and fan-out candidates; independent duplicates unvalidated |
| Hardcoded Jurisdiction Logic | ≥4 instances | ≥80% precision | State-scoped rule candidates; package-level authority unresolved |
| Null Reference Clause | ≥2 explicit citation fixtures | ≥70% correct lifecycle classification on a labeled synthetic/current set | No validated real instance; authoritative archive lookup required |

---

## Deliverables

### Sandbox 007 Documents

1. **README.md** — Sandbox overview, scope, stages, integration points
2. **DETECTION_STRATEGY_MATRIX.md** — Master reference: all 25 strategies with complexity, applicability, candidate signals, evidence boundaries, and phased roadmap
3. **STAGE-001-COMPLETION.md** — This document: strategy results, candidate signals, readiness assessment, and limitations
4. **lessons/README.md** — Five evidence-labeled, smell-specific detector-design lessons with synthetic examples

### Repository Documentation Updates

- **SMELL_TAXONOMY_INDEX.md** — New master landing page for all 159 smells
- **BOOTSTRAP.md** — Updated Documentation Map with all three smell taxonomies
- **README.md** — Added smell inventory to Completed Evidence section
- **legal_code_smell_taxonomy.md**, **insurance_policy_smells.md**, **insurance_claims_smells.md** — Added cross-taxonomy reference tables

---

## Next Steps (Stage 002: Phase 1 MVP Implementation)

### Immediate Tasks

- [ ] Review DETECTION_STRATEGY_MATRIX.md with implementation team
- [ ] Assign prototype development to agent(s) or team member
- [ ] Create Stage 002 implementation plan with timeline and resource allocation

### Implementation Plan

1. **Circular Definition detectors** (#1 + #4)
   - Reuse SMELL2-H004 definition-extraction concepts in a Sandbox 007 prototype
   - Add term nodes or `definition_depends_on` edges rather than scoring the current `defines_term` self-loops
   - Add literal term-echo scoring and package-completeness validation
   - Test against KFBM manuals

2. **Rule Duplication detectors** (#1 + #2 + #3)
   - Implement versioned Sandbox 007 clause fingerprinting and normalization
   - Build cross-reference fan-out detection
   - Test against KFBM/KNIC forms and endorsements

3. **Hardcoded Jurisdiction Logic detectors** (#1 + #3)
   - Citation audit pipeline for rate/underwriting rule text
   - State-scoped header mining
   - Test against KNIC/KFBM manuals

4. **Null Reference Clause detector** (#1)
   - Citation resolution and validation
   - Test against named bulletins and SERFF references

### Success Validation

- [ ] Execute Phase 1 MVP detectors on Kentucky corpus
- [ ] Measure precision and recall on a labeled set of positive and negative cases
- [ ] Document false-positive patterns and mitigation strategies
- [ ] Prepare Phase 2 roadmap with graph-based strategies

---

## Key Reusable Insights

These are formalized, with evidence limits, in the
[Sandbox 007 lesson catalog](lessons/README.md).

1. **Textual similarity + normalization** generates Rule Duplication candidates; verified lineage and material divergence make them actionable.
2. **Typed graph relationships** are required for semantic cycles and missing-authority gaps; generic edges and current definition self-loops are insufficient.
3. **Package-level reconciliation** is required before escalating an absent inline citation or unresolved reference.
4. **The current evidence is uneven**: three smells have observed candidate signals, Null Reference needs authority-lifecycle validation, and Spec-Code Divergence has no system-side comparator.
5. **Phased complexity** supports bounded prototyping only when projected counts and precision remain labeled as future targets.

---

## Session History

- **2026-07-14 18:33**: Planning began; discovered 80+ code smells → identified 159 total
- **2026-07-14 18:39**: Five agents launched in parallel for strategy development
- **2026-07-14 18:41**: All five agents completed; 25 strategies consolidated into matrix
- **2026-07-14 18:54**: Sandbox 007 created with matrix and completion documentation

**Total duration**: ~21 minutes from planning to Sandbox 007 handoff.

---

## Recommended Reading Order

1. **[DETECTION_STRATEGY_MATRIX.md](DETECTION_STRATEGY_MATRIX.md)** — All 25 strategies and evidence boundaries
2. **[lessons/README.md](lessons/README.md)** — Five reusable detector-design lessons
3. **[README.md](README.md)** — Sandbox context and integration points
4. **[SMELL_TAXONOMY_INDEX.md](../../SMELL_TAXONOMY_INDEX.md)** — Full 159-smell landscape
5. **[Sandbox 002 Phish Specs](../002-claims-regulatory-automation/002-five-policy-layer-phish.md)** — Base layer (five operationalized smells)
6. **[Sandbox 001 Typed-Edge Lesson](../001-legal-debt-primitives/stages/004-typed-edge-study/LESSON.md)** — Reusable patterns for typed graph strategies
