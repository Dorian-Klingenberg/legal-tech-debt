# Stage 006 Lessons

Stage: 006-deterministic-detectors
First lesson recorded: 2026-06-04 (session 4)

---

## Lesson 1: Filter Corpus Layer at the Runner, Not at Each Detector

### Problem

All four Smell 3 findings in the first production run were false positives. The detectors had fired on Kentucky statutory and regulatory nodes (KY-KRS-*, KY-KAR-*, KY-DOI-*) using standard legislative drafting phrases ("except as otherwise provided," "subject to all terms"). Suggesting a carrier amend a Kentucky statute is not actionable and would undermine a client report.

### Why It Mattered

The regulatory/statutory corpus exists so detectors can check carrier filings *against* it. Running detectors on that reference layer inverts the purpose of the pipeline entirely — it treats the standard as the target.

### Root Cause

The `source_type` field was blank for all statutory/regulatory nodes — it was never populated during ingestion. Detectors could not guard on it. Without a field to filter on, each detector would need its own ad hoc guard, which is fragile and easy to miss when adding new detectors.

### Pattern or Solution

**Short-term (implemented):** Add a source ID prefix guard at the runner level — one predicate covers all detectors:

```python
_REGULATORY_PREFIXES = ("KY-KRS-", "KY-KAR-", "KY-DOI-")

def _is_carrier_node(node: dict) -> bool:
    return not node.get("source_id", "").startswith(_REGULATORY_PREFIXES)

# In run_detectors():
carrier_nodes = [n for n in nodes if _is_carrier_node(n)]
```

The runner logs the skip count so each run shows how many corpus nodes were excluded.

**Long-term (deferred, BACKLOG-006 scope):** Populate `source_type` correctly in Stage 002 ingestion from the corpus manifest. Detectors then guard on `source_type not in {"ky_statute", "ky_regulation", "doi_bulletin"}` — semantic rather than ID-prefix-based.

### Why the Runner, Not Each Detector

A single guard in the runner covers all current and future detectors with no repetition. Per-detector guards create drift risk: a new detector added later will silently fire on corpus nodes unless the developer remembers to add the guard. Centralize authoritative filters.

### Evidence

- Run `20260604_130606_18b0dec5`: 4 of 4 Smell 3 findings were false positives on KRS/KAR nodes — 100% false positive rate for that smell in an unguarded run.
- After guard: smoke test confirmed `_is_carrier_node({"source_id": "KY-KRS-304-14"}) == False` and `_is_carrier_node({"source_id": "KNIC-001"}) == True`.

### Limitations

The prefix guard is brittle if source ID conventions change. If a future corpus adds a new regulatory source type with a different prefix pattern, the guard must be updated. The long-term `source_type` field approach is more robust.

### What to Reuse Next Time

Any pipeline that processes a mixed corpus (reference layer + target layer) needs an explicit layer filter at the outermost processing boundary — not inside individual analysis functions. Define the filter once, apply it before any analysis runs, log what was filtered.

---

## Lesson 2: Smoke-Test Predicate Logic Before Relying on It in a Pipeline

### Pattern

When adding a filter predicate to a data pipeline, always run a quick inline test that covers both the true and false cases before considering it done:

```python
python -c "
import detector_runner as r
assert not r._is_carrier_node({'source_id': 'KY-KRS-304-14'})
assert r._is_carrier_node({'source_id': 'KNIC-001'})
print('OK')
"
```

This catches encoding issues, import errors, and inverted logic before a full pipeline run. Costs 5 seconds. A full re-run costs minutes and produces output that must be diffed to verify the fix landed.

### Evidence

Applied this session for the BACKLOG-010 fix and for the `--anonymize` flag in `report_builder.py`. Both smoke tests caught correct behavior on first run.
