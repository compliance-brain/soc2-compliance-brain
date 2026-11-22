# People Security Policy

<!-- policy: POL-04 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Covers security across the employee lifecycle: hiring, onboarding, training, role changes and leaving. Linked controls: HR-01, HR-02, HR-03, HR-04, HR-05, HR-06, HR-07, AC-02, AC-17. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Headcount, HR System, Workforce model, Country/Region(s), Identity and Authentication, Device Management, Password Manager). 👤 The owner answers: Who runs onboarding, and what's on the checklist? When someone leaves, who tells IT and how quickly is access removed? Do contractors go through the same steps? How is security training done today?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Background checks (default: Reference and right-to-work checks as a minimum)}}`
> - [ ] `{{Confirm: Confidentiality (default: Before first access)}}`
> - [ ] `{{Confirm: Onboarding (default: Checklist completed in the first week)}}`
> - [ ] `{{Confirm: Security training (default: Within 30 days of starting, then annually)}}`
> - [ ] `{{Confirm: Secure development training (default: Annually)}}`
> - [ ] `{{Confirm: Phishing simulations (default: At least twice a year)}}`
> - [ ] `{{Confirm: Roles and performance (default: Annually)}}`
> - [ ] `{{Confirm: Role changes (default: Within 5 business days of the change)}}`
> - [ ] `{{Confirm: Offboarding (default: Accounts disabled within 1 business day of the last day)}}`

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

### Secure development training

Engineers complete secure development training at least annually.

<sub>POL-04.05 · Controls: HR-05 · Tailor using: Code Repository</sub>

### Phishing simulations

The company runs phishing simulations and follows up with staff who need more training.

<sub>POL-04.06 · Controls: HR-06 · Tailor using: Workspace</sub>

### Roles and performance

Staff have documented roles and regular performance reviews that cover security responsibilities where relevant.

<sub>POL-04.07 · Controls: HR-04, HR-07 · Tailor using: HR System</sub>

### Role changes

When someone changes role, their access is updated to match the new role and access they no longer need is removed.

<sub>POL-04.08 · Controls: AC-02 · Tailor using: Access ownership</sub>

### Offboarding

When someone leaves, their accounts are disabled, company devices are returned or wiped, and shared credentials they knew are changed.

<sub>POL-04.09 · Controls: AC-02, AC-17 · Tailor using: HR System, Identity and Authentication, Device Management, Password Manager</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
