# Incident Response Policy

<!-- policy: POL-12 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Reporting (POL-12.01): Report immediately}}`
> - [ ] `{{Confirm: Severity and escalation (POL-12.05): Three or four severity levels}}`
> - [ ] `{{Confirm: Customer and regulator notice (POL-12.06): Check contracts and each region's breach notification law}}`
> - [ ] `{{Confirm: Testing the plan (POL-12.08): Annually}}`

## Purpose

Sets out how security incidents are reported, handled, communicated and learned from.

## Scope

Security and availability incidents affecting the in-scope system, company data or customer data.

## Policy statements

### Reporting

Anyone who suspects an incident reports it straight away through {{incident channel: #incidents in Slack}}.

<sub>POL-12.01 · Controls: IR-01, CO-01 · Tailor using: Incident response</sub>

### Roles (coordinated)

A named incident lead coordinates the response and brings in engineering, leadership and communications as needed.

<sub>POL-12.03 · Controls: IR-02B · Tailor using: Incident response</sub>

### Severity and escalation

Incidents are classified by severity, which sets response times and who is told.

<sub>POL-12.05 · Controls: IR-03 · Tailor using: Incident response</sub>

### Customer and regulator notice

Affected customers and regulators are notified within the timeframes in contracts and law.

<sub>POL-12.06 · Controls: IR-03 · Tailor using: Service Commitments, Regulatory Drivers, Country/Region(s)</sub>

### Incident records

Each incident is recorded with its timeline, impact, actions and outcome.

<sub>POL-12.07 · Controls: IR-03 · Tailor using: Ticketing</sub>

### Testing the plan

The response plan is tested at least annually through a tabletop exercise or a review of a real incident.

<sub>POL-12.08 · Controls: IR-04 · Tailor using: Incident response</sub>

## Add if your setup differs

<details>
<summary>3 more library statements, and when each applies</summary>

- **Roles (security-led)** (POL-12.02; controls IR-02A). *Applies when:* All stages, when Incident response is Security-led.  
  The security team leads incidents, with engineering, leadership and communications roles defined.
- **Roles (engineering-led)** (POL-12.04; controls IR-02C). *Applies when:* All stages, when Incident response is Engineering-led.  
  The on-call engineer leads incidents and escalates to {{Technical Lead: CTO}} and leadership by severity.
- **Post-incident review** (POL-12.09; controls IR-05). *Applies when:* Scaleup and Enterprise. Always included.  
  Significant incidents get a review that identifies the root cause and actions, tracked to completion.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: If you had a security incident tonight, who would lead it? Who decides whether to tell customers? How quickly have you promised to notify customers of a breach?

Profile fields to draw on: Incident response, Service Commitments, Regulatory Drivers, Country/Region(s), Customer Geography, Status Page.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
