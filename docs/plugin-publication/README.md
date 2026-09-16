# RadarJobs publication package

Research date: September 16, 2026. Product version: 1.0.0. Developer: Revenir.

## Official public distribution answer

**Yes, the current official documentation describes self-service submission** at
[OpenAI Platform Plugins](https://platform.openai.com/plugins). An organization
owner or member with **Apps Management: Write** permissions can submit. Developer
or business identity verification is required. Review and subsequent publication
are separate steps; submission does not guarantee approval or visibility.

The current browser reached the portal's login page. Revenir's organization
identity verification, role, and account-specific eligibility have not been
verified. No draft, public submission, contact to OpenAI, or listing change has
been made. Owner approval is required before submission.

The official process requires a reachable public HTTPS MCP server, accurate tool
metadata and annotations, listing assets, privacy/terms/support information,
test cases, country availability, and required attestations. Authenticate only
if needed; RadarJobs 1.0.0 is anonymous. Provide no demo credentials. Complete
any portal-issued domain challenge only after the actual challenge is issued;
never invent a token. Review duration varies; no fixed SLA is promised.

After approval, the developer publishes through the portal. That is the route
to the public directory shared by ChatGPT and Codex, subject to surface/platform
support. A local install, GitHub import, or workspace listing is not that event.

**OpenAI Verified is separate:** OpenAI works with selected developers to review
quality, reliability and usefulness. Public submission or listing does not
automatically confer this badge. No independent badge application or guaranteed
eligibility was established by the documentation reviewed.

## Architecture

One remote MCP-backed plugin plus one precise skill. A registered RadarJobs app
ID is not available in the account's installed catalog; inventing an `.app.json`
reference would not create an app. The HTTPS MCP server reuses the existing
Radar backend, public query semantics, taxonomy and liveness policy. No duplicate
database, ranker, auth, billing or language parser exists in the package.

The current local official scaffold emits `.codex-plugin/plugin.json`; current
OpenAI documentation still supports that compatibility form alongside the newer
portable root manifest. We use the supported scaffold/validator output rather
than maintain competing manifests. Imported MCP plugins can receive **Desktop
only**, even with HTTPS. ChatGPT web availability requires the supported reviewed
integration path and must be verified after approval; it is not promised today.

## Distribution surfaces

- A: local installation and actual execution evidence belong in `test-evidence.md`.
- B: public GitHub marketplace is a separate manual distribution route.
- C: package is importable by eligible workspace administrators; no workspace publication is implied.
- D: materials are prepared here; eligibility, domain verification and final portal attestations remain owner actions where required.
- E: not submitted. Explicit owner approval required.
- F: not publicly listed. No OpenAI Verified claim.

## Official sources

- [Submission workflow](https://developers.openai.com/plugins/deploy/submission)
- [Building plugins and manifests](https://developers.openai.com/plugins/build/plugins)
- [Review requirements](https://developers.openai.com/plugins/deploy/app-review)
- [Plugin guidelines](https://developers.openai.com/plugins/app-guidelines)
- [ChatGPT plugin documentation](https://learn.chatgpt.com/docs/plugins)
- [Availability, workspace boundaries, Desktop only and Verified](https://help.openai.com/en/articles/20001256/)
- [Official OpenAI plugin examples](https://github.com/openai/plugins)

## Contents

`listing-copy.md`, `review-checklist.md`, `privacy-data-flow.md`, `test-evidence.md`,
`screenshots/` and `assets/`. The screenshots must use recorded real responses or
an explicitly labeled example, never invented inventory or a fabricated Codex UI.


## Asset format and portal boundary

The installed official manifest validator accepts PNG screenshot assets under
`assets/`; no fixed pixel dimensions were specified in that local schema. The
prepared interaction examples use 2000 × 1250 PNG and real recorded responses,
with an explicit label distinguishing them from Codex application screenshots.
Any additional portal-specific crop/size requirement must be checked after login.
The existing Revenir square logo is reused unchanged in light/dark contexts.
