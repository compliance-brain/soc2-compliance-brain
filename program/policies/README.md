# Policies

> [!NOTE]
> **🧭 Guide.** Fifteen policies, one per policy in the library, drafted for the reference company: 14 are in scope for it, with 87 statements written out, and the Privacy Policy (internal) is marked not in scope. Each policy also lists its other library statements, and when each applies, under **Add if your setup differs**. Your agent swaps the `{{label: example}}` values for yours, adds or removes statements to match your [scope](../controls/scope.md), and retires any policy you don't need. Under 100 people, keep each statement to one short paragraph (AI Guidance 4.2 and 6.2).

## Before you build

Settle three choices with your agent and record them in the audit trail (6.1):

- **Depth:** Light (the in-scope statements, one paragraph each) or Detailed (the fuller document set in [policy-documents.csv](../../brain/library/policy-documents.csv)).
- **Alignment:** Defaults (role names and library defaults, confirmed in a line each) or Tailored (every setting checked against the system that enforces it).
- **Format:** Markdown here, or documents in your program home.

With no preference, build Light with Defaults here, and step up later where an auditor will test the detail.

## Each policy file

- A header comment holding the policy ID, status (`Draft`, `Ready for approval`, `Needs update`, `Approved` or `Retired`), version, owner, approver, approval date, and whether staff must acknowledge it.
- 🧭 Guide, ✏️ Adapt and ✅ Confirm boxes. Delete Guide and Adapt once adapted; keep Confirm items until they're resolved or accepted at sign-off.
- Statements with `{{placeholders}}`, each followed by its reference, linked controls and the profile fields to tailor it from.

## Approval

1. Resolve the Confirm items, set the status to `Ready for approval` and open a pull request.
2. The approver reviews and merges it. Management approves; the agent never does (6.8).
3. Add a Policy approval row to [sign-off-log.csv](../records/sign-off-log.csv), listing any Confirm items accepted while still open.
4. Set the status to `Approved` and fill in `approved-by` and `approved-on`. Review in 12 months, or sooner if something material changes.
5. For policies staff must acknowledge, record acknowledgements in [policy-acknowledgements.csv](../records/policy-acknowledgements.csv).

A finished policy has no placeholders, `undefined` or TBC left, names other policies by their exact title and only if in scope, and links every in-scope control it covers (6.8).
