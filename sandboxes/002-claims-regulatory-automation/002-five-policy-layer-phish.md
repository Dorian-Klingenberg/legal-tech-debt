Below are blueprints for your **five homeowners-policy-layer phish**, each with:

- A human-readable detection spec (what to look for, from where).
- A few **Gherkin scenarios** showing how you’d express this as tests against a KY corpus.

All of these assume you have:  
- KY statutes/regs (KRS 304 + 806 KAR).  
- KY homeowners SERFF filings (forms + rate/rule manuals) via SFA. [insurance.ky](https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf)

Current scope note: focus on homeowners insurance. Do not use auto, motor vehicle, no-fault, or PIP examples unless a homeowners filing directly cross-references them and the reference is only being recorded as context.

***

## Phish 1 – Overbroad / Non‑deterministic Exclusions

### Human-readable spec

**Goal:** Flag exclusions whose scope is so broad or fuzzy that courts are likely to re-interpret them (e.g., “governmental action”, “virus”, “data”, “arising out of” everything).

**Inputs:**

- All KY P&C policy forms and endorsements from SERFF, 2018+. [insurance.ky](https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=665)

**Signals:**

1. **Trigger phrases:**
   - `“arising out of”`, `“resulting from”`, `“directly or indirectly”`, `“in any sequence”`.
   - Exclusions for:
     - “virus”, “bacteria”, “communicable disease”.
     - “governmental action”, “order of civil authority”, “ordinance or law”.
     - “data”, “data-related loss”, “electronic data”.  

2. **Overbroad subject:**
   - The thing being excluded is defined as:
     - Any act of “government” or “public authority” without carve-outs (e.g., for emergency services, code upgrades).
     - Any “virus or bacteria” regardless of context (surface vs. systemic).  

3. **Conflict with coverage grant:**
   - The exclusion applies to the same peril the insuring agreement was clearly written to cover (e.g., BI from closure by civil authority) without clear prioritization or narrowing.

**Detectability:**

- Pure text analysis: regex + a simple clause graph are enough to flag any exclusion with the trigger phrases plus a very broad subject, especially when it intersects the main property/BI grant.

### Gherkin examples

```gherkin
Feature: Detect overbroad exclusions in Kentucky property forms

  Background:
    Given I have loaded all Kentucky P&C policy forms and endorsements filed via SERFF since 2018

  Scenario: Exclusion uses "arising out of" with a broad governmental subject
    When I scan exclusions for phrases "arising out of" or "resulting from"
    And the subject of the exclusion includes "governmental action" or "order of any governmental authority"
    And the exclusion is not limited to a specific listed peril or narrow scenario
    Then I flag this exclusion as a potential Overbroad Exclusion smell

  Scenario: Data/virus exclusion drafted to sweep in any related loss
    When I scan exclusions for "virus", "bacteria", or "electronic data"
    And the exclusion also contains "directly or indirectly" or "in any sequence"
    And there is no exception clause preserving core property coverage
    Then I flag this exclusion as a potential Non-deterministic Exclusion smell
```

***

## Phish 2 – Magic Number / Magic Valuation Terms

### Human-readable spec

**Goal:** Find undefined temporal and valuation terms where operations clearly expect a concrete number or formula.

**Inputs:**

- KY homeowners policy forms and endorsements.
- KY statutes/regs that impose concrete timelines (prompt pay, notice). [law.justia](https://law.justia.com/codes/kentucky/2018/chapter-304/subtitle-14/)

**Signals:**

1. **Temporal “magic numbers”:**
   - Policy text uses:
     - “within a reasonable time”
     - “prompt notice”
     - “as soon as practicable”
     - “promptly investigate”
   - **Without**:
     - A cross-reference to a specific statutory time (e.g., 30/45/60 days), or
     - Any defined number of days in definitions/conditions.

2. **Valuation “magic terms”:**
   - Uses terms like:
     - “customary and reasonable charges”, “usual and customary”.
     - “actual cash value”, “fair market value”.
   - **Without**:
     - A definition section that specifies a formula (e.g., “replacement cost less depreciation for age and condition using schedule X”), or
     - A reference to a named, versioned manual.

3. **Mismatch with KY law:**
   - KRS/KAR imposes a concrete timeline or requirement, but the policy language remains vague (“as required by law”) rather than specifying it. [law.justia](https://law.justia.com/codes/kentucky/chapter-304/subtitle-304-14/)

### Gherkin examples

```gherkin
Feature: Detect magic temporal and valuation terms in Kentucky policies

  Background:
    Given I have loaded all Kentucky P&C policy forms filed via SERFF since 2018
    And I have loaded Kentucky prompt-pay and notice requirements from KRS and KAR

  Scenario: Undefined temporal magic term
    When I scan policy conditions for phrases "prompt notice", "as soon as practicable", or "within a reasonable time"
    And I do not find a defined number of days in the policy definitions, conditions, or a statutory cross-reference
    Then I flag this clause as a Magic Number (Time) smell

  Scenario: Undefined valuation term for ACV
    When I scan policy definitions for "actual cash value" or "fair market value"
    And the definition does not specify a calculation formula or reference a named, versioned manual
    Then I flag this term as a Magic Valuation Term smell
```

***

## Phish 3 – Coverage Inversion / Contradictory Conditions

### Human-readable spec

**Goal:** Identify policies where insuring agreements appear broad but are quietly nullified by nested exclusions and exceptions.

**Inputs:**

- Full Kentucky product packages from SERFF (base form + mandatory endorsements + common optional endorsements). [insurance.ky](https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf)

**Signals:**

1. **Broad grant + heavy exclusion stack:**
   - Insuring agreement: “We insure against risk of direct physical loss to property…”
   - Followed by multiple endorsements that:
     - Exclude large families of perils (water, mold, virus, governmental action, ordinance or law), and
     - Apply “notwithstanding any other provision” language.

2. **Nested exception hell:**
   - Exclusion with “except as provided in endorsement X,” and endorsement X has “this insurance does not apply except as otherwise provided in endorsement Y,” etc.

3. **Direct contradictions:**
   - Two clauses both triggered by the same peril (e.g., wind-driven rain), one granting coverage, another applying a sublimit or exclusion, with no priority rule.

**Detectability:**

- Build a simple graph:
  - Nodes: grants, exclusions, exceptions, endorsements.
  - Edges: “applies to”, “except as provided in”.
- Coverage inversion is detectable when a major grant node has **no remaining uncovered path** once all exclusions/endorsements are applied.

### Gherkin examples

```gherkin
Feature: Detect coverage inversion in Kentucky property policies

  Background:
    Given I have assembled complete policy packages for each Kentucky homeowners product from SERFF

  Scenario: Broad grant fully hollowed out by exclusions
    When I identify an insuring agreement that covers "risk of direct physical loss"
    And I identify exclusions and endorsements that remove coverage for all common perils for that coverage part
    And no remaining peril-specific grant survives after applying exclusions and exceptions
    Then I flag this coverage as a Coverage Inversion smell

  Scenario: Conflicting clauses for the same peril
    When I detect two clauses that both apply to "wind-driven rain" losses
    And one clause grants full coverage while another applies a sublimit or total exclusion
    And there is no explicit precedence rule between them
    Then I flag this as a Contradictory Conditions smell
```

***

## Phish 4 – Calculation Rule Drift / Unversioned Rate Reference

### Human-readable spec

**Goal:** Find rating rules that reference external manuals or “current” values without a locked version or explicit calculation steps.

**Inputs:**

- KY SERFF **rate and rule** filings (not just forms). [insurance.ky](https://insurance.ky.gov/ppc/newstatic_Info.aspx?static_ID=665)
- KY regs on rating organizations and rate filings (806 KAR 13).*. [kyrules.elaws](https://kyrules.elaws.us/rule/806kar13)

**Signals:**

1. **Unversioned manual references:**
   - Phrases like:
     - “per current ISO loss costs”
     - “according to current bureau manual”
     - “per the company’s current rating guidelines”
   - **Without**:
     - An edition date (e.g., “ISO HO-3 04/91”) or
     - A specific document ID/version.

2. **Opaque calculation references:**
   - Rules that say:
     - “ACV shall be determined in accordance with company guidelines”
     - “Premium shall be determined based on underwriting judgment and company rating plans”
   - **Without**:
     - Any spelled-out formula or algorithm in the filed rules.

3. **Mismatch with filing expectations:**
   - 806 KAR 13 expects filed rates and rules to be auditable and to correspond to the actual rating organization or internal manual being used. [law.cornell](https://www.law.cornell.edu/regulations/kentucky/title-806/chapter-13)

### Gherkin examples

```gherkin
Feature: Detect unversioned and opaque rating references in Kentucky filings

  Background:
    Given I have loaded all Kentucky P&C rate and rule filings from SERFF since 2018
    And I have loaded Kentucky regulations on rating organizations and rate filings

  Scenario: Unversioned reference to bureau loss costs
    When I scan rating rules for phrases like "current ISO loss costs" or "current bureau manual"
    And no edition date, document ID, or version number appears near the reference
    Then I flag this rule as an Unversioned Rate Reference smell

  Scenario: Opaque ACV calculation reference
    When a rating or rule filing defines "actual cash value" or a key premium factor
    And the definition only refers to "company guidelines" or "current rating plans" without further detail
    Then I flag this as a Calculation Rule Drift risk
```

***

## Phish 5 – Regulatory Mapping Smells (“per state law”, null references)

### Human-readable spec

**Goal:** Find policy and filing language that punts to “state law” without citations, jurisdiction lists, or versioning, especially in multi-state forms.

**Inputs:**

- KY forms and endorsements from SERFF that are filed as multi-state or use generic “applicable law” language. [insurance.ky](https://insurance.ky.gov/ppc/Documents/publicaccessinsurancefilingsforproperty.pdf)
- KY-specific requirements in KRS 304 and 806 KAR (e.g., notice days, cancellation reasons). [law.justia](https://law.justia.com/codes/kentucky/2018/chapter-304/subtitle-20/)

**Signals:**

1. **Null references to law:**
   - Phrases such as:
     - “as required by state law”
     - “where permitted by law”
     - “in accordance with applicable law”
   - **Without**:
     - A specific citation (e.g., “KRS 304.20‑040”), or
     - A schedule listing state-specific parameters.

2. **Multi-state use with single generic clause:**
   - Same form is filed in KY and other states, but cancellation/notice provisions are generic and do not parameterize required days or reasons.

3. **References to bulletins/circulars without versioning:**
   - “per DOI Bulletin 2019‑04” or similar, without any indication of how supersession is handled over time.

### Gherkin examples

```gherkin
Feature: Detect regulatory mapping smells in Kentucky policy forms

  Background:
    Given I have loaded all Kentucky P&C policy forms and endorsements from SERFF since 2018
    And I have loaded Kentucky statutory and regulatory requirements for notice, cancellation, and mandatory coverages

  Scenario: Generic "as required by state law" with no citation
    When I scan policy conditions for phrases "as required by state law" or "in accordance with applicable law"
    And I find no specific statute citation or state-specific schedule in the form
    Then I flag this clause as an Unversioned Statutory Reference smell

  Scenario: Multi-state cancellation language without Kentucky-specific parameters
    When a form is filed for use in multiple states including Kentucky
    And the cancellation section does not specify the number of days' notice or permissible reasons per state
    And Kentucky law imposes concrete notice day requirements for that line
    Then I flag this as a Jurisdictional Inheritance / Regulatory Mapping smell
```

***

If you want to go one step further, I can take one KY homeowners program (from a named SERFF filing) and walk through a concrete, end-to-end example: show exactly which clauses are flagged by these Gherkin scenarios and how they correspond to your smells.
