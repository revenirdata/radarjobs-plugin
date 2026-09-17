# RadarJobs authenticated release evidence

Date: September 16, 2026. Candidate version: 2.0.0.

## Verified locally

Backend focused tests cover the five-tool descriptor contract, explicit hints,
output schemas, bounded search, unsupported filters, neutral entitlement
failure, taxonomy, fixed-origin job projection, guard limits, OAuth metadata,
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

Reviewable branches and current CI are linked below. Production MCP acceptance
remains required after review and deployment.

- Backend final-head CI: [successful validate run](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35173517484/job/105050080289) for commit `5a0e5d902725b0edffc5f8fa02fd0c9176373b6b`.
- Website final-head CI: [successful public-conversion run](https://github.com/revenirdata/revenir-website/actions/runs/35173758345/job/105050811876) and [successful Radar-product run](https://github.com/revenirdata/revenir-website/actions/runs/35173758248/job/105050811969) for commit `a6e0e176fe841cfeb77c000b09fc3f42f5354ee9`.

The official plugin validator passes. `chatgpt-app-submission.json` validates
against the live OpenAI Draft 2020-12 schema and contains five tools, exactly five
positive tests, and exactly three negative tests.

Review branches:

- backend OAuth and tools: [revenir-radar-backend PR #333](https://github.com/revenirdata/revenir-radar-backend/pull/333)
- consent and support pages: [revenir-website PR #110](https://github.com/revenirdata/revenir-website/pull/110)
- publication package: [radarjobs-plugin PR #2](https://github.com/revenirdata/radarjobs-plugin/pull/2)

## Production status

The currently deployed MCP still represents the previous anonymous version.
Version 2.0.0 must not be uploaded or demonstrated as complete until the reviewed
backend and website changes are deployed and the live endpoint exposes OAuth and
the five authenticated tools.

The support URL is intended to be
https://www.revenirdata.com/support. It becomes a valid submission value only
after the reviewed website change is deployed and returns HTTP 200.

## Historical evidence

The prior anonymous release was verified against backend production SHA
`159b9eb93fcee1f9000ca085f532cfd3f4e155aa`, including the shared
engagement-evidence correction. That evidence establishes inventory correctness
but does not establish authenticated version 2.0.0 behavior.
