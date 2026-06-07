# Executive Summary: What I Have Been Working On

Status: Working draft  
Audience: Family / non-technical reader  
Purpose: Explain the project clearly, including why the work may have economic value

---

## Short Version

I have been working on a focused AI and legal-technology project called **Legal Tech Debt**.

The idea is simple: legal and regulatory documents can accumulate hidden problems the same way software systems do. Insurance policies, rate manuals, forms, endorsements, and regulations often depend on one another. Over time, they can develop unclear definitions, missing citations, outdated references, contradictory wording, or rules that are hard to trace back to the law.

Those issues may sit quietly in documents for years. But when they appear during a claim dispute, lawsuit, class action, regulator review, or market conduct examination, they can become expensive.

My work is about finding those problems earlier.

The near-term goal is not to replace lawyers or compliance professionals. It is to build a review tool that gives them better evidence:

- here is a possible problem,
- here is the source document,
- here is why it may matter,
- here is what a human expert should check next.

---

## Why This Fits The Moment

Canada is investing heavily in artificial intelligence. In Budget 2024, the federal government announced a **CAD 2.4 billion AI package** to support AI compute infrastructure, AI adoption, safety, and Canadian AI companies. A major part of that is the **CAD 2 billion Canadian Sovereign AI Compute Strategy**, which is meant to give Canadian researchers, companies, and innovators better access to domestic AI computing capacity.

This matters because AI is moving from novelty into infrastructure. The serious opportunities are not only chatbots or image generation. They are specialized tools that help professionals do complex work faster, with better evidence and better review.

Legal and regulatory compliance is one of those areas. It is document-heavy, expensive, detail-oriented, and risky when mistakes are missed.

---

## The Problem

Insurance companies operate inside a dense web of documents:

- policy forms,
- endorsements,
- rate manuals,
- underwriting rules,
- state laws,
- administrative regulations,
- regulator filings,
- claim settlement standards,
- bureau forms,
- internal product specifications.

These documents are not independent. A policy phrase may depend on a regulation. A rate rule may depend on a filing. A claim settlement method may depend on both policy wording and state law. A single unclear phrase can affect many claims or many policyholders.

The problem is that these relationships are often not easy to see.

A document might say "actual cash value" without explaining how that value is calculated. A rate manual might refer to "the Manual for that state" without saying which version. A filing might describe a rating factor without clearly citing the Kentucky law or regulation that authorizes it. A policy may use timing language like "reasonable time" without defining what that means.

Each of those may look small. But in insurance, small wording gaps can scale across an entire book of business.

---

## The Money Argument

The financial value is prevention.

Insurance companies already spend money on legal review, compliance review, policy filings, claim disputes, market conduct exams, remediation, and outside counsel. This project is not trying to create a brand-new budget category. It is trying to make an existing expensive activity more targeted and more evidence-based.

The business case is that finding a problem early is cheaper than discovering it later.

A wording gap or filing problem may be inexpensive to fix while it is still just a document issue. It may require a policy clarification, a filing amendment, a better citation, or a more explicit definition.

But if the same gap is discovered later by a regulator, plaintiff attorney, claims dispute, or class action, the cost can be much higher. The carrier may face legal fees, re-filing work, claim reprocessing, regulatory penalties, customer complaints, settlement exposure, and reputational damage.

The economics do not require the tool to prevent every possible problem. Even partial prevention can matter.

For example:

> If a structured review costs tens of thousands of dollars and helps prevent, reduce, or better prepare for a million-dollar dispute, examination, or remediation event, the review can justify itself.

That is the core financial argument.

It is not "AI will magically make money." It is:

> Insurance compliance mistakes are already expensive. AI-assisted evidence review may help find some of them earlier, while they are still cheaper to address.

---

## Why Insurance Is A Good Starting Point

Insurance is a practical starting domain because it has three things at once:

1. **High document complexity.** Policies, endorsements, rate manuals, filings, and regulations all interact.
2. **Real financial consequences.** Ambiguous wording can lead to claim disputes, litigation, regulatory findings, or class-action exposure.
3. **Reviewable evidence.** The source documents exist. A tool can point to the exact provision, citation, or missing connection that needs human review.

This makes insurance a better fit than a vague, general-purpose AI idea.

The work is not "ask AI what the law means." It is closer to a specialized inspection tool:

> Scan the documents. Detect known risk patterns. Preserve the evidence. Give the expert a clear review path.

---

## What Has Been Built So Far

This is currently a proof of concept, not a finished company or production platform.

The project has already built:

- a Kentucky homeowners insurance research corpus,
- document parsing and evidence extraction,
- deterministic detectors for several policy and filing risk patterns,
- source-traceable findings,
- an executive summary report,
- an expert drill-down report,
- carrier-specific report variants,
- copyright-safe sanitized output that avoids reproducing protected policy text,
- a draft direction for an interactive review workbench.

The current prototype focuses on Kentucky homeowners insurance because a narrow, real-document test is more useful than a broad hypothetical one.

---

## What The Tool Looks For

The project looks for "legal code smells" in insurance documents. These are patterns that suggest a document may be hard to interpret, hard to audit, or risky in a claim or regulatory setting.

Examples include:

- undefined valuation terms,
- unclear timing standards,
- unversioned references to external manuals,
- rate methods without clear regulatory citations,
- claim settlement methods that are not fully explained,
- missing links between policy language and regulatory authority.

These findings are not automatic legal conclusions. They are review leads. A human expert still decides whether the finding is valid, serious, and worth fixing.

That distinction is important. The project is meant to support expert judgment, not replace it.

---

## What Makes This Different From A Generic AI Tool

Most AI tools summarize text or answer questions. That can be useful, but it is not enough for legal or compliance work.

This project is different because it is built around evidence:

- every finding should trace back to source documents,
- uncertainty should be visible,
- the tool should separate internal evidence from commercial-safe summaries,
- the output should be readable by compliance, legal, claims, and product people,
- the system should avoid pretending to give legal advice.

The product idea is not a chatbot. It is a review report or workbench that helps experts inspect risk patterns faster and more consistently.

---

## Why This Might Become A Business

The potential buyer is an insurance carrier, compliance team, product/forms team, legal department, consulting firm, or regulatory review group.

The first product does not need to be a full subscription software platform. A focused expert review report could be enough if it helps a carrier answer questions like:

- Where are our policy wording gaps?
- Which findings are most likely to create claim disputes?
- Which rate or filing rules are hard to trace back to authority?
- What should counsel or compliance review first?
- What should we fix before a regulator or plaintiff attorney finds it?

That is a concrete business use case.

The early product could look more like a specialized audit report than a subscription platform. That keeps validation cheaper and more realistic before building expensive infrastructure.

---

## What This Could Mean Financially For Me

The personal financial argument is not that this is already a business. It is that the project may not need to become a large company before it becomes worth testing seriously.

So far, the proof of concept has examined only **two insurance carriers in one state**: Kentucky homeowners insurance. It has also focused on only **five policy-layer smell categories**, while the larger taxonomy contains many more possible smell patterns across policy wording, rating, underwriting, claims, regulatory mapping, and system traceability.

That means the current work has tested only a small slice of the possible market. It is evidence that the method can produce useful-looking findings at prototype scale, not proof that customers will buy it or that the whole market is large.

Even in that small slice, the prototype found reviewable findings, built an executive report, and produced expert drill-down report variants. That suggests the method may have room to expand, but each expansion would need to be tested:

- more carriers in Kentucky,
- more states,
- more insurance lines,
- more smell categories,
- deeper per-carrier reports,
- periodic re-scans after new filings or regulatory changes.

The near-term revenue model would probably be modest and service-like: specialized annual or periodic review reports rather than a large software platform. A possible target price might be **USD 60,000 to USD 90,000 per year** for a focused report and review workflow, but that is a hypothesis, not a proven price. The real price would depend on buyer feedback, scope, report quality, expert involvement, and whether the buyer sees enough risk reduction or time savings.

That price range is not pulled from nowhere, but it is also not validated yet. It is a plausible range to test because the work would not be a simple automated scan. A credible report would involve source collection, parsing, detector runs, evidence review, finding triage, copyright-safe summary writing, expert-facing report preparation, and a discussion with the buyer about what the findings mean. In professional services terms, that is closer to a specialized compliance or risk review than a downloadable software subscription.

The range also has to be judged against the buyer's alternative costs. An insurer already pays for compliance staff, product/forms review, outside counsel, filing support, claims dispute handling, and regulator response. If a report helps focus even a small part of that work, or helps identify one issue before it becomes a larger remediation or dispute, then a five-figure annual review is not automatically unreasonable. Whether it is actually acceptable depends on what real buyers say after seeing the prototype.

The reason that price range matters is that the project would not need hundreds of customers to become worthwhile. If the report proved valuable enough for even a few serious buyers, it could support the work while the product is still being refined.

For example:

> Three annual report clients at USD 60,000 would be USD 180,000 per year.  
> Five annual report clients at USD 90,000 would be USD 450,000 per year.

Those numbers are not forecasts. They are simple scenario math showing why the idea is worth testing. To be real, those scenarios would require several things that have not been proven yet:

- experts must agree the findings are useful,
- buyers must believe the report reduces real risk or saves real time,
- the report must be legally and professionally safe to share,
- source access must be good enough for repeatable work,
- and at least a small number of customers must be willing to pay.

That is what makes the project interesting financially: the first viable version could be narrow, specialized, and relatively low-infrastructure. But the next step is still validation, not assuming the market is already there.

---

## Current Risks

There are still real risks.

The biggest risk is commercial validation: professionals may find the report interesting but not valuable enough to pay for. That has to be tested.

Other risks include:

- source documents may be hard to obtain in some states,
- some findings may be too uncertain without expert review,
- the scope could become too broad,
- insurers may already have internal processes that partially address this,
- the product has to be careful about not giving legal advice.

These risks are being managed by keeping the work narrow, local, evidence-based, and prototype-oriented.

---

## What Comes Next

The next useful step is not to build a giant platform.

The next useful step is to finish a clear interactive prototype of the expert report and show it to a small number of insurance, compliance, legal, or product professionals.

The key question is:

> Would this help you find, explain, prioritize, or fix real policy and compliance issues earlier?

If experts say yes, the project has a credible path forward. If they say no, the project can be narrowed or redirected before too much time or money is spent.

---

## Bottom Line

This is a serious, focused AI/legal-tech exploration.

It is not a vague AI idea. It is not an attempt to replace lawyers. It is not yet a finished business.

It is a proof of concept for using AI-assisted and rules-based document analysis to find potential insurance policy and compliance problems earlier than they are usually found.

The technical proof of concept works at prototype scale. The next proof is whether real professionals see enough value in the report to pay for it.

---

## Public Context Sources

- Government of Canada: Budget 2024 AI package and Canada's AI advantage  
  https://www.pm.gc.ca/en/news/news-releases/2024/04/07/securing-canadas-ai

- Government of Canada: Canadian Sovereign AI Compute Strategy  
  https://www.canada.ca/en/innovation-science-economic-development/news/2024/12/canada-to-drive-billions-in-investments-to-build-domestic-ai-compute-capacity-at-home.html

- Government of Canada: AI Compute Access Fund  
  https://www.canada.ca/en/innovation-science-economic-development/news/2025/03/government-of-canada-introduces-ai-compute-access-fund-to-support-canadian-innovators.html

- Government of Canada: Cohere AI compute investment  
  https://www.canada.ca/en/department-finance/news/2024/12/deputy-prime-minister-announces-240-million-for-cohere-to-scale-up-ai-compute-capacity.html

- Law Smells research overview  
  https://research.aalto.fi/en/publications/law-smells-defining-and-detecting-problematic-patterns-in-legal-d

- OpenFisca: Rules as Code platform  
  https://openfisca.org/en/
