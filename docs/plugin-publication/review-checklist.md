# RadarJobs authenticated submission checklist

## Source and security

- [x] Five tools inspected against their implementations.
- [x] Every tool declares all three hints explicitly.
- [x] Every tool declares an output schema.
- [x] No tool input solicits credentials, payment details, resumes, or account IDs.
- [x] OAuth uses authorization code flow, S256 PKCE, resource binding, short-lived
  access tokens, refresh rotation, replay-family revocation, and a revocation
  endpoint.
- [x] Existing RadarJobs identity, profile, membership, and recommendations remain
  authoritative.
- [x] No in-chat purchase, checkout, subscription mutation, job application, or
  message sending.
- [x] RadarJobs deletion removes plugin grants and tokens.

## Review assets

- [x] Listing copy and privacy/data-flow documentation updated for authentication.
- [x] Dedicated customer-support page implemented at `/support`.
- [x] Reviewer demo storyboard and exact prompts prepared.
- [x] Exactly five positive and three negative submission tests prepared.
- [ ] Authenticated production MCP and support URL deployed after owner review.
- [ ] Reviewer account created with usable access and no MFA/email/SMS challenge.
- [ ] Demo video recorded against deployed production and checked for secrets/PII.
- [ ] Final production OAuth and cross-account isolation matrix completed.

## Account-bound portal fields

- [ ] Revenir developer/business verification confirmed in the portal.
- [ ] Apps Management: Write permission confirmed.
- [ ] Portal-issued domain challenge completed if requested.
- [ ] Exact launch countries selected by the authorized owner.
- [ ] Reviewer credentials entered only in the portal, never committed.
- [ ] Final attestations reviewed and approved by the owner.
- [ ] Owner manually uploads `chatgpt-app-submission.json` and the demo video.

No submission, review approval, publication, public listing, or Verified status is
claimed by this repository.
