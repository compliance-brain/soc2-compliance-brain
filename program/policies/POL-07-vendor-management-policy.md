# Vendor Management Policy

<!-- policy: POL-07 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how vendors are selected, assessed, contracted and reviewed, based on the data and services they provide. Linked controls: VM-01A, VM-01B, VM-02, VM-03, VM-04, VM-05A, VM-05B, AI-01, AI-03. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Vendor management, Subservice Providers, Infrastructure, Hosting Platform, AI Models and Platforms). 👤 The owner answers: Who can sign up for a new tool, and does anyone check it first? Who pays the bills and keeps the contracts? Which vendors would hurt most if they went down?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Onboarding (central) (default: Review before any data is shared)}}`
> - [ ] `{{Confirm: Annual review (default: Annually for Tier 1 and 2)}}`
> - [ ] `{{Confirm: Subservice organisations (default: Annually)}}`
> - [ ] `{{Confirm: AI providers (default: No training on customer data)}}`

## Purpose

Sets out how vendors are selected, assessed, contracted and reviewed, based on the data and services they provide.

## Scope

All third parties that provide services, hold company or customer data, or have access to company systems.

## Policy statements

### Vendor inventory

The company keeps a register of vendors showing what each provides, the data it can access, its tier and its owner.

<sub>POL-07.01 · Controls: VM-01A, VM-01B · Tailor using: Vendors tab</sub>

### Onboarding (central)

New vendors are reviewed and approved by {{role}} before they receive company data or system access.

<sub>POL-07.02 · Controls: VM-01A · Tailor using: Vendor management</sub>

### Onboarding (owner-led)

The team adopting a vendor reviews it against the tier requirements and records the approval in the register.

<sub>POL-07.03 · Controls: VM-01B · Tailor using: Vendor management</sub>

### Agreements

Vendors that handle company or customer data have written terms covering security and confidentiality, and a data processing agreement where they process personal data.

<sub>POL-07.04 · Controls: VM-03 · Tailor using: Customer Types, Regulatory Drivers</sub>

### Annual review

Tier 1 and Tier 2 vendors are reviewed at least annually, including their latest SOC 2 or ISO 27001 report and the controls they expect their customers to run.

<sub>POL-07.05 · Controls: VM-02 · Tailor using: Vendors tab</sub>

### Subservice organisations

Controls the company relies on from cloud and hosting providers are identified, and the providers' assurance reports are reviewed.

<sub>POL-07.06 · Controls: VM-05A, VM-05B · Tailor using: Infrastructure, Hosting Platform, Subservice Providers</sub>

### AI providers

AI tools and model providers are approved before use, and their terms are checked for training on customer data, retention and data location.

<sub>POL-07.07 · Controls: AI-01, AI-03 · Tailor using: AI Models and Platforms</sub>

### Ongoing monitoring

Critical vendors are monitored for security incidents and changes in their assurance between reviews.

<sub>POL-07.08 · Controls: VM-04 · Tailor using: Compliance Automation</sub>

### Vendor offboarding

When a vendor relationship ends, its access is removed and it confirms return or deletion of company data.

<sub>POL-07.09 · Controls: VM-03 · Tailor using: Vendors tab</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
