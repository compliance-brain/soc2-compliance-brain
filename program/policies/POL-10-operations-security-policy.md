# Operations Security Policy

<!-- policy: POL-10 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Vulnerability scanning (POL-10.05): Infrastructure at least monthly; code on every change}}`
> - [ ] `{{Confirm: Remediation timeframes (POL-10.06): Critical 7 days, High 30 days, Medium 90 days}}`
> - [ ] `{{Confirm: Penetration testing (POL-10.07): Annually}}`
> - [ ] `{{Confirm: Cloud configuration (POL-10.08): Quarterly if checked by hand}}`
> - [ ] `{{Confirm: Logging (POL-10.10): Kept 12 months}}`

## Purpose

Sets out how infrastructure is secured, monitored and kept free of known vulnerabilities.

## Scope

Production infrastructure, cloud accounts, networks and the tools that monitor them.

## Policy statements

### Network restrictions

Production networks allow only the inbound traffic they need, and management access goes through approved paths.

<sub>POL-10.01 · Controls: NS-01A · Tailor using: Infrastructure, Infrastructure operations</sub>

### No public data stores

Databases and storage buckets holding customer data aren't publicly accessible.

<sub>POL-10.02 · Controls: NS-02 · Tailor using: Databases, Cloud Configuration Monitoring</sub>

### Edge protection

Public endpoints are protected by {{edge protection: Cloudflare WAF}} against common attacks and denial of service.

<sub>POL-10.03 · Controls: NS-06 · Tailor using: Edge and Web Protection</sub>

### Database configuration

Databases follow secure configuration settings, including access controls and backups.

<sub>POL-10.04 · Controls: NS-07 · Tailor using: Databases</sub>

### Vulnerability scanning

Infrastructure and code are scanned for vulnerabilities, automatically where tools allow.

<sub>POL-10.05 · Controls: TV-01A, TV-02A · Tailor using: Infrastructure Vulnerability Scanning, Software Vulnerability Scanning</sub>

### Remediation timeframes

Vulnerabilities are fixed within set timeframes by severity. Exceptions are approved and tracked.

<sub>POL-10.06 · Controls: TV-03 · Tailor using: Ticketing</sub>

### Penetration testing

An independent penetration test is done at least annually, and findings are tracked to closure.

<sub>POL-10.07 · Controls: TV-04 · Tailor using: Penetration Test Status, Penetration Test Approach</sub>

### Cloud configuration

Cloud settings are checked against a security baseline, continuously or at least quarterly.

<sub>POL-10.08 · Controls: TV-06A · Tailor using: Cloud Configuration Monitoring</sub>

### Logging

Security-relevant activity in production, the identity provider and cloud accounts is logged, protected from change and kept for {{log retention: 12 months}}.

<sub>POL-10.10 · Controls: LM-01A · Tailor using: Audit Logging</sub>

### Alerts and response

Suspicious activity raises alerts to {{alert recipients: the engineering on-call rota}}, who triage them within set times.

<sub>POL-10.11 · Controls: LM-02A · Tailor using: Security Threat Detection, Incident response</sub>

## Add if your setup differs

<details>
<summary>2 more library statements, and when each applies</summary>

- **Patching** (POL-10.09; controls TV-07). *Applies when:* All stages, when Infrastructure operations is Self-managed.  
  Servers the company manages are patched within the remediation timeframes.
- **Log review and round-the-clock monitoring** (POL-10.12; controls LM-04, LM-05). *Applies when:* Enterprise only. Always included.  
  Logs are reviewed regularly and security monitoring runs around the clock.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Who gets alerted if something looks wrong in production, and at what hours? How do you find out about vulnerabilities today? When was your last pen test?

Profile fields to draw on: Infrastructure, Hosting Platform, Infrastructure operations, Edge and Web Protection, Infrastructure Vulnerability Scanning, Software Vulnerability Scanning, Audit Logging, Security Threat Detection, Penetration Test Status.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
