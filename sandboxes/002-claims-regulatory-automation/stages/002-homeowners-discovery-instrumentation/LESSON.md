# Stage 002 Lessons

Stage: 002-homeowners-discovery-instrumentation
Pipeline version: 002.1.0
First run: 2026-06-03
Run ID: caba8e20-e894-42a3-b782-5e988113832a

---

## What This Stage Proved

The Stage 002 pipeline works end-to-end:

- Six corpus files (3 HTML KAR pages, 2 PDF DOI documents, 2 PDF-as-.html KRS statutes) became 40 source-traceable legal nodes, 42 formal citations, 5 broader references, 115 graph edges, 12 candidate evidence items, and a discovery report.
- All records carry `schema_version`, `run_id`, and `created_at`.
- Node IDs are deterministic under the current parsing strategy.
- Parser quality is visible through the parse warning system (2 `extension_mismatch` warnings for KRS PDFs saved with .html extensions).
- Docling parsed all PDFs without table failures; HTML parsing via BeautifulSoup was instant and produced well-structured blocks from KAR regulation pages.

---

## Parser Quality Observations

### KAR HTML pages (KY-KAR-806-14-006, KY-KAR-806-13-150)

- The Kentucky legislature KAR HTML structure is clean and deterministic: `<section class="section" data-level="N">` maps directly to legal hierarchy.
- Status: `success`, 48–75 blocks per source, parser fast (<0.1s).
- No warnings, no table failures.
- Metadata blocks (RELATES TO, STATUTORY AUTHORITY, NECESSITY) parse correctly.

### KRS statute files saved as PDF (KY-KRS-304-12-230, KY-KRS-304-14)

- Both files have `.html` extensions but contain PDF binary content. The pipeline detected this via magic bytes and emitted `extension_mismatch` warnings, routing to Docling.
- The small KRS statute PDF (4 KB) produced only 6 blocks with Docling — structural fidelity is limited for very small single-page PDFs. The first parse also triggered Docling model weight loading (~35s).
- The larger KRS chapter PDF (16 KB) produced 35 blocks and extracted 4 KRS citations correctly.
- Status: `partial` (due to extension mismatch warning).
- **Implication**: For future stages, download KRS statute HTML directly rather than using PDFs-saved-as-HTML.

### DOI PDFs (KY-DOI-BULLETIN-2026-01, KY-DOI-AO-2023-08)

- Docling parsed both successfully: 36 and 26 blocks.
- The larger advisory opinion (447 KB, multiple pages) parsed significantly faster than the small KRS PDFs — Docling performs better on multi-page text-layer PDFs than on tiny single-page PDFs.
- Status: `success`, no table failures.
- Model initialization took ~40s for the first PDF source in a cold session; subsequent sources reuse cached weights.

---

## Corpus Source Type Gap

The biggest lesson: **statutes, regulations, and DOI bulletins don't exhibit the same smells as insurance policy forms**.

The five active smells (overbroad exclusions, magic valuation terms, coverage inversion, calculation drift, regulatory mapping) are primarily smell patterns in:

- Homeowners **policy forms** (the insuring agreement, exclusions, conditions)
- Carrier **endorsements**
- Rate/manual **filings** (like the KNIC SERFF filing)

The statutory and regulatory sources in this slice are useful for:
- Extracting KRS/KAR citations (42 found)
- Confirming what the regulatory framework requires
- Identifying where carrier policies must map to law (smell 5)
- Identifying regulatory definitions of valuation terms (smell 2)

But they don't contain the smell-triggering language because statutes define requirements, not the contractual exclusions or unversioned rate references that insurance forms use.

---

## Candidate Evidence Analysis

### Smell 2: Magic Number / Magic Valuation Terms — 10 hits

- All 10 hits were for `SMELL2-H001` ("reasonable") in regulatory text.
- Most are standard administrative boilerplate ("reasonable administrative regulations", "reasonable investigation") rather than undefined valuation terms in claims settlement.
- **False positive rate is high** for regulatory sources on this heuristic.
- True positives: the DOI Bulletin hits on "reasonable investigation" and "reasonably justify the denial" are more interesting — they document what the DOI considers a reasonable claims process without defining what "reasonable" means numerically.
- **For Stage 003**: Add source-type filtering to candidate evidence. `krs_statute` and `kar_regulation` hits on SMELL2-H001 should be demoted; `doi_bulletin` and carrier policy form hits should be promoted.

### Smell 4: Calculation Rule Drift — 2 hits

- Both hits were for `SMELL4-H003` ("underwriting guidelines") in the DOI Bulletin.
- The DOI Bulletin's requirement that insurers "specify the specific property conditions noncompliant with the insurer's underwriting guidelines" without requiring those guidelines to be versioned or filed is a real smell-4 instance.
- **This is good candidate evidence.** A reviewer should ask: are the underwriting guidelines referenced here filed with the DOI and versioned?

### Smells 1, 3, 5: No hits

- **Smell 1** (Overbroad Exclusions): The context filter requiring proximity to exclusion language (`exclud`, `does not cover`, etc.) correctly suppressed hits in regulatory text. No false positives. No true positives — regulatory sources don't use exclusion language.
- **Smell 3** (Coverage Inversion): Correctly suppressed. Coverage inversion requires policy form language.
- **Smell 5** (Regulatory Mapping): The KRS-nearby filter correctly identified that official regulatory documents DO cite KRS properly — the null reference smell is not present in statutes or DOI bulletins. It is more likely to appear in carrier policy forms that use "as required by state law" without a citation.

---

## What This Corpus Slice Cannot Prove

- Smells 1, 3, and 5 require **carrier policy form text** — the base homeowners form, endorsements, conditions. None of the six selected sources are policy forms.
- Smell 4 requires a **SERFF rate/rule filing** (e.g., KY-SERFF-KNIC-127064322) to find unversioned manual references in carrier-filed rate rules.
- The KNIC SERFF filing (~988 KB) was intentionally excluded from this first slice due to size; it is the next obvious corpus addition for smells 1, 3, 4.

---

## Node Count Observation

40 nodes from 226 blocks is lower than ideal. This is a segmenter artifact:

- The segmenter merges consecutive paragraph and list-item blocks under the most recent heading node, producing fewer but richer nodes.
- The KRS PDFs produced very few nodes (2 each) because Docling's output for small PDFs has limited structure — mostly paragraphs without headings.
- The KAR HTML sources produced 11–16 nodes each, which is reasonable.

**For Stage 003**: Consider whether paragraph-level nodes should also be created as separate retrieval targets rather than merged into heading nodes. This would increase node count and improve retrieval granularity.

---

## Recommendations for Stage 003

1. **Add carrier policy form sources** — at minimum one homeowners base form (HO-3 or similar) to get smell-1 and smell-3 coverage. The KNIC SERFF filing is the best available source for this.
2. **Add source-type weight to candidate evidence** — regulatory source + SMELL2-H001 should be lower confidence than carrier form + SMELL2-H001.
3. **Re-download KRS statute sources as HTML** — the PDF-as-HTML encoding limits Docling's structural output. The KRS statute pages render as clean HTML when accessed directly.
4. **Consider paragraph-level retrieval nodes** — merge behavior in the segmenter reduces retrieval granularity. A flat paragraph node index alongside the hierarchical heading nodes may improve retrieval recall.
5. **Build smell-specific queries** for the gold set using the 10 smell-2 evidence items and 2 smell-4 items already found.
6. **Pre-warm Docling per session** — the first Docling call per run loads model weights (~35–40s). A warm-up call at pipeline startup would reduce apparent per-source latency.
