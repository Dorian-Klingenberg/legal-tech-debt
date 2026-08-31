"""Local, deterministic legal-smell detection engine."""

from .contracts import Edge, Finding, Node, EvidenceCorpus, SCHEMA_VERSION
from .engine import DetectorEngine

__all__ = [
    "DetectorEngine",
    "Edge",
    "EvidenceCorpus",
    "Finding",
    "Node",
    "SCHEMA_VERSION",
]

