# Incident Response Policy

<!-- policy: POL-12 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how security incidents are reported, handled, communicated and learned from. Linked controls: IR-01, IR-02A, IR-02B, IR-02C, IR-03, IR-04, IR-05, CO-01, PR-07. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Incident response, Service Commitments, Regulatory Drivers, Country/Region(s), Customer Geography, Status Page). 👤 The owner answers: If you had a security incident tonight, who would lead it? Who decides whether to tell customers? How quickly have you promised to notify customers of a breach?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Reporting (default: Report immediately)}}`
> - [ ] `{{Confirm: Severity and escalation (default: Three or four severity levels)}}`
> - [ ] `{{Confirm: Customer and regulator notice (default: Check contracts and each region's breach notification law)}}`
> - [ ] `{{Confirm: Testing the plan (default: Annually)}}`

## Purpose

Sets out how security incidents are reported, handled, communicated and learned from.

## Scope

Security and availability incidents affecting the in-scope system, company data or customer data.

## Policy statements

### Reporting

Anyone who suspects an incident reports it straight away through {{channel}}.

<sub>POL-12.01 · Controls: IR-01, CO-01 · Tailor using: Incident response</sub>

### Roles (security-led)

The security team leads incidents, with engineering, leadership and communications roles defined.

<sub>POL-12.02 · Controls: IR-02A · Tailor using: Incident response</sub>

### Roles (coordinated)

A named incident lead coordinates the response and brings in engineering, leadership and communications as needed.

<sub>POL-12.03 · Controls: IR-02B · Tailor using: Incident response</sub>

### Roles (engineering-led)

The on-call engineer leads incidents and escalates to {{Technical Lead}} and leadership by severity.

<sub>POL-12.04 · Controls: IR-02C · Tailor using: Incident response</sub>

### Severity and escalation

Incidents are classified by severity, which sets response times and who is told.

<sub>POL-12.05 · Controls: IR-03 · Tailor using: Incident response</sub>

### Customer and regulator notice

Affected customers and regulators are notified within the timeframes in contracts and law.

<sub>POL-12.06 · Controls: IR-03, PR-07 · Tailor using: Service Commitments, Regulatory Drivers, Country/Region(s)</sub>

### Incident records

Each incident is recorded with its timeline, impact, actions and outcome.

<sub>POL-12.07 · Controls: IR-03 · Tailor using: Ticketing</sub>

### Testing the plan

The response plan is tested at least annually through a tabletop exercise or a review of a real incident.

<sub>POL-12.08 · Controls: IR-04 · Tailor using: Incident response</sub>

### Post-incident review

Significant incidents get a review that identifies the root cause and actions, tracked to completion.

<sub>POL-12.09 · Controls: IR-05 · Tailor using: Ticketing</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
