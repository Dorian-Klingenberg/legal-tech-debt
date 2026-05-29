# Dependency Matrix Notes

## Direction

The sandbox uses this convention:

```text
A[i, j] = 1 means node i depends on node j
```

Rows are dependents. Columns are dependencies.

Example:

```text
Section 300 -> Section 310
```

appears as:

```text
A[section:300, section:310] = 1
```

## Output Files

- `section_index.csv`: stable node ordering for matrix rows and columns.
- `adjacency_matrix.csv`: direct dependency matrix `A`.
- `two_hop_matrix.csv`: boolean matrix product `A^2`.
- `transitive_closure.csv`: all reachable dependency paths.
- `dependency_roots.json`: terminal reachable dependencies and cycle nodes.

## Why Include Missing Nodes?

Dangling references are represented as `missing:<section-id>` nodes. This keeps unresolved references in the matrix instead of dropping them.

For example, a reference to missing Section 900 becomes:

```text
section:300 -> missing:900
```

That lets the roots calculation reveal `missing:900` as a terminal dependency.

## Root Definition

For a given node, dependency roots are reachable dependency nodes with no further reachable dependencies in the transitive closure matrix.

This means:

- `section:300` can root at `section:310` and `missing:900`.
- cycle members such as `section:400` and `section:410` do not have terminal roots until the cycle is broken.

## Performance Hypothesis

Graph traversal is likely better for one-off local questions. Matrix closure is likely better for repeated whole-corpus reachability, impact analysis, cycle detection, blast-radius scoring, and version-to-version comparison.

For larger corpora, the next matrix step is sparse matrices or bitsets rather than dense CSV.
