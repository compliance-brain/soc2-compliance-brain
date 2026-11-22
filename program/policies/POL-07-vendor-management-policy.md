# Vendor Management Policy

<!-- policy: POL-07 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Onboarding (central) (POL-07.02): Review before any data is shared}}`
> - [ ] `{{Confirm: Annual review (POL-07.05): Annually for Tier 1 and 2}}`
> - [ ] `{{Confirm: Subservice organisations (POL-07.06): Annually}}`
> - [ ] `{{Confirm: AI providers (POL-07.07): No training on customer data}}`

## Purpose

Sets out how vendors are selected, assessed, contracted and reviewed, based on the data and services they provide.

## Scope

All third parties that provide services, hold company or customer data, or have access to company systems.

## Policy statements

### Vendor inventory

The company keeps a register of vendors showing what each provides, the data it can access, its tier and its owner.

<sub>POL-07.01 · Controls: VM-01A · Tailor using: Vendors tab</sub>

### Onboarding (central)

New vendors are reviewed and approved by {{vendor approver: Head of Operations}} before they receive company data or system access.

<sub>POL-07.02 · Controls: VM-01A · Tailor using: Vendor management</sub>

### Agreements

Vendors that handle company or customer data have written terms covering security and confidentiality, and a data processing agreement where they process personal data.

<sub>POL-07.04 · Controls: VM-03 · Tailor using: Customer Types, Regulatory Drivers</sub>

### Annual review

Tier 1 and Tier 2 vendors are reviewed at least annually, including their latest SOC 2 or ISO 27001 report and the controls they expect their customers to run.

<sub>POL-07.05 · Controls: VM-02 · Tailor using: Vendors tab</sub>

### Subservice organisations

Controls the company relies on from cloud and hosting providers are identified, and the providers' assurance reports are reviewed.

<sub>POL-07.06 · Controls: VM-05A · Tailor using: Infrastructure, Hosting Platform, Subservice Providers</sub>

### AI providers

AI tools and model providers are approved before use, and their terms are checked for training on customer data, retention and data location.

<sub>POL-07.07 · Controls: AI-01, AI-03 · Tailor using: AI Models and Platforms</sub>

### Vendor offboarding

When a vendor relationship ends, its access is removed and it confirms return or deletion of company data.

<sub>POL-07.09 · Controls: VM-03 · Tailor using: Vendors tab</sub>

## Add if your setup differs

<details>
<summary>2 more library statements, and when each applies</summary>

- **Onboarding (owner-led)** (POL-07.03; controls VM-01B). *Applies when:* All stages, when Vendor management is Federated or Distributed.  
  The team adopting a vendor reviews it against the tier requirements and records the approval in the register.
- **Ongoing monitoring** (POL-07.08; controls VM-04). *Applies when:* Enterprise only. Always included.  
  Critical vendors are monitored for security incidents and changes in their assurance between reviews.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who can sign up for a new tool, and does anyone check it first? Who pays the bills and keeps the contracts? Which vendors would hurt most if they went down?

Profile fields to draw on: Vendor management, Subservice Providers, Infrastructure, Hosting Platform, AI Models and Platforms.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
