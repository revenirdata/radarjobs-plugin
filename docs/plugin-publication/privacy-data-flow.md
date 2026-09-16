# Privacy, data flow and safety

1. User asks Codex for contract technology opportunities. OpenAI processes the
   conversation under its own terms and account/workspace settings.
2. Codex resolves language into minimal structured filters. The skill excludes
   resumes, personal contacts, complete conversations and private project data.
3. HTTPS MCP sends those filters or a selected public opportunity UUID to the
   existing Revenir Radar backend. No key, OAuth grant, account, card or cookie is
   required for this anonymous surface.
4. The backend admits the request under shared limits and queries already-stored
   opportunity data. No crawling, discovery, ingestion or model inference starts.
5. A strict allowlist returns public facts, bounded evidence and fixed-origin
   Revenir links. Employer/intermediary/source identities remain distinct. Unknown
   pay and engagement remain unknown; liveness is checked under the public policy.
6. Operational records use the existing anonymous usage table: a salted network
   hash, time, endpoint/tool, filter names (not values), response status, success,
   result count and latency. Raw filter values and prompts are not stored by this
   telemetry. Existing infrastructure/security logging still applies. No new fixed
   retention/deletion schedule is promised.
7. A clicked link carries `utm_source=openai&utm_medium=plugin&utm_campaign=radarjobs_codex`.
   The existing website first/latest-touch attribution supports landing and signup
   attribution. Browser events may be blocked; metrics are not guaranteed counts.

No user profile or authenticated account data is exposed. Public job data may
itself contain organization/location/source text. All source strings are untrusted
data, not executable instructions. Markup/control characters are stripped and
text is bounded, but instruction isolation is also enforced by the plugin skill
and server instructions; sanitization is not claimed to solve prompt injection.

Tools have no ability to read local files, run shell commands, change subscriptions,
apply for jobs or initiate email. They return no arbitrary application URLs.
Current OpenAI annotations conservatively mark logging as a write side effect;
business behavior is read-only, non-destructive and limited to existing inventory.

## Abuse boundary

At most five results. Broad searches without a role/title inspect only the 2,000 most recently discovered technology opportunities and disclose that scope. No cursor or offset, no before-date enumeration, 8 KiB body
limit, no JSON-RPC batches, 4-second SQL statement timeout, pre-query shared
PostgreSQL advisory-lock admission, 30 tool calls/hour and 75/day per network.
Protocol requests are limited to 120/hour and 300/day per network, with global
120/minute and 10,000/day ceilings. IPv6 networks are grouped by /64. Caddy
overwrites the client identity header; arbitrary X-Forwarded-For cannot rotate it.
Unavailable metering fails closed. Distributed abuse is bounded by the global
budget; no claim of perfect prevention is made.

The current acquisition surface still has a cumulative-enumeration limitation:
repeated, varied targeted searches can expose more unique public jobs over time
than one broad recent-2,000 preview, even though each response, network window and
global budget is bounded. This release intentionally keeps that public policy.
Unique-job exposure caps, a recent-2,000 restriction for targeted searches,
detail-to-search binding, and additional public HTML or sitemap restrictions are
separate product-policy work and are not represented as implemented here.

## Phase 2

Personalization would require a separately reviewed standards-compliant provider
OAuth integration with scoped account authorization, PKCE and revocation, using
the current OpenAI MCP/app requirements and Radar's account service. Existing web
sessions are not repurposed into unsafe plugin tokens. No such flow is implemented
or required for this release.
