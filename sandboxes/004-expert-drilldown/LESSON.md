# Lessons — Sandbox 004: Expert Drill-Down Report

---

## Lesson 1: Ground truth is internal disclosure, not external standard

**What happened:** We initially assumed we needed ISO HO 00 03/05 base forms to make the H003 (ACV methodology) finding. SERFF searches found no independently filed ISO base forms for either carrier. The question "do we even need these?" led to the key insight.

**The lesson:** When auditing a carrier's filed documents, the finding is "your own documents don't disclose X" — not "you differ from ISO." ISO content is established fact in litigation and regulation; we can assert it without holding a copy. Phase 1 product findings are entirely self-contained within the carrier's own SERFF filing package.

**Application:** Before procuring external reference material, ask whether the finding can be made from the carrier's own documents alone. If yes, external procurement is nice-to-have, not required.

---

## Lesson 2: SERFF defaults to the last-used state — always use direct state URLs

**What happened:** Navigating to SERFF Filing Access landed in Michigan (the last-used state from a prior session), not Kentucky. This caused confusion and wasted time.

**The lesson:** SERFF Filing Access is state-partitioned. The site does not auto-detect or prompt for state — it silently serves the last-used state. Direct state home URLs bypass this:
- Kentucky: `https://filingaccess.serff.com/sfa/home/KY`

**Application:** Log the direct state URL in `CORPUS-SOURCES.md` under "Procurement URLs" whenever a new state is searched. Never navigate via the root URL without knowing which state will be selected.

---

## Lesson 3: KFBM is the higher-value corpus target — proprietary form carriers generate more findings

**What happened:** KFBM's HO 04 93 is a proprietary base form, not ISO. Every deviation from industry standard is untested by decades of case law. KNIC licenses ISO by reference and has fewer filing-layer anomalies.

**The lesson:** Target carriers based on ISO divergence, not carrier size. The legal tech debt lives in: proprietary base forms, heavy endorsement stacks that override ISO provisions, and proprietary rate/underwriting methodologies. Pure ISO adopters are low-value targets; heavy divergers are high-value.

**Application:** When selecting corpus carriers or scoping new engagements, check whether the carrier uses ISO base forms or proprietary forms. Proprietary-form carriers warrant deeper analysis.

---

## Lesson 4: The drill-down report is stronger when grounded in concrete claim scenarios

**What happened:** The H003 entry is the most compelling of the three because it ties the gap directly to a high-frequency, high-value claim type (windstorm/hail, roof surfacing) affecting a large proportion of the active book (roofs older than 7 years). The KFBM 7-year rule made the exposure concrete and quantifiable in a way that more abstract findings cannot.

**The lesson:** For each drill-down entry, identify: (1) the most common claim type the gap affects; (2) the proportion of the book at risk; (3) a named legal precedent matching the exact gap. These three elements move the finding from "interesting observation" to "this is a live liability."

**Application:** When building drill-down entries, start with the claim scenario before writing the compliance citations. The scenario anchors the reader; the citations support it.

---

## Lesson 5: The four structural gap types (Jem framework) map cleanly to existing work

**What happened:** External input from Jem identified four structural gap types that a SERFF filing auditor should target. Three of the four were already partially or fully implemented in Sandbox 002.

**The lesson:** The "isolated graph database per filing package" framing (extract manifest → cross-reference payload → flag vacuums) is exactly what Stage 003 retrieval bundles and Stage 006 Smell 5 gap detection already implement. The vocabulary was missing, not the implementation. When external input provides cleaner vocabulary for existing work, update the documentation — it sharpens the product story and makes the engineering more legible.

**Application:** Review new framing inputs against existing ADRs and detector code before adding new backlog items. Often the implementation exists; the framing is what needs updating.
