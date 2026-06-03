# Secret Scan Report

_Date: 2026-06-01_

## Summary

A read-only secret scan triage was performed against this repository.

## Review status

**Complete. No action required.**

On 2026-06-03, the repo owner reviewed the reported secret-scan findings and confirmed that they are false positives. The identified values are public client-side keys, public vendor/embed identifiers, or scanner matches from archived/source-captured third-party HTML under `sources/`, not this repository's operational secrets.

### Findings

Several secret-like values were identified, primarily inside archived or source-captured third-party HTML files under `sources/`.

These were reviewed and classified as false positives: public frontend keys or third-party embed tokens from archived/source-captured third-party HTML, not this organization's own operational secrets.

### Notable examples

- Google API key-like values found in archived HTML/JS.
- Public-looking analytics or vendor keys such as Segment write keys, search keys, Datadog/public browser tokens, reCAPTCHA site keys, and embed tokens.
- Because this repository appears to store captured third-party web content, some scanner hits may be expected false positives or public client keys.

## Action requested

No follow-up action is requested. Future agents should not treat this report as an open blocker.

## Suggested next checks

None required based on the owner's 2026-06-03 review.
