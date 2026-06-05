# Lesson: Regional DOI Enforcement Actions Are Behind FOIA Walls

Date: 2026-06-05
Session: Backlog implementation session C/D
Source: BACKLOG-015 case library research
Related: `sandboxes/004-expert-drilldown/data/case_library.json`, `dollar_anchors.json`

---

## Problem or Question

When building a heuristic-matched case library for regulatory gap heuristics (SMELL4-H001, SMELL5-H004, H006), we needed specific enforcement actions from regional DOI offices (KY, TN, OH, WV) to document that these exact violation patterns have been cited by regulators. Web search and direct portal access returned nothing.

Why?

---

## Why It Mattered

Without real enforcement examples, the risk framing for regulatory gap heuristics is based on mechanism only ("DOI exams exist and produce fines") rather than named precedent ("DOI found X at carrier Y and ordered Z"). Named precedent is materially stronger in a prospect conversation.

---

## Pattern: FOIA Wall Is Systematic, Not Incidental

DOI market conduct exam reports for KY, TN, OH, and WV are systematically not publicly indexed on the web. This is not a gap in our search — it is a structural feature of how these agencies operate:

- KY DOI: market conduct portal returns 404; KY DOI website acknowledges exam reports exist but does not publish them
- TN DOI: enforcement page not publicly indexed via web search
- OH DOI: enforcement portal returns 404
- WV Insurance Commission: login-gated portal; no public enforcement index
- NAIC central enforcement database: covers only *unlicensed* carriers, not rate/methodology compliance violations by licensed carriers
- Property Insurance Coverage Law Blog confirmed: Oklahoma only publishes exam reports on FOIA request; last public one was 2009 — pattern consistent across region

**The Merlin Law Group blog post title says it well: "The Case of the Missing Market Conduct Exams."**

---

## Pattern: Correct Framing When Examples Are Behind FOIA Walls

Do not claim the enforcement actions don't exist. Claim the mechanism is documented and the specific examples are behind a records wall:

> "Market conduct exams for this class of violation are documented at the $750K–$2.5M range (FL OIR, LA DOI, SD DLR — all sourced). Kentucky DOI acknowledges equivalent examinations on its own website. Specific Kentucky findings are not publicly indexed — an open records request (502-564-3630) is the retrieval path."

This is honest, defensible, and does not understate the risk.

---

## Pattern: Source Citations Catch Factual Errors

When we added `source_url` fields to `dollar_anchors.json`, we found two factual errors that had been carried forward from project research without verification:

1. State Farm $15.6M "property claims" settlement — actually an **Arkansas auto** total-loss case (Chadwick v. State Farm, E.D. Ark.). The ACV methodology dispute pattern is analogous but the specific case was auto, not homeowners.
2. Louisiana fines described as "nearly $1 million" — confirmed figure is **$764,750**. Overstated by ~$235K.

Both errors were invisible until URLs were added and the sources checked. Lesson: source citations are a correctness control, not just a provenance record.

---

## Concrete Example

`dollar_anchors.json` before and after:

Before:
```json
"dollar_figure": "~$1 million proposed fines"
```

After (verified):
```json
"dollar_figure": "$764,750 proposed fines across five carriers",
"source_url": ["https://www.insurancejournal.com/news/southcentral/2022/04/18/663381.htm"],
"source_note": "Verified 2026-06-05 via Insurance Journal (April 18, 2022)."
```

---

## What To Reuse Next Time

- [ ] When researching regional enforcement actions, expect FOIA walls for KY/TN/OH/WV. Don't spend more than one search round per state.
- [ ] Document gap sentinels with the search sources tried, the FOIA barrier, and the open records path — not just "no case found."
- [ ] Always add `source_url` to dollar anchor entries. No figure should be asserted without a note on where it came from.
- [ ] Use the documented enforcement mechanism (FL OIR, LA DOI, SD DLR) as the risk anchor when specific regional examples are unavailable.
- [ ] When a source can't be fetched (403, PDF binary), note the barrier and the fallback source used. Do not mark [VERIFY] and move on without noting why.

---

## Limitations

- This lesson applies to KY/TN/OH/WV. California CDI, Florida OIR, and NY DFS publish enforcement actions publicly and are searchable. Regional variation exists.
- FOIA requests may or may not produce results depending on the state's open records law and the specificity of the request. KY open records requests (KRS 61.870) are generally honored for regulatory actions.
- The SD DLR exam report PDF was found publicly; South Dakota appears to be more transparent than the target states.
