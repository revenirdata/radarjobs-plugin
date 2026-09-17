# OpenAI reviewer account plan

Do not create this account until the owner approves production test state.

## Proposed setup

- Create one dedicated production RadarJobs account classified as a test account.
- Use a Revenir-controlled reviewer email that is not a personal customer
  identity. Store its password only in the OpenAI submission portal and the
  approved Revenir secret manager; never commit it.
- Require no MFA, email confirmation, SMS confirmation, private network, or
  Google-only login.
- Complete a synthetic contract-tech profile and preferences with no real
  person's resume, contact details, or employment history.
- Generate one normal recommendation set through the existing reviewed product
  workflow.
- Grant a clearly recorded temporary complimentary paid-equivalent access window
  through the existing operator control, with a stated expiry after the expected
  review period. Do not create a Stripe customer, subscription, card, invoice, or
  automatic renewal.
- Verify the account can execute all five submitted positive tests and the
  Developer Mode demo without exposing another user's data.

## Cleanup and monitoring

Record the account ID, creation time, access reason, access expiry, reviewer
purpose, and responsible operator in the existing audit surface. After review,
revoke the OAuth grant, rotate/remove the portal password, and either extend the
documented review window with approval or delete/reset the synthetic account
through the existing test-account workflow.

This reviewer account is separate from the 30-day early-adopter program and does
not establish a plugin-wide complimentary-access policy.
