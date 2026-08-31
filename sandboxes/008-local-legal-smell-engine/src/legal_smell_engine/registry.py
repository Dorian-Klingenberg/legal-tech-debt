from __future__ import annotations

from collections.abc import Callable, Iterator

from .contracts import DetectionRun, Finding
from .detectors import smell2_valuation
from .detectors import smell1_exclusions, smell3_coverage_inversion, smell4_calculation_drift, smell5_regulatory_mapping
from .detectors.base import Detector

DetectorFactory = Callable[[], Detector]


def _smell1() -> Detector:
    return smell1_exclusions


def _smell2() -> Detector:
    return smell2_valuation


def _smell3() -> Detector:
    return smell3_coverage_inversion


def _smell4() -> Detector:
    return smell4_calculation_drift


def _smell5() -> Detector:
    return smell5_regulatory_mapping


_FACTORIES: dict[str, DetectorFactory] = {
    "SMELL1": _smell1,
    "SMELL2": _smell2,
    "SMELL3": _smell3,
    "SMELL4": _smell4,
    "SMELL5": _smell5,
}


def register_detector(smell_id: str, factory: DetectorFactory) -> None:
    _FACTORIES[smell_id.upper()] = factory


def registered_smells() -> tuple[str, ...]:
    return tuple(sorted(_FACTORIES))


def detect_for(smell_id: str, run: DetectionRun) -> Iterator[Finding]:
    factory = _FACTORIES.get(smell_id.upper())
    if factory is None:
        raise KeyError(f"Unknown smell '{smell_id}'. Registered smells: {', '.join(registered_smells())}")
    yield from factory().detect(run)
