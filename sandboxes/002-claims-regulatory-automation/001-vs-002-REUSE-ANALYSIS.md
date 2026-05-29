# 001 → 002 Overlap Analysis: What's Already Done

Status note: Sandbox 001 is now closed as foundational research. Use this document as background analysis, and use [002-CARRY-FORWARD-FROM-001.md](002-CARRY-FORWARD-FROM-001.md) as the active carry-forward decision record.

## Executive Summary

Sandbox 001 (Legal Debt Primitives) has completed **foundational research and core pattern detection infrastructure**. It has proven the core defect detection concept works, but is domain-agnostic and test-focused rather than insurance-specific or production-ready.

**Completion Status for 002 Phase 1**:
- ✅ **40-50% of foundational concepts proven** in 001
- ⚠️ **0-10% of insurance-specific adaptation** (001 is generic)
- ❌ **0% of regulatory automation** (001 has no regulatory feed integration)
- ❌ **0% of claims-specific logic** (001 is intentionally domain-agnostic)

---

## What 001 Has Successfully Built (Reusable for 002)

### 1. **Dependency Detection Core** ✅
**001 Status**: Complete and proven

**What it does**:
- Extracts section anchors (definitions, clauses) from source text
- Identifies references between sections
- Builds adjacency matrices and transitive closure
- Detects dangling references (broken links)
- Detects circular references
- Detects orphan definitions

**Evidence**:
- `stages/001-baseline`: Pure Python implementation, no dependencies
- `stages/003-kentucky-insurance-sample`: 60 sections, 197 references, working on real insurance content
- `output/adjacency_matrix.csv`: Full reachability analysis
- `output/transitive_closure.csv`: All-paths closure

**Reusable for 002?** ✅ **YES**
- The core reference detection and circular dependency detection works
- Can be directly integrated into Broken Link Detector + Cyclic Dependency detection
- No modifications needed; works "as-is"

---

### 2. **Graph Representation & Matrix Algebra** ✅
**001 Status**: Multiple implementations tested

**What it does**:
- Dense adjacency matrices (list-of-lists)
- Bitset representations for performance
- Sparse edge-list multiplication
- Transitive closure computation
- Two-hop reachability analysis

**Evidence**:
- `stages/006-matrix-performance-lab`: Performance tested across representations
- Output performance metrics already captured

**Reusable for 002?** ✅ **YES**
- Exact algorithms can be reused for dependency graph analysis
- 006 stage confirms matrix performance is acceptable at 5,000+ node scale
- No need to reinvent; can import directly

---

### 3. **Dashboard Mockup + Visualization** ✅
**001 Status**: Working static dashboard prototype

**What it does**:
- Interactive HTML dashboard showing graph structure
- Drill-down into findings and dependencies
- Matrix visualization
- Finding details and evidence snippets

**Evidence**:
- `stages/002-dashboard-mockup/dashboard.html`: Working prototype
- Data-driven from actual probe output

**Reusable for 002?** ✅ **PARTIALLY**
- HTML/CSS structure can be reused
- Data schema is different (001 = generic findings; 002 = claims-specific alerts)
- UI flow is reusable; content needs insurance domain adaptation

---

### 4. **Edge Type Taxonomy Framework** ✅
**001 Status**: Defined; manual labeling workflow tested

**What it does**:
- Categorizes reference types (implements, verifies, retains, routes, etc.)
- Hand-labeling guide for semantic classification
- Typed reachability rules

**Evidence**:
- `stages/004-typed-edge-study`: Edge type taxonomy and labeling queue
- Hand-labeled seed dataset created

**Reusable for 002?** ⚠️ **PARTIAL**
- Concept of typed edges is reusable
- Insurance-specific edge types need refinement (e.g., "overrides," "supersedes," "contradicts")
- 001's generic taxonomy can be starting point; 002 needs domain extension

---

### 5. **Lesson Documentation + Scientific Method** ✅
**001 Status**: Well-documented stage progression

**What it does**:
- Each stage has clear problem statement, experiment design, results, and next question
- Preserved evidence for every hypothesis
- Reusable experimental workflow

**Evidence**:
- `NEXT_STAGES.md`: 8+ candidate follow-on experiments defined
- Each stage has `LESSON.md` explaining what was learned

**Reusable for 002?** ✅ **YES**
- Use same staging methodology for 002 experiments
- Can copy the documentation patterns
- Proven to be maintainable and clear

---

## What 001 Does NOT Have (Must Be Built for 002)

### ❌ **Regulatory Feed Integration**
**001 Status**: None (intentionally out of scope)

**Why 002 needs it**:
- Phase 1 of 002 requires detecting broken statutory references
- Phase 2 requires ingesting and diffing regulatory changes
- 001 assumes static corpus; 002 needs live regulatory feeds

**Build effort for 002**: 2-3 weeks
- NAIC bulletin scraper
- State legislative API integration
- Federal Register feed processor
- Statute version tracking database

---

### ❌ **Claims-Specific Domain Logic**
**001 Status**: None (intentionally generic)

**Why 002 needs it**:
- 001 detects generic "dangling references"
- 002 needs "broken policy citations to repealed statutes"
- 001 detects generic "circular references"
- 002 needs "mutually-exclusive coverage definitions"

**Build effort for 002**: 3-4 weeks
- Claims domain terminology and rules
- Insurance-specific reference types
- Coverage logic interpretation
- Regulatory mapping (NAIC → internal policies)

---

### ❌ **Non-Determinism Detection**
**001 Status**: None (different problem class)

**Why 002 needs it**:
- 001: "Is this reference broken?" (binary structural check)
- 002: "Do these claims get decided consistently?" (semantic analysis of interpretation variance)

**Build effort for 002**: 4-6 weeks
- NLP embeddings for semantic similarity
- Claims decision history clustering
- Ambiguous term detection
- Adjudication consistency scoring

---

### ❌ **Regulatory Drift Mapping**
**001 Status**: None

**Why 002 needs it**:
- 001: Detects existing dangling references
- 002: Detects when NEW regulations make existing policies stale
- Different problem: future drift vs. current brokenness

**Build effort for 002**: 4-6 weeks
- Regulatory change detection
- Semantic diff between old and new rules
- Impact mapping (which policies affected?)
- Alert prioritization and escalation

---

### ❌ **Claims PAS Integration**
**001 Status**: None

**Why 002 needs it**:
- Decision Audit Trail requires capturing live claim decisions
- Mapping policy language → actual claim outcomes
- Not needed in 001 (test corpus only)

**Build effort for 002**: 6-8 weeks
- Guidewire/Duck Creek API integration
- Decision capture schema
- Historical claims analysis
- Evidence packet generation

---

### ❌ **Scope Creep Detection**
**001 Status**: None

**Why 002 needs it**:
- 001: Detects dangling/broken/circular references
- 002: Detects when coverage definitions are being used beyond original scope
- Different detection approach: behavior analysis + definition tracking

**Build effort for 002**: 4-6 weeks
- Coverage term definition tracking
- Claims history pattern analysis
- Scope violation scoring
- Remediation recommendations

---

## Reusable Code/Artifacts Checklist

### ✅ Can Import Directly from 001:

1. **Reference extraction logic**
   - File: `001/src/legal_debt_probe.py` (core parsing)
   - Effort to adapt: < 1 week

2. **Graph representation**
   - Files: `001/src/` (adjacency matrix, closure computation)
   - Effort to adapt: < 3 days (add edge types)

3. **Matrix algebra**
   - Files: `001/src/` (multiplication, closure)
   - Effort: 0 (use as-is)

4. **Dashboard skeleton**
   - File: `stages/002-dashboard-mockup/dashboard.html`
   - Effort to adapt: 1-2 weeks (add insurance data, new findings)

5. **Stage methodology + documentation templates**
   - Files: `STAGING.md`, stage examples
   - Effort: < 1 week (copy and adapt naming)

### ⚠️ Needs Significant Adaptation:

1. **Edge type taxonomy**
   - Current: Generic (implements, verifies, routes)
   - Needed: Insurance-specific (supersedes, contradicts, excludes, covers)
   - Effort: 1-2 weeks

2. **Test corpus generation**
   - Current: Kentucky insurance sample (generic)
   - Needed: NAIC model laws + multi-state policies
   - Effort: 2-3 weeks (legal review required)

3. **Finding schema**
   - Current: Generic "findings.json"
   - Needed: Claims-specific alert types (broken link, ambiguity, drift)
   - Effort: 1 week

### ❌ Must Build from Scratch:

1. Regulatory feed integration (2-3 weeks)
2. Non-determinism detector (4-6 weeks)
3. Regulatory drift map (4-6 weeks)
4. Claims PAS integration (6-8 weeks)
5. Scope creep detector (4-6 weeks)

---

## Phase 1 (002 Validation) Reuse Assessment

**Phase 1 Objective**: Prove Broken Link Detector works on real insurance policy corpus

### What Can Be Reused from 001:

1. ✅ **Reference extraction** → Extract citations from policies (001 core strength)
2. ✅ **Broken reference detection** → Check citations against statute database (001 detects dangling refs)
3. ✅ **Output report format** → Adapt 001's findings.json for Phase 1 alerts
4. ✅ **Dashboard visualization** → Use 001's HTML structure for drill-down
5. ✅ **Test infrastructure** → Reuse 001's stage methodology

### What Must Be Built for Phase 1:

1. ❌ **Statute database lookup** → Need live API to Cornell Law, state legislatures (NEW)
2. ❌ **Insurance policy corpus** → Need real NAIC + state policies (NEW, requires legal review)
3. ❌ **Severity scoring** → How critical is each broken link? (NEW)
4. ❌ **Insurance-domain validation** → Confirm with compliance SME (NEW)

### Phase 1 Build Timeline If Starting from 001:

| Task | Source | Effort | Duration |
|---|---|---|---|
| Adapt reference extraction | 001 | Reuse + config | 3 days |
| Build statute lookup service | NEW | Build | 5 days |
| Gather policy corpus | NEW | Manual | 3 days |
| Create broken-link detector | Mix | 60% reuse, 40% new | 5 days |
| Build report generation | 001 | Adapt | 2 days |
| Severity + remediation model | NEW | Design + build | 3 days |
| Dashboard adaptation | 001 | Adapt | 5 days |
| **Total Phase 1** | — | — | **~3-4 weeks** |

*vs. building from scratch: ~6-8 weeks*

---

## Recommendation

### Starting Point for 002:

1. **Clone 001's core infrastructure** (reference detection, graph, matrix algebra)
2. **Extend 001's edge type system** for insurance semantics
3. **Build Phase 1 (Broken Link Detector)** on top of proven 001 foundation
4. **Plan Phase 2+ as new work** (regulatory feeds, non-determinism, drift detection)

### Estimated Time Savings:

- **With 001 reuse**: 12-16 weeks for Phase 1 + 2 (Validation + Build)
- **Without 001 reuse**: 20-24 weeks
- **Savings**: 4-8 weeks (~30%)

### Key Dependency:

001's core assumption (reference extraction works) must remain true. If the reference extraction doesn't adapt well to claims context, you'll need to rebuild from scratch (likely weeks lost). Recommend validating on real NAIC + policy corpus in first week of 002 Phase 1.

---

*Analysis Date: May 2026*
