# COMPLETE SEED EDGE LIST (All 46 Edges)

## Reference Table

| ID | From | To | Document | Line | Type | Conf | Reach | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|
| E001 | 1000 | 304.39.010 | commonwealth_auto_claims_playbook_synthetic.md | 8 | implements_authority | high | live | Playbook scope says it implements the authority | Internal procedure to statute-like authority |
| E002 | 1000 | 304.39.080 | commonwealth_auto_claims_playbook_synthetic.md | 8 | implements_authority | high | live | Playbook scope says it implements the security authority | |
| E003 | 1000 | 304.39.117 | commonwealth_auto_claims_playbook_synthetic.md | 8 | implements_authority | high | live | Playbook scope says it implements proof-of-insurance authority | |
| E004 | 1000 | 304.20.040 | commonwealth_auto_claims_playbook_synthetic.md | 8 | implements_authority | high | live | Playbook scope says it implements cancellation notice authority | |
| E005 | 1000 | 806.39.070.2 | commonwealth_auto_claims_playbook_synthetic.md | 8 | implements_authority | high | live | Playbook scope says it implements proof-card regulation | |
| E006 | 1010 | 1020 | commonwealth_auto_claims_playbook_synthetic.md | 13 | workflow_handoff | medium | live | Classification can route the claim to PIP routing | |
| E007 | 1010 | 1030 | commonwealth_auto_claims_playbook_synthetic.md | 13 | workflow_handoff | medium | live | Classification can route the claim to proof validation | |
| E008 | 1020 | 304.39.030 | commonwealth_auto_claims_playbook_synthetic.md | 17 | validates_against | high | live | PIP routing verifies eligibility under the target | |
| E009 | 1020 | 304.39.040 | commonwealth_auto_claims_playbook_synthetic.md | 17 | validates_against | high | live | PIP routing verifies payment duty under the target | |
| E010 | 1020 | 1040 | commonwealth_auto_claims_playbook_synthetic.md | 18 | workflow_handoff | high | live | File moves to no-fault rejection handling if rejection is alleged | |
| E011 | 1030 | 304.39.117 | commonwealth_auto_claims_playbook_synthetic.md | 22 | proof_requirement | high | live | Proof validation compares records against proof authority | |
| E012 | 1030 | 806.39.070.4 | commonwealth_auto_claims_playbook_synthetic.md | 22 | reporting_requirement | high | live | Proof validation checks electronic reporting requirements | |
| E013 | 1030 | 806.39.070.7 | commonwealth_auto_claims_playbook_synthetic.md | 23 | exception_process | high | live | Electronic reporting failure invokes the exception path | |
| E014 | 1040 | 304.39.060 | commonwealth_auto_claims_playbook_synthetic.md | 27 | validates_against | high | live | Adjuster confirms the no-fault election under the target | |
| E015 | 1040 | 1020 | commonwealth_auto_claims_playbook_synthetic.md | 28 | review_loop | high | visible_only | Missing rejection form returns file to PIP routing | Loop should be visible but may not imply legal authority |
| E016 | 1050 | 304.20.040 | commonwealth_auto_claims_playbook_synthetic.md | 32 | notice_requirement | high | live | Cancellation hold compares the cancellation notice statute | |
| E017 | 1050 | 304.39.085 | commonwealth_auto_claims_playbook_synthetic.md | 32 | reporting_requirement | high | live | Cancellation hold checks termination reporting before release | |
| E018 | 1050 | 1090 | commonwealth_auto_claims_playbook_synthetic.md | 33 | workflow_handoff | high | live | Notice workflow remains open until hold is cleared | |
| E019 | 1060 | 304.39.110 | commonwealth_auto_claims_playbook_synthetic.md | 37 | validates_against | high | live | Liability limit verification confirms required minimum limits | |
| E020 | 1060 | 1070 | commonwealth_auto_claims_playbook_synthetic.md | 38 | workflow_handoff | high | live | UM exposure moves file to escalation | |
| E021 | 1070 | 304.20.020 | commonwealth_auto_claims_playbook_synthetic.md | 42 | cites_authority | medium | live | UM escalation documents connection to uninsured motorist authority | **UNCERTAIN - could be implements_authority** |
| E022 | 1070 | 1120 | commonwealth_auto_claims_playbook_synthetic.md | 43 | requires_evidence | high | live | External authority source must be recorded in evidence packet | |
| E023 | 1080 | 806.39.070.8 | commonwealth_auto_claims_playbook_synthetic.md | 47 | implements_authority | medium | live | Template update reconciles with forms library regulation | **UNCERTAIN - partial implementation?** |
| E024 | 1080 | 1030 | commonwealth_auto_claims_playbook_synthetic.md | 47 | coordinates_with | medium | review | Template updates reconcile with proof validation workflow | **UNCERTAIN - needs SME decision** |
| E025 | 1090 | 304.20.040 | commonwealth_auto_claims_playbook_synthetic.md | 52 | notice_requirement | high | live | Notice workflow begins when cancellation authority applies | |
| E026 | 1090 | 1110 | commonwealth_auto_claims_playbook_synthetic.md | 53 | workflow_handoff | high | live | Producer communications must remain synchronized with notice workflow | |
| E027 | 1100 | 304.20.320 | commonwealth_auto_claims_playbook_synthetic.md | 57 | notice_requirement | high | live | Adverse action letter explains specific reason required by target | |
| E028 | 1100 | 304.20.360 | commonwealth_auto_claims_playbook_synthetic.md | 58 | notice_requirement | medium | live | Privacy content is checked against privacy notice authority | **UNCERTAIN - should probably be high** |
| E029 | 1100 | 1120 | commonwealth_auto_claims_playbook_synthetic.md | 58 | requires_evidence | high | live | Letter content depends on evidence packet | |
| E030 | 1110 | 806.39.070.3 | commonwealth_auto_claims_playbook_synthetic.md | 62 | proof_requirement | high | live | Producer communication uses printed card details | |
| E031 | 1110 | 1090 | commonwealth_auto_claims_playbook_synthetic.md | 63 | review_loop | high | visible_only | Corrected producer data reopens notice workflow | |
| E032 | 1120 | 304.20.340 | commonwealth_auto_claims_playbook_synthetic.md | 67 | requires_evidence | medium | live | Evidence packet includes source excerpts for recordkeeping authority | **UNCERTAIN - could be records_retention?** |
| E033 | 1120 | 1030 | commonwealth_auto_claims_playbook_synthetic.md | 67 | requires_evidence | high | live | Evidence packet includes proof-card documents from proof validation | |
| E034 | 1120 | 9999 | commonwealth_auto_claims_playbook_synthetic.md | 68 | stale_reference | high | exclude | Historical checklist cites missing section and must be retired | **DEFECT** |
| E035 | 1200 | 304.39.120 | commonwealth_auto_claims_playbook_synthetic.md | 72 | records_retention | medium | live | Applicant intake stores disclosure election described by target | **UNCERTAIN - evidence vs retention boundary** |
| E036 | 1200 | 1040 | commonwealth_auto_claims_playbook_synthetic.md | 72 | workflow_handoff | high | live | Missing election evidence routes to no-fault rejection handling | |
| E037 | 1300 | 806.39.070.5 | commonwealth_auto_claims_playbook_synthetic.md | 77 | exception_process | high | live | Digital proof exception arises when ordinary presentation cannot satisfy target | |
| E038 | 1300 | 1400 | commonwealth_auto_claims_playbook_synthetic.md | 78 | exception_process | high | live | Exception owner consults printed fallback before closing | |
| E039 | 1400 | 1300 | commonwealth_auto_claims_playbook_synthetic.md | 82 | review_loop | high | visible_only | Printed fallback applies after digital exception fails | |
| E040 | 1500 | 304.39.200 | commonwealth_auto_claims_playbook_synthetic.md | 87 | records_retention | high | live | Retention preserves records supporting reparations decisions | |
| E041 | 1500 | 806.39.070.7 | commonwealth_auto_claims_playbook_synthetic.md | 87 | records_retention | high | live | Retention preserves electronic reporting exception evidence | |
| E042 | 1600 | 1700 | commonwealth_auto_claims_playbook_synthetic.md | 92 | workflow_handoff | high | live | Systemic issues escalate to quality audit | |
| E043 | 1700 | 1600 | commonwealth_auto_claims_playbook_synthetic.md | 97 | review_loop | high | visible_only | Audit can reopen supervisory review | |
| E044 | 304.39.087 | 304.39.888 | ky_motor_vehicle_insurance_code_synthetic.md | 69 | stale_reference | high | exclude | Legacy batch files refer to missing stale source | **DEFECT** |
| E045 | 304.20.340 | 304.20.999 | ky_auto_policy_notice_statute_synthetic.md | 43 | stale_reference | high | exclude | Legacy retention map cites missing source | **DEFECT** |
| E046 | 806.39.070.7 | 806.39.070.9 | ky_proof_of_insurance_regulation_synthetic.md | 38 | stale_reference | high | exclude | Obsolete exception code table references missing section | **DEFECT** |

---

## EDGES GROUPED BY TYPE

### implements_authority (6 edges)
- E001, E002, E003, E004, E005, E023

### workflow_handoff (8 edges)  
- E006, E007, E010, E018, E020, E026, E036, E042

### validates_against (4 edges)
- E008, E009, E014, E019

### proof_requirement (2 edges)
- E011, E030

### reporting_requirement (2 edges)
- E012, E017

### exception_process (3 edges)
- E013, E037, E038

### notice_requirement (4 edges)
- E016, E025, E027, E028

### requires_evidence (4 edges)
- E022, E029, E032, E033

### records_retention (3 edges)
- E035, E040, E041

### review_loop (4 edges)
- E015, E031, E039, E043

### stale_reference (4 edges)
- E034, E044, E045, E046

### cites_authority (1 edge)
- E021

### coordinates_with (1 edge)
- E024

---

## EDGES BY CONFIDENCE

### High Confidence (40 edges)
E001, E002, E003, E004, E005, E008, E009, E010, E011, E012, E013, E014, E015, E016, E017, E018, E019, E020, E022, E025, E026, E027, E029, E030, E031, E033, E034, E036, E037, E038, E039, E040, E041, E042, E043, E044, E045, E046

### Medium Confidence (6 edges)
E006, E007, E021, E023, E024, E028, E032, E035

### Low Confidence (0 edges)
None

---

## EDGES BY REACHABILITY

### live (37 edges)
E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012, E013, E014, E016, E017, E018, E019, E020, E021, E022, E023, E025, E026, E027, E028, E029, E030, E032, E033, E035, E036, E037, E038, E040, E041, E042

### visible_only (4 edges)
E015, E031, E039, E043

### exclude (4 edges)
E034, E044, E045, E046

### review (1 edge)
E024

---

## KEY OBSERVATIONS

### Authority Domain (To statute/regulation sections)
- 304.* and 806.* targets: 26 edges
- These are dominated by: implements_authority, validates_against, notice_requirement, records_retention, reporting_requirement, proof_requirement
- All authority-type edges have 100% consistency in target domain

### Internal Workflow Domain (To internal sections 1000+)
- Internal targets: 19 edges
- These are dominated by: workflow_handoff, review_loop, coordinates_with, and some exception_process
- All workflow-type edges have 100% consistency in target domain

### Evidence/Recordkeeping Domain (Internal or mixed)
- Mixed targets: 4 edges
- Types: requires_evidence (mixed), records_retention (statute), exception_process (mixed)
- Semantically inverse pattern between requires_evidence and records_retention

### Stale/Defective Domain
- 4 stale_reference edges pointing to invalid targets or missing sections
- 100% detection rate for structural defects
- Perfect reachability classification (exclude)

---
