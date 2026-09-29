# RadarJobs listing copy

| Field | Value |
|---|---|
| Name | RadarJobs |
| Subtitle | Find tech jobs |
| Developer | Revenir |
| Version | 3.0.0 |
| Category | Productivity |
| Website | https://www.revenirdata.com/radar/jobs |
| Support | https://www.revenirdata.com/support |
| Privacy | https://www.revenirdata.com/privacy |
| Terms | https://www.revenirdata.com/terms |
| MCP URL | https://api.revenirdata.com/radarjobs/mcp-v3 |
| Authentication | OAuth 2.1 authorization code with S256 PKCE |

## Description

Connect your RadarJobs account to search current U.S. technology jobs across
ordinary W-2 employment and contract work, inspect a selected job, and review your personalized
recommendations. Search accepts ordinary role wording and returns presentation-ready
results with both the actual source posting and RadarJobs detail links.

RadarJobs does not submit applications, save jobs, upload resumes, sell access,
start checkout, or change subscriptions in ChatGPT. Search supports documented
ordinary W-2 employment plus 1099, C2C, and W-2 contract arrangements. Remote status does not guarantee
worldwide eligibility, and unknown compensation or eligibility remains unknown.

## Account and access

Connection uses the existing RadarJobs identity and membership. A user without an
account can create one in the adjacent Revenir authorization flow, then return to
approve the connection. Search requires existing active paid-equivalent access.
An eligible exploration account can read its current personalized preview.
Account status responses link neutrally to the RadarJobs account page; they do
not advertise plans or link directly to checkout.

## Capabilities

- Search current U.S. technology inventory with bounded filters and at most
  five results.
- Read existing personalized recommendations; no recommendation generation.
- Inspect an eligible opportunity by UUID.

No job application, saved-job mutation, alert mutation, resume processing,
billing, subscription, email, crawling, or new model inference is exposed.

## Commerce answer

The plugin itself does not facilitate a purchase or expose checkout. Select
**No** when the portal asks whether this plugin performs commerce or enables a
purchase in ChatGPT. RadarJobs is an existing commercial service and the plugin
honors the user's existing entitlement; disclose that distinction if the portal
separately asks about the developer's business model.

## Release notes

Expanded RadarJobs from contract-only search to current U.S. technology jobs while preserving deep contract filters, with three bounded tools, S256 PKCE,
opaque rotating tokens, revocation, shared account entitlements, personalized
recommendation reads, and no in-chat commerce.
