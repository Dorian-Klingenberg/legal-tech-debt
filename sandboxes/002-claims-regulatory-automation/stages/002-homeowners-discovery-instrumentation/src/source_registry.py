"""Read the source manifest subset and build Source records."""
from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from models import SCHEMA_VERSION, Source


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _detect_file_type(path: Path) -> str:
    try:
        with open(path, "rb") as f:
            magic = f.read(5)
        if magic.startswith(b"%PDF-"):
            return "pdf"
        decoded = magic.decode("utf-8", errors="replace").lower()
        if decoded.startswith("<!doc") or decoded.startswith("<html") or decoded.startswith("<?xml"):
            return "html"
        return "unknown"
    except OSError:
        return "unknown"


def load_sources(manifest_path: Path, run_id: str) -> list[Source]:
    now = datetime.now(timezone.utc).isoformat()
    sources: list[Source] = []

    with open(manifest_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            source_id = row["source_id"].strip()
            smell_ids = [int(s.strip()) for s in row["smell_ids"].strip('"').split(",") if s.strip().isdigit()]
            downloaded_path = Path(row["downloaded_path"].strip())

            detected = _detect_file_type(downloaded_path)
            ext = downloaded_path.suffix.lower().lstrip(".")
            ext_type = "pdf" if ext == "pdf" else "html" if ext in ("html", "htm") else "unknown"
            extension_matches = detected == ext_type or (detected == "unknown" and ext_type == "unknown")

            sources.append(Source(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                source_id=source_id,
                title=row["title"].strip(),
                source_type=row["source_type"].strip(),
                smell_ids=smell_ids,
                url=row["url"].strip(),
                downloaded_path=str(downloaded_path),
                file_bytes=int(row["file_bytes"].strip()),
                downloaded_at=row["downloaded_at"].strip(),
                source_hash=_sha256(downloaded_path),
                detected_file_type=detected,
                extension_matches_type=extension_matches,
            ))

    return sources
