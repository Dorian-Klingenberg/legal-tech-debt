# Edge Labeling Guide

## Labeling Unit

Label one extracted reference at a time.

The unit is:

- source section
- target section
- source document
- line
- snippet

Do not label based only on the section numbers. Read the snippet.

## Required Fields

`proposed_type`

The best edge type from [EDGE_TYPE_FRAMEWORK.md](EDGE_TYPE_FRAMEWORK.md).

`confidence`

Use:

- `high` when the wording clearly indicates the type
- `medium` when the type is plausible but another type is possible
- `low` when the edge needs SME review

`rationale`

One short explanation of why the label fits.

`typed_reachability`

Use:

- `live` for edges that may participate in valid typed reachability
- `visible_only` for edges that should be shown but should not produce closure
- `exclude` for stale or invalid edges
- `review` when the rule is undecided

## Practical Heuristics

Words like `implements`, `administered under`, and `operationalizes` often indicate `implements_authority`.

Words like `verify`, `confirm`, `compare`, `checked`, and `screen` often indicate `validates_against`.

Words like `route`, `move`, `return`, `reopened`, and `escalated` often indicate workflow relationships.

Words like `retain`, `record`, `packet`, `archive`, and `evidence` often indicate `requires_evidence` or `records_retention`.

Words like `stale`, `obsolete`, `retired`, `legacy`, and `missing` often indicate `stale_reference`.

## Ambiguity Rule

If one edge could reasonably have two types, do not invent a hybrid type immediately.

Choose the dominant type, mark confidence `medium` or `low`, and record the alternate in notes. If the same ambiguity repeats, promote it to a framework question.
