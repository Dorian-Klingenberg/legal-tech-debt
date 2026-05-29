# Legal Debt Probe Report

Sections found: 10
References found: 7
Findings found: 8

## Findings

### DanglingReference (high)

- Source: `homeowners_property_reference.md:16`
- Message: Section 300 references missing Section 900.
- Evidence: Notices required by this section must comply with Section 900.

### CircularReference (medium)

- Source: `homeowners_property_reference.md:25`
- Message: Section 400 and Section 410 reference each other.
- Evidence: Claim notice timing is governed by Section 410. / Exceptions to claim notice timing are governed by Section 400.

### OrphanDefinition (low)

- Source: `homeowners_property_reference.md:9`
- Message: Defined term "Covered dwelling" appears to be unused outside its definition.
- Evidence: - "Covered dwelling" means a residence premises insured under a homeowners policy subject to this reference.

### OrphanDefinition (low)

- Source: `homeowners_property_reference.md:10`
- Message: Defined term "Legacy endorsement" appears to be unused outside its definition.
- Evidence: - "Legacy endorsement" means a homeowners endorsement form retired before January 1, 2020.

### OrphanDefinition (low)

- Source: `homeowners_property_reference.md:11`
- Message: Defined term "Policy year" appears to be unused outside its definition.
- Evidence: - "Policy year" means the annual period beginning on the policy effective date.

### UnversionedExternalAuthority (medium)

- Source: `homeowners_claims_manual.md:18`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: The homeowners product team should consult NAIC guidance and ISO homeowners circulars when updating forms and templates.

### UnversionedExternalAuthority (medium)

- Source: `homeowners_property_reference.md:20`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: Coverage amounts shall follow NAIC Model Law guidance unless a more specific Kentucky property rule applies.

### UnversionedExternalAuthority (medium)

- Source: `homeowners_property_reference.md:21`
- Message: ISO is referenced without an obvious version, date, or effective source anchor.
- Evidence: The disclosure template must follow ISO homeowners form language.

## Section Graph Edges

- Section 10 -> Section 300 (`homeowners_claims_manual.md:5`)
- Section 10 -> Section 310 (`homeowners_claims_manual.md:5`)
- Section 20 -> Section 30 (`homeowners_claims_manual.md:10`)
- Section 300 -> Section 310 (`homeowners_property_reference.md:15`)
- Section 300 -> Section 900 (`homeowners_property_reference.md:16`)
- Section 400 -> Section 410 (`homeowners_property_reference.md:25`)
- Section 410 -> Section 400 (`homeowners_property_reference.md:29`)

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
