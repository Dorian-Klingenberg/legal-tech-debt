# Stage 003 — Twenty-Smell Model Benchmark

This is a deliberately separate benchmark lane inside Sandbox 008. It is for exercising new models against twenty legal code-smell detection tasks without mixing their prompts, fixtures, or results into the Stage 001 engine calibration or Stage 002 adapter work.

Start here:

- [Stage plan](STAGE.md)
- [Smell selection and complexity distribution](SMELL_SELECTION.md)
- [Benchmark task contract](prompts/benchmark-task.md)
- [Results area](results/README.md)

The benchmark is a model-evaluation and detector-design surface, not a claim that all twenty smells are production-ready detectors. Each smell must carry its own evidence expectations, positive examples, negative examples, and explicit insufficiency conditions.

## Current status

- Scope selected: 20 new smells, split 8 low / 8 medium / 4 high complexity.
- Work organization: five parallel groups of four smells, with disjoint write areas.
- Results boundary: `results/` belongs only to this benchmark.
- Existing engine outputs remain under the parent Sandbox 008 directories and are not overwritten.
