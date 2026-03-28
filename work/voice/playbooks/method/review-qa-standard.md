# Voice Review / QA Standard

Purpose: define the minimum standard for review-readiness and QA-readiness.

## Review packet must include

- objective
- asset under review
- current scope
- confirmed signal
- unverified areas
- what looks strong
- what looks weak
- missing before review-ready
- missing before deploy-ready
- recommended patch set
- recommended next move

## QA note must include

- scope tested
- confirmed behavior
- unverified behavior
- known risks
- recommended next move

## Evidence labels

Use these labels explicitly:
- confirmed
- inferred
- assumed
- unverified

## Readiness rule

Keep these states separate:
- review-ready
- deploy-ready
- live-proven

Do not collapse them into one confidence claim.

## Review language rule

Review output must be concrete enough that Adam or a collaborator can act on it without extra interpretation.

## QA language rule

QA notes should describe real evidence, not confidence theater.
If a path was not tested, say so directly.
