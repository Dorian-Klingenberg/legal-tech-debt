# Stage Workflow

This sandbox is organized as a sequence of stages. A stage is a preserved experiment state: code, sample data, notes, and generated evidence that can be rerun later.

## Why Stages

The project is pre-phase A. The goal is to explore what is possible, not prematurely converge on architecture. Stages let us try ideas without losing the last working state.

## Stage Rules

- Every stage must be independently runnable.
- Every stage should have a `STAGE.md` with purpose, command, result, and status.
- Every stage should have a `LESSON.md` that explains the stage as if teaching a careful reader from first principles.
- Do not mutate a frozen stage for a new idea.
- Clone the previous stage, rename it, then experiment in the new stage.
- Keep generated outputs if they are evidence for the stage.
- Avoid introducing dependencies unless the stage is specifically about evaluating them.

## Naming

Use three digits plus a short slug:

```text
001-baseline
002-dashboard-mockup
003-kentucky-insurance-sample
004-typed-edge-study
005-typed-matrix-prototype
006-matrix-performance
```

## Done Criteria

A stage is done when:

- the main command runs
- outputs are generated or the failure is documented
- observations are captured
- the lesson explains what the stage taught, what it did not prove, and what question comes next
- the next question is clear

## Lesson Style

The lesson should be patient, concrete, example-first, and technically precise. It should explain the idea in a way that helps a reader learn the topic while also preserving useful engineering evidence.

Useful lesson sections:

- the problem this stage investigates
- the smallest example that makes the idea visible
- the representation chosen
- what worked
- what failed or surprised us
- what this stage proves
- what this stage does not prove
- the next question

## Clone Command

From the sandbox root:

```powershell
python .\tools\new_stage.py --from 004-typed-edge-study --to 005-typed-matrix-prototype --title "Typed Matrix Prototype" --include-output
```

By default, the helper copies source, data, and notes but starts the new stage with an empty `output/` folder. Use `--include-output` if the new stage should inherit generated evidence too.
