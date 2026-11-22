# Registers

> [!NOTE]
> **🧭 Guide.** Size the registers to your stage (AI Guidance 10.1). Early-stage companies need 10 to 20 high-level risks a founder can review in one sitting, and only the vendors that deliver the service or hold data. Anything a law or contract requires is there from day one, such as a business associate agreement column once HIPAA applies (10.2).

## Risk register: [risk-register.csv](risk-register.csv)

Start from the in-scope risks in [scope.md](../controls/scope.md) and the blueprints in [risks.csv](../../brain/library/risks.csv), rewritten for your company.

| Column | What to put |
| --- | --- |
| ID | The library ID (R-07) or your own (R-101) |
| Risk | What could go wrong, in a sentence |
| Owner | The role accountable for it |
| Likelihood, Impact | 1 to 5, using the scales in [brain/library/README.md](../../brain/library/README.md#risk-rating) |
| Rating | Likelihood × Impact. Medium from 5, High from 10, Critical from 20 |
| Treatment | `Reduce`, `Accept`, `Transfer` or `Avoid` |
| Linked controls | The control IDs that treat it |
| Last reviewed | Date of the last review |
| Notes | Treatment plan, or who accepted it and when (also log acceptances in the sign-off log) |

Add residual scoring and acceptance columns when you grow, or when an auditor or customer asks (10.3).

## Vendor register: [vendor-register.csv](vendor-register.csv)

The tier sets the checks: see [vendor-tiers.csv](../../brain/library/vendor-tiers.csv). Find vendors with [vendor-categories.csv](../../brain/library/vendor-categories.csv) and your tool and billing list.

| Column | What to put |
| --- | --- |
| Vendor | Name |
| What they provide | One line |
| Data held | The most sensitive data they hold or can reach |
| Tier | `Tier 1 – Critical`, `Tier 2 – High` or `Tier 3 – Low` |
| Assurance | SOC 2 or ISO 27001 report (and when reviewed), questionnaire, or none |
| Contract and DPA | What's in place |
| Owner | Who manages the relationship |
| Last review, Next review | 12 months for Tiers 1 and 2; 24 months for Tier 3 |
| Notes | Subservice organisation? Controls they expect you to run? |

## People: [people.csv](people.csv)

One row per employee or contractor with access, so onboarding, training, acknowledgements and leaving are evidenced in one place. Record names and roles only, no other personal details. Type is `Employee`, `Contractor` or `Founder`; Status is `Active`, `Leaving` or `Left`. Founders may hold admin access by role and don't need performance reviews (AI Guidance 4.1).
