# Operations Security Policy

<!-- policy: POL-10 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how infrastructure is secured, monitored and kept free of known vulnerabilities. Linked controls: NS-01A, NS-01B, NS-02, NS-06, NS-07, TV-01A, TV-01B, TV-02A, TV-02B, TV-03, TV-04, TV-05, TV-06A, TV-06B, TV-07, LM-01A, LM-01B, LM-02A, LM-02B, LM-03, LM-04, LM-05. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Infrastructure, Hosting Platform, Infrastructure operations, Edge and Web Protection, Infrastructure Vulnerability Scanning, Software Vulnerability Scanning, Audit Logging, Security Threat Detection, Penetration Test Status). 👤 The owner answers: Who gets alerted if something looks wrong in production, and at what hours? How do you find out about vulnerabilities today? When was your last pen test?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Vulnerability scanning (default: Infrastructure at least monthly; code on every change)}}`
> - [ ] `{{Confirm: Remediation timeframes (default: Critical 7 days, High 30 days, Medium 90 days)}}`
> - [ ] `{{Confirm: Penetration testing (default: Annually)}}`
> - [ ] `{{Confirm: Cloud configuration (default: Quarterly if checked by hand)}}`
> - [ ] `{{Confirm: Logging (default: Kept 12 months)}}`

## Purpose

Sets out how infrastructure is secured, monitored and kept free of known vulnerabilities.

## Scope

Production infrastructure, cloud accounts, networks and the tools that monitor them.

## Policy statements

### Network restrictions

Production networks allow only the inbound traffic they need, and management access goes through approved paths.

<sub>POL-10.01 · Controls: NS-01A, NS-01B · Tailor using: Infrastructure, Infrastructure operations</sub>

### No public data stores

Databases and storage buckets holding customer data aren't publicly accessible.

<sub>POL-10.02 · Controls: NS-02 · Tailor using: Databases, Cloud Configuration Monitoring</sub>

### Edge protection

Public endpoints are protected by {{edge or WAF service}} against common attacks and denial of service.

<sub>POL-10.03 · Controls: NS-06 · Tailor using: Edge and Web Protection</sub>

### Database configuration

Databases follow secure configuration settings, including access controls and backups.

<sub>POL-10.04 · Controls: NS-07 · Tailor using: Databases</sub>

### Vulnerability scanning

Infrastructure and code are scanned for vulnerabilities, automatically where tools allow.

<sub>POL-10.05 · Controls: TV-01A, TV-01B, TV-02A, TV-02B · Tailor using: Infrastructure Vulnerability Scanning, Software Vulnerability Scanning</sub>

### Remediation timeframes

Vulnerabilities are fixed within set timeframes by severity. Exceptions are approved and tracked.

<sub>POL-10.06 · Controls: TV-03 · Tailor using: Ticketing</sub>

### Penetration testing

An independent penetration test is done at least annually, and findings are tracked to closure.

<sub>POL-10.07 · Controls: TV-04, TV-05 · Tailor using: Penetration Test Status, Penetration Test Approach</sub>

### Cloud configuration

Cloud settings are checked against a security baseline, continuously or at least quarterly.

<sub>POL-10.08 · Controls: TV-06A, TV-06B · Tailor using: Cloud Configuration Monitoring</sub>

### Patching

Servers the company manages are patched within the remediation timeframes.

<sub>POL-10.09 · Controls: TV-07 · Tailor using: Infrastructure operations</sub>

### Logging

Security-relevant activity in production, the identity provider and cloud accounts is logged, protected from change and kept for {{period}}.

<sub>POL-10.10 · Controls: LM-01A, LM-01B · Tailor using: Audit Logging</sub>

### Alerts and response

Suspicious activity raises alerts to {{team or on-call rota}}, who triage them within set times.

<sub>POL-10.11 · Controls: LM-02A, LM-02B, LM-03 · Tailor using: Security Threat Detection, Incident response</sub>

### Log review and round-the-clock monitoring

Logs are reviewed regularly and security monitoring runs around the clock.

<sub>POL-10.12 · Controls: LM-04, LM-05 · Tailor using: Company Stage</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
