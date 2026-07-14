# Lessons — Sandbox 004: Expert Drill-Down Report

---

## Lesson 1: Internal disclosure is useful only with an explicit package boundary

**What happened:** We initially assumed we needed ISO HO 00 03/05 base forms to make the H003 (ACV methodology) finding. SERFF searches found no independently filed ISO base forms for either carrier. The question "do we even need these?" led to the key insight.

**The lesson:** When auditing filed documents, prefer the narrower question "is X disclosed in the material reviewed?" over an unsupported comparison with an external standard. If the public package is incomplete, the report must distinguish a corpus limitation from a confirmed filing defect.

**Application:** Before procuring external reference material, ask whether the finding can be made from the carrier's own documents alone. If yes, external procurement is nice-to-have, not required.

---

## Lesson 2: SERFF defaults to the last-used state — always use direct state URLs

**What happened:** Navigating to SERFF Filing Access landed in Michigan (the last-used state from a prior session), not Kentucky. This caused confusion and wasted time.

**The lesson:** SERFF Filing Access is state-partitioned. The site does not auto-detect or prompt for state — it silently serves the last-used state. Direct state home URLs bypass this:
- Kentucky: `https://filingaccess.serff.com/sfa/home/KY`

**Application:** Log the direct state URL in `CORPUS-SOURCES.md` under "Procurement URLs" whenever a new state is searched. Never navigate via the root URL without knowing which state will be selected.

---

## Lesson 3: Verify a form's role before inferring carrier architecture

**What happened:** Early notes treated KFBM's HO 04 93 as a proprietary base form. Later source verification established that ISO HO 04 93 is a roof-surfacing ACV endorsement. KFBM's actual base-jacket form number remains unknown.

**The lesson:** A form number or SERFF attachment is not enough to infer whether a document is a jacket, endorsement, schedule, or amendment. Validate the document role before describing a carrier as an ISO adopter, diverger, or proprietary-form target. Package complexity may still be valuable, but that remains a tested hypothesis rather than a fact derived from HO 04 93.

**Application:** When selecting corpus carriers or scoping new engagements, record the evidence for every form-role and adoption claim. If the base package is unavailable, name that limitation and target issue classes that the available documents can actually support.

---

## Lesson 4: The drill-down report is stronger when grounded in concrete claim scenarios

**What happened:** The H003 entry is the most compelling of the three because it ties the gap directly to a high-frequency, high-value claim type (windstorm/hail, roof surfacing) affecting a large proportion of the active book (roofs older than 7 years). The KFBM 7-year rule made the exposure concrete and quantifiable in a way that more abstract findings cannot.

**The lesson:** For each drill-down entry, identify the relevant claim scenario, exposure evidence if it is actually available, and the closest verified legal or regulatory anchor. Do not infer a book-wide exposure percentage or "live liability" from a filing clause alone.

**Application:** When building drill-down entries, start with the claim scenario before writing the compliance citations. The scenario anchors the reader; the citations support it.

---

## Lesson 5: The four structural gap types (Jem framework) map cleanly to existing work

**What happened:** External input from Jem identified four structural gap types that a SERFF filing auditor should target. Three of the four were already partially or fully implemented in Sandbox 002.

**The lesson:** The "isolated graph database per filing package" framing (extract manifest → cross-reference payload → flag vacuums) is exactly what Stage 003 retrieval bundles and Stage 006 Smell 5 gap detection already implement. The vocabulary was missing, not the implementation. When external input provides cleaner vocabulary for existing work, update the documentation — it sharpens the product story and makes the engineering more legible.

**Application:** Review new framing inputs against existing ADRs and detector code before adding new backlog items. Often the implementation exists; the framing is what needs updating.
