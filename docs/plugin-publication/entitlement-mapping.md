# RadarJobs entitlement mapping

The plugin exposes product states, not Stripe identifiers, prices, or internal
billing records.

| Real backend condition | Plugin state | Search | Recommendations | Detail |
|---|---|---|---|---|
| New connection, no profile/preferences, or onboarding incomplete | `onboarding` | unavailable | setup-required response | unavailable |
| Onboarding complete without current paid-equivalent access, including a pending/free account | `exploration` | unavailable | existing top-five personalized preview | only jobs in that account's visible preview |
| Active fixed access pass or complimentary paid-equivalent window | `active` | available | existing personalized set | current eligible inventory |
| Active paid membership | `active` | available | existing personalized set | current eligible inventory |
| Trialing before `trial_ends_at` | `active` | available | existing personalized set | current eligible inventory |
| Canceling before `current_period_end` | `active` | available | existing personalized set | current eligible inventory |
| Expired access/trial or canceled period after its end, with completed onboarding | `exploration` | unavailable | existing top-five personalized preview | only jobs in that preview |
| Previously activated but onboarding is not complete | `expired` | unavailable | setup-required response | unavailable |
| Disabled/deleted Radar account or revoked/expired OAuth token | authentication failure | unavailable | unavailable | unavailable |

An empty recommendation set returns an explicit no-current-recommendations state;
it does not start generation. An unavailable search returns neutral account
information and the attributed RadarJobs account page. The plugin never displays
plans, prices, checkout, or an upgrade action.
