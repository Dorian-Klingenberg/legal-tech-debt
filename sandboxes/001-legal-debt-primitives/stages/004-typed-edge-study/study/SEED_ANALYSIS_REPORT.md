# SEED EDGE ANALYSIS REPORT
## 46 Labeled Edges from Stage 004-typed-edge-study

Generated: 2026-05-19

---

## EXECUTIVE SUMMARY

**Total edges labeled: 46**
**Edge types represented: 13**
**Confidence distribution:**
- High: 40 edges (87%)
- Medium: 6 edges (13%)
- Low: 0 edges (0%)

**Key finding: The taxonomy is largely stable, but exhibits three refinement opportunities:**
1. Authority-checking types (validates_against, proof_requirement, reporting_requirement) need clearer separation
2. Evidence handling (requires_evidence vs records_retention) conflates two different legal meanings
3. Weak types: coordinates_with (1 edge, uncertain), cites_authority (1 edge, uncertain)

---

## TYPE DISTRIBUTION

### Tier 1: Heavily Used (>5 edges)
- **workflow_handoff** (8 edges) - Routes work between internal sections
- **implements_authority** (6 edges) - Internal policy operationalizes external rule

### Tier 2: Common (3-4 edges each)
- **validates_against** (4 edges) - Check/verification against authority
- **stale_reference** (4 edges) - Dangling/obsolete citations
- **review_loop** (4 edges) - Loopback for reopening/audit
- **requires_evidence** (4 edges) - Dependency on evidence/records
- **notice_requirement** (4 edges) - Dependency on notice content

### Tier 3: Present (2-3 edges)
- **records_retention** (3 edges) - Recordkeeping duty from authority
- **exception_process** (3 edges) - Non-standard path handling
- **reporting_requirement** (2 edges) - Reporting to regulator
- **proof_requirement** (2 edges) - Proof-of-insurance requirement

### Tier 4: Rare/Problematic (<2 edges)
- **coordinates_with** (1 edge, medium confidence, review) - TOO VAGUE
- **cites_authority** (1 edge, medium confidence) - UNDERUTILIZED COMPARED TO implements_authority

---

## CONFIDENCE ANALYSIS

**8 edges are not 'high' confidence:**

| Edge | Type | Conf | Issue | Note |
|------|------|------|-------|------|
| E006 | workflow_handoff | medium | Early classification edges | Weak routing signal |
| E007 | workflow_handoff | medium | Early classification edges | Weak routing signal |
| E021 | cites_authority | medium | Background reference to UM law | Could be implements_authority? |
| E023 | implements_authority | medium | Template reconciliation | Partial implementation? |
| E024 | coordinates_with | medium | REVIEW | Should this be implements_authority or requires_evidence? |
| E028 | notice_requirement | medium | Privacy notice | Weaker than substantive notices |
| E032 | requires_evidence | medium | Recordkeeping authority inclusion | Could be records_retention? |
| E035 | records_retention | medium | Applicant disclosure storage | Borderline evidence vs retention |

**Critical ambiguity: E024 (coordinates_with) is uncertain, suggesting the type needs refinement.**

---

## SEMANTIC PATTERNS

### Authority-Target Pattern
**All authority-checking types point to statute/regulation sections (304.*, 806.*):**
- implements_authority: 6/6 to statute
- validates_against: 4/4 to statute
- notice_requirement: 4/4 to statute
- records_retention: 3/3 to statute
- reporting_requirement: 2/2 to statute
- proof_requirement: 2/2 to statute

**Insight: These types are clearly distinguished by legal domain, not just semantics.**

### Internal Workflow Pattern
**All workflow types point to internal sections (1000+):**
- workflow_handoff: 8/8 internal
- review_loop: 4/4 internal
- coordinates_with: 1/1 internal
- exception_process: 2/3 internal (1 to statute)

**Insight: Workflow is entirely internal. But exception_process has a statute reference—possible type split?**

### Evidence Handling
**Requires_evidence and records_retention both deal with evidence but have different meanings:**
- requires_evidence: Points to internal steps that provide evidence (3/4 internal)
- records_retention: Points to authorities that create recordkeeping duties (3/3 statute)

**Insight: These are semantically inverse. Requires_evidence says "I need evidence FROM X." Records_retention says "I must record because X requires it."**

---

## REACHABILITY CLARITY

**100% consistency: Each type has a single reachability mode across all its instances.**

- 11 types marked as 'live'
- 1 type (review_loop) marked as 'visible_only'
- 1 type (stale_reference) marked as 'exclude'

**No type has split reachability modes. Framework is semantically coherent.**

---

## GAPS & CONTRADICTIONS FOUND

### 1. **cites_authority is underutilized** (1 edge)
- Only E021 uses it, marked medium confidence
- Current framework distinguishes: cites_authority, implements_authority, validates_against
- But data shows implements_authority dominates (6 vs 1)
- **Question: Is cites_authority needed, or should it merge with implements_authority?**
- **Recommendation: Either delete or clarify the difference. Currently confusing.**

### 2. **coordinates_with is too vague** (1 edge, uncertain)
- E024: "Template updates reconcile with proof validation workflow"
- Marked medium confidence + review reachability
- Doesn't fit existing types cleanly
- **Question: Is this bidirectional implements_authority? Or a new "bidirectional_dependency" type?**
- **Recommendation: Eliminate. Reframe as directional implements_authority or requires_evidence.**

### 3. **exception_process mixes two patterns**
- E037, E038: Internal process when ordinary processing fails
- E013: "Electronic reporting failure invokes the exception path" (points to statute)
- **Question: Should exception_process split into exception_handling (internal) and exception_authority (statute)?**
- **Recommendation: Likely should split. Exception authority is different from exception workflow.**

### 4. **Proof_requirement vs reporting_requirement unclear**
- E011, E030: proof_requirement (2 edges) - "compares records" and "uses printed card details"
- E012, E017: reporting_requirement (2 edges) - "checks electronic reporting" and "checks termination reporting"
- **Question: Are these two distinct concepts or one "regulatory_check" type?**
- **Recommendation: Keep separate but clarify: proof_requirement = compliance with proof rules; reporting_requirement = compliance with reporting obligations.**

### 5. **Notice_requirement is broad**
- Covers: cancellation notice (E016, E025), adverse action (E027), privacy notice (E028)
- All are compliance notices, but different legal significance
- **Question: Should notice_requirement split by notice type?**
- **Recommendation: Probably not. All are notice-type compliance dependencies. E028 (privacy) should be high confidence too.**

### 6. **requires_evidence vs records_retention are semantically inverse**
- requires_evidence: "Letter content depends on evidence packet" (E029)
- records_retention: "Retention preserves records supporting reparations decisions" (E040)
- **Question: Should they be unified?**
- **Recommendation: Keep separate but clarify semantics. Requires_evidence = "needs evidence as input." Records_retention = "must preserve evidence as output."**

---

## VALIDATION OPPORTUNITIES

### High Confidence Edges (40/46) - Validated ✓
- All major types represented
- Framework captures real distinctions
- No false positives detected

### Medium Confidence Edges (6/46) - Need Refinement
- E006, E007: workflow_handoff early in routing (weak signals → possible early_routing type?)
- E021: cites_authority vs implements_authority boundary
- E023: partial implements_authority (template vs full implementation)
- E024: coordinates_with boundary (needs framework elimination or clarification)
- E028: privacy notice vs operational notice (should be high confidence)
- E032, E035: evidence vs retention boundary (clear semantics exist)

### Completely Stale (4 edges) - Perfect Detection ✓
- E034, E044, E045, E046 all stale_reference (3-4 to invalid targets)
- Framework catches structural defects reliably

---

## RECOMMENDATIONS FOR TAXONOMY REFINEMENT

### Phase 1: Eliminate Weak Types
1. **Delete `cites_authority`** (1 edge, redundant with implements_authority)
   - Merge E021 into implements_authority with note "background reference"
   
2. **Delete `coordinates_with`** (1 edge, too vague)
   - Merge E024 into implements_authority or requires_evidence
   - Decision: Is template updates about "implementing" the other workflow or "requiring evidence from" it?
   - Likely: requires_evidence (template needs proof validation output)

### Phase 2: Clarify Boundary Types
3. **Refine `exception_process`** (3 edges, 2 internal + 1 statute)
   - Separate into: exception_handling (internal) and exception_authority (statute reference)
   - E013 becomes exception_authority
   - E037, E038 remain exception_handling
   
4. **Sharpen `proof_requirement` vs `reporting_requirement`**
   - proof_requirement: Dependencies on proof-of-insurance rules
   - reporting_requirement: Dependencies on regulatory reporting rules
   - Keep both but make definitions more distinct in framework
   - E030 (printed card) is squarely proof_requirement ✓
   - E012, E017 are squarely reporting_requirement ✓

5. **Clarify `notice_requirement`**
   - Add note: Covers all notice types (cancellation, adverse action, privacy)
   - Bump E028 confidence from medium to high (privacy notice is still a compliance requirement)

6. **Separate `requires_evidence` and `records_retention` semantics**
   - requires_evidence: "Source depends on target to provide/supply evidence"
   - records_retention: "Source must retain/preserve records because target requires it"
   - E032, E035 ambiguity should resolve when semantics are clear
   - E032: "Evidence packet includes source excerpts" = requires_evidence ✓
   - E035: "Intake stores disclosure election described by target" = records_retention ✓

### Phase 3: After Refinement
7. **Relabel uncertain edges with new taxonomy**
8. **Update EDGE_TYPE_FRAMEWORK.md** with:
   - Clearer definitions for remaining 11 types
   - Explicit decision tree for borderline cases
   - Better path composition rules for typed closure

---

## SUMMARY STATS

| Metric | Value | Insight |
|--------|-------|---------|
| Total edges | 46 | Good coverage |
| Type count | 13 | Should reduce to ~11 |
| High confidence | 40 (87%) | Solid labeling |
| Types fully consistent | 13/13 (100%) | No split reachability modes |
| Types with 1 edge | 2 | Candidates for removal |
| Internal-only types | 4 | Workflow is separate domain |
| Statute-only types | 6 | Authority is separate domain |
| Stale edge detection | 100% | Perfect precision |

---
