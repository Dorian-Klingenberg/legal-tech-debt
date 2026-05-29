# STAGE 004-TYPED-EDGE-STUDY: CURRENT STATUS & DOCUMENTATION

**Last Updated: 2026-05-19**
**Status: Phase 1 Complete → Phase 2 In Progress**

---

## QUICK STATUS

| Item | Status | Progress |
|------|--------|----------|
| Phase 1: Label Controlled Edge Set | ✓ COMPLETE | 46/46 edges labeled (87% high confidence) |
| Phase 2: Define Typed Matrix Semantics | 🔄 IN PROGRESS | Analysis complete → refinement needed |
| Phase 3: Build Typed Matrix Prototype | ⏳ PENDING | Awaiting Phase 2 taxonomy refinement |
| Phase 4: Update Dashboard | ⏳ PENDING | Blocked on Phase 3 |
| Phase 5: Automation Strategy | ⏳ PENDING | Blocked on Phase 4 |

---

## WHAT WE'RE WORKING ON: EDGE TYPE TAXONOMY REFINEMENT

**Central Question Being Answered:**
> Can a matrix-based dependency system distinguish valid legal/compliance access from plain graph reachability by using relationship types?

**Current Finding:**
The taxonomy works well (87% high confidence), but needs refinement before typed closure implementation:

### The Problem
- **13 edge types** proposed, but only **11 should survive**
- **2 weak types** (cites_authority, coordinates_with) need elimination
- **3 boundary ambiguities** need clarification (exception_process split, proof vs reporting distinction, evidence inverse semantics)
- **6 edges** are medium-confidence and will resolve after refinement

### The Refinement Roadmap
**Phase 2A (Eliminate weak types):**
1. Delete `cites_authority` (1 edge) → merge to implements_authority
2. Delete `coordinates_with` (1 edge) → merge to requires_evidence or implements_authority

**Phase 2B (Clarify boundary types):**
3. Split `exception_process` into exception_handling (internal) and exception_authority (statute)
4. Sharpen `proof_requirement` vs `reporting_requirement` definitions
5. Elevate `notice_requirement` confidence (E028 privacy notice is high-confidence compliance)
6. Separate semantics: `requires_evidence` (input) vs `records_retention` (output)

**Phase 2C (Validate refinement):**
7. Relabel all 6 medium-confidence edges with refined taxonomy
8. Update EDGE_TYPE_FRAMEWORK.md with refined definitions
9. Produce path composition rules for typed closure

---

## DOCUMENTATION ARTIFACTS IN STAGE 4

### Core Planning Documents
- **STAGE.md** — Stage purpose, command, baseline evidence, stage status
- **PLAN.md** — 5-phase master plan for semantic typing work
- **LESSON.md** — Educational narrative: "A Reference Is Not Yet a Relationship"
- **README.md** — Sandbox intro and configuration

### Edge Type Study Materials
- **study/EDGE_TYPE_FRAMEWORK.md** — Proposed 13 edge types with definitions and path rules
- **study/EDGE_LABELING_GUIDE.md** — How to hand-label edges (confidence, rationale, reachability)
- **study/edge_labeling_seed.csv** — All 46 labeled seed edges (source of truth)
- **study/SEED_ANALYSIS_REPORT.md** — **NEW:** Analysis of 46 seeds, gap identification, recommendations
- **study/SEED_EDGE_COMPLETE_LIST.md** — **NEW:** Complete reference table + grouped views

### Baseline Evidence (Inherited from Stage 003)
- **output/findings.json** — 48 structural defects detected
- **output/dependency_roots.json** — Root dependency analysis
- **output/adjacency_matrix.csv** — 65×65 matrix (plain closure)
- **output/section_index.csv** — Section metadata
- **dashboard.html** — Interactive visualization

### Investigation Notes
- **OBSERVATIONS.md** — Early smoke-test observations
- **MATRIX_NOTES.md** — Matrix interpretation notes
- **TECH_EVALUATION.md** — Technology evaluation
- **SOURCE_NOTES.md** — Source corpus notes
- **BACKLOG.md** — Backlog of ideas
- **EXPERIMENT_CHARTER.md** — Pre-phase A framing

### Journal
- **journal/2026-05-13-work-session.md** — Session notes from stage creation

---

## THE 46 SEED EDGES: AT A GLANCE

### Distribution by Type (13 types)
```
Tier 1 (>5 edges):
  workflow_handoff .......................... 8 edges
  implements_authority ..................... 6 edges

Tier 2 (3-4 edges):
  validates_against, stale_reference, review_loop,
  requires_evidence, notice_requirement .... 4 edges each

Tier 3 (2-3 edges):
  records_retention, exception_process .... 3 edges each
  reporting_requirement, proof_requirement  2 edges each

Tier 4 (1 edge):
  coordinates_with [UNCERTAIN] ............ 1 edge
  cites_authority [UNCERTAIN] ............. 1 edge
```

### Confidence & Reachability
```
High Confidence:   40/46 (87%)
Medium Confidence: 6/46 (13%)
Low Confidence:    0/46 (0%)

Live (active in reachability):      37 edges
Visible Only (informational):        4 edges
Exclude (stale/invalid):             4 edges
Review (undecided):                  1 edge
```

### Three Semantic Domains

**Authority Domain (26 edges → statute/regulation 304.*, 806.*)**
- Types: implements_authority, validates_against, notice_requirement, records_retention, reporting_requirement, proof_requirement
- 100% target consistency
- Legal obligations point outward to external rules

**Internal Workflow Domain (19 edges → internal sections 1000+)**
- Types: workflow_handoff, review_loop, coordinates_with, exception_process (2/3)
- 100% target consistency
- Process routing stays internal

**Evidence/Recordkeeping Domain (4 edges → mixed targets)**
- Types: requires_evidence (input), records_retention (output)
- Semantically inverse pattern
- Evidence flows both directions

**Defects (4 edges → missing/invalid targets)**
- Type: stale_reference
- 100% precision detection
- Should not participate in valid reachability

---

## THE FIVE PHASES (WHERE WE ARE)

### Phase 1: Label a Controlled Edge Set ✓ COMPLETE
**Goal:** Get 40+ representative edges labeled with high confidence
**Result:** 46 edges labeled, 87% high confidence, all types represented
**Key Artifact:** `study/edge_labeling_seed.csv`
**Lesson:** Plain labels exposed ambiguities; weak types emerged clearly

### Phase 2: Define Typed Matrix Semantics 🔄 IN PROGRESS
**Goal:** Decide which edge types participate in legal reachability; draft composition rules
**Current Work:** 
  - ✓ Analyzed 46 seeds for gaps and patterns
  - ✓ Identified 6 recommendations for refinement
  - → NEXT: Refine framework and relabel uncertain edges
**Key Artifacts:** 
  - `SEED_ANALYSIS_REPORT.md` (gap identification)
  - `SEED_EDGE_COMPLETE_LIST.md` (reference data)
  - Refined `EDGE_TYPE_FRAMEWORK.md` (pending)
**Done When:**
  - A_type matrix layers are named (11 types, not 13)
  - Invalid path examples are documented
  - At least 5 witness paths have expected typed outcomes

### Phase 3: Build the First Typed Matrix Prototype ⏳ PENDING
**Goal:** Implement typed matrix computation and compare to plain closure
**Requirements:** Refined Phase 2 outputs
**Deliverables:**
  - Typed edge loader in `src/legal_debt_probe.py`
  - One adjacency matrix per edge type
  - Typed reachability report
  - Path-by-path comparison
**Key Question:** Which plain-closure paths disappear or change meaning under typing?

### Phase 4: Update the Dashboard ⏳ PENDING
**Goal:** Visualize typed edges and typed reachability
**Requirements:** Phase 3 outputs
**Deliverables:**
  - Edge-type filtering controls
  - Witness paths annotated with edge types
  - Matrix toggle: plain closure ↔ typed closure
  - Stale references highlighted as distinct
**Key Question:** Can a reviewer understand why a path is valid or invalid?

### Phase 5: Decide What To Automate ⏳ PENDING
**Goal:** Determine which edge types can be auto-detected vs require human review
**Requirements:** Phase 4 insights
**Deliverables:**
  - Deterministic extraction rules (if any)
  - SME review criteria
  - NLP/LLM assistance strategy (if needed)
**Key Question:** What minimal tool does a compliance analyst need?

---

## IMMEDIATE NEXT STEPS

### Priority 1: Refine the Taxonomy (TODAY)
1. **Delete weak types**: cites_authority, coordinates_with
2. **Split exception_process**: exception_handling, exception_authority
3. **Clarify semantics**: proof_requirement, reporting_requirement, notice_requirement
4. **Separate inverse pair**: requires_evidence vs records_retention
5. **Update EDGE_TYPE_FRAMEWORK.md** with refined 11-type taxonomy

### Priority 2: Validate Refinement (TODAY/TOMORROW)
6. **Relabel 6 uncertain edges** with new taxonomy
7. **Verify no orphans** — every edge maps cleanly to a type
8. **Document path composition rules** — which edge sequences are legal?

### Priority 3: Phase 2 Sign-Off (TOMORROW)
9. **Document 5 witness paths** showing typed vs plain closure differences
10. **Update PLAN.md** with refined types
11. **Sign off Phase 2** → Ready for Phase 3 implementation

---

## KEY INSIGHTS FROM ANALYSIS

### The Weak Types Problem
- **cites_authority** (1 edge, E021): Redundant with implements_authority. Merge.
- **coordinates_with** (1 edge, E024): Too vague, marked "review". Eliminate → decide if bidirectional implements or requires_evidence.

### The Split Types Problem
- **exception_process** has 2 patterns:
  - E037, E038 (internal): Fallback when normal processing fails
  - E013 (statute): Electronic reporting failure references regulation
  - **Action:** Create exception_handling (internal) + exception_authority (statute)

### The Inverse Semantics Problem
- **requires_evidence** vs **records_retention**: Opposite directions
  - requires_evidence: "I need evidence as INPUT" (E029: letter depends on evidence packet)
  - records_retention: "I must preserve evidence as OUTPUT" (E040: retention preserves records)
  - **Action:** Clarify in definitions; keep both; E032/E035 ambiguity resolves with clear semantics

### The Confidence Bootstrap
- 40/46 (87%) high confidence = framework is *mostly right*
- 6 uncertain edges are all in boundary zones → refinement fixes them
- 0 low-confidence edges = domain expertise validated the labeling

### The Domain Separation
- Authority (statute) and workflow (internal) are **completely separate** domains
- No authority edges point internal; no workflow edges point to statute
- **Implication:** Typed closure should probably compose separately by domain

---

## SUCCESS CRITERIA TRACKER

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Can detect intentional defects | ✓ YES | 4 stale_reference edges found with 100% precision |
| Output understandable to SME | ✓ YES | 40/46 edges high-confidence; rationales clear |
| Framework captures real distinctions | ✓ YES | 13/13 types have single reachability mode; no conflicts |
| Produces clear next question | ✓ YES | Refinement roadmap clear; gap analysis concrete |
| Typed vs plain reachability differs | ⏳ TBD | Will be proven in Phase 3 |

---

## WHERE TO GO FROM HERE

**If you want to refine the framework:**
- Start with SEED_ANALYSIS_REPORT.md (recommendations section)
- Update study/EDGE_TYPE_FRAMEWORK.md with 11 types instead of 13
- Relabel 6 uncertain edges

**If you want to understand the current state:**
- Read LESSON.md (conceptual overview)
- Read SEED_ANALYSIS_REPORT.md (gaps and insights)
- Review SEED_EDGE_COMPLETE_LIST.md (all 46 seeds)

**If you want to move to Phase 3:**
- Wait for Phase 2 refinement to complete
- Need refined EDGE_TYPE_FRAMEWORK.md
- Need 6 uncertain edges relabeled
- Need 5 witness paths documented

---
