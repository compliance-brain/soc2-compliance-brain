# Access Control Policy

<!-- policy: POL-05 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how access to systems and data is requested, approved, reviewed and removed. Linked controls: AC-01A, AC-01B, AC-02, AC-03A, AC-03B, AC-04, AC-05A, AC-05B, AC-05C, AC-06, AC-07, AC-08, AC-09, AC-10A, AC-10B, AC-11, AC-12, AC-13A, AC-13B, AC-13C, AC-14, AC-15, AC-16. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Access ownership, Privileged & production access, Provider access to customer data, Customer administration, Identity and Authentication, Password Manager, Privileged Access Management). 👤 The owner answers: Who approves access for a new starter, and where is that recorded? Who has admin access to production today? When do your people look at customer data, and who allows it?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Access requests (central) (default: Approval recorded before access is granted)}}`
> - [ ] `{{Confirm: Access requests (owner-led) (default: Approval recorded before access is granted)}}`
> - [ ] `{{Confirm: Unique accounts and MFA (default: MFA enforced by system setting)}}`
> - [ ] `{{Confirm: Passwords (default: Minimum 12 characters)}}`
> - [ ] `{{Confirm: Access reviews (default: Quarterly for production and customer data systems)}}`
> - [ ] `{{Confirm: Privileged access (standing) (default: Quarterly review)}}`
> - [ ] `{{Confirm: Privileged access (temporary or just in time) (default: Expires automatically, usually within hours)}}`
> - [ ] `{{Confirm: Access to customer data (default: Exception only, approved by [role])}}`
> - [ ] `{{Confirm: Access removal (default: Within 1 business day)}}`

## Purpose

Sets out how access to systems and data is requested, approved, reviewed and removed.

## Scope

All systems in the system boundary, including production, the identity provider, workspace and code repository.

## Policy statements

### Access requests (central)

Access is requested and approved through {{identity provider or ticketing}} and granted by {{IT or platform owner}} based on role.

<sub>POL-05.01 · Controls: AC-01A · Tailor using: Access ownership, Identity and Authentication, Ticketing</sub>

### Access requests (owner-led)

Each system owner approves and grants access to their system based on role, and keeps a record of the approval.

<sub>POL-05.02 · Controls: AC-01B · Tailor using: Access ownership</sub>

### Least privilege

Access is limited to what each role needs. Admin rights are given only where the role requires them.

<sub>POL-05.03 · Controls: AC-04 · Tailor using: Access ownership</sub>

### Unique accounts and MFA

Everyone uses their own account. Multi-factor authentication is required for the identity provider, workspace, code repository, cloud consoles and any system holding customer data.

<sub>POL-05.04 · Controls: AC-07, AC-11 · Tailor using: Identity and Authentication, Workspace, Infrastructure, Code Repository</sub>

### Single sign-on

Systems sign in through {{identity provider}} where supported, and the identity provider enforces password and session rules.

<sub>POL-05.05 · Controls: AC-08, AC-09 · Tailor using: Identity and Authentication</sub>

### Passwords

Passwords are unique, stored in {{password manager}} and meet the minimum length set in the identity provider.

<sub>POL-05.06 · Controls: AC-10A, AC-10B · Tailor using: Password Manager, Identity and Authentication</sub>

### Access reviews

Access to in-scope systems is reviewed at least quarterly by {{reviewer}}, and access that is no longer needed is removed.

<sub>POL-05.07 · Controls: AC-03A, AC-03B · Tailor using: Access ownership, Headcount</sub>

### Privileged access (standing)

Standing admin and production access is limited to named people, approved by {{Technical Lead}} and reviewed at least quarterly.

<sub>POL-05.08 · Controls: AC-05A · Tailor using: Privileged & production access</sub>

### Privileged access (temporary or just in time)

Admin and production access is requested when needed, approved, time-limited and logged.

<sub>POL-05.09 · Controls: AC-05B, AC-05C, AC-06 · Tailor using: Privileged & production access, Privileged Access Management</sub>

### Root and break-glass accounts

Root and break-glass accounts are protected with MFA, stored securely and used only in emergencies, and each use is reviewed.

<sub>POL-05.10 · Controls: AC-12 · Tailor using: Infrastructure</sub>

### Access to customer data

Staff access customer data only to support a customer or resolve an incident, with approval where required, and the access is logged.

<sub>POL-05.11 · Controls: AC-13A, AC-13B, AC-13C · Tailor using: Provider access to customer data</sub>

### Administration for customers

Where staff administer customer accounts, they act only on a customer's documented request.

<sub>POL-05.12 · Controls: AC-14 · Tailor using: Customer administration</sub>

### Service accounts and API keys

Service accounts and API keys have a named owner and minimum permissions, and are rotated when people with access to them leave.

<sub>POL-05.13 · Controls: AC-15 · Tailor using: Application Secrets and Encryption</sub>

### Segregation of duties

No single person can both make and approve a high-risk change, payment or access grant.

<sub>POL-05.14 · Controls: AC-16 · Tailor using: Headcount</sub>

### Access removal

Access is removed when it is no longer needed, and within {{timeframe}} of someone leaving.

<sub>POL-05.15 · Controls: AC-02 · Tailor using: HR System, Identity and Authentication</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
