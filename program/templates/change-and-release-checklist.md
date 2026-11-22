# Change and release checklist

> [!NOTE]
> **🧭 Guide.** Controls CM-02A, CM-03B, CM-04A, CM-05, CM-06A, CM-08A, CM-09, CM-12 and AI-13. For the reference company these are *configured once* in `{{code repository: GitHub}}` and `{{CI/CD: GitHub Actions}}`, so the evidence is the settings plus a sample of pull requests, not a form for every change. Screenshot the settings once in the audit period (AI Guidance 4.6).

## Set up once (and screenshot)

- [ ] Main branch protected: no direct pushes, pull request required (CM-02A)
- [ ] At least one approving review required, and not by the author (CM-03B, AI-13 for AI-written code)
- [ ] Required checks must pass before merge: tests, `{{code scanner: GitHub Dependabot}}` and other security checks (CM-04A, CM-09)
- [ ] Only `{{deployers: engineers in the deploy team}}` can deploy to production, through the pipeline (CM-06A)
- [ ] Separate development, staging and production environments and credentials (CM-05)
- [ ] Infrastructure changes go through `{{infrastructure as code: Terraform}}` in pull requests (CM-08A)
- [ ] Changes link to a `{{ticketing: Linear}}` issue (CM-12)

## Each change (built into the pull request)

- [ ] Linked issue explains the change
- [ ] Reviewed and approved by someone other than the author
- [ ] Checks passed
- [ ] Deployed through the pipeline; rollback known

## Emergency changes

If a fix can't wait for review, deploy it, then get a review within `{{timeframe: 1 business day}}` and note why in the issue.
