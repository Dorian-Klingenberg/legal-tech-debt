"""Write Stage 002 records to JSONL and JSON output files."""
from __future__ import annotations

import dataclasses
import json
from pathlib import Path
from typing import Any


def _to_dict(obj: Any) -> dict:
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    return obj


def write_jsonl(records: list[Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(_to_dict(rec), ensure_ascii=False) + "\n")


def write_json(obj: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(_to_dict(obj) if dataclasses.is_dataclass(obj) else obj, f, indent=2, ensure_ascii=False)
        f.write("\n")
