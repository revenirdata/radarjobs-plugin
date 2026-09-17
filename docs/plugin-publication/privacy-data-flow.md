# Privacy, authentication, and data flow

1. ChatGPT discovers the RadarJobs protected-resource and authorization-server
   metadata and registers a public OAuth client.
2. The user signs in to or creates their existing RadarJobs account on Revenir's
   website, reviews the disclosed data categories, and approves or denies the
   connection.
3. Authorization uses an authorization code bound to the exact client, redirect
   URI, resource, scopes, and S256 PKCE challenge. Codes are single-use.
4. RadarJobs issues short-lived opaque access tokens and rotating opaque refresh
   tokens. Only token hashes are stored. Refresh-token replay revokes the grant's
   token family. The revocation endpoint disconnects the grant.
5. The MCP server derives the Radar account solely from the verified token
   subject. No tool accepts an account ID, password, API key, card detail, resume,
   or OAuth token as model-supplied input.
6. Tools read the connected account's setup/access state, current contract-job
   inventory, existing recommendation set, eligible job detail, or taxonomy.
   They never start checkout, modify billing, submit applications, send messages,
   crawl providers, or launch paid inference.
7. Every tool call records bounded account telemetry in the existing Radar
   request-event store. Because this changes operational state, all tools are
   conservatively annotated `readOnlyHint: false`; business behavior remains
   non-destructive.
8. Deleting RadarJobs from a shared Revenir account deletes its OAuth grants and
   cascades authorization codes and tokens while preserving unrelated Radar API
   state. Full account deletion also cascades those records.

## Data returned to ChatGPT

- account access state and setup readiness;
- requested job results and eligible job detail;
- existing personalized recommendation results;
- public taxonomy identifiers;
- fixed-origin RadarJobs and account links.

No payment-card data, password, API key, raw resume text, complete profile,
internal score, source application URL, or unrestricted provider metadata is
returned.

## Scope and isolation

The only requested scope is `radarjobs:read`. The account is bound at approval,
and tools have no account selector. Search requires existing access. Exploration
detail is restricted to the connected account's visible recommendation preview.
All returned job/source strings remain untrusted data and never become executable
instructions.

## Disconnect and deletion

Users can disconnect RadarJobs from ChatGPT's connected-app settings. OAuth token
revocation invalidates the RadarJobs grant. Users can also delete RadarJobs
through the existing RadarJobs account controls; the backend deletes associated
grants and tokens. Support is available at
https://www.revenirdata.com/support.
