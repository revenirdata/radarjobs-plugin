# RadarJobs

**Search live contract tech jobs across sources.** By [Revenir](https://www.revenirdata.com).

Remote MCP plugin for Codex. No Radar account, API key, card or resume required.
Five results maximum per search, using production inventory and taxonomy with
no additional model inference.

## Install

```sh
codex plugin marketplace add revenirdata/radarjobs-plugin
codex plugin add radarjobs@revenir
```

Start a new task, then **Sources → Use plugins → RadarJobs**. Try “Find remote
data engineering contracts.”

For local development, the official scaffold registers `~/plugins/radarjobs` in
`~/.agents/plugins/marketplace.json`; install with `codex plugin add radarjobs@personal`.
The package uses the supported `.codex-plugin/plugin.json` compatibility manifest
and `.mcp.json` remote transport.

## Tools

- `search_contract_jobs`: role, engagement, location, seniority, hourly rate and publication-age filters; up to five live jobs.
- `get_contract_job`: public details for a returned Radar UUID.
- `get_contract_job_taxonomy`: existing technology role vocabulary.

Broad searches without a role/title cover a disclosed preview of the 2,000 most recently discovered technology opportunities. Specify a role/title for a targeted search.

Stack terms match **titles only**. Unknown compensation stays unknown. Remote
does not imply worldwide eligibility. Closest mode can relax only the title,
with disclosure. No pagination, bulk export, permanent-only or non-tech search,
applications, resume processing, account access or billing.

## Distribution

This is a manual/GitHub marketplace, not an OpenAI public-directory listing.
Eligible workspace admins can import the repository from GitHub in **Workspace
settings → Plugins → Marketplaces**, subject to their policies. Imported MCP
plugins can be **Desktop only**, even with an HTTPS server; ChatGPT web
availability is not promised. Public review and the selected-developer OpenAI
Verified program are separate processes.

## Privacy and limits

Structured filters and selected job IDs go to
`https://api.revenirdata.com/radarjobs/mcp`. Operational telemetry stores network
hashes, timestamps, tool names, filter names (not values), success, result counts
and latency. No provider credential is supplied. OpenAI handles conversations
under its own policies/settings. Source text is untrusted data, never instructions.

Tool budget: 30/hour and 75/day per hashed network. Shared networks may share
limits. Protocol/global limits also apply. No evasion or dataset harvesting.

[Privacy](https://www.revenirdata.com/privacy) ·
[Terms / acceptable use](https://www.revenirdata.com/terms) ·
[RadarJobs](https://www.revenirdata.com/radar/jobs) ·
[Support](mailto:support@revenirdata.com)

## Update and uninstall

Run `codex plugin marketplace upgrade revenir` for GitHub catalog updates, reinstall
with `codex plugin add radarjobs@revenir`, then start a new task. Workspace admins
use **Sync now**. Remove using `codex plugin remove radarjobs@revenir` or the
plugin UI (use `@personal` for the local development copy). This anonymous
version has no provider-account authorization to revoke.

See [publication materials](docs/plugin-publication/README.md) for official
requirements, data flow, evidence, assets and distribution status. The backend
lives in the existing Revenir Radar service; this package has no duplicate engine.
