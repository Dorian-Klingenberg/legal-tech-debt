# Stage 003 Results

This directory is intentionally separate from the parent engine's outputs. Store every model or agent run in a timestamped or otherwise stable `results/<run-id>/` folder.

Recommended contents for a run:

- `run.json` — model name/version, prompt template version, timestamp, and fixture set
- `predictions.jsonl` — one contract-compliant result per smell fixture
- `metrics.json` — aggregate metrics, abstention counts, and per-complexity metrics
- `review-notes.md` — human adjudication for disputed or high-complexity cases

Do not overwrite prior runs. A run directory is an immutable record once reviewed.
