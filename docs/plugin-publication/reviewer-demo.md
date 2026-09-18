# RadarJobs reviewer demo video

## Recording requirement

Record this only after the authenticated backend and support page are deployed.
Use a dedicated reviewer account with representative recommendations and active
paid-equivalent access. The account must not require MFA, email confirmation, or
SMS during review. Never show its password, browser password manager, access
tokens, developer console, production logs, or another customer's data.

Target length: 2.5 to 4 minutes. Record at 1080p with readable text and one
continuous flow where practical.

## Shot list and narration

1. **Listing and connection (30–45 seconds).** Start from the RadarJobs plugin
   listing in ChatGPT. State: “RadarJobs connects to an existing RadarJobs
   account. It does not sell access or submit job applications in ChatGPT.”
   Select Connect.
2. **Authorization (30–45 seconds).** Show the Revenir-hosted connection page,
   its disclosed data categories, and the signed-in reviewer identity without
   revealing credentials. Approve the connection and return to ChatGPT.
3. **Search (45–60 seconds).** Prompt: “Use RadarJobs to find 5 current remote
   data engineering contract jobs in the United States. I’m looking for 1099 work
   paying at least $50/hour.” Show one direct `search_contract_jobs` invocation,
   presentation-ready results, and both links. Do not show a readiness or taxonomy
   preflight because neither exists in the current contract.
4. **Personalization (30 seconds).** Prompt: “Show my complete current RadarJobs
   recommendations.” Show existing recommendations from
   `get_my_radarjobs_recommendations`; explain that the plugin reads the
   already-generated set.
5. **Detail (20–30 seconds).** Ask: “Show me more about the first result.” Show
   the single selected `get_contract_job` result, actual source-posting link, and
   RadarJobs detail link.
6. **Boundary (20–30 seconds).** Prompt: “Apply to the first job and buy me a
   subscription if needed.” Show that RadarJobs does neither action and does not
   trigger a purchase/application tool.
7. **Disconnect/support (20–30 seconds).** Show the ChatGPT connected-app
   disconnect control, then briefly open https://www.revenirdata.com/support.

## Final video QA

- The plugin name is RadarJobs throughout.
- Every shown result comes from the deployed production MCP.
- OAuth consent, successful return, tool invocation, and output are legible.
- No password, token, email inbox, payment detail, internal URL, or customer PII
  appears.
- No checkout, pricing pitch, application claim, or unsupported capability
  appears.
- Audio is clear, cursor movement is deliberate, and no notifications appear.
- The uploaded file/link is accessible to OpenAI reviewers without requesting
  access.
