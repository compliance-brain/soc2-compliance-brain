# Your program

Everything in this folder belongs to your company. It starts as a complete first draft for a **reference company**: a simple, fully remote 10-person B2B SaaS on AWS, with Google Workspace sign-in, code on GitHub and company-managed laptops, going for SOC 2 Security. You can read it end to end and see what a lean program looks like.

The reference company's answers are written as variables like `{{identity provider: Google Workspace}}`: the label says what it is, and the value is the reference company's answer. Your agent replaces each one from your profile. Where your context differs, [what-else-to-add.md](what-else-to-add.md) and each policy's **Add if your setup differs** section say what to add or swap, drawn from the full library in [brain/](../brain/).

Work through it in this order with your AI agent.

1. **[Your context](context/).** Link the documents you already have in `context-sources.csv`, then let your agent draft `profile.yaml` from them. Answer what you know; TBC is fine. A person reviews the profile and logs the review in the audit trail.
2. **[Your controls](controls/).** Run `python3 tools/scope.py`, then build `control-list.csv` from `scope.md`. It's what you'll be audited on, your to-do list and your dashboard.
3. **[Policies](policies/).** Keep only the policies and statements in scope, draft them from the profile, and work through each Confirm box.
4. **[Registers](registers/).** 10 to 20 high-level risks; the vendors that deliver your service or hold your data; your people.
5. **Approve.** Policies go to the approver as a pull request. Record each decision in `records/sign-off-log.csv`, then have staff acknowledge in `records/policy-acknowledgements.csv`.
6. **Run it.** Schedule recurring controls in `records/activity-log.csv`, use the [templates](templates/), follow the [plans](plans/) and keep [evidence](evidence/) lean.
7. **Keep the audit trail from day one.** Log each meaningful change in `records/audit-trail.csv`, whether a person or an AI made it, with a reviewer for AI work. Revisit your context every quarter and whenever the business changes.

## How approvals work

1. **Policies:** resolve the Confirm box, open a pull request, and have the approver review and merge it. Then add a Policy approval row to the sign-off log and set `status: Approved`, `approved-by` and `approved-on` in the policy's header comment. Review every 12 months.
2. **Open items at approval:** list any Confirm items still open in the sign-off row's "Open Confirm items accepted" column, so the decision is visible.
3. **Acknowledgements:** staff acknowledge policies when they join, every year and after a material change.
4. **Registers:** add a Risk register review or Vendor register review row to the sign-off log at least annually, plus a Risk acceptance or Vendor approval row for each individual decision.
5. **One rule for every record:** don't edit past audit trail or sign-off rows. If one is wrong, add a correcting row that refers to the original.

## Working in another tool

If your program lives in Notion, Google Workspace, Microsoft 365, monday.com or a compliance platform, keep `context/`, the audit trail and the library here, and build the records in that tool. Record what lives where in `profile.yaml`.
