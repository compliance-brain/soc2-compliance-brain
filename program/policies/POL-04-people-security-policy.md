# People Security Policy

<!-- policy: POL-04 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Background checks (POL-04.01): Reference and right-to-work checks as a minimum}}`
> - [ ] `{{Confirm: Confidentiality (POL-04.02): Before first access}}`
> - [ ] `{{Confirm: Onboarding (POL-04.03): Checklist completed in the first week}}`
> - [ ] `{{Confirm: Security training (POL-04.04): Within 30 days of starting, then annually}}`
> - [ ] `{{Confirm: Roles and performance (POL-04.07): Annually}}`
> - [ ] `{{Confirm: Role changes (POL-04.08): Within 5 business days of the change}}`
> - [ ] `{{Confirm: Offboarding (POL-04.09): Accounts disabled within 1 business day of the last day}}`

## Purpose

Covers security across the employee lifecycle: hiring, onboarding, training, role changes and leaving.

## Scope

Employees and contractors with access to company systems or data.

## Policy statements

### Background checks

New hires in roles with access to customer data or production systems are background checked before they start, where local law allows.

<sub>POL-04.01 · Controls: HR-01 · Tailor using: Country/Region(s), Workforce model</sub>

### Confidentiality

Employees and contractors sign confidentiality terms before they get access to company systems or data.

<sub>POL-04.02 · Controls: HR-03 · Tailor using: Employment and contractor agreement templates</sub>

### Onboarding

New starters follow an onboarding checklist covering accounts, device set-up, policy acknowledgement and security training.

<sub>POL-04.03 · Controls: HR-02, AC-17 · Tailor using: HR System, Identity and Authentication, Device Management</sub>

### Security training

Staff complete security awareness training when they join and at least annually.

<sub>POL-04.04 · Controls: HR-02 · Tailor using: Headcount, training tool</sub>

### Roles and performance

Staff have documented roles and regular performance reviews that cover security responsibilities where relevant.

<sub>POL-04.07 · Controls: HR-04 · Tailor using: HR System</sub>

### Role changes

When someone changes role, their access is updated to match the new role and access they no longer need is removed.

<sub>POL-04.08 · Controls: AC-02 · Tailor using: Access ownership</sub>

### Offboarding

When someone leaves, their accounts are disabled, company devices are returned or wiped, and shared credentials they knew are changed.

<sub>POL-04.09 · Controls: AC-02, AC-17 · Tailor using: HR System, Identity and Authentication, Device Management, Password Manager</sub>

## Add if your setup differs

<details>
<summary>2 more library statements, and when each applies</summary>

- **Secure development training** (POL-04.05; controls HR-05). *Applies when:* Scaleup and Enterprise, when a Code Repository tool is named.  
  Engineers complete secure development training at least annually.
- **Phishing simulations** (POL-04.06; controls HR-06). *Applies when:* Scaleup and Enterprise. Always included.  
  The company runs phishing simulations and follows up with staff who need more training.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who runs onboarding, and what's on the checklist? When someone leaves, who tells IT and how quickly is access removed? Do contractors go through the same steps? How is security training done today?

Profile fields to draw on: Headcount, HR System, Workforce model, Country/Region(s), Identity and Authentication, Device Management, Password Manager.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
