# ADR-011: H003 Findings Reclassified — Undisclosed Calculation Methodology (Smell 4), Not Undefined Term (Smell 2)

Date: 2026-06-04
Status: Accepted
Deciders: Dorian Klingenberg, Claude Code

---

## Context

During Sandbox 004 scoping, the question was raised: is ACV actually undefined in the carrier filings, or is it defined in the base ISO policy form that is not in our corpus?

Inspection of the corpus node structure revealed:
- Neither the KNIC nor KFBM corpus contains a definitions section that covers "actual cash value" or "replacement cost."
- The base ISO homeowners policy form (HO 00 03, HO 00 05) — which is where ACV is typically defined in a standard homeowners policy package — is **not in our corpus**.
- SERFF filings contain rate manuals, endorsements, condition amendments, and rate data. The base ISO form is filed separately and is not included in the SERFF filing documents we downloaded.

The base ISO HO 00 03 form does define ACV, typically as: "fair and reasonable cost to repair or replace property with the same material and quality, minus physical deterioration and depreciation." Carriers file this form with the DOI as part of their policy package.

What the carrier filings we do have — endorsements, rate manuals, condition amendments — do NOT contain is:
- The calculation methodology for ACV: whether labor costs are depreciated, which depreciation schedule is used, which external tool (Xactimate, CoreLogic, Marshall & Swift) produces the figure
- Any citation to the tool, index, or methodology that will be applied at time of claim
- Any versioned reference to the base form or valuation standard being used

This is the pattern that produced the labor depreciation class-action wave beginning in 2015: carriers had a term defined in the base form, but the specific methodology applied at claim time — depreciating labor costs — was nowhere disclosed in the policy package.

---

## Decision

**H003 findings are reclassified from Smell 2 (undefined magic term) to Smell 4 (unversioned/undisclosed external methodology).**

The finding is not "ACV is undefined." The finding is: "The ACV calculation methodology — specifically, whether labor costs are depreciated, which external tool or index produces the figure, and what version of that tool applies — is not disclosed anywhere in the filed endorsements or rate documents. A claimant cannot determine from the policy package how their settlement amount will be calculated."

This framing is:
1. **Defensible** — it survives the response "ACV is defined in the base form." The response to that is: "Correct, and that definition does not specify the calculation methodology your adjusters will apply."
2. **Matched to the actual litigation pattern** — the labor depreciation class actions were not about ACV being undefined; they were about carriers applying a specific undisclosed methodology (depreciating labor).
3. **Correctly categorized** — this is a Smell 4 pattern (unversioned/unspecified external reference), not a Smell 2 pattern (undefined term).

---

## Alternatives Considered

### 1. Keep H003 findings as Smell 2 — Rejected

"ACV is undefined in this filing" is dismissible in a client conversation by pointing to the base policy form. A compliance officer or coverage attorney can close that finding in thirty seconds. It does not survive professional scrutiny.

### 2. Discard H003 findings entirely — Rejected

The underlying gap is real and consequential. The labor depreciation class actions are direct evidence that this exact gap — an undisclosed ACV calculation methodology — causes material harm. Discarding the findings would be a false negative.

### 3. Reclassify to Smell 4 with corpus caveat — Accepted

H003 detector output is valid as a signal that ACV/replacement cost appears in a loss settlement context without a methodology anchor. The filing does not disclose how that value will be calculated. This is a Smell 4 finding: the methodology is externally determined at claim time but is not cited, versioned, or disclosed in the filing.

---

## Consequences

### Immediate

- All H003 findings in `enriched_findings.jsonl` carry the wrong smell classification. The detector findings themselves remain valid evidence; the framing in any human-facing output (drill-down report, executive summary) must use the Smell 4 framing.
- The executive summary currently describes H003 as "undefined valuation terms." This is partially accurate but should be sharpened in the next report generation to "undisclosed valuation methodology."
- The drill-down report (BACKLOG-017) must use the Smell 4 framing for all H003 entries.

### Corpus

- **ISO base forms are treated as an implicit gold standard and will not be procured (decided 2026-06-04).** ISO HO 00 03 and HO 00 05 define ACV — this is established fact in insurance regulation and litigation, documented in decades of case law. We do not need to hold a copy to assert it. SERFF searches for both KNIC (form filings KNIC-132500003, KNIC-133829383) and KFBM (full form filing history) found no independently filed ISO base forms — consistent with standard industry practice of licensing ISO forms by reference rather than re-filing them.
- KFBM uses a proprietary base form (HO 04 93), which is already in corpus. The H003 drill-down entry for KFBM can be grounded directly in that form.
- For KNIC, we assert from established industry knowledge that the ISO base form defines ACV but does not specify depreciation methodology. No copy is required to make the finding.
- BACKLOG-018 (ISO base form procurement) is closed. The gap record ISO-HO-BASE-FORMS in KNOWN-GAPS.md is retained for reference but is not an active collection target.

### Detectors

- The H003 detector heuristic is correctly identifying the pattern (ACV/RC in loss settlement context without methodology anchor). No change to the detector code is needed.
- The `smell_name` and `heuristic_id` fields in findings will remain as-is. The reframing is applied at the report and drill-down entry layer, not at the finding data layer.
- A future detector improvement (BACKLOG-006 / BACKLOG-008 scope) could explicitly check for an external tool citation near ACV/RC terms and emit a Smell 4 finding directly. Not required now.

### BACKLOG

- BACKLOG-008 (Smell 2 / Smell 4 miscategorization) is resolved by this ADR. The resolution is: H003 findings are Smell 4, not Smell 2.

---

## Evidence

- Corpus node inspection (2026-06-04): zero definition-section nodes for ACV or replacement cost in KNIC or KFBM carrier sources.
- ISO HO 00 03 form structure: publicly documented; base form defines ACV but does not specify calculation methodology.
- Labor depreciation class-action wave (2015+): established that ACV methodology gaps — not undefined ACV — are the litigation trigger. Documented in `002-ROI-CASES-FIVE-SMELLS.md`.
- Human review notes, Stage 001 (`validation/human-review-notes.md`): BACKLOG-008 flagged this exact issue during the first Sandbox 003 review pass.
