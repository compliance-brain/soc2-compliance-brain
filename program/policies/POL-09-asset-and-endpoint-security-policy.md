# Asset and Endpoint Security Policy

<!-- policy: POL-09 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how devices and other assets are tracked, secured and disposed of, and how physical sites are protected. Linked controls: EP-01A, EP-01B, EP-02A, EP-02B, EP-03, EP-04, EP-05, EP-06, PS-01, PS-02, AV-08. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Device Management, Endpoint Protection, Endpoint model, Facilities, Workforce model). 👤 The owner answers: Who sets up laptops for new starters? What happens to a laptop when someone leaves? Is there an office with anything sensitive in it?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Device settings (checked) (default: Quarterly)}}`

## Purpose

Sets out how devices and other assets are tracked, secured and disposed of, and how physical sites are protected.

## Scope

Company-owned and personal devices used for work, and any offices or equipment in scope.

## Policy statements

### Asset inventory

The company keeps an inventory of devices and other assets, with an owner for each.

<sub>POL-09.01 · Controls: EP-03 · Tailor using: Device Management</sub>

### Device settings (managed)

Company devices are enrolled in {{device management}}, which enforces disk encryption, screen lock, operating system updates and firewall.

<sub>POL-09.02 · Controls: EP-01A · Tailor using: Device Management</sub>

### Device settings (checked)

Devices are checked against the required settings (encryption, screen lock, updates) at onboarding and at least quarterly.

<sub>POL-09.03 · Controls: EP-01B · Tailor using: Endpoint model</sub>

### Malware protection

Devices run {{endpoint protection}} and its alerts are reviewed.

<sub>POL-09.04 · Controls: EP-02A, EP-02B · Tailor using: Endpoint Protection</sub>

### Personal devices

Personal devices used for work meet the same minimum settings, and their access is limited to approved apps.

<sub>POL-09.05 · Controls: EP-05 · Tailor using: Endpoint model</sub>

### Device trust

Access to sensitive systems is limited to managed devices that pass health checks.

<sub>POL-09.06 · Controls: EP-06 · Tailor using: Identity and Authentication, Device Management</sub>

### Disposal

Devices and media are securely wiped or destroyed before reuse or disposal, and this is recorded.

<sub>POL-09.07 · Controls: EP-04 · Tailor using: Device Management</sub>

### Physical security

Offices and areas with in-scope equipment limit entry to authorised people, and visitors are logged.

<sub>POL-09.08 · Controls: PS-01 · Tailor using: Facilities</sub>

### Equipment at customer sites

Devices deployed at customer sites are tracked, hardened and monitored.

<sub>POL-09.09 · Controls: PS-02 · Tailor using: Facilities</sub>

### Environmental protection

Server rooms and data centres the company runs have maintained power, fire and climate protection.

<sub>POL-09.10 · Controls: AV-08 · Tailor using: Facilities</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
