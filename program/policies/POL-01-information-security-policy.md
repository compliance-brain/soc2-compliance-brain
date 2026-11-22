# Information Security Policy

<!-- policy: POL-01 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: yes -->

> [!NOTE]
> **🧭 Guide.** Sets out how the company protects the information it holds and the service it provides, who is responsible, and how the policy set is managed. Linked controls: GV-01, GV-02A, GV-02B, GV-03, GV-07, GV-09, GV-12, GV-13, RM-04, CO-01. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Team Details, Governance, Operating Cadence, Company Stage, Framework Scope, Control execution). 👤 The owner answers: Who signs off policies? Which leadership meeting already happens where security could be a standing item? Who do staff go to with a security question?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Roles (default: Name roles in the policy, not individuals)}}`
> - [ ] `{{Confirm: Policy management (default: Annual review)}}`
> - [ ] `{{Confirm: Oversight (committee) (default: Quarterly)}}`
> - [ ] `{{Confirm: Oversight (management) (default: Every six months, in an existing leadership meeting)}}`
> - [ ] `{{Confirm: Organisational structure (default: Updated as changes happen)}}`
> - [ ] `{{Confirm: Exceptions (default: Up to 12 months per exception)}}`
> - [ ] `{{Confirm: Automated and agent-run controls (default: Owner checks at least quarterly)}}`
> - [ ] `{{Confirm: Reporting security concerns (default: A security@ address or trust page form)}}`
> - [ ] `{{Confirm: Control review (default: Annually)}}`

## Purpose

Sets out how the company protects the information it holds and the service it provides, who is responsible, and how the policy set is managed.

## Scope

All staff, contractors and systems in the system boundary.

## Policy statements

### Roles

{{Compliance Owner}} is accountable for the information security program. {{Technical Lead}} owns technical controls and {{Governance Lead}} owns governance and business risk.

<sub>POL-01.01 · Controls: GV-01, GV-03 · Tailor using: Team Details: Compliance Owner, Technical Lead, Governance Lead</sub>

### Policy management

Policies are approved by management, published where all staff can read them, and reviewed at least annually or after a significant change.

<sub>POL-01.02 · Controls: GV-01 · Tailor using: Program home, Knowledge Management</sub>

### Oversight (committee)

A security committee meets at least quarterly under a written charter and records its decisions and actions.

<sub>POL-01.03 · Controls: GV-02A · Tailor using: Governance, Operating Cadence</sub>

### Oversight (management)

Leadership reviews the security program at least every six months in an existing meeting and records decisions and actions.

<sub>POL-01.04 · Controls: GV-02B · Tailor using: Governance, Operating Cadence</sub>

### Organisational structure

The company keeps an organisational chart showing reporting lines and updates it when the structure changes.

<sub>POL-01.05 · Controls: GV-03 · Tailor using: HR System, Headcount</sub>

### Security lead

A named security lead coordinates the program day to day and reports to management.

<sub>POL-01.06 · Controls: GV-07 · Tailor using: Team Details, Company Stage</sub>

### Exceptions

Exceptions to policy are requested in writing, approved by the policy owner, time-limited and recorded.

<sub>POL-01.07 · Controls: GV-09 · Tailor using: Ticketing</sub>

### Automated and agent-run controls

Each control performed by automation or an AI agent has a named person who owns it, reviews its exceptions and checks it is still working.

<sub>POL-01.08 · Controls: GV-12, GV-13 · Tailor using: Control execution, Compliance Automation, AI Models and Platforms</sub>

### Reporting security concerns

Staff, customers and researchers can report security issues through a published channel, and reports are triaged promptly.

<sub>POL-01.09 · Controls: CO-01 · Tailor using: Domain (security or trust page)</sub>

### Control review

The control framework is reviewed at least annually and when systems, risks or commitments change.

<sub>POL-01.10 · Controls: RM-04 · Tailor using: Controls tab, Planned Changes</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
