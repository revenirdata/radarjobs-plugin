# RadarJobs listing copy

| Field | Value |
|---|---|
| Name | RadarJobs |
| Subtitle | Search contract tech jobs |
| Developer | Revenir |
| Version | 2.0.0 |
| Category | Productivity |
| Website | https://www.revenirdata.com/radar/jobs |
| Support | https://www.revenirdata.com/support |
| Privacy | https://www.revenirdata.com/privacy |
| Terms | https://www.revenirdata.com/terms |
| MCP URL | https://api.revenirdata.com/radarjobs/mcp |
| Authentication | OAuth 2.1 authorization code with S256 PKCE |

## Description

Connect your RadarJobs account to search current contract technology
opportunities, inspect job details and taxonomy, check account readiness, and
review your existing personalized recommendations. RadarJobs uses the access and
setup state already attached to your account.

RadarJobs does not submit applications, save jobs, upload resumes, sell access,
start checkout, or change subscriptions in ChatGPT. Search supports documented
1099, C2C, and W-2 contract arrangements. Remote status does not guarantee
worldwide eligibility, and unknown compensation or eligibility remains unknown.

## Account and access

Connection uses the existing RadarJobs identity and membership. A user without an
account can create one in the adjacent Revenir authorization flow, then return to
approve the connection. Search requires existing active paid-equivalent access.
An eligible exploration account can read its current personalized preview.
Account status responses link neutrally to the RadarJobs account page; they do
not advertise plans or link directly to checkout.

## Capabilities

- Read the connected account's RadarJobs setup and access state.
- Search current contract technology inventory with bounded filters and at most
  five results.
- Read existing personalized recommendations; no recommendation generation.
- Inspect an eligible opportunity by UUID.
- Read RadarJobs taxonomy identifiers.

No job application, saved-job mutation, alert mutation, resume processing,
billing, subscription, email, crawling, or new model inference is exposed.

## Commerce answer

The plugin itself does not facilitate a purchase or expose checkout. Select
**No** when the portal asks whether this plugin performs commerce or enables a
purchase in ChatGPT. RadarJobs is an existing commercial service and the plugin
honors the user's existing entitlement; disclose that distinction if the portal
separately asks about the developer's business model.

## Release notes

Authenticated RadarJobs account connection with five bounded tools, S256 PKCE,
opaque rotating tokens, revocation, shared account entitlements, personalized
recommendation reads, and no in-chat commerce.
