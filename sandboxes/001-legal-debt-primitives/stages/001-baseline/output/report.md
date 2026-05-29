# Legal Debt Probe Report

Sections found: 10
References found: 7
Findings found: 8

## Findings

### DanglingReference (high)

- Source: `state_minimum_coverage_statute.md:16`
- Message: Section 300 references missing Section 900.
- Evidence: Notices required by this section must comply with Section 900.

### CircularReference (medium)

- Source: `state_minimum_coverage_statute.md:25`
- Message: Section 400 and Section 410 reference each other.
- Evidence: Claim notice timing is governed by Section 410. / Exceptions to claim notice timing are governed by Section 400.

### OrphanDefinition (low)

- Source: `state_minimum_coverage_statute.md:9`
- Message: Defined term "Covered vehicle" appears to be unused outside its definition.
- Evidence: - "Covered vehicle" means a vehicle insured under a policy subject to this chapter.

### OrphanDefinition (low)

- Source: `state_minimum_coverage_statute.md:10`
- Message: Defined term "Legacy endorsement" appears to be unused outside its definition.
- Evidence: - "Legacy endorsement" means an endorsement form retired before January 1, 2020.

### OrphanDefinition (low)

- Source: `state_minimum_coverage_statute.md:11`
- Message: Defined term "Policy year" appears to be unused outside its definition.
- Evidence: - "Policy year" means the annual period beginning on the policy effective date.

### UnversionedExternalAuthority (medium)

- Source: `internal_policy_manual.md:18`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: The claims team should consult NAIC guidance and ISO circulars when updating templates.

### UnversionedExternalAuthority (medium)

- Source: `state_minimum_coverage_statute.md:20`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: Coverage amounts shall follow NAIC Model Law guidance unless a more specific state rule applies.

### UnversionedExternalAuthority (medium)

- Source: `state_minimum_coverage_statute.md:21`
- Message: ISO is referenced without an obvious version, date, or effective source anchor.
- Evidence: The disclosure template must follow ISO form language.

## Section Graph Edges

- Section 10 -> Section 300 (`internal_policy_manual.md:5`)
- Section 10 -> Section 310 (`internal_policy_manual.md:5`)
- Section 20 -> Section 30 (`internal_policy_manual.md:10`)
- Section 300 -> Section 310 (`state_minimum_coverage_statute.md:15`)
- Section 300 -> Section 900 (`state_minimum_coverage_statute.md:16`)
- Section 400 -> Section 410 (`state_minimum_coverage_statute.md:25`)
- Section 410 -> Section 400 (`state_minimum_coverage_statute.md:29`)

## Matrix Outputs

Matrix direction: `A[i,j] = 1` means node `i` depends on node `j`.

- `section_index.csv`: matrix node index and labels
- `adjacency_matrix.csv`: direct dependency matrix `A`
- `two_hop_matrix.csv`: boolean matrix product `A^2`
- `transitive_closure.csv`: all reachable dependencies
- `dependency_roots.json`: terminal dependency roots and cycle nodes

## Dependency Roots

- `section:10` -> `section:310`, `missing:900`
- `section:20` -> `section:30`
- `section:300` -> `section:310`, `missing:900`

## Cycle Nodes

- `section:400`
- `section:410`
