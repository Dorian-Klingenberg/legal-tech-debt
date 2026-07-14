# Stage 001 Human Review Notes

> Historical validation set: these notes review Sandbox 003's 35-finding June 4 snapshot. The canonical current Stage 006 output contains 31 findings after four regulatory-layer Smell 3 false positives were removed.

Reviewer: Dorian Klingenberg  
Date: 2026-06-04  
Sample reviewed: all 35 findings  
Purpose: Validate LLM severity ratings and flag miscategorizations before Stage 002

---

## Smell 1 — Overbroad / Non-deterministic Exclusions (1 finding)

### s1-0001 — SMELL1-H002 — LOW confidence — LLM: HIGH
**Reassessment: FALSE POSITIVE / MISCATEGORIZED**  
Evidence text is from a "Your Duties After Loss" notice provision (KFBM endorsement HO FB 01 07 26), not a coverage exclusion. The phrase "any claim" triggered H002 but the context is a late-notice condition, not an exclusion. The provision sets a one-year reporting deadline; "this policy shall provide no coverage" is the consequence of late notice, not an overbroad exclusion scope.  
**Action:** Flag as false positive. Underlying structural issue tracked in BACKLOG-006 — Smell 1 detectors fire identically on exclusions, conditions with coverage consequences, and coverage grants. Fix requires node-level language context annotation, not provision-type filtering.

---

## Smell 2 — Magic Number / Magic Valuation Terms (17 findings)

### Group A: "Replacement Cost" undefined — H003 (s2-0003 through s2-0007, s2-0010, s2-0011, s2-0015, s2-0016)
**Reassessment: REAL — but may be Smell 4 (Unversioned Rate Reference) more than Smell 2**  
Replacement cost is often pulled from an external source (e.g., Xactimate, CoreLogic) at time of policy issuance. If the carrier uses such a tool but does not reference it in the filing, the term is not undefined per se — it is externally defined but untraceable from the filing. The finding is real, but the category may be wrong: this is a traceability / unversioned-reference gap (Smell 4) rather than an undefined magic term (Smell 2).  
**Severity: HIGH remains appropriate** given that ACV vs. replacement cost is one of the most litigated areas in homeowners claims and the methodology is not visible in the filing.  
**Action:** In Stage 002/003 output, note that "replacement cost" findings may indicate an external calculation source that is not cited — recommend verifying whether the carrier's filed rate manual or endorsement references a valuation tool.

### Group B: "Reasonable time" undefined — H001 (s2-0008, s2-0009, s2-0013, s2-0014, s2-0017, s2-0018)
**Reassessment: REAL — but severity may be overstated**  
All six findings are in roof surfacing / windstorm-or-hail loss settlement conditions. "Reasonable time" controls whether a loss is settled at replacement cost or ACV — a direct payment impact. However, "reasonable time" may be defined in Kentucky statute or regulation (KRS/KAR), in which case the carrier can rely on that definition without restating it and these findings would be low severity.  
**Severity: MEDIUM** pending a KRS/KAR cross-reference check. If no statutory definition exists, HIGH is appropriate.  
**Action:** Add to pipeline backlog — check whether KRS or KAR defines "reasonable time" for property claims settlement. Until confirmed, flag as MEDIUM in report.

### Finding s2-0002: "Market value" in underwriting eligibility criteria — H003
**Reassessment: LOW — different risk category**  
"Market value" appears in a description of favorable underwriting characteristics ("Located in stable or improving area with favorable impact on market value"), not in a claims payment or loss settlement context. This is an underwriting eligibility signal assessed at time of application, not a term that drives claim payment calculations. Not a claims-layer smell.  
**Severity: LOW**

### Finding s2-0003: "Replacement Cost" in special state requirements endorsement list — H003
**Reassessment: FALSE POSITIVE**  
Evidence text is a table of required endorsements (Section 210, KNIC). "Replacement Cost" appears as part of an endorsement name ("Personal Property Replacement Cost - HO 04 90"), not as a valuation term requiring definition. No actionable finding here.  
**Severity: FALSE POSITIVE**

---

---

## Smell 3 — Coverage Inversion / Contradictory Conditions (4 findings)

### s3-0019 through s3-0022 — SMELL3-H002 — LOW confidence — LLM: HIGH
**Reassessment: ALL FOUR ARE FALSE POSITIVES — wrong source layer**  
All four findings are on Kentucky statutory and regulatory nodes (KY-KRS-304-14, KY-KAR-806-13-150, KY-KAR-806-12-095). The heuristic fired on standard legislative drafting ("except as otherwise provided", "except as provided in this subsection"). These sources are reference material — they exist so we can check carrier filings *against* them. Smell detectors must not fire on statutory/regulatory nodes; suggesting a carrier amend a Kentucky statute is not actionable.  
**Action:** Apply source ID prefix guard to all detectors (skip KY-KRS-*, KY-KAR-*, KY-DOI-* nodes). Tracked in BACKLOG-010.

---

## Smell 4 — Calculation Rule Drift / Unversioned Rate Reference (1 finding)

### s4-0023 — SMELL4-H001 — HIGH confidence — LLM: HIGH
**Reassessment: CONFIRMED HIGH**  
KNIC rate manual refers to "the Manual for that state" with no version, edition, or date. Unversioned external manual reference in a rate rule is a clean, auditable finding — if the external manual changes, there is no way to determine which version governed a specific claim. Remediation is concrete: add edition and effective date.

---

## Smell 5 — Regulatory Mapping (12 findings)

### H004 findings (s5-0024 through s5-0028) — MEDIUM confidence — LLM: HIGH
**Reassessment: CONFIRMED — real findings, HIGH appropriate**  
Rate information, homeowner risk factor, base premium computation, deductible factor, roof rating factor — all rating methodology nodes with no traceable edge to KRS/KAR/DOI authority in the graph. This is precisely what H004 is designed to catch. Both KNIC and KFBM have H004 findings, making these industry-wide patterns — strongest signal class.

### H005 findings (s5-0029 through s5-0030) — MEDIUM confidence — LLM: HIGH
**Reassessment: MIXED**  
- s5-0029: "Section II Coverage is not mandatory for the secondary residence policy" — **statement of requirement, not provision.** This is a filing instruction telling agents how to structure a secondary residence policy, not a coverage provision asserting regulatory authority. To confirm a real problem, you would need to compare against an actual issued policy and verify Section II was handled correctly. Not actionable from the filing alone. **Downgrade to LOW / informational.**  
- s5-0030: "The policy must be endorsed to provide an automatic annual increase" — mandatory language with no regulatory citation. This is closer to a real finding — it is asserting a filing requirement that should have a regulatory basis. Inflation guard requirement may have a DOI basis not visible in this filing. **MEDIUM pending cross-reference check.**

### H006 findings (s5-0031 through s5-0035) — LOW confidence — LLM: HIGH (except s5-0031 MEDIUM)
**Reassessment: WEAK — most are section headers, table-of-contents entries, or duplicates**  
- s5-0031: Coverage C replacement cost section — already flagged by Smell 2. Duplicate signal.  
- s5-0032: Evidence text is just the section header "Roof Surface Loss Settlement" — no substantive content. Likely false positive.  
- s5-0033: Endorsement table of contents — same issue as s2-0003. False positive.  
- s5-0034: Overlaps with the notice provision already flagged in Smell 1 (s1-0001). Duplicate signal.  
- s5-0035: Inflation guard section — "the inflation percentage is based on an index of construction costs" with no citation to which index. This one is real — the index is unversioned and unidentified. Keep.  
**Severity for s5-0032, s5-0033:** FALSE POSITIVE — insufficient evidence text.  
**Severity for s5-0031, s5-0034:** DUPLICATE — already captured under Smell 2 and Smell 1 respectively.  
**Severity for s5-0035:** MEDIUM — real finding, weaker than H004 but actionable.

---

## Pipeline gaps identified during review

1. **BACKLOG-006**: Smell 1 detectors need node-level language context — cannot distinguish exclusions from conditions with coverage consequences.
2. **BACKLOG-007**: No KRS/KAR definitional cross-reference check. "Reasonable time" and similar terms may be defined in statute; findings would drop in severity if statutory definition exists.
3. **BACKLOG-008**: Replacement cost / ACV findings may be Smell 4 (unversioned external reference) rather than Smell 2 (undefined magic term).
4. **BACKLOG-009**: Candidate new smell identified — Non-Deterministic Underwriting / Eligibility Criteria ("favorable impact on market value" in KNIC underwriting guidelines).
5. **BACKLOG-010**: All smell detectors fire on statutory/regulatory corpus nodes. Source ID prefix guard needed immediately (skip KY-KRS-*, KY-KAR-*, KY-DOI-*). All four Smell 3 findings are false positives as a result.
6. **BACKLOG-011**: Section headers, titles, and document structure nodes produce false positives. Detectors should skip nodes below a minimum substantive text threshold.
7. **BACKLOG-012**: H005 heuristic fires on statements of filing requirement as well as statements of provision. These are different: a requirement tells an agent how to structure a policy; a provision asserts regulatory authority in a coverage context. H005 needs a context guard to distinguish the two — likely requires the same node-level language context annotation as BACKLOG-006.

## Summary: Confirmed findings for Stage 002/003

| Finding ID | Smell | Assessment |
|---|---|---|
| s1-0001 | 1 | False positive — notice provision, not exclusion |
| s2-0002 | 2 | LOW — underwriting criteria, not claims layer |
| s2-0003 | 2 | False positive — endorsement table of contents |
| s2-0004 through s2-0007 | 2 | HIGH — replacement cost undefined (may be Smell 4 overlap) |
| s2-0008, s2-0009, s2-0013, s2-0014, s2-0017, s2-0018 | 2 | MEDIUM — "reasonable time" undefined (KRS check pending) |
| s2-0010, s2-0011, s2-0015, s2-0016 | 2 | HIGH — ACV undefined in loss settlement conditions |
| s2-0012 | 2 | HIGH — ACV in roof surfacing endorsement |
| s3-0019 through s3-0022 | 3 | False positive — statutory nodes, wrong source layer |
| s4-0023 | 4 | HIGH confirmed — unversioned manual reference |
| s5-0024 through s5-0028 | 5 | HIGH confirmed — H004 rate nodes with no regulatory edge |
| s5-0029, s5-0030 | 5 | HIGH confirmed — H005 mandatory coverage claims |
| s5-0031 | 5 | Duplicate of Smell 2 finding |
| s5-0032, s5-0033 | 5 | False positive — section header / table of contents only |
| s5-0034 | 5 | Duplicate of Smell 1 finding |
| s5-0035 | 5 | MEDIUM confirmed — unidentified construction cost index |
