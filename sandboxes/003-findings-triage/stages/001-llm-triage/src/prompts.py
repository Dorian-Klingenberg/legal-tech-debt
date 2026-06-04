"""Prompt templates for Stage 001 LLM triage — versioned."""
from __future__ import annotations

TIER1_VERSION = "1.0.0"
TIER2_VERSION = "1.1.0"

# Model IDs — kept here so prompts.py is the single source of truth for versioning.
# triage_runner.py imports and uses these directly.
TIER1_MODEL = "gpt-4o-mini"
TIER2_MODEL = "gpt-4o"

# ---------------------------------------------------------------------------
# Tier 1 — mechanical annotation (Haiku or equivalent small/fast model)
# ---------------------------------------------------------------------------
# Audience: claims professional.
# Constraint: stay inside the evidence text. No invented facts, statutes, or
# dollar figures.

TIER1_SYSTEM = """\
You are a legal document analyst reviewing insurance policy filings for a claims professional.
Your job is to explain what a flagged issue means in plain terms a claims handler or coverage attorney can act on.
You may only draw on information present in the evidence text and the analysis provided.
Do not introduce statutes, case law, dollar figures, or legal conclusions not already stated in the input.
Respond with valid JSON only — no prose, no markdown fences."""

TIER1_USER_TEMPLATE = """\
A policy filing has been flagged for a potential issue. Annotate it.

SMELL: {smell_name}
HEURISTIC: {heuristic_id}
SOURCE: {source_id} ({source_type})
SECTION: {section_path}

EVIDENCE TEXT (excerpt from the filing):
{evidence_text}

DETECTOR RATIONALE:
{rationale}

REVIEWER QUESTION:
{reviewer_question}

FALSE POSITIVE NOTE:
{false_positive_risk}

CONFIDENCE: {confidence}

Respond with exactly this JSON structure:
{{
  "plain_english": "2-3 sentences. What is the problem in plain language a claims handler can understand? What does this language mean for a policyholder making a claim?",
  "dispute_scenario": "1-3 sentences. Describe a realistic claim scenario where this language causes a payment dispute or coverage denial. Focus on what happens at time of claim, not in a regulatory audit.",
  "fp_assessment": "1-2 sentences. Is this likely a real issue or a false positive? What specific check should a reviewer do to confirm?"
}}"""


# ---------------------------------------------------------------------------
# Tier 2 — judgment annotation (Sonnet or equivalent larger model)
# ---------------------------------------------------------------------------
# Audience: claims professional + executive sponsor.
# Constraint: base severity on claim frequency, litigation sensitivity,
# regulatory exposure only. No invented dollar figures.

TIER2_SYSTEM = """\
You are a senior insurance coverage analyst advising a claims professional and executive leadership.
Your job is to assess how seriously a flagged policy issue should be prioritized for remediation — based on its
potential to generate claim disputes, litigation exposure, or regulatory challenge in Kentucky.
Base your severity assessment only on claim frequency patterns, litigation sensitivity of the coverage area,
and regulatory exposure risk. Do not invent dollar amounts, settlement figures, or case citations.
Respond with valid JSON only — no prose, no markdown fences."""

TIER2_USER_TEMPLATE = """\
A policy filing has been flagged and pre-annotated. Provide severity and remediation guidance.

SMELL: {smell_name}
HEURISTIC: {heuristic_id}
SOURCE: {source_id} ({source_type})
SECTION: {section_path}
CONFIDENCE: {confidence}

EVIDENCE TEXT:
{evidence_text}

DETECTOR RATIONALE:
{rationale}

PLAIN-ENGLISH SUMMARY (from pre-annotation):
{plain_english}

DISPUTE SCENARIO (from pre-annotation):
{dispute_scenario}
{supporting_nodes_block}
Respond with exactly this JSON structure:
{{
  "business_severity": "HIGH or MEDIUM or LOW",
  "severity_rationale": "2-4 sentences. Why this severity? Address claim frequency likelihood, litigation sensitivity of this coverage area, and regulatory exposure in Kentucky specifically.",
  "remediation_direction": "1-3 sentences. What concrete action should a compliance team or filing attorney take? Be specific: add a definition, anchor a version reference, replace open-ended timing language, etc.",
  "triage_verdict": "One sentence combining detector confidence and business severity into a clear action signal for a claims reviewer. Examples: 'Confirm finding, then escalate — high consequence if real.' / 'Low confidence but high stakes — verify before filing.' / 'Likely real and moderate risk — assign for review.' Do not repeat the severity label verbatim."
}}"""

SUPPORTING_NODES_BLOCK_TEMPLATE = """\
SUPPORTING SECTIONS ({count} total carrier nodes with no regulatory edge):
{samples}
"""


def _safe(finding: dict, key: str) -> str:
    """Get a finding field and escape curly braces so str.format() won't choke."""
    return finding.get(key, "").replace("{", "{{").replace("}", "}}")


def build_tier1_prompt(finding: dict) -> tuple[str, str]:
    """Return (system, user) strings for Tier 1."""
    return TIER1_SYSTEM, TIER1_USER_TEMPLATE.format(
        smell_name=_safe(finding, "smell_name"),
        heuristic_id=_safe(finding, "heuristic_id"),
        source_id=_safe(finding, "source_id"),
        source_type=_safe(finding, "source_type"),
        section_path=_safe(finding, "section_path"),
        evidence_text=_safe(finding, "evidence_text"),
        rationale=_safe(finding, "rationale"),
        reviewer_question=_safe(finding, "reviewer_question"),
        false_positive_risk=_safe(finding, "false_positive_risk"),
        confidence=_safe(finding, "confidence"),
    )


def build_tier2_prompt(finding: dict, tier1: dict) -> tuple[str, str]:
    """Return (system, user) strings for Tier 2."""
    supporting_nodes = finding.get("supporting_nodes", [])
    if supporting_nodes:
        # Show first 3 supporting node section paths as context; don't flood the prompt
        samples = "\n".join(
            f"  - {n.get('section_path', '')}" for n in supporting_nodes[:3]
        )
        if len(supporting_nodes) > 3:
            samples += f"\n  ... and {len(supporting_nodes) - 3} more"
        supporting_nodes_block = "\n" + SUPPORTING_NODES_BLOCK_TEMPLATE.format(
            count=len(supporting_nodes), samples=samples
        )
    else:
        supporting_nodes_block = ""

    def _t1(key: str) -> str:
        return tier1.get(key, "").replace("{", "{{").replace("}", "}}")

    return TIER2_SYSTEM, TIER2_USER_TEMPLATE.format(
        smell_name=_safe(finding, "smell_name"),
        heuristic_id=_safe(finding, "heuristic_id"),
        source_id=_safe(finding, "source_id"),
        source_type=_safe(finding, "source_type"),
        section_path=_safe(finding, "section_path"),
        evidence_text=_safe(finding, "evidence_text"),
        rationale=_safe(finding, "rationale"),
        confidence=_safe(finding, "confidence"),
        plain_english=_t1("plain_english"),
        dispute_scenario=_t1("dispute_scenario"),
        supporting_nodes_block=supporting_nodes_block,
    )
