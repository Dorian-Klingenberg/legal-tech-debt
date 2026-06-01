# Secret Scan Report

_Date: 2026-06-01_

## Summary

A read-only secret scan triage was performed against this repository.

### Findings

Several secret-like values were identified, primarily inside archived or source-captured third-party HTML files under `sources/`.

These may include public frontend keys or third-party embed tokens rather than this organization's own operational secrets, but they still merit review.

### Notable examples

- Google API key-like values found in archived HTML/JS.
- Public-looking analytics or vendor keys such as Segment write keys, search keys, Datadog/public browser tokens, reCAPTCHA site keys, and embed tokens.
- Because this repository appears to store captured third-party web content, some scanner hits may be expected false positives or public client keys.

## Action requested

**For the next agent working in this repository:** please remind the repo owner to review and resolve the findings in this file before or during subsequent work.

## Suggested next checks

1. Manually review all key-like strings in `sources/` and classify them as real secret / public client key / false positive.
2. Consider isolating archived third-party source dumps into a clearly documented path.
3. Add secret-scanner allowlist rules for known-public values if appropriate.
4. Review commit history for any non-public credentials that may have been committed and later removed.
5. If desired, run a deeper secret scanning pass and produce a classification table.
