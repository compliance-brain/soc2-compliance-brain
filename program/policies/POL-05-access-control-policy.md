# Access Control Policy

<!-- policy: POL-05 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Access requests (central) (POL-05.01): Approval recorded before access is granted}}`
> - [ ] `{{Confirm: Unique accounts and MFA (POL-05.04): MFA enforced by system setting}}`
> - [ ] `{{Confirm: Passwords (POL-05.06): Minimum 12 characters}}`
> - [ ] `{{Confirm: Access reviews (POL-05.07): Quarterly for production and customer data systems}}`
> - [ ] `{{Confirm: Privileged access (standing) (POL-05.08): Quarterly review}}`
> - [ ] `{{Confirm: Access to customer data (POL-05.11): Exception only, approved by CTO}}`
> - [ ] `{{Confirm: Access removal (POL-05.15): Within 1 business day}}`

## Purpose

Sets out how access to systems and data is requested, approved, reviewed and removed.

## Scope

All systems in the system boundary, including production, the identity provider, workspace and code repository.

## Policy statements

### Access requests (central)

Access is requested and approved through {{request channel: a Linear access request}} and granted by {{access approver: CTO}} based on role.

<sub>POL-05.01 · Controls: AC-01A · Tailor using: Access ownership, Identity and Authentication, Ticketing</sub>

### Least privilege

Access is limited to what each role needs. Admin rights are given only where the role requires them.

<sub>POL-05.03 · Controls: AC-04 · Tailor using: Access ownership</sub>

### Unique accounts and MFA

Everyone uses their own account. Multi-factor authentication is required for the identity provider, workspace, code repository, cloud consoles and any system holding customer data.

<sub>POL-05.04 · Controls: AC-07, AC-11 · Tailor using: Identity and Authentication, Workspace, Infrastructure, Code Repository</sub>

### Single sign-on

Systems sign in through {{identity provider: Google Workspace}} where supported, and the identity provider enforces password and session rules.

<sub>POL-05.05 · Controls: AC-08, AC-09 · Tailor using: Identity and Authentication</sub>

### Passwords

Passwords are unique, stored in {{password manager: 1Password}} and meet the minimum length set in the identity provider.

<sub>POL-05.06 · Controls: AC-10A · Tailor using: Password Manager, Identity and Authentication</sub>

### Access reviews

Access to in-scope systems is reviewed at least quarterly by {{reviewer: CTO}}, and access that is no longer needed is removed.

<sub>POL-05.07 · Controls: AC-03A · Tailor using: Access ownership, Headcount</sub>

### Privileged access (standing)

Standing admin and production access is limited to named people, approved by {{Technical Lead: CTO}} and reviewed at least quarterly.

<sub>POL-05.08 · Controls: AC-05A · Tailor using: Privileged & production access</sub>

### Root and break-glass accounts

Root and break-glass accounts are protected with MFA, stored securely and used only in emergencies, and each use is reviewed.

<sub>POL-05.10 · Controls: AC-12 · Tailor using: Infrastructure</sub>

### Access to customer data

Staff access customer data only to support a customer or resolve an incident, with approval where required, and the access is logged.

<sub>POL-05.11 · Controls: AC-13B · Tailor using: Provider access to customer data</sub>

### Access removal

Access is removed when it is no longer needed, and within {{timeframe: 1 business day}} of someone leaving.

<sub>POL-05.15 · Controls: AC-02 · Tailor using: HR System, Identity and Authentication</sub>

## Add if your setup differs

<details>
<summary>5 more library statements, and when each applies</summary>

- **Access requests (owner-led)** (POL-05.02; controls AC-01B). *Applies when:* All stages, when Access ownership isn't Centralised (or isn't answered yet).  
  Each system owner approves and grants access to their system based on role, and keeps a record of the approval.
- **Privileged access (temporary or just in time)** (POL-05.09; controls AC-05B, AC-05C, AC-06). *Applies when:* All stages, when Privileged & production access is Temporary / elevated.  
  Admin and production access is requested when needed, approved, time-limited and logged.
- **Administration for customers** (POL-05.12; controls AC-14). *Applies when:* All stages, when Customer administration is Provider-managed or Shared.  
  Where staff administer customer accounts, they act only on a customer's documented request.
- **Service accounts and API keys** (POL-05.13; controls AC-15). *Applies when:* Scaleup and Enterprise. Always included.  
  Service accounts and API keys have a named owner and minimum permissions, and are rotated when people with access to them leave.
- **Segregation of duties** (POL-05.14; controls AC-16). *Applies when:* Enterprise only. Always included.  
  No single person can both make and approve a high-risk change, payment or access grant.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who approves access for a new starter, and where is that recorded? Who has admin access to production today? When do your people look at customer data, and who allows it?

Profile fields to draw on: Access ownership, Privileged & production access, Provider access to customer data, Customer administration, Identity and Authentication, Password Manager, Privileged Access Management.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
