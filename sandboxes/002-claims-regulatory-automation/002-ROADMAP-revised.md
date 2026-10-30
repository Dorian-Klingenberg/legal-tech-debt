# Sandbox 002 Roadmap (Revised): Five Policy-Layer Phish for Kentucky Homeowners

*Version 3.0 — June 2026*

This is the active Sandbox 002 roadmap. It narrows near-term execution to **Kentucky homeowners** and the **five policy-layer phish** workstream.

---

## Scope and Operating Constraints

- Active sandbox: **Sandbox 002**
- Active domain: **Kentucky homeowners insurance**
- Active layer: **policy/rate/rule text and references**, not broad claims-platform automation
- Delivery style: **lightweight, explainable, fixture-first prototypes**
- Out of scope unless explicitly reopened: personal auto, motor vehicle, no-fault, PIP, heavy infrastructure, and premature productization

---

## Phase 0: Lock Inputs and Detector Contracts (Week 0–1)

**Objective**: Make the five-phish plan executable with concrete fixtures and detector contracts.

### Deliverables

1. **KY homeowners fixture pack (small, explicit)**
   - Forms + endorsements
   - Rate/rule excerpts
   - KY legal references used for citation checks
2. **Detector contracts for all five phish**
   - signal patterns
   - minimum required inputs
   - explainable output schema
3. **Phase 1 implementation ordering**
   - choose the first two detector passes from the five-phish set

### Success Criteria

- ✅ Fixture pack is reproducible and documented
- ✅ Detector contracts are clear enough to implement without architecture expansion
- ✅ Phase 1 ordering is explicitly justified

---

## Phase 1: First Two Detector Passes (Weeks 1–4)

**Objective**: Ship two high-value, explainable detector prototypes against the KY fixture.

### Recommended first implementation targets

1. **Regulatory Mapping + Broken/Null Reference pass (Phish 5)**
   - detect generic legal references without concrete KY anchors
   - detect null internal references and obvious stale external references
2. **Calculation Rule Drift / Unversioned Rate Reference pass (Phish 4)**
   - flag unversioned "current manual/current guideline" references
   - flag opaque calculation language lacking explicit formula/version anchors

### Outputs

- `findings.json` (typed findings by phish and severity)
- `report.md` (human-readable explanation with clause snippets and trigger rationale)
- fixture-level evidence tables (CSV/Markdown) for traceability

### Success Criteria

- ✅ Both passes run deterministically on the KY fixture
- ✅ Findings are traceable to explicit text evidence
- ✅ Reviewer can understand each flag without opaque model behavior

---

## Phase 2: Complete Five-Phish Coverage (Weeks 5–8)

**Objective**: Add the remaining three policy-layer phish as incremental detectors.

### Added detectors

3. Overbroad / Non-deterministic Exclusions (Phish 1)  
4. Magic Number / Magic Valuation Terms (Phish 2)  
5. Coverage Inversion / Contradictory Conditions (Phish 3)

### Success Criteria

- ✅ All five phish have executable detector logic on the KY fixture
- ✅ Output format is consistent across all detectors
- ✅ False-positive notes and known limits are documented per detector

---

## Phase 3: Calibration and Hardening (Weeks 9–12)

**Objective**: Improve quality and explainability before any broader expansion.

### Deliverables

1. **Calibration pass**
   - tune rules based on fixture review feedback
2. **Detector runbook**
   - how to run, interpret, and review findings
3. **Prioritized next-step backlog**
   - candidate enhancements that preserve lightweight sandbox constraints

### Success Criteria

- ✅ Meaningful false-positive reduction on fixture re-runs
- ✅ Detector behavior is stable across repeated runs
- ✅ Next-step backlog is scoped as small prototype increments
- ✅ Go/no-go: expand fixture breadth only if explainability and stability remain strong

---

## Decision Gates

**After Phase 0**: Are fixtures and detector contracts clear enough to avoid infrastructure creep?  
**After Phase 1**: Do the first two passes produce actionable, explainable findings?  
**After Phase 2**: Do all five phish produce coherent policy-layer insights on KY fixtures?  
**After Phase 3**: Is detector quality high enough to justify expanding fixtures or scope?

---

## Related Documents

- [002-claims-regulatory-automation-README.md](002-claims-regulatory-automation-README.md)
- [002-five-policy-layer-phish.md](002-five-policy-layer-phish.md)
- [002-PAIN-POINTS-TAXONOMY.md](002-PAIN-POINTS-TAXONOMY.md)
- [002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md](002-KENTUCKY-INSURANCE-DATA-PROCUREMENT.md)
