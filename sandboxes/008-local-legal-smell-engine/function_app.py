"""Azure Functions Python v2 host entrypoint for the local smell engine."""
from __future__ import annotations

import json

import azure.functions as func

from legal_smell_engine.adapters.azure_function import review_json_payload

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="review", methods=["POST"])
def review(req: func.HttpRequest) -> func.HttpResponse:
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

