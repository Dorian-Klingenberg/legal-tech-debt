# Stage 001: Baseline

Created: 2026-05-13

## Purpose

This stage is the first stable, working baseline for the legal debt primitives sandbox.

It includes:

- synthetic Markdown corpus
- deterministic section and reference extraction
- direct graph-edge reporting
- dependency matrix exports
- two-hop matrix product
- transitive closure
- dependency-root derivation
- cycle-node detection

## Baseline Command

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

## Baseline Result

- 10 sections
- 7 references
- 8 findings
- matrix outputs written to `output/`

## Stage Status

Frozen baseline. Future experiments should clone this stage into a new numbered stage rather than modifying this one directly.

## Lesson

See [LESSON.md](LESSON.md) for the book-style explanation of what this stage teaches.
