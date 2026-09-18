# RadarJobs public submission package

Candidate version: 2.0.1. Developer: Revenir.

This directory is the review source of truth for the authenticated RadarJobs
plugin. The plugin connects to one existing RadarJobs account through OAuth and
exposes three bounded tools for contract-job search, existing recommendations,
and eligible job detail. Search accepts ordinary role wording and returns
presentation-ready results without readiness, taxonomy, or per-result detail
preflights.

## Portal values

- Website: https://www.revenirdata.com/radar/jobs
- Support: https://www.revenirdata.com/support
- Privacy: https://www.revenirdata.com/privacy
- Terms: https://www.revenirdata.com/terms
- MCP: https://api.revenirdata.com/radarjobs/mcp
- Authentication: OAuth 2.1 authorization code with S256 PKCE
- Commerce in ChatGPT: No

The support URL and authenticated MCP are deployed and live-verified values.

## Contents

- `listing-copy.md`: portal-facing product and capability copy.
- `privacy-data-flow.md`: OAuth, data use, isolation, disconnect, and deletion.
- `entitlement-mapping.md`: exact backend state to plugin behavior.
- `review-checklist.md`: completed source checks and unresolved owner/live steps.
- `test-evidence.md`: verified local and deployed production results.
- `reviewer-demo.md`: exact video script, prompts, and privacy QA.
- `reviewer-account-plan.md`: owner-gated synthetic reviewer access and cleanup.
- `chatgpt-app-submission.json` at repository root: generated partial form data.

`search-evidence.json` records the current authenticated three-tool production
verification. The images under `screenshots/` and `assets/`, the evidence under
`history/`, and `scripts/build-historical-demo.py` document the earlier anonymous
release. They are retained as explicitly labeled history and must not be uploaded
as authenticated 2.0.1 interaction evidence. The reviewer demo must be recorded
from the deployed authenticated production flow.

## Submission boundary

The repository does not establish developer identity, business verification,
portal permissions, a domain verification token, launch countries, reviewer
credentials, or attestation authority. Those values stay unresolved for the
authorized owner. No submission, upload, merge, deployment, review approval,
listing, or Verified status is claimed.
