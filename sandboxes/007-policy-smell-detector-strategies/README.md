# Sandbox 007: Policy Smell Detector Strategies

**Status**: Active; Stage 001 complete and ready for prototype implementation  
**Started**: 2026-07-14  
**Scope**: Detection strategy development and prototyping for policy-layer code smells beyond the five operationalized Sandbox 002 smells

## Purpose

This sandbox builds on the 159-smell taxonomy and the five operationalized Kentucky homeowners policy-layer smells from Sandbox 002. It systematically develops detection strategies for additional high-value smells and prototypes implementations.

**Working thesis:**

> Five high-value policy-layer smells (Circular Definition, Rule Duplication, Hardcoded Jurisdiction Logic, Null Reference Clause, Spec-Code Divergence) have practical detection strategies that can be implemented in phases. Phase 1 MVP strategies are implementable now on the Kentucky corpus. Phase 2 strategies leverage Sandbox 002's graph architecture. Phase 3+ strategies require system-level data integration.

## Documentation and Stages

### Stage 001: Detection Strategy Development (Complete)

Five parallel agents analyzed five policy-layer smells and developed **25 detection strategies** (5 per smell).

**Deliverables:**
- `DETECTION_STRATEGY_MATRIX.md` — Unified matrix with all 25 strategies, complexity, applicability, real corpus examples, and phased roadmap
- `STAGE-001-COMPLETION.md` — Session summary documenting real corpus signals discovered
- Implementation checklist for Phase 1 MVP

**Key Findings:**
- 10+ real corpus signals discovered in Kentucky homeowners documents
- Phase 1 MVP: 4 smells, ~12 strategies, all implementable on current corpus
- Phase 2 Extended: Graph-based strategies aligned with Sandbox 002 architecture
- Phase 3+: Requires system-level data (PAS/claims)

**Real Corpus Examples:**
- Circular Definition: KFBM self-referential UW manual definition
- Rule Duplication: KFBM/ISO roof ACV duplicates with divergence; KNIC multi-form rewrites
- Hardcoded Jurisdiction Logic: KNIC/KFBM missing citations ("Special State Requirements")
- Null Reference Clause: Superseded bulletins without version control

### Stage 002: Phase 1 MVP Implementation (Ready; not started)

Implement 4 smells with ~12 recommended strategies:

1. **Circular Definition** (#1 + #4)
2. **Rule Duplication** (#1 + #2 + #3)
3. **Hardcoded Jurisdiction Logic** (#1 + #3)
4. **Null Reference Clause** (#1)

**Scope:** Test against Kentucky corpus; measure detection accuracy, false-positive rates.

### Stage 003: Phase 2 Extended Implementation (Planned)

Implement graph-based strategies for all five smells leveraging Sandbox 002's existing architecture.

### Stage 004: Phase 3 System-Integration (Planned)

Integrate Spec-Code Divergence and other system-level detectors with PAS/claims data.

### Stage 005: Cross-Smell Validation & Scaling (Planned)

Validate Phase 1–3 findings; expand to additional smell categories (claims-layer, structural, dependency).

## Key Documents

| Document | Purpose |
|---|---|
| **[DETECTION_STRATEGY_MATRIX.md](DETECTION_STRATEGY_MATRIX.md)** | Master reference; 25 strategies across 5 smells with phased roadmap and real corpus examples |
| **[STAGE-001-COMPLETION.md](STAGE-001-COMPLETION.md)** | Session summary and detailed real corpus signals |
| `stages/001-strategy-development/STAGE.md` | Stage 001 detailed results (TBD) |
| `stages/002-phase1-mvp/STAGE.md` | Phase 1 MVP implementation plan (TBD) |

## Integration with Other Sandboxes

**Sandbox 002 (Claims-Regulatory Automation):**
- Sandbox 007 builds on Sandbox 002's five operationalized Kentucky homeowners policy-layer smells
- Phase 2 strategies extend Sandbox 002's graph architecture and node/edge model
- Sandbox 007 detectors eventually feed back into Sandbox 002's Stage 006 detector pipeline

**Sandbox 001 (Legal Debt Primitives):**
- Circular Definition strategy #3 reuses Sandbox 001's typed-edge cycle detection
- Hardcoded Jurisdiction Logic strategy #2 extends Sandbox 001's graph-gap detection
- Sandbox 001's lessons on edge typing directly inform Phase 2 extended strategies

**Sandbox 003–006:**
- Findings from Sandbox 007 will populate Sandbox 003 (findings triage)
- Sandbox 004 (expert drill-down) can showcase Sandbox 007 detector findings
- Sandbox 006 (interactive workbench) can visualize Sandbox 007 strategies and findings

## Success Criteria

**Phase 1 MVP (Stage 002):**
- [ ] Detect ≥3 Circular Definition instances in KFBM manuals
- [ ] Detect ≥5 Rule Duplication clusters (KFBM/KNIC/ISO)
- [ ] Detect ≥4 Hardcoded Jurisdiction Logic instances
- [ ] Detect ≥2 Null Reference Clause citations
- [ ] Document false-positive handling
- [ ] Achieve ≥80% precision on core signals

**Phase 2 Extended (Stage 003):**
- [ ] Implement all five graph-based strategies
- [ ] Cross-validate with Sandbox 002's Phish 1–5 detectors
- [ ] Expand coverage to all five smells with medium complexity

**Phase 3+ (Stage 004):**
- [ ] Implement system-level Spec-Code Divergence detector
- [ ] Compare policy findings against PAS/claims outcomes
- [ ] Identify cross-system patterns not detectable from policy alone

## Quick Navigation

- **[DETECTION_STRATEGY_MATRIX.md](DETECTION_STRATEGY_MATRIX.md)** — Start here for all 25 strategies
- **[SMELL_TAXONOMY_INDEX.md](../../SMELL_TAXONOMY_INDEX.md)** — Full 159-smell inventory
- **[Sandbox 002 Five Phish](../002-claims-regulatory-automation/002-five-policy-layer-phish.md)** — Base layer operationalized smells
- **[Sandbox 001 Lessons](../001-legal-debt-primitives/LESSON.md)** — Reusable patterns (typed edges, graph gaps)

---

## Reusable Lessons

See `LESSON.md` (TBD) for sandbox-wide patterns and insights from this experiment.
