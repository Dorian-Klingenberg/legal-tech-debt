# STAGE 004 DOCUMENTATION MAP

## Directory Structure

```
stages/004-typed-edge-study/
├── STAGE_004_STATUS.md ..................... ← YOU ARE HERE (Current overview)
├── STAGE.md .............................. Stage purpose & status
├── PLAN.md .............................. 5-phase master plan
├── LESSON.md ............................ Educational narrative
├── README.md ............................ Sandbox config
│
├── study/ ......................... Core study materials
│   ├── EDGE_TYPE_FRAMEWORK.md ........... Proposed 13 types (NEEDS REFINEMENT)
│   ├── EDGE_LABELING_GUIDE.md ........... How to label edges
│   ├── edge_labeling_seed.csv ........... All 46 labeled edges (SOURCE OF TRUTH)
│   ├── SEED_ANALYSIS_REPORT.md ......... **NEW** Gap analysis & recommendations
│   └── SEED_EDGE_COMPLETE_LIST.md ...... **NEW** Complete reference + grouped views
│
├── output/ ......................... Generated evidence
│   ├── findings.json ................... 48 structural defects
│   ├── dependency_roots.json ........... Root analysis
│   ├── adjacency_matrix.csv ............ 65×65 plain closure matrix
│   ├── section_index.csv ............... Section metadata
│   └── transitive_closure.csv .......... Computed closure
│
├── data/ ............................. Input corpus
│   └── corpus/ ........................ Kentucky insurance sample (60 sections)
│
├── src/ .............................. Source code
│   └── legal_debt_probe.py ............ Main probe (will add typed matrix support)
│
├── journal/ .......................... Session notes
│   └── 2026-05-13-work-session.md .... Stage creation notes
│
├── dashboard.html .................... Interactive visualization
├── OBSERVATIONS.md ................... Smoke-test observations
├── MATRIX_NOTES.md ................... Matrix interpretation
├── TECH_EVALUATION.md ................ Tech stack notes
├── BACKLOG.md ........................ Backlog of ideas
└── EXPERIMENT_CHARTER.md ............ Pre-phase A framing
```

---

## READING ORDER BY PURPOSE

### I Want Quick Context (10 min)
1. **STAGE_004_STATUS.md** (this file) — Where we are + next steps
2. **LESSON.md** (first 30 lines) — Core insight: "A reference is not yet a relationship"
3. **PLAN.md** (first 30 lines) — The 5 phases

### I Want Full Context (30 min)
1. **STAGE_004_STATUS.md** — Full overview
2. **LESSON.md** — Complete educational narrative
3. **SEED_ANALYSIS_REPORT.md** (Summary Stats section) — Analysis at a glance
4. **PLAN.md** — All 5 phases

### I Want To Understand the Seed Data (45 min)
1. **SEED_ANALYSIS_REPORT.md** — Why each type was chosen, gaps found
2. **SEED_EDGE_COMPLETE_LIST.md** — All 46 edges in reference table
3. **study/edge_labeling_seed.csv** — Raw data (CSV format)
4. **EDGE_LABELING_GUIDE.md** — How labels were assigned

### I Want To Refine the Framework (Today)
1. **SEED_ANALYSIS_REPORT.md** → "RECOMMENDATIONS FOR TAXONOMY REFINEMENT" section
2. **study/EDGE_TYPE_FRAMEWORK.md** → Current 13-type definitions
3. **SEED_EDGE_COMPLETE_LIST.md** → See all edges by type
4. Create refined framework with 11 types
5. Relabel 6 uncertain edges

### I Want To Move to Phase 3 (Implementation)
1. **PLAN.md** → Phase 3 requirements
2. **study/EDGE_TYPE_FRAMEWORK.md** (refined version) → Type definitions
3. **study/edge_labeling_seed.csv** (updated) → All 46 seeds with refined types
4. **src/legal_debt_probe.py** → Where to add typed matrix support

---

## WHAT EACH DOCUMENT DOES

### Planning & Status
- **STAGE.md** — Stage metadata, purpose, command, baseline evidence
- **PLAN.md** — 5-phase decomposition of work
- **STAGE_004_STATUS.md** — Current progress, next steps, success criteria

### Education & Framing
- **LESSON.md** — Teaches why typed edges are necessary using small examples
- **EXPERIMENT_CHARTER.md** — Pre-phase A framing: hypotheses and evidence to capture
- **README.md** — Sandbox setup and configuration

### Edge Type Study
- **EDGE_TYPE_FRAMEWORK.md** — Definitions of 13 types + path composition rules
- **EDGE_LABELING_GUIDE.md** — Practical heuristics for labeling edges
- **edge_labeling_seed.csv** — Hand-labeled ground truth (46 edges)

### Analysis (NEW)
- **SEED_ANALYSIS_REPORT.md** — Breakdown of 46 seeds, gaps, recommendations
- **SEED_EDGE_COMPLETE_LIST.md** — Reference table + grouped views

### Investigation Notes
- **OBSERVATIONS.md** — Initial smoke-test findings
- **MATRIX_NOTES.md** — Interpretation of baseline matrices
- **TECH_EVALUATION.md** — Technology stack evaluation
- **BACKLOG.md** — Parking lot for ideas

---

## KEY DATA

### The 46 Seed Edges

**By Type (top 5):**
- workflow_handoff (8): E006, E007, E010, E018, E020, E026, E036, E042
- implements_authority (6): E001, E002, E003, E004, E005, E023
- validates_against (4): E008, E009, E014, E019
- stale_reference (4): E034, E044, E045, E046
- review_loop (4): E015, E031, E039, E043

**By Confidence:**
- High (40): Most edges, clear types
- Medium (6): E006, E007, E021, E023, E024, E028, E032, E035 — NEED REFINEMENT
- Low (0): None — framework is solid!

**By Reachability:**
- live (37): Participate in valid reachability
- visible_only (4): Informational only
- exclude (4): Stale/invalid
- review (1): Undecided

### The Inherited Baseline (from Stage 003)

```
Kentucky Insurance Sample:
- 60 sections (internal + statute)
- 197 references extracted
- 65 matrix nodes
- 48 structural defects found
- 65×65 adjacency matrix computed
- Interactive dashboard built
```

---

## CRITICAL DECISION POINTS

### Before Phase 2 Can Close:

**Decision 1: Eliminate Weak Types?**
- Current: 13 types (cites_authority, coordinates_with underused)
- Proposed: 11 types (delete 2, merge into stronger types)
- **Action Required:** Decide whether to keep or merge

**Decision 2: Split exception_process?**
- Current: 3 edges (2 internal, 1 statue reference)
- Proposed: exception_handling + exception_authority
- **Action Required:** Decide if worth the split

**Decision 3: Proof vs Reporting?**
- Current: 2 + 2 edges, definitions weak
- Proposed: Clarified definitions + decision tree
- **Action Required:** Write clear distinctions

**Decision 4: Evidence inverse semantics?**
- Current: requires_evidence vs records_retention (opposite directions)
- Proposed: Make directions explicit in definitions
- **Action Required:** Clarify input vs output semantics

**Decision 5: Path composition rules?**
- Current: Generic "any edge type can compose"
- Proposed: Valid sequences (e.g., implements → validates, but not workflows → authority)
- **Action Required:** Document at least 5 path rules

---

## SUCCESS METRICS

### Phase 1: ✓ COMPLETE
- [x] 40+ edges labeled (46 done)
- [x] 80%+ high confidence (87% done)
- [x] All types represented (13/13)
- [x] Stale references identified (4/4)

### Phase 2: 🔄 IN PROGRESS
- [x] Analysis of gaps complete
- [x] Recommendations documented
- [ ] Framework refined (11 types)
- [ ] 6 uncertain edges relabeled
- [ ] 5 witness paths documented
- [ ] Path composition rules written

### Phase 3: ⏳ BLOCKED (awaiting Phase 2)
- [ ] Typed edge loader built
- [ ] Typed matrices emitted
- [ ] Typed reachability report generated
- [ ] Plain vs typed closure compared

### Phase 4: ⏳ BLOCKED (awaiting Phase 3)
- [ ] Dashboard edge-type filtering
- [ ] Witness paths annotated
- [ ] Matrix toggle implemented

### Phase 5: ⏳ BLOCKED (awaiting Phase 4)
- [ ] Extraction rules identified
- [ ] SME review criteria documented
- [ ] NLP/LLM strategy drafted

---

## WHERE TO FIND THINGS

**I need the edge type definitions**
→ study/EDGE_TYPE_FRAMEWORK.md

**I need all 46 edges in one place**
→ study/SEED_EDGE_COMPLETE_LIST.md OR study/edge_labeling_seed.csv

**I need to understand why type X is weak**
→ SEED_ANALYSIS_REPORT.md (Gaps & Contradictions section)

**I need to know how confident each edge is**
→ SEED_EDGE_COMPLETE_LIST.md (Edges by Confidence section)

**I need to understand the philosophy**
→ LESSON.md

**I need the 5-phase plan**
→ PLAN.md

**I need the next 3 tasks**
→ STAGE_004_STATUS.md (Immediate Next Steps section)

---
