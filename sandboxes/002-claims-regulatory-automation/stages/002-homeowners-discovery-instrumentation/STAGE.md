# Stage 002: Homeowners Discovery And Instrumentation

Status: Complete; preserved as first discovery-and-instrumentation stage
Location: `stages/002-homeowners-discovery-instrumentation/`
Sandbox: 002 — Kentucky homeowners insurance
Created: 2026-06-03

> Current Sandbox 002 state is summarized in `../../CLOSURE.md`; the repository root `README.md` controls current project work. `../../HANDOFF-2026-06-04b.md` is a historical closure-era snapshot.

## Completion Checklist

- [x] Implement the deterministic JSONL-first pipeline.
- [x] Repair the output to the artifact contract.
- [x] Preserve the 28-source, 353-node run used downstream.
- [x] Freeze the stage at Sandbox 002 closure.

## Objective

Build a deterministic, JSONL-first discovery-and-instrumentation pipeline over a small Kentucky homeowners corpus subset.

Turn selected real corpus files into source-traceable legal evidence records, parser diagnostics, conservative graph edges, future-compatible retrieval bundles, and candidate evidence for the five active smells.

## Selected Sources

Six sources selected from `corpus/kentucky-homeowners-policy-smells/_download_manifest.csv`.
Target: roughly one source per smell, two source types (HTML KAR pages, PDF DOI/SERFF documents).

| source_id | source_type | size | file_type | smells |
|---|---|---|---|---|
| KY-KRS-304-12-230 | krs_statute | 4 KB | PDF saved as .html | 2, 5 |
| KY-KRS-304-14 | krs_statute | 16 KB | PDF saved as .html | 1, 2, 3, 5 |
| KY-KAR-806-14-006 | kar_regulation | 55 KB | HTML | 1, 3, 5 |
| KY-KAR-806-13-150 | kar_regulation | 88 KB | HTML | 4, 5 |
| KY-DOI-BULLETIN-2026-01 | doi_bulletin | 127 KB | PDF | 1, 5 |
| KY-DOI-AO-2023-08 | doi_bulletin | 447 KB | PDF | 2, 3, 5 |

### Smell coverage

| Smell | Sources |
|---|---|
| 1 — Overbroad/Non-deterministic Exclusions | KY-KRS-304-14, KY-KAR-806-14-006, KY-DOI-BULLETIN-2026-01 |
| 2 — Magic Number/Magic Valuation Terms | KY-KRS-304-12-230, KY-KRS-304-14, KY-DOI-AO-2023-08 |
| 3 — Coverage Inversion/Contradictory Conditions | KY-KRS-304-14, KY-KAR-806-14-006, KY-DOI-AO-2023-08 |
| 4 — Calculation Rule Drift/Unversioned Rate Reference | KY-KAR-806-13-150 (sparse — no SERFF filing in this slice) |
| 5 — Regulatory Mapping Smells | all six |

Smell 4 coverage is intentionally thin in this slice. The KNIC SERFF filing (KY-SERFF-KNIC-127064322, ~988 KB) is the richer smell-4 source. It is a known gap for this first pass.

## Parser Notes

Two KRS statute files were saved with `.html` extensions but contain PDF binary content. The pipeline detects this via magic bytes, routes them to the Docling PDF parser, and emits `extension_mismatch` parse warnings for each.

- HTML parser: targets the Kentucky legislature KAR HTML structure (`<section class="section" data-level="N">`)
- PDF parser: Docling 2.93.0 (verified installed)

## Key Constraints

- No final legal findings — only candidate evidence
- No vector store or semantic retrieval
- No LLM in the main pipeline
- No manual reviewer annotations
- No cross-document topic modeling
- All records carry `schema_version`, `run_id`, `created_at`
- Node IDs are deterministic under this parsing strategy; changes that break ID stability require a schema version bump

## Outputs

See `output/` after running the pipeline:

```
python src/pipeline.py --manifest data/source_manifest_subset.csv
```

All outputs are relative to this stage directory. The corpus files are read from the absolute paths in the manifest.

## Limitations

- Smell 4 candidate evidence is sparse without the SERFF filing
- Docling parsing of small KRS PDFs may produce limited structure (short single-section documents)
- No endorsement-level or schedule-level parsing in this slice
- Graph edges are conservative — no cross-document edges in Stage 002
