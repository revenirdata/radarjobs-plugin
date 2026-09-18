# RadarJobs authenticated release evidence

Date: September 18, 2026. Candidate version: 2.0.2.

## Prior candidate validation

Backend focused tests cover the three-tool descriptor contract, explicit hints,
output schemas, bounded presentation-ready search, unsupported filters, neutral
entitlement failure, source and RadarJobs links, guard limits, OAuth metadata,
unauthenticated MCP rejection, and RadarJobs-deletion grant cleanup.
The current focused result is **51 passed, 7 skipped**. The skips are
PostgreSQL-backed tests because Docker Desktop was unavailable locally. The
latest complete local backend suite is **730 passed, 367 skipped**; skipped tests
are the repository's PostgreSQL-backed integration groups in this environment.

The authenticated OAuth lifecycle matrix covers authorization-code exchange,
code replay rejection, refresh rotation and replay-family revocation, explicit
revocation, and cross-account subject isolation. It is implemented but remains
part of the PostgreSQL-backed group that could not run locally.

Website tests cover the dedicated support page, noindex connection page, bounded
request handle, sign-in/sign-up return path, OpenAI attribution, disclosed data
categories, absence of checkout copy, same-origin approval, and server-held Radar
session use. The full website Node suite also passes.
The full result is **260 passed**. ESLint passes for every changed TypeScript
component and route. Repository-wide TypeScript is blocked in this sparse
worktree by pre-existing missing static image modules, not by a reported error in
the changed files.

The deployed correction passed final-head backend CI and the distribution package
passed the skill validator, plugin validator, Python compilation, JSON parsing,
and stale-reference scan.

- Backend final-head CI: [successful validate run](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35330848987/job/105554602962) for commit `8462e0824b3ee71b236c357c416d532c074d75da`.
- Website final-head CI: [successful public-conversion run](https://github.com/revenirdata/revenir-website/actions/runs/35173758345/job/105050811876) and [successful Radar-product run](https://github.com/revenirdata/revenir-website/actions/runs/35173758248/job/105050811969) for commit `a6e0e176fe841cfeb77c000b09fc3f42f5354ee9`.

The official plugin validator passes. `chatgpt-app-submission.json` uses the
Apps SDK `$schema` URL required by the submission portal and installed OpenAI
submission skill. That URL currently redirects to the `/plugins/` schema, whose
internal `$schema` constant still names the redirected URL; after substituting
only that upstream constant, the payload validates against the remaining live
Draft 2020-12 schema. It contains three tools, exactly five positive tests, and
exactly three negative tests.

Review branches:

- backend OAuth and tools: [revenir-radar-backend PR #333](https://github.com/revenirdata/revenir-radar-backend/pull/333)
- consent and support pages: [revenir-website PR #110](https://github.com/revenirdata/revenir-website/pull/110)
- direct-search server correction: [revenir-radar-backend PR #346](https://github.com/revenirdata/revenir-radar-backend/pull/346)
- versioned MCP transport URL: [revenir-radar-backend PR #347](https://github.com/revenirdata/revenir-radar-backend/pull/347)
- three-tool publication package: [radarjobs-plugin PR #3](https://github.com/revenirdata/radarjobs-plugin/pull/3)

## Production status

Production exposes the authenticated three-tool contract at
`https://api.revenirdata.com/radarjobs/mcp-v2`. Live verification against backend SHA
`f6056ee81fa5d5b35847964270512e87dcef8c01` confirmed that the versioned transport is deployed,
requires OAuth, and advertises the canonical RadarJobs protected-resource metadata. The
authenticated verifier for the same mounted application confirmed MCP version 2.2.1, the exact tool catalog,
presentation-ready output schema, source and RadarJobs links, and a bounded
five-result search in 1.872 seconds. The [production deployment](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35331308035)
and [authenticated verifier](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35331501879)
both completed successfully. The versioned route was deployed by [production run 35335551713](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35335551713).
Its distinct transport URL prevents an existing ChatGPT connector cache from retaining
the retired account-state and taxonomy tools while preserving the same OAuth resource.

The deployed support URL is https://www.revenirdata.com/support and returns the
reviewed customer-support surface.

## Historical evidence

The prior anonymous release was verified against backend production SHA
`159b9eb93fcee1f9000ca085f532cfd3f4e155aa`, including the shared
engagement-evidence correction. That evidence establishes inventory correctness
but does not establish authenticated version 2.0.2 behavior.
