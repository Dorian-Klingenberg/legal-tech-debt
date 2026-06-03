# Stage 002 Discovery Report

Run ID: `caba8e20-e894-42a3-b782-5e988113832a`
Created: 2026-06-03T16:46:34.594289+00:00
Pipeline: 002.1.0

---

## Sources

6 sources processed.

| source_id | type | detected | ext_ok | blocks | nodes |
|---|---|---|---|---:|---:|
| KY-KRS-304-12-230 | krs_statute | pdf | ✗ | 6 | 2 |
| KY-KRS-304-14 | krs_statute | pdf | ✗ | 35 | 2 |
| KY-KAR-806-14-006 | kar_regulation | html | ✓ | 48 | 11 |
| KY-KAR-806-13-150 | kar_regulation | html | ✓ | 75 | 16 |
| KY-DOI-BULLETIN-2026-01 | doi_bulletin | pdf | ✓ | 36 | 4 |
| KY-DOI-AO-2023-08 | doi_bulletin | pdf | ✓ | 26 | 5 |

## Parser Summary

- **KY-KRS-304-12-230**: docling_2.93.0, status=partial, 6 blocks, 1 warnings, 0 table failures, 35.6s
- **KY-KRS-304-14**: docling_2.93.0, status=partial, 35 blocks, 1 warnings, 0 table failures, 4.8s
- **KY-KAR-806-14-006**: html_bs4_kar_v1, status=success, 48 blocks, 0 warnings, 0 table failures, 0.0s
- **KY-KAR-806-13-150**: html_bs4_kar_v1, status=success, 75 blocks, 0 warnings, 0 table failures, 0.0s
- **KY-DOI-BULLETIN-2026-01**: docling_2.93.0, status=success, 36 blocks, 0 warnings, 0 table failures, 40.2s
- **KY-DOI-AO-2023-08**: docling_2.93.0, status=success, 26 blocks, 0 warnings, 0 table failures, 3.5s

## Counts

- Blocks: 226
- Nodes: 40
- Citations: 42
- References: 5
- Edges: 115
- Table failures: 0
- Parse warnings: 2
- Candidate evidence: 12
- Retrieval bundles: 5

## Candidate Evidence by Smell

### Smell 1: Overbroad / Non-deterministic Exclusions

No candidate evidence found in this corpus slice.

### Smell 2: Magic Number / Magic Valuation Terms

10 candidate evidence items.

- **SMELL2-H001** in `KY-KRS-304-14` at `KY-KRS-304-14 > 304.14-120   Filing and approval of forms.`
  - "Reasonable" without a defined standard or formula is a magic valuation term
  - Evidence: _all  state  the  grounds therefor and the particulars thereof in such detail as reasonably to inform the insurer. (b) An_
  - Parser confidence: medium
  - Reviewer question: Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?

- **SMELL2-H001** in `KY-KAR-806-14-006` at `KY-KAR-806-14-006::meta::6fdb16291505b9feefbd`
  - "Reasonable" without a defined standard or formula is a magic valuation term
  - Evidence: _NCTION, AND CONFORMITY: KRS 304.2-110 authorizes the commissioner to promulgate reasonable administrative regulations ne_
  - Parser confidence: high
  - Reviewer question: Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?

- **SMELL2-H001** in `KY-DOI-BULLETIN-2026-01` at `KY-DOI-BULLETIN-2026-01 > BULLETIN 2026-01`
  - "Reasonable" without a defined standard or formula is a magic valuation term
  - Evidence: _he claim or coverage at issue, or to refuse to pay a claim without conducting a reasonable investigation based upon all _
  - Parser confidence: high
  - Reviewer question: Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?

- **SMELL2-H001** in `KY-DOI-BULLETIN-2026-01` at `KY-DOI-BULLETIN-2026-01 > BULLETIN 2026-01`
  - "Reasonable" without a defined standard or formula is a magic valuation term
  - Evidence: _capture ""all available information" relevant to a claim and, therefore, cannot reasonably justify the denial of a prope_
  - Parser confidence: high
  - Reviewer question: Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?

- **SMELL2-H001** in `KY-DOI-BULLETIN-2026-01` at `KY-DOI-BULLETIN-2026-01 > BULLETIN 2026-01`
  - "Reasonable" without a defined standard or formula is a magic valuation term
  - Evidence: _elling or nonrenewing policies based on those images. Providing insureds with a reasonable opportunity to submit evidenc_
  - Parser confidence: high
  - Reviewer question: Is this term defined in the policy or by a specific versioned standard a reviewer can locate at time of loss?

  _(+ 5 more — see candidate_evidence.jsonl)_

### Smell 3: Coverage Inversion / Contradictory Conditions

No candidate evidence found in this corpus slice.

### Smell 4: Calculation Rule Drift / Unversioned Rate Reference

2 candidate evidence items.

- **SMELL4-H003** in `KY-DOI-BULLETIN-2026-01` at `KY-DOI-BULLETIN-2026-01 > BULLETIN 2026-01`
  - "Guidelines" reference without version or filing anchor — unversioned calculation dependency
  - Evidence: _alize the specific property conditions that are noncompliant with the insurer's underwriting guidelines; (2) the images _
  - Parser confidence: high
  - Reviewer question: Is the calculation rule or referenced manual anchored to a specific version, edition, or filing date?

- **SMELL4-H003** in `KY-DOI-BULLETIN-2026-01` at `KY-DOI-BULLETIN-2026-01 > BULLETIN 2026-01`
  - "Guidelines" reference without version or filing anchor — unversioned calculation dependency
  - Evidence: _ifies the specific property conditions that are noncompliant with the insurer's underwriting guidelines; and (3) the ima_
  - Parser confidence: high
  - Reviewer question: Is the calculation rule or referenced manual anchored to a specific version, edition, or filing date?


### Smell 5: Regulatory Mapping Smells

No candidate evidence found in this corpus slice.

## Parse Warnings

- **extension_mismatch** in `KY-KRS-304-12-230`: File has .html extension but PDF magic bytes detected; routing to Docling PDF parser. Source: KY-KRS-304-12-230.html
- **extension_mismatch** in `KY-KRS-304-14`: File has .html extension but PDF magic bytes detected; routing to Docling PDF parser. Source: KY-KRS-304-14.html

## Table Failures

No table failures.

## Known Gaps

- Smell 4 coverage is sparse. The KNIC SERFF rate/rule filing (KY-SERFF-KNIC-127064322, ~988 KB) was not included in this slice.
- No endorsement-level or schedule-level parsing in this slice.
- KRS statute pages were saved as PDFs with .html extensions; Docling parsed them but structural fidelity depends on PDF content quality.
- No cross-document edges. Each source is processed independently.

---

_This report is generated output. Do not edit manually._
_Candidate evidence items are not legal findings._
