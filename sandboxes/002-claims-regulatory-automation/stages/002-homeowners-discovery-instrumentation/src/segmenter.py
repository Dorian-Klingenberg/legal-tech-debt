"""Build legal Nodes from a flat list of Blocks using section hierarchy.

For KAR HTML blocks, the hierarchy is explicit in block.level.
For PDF blocks, we infer hierarchy from heading depth.

Node IDs are deterministic: sha256(source_id::section_path)[:20].
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

import ids as id_gen
from models import SCHEMA_VERSION, Block, Node

_DEFINITION_RE = re.compile(r'^\s*"([^"]+)"\s+(?:means|is defined)', re.IGNORECASE)


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _node_type_from_block(block: Block, depth: int) -> str:
    if depth == 0:
        return "document"
    text = block.text.strip()
    if _DEFINITION_RE.match(text):
        return "definition"
    if block.block_type == "table":
        return "table"
    if block.block_type == "list_item" or depth >= 3:
        return "list_item"
    if depth == 1:
        return "section"
    if depth == 2:
        return "subsection"
    return "clause"


def build_nodes(
    source_id: str,
    source_hash: str,
    source_title: str,
    blocks: list[Block],
    run_id: str,
) -> list[Node]:
    now = datetime.now(timezone.utc).isoformat()
    nodes: list[Node] = []

    # Document-level root node
    root_path = source_id
    root_id = id_gen.node_id(source_id, root_path)
    doc_node = Node(
        schema_version=SCHEMA_VERSION,
        run_id=run_id,
        created_at=now,
        node_id=root_id,
        source_id=source_id,
        source_hash=source_hash,
        node_type="document",
        section_path=root_path,
        title=source_title,
        text=source_title,
        retrievable_text=_clean(source_title),
        page_number=None,
        element_ref=None,
        parent_node_id=None,
        depth=0,
        block_ids=[],
    )
    nodes.append(doc_node)

    # Stack tracks (section_path_str, node_id, depth) for parent resolution
    path_stack: list[tuple[str, str, int]] = [(root_path, root_id, 0)]

    # Group consecutive non-heading blocks under the most recent heading
    current_heading_path: str = root_path
    current_heading_id: str = root_id
    current_heading_depth: int = 0

    for block in blocks:
        if block.block_type in ("citation_header",):
            # Treat as the document-level heading — already covered by doc_node
            doc_node.block_ids.append(block.block_id)
            continue

        if block.block_type == "metadata":
            # Metadata blocks become nodes directly under root
            meta_path = f"{root_path}::meta::{block.block_id}"
            nid = id_gen.node_id(source_id, meta_path)
            n = Node(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                node_id=nid,
                source_id=source_id,
                source_hash=source_hash,
                node_type="metadata_block",
                section_path=meta_path,
                title=None,
                text=block.text,
                retrievable_text=_clean(block.text),
                page_number=block.page_number,
                element_ref=block.element_ref,
                parent_node_id=root_id,
                depth=1,
                block_ids=[block.block_id],
            )
            nodes.append(n)
            continue

        if block.block_type == "history":
            continue  # history footers not indexed as retrieval nodes

        if block.block_type in ("heading",):
            # New section — update stack
            level = block.level if block.level is not None else 1
            depth = level + 1  # level 0 = depth 1 (under root)

            # Build section path from heading text
            section_label = block.text.strip()
            # Pop stack back to the appropriate parent depth
            while path_stack and path_stack[-1][2] >= depth:
                path_stack.pop()

            parent_path, parent_id, _ = path_stack[-1] if path_stack else (root_path, root_id, 0)
            section_path = f"{parent_path} > {section_label}"
            nid = id_gen.node_id(source_id, section_path)

            n = Node(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                node_id=nid,
                source_id=source_id,
                source_hash=source_hash,
                node_type=_node_type_from_block(block, depth),
                section_path=section_path,
                title=section_label,
                text=block.text,
                retrievable_text=_clean(block.text),
                page_number=block.page_number,
                element_ref=block.element_ref,
                parent_node_id=parent_id,
                depth=depth,
                block_ids=[block.block_id],
            )
            nodes.append(n)
            path_stack.append((section_path, nid, depth))
            current_heading_path = section_path
            current_heading_id = nid
            current_heading_depth = depth

        elif block.block_type in ("paragraph", "list_item"):
            # Attach to the most recent heading node's text
            if nodes and nodes[-1].node_id == current_heading_id:
                # Append text to the current heading node
                target = nodes[-1]
                if target.text != block.text:
                    combined = f"{target.text}\n{block.text}".strip()
                    # Replace the node in-place via index
                    idx = next(i for i, nd in enumerate(nodes) if nd.node_id == current_heading_id)
                    nodes[idx] = Node(
                        schema_version=target.schema_version,
                        run_id=target.run_id,
                        created_at=target.created_at,
                        node_id=target.node_id,
                        source_id=target.source_id,
                        source_hash=target.source_hash,
                        node_type=target.node_type,
                        section_path=target.section_path,
                        title=target.title,
                        text=combined,
                        retrievable_text=_clean(combined),
                        page_number=target.page_number,
                        element_ref=target.element_ref,
                        parent_node_id=target.parent_node_id,
                        depth=target.depth,
                        block_ids=target.block_ids + [block.block_id],
                    )
            else:
                # Standalone paragraph — create its own node
                depth = current_heading_depth + 1
                para_path = f"{current_heading_path} > p:{block.block_id[:8]}"
                nid = id_gen.node_id(source_id, para_path)
                n = Node(
                    schema_version=SCHEMA_VERSION,
                    run_id=run_id,
                    created_at=now,
                    node_id=nid,
                    source_id=source_id,
                    source_hash=source_hash,
                    node_type=_node_type_from_block(block, depth),
                    section_path=para_path,
                    title=None,
                    text=block.text,
                    retrievable_text=_clean(block.text),
                    page_number=block.page_number,
                    element_ref=block.element_ref,
                    parent_node_id=current_heading_id,
                    depth=depth,
                    block_ids=[block.block_id],
                )
                nodes.append(n)

        elif block.block_type == "table":
            depth = current_heading_depth + 1
            table_path = f"{current_heading_path} > table:{block.block_id[:8]}"
            nid = id_gen.node_id(source_id, table_path)
            n = Node(
                schema_version=SCHEMA_VERSION,
                run_id=run_id,
                created_at=now,
                node_id=nid,
                source_id=source_id,
                source_hash=source_hash,
                node_type="table",
                section_path=table_path,
                title=None,
                text=block.text,
                retrievable_text=_clean(block.text),
                page_number=block.page_number,
                element_ref=block.element_ref,
                parent_node_id=current_heading_id,
                depth=depth,
                block_ids=[block.block_id],
            )
            nodes.append(n)

    return nodes
