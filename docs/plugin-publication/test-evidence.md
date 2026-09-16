# RadarJobs verification — September 16, 2026

This records actual checks, not a public-directory approval. Raw public MCP
responses are in `search-evidence.json`; installed metadata is in
`local-install-proof.json`; legal route checks are in `legal-url-proof.json`.

## Live anonymous acceptance

Production endpoint: `https://api.revenirdata.com/radarjobs/mcp`. No account,
API key, cookies, test inventory or additional LLM inference was used.

| Request | Actual result | Tool latency |
|---|---|---|
| Remote 1099 senior data engineering | 5 live normalized matches | 919 ms |
| C2C Snowflake contracts | 4 live normalized matches | 1,420 ms |
| Remote AI engineer contracts | 5 live normalized matches | 1,197 ms |
| At least 80 USD/hour | 1 match in disclosed recent-2,000 preview | 947 ms |
| Forward deployed engineer or AI engineer | 5 exact matches; no relaxation needed | 761 ms |
| Deliberately nonexistent title | 0 results | 1,207 ms |
| Unsupported `skills` field | Validation error, no invented filter | 492 ms |
| Permanent nursing job | Validation error, outside contract-tech scope | 457 ms |

Initialization, `tools/list`, taxonomy and detail were exercised over real HTTP.
The returned surface contains exactly `search_contract_jobs`, `get_contract_job`
and `get_contract_job_taxonomy`. Assertions check the five-result bound, live
status, requested contract/remote filters, hourly USD rates, preserved role
filters during title relaxation, and fixed-origin campaign links.

These are normalized inventory matches, not independently verified hiring
eligibility. One returned record contains W-2-only evidence alongside a 1099
label. The skill explicitly requires surfacing such conflicts and preserving
uncertainty. The complete raw matrix is retained, including thin source titles;
the listing examples show three selected real records per request.

## Result links and attribution

An initial job click exposed a pre-existing slow related-card query: 6.326 seconds
of a 6.748-second backend detail request. It intermittently exceeded the website's
eight-second timeout and became a false 404. Backend PR #331 bounds related-card
candidates to 500 recent same-family technology opportunities before existing
contract, freshness and indexability filtering. Main job eligibility is unchanged.

The resumed acceptance check (`python scripts/verify-live.py --links-only`)
records final HTTP status, rendered title, signup CTA, unchanged opportunity ID,
attributed URL and deployment identifiers in `search-evidence.json`.

All five links passed: HTTP 200, correct rendered title and signup CTA, with
214–1,155 ms website responses. Two direct backend detail reads completed in
973 ms and 1,609 ms after the fix. A real Snowflake result was also opened in
the background browser and showed the correct job, contract type, source, CTA
and retained campaign URL.

Final backend production SHA: `d6e2c7652b8702e7131e1d05fd09bf883e6e47e6`.
[Deployment run 35089121077](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35089121077) completed successfully.

Website tests verify the exact `openai / plugin / radarjobs_codex` campaign and
public-job/landing paths, using existing first/latest-touch and signup attribution.
No fake user signup or customer account was created for acceptance.

## Repository checks

- Backend PRs [#329](https://github.com/revenirdata/revenir-radar-backend/pull/329),
  [#330](https://github.com/revenirdata/revenir-radar-backend/pull/330), and
  [#331](https://github.com/revenirdata/revenir-radar-backend/pull/331).
- Final backend CI: **1,058 passed, 1 skipped**, with PostgreSQL;
  [run 35088678425](https://github.com/revenirdata/revenir-radar-backend/actions/runs/35088678425).
  Ruff, repository boundaries, public developer contract, migrations, production
  image and Run Inspector build passed. The earlier plugin-only release CI passed
  1,057 tests; the additional regression verifies bounded related previews.
- Local focused backend checks: **31 passed, 1 skipped**. The skipped local test
  requires PostgreSQL; database-backed checks ran in CI.
- Tests exercise invalid filters, anonymous bounds, safe projection, prompt-injection
  text handling, closest-mode preservation, body/protocol limits, spoofed proxy
  headers, atomic rate admission and fail-closed telemetry.
- Website [PR #109](https://github.com/revenirdata/revenir-website/pull/109):
  **255 Node tests passed**, TypeScript and Next.js production build passed;
  deployment and required GitHub checks passed. Live website SHA:
  `6eae2e0707fd3f490156f216146be5da94b23d72`.
- Official plugin validator and official skill validator passed. The skill validator
  requires Python UTF-8 mode on Windows (`python -X utf8`).

## Local installation and appearance evidence

`codex plugin add radarjobs@personal` installed and enabled the plugin. Codex's
actual `plugin/read` response recognizes RadarJobs, Revenir, the description,
three starter prompts, the company logo, both image assets, the enabled skill
and remote MCP server. The local development version is
`1.0.0+codex.20260916111144`; the distributable package remains `1.0.0`.

**Native Codex plugin-panel rendering was not visually inspected:** native app
control is unavailable in this session. Recognition and asset existence are
verified through the app-server, not claimed as a visual screenshot. A new task
is needed to load the newly installed plugin into an existing Codex session.

The two 2000 × 1250 PNGs were rendered in the background browser from recorded
production responses and visually inspected. They reuse the actual Revenir logo,
and each states **“Illustrated tool response, not a Codex UI screenshot.”** They
are listing examples, not evidence of a fabricated Codex interface.

## Public submission boundary

The official portal was reached, but it requires login. No organization identity,
role, domain challenge, countries or attestation was guessed. No submission,
OpenAI contact, workspace publication or public-directory listing was performed.
Owner authorization is required before public submission. OpenAI review and
publication remain separate from GitHub/manual installation.
