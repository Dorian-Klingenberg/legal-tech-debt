# Project Backlog

Status: Active
Scope: Cross-sandbox items with no current sandbox home
Last updated: 2026-06-04

This file tracks open questions, deferred tasks, and homeless backlog items — things that are real enough to record but not yet assigned to a sandbox or stage. Items are checked off when resolved, not deleted, so the search history stays visible.

---

## Open Items

### [ ] BACKLOG-001: Smell 5 Detector Calibration

**Status:** Open — no sandbox assigned  
**Affects:** Sandbox 002 Stage 006; Sandbox 003 five-smell completeness claim  
**Priority:** Must resolve before claiming five-smell completeness

The Regulatory Mapping smell detector (Smell 5) produces zero findings on the expanded 28-source corpus (run `18b0dec5`). This is almost certainly under-recall from uncalibrated heuristics, not a clean negative result.

**What we know:**
- The most promising targets are the KFBM DOI objection response and rate manual filings, which should contain KRS/KAR citation gaps the current heuristics are not firing on.
- ADR-009 formally records this as a known limitation and a non-blocker to starting Sandbox 003.
- Sandbox 003 must not claim five-smell completeness until this is resolved.

**Next action:** Inspect KFBM DOI objection response and rate manual nodes from run `18b0dec5`; identify why Smell 5 heuristics are not triggering; patch and rerun detector.

---

### [ ] BACKLOG-002: Corpus File Extension Mismatches

**Status:** Open — low priority  
**Affects:** Corpus parsing warnings; no stage is currently blocked

Two corpus files are named `.html` but contain PDF content:
- `KY-KRS-304-12-230`
- `KY-KRS-304-14`

A third file with the same issue (`KY-KRS-304-13`) was already renamed. The pipeline parses these with warnings and does produce nodes, so nothing is blocked.

**Next action:** Rename both files to `.pdf`, update `_download_manifest.csv`, rerun Stage 002 to confirm warnings clear.

---

### [ ] BACKLOG-003: Kentucky Growers Insurance Company (KGIC) SERFF Search

**Status:** Open — no filings found in SFA  
**Affects:** `corpus/kentucky-homeowners-policy-smells/KNOWN-GAPS.md` (Gap ID: KY-SERFF-KGIC-POST2018)

**Search history:**
- 2026-06-03: User searched SERFF Filing Access for Kentucky Growers Insurance Company homeowners/dwelling filings (KY, TOI 04.0/04.1). No entry found — carrier may not file homeowners in SERFF or may file under a different name.
- 2026-06-04: Attempted recheck to confirm — SERFF Filing Access site was down.

**What we know:**
- This is not "manual retrieval required" — it is "searched and came up empty."
- Until the site is back up and a confirmed second search is run, treat as likely not present in SFA.
- Low urgency: the current KNIC and KFBM corpus is sufficient for Sandbox 003.

**Next action:** When SFA is back up, rerun the search: State = Kentucky, TOI = 04.0 then 04.1, Company = "Growers" / "Kentucky Growers". If still no results, close this gap as not available in SFA and update `KNOWN-GAPS.md`.

---

### [ ] BACKLOG-004: Stage 005 Semantic Retrieval Re-open Conditions

**Status:** Open — one of three gates met  
**Affects:** Sandbox 002 Stage 005; ADR-002; vector store selection (ADR-005)

Re-opening semantic retrieval requires all three conditions:
- [x] Second carrier homeowners corpus present (KFBM added 2026-06-03)
- [ ] At least one gold set item written as a plain-English reviewer paraphrase query (not document vocabulary)
- [ ] At least one documented BM25 failure that a concept-level query would fix

**What we know:**
- BM25 currently hits 21/21 (100%) on the existing gold set, but the gold set queries are written in document vocabulary, making it an unfairly easy test for BM25.
- Semantic retrieval scored 76% on the same queries — not because embeddings are weak, but because the queries are phrase-matchable.
- A fair evaluation needs reviewer-style paraphrase queries and a real BM25 miss.

**Next action:** Defer until after Sandbox 003. At that point, draft 3–5 paraphrase-style reviewer questions (e.g., "does this policy explain how the company decides what something is worth?") and check whether BM25 misses them.

---

## Resolved Items

| ID | Item | Resolution | Date |
|---|---|---|---|
| — | KFBM SERFF filings (KY-SERFF-KFBM-POST2018) | 11 files from 5 filings extracted and added to corpus | 2026-06-03 |
