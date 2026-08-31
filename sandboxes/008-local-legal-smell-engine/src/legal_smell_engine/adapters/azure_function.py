"""Optional Azure Functions HTTP adapter around the local engine."""
from __future__ import annotations

import json
from typing import Any

from .mcp_server import review_payload


def review_json_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a JSON-serializable response without requiring Azure locally."""
    findings = review_payload(
        nodes=list(payload.get("nodes", [])),
        edges=list(payload.get("edges", [])),
        run_id=str(payload.get("run_id", "azure-function-run")),
        smell_ids=payload.get("smell_ids"),
    )
    return {"schema_version": "1.0.0", "run_id": str(payload.get("run_id", "azure-function-run")), "findings": findings}


def main(req: Any) -> Any:
    try:
        import azure.functions as func
    except ImportError as exc:  # pragma: no cover - exercised only without optional extra
        raise RuntimeError("Install the Azure extra with: pip install '.[azure]'") from exc

    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse("Request body must be valid JSON.", status_code=400)
    if not isinstance(payload, dict):
        return func.HttpResponse("Request body must be a JSON object.", status_code=400)
    return func.HttpResponse(
        json.dumps(review_json_payload(payload), ensure_ascii=False),
        status_code=200,
        mimetype="application/json",
    )

