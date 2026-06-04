"""Stage 001: LLM-assisted finding triage.

Reads detector_findings.jsonl from a Sandbox 002 Stage 006 run, enriches each
finding with two LLM annotation tiers, and writes enriched_findings.jsonl.

Usage:
    python triage_runner.py [--findings PATH] [--output PATH] [--sample N]

Defaults:
    --findings  sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl
    --output    sandboxes/003-findings-triage/stages/001-llm-triage/output/enriched_findings.jsonl
    --sample    0  (0 = all findings)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parents[5] / ".env")

from models import EnrichedFinding, JudgmentAnnotation, TriageAnnotation
from prompts import (
    TIER1_MODEL,
    TIER1_VERSION,
    TIER2_MODEL,
    TIER2_VERSION,
    build_tier1_prompt,
    build_tier2_prompt,
)

REPO_ROOT = Path(__file__).resolve().parents[5]

DEFAULT_FINDINGS = (
    REPO_ROOT
    / "sandboxes/002-claims-regulatory-automation/output/006/20260604_130606_18b0dec5/detector_findings.jsonl"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "sandboxes/003-findings-triage/stages/001-llm-triage/output/enriched_findings.jsonl"
)
MAX_TOKENS = 1024
RETRY_LIMIT = 3
RETRY_DELAY = 5.0


def call_llm(client: OpenAI, model: str, system: str, user: str) -> str:
    for attempt in range(1, RETRY_LIMIT + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=MAX_TOKENS,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            return response.choices[0].message.content
        except Exception as exc:
            if attempt == RETRY_LIMIT:
                raise
            print(f"  [retry {attempt}/{RETRY_LIMIT}] {exc}", file=sys.stderr)
            time.sleep(RETRY_DELAY)
    raise RuntimeError("unreachable")


def parse_json_response(raw: str, finding_id: str, tier: str) -> dict:
    # Strip markdown code fences that some models wrap around JSON
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[-1]
        text = text.rsplit("```", 1)[0].strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        print(
            f"  [WARN] JSON parse failed for {finding_id} tier={tier}: {exc}",
            file=sys.stderr,
        )
        # Return a stub so the run doesn't abort; flag it for manual review
        return {"_parse_error": str(exc), "_raw": raw}


def enrich_finding(client: anthropic.Anthropic, finding: dict) -> EnrichedFinding:
    fid = finding.get("finding_id", "?")

    # Tier 1
    sys1, usr1 = build_tier1_prompt(finding)
    raw1 = call_llm(client, TIER1_MODEL, sys1, usr1)
    t1 = parse_json_response(raw1, fid, "tier1")

    triage = TriageAnnotation(
        plain_english=t1.get("plain_english", t1.get("_raw", "")),
        dispute_scenario=t1.get("dispute_scenario", ""),
        fp_assessment=t1.get("fp_assessment", ""),
        model=TIER1_MODEL,
        prompt_version=TIER1_VERSION,
    )

    # Tier 2
    sys2, usr2 = build_tier2_prompt(finding, t1)
    raw2 = call_llm(client, TIER2_MODEL, sys2, usr2)
    t2 = parse_json_response(raw2, fid, "tier2")

    judgment = JudgmentAnnotation(
        business_severity=t2.get("business_severity", ""),
        severity_rationale=t2.get("severity_rationale", t2.get("_raw", "")),
        remediation_direction=t2.get("remediation_direction", ""),
        triage_verdict=t2.get("triage_verdict", ""),
        model=TIER2_MODEL,
        prompt_version=TIER2_VERSION,
    )

    return EnrichedFinding(original=finding, triage=triage, judgment=judgment)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--findings", type=Path, default=DEFAULT_FINDINGS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sample", type=int, default=0, help="0 = all findings")
    args = parser.parse_args()

    if not args.findings.exists():
        sys.exit(f"Findings file not found: {args.findings}")

    findings = []
    with open(args.findings, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                findings.append(json.loads(line))

    if args.sample > 0:
        findings = findings[: args.sample]

    print(f"Enriching {len(findings)} finding(s)...")
    print(f"  Tier 1 model: {TIER1_MODEL}")
    print(f"  Tier 2 model: {TIER2_MODEL}")
    print(f"  Output: {args.output}")

    client = OpenAI()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    enriched = []
    errors = []
    for i, finding in enumerate(findings, 1):
        fid = finding.get("finding_id", f"#{i}")
        smell = finding.get("smell_id", "?")
        print(f"  [{i}/{len(findings)}] {fid} (smell {smell})", end="", flush=True)
        try:
            result = enrich_finding(client, finding)
            enriched.append(result)
            print(" OK")
        except Exception as exc:
            print(f" ERROR: {exc}")
            errors.append({"finding_id": fid, "error": str(exc)})

    with open(args.output, "w", encoding="utf-8") as fh:
        for ef in enriched:
            fh.write(json.dumps(ef.to_dict(), ensure_ascii=False) + "\n")

    print(f"\nDone. {len(enriched)} enriched, {len(errors)} errors.")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  {e['finding_id']}: {e['error']}")

    # Write a brief run manifest alongside the output
    manifest = {
        "stage": "003-001-llm-triage",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "findings_source": str(args.findings),
        "total_findings": len(findings),
        "enriched": len(enriched),
        "errors": len(errors),
        "tier1_model": TIER1_MODEL,
        "tier2_model": TIER2_MODEL,
        "tier1_prompt_version": TIER1_VERSION,
        "tier2_prompt_version": TIER2_VERSION,
    }
    manifest_path = args.output.parent / "run_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
