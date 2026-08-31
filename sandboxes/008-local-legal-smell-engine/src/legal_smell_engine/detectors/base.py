from __future__ import annotations

from collections.abc import Iterator
from typing import Protocol

from ..contracts import DetectionRun, Finding


class Detector(Protocol):
    SMELL_ID: int
    SMELL_NAME: str

    def detect(self, run: DetectionRun) -> Iterator[Finding]: ...

