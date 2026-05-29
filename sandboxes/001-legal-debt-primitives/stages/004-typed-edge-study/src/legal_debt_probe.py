from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SECTION_HEADING_RE = re.compile(
    r"(?im)^\s{0,3}#{1,6}\s+(?:Section\s+)?(?P<section>\d+(?:\.\d+)*)\b(?P<title>[^\n]*)"
)
REFERENCE_RE = re.compile(r"\b(?:Section|Sec\.)\s+(?P<section>\d+(?:\.\d+)*)\b|§\s*(?P<section_symbol>\d+(?:\.\d+)*)")
DEFINITION_RE = re.compile(r'(?im)^[ \t]*[-*]?[ \t]*"(?P<term>[^"]+)"\s+means\b')
EXTERNAL_AUTHORITY_RE = re.compile(r"\b(?P<authority>NAIC|ISO|ACA|ERISA|FCRA|GDPR)\b(?P<context>[^\n.]{0,120})", re.IGNORECASE)
VERSION_HINT_RE = re.compile(r"\b(?:19|20)\d{2}\b|\bversion\b|\bv\d+\b|\beffective\b", re.IGNORECASE)


@dataclass(frozen=True)
class Section:
    id: str
    title: str
    document: str
    line: int
    body_offset: int
    body: str


@dataclass(frozen=True)
class Reference:
    from_section: str
    to_section: str
    document: str
    line: int
    snippet: str


@dataclass(frozen=True)
class Finding:
    detector: str
    severity: str
    document: str
    line: int
    message: str
    evidence: str


@dataclass(frozen=True)
class MatrixNode:
    key: str
    label: str
    kind: str
    section_id: str
    document: str
    line: int | None
    title: str


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def snippet_at(text: str, offset: int) -> str:
    start = max(text.rfind("\n", 0, offset) + 1, 0)
    end = text.find("\n", offset)
    if end == -1:
        end = len(text)
    return text[start:end].strip()


def read_corpus(corpus_dir: Path) -> dict[str, str]:
    documents: dict[str, str] = {}
    for path in sorted(corpus_dir.glob("*.md")):
        documents[path.name] = path.read_text(encoding="utf-8")
    return documents


def extract_sections(document: str, text: str) -> list[Section]:
    matches = list(SECTION_HEADING_RE.finditer(text))
    sections: list[Section] = []

    for index, match in enumerate(matches):
        section_id = match.group("section")
        title = match.group("title").strip(" .-")
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(
            Section(
                id=section_id,
                title=title,
                document=document,
                line=line_number(text, match.start()),
                body_offset=body_start,
                body=text[body_start:body_end],
            )
        )

    return sections


def extract_references(document: str, text: str, sections: list[Section]) -> list[Reference]:
    references: list[Reference] = []
    for section in sections:
        for match in REFERENCE_RE.finditer(section.body):
            to_section = match.group("section") or match.group("section_symbol")
            if not to_section:
                continue
            absolute_offset = section.body_offset + match.start()
            references.append(
                Reference(
                    from_section=section.id,
                    to_section=to_section,
                    document=document,
                    line=line_number(text, absolute_offset),
                    snippet=snippet_at(text, absolute_offset),
                )
            )
    return references


def detect_dangling_references(references: Iterable[Reference], known_sections: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for ref in references:
        if ref.to_section not in known_sections:
            findings.append(
                Finding(
                    detector="DanglingReference",
                    severity="high",
                    document=ref.document,
                    line=ref.line,
                    message=f"Section {ref.from_section} references missing Section {ref.to_section}.",
                    evidence=ref.snippet,
                )
            )
    return findings


def detect_circular_references(references: Iterable[Reference]) -> list[Finding]:
    edges = {(ref.from_section, ref.to_section): ref for ref in references if ref.from_section != "document"}
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()

    for (source, target), ref in edges.items():
        reverse = (target, source)
        if reverse in edges and tuple(sorted((source, target))) not in seen:
            seen.add(tuple(sorted((source, target))))
            findings.append(
                Finding(
                    detector="CircularReference",
                    severity="medium",
                    document=ref.document,
                    line=ref.line,
                    message=f"Section {source} and Section {target} reference each other.",
                    evidence=f"{ref.snippet} / {edges[reverse].snippet}",
                )
            )
    return findings


def detect_orphan_definitions(documents: dict[str, str]) -> list[Finding]:
    all_text = "\n".join(documents.values()).lower()
    findings: list[Finding] = []

    for document, text in documents.items():
        for match in DEFINITION_RE.finditer(text):
            term = match.group("term")
            occurrences = len(re.findall(rf"\b{re.escape(term.lower())}\b", all_text))
            if occurrences <= 1:
                findings.append(
                    Finding(
                        detector="OrphanDefinition",
                        severity="low",
                        document=document,
                        line=line_number(text, match.start()),
                        message=f'Defined term "{term}" appears to be unused outside its definition.',
                        evidence=snippet_at(text, match.start()),
                    )
                )
    return findings


def detect_unversioned_external_authorities(documents: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []
    for document, text in documents.items():
        for match in EXTERNAL_AUTHORITY_RE.finditer(text):
            evidence = snippet_at(text, match.start())
            if not VERSION_HINT_RE.search(evidence):
                findings.append(
                    Finding(
                        detector="UnversionedExternalAuthority",
                        severity="medium",
                        document=document,
                        line=line_number(text, match.start()),
                        message=f"{match.group('authority').upper()} is referenced without an obvious version, date, or effective source anchor.",
                        evidence=evidence,
                    )
                )
    return findings


def section_key(section_id: str) -> str:
    return f"section:{section_id}"


def missing_key(section_id: str) -> str:
    return f"missing:{section_id}"


def boolean_matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    result = [[0 for _ in range(size)] for _ in range(size)]

    for row_index, row in enumerate(left):
        active_columns = [column_index for column_index, value in enumerate(row) if value]
        for column_index in active_columns:
            right_row = right[column_index]
            for target_index, value in enumerate(right_row):
                if value:
                    result[row_index][target_index] = 1

    return result


def transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    closure = [row[:] for row in matrix]
    size = len(matrix)

    for intermediate in range(size):
        for source in range(size):
            if closure[source][intermediate]:
                for target in range(size):
                    if closure[intermediate][target]:
                        closure[source][target] = 1

    return closure


def build_matrix_nodes(sections: list[Section], references: list[Reference]) -> list[MatrixNode]:
    known_sections = {section.id for section in sections}
    nodes: list[MatrixNode] = []
    seen: set[str] = set()

    for section in sections:
        key = section_key(section.id)
        if key in seen:
            continue
        seen.add(key)
        nodes.append(
            MatrixNode(
                key=key,
                label=f"Section {section.id}",
                kind="section",
                section_id=section.id,
                document=section.document,
                line=section.line,
                title=section.title,
            )
        )

    missing_section_ids = sorted({ref.to_section for ref in references if ref.to_section not in known_sections})
    for section_id in missing_section_ids:
        nodes.append(
            MatrixNode(
                key=missing_key(section_id),
                label=f"Missing Section {section_id}",
                kind="missing",
                section_id=section_id,
                document="",
                line=None,
                title="unresolved reference target",
            )
        )

    return nodes


def build_adjacency_matrix(nodes: list[MatrixNode], references: list[Reference]) -> list[list[int]]:
    node_index = {node.key: index for index, node in enumerate(nodes)}
    known_section_ids = {node.section_id for node in nodes if node.kind == "section"}
    matrix = [[0 for _ in nodes] for _ in nodes]

    for ref in references:
        source_key = section_key(ref.from_section)
        target_key = section_key(ref.to_section) if ref.to_section in known_section_ids else missing_key(ref.to_section)
        if source_key not in node_index or target_key not in node_index:
            continue
        matrix[node_index[source_key]][node_index[target_key]] = 1

    return matrix


def dependency_roots(nodes: list[MatrixNode], closure: list[list[int]]) -> dict[str, list[str]]:
    roots_by_node: dict[str, list[str]] = {}

    for source_index, node in enumerate(nodes):
        reachable = [target_index for target_index, value in enumerate(closure[source_index]) if value]
        roots = [
            nodes[target_index].key
            for target_index in reachable
            if not any(closure[target_index])
        ]
        roots_by_node[node.key] = roots

    return roots_by_node


def write_section_index(path: Path, nodes: list[MatrixNode]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["index", "node_key", "label", "kind", "section_id", "document", "line", "title"])
        for index, node in enumerate(nodes):
            writer.writerow([index, node.key, node.label, node.kind, node.section_id, node.document, node.line or "", node.title])


def write_matrix_csv(path: Path, nodes: list[MatrixNode], matrix: list[list[int]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["depends_on"] + [node.key for node in nodes])
        for node, row in zip(nodes, matrix):
            writer.writerow([node.key] + row)


def write_dependency_roots(path: Path, nodes: list[MatrixNode], roots_by_node: dict[str, list[str]], closure: list[list[int]]) -> None:
    node_by_key = {node.key: node for node in nodes}
    cycle_nodes = [node.key for index, node in enumerate(nodes) if closure[index][index]]
    payload = {
        "edge_direction": "A[i,j] = 1 means node i depends on node j",
        "root_definition": "For a node, dependency roots are reachable dependency nodes with no further reachable dependencies in the closure matrix.",
        "nodes": [asdict(node) for node in nodes],
        "cycle_nodes": cycle_nodes,
        "roots_by_node": {
            key: [
                {
                    "key": root_key,
                    "label": node_by_key[root_key].label,
                    "kind": node_by_key[root_key].kind,
                }
                for root_key in roots
            ]
            for key, roots in roots_by_node.items()
        },
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def build_markdown_report(
    findings: list[Finding],
    references: list[Reference],
    sections: list[Section],
    roots_by_node: dict[str, list[str]],
    cycle_nodes: list[str],
) -> str:
    lines = [
        "# Legal Debt Probe Report",
        "",
        f"Sections found: {len(sections)}",
        f"References found: {len(references)}",
        f"Findings found: {len(findings)}",
        "",
        "## Findings",
        "",
    ]

    if not findings:
        lines.append("No findings.")
    else:
        for finding in findings:
            lines.extend(
                [
                    f"### {finding.detector} ({finding.severity})",
                    "",
                    f"- Source: `{finding.document}:{finding.line}`",
                    f"- Message: {finding.message}",
                    f"- Evidence: {finding.evidence}",
                    "",
                ]
            )

    lines.extend(["## Section Graph Edges", ""])
    for ref in references:
        lines.append(f"- Section {ref.from_section} -> Section {ref.to_section} (`{ref.document}:{ref.line}`)")

    lines.extend(
        [
            "",
            "## Matrix Outputs",
            "",
            "Matrix direction: `A[i,j] = 1` means node `i` depends on node `j`.",
            "",
            "- `section_index.csv`: matrix node index and labels",
            "- `adjacency_matrix.csv`: direct dependency matrix `A`",
            "- `two_hop_matrix.csv`: boolean matrix product `A^2`",
            "- `transitive_closure.csv`: all reachable dependencies",
            "- `dependency_roots.json`: terminal dependency roots and cycle nodes",
            "",
            "## Dependency Roots",
            "",
        ]
    )
    for node_key, roots in roots_by_node.items():
        if roots:
            lines.append(f"- `{node_key}` -> {', '.join(f'`{root}`' for root in roots)}")

    if cycle_nodes:
        lines.extend(["", "## Cycle Nodes", ""])
        for node_key in cycle_nodes:
            lines.append(f"- `{node_key}`")

    return "\n".join(lines) + "\n"


def run(corpus_dir: Path, out_dir: Path) -> dict[str, object]:
    documents = read_corpus(corpus_dir)
    sections_by_doc = {name: extract_sections(name, text) for name, text in documents.items()}
    sections = [section for doc_sections in sections_by_doc.values() for section in doc_sections]
    references = [
        reference
        for name, text in documents.items()
        for reference in extract_references(name, text, sections_by_doc[name])
    ]
    known_sections = {section.id for section in sections}
    matrix_nodes = build_matrix_nodes(sections, references)
    adjacency_matrix = build_adjacency_matrix(matrix_nodes, references)
    two_hop_matrix = boolean_matrix_multiply(adjacency_matrix, adjacency_matrix)
    closure_matrix = transitive_closure(adjacency_matrix)
    roots_by_node = dependency_roots(matrix_nodes, closure_matrix)
    cycle_nodes = [node.key for index, node in enumerate(matrix_nodes) if closure_matrix[index][index]]

    findings: list[Finding] = []
    findings.extend(detect_dangling_references(references, known_sections))
    findings.extend(detect_circular_references(references))
    findings.extend(detect_orphan_definitions(documents))
    findings.extend(detect_unversioned_external_authorities(documents))

    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "sections": [asdict(section) for section in sections],
        "references": [asdict(reference) for reference in references],
        "findings": [asdict(finding) for finding in findings],
        "matrix_nodes": [asdict(node) for node in matrix_nodes],
        "cycle_nodes": cycle_nodes,
    }
    write_section_index(out_dir / "section_index.csv", matrix_nodes)
    write_matrix_csv(out_dir / "adjacency_matrix.csv", matrix_nodes, adjacency_matrix)
    write_matrix_csv(out_dir / "two_hop_matrix.csv", matrix_nodes, two_hop_matrix)
    write_matrix_csv(out_dir / "transitive_closure.csv", matrix_nodes, closure_matrix)
    write_dependency_roots(out_dir / "dependency_roots.json", matrix_nodes, roots_by_node, closure_matrix)
    (out_dir / "findings.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (out_dir / "report.md").write_text(
        build_markdown_report(findings, references, sections, roots_by_node, cycle_nodes),
        encoding="utf-8",
    )
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a lightweight legal debt probe over a Markdown corpus.")
    parser.add_argument("--corpus", type=Path, required=True, help="Directory containing Markdown source documents.")
    parser.add_argument("--out", type=Path, required=True, help="Directory for report outputs.")
    args = parser.parse_args()

    payload = run(args.corpus, args.out)
    print(
        f"Wrote {len(payload['findings'])} findings, "
        f"{len(payload['references'])} references, "
        f"and {len(payload['sections'])} sections to {args.out}"
    )


if __name__ == "__main__":
    main()
