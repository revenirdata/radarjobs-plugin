# RadarJobs

**Find contract tech jobs with your RadarJobs account.** By
[Revenir](https://www.revenirdata.com).

RadarJobs connects through OAuth and reuses the account, setup, access, and
recommendations already owned by the Radar backend. It does not require an API
key and does not expose checkout, subscription changes, job applications, resume
upload, or new recommendation generation in ChatGPT.

## Tools

- `search_contract_jobs`: search current contract-tech inventory with bounded
  filters and at most five presentation-ready results.
- `get_my_radarjobs_recommendations`: read the existing personalized set.
- `get_contract_job`: inspect an eligible opportunity.

Search accepts ordinary role wording directly. It does not require an account
state or taxonomy preflight, and its result already includes the fields and links
needed for presentation. Clients must not call detail once per search result.

Search supports documented 1099, C2C, and W-2 contract arrangements. Unknown
compensation stays unknown. Remote does not guarantee worldwide eligibility.
Closest matching may relax only the title and reports that relaxation.

## Connection

The production MCP URL is
`https://api.revenirdata.com/radarjobs/mcp`. ChatGPT discovers OAuth metadata,
opens a Revenir-hosted consent page, and returns after the user approves the
`radarjobs:read` scope. The server derives identity from the token; tools never
accept an account ID or credential.

## Distribution status

Version 2.0.1 documents the deployed authenticated three-tool contract. It must
not be represented as submitted, approved, or publicly listed until those portal
steps actually occur.

[Privacy](https://www.revenirdata.com/privacy) ·
[Terms](https://www.revenirdata.com/terms) ·
[RadarJobs](https://www.revenirdata.com/radar/jobs) ·
[Support](https://www.revenirdata.com/support)

See [publication materials](docs/plugin-publication/README.md) for listing copy,
data flow, test evidence, reviewer checklist, and the demo-video storyboard.
