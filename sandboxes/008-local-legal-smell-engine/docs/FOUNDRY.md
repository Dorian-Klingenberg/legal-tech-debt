# Microsoft Foundry Integration Boundary

The local engine is the source of truth for detector behavior. Microsoft
Foundry should consume it through an adapter rather than reimplementing the
heuristics in a prompt.

## Recommended first path

1. Install the optional MCP extra: `pip install '.[mcp]'`.
2. Run `python -m legal_smell_engine.adapters.mcp_server` locally or host the
   same MCP server behind an approved HTTPS endpoint.
3. Register the MCP server as a Foundry tool or tool connection.
4. Pass source-traceable `nodes` and optional typed `edges` to the
   `review_legal_smells` tool.
5. Keep the Foundry agent responsible for orchestration and explanation; keep
   detector execution and evidence contracts in the Python engine.

## Hosted alternative

The optional Azure Functions adapter exposes the same operation as an HTTP
endpoint. A Foundry agent can call that endpoint through an appropriate custom
tool or API connection. Authentication, network exposure, rate limits, and
secret management are deployment decisions and are not included in this
prototype.

The Azure Functions Python v2 scaffold is the sandbox root's
`function_app.py`. From that directory, install `requirements.txt` and run it
with Azure Functions Core Tools. The route is `POST /api/review` and uses the
same JSON payload shown below.

## Payload shape

```json
{
  "run_id": "foundry-demo-001",
  "smell_ids": ["SMELL2", "SMELL5"],
  "nodes": [
    {
      "node_id": "node-1",
      "source_id": "synthetic-policy",
      "source_type": "serff_form_filing",
      "section_path": "Loss Settlement",
      "text": "We pay actual cash value within a reasonable time."
    }
  ],
  "edges": []
}
```

The output remains a list of review leads with evidence and provenance. The
agent must not present them as legal advice or confirmed noncompliance.
