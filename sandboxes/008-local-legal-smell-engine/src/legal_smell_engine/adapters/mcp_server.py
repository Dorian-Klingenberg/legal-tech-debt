"""Optional MCP adapter around the local engine.

Install the optional dependency with ``pip install '.[mcp]'`` before running
this module as an MCP server. The pure ``review_payload`` helper is testable
without the MCP SDK.
"""
from __future__ import annotations

from typing import Any

from ..contracts import Edge, EvidenceCorpus, Node
from ..engine import DetectorEngine


def review_payload(
    nodes: list[dict[str, Any]],
    edges: list[dict[str, Any]] | None = None,
    run_id: str = "mcp-run",
    smell_ids: list[str] | None = None,
) -> list[dict[str, Any]]:
    corpus = EvidenceCorpus(
        run_id=run_id,
        nodes=[Node.from_dict(node) for node in nodes],
        edges=[Edge.from_dict(edge) for edge in (edges or [])],
    )
    return [finding.to_dict() for finding in DetectorEngine(corpus).run_detectors(smell_ids)]


def create_server() -> Any:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:  # pragma: no cover - exercised only without optional extra
        raise RuntimeError("Install the MCP extra with: pip install '.[mcp]'") from exc

    server = FastMCP("Local Legal Smell Engine")

    @server.tool()
    def review_legal_smells(
        nodes: list[dict[str, Any]],
        edges: list[dict[str, Any]] | None = None,
        run_id: str = "mcp-run",
        smell_ids: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """Run source-traceable legal smell detectors over supplied evidence nodes."""
        return review_payload(nodes, edges, run_id, smell_ids)

    return server


def main() -> None:
    create_server().run()


if __name__ == "__main__":
    main()

