# Asset and Endpoint Security Policy

<!-- policy: POL-09 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

## Purpose

Sets out how devices and other assets are tracked, secured and disposed of, and how physical sites are protected.

## Scope

Company-owned and personal devices used for work, and any offices or equipment in scope.

## Policy statements

### Asset inventory

The company keeps an inventory of devices and other assets, with an owner for each.

<sub>POL-09.01 · Controls: EP-03 · Tailor using: Device Management</sub>

### Device settings (managed)

Company devices are enrolled in {{device management: Kandji}}, which enforces disk encryption, screen lock, operating system updates and firewall.

<sub>POL-09.02 · Controls: EP-01A · Tailor using: Device Management</sub>

### Malware protection

Devices run {{endpoint protection: the operating system's built-in malware protection, enforced through Kandji}} and its alerts are reviewed.

<sub>POL-09.04 · Controls: EP-02B · Tailor using: Endpoint Protection</sub>

### Disposal

Devices and media are securely wiped or destroyed before reuse or disposal, and this is recorded.

<sub>POL-09.07 · Controls: EP-04 · Tailor using: Device Management</sub>

## Add if your setup differs

<details>
<summary>6 more library statements, and when each applies</summary>

- **Device settings (checked)** (POL-09.03; controls EP-01B). *Applies when:* All stages, when no Device Management tool is named (or it's TBC).  
  Devices are checked against the required settings (encryption, screen lock, updates) at onboarding and at least quarterly.
- **Personal devices** (POL-09.05; controls EP-05). *Applies when:* All stages, when Endpoint model is BYOD or Mixed.  
  Personal devices used for work meet the same minimum settings, and their access is limited to approved apps.
- **Device trust** (POL-09.06; controls EP-06). *Applies when:* Enterprise only, when Endpoint model isn't BYOD (or isn't answered yet).  
  Access to sensitive systems is limited to managed devices that pass health checks.
- **Physical security** (POL-09.08; controls PS-01). *Applies when:* All stages, when Facilities is Office(s) with in-scope equipment, On-premises data centre / server room, Manufacturing / production site or Warehouse / logistics site.  
  Offices and areas with in-scope equipment limit entry to authorised people, and visitors are logged.
- **Equipment at customer sites** (POL-09.09; controls PS-02). *Applies when:* All stages, when Facilities is Customer sites (company devices deployed).  
  Devices deployed at customer sites are tracked, hardened and monitored.
- **Environmental protection** (POL-09.10; controls AV-08). *Applies when:* All stages, when Availability is in scope, and Facilities is On-premises data centre / server room or Colocation data centre.  
  Server rooms and data centres the company runs have maintained power, fire and climate protection.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who sets up laptops for new starters? What happens to a laptop when someone leaves? Is there an office with anything sensitive in it?

Profile fields to draw on: Device Management, Endpoint Protection, Endpoint model, Facilities, Workforce model.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
