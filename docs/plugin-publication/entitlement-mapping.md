# RadarJobs entitlement mapping

The plugin exposes product states, not Stripe identifiers, prices, or internal
billing records.

| Real backend condition | Plugin state | Search | Workspaces | Recommendations | Detail |
|---|---|---|---|---|---|
| New connection, no profile/preferences, or onboarding incomplete | `onboarding` | one bounded preview, then setup required | create/list/update available; one run can use the preview | setup-required response | unavailable |
| Onboarding complete without current paid-equivalent access, including a pending/free account | `exploration` | one bounded preview if unused | create/list/update available; run follows search access | existing top-five personalized preview | only jobs in that account's visible preview |
| Active fixed access pass or complimentary paid-equivalent window | `active` | available | available | existing personalized set | current eligible inventory |
| Active paid membership | `active` | available | available | existing personalized set | current eligible inventory |
| Trialing before `trial_ends_at` | `active` | available | available | existing personalized set | current eligible inventory |
| Canceling before `current_period_end` | `active` | available | available | existing personalized set | current eligible inventory |
| Expired access/trial or canceled period after its end, with completed onboarding | `exploration` | one bounded preview if unused | create/list/update available; run follows search access | existing top-five personalized preview | only jobs in that preview |
| Previously activated but onboarding is not complete | `expired` | one bounded preview, then setup required | create/list/update available; one run can use the preview | setup-required response | unavailable |
| Disabled/deleted Radar account or revoked/expired OAuth token | authentication failure | unavailable | unavailable | unavailable | unavailable |

An empty recommendation set returns an explicit no-current-recommendations state; it does not start generation. The first successful search or workspace run consumes the single setup-free preview. Later unavailable searches return a setup or account link. The plugin never displays plans, prices, checkout, or an upgrade action.
