# Sandbox 007: Policy Smell Detector Strategies

**Status**: Active; Stage 001 complete and ready for prototype implementation
**Started**: 2026-07-14
**Scope**: Detection strategy development and prototyping for policy-layer code smells beyond the five operationalized Sandbox 002 smells

## Purpose

This sandbox builds on the 159-smell taxonomy and the five operationalized Kentucky homeowners policy-layer smells from Sandbox 002. It systematically develops detection strategies for additional high-value smells and prototypes implementations.

**Working thesis:**

> Five high-value policy-layer smells (Circular Definition, Rule Duplication, Hardcoded Jurisdiction Logic, Null Reference Clause, Spec-Code Divergence) have candidate detection strategies that can be evaluated in phases. The current policy corpus supports Phase 1 prototyping for the first four, with different evidence limits. Spec-Code Divergence requires a versioned policy-to-system comparator and cannot be established from the current corpus.

## Documentation and Stages

### Stage 001: Detection Strategy Development (Complete)

Five parallel agents analyzed five policy-layer smells and developed **25 detection strategies** (5 per smell).

**Deliverables:**
- `DETECTION_STRATEGY_MATRIX.md` — Unified matrix with all 25 strategies, complexity, applicability, candidate corpus signals, evidence boundaries, and phased roadmap
- `STAGE-001-COMPLETION.md` — Session summary documenting candidate corpus signals and evidence limits
- Implementation checklist for Phase 1 MVP

**Key Findings:**
- Candidate corpus signals identified for Circular Definition, Rule Duplication, and Hardcoded Jurisdiction Logic
- Null Reference Clause has a defined authority-lifecycle validation path but no confirmed corpus instance
- Spec-Code Divergence has no paired system-side evidence in the current corpus
- Phase 1 MVP: 4 smells, ~12 strategies, all implementable on current corpus
- Phase 2 Extended: Graph-based strategies aligned with Sandbox 002 architecture
- Phase 3+: Requires system-level data (PAS/claims)

**Candidate Corpus Signals:**
- Circular Definition: KFBM term-echo candidate in an underwriting manual
- Rule Duplication: KFBM/ISO roof-form comparison candidate and KNIC/KFBM multi-form fan-out
- Hardcoded Jurisdiction Logic: KNIC/KFBM state-scoped rule candidates without nearby citations
- Null Reference Clause: authority versioning and archive dependencies; no instance validated

### Stage 002: Phase 1 MVP Implementation (Ready; not started)

Implement 4 smells with ~12 recommended strategies:

1. **Circular Definition** (#1 + #4)
2. **Rule Duplication** (#1 + #2 + #3)
3. **Hardcoded Jurisdiction Logic** (#1 + #3)
4. **Null Reference Clause** (#1)
   - Phase 1 covers extraction/current-corpus resolution mechanics and synthetic authority-lifecycle fixtures
   - Real null-status validation requires authoritative current and archival sources in Phase 2

**Scope:** Test the first three detectors against the Kentucky corpus. Exercise
Null Reference extraction and current-corpus resolution with labeled synthetic
lifecycle fixtures, and measure that classifier separately from real-corpus
detector precision.

### Stage 003: Phase 2 Extended Implementation (Planned)

Implement graph-based strategies for the four policy-corpus smells and design a synthetic, versioned specification-to-configuration traceability contract for Spec-Code Divergence. Reuse Sandbox 002's identity and evidence patterns without treating its current definition self-loops or closed schemas as ready-made semantic relationships.

### Stage 004: Phase 3 System-Integration (Planned)

Evaluate Spec-Code Divergence only after paired PAS/configuration artifacts are explicitly authorized and version-aligned. Claims or outcome data is a later evidence layer, not a prerequisite for a static spec-to-rule comparison.

### Stage 005: Cross-Smell Validation & Scaling (Planned)

Validate Phase 1–3 findings; expand to additional smell categories (claims-layer, structural, dependency).

## Key Documents

| Document | Purpose |
|---|---|
| **[DETECTION_STRATEGY_MATRIX.md](DETECTION_STRATEGY_MATRIX.md)** | Master reference; 25 strategies across 5 smells with phased roadmap, candidate signals, and evidence boundaries |
| **[STAGE-001-COMPLETION.md](STAGE-001-COMPLETION.md)** | Session summary, candidate corpus signals, and evidence limits |
| `stages/001-strategy-development/STAGE.md` | Stage 001 detailed results (TBD) |
| `stages/002-phase1-mvp/STAGE.md` | Phase 1 MVP implementation plan (TBD) |

## Integration with Other Sandboxes

**Sandbox 002 (Claims-Regulatory Automation):**
- Sandbox 007 builds on Sandbox 002's five operationalized Kentucky homeowners policy-layer smells
- Phase 2 strategies extend Sandbox 002's graph architecture and node/edge model
- Sandbox 007 may reuse preserved Sandbox 002 artifacts or define versioned downstream extensions; feeding detectors back into the closed Stage 006 pipeline requires an explicit Sandbox 002 reopen decision

**Sandbox 001 (Legal Debt Primitives):**
- Circular Definition strategy #3 reuses Sandbox 001's typed-edge cycle detection
- Hardcoded Jurisdiction Logic strategy #2 extends Sandbox 001's graph-gap detection
- Sandbox 001's lessons on edge typing directly inform Phase 2 extended strategies

**Sandbox 003–006:**
- Reuse Sandbox 003's triage patterns in new Sandbox 007 outputs; do not write into the completed Sandbox 003 artifacts without an explicit reopen decision
- Reuse Sandbox 004's drill-down patterns for new Sandbox 007 artifacts; keep the completed Sandbox 004 outputs preserved
- Reuse Sandbox 006's workbench patterns in a separately scoped follow-on; do not mutate its review-gated output implicitly

## Success Criteria

**Phase 1 MVP (Stage 002):**
- [ ] Detect ≥3 Circular Definition instances in KFBM manuals
- [ ] Detect ≥5 Rule Duplication clusters (KFBM/KNIC/ISO)
- [ ] Detect ≥4 Hardcoded Jurisdiction Logic instances
- [ ] Resolve ≥2 explicit Null Reference citation fixtures and distinguish live, unresolved-evidence, and synthetic retired-authority cases
- [ ] Document false-positive handling
- [ ] Achieve ≥80% precision on the first three corpus detectors; measure Null Reference lifecycle classification separately on labeled fixtures

**Phase 2 Extended (Stage 003):**
- [ ] Implement graph-based strategies for the four policy-corpus smells
- [ ] Define a synthetic, versioned spec-to-config traceability contract for Spec-Code Divergence
- [ ] Cross-validate with Sandbox 002's Phish 1–5 detectors
- [ ] Keep real Spec-Code Divergence coverage gated on paired system artifacts

**Phase 3+ (Stage 004):**
- [ ] Implement system-level Spec-Code Divergence detector
- [ ] Compare policy findings against PAS/claims outcomes
- [ ] Identify cross-system patterns not detectable from policy alone

## Quick Navigation

- **[DETECTION_STRATEGY_MATRIX.md](DETECTION_STRATEGY_MATRIX.md)** — Start here for all 25 strategies
- **[SMELL_TAXONOMY_INDEX.md](../../SMELL_TAXONOMY_INDEX.md)** — Full 159-smell inventory
- **[Sandbox 002 Five Phish](../002-claims-regulatory-automation/002-five-policy-layer-phish.md)** — Base layer operationalized smells
- **[Sandbox 001 Typed-Edge Lesson](../001-legal-debt-primitives/stages/004-typed-edge-study/LESSON.md)** — Reusable typed-edge and witness-path patterns

---

## Reusable Lessons

See the [five smell-specific detector-design lessons](lessons/README.md).
Their examples are synthetic, and each lesson distinguishes observed evidence,
inherited engineering evidence, and proposed work that Stage 002 has not yet
validated.
