from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path


IGNORE_NAMES = {"__pycache__"}
IGNORE_SUFFIXES = {".pyc", ".pyo"}


def ignore_stage_items(include_output: bool):
    def ignore(_directory: str, names: list[str]) -> set[str]:
        ignored: set[str] = set()
        for name in names:
            if name in IGNORE_NAMES:
                ignored.add(name)
            elif Path(name).suffix in IGNORE_SUFFIXES:
                ignored.add(name)
            elif not include_output and name == "output":
                ignored.add(name)
        return ignored

    return ignore


def write_stage_metadata(target: Path, source_name: str, stage_name: str, title: str) -> None:
    stage_file = target / "STAGE.md"
    stage_file.write_text(
        "\n".join(
            [
                f"# Stage {stage_name}: {title}",
                "",
                f"Created: {date.today().isoformat()}",
                f"Cloned from: `{source_name}`",
                "",
                "## Purpose",
                "",
                "Describe the experiment this stage is meant to run.",
                "",
                "## Command",
                "",
                "```powershell",
                "python .\\src\\legal_debt_probe.py --corpus .\\data\\corpus --out .\\output",
                "```",
                "",
                "## Result",
                "",
                "Record the run result here after the stage has evidence.",
                "",
                "## Observations",
                "",
                "Record what changed, what worked, what failed, and what question this stage raises next.",
                "",
                "## Stage Status",
                "",
                "Active.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_lesson_template(target: Path, stage_name: str, title: str) -> None:
    lesson_file = target / "LESSON.md"
    lesson_file.write_text(
        "\n".join(
            [
                f"# Lesson: {title}",
                "",
                f"This lesson belongs to `{stage_name}`.",
                "",
                "Write this as a patient, concrete explanation for a reader who is learning the idea while following the experiment.",
                "",
                "## The Question",
                "",
                "What question is this stage trying to answer?",
                "",
                "## The Smallest Example",
                "",
                "What is the smallest example that makes the idea visible?",
                "",
                "## The Representation",
                "",
                "What data structures, files, or mathematical objects does this stage use?",
                "",
                "## What Worked",
                "",
                "What did the stage successfully demonstrate?",
                "",
                "## What Surprised Us",
                "",
                "What false positives, edge cases, bugs, or awkward concepts appeared?",
                "",
                "## What This Proves",
                "",
                "What can we now say with evidence?",
                "",
                "## What This Does Not Prove",
                "",
                "What remains unknown?",
                "",
                "## The Next Question",
                "",
                "What should the next stage investigate?",
                "",
            ]
        ),
        encoding="utf-8",
    )


def clone_stage(source: Path, target: Path, include_output: bool, title: str) -> None:
    if not source.exists():
        raise SystemExit(f"Source stage does not exist: {source}")
    if target.exists():
        raise SystemExit(f"Target stage already exists: {target}")

    shutil.copytree(source, target, ignore=ignore_stage_items(include_output))
    (target / "output").mkdir(exist_ok=True)
    write_stage_metadata(target, source.name, target.name, title)
    write_lesson_template(target, target.name, title)


def main() -> None:
    parser = argparse.ArgumentParser(description="Clone one sandbox stage into the next experiment stage.")
    parser.add_argument("--from", dest="from_stage", required=True, help="Source stage folder name, e.g. 001-baseline.")
    parser.add_argument("--to", dest="to_stage", required=True, help="Target stage folder name, e.g. 005-typed-matrix-prototype.")
    parser.add_argument("--title", required=True, help="Human-readable title for the target stage.")
    parser.add_argument("--include-output", action="store_true", help="Copy generated output from the source stage.")
    args = parser.parse_args()

    sandbox_root = Path(__file__).resolve().parents[1]
    stages_dir = sandbox_root / "stages"
    clone_stage(
        source=stages_dir / args.from_stage,
        target=stages_dir / args.to_stage,
        include_output=args.include_output,
        title=args.title,
    )
    print(f"Created {stages_dir / args.to_stage}")


if __name__ == "__main__":
    main()
