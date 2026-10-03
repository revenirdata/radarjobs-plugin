# RadarJobs all-tech release evidence

Date: September 27, 2026. Candidate version: 1.0.2.

## Source validation

The backend release defines a separate all-tech OAuth resource at
`https://api.revenirdata.com/radarjobs/mcp-v3`. Its three tools are
`search_tech_jobs`, `get_my_radarjobs_recommendations`, and `get_tech_job`.
The existing contract-only v1/v2 resources remain unchanged for installed clients.

Backend validation covers national technology inventory eligibility, W-2 and
contract filtering, the three-tool descriptors, explicit annotations, output
schemas, OAuth resource metadata, bounded results, recommendation reads, and
eligible detail reads.

- Authoritative PostgreSQL CI: **1,458 passed, 7 skipped**, followed by the Run
  Inspector build and production-image build.
- Final-head CI:
  [run 36368745454](https://github.com/revenirdata/revenir-radar-backend/actions/runs/36368745454)
  for commit `11bcdba5b17f3af1dc0ca4a2a6692601651e90dc`.
- Local focused all-tech suite: **105 passed, 67 skipped**.
- Local full suite available without PostgreSQL: **1,020 passed, 445 skipped**.
- Ruff and the generated developer OpenAPI contract check passed.

Website validation covers the existing RadarJobs conversion funnel, national
metadata, state routes, OAuth consent copy, top-level product/API copy, and the
exact tagline “A clean contract for tech jobs data.”

- Full website suite: **294 passed**.
- Production build: passed.
- Final-head public-conversion and Radar-product checks:
  [PR #167](https://github.com/revenirdata/revenir-website/pull/167).

The distribution package passes Python compilation and JSON parsing.
`chatgpt-app-submission.json` contains exactly three tools, five positive test
cases, and three negative test cases. All three deployed tool descriptors declare
explicit read-only, open-world, and destructive hints plus output schemas.
No tool input solicits credentials, payment details, resumes, account IDs,
government identifiers, or MFA codes.

## Production verification

Backend revision `e7412e5f709b6f6ef52faee97d0362f7c26c1116` was deployed by
[production run 36369093810](https://github.com/revenirdata/revenir-radar-backend/actions/runs/36369093810).
Live verification confirmed:

- `/readyz` reports `ready`, PostgreSQL reports `ok`, and the exact build SHA is active.
- `/healthz` reports `ok`.
- `/.well-known/oauth-protected-resource/radarjobs/mcp-v3` advertises the exact
  v3 resource and `https://api.revenirdata.com/` authorization server.
- An unauthenticated MCP initialize request receives `401` with the v3 resource
  metadata challenge.

An authenticated v3 search was not run from this checkout because it has no
`RADARJOBS_ACCESS_TOKEN`. The authoritative backend CI verifies the exact v3 tool
catalog and behavior. The submission reviewer flow must still exercise OAuth and
one authenticated interaction before the release evidence is considered complete.

## Historical evidence

`docs/plugin-publication/history/` contains the earlier anonymous release
evidence. The current `search-evidence.json` remains v2 evidence until the
authenticated v3 verifier overwrites it.
