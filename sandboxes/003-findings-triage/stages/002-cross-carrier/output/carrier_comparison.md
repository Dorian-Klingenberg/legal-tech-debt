# Stage 002: Cross-Carrier Pattern Analysis

Run: 2026-06-04  
Confirmed findings: 25 of 35 total  

---

## Smell 2: Magic Number / Magic Valuation Terms

**Confirmed findings:** 16  
**Industry-wide patterns:** 1  
**Carrier-specific patterns:** 1  

| Heuristic | Pattern | KNIC | KFBM | Terms Flagged |
|---|---|---|---|---|
| SMELL2-H001 | carrier-specific (KFBM) | 0 | 6 | Reasonable |
| SMELL2-H003 | **industry-wide** | 5 | 5 | Actual Cash Value, REPLACEMENT COST, Replacement Cost |

**Industry-wide patterns (strongest signal):**

- **SMELL2-H003** — terms: Actual Cash Value, REPLACEMENT COST, Replacement Cost: 5 KNIC finding(s), 5 KFBM finding(s)

**Carrier-specific patterns:**

- **SMELL2-H001** (KFBM only) — terms: Reasonable: 6 finding(s)

---

## Smell 4: Calculation Rule Drift / Unversioned Rate Reference

**Confirmed findings:** 1  
**Industry-wide patterns:** 0  
**Carrier-specific patterns:** 1  

| Heuristic | Pattern | KNIC | KFBM | Terms Flagged |
|---|---|---|---|---|
| SMELL4-H001 | carrier-specific (KNIC) | 1 | 0 | the Manual |

**Carrier-specific patterns:**

- **SMELL4-H001** (KNIC only) — terms: the Manual: 1 finding(s)

---

## Smell 5: Regulatory Mapping Smells

**Confirmed findings:** 8  
**Industry-wide patterns:** 2  
**Carrier-specific patterns:** 1  

| Heuristic | Pattern | KNIC | KFBM | Terms Flagged |
|---|---|---|---|---|
| SMELL5-H004 | **industry-wide** | 1 | 4 | — |
| SMELL5-H005 | **industry-wide** | 1 | 1 | — |
| SMELL5-H006 | carrier-specific (KFBM) | 0 | 1 | — |

**Industry-wide patterns (strongest signal):**

- **SMELL5-H004**: 1 KNIC finding(s), 4 KFBM finding(s)
- **SMELL5-H005**: 1 KNIC finding(s), 1 KFBM finding(s)

**Carrier-specific patterns:**

- **SMELL5-H006** (KFBM only): 1 finding(s)

---
