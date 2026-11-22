# Information Security Policy

<!-- policy: POL-01 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: yes -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Roles (POL-01.01): Name roles in the policy, not individuals}}`
> - [ ] `{{Confirm: Policy management (POL-01.02): Annual review}}`
> - [ ] `{{Confirm: Oversight (management) (POL-01.04): Every six months, in an existing leadership meeting}}`
> - [ ] `{{Confirm: Organisational structure (POL-01.05): Updated as changes happen}}`
> - [ ] `{{Confirm: Automated and agent-run controls (POL-01.08): Owner checks at least quarterly}}`
> - [ ] `{{Confirm: Reporting security concerns (POL-01.09): A security@ address or trust page form}}`
> - [ ] `{{Confirm: Control review (POL-01.10): Annually}}`

## Purpose

Sets out how the company protects the information it holds and the service it provides, who is responsible, and how the policy set is managed.

## Scope

All staff, contractors and systems in the system boundary.

## Policy statements

### Roles

{{Compliance Owner: CTO}} is accountable for the information security program. {{Technical Lead: CTO}} owns technical controls and {{Governance Lead: CEO}} owns governance and business risk.

<sub>POL-01.01 · Controls: GV-01, GV-03 · Tailor using: Team Details: Compliance Owner, Technical Lead, Governance Lead</sub>

### Policy management

Policies are approved by management, published where all staff can read them, and reviewed at least annually or after a significant change.

<sub>POL-01.02 · Controls: GV-01 · Tailor using: Program home, Knowledge Management</sub>

### Oversight (management)

Leadership reviews the security program at least every six months in an existing meeting and records decisions and actions.

<sub>POL-01.04 · Controls: GV-02B · Tailor using: Governance, Operating Cadence</sub>

### Organisational structure

The company keeps an organisational chart showing reporting lines and updates it when the structure changes.

<sub>POL-01.05 · Controls: GV-03 · Tailor using: HR System, Headcount</sub>

### Automated and agent-run controls

Each control performed by automation or an AI agent has a named person who owns it, reviews its exceptions and checks it is still working.

<sub>POL-01.08 · Controls: GV-13 · Tailor using: Control execution, Compliance Automation, AI Models and Platforms</sub>

### Reporting security concerns

Staff, customers and researchers can report security issues through a published channel, and reports are triaged promptly.

<sub>POL-01.09 · Controls: CO-01 · Tailor using: Domain (security or trust page)</sub>

### Control review

The control framework is reviewed at least annually and when systems, risks or commitments change.

<sub>POL-01.10 · Controls: RM-04 · Tailor using: Controls tab, Planned Changes</sub>

## Add if your setup differs

<details>
<summary>3 more library statements, and when each applies</summary>

- **Oversight (committee)** (POL-01.03; controls GV-02A). *Applies when:* All stages, when Governance is Formal committees.  
  A security committee meets at least quarterly under a written charter and records its decisions and actions.
- **Security lead** (POL-01.06; controls GV-07). *Applies when:* Scaleup and Enterprise. Always included.  
  A named security lead coordinates the program day to day and reports to management.
- **Exceptions** (POL-01.07; controls GV-09). *Applies when:* Enterprise only. Always included.  
  Exceptions to policy are requested in writing, approved by the policy owner, time-limited and recorded.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who signs off policies? Which leadership meeting already happens where security could be a standing item? Who do staff go to with a security question?

Profile fields to draw on: Team Details, Governance, Operating Cadence, Company Stage, Framework Scope, Control execution.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
