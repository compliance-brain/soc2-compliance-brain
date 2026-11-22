# Business Continuity and Disaster Recovery Policy

<!-- policy: POL-13 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how the company keeps the service running and recovers data and systems after a disruption. Linked controls: BC-01A, BC-01B, BC-02, AV-01A, AV-01B, AV-02, AV-03, AV-04A, AV-04B, AV-05A, AV-05B, AV-06, AV-07A, AV-07B, AV-09. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Backups and Recovery, Availability responsibility, Service Commitments, Hosting Platform, Auto-scaling, Availability Monitoring, Status Page). 👤 The owner answers: If your main cloud region went down, what would you do? How much data could you afford to lose? Have you ever restored from a backup?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Backups (default: Daily, kept 30 days)}}`
> - [ ] `{{Confirm: Continuity plan (default: Targets that match customer commitments)}}`
> - [ ] `{{Confirm: Restore testing (default: Annually; quarterly where availability is committed)}}`
> - [ ] `{{Confirm: Plan testing (default: Annually)}}`

## Purpose

Sets out how the company keeps the service running and recovers data and systems after a disruption.

## Scope

The in-scope service, its data, and the people and vendors it depends on.

## Policy statements

### Backups

Customer data and critical systems are backed up automatically, encrypted and kept in a separate location.

<sub>POL-13.01 · Controls: BC-01A, BC-01B · Tailor using: Backups and Recovery</sub>

### Continuity plan

A continuity and recovery plan sets recovery time and data loss targets and the steps to restore service.

<sub>POL-13.02 · Controls: BC-02 · Tailor using: Service Commitments, Availability responsibility</sub>

### Restore testing

Backups are test-restored at least annually and the results recorded.

<sub>POL-13.03 · Controls: AV-01A, AV-01B · Tailor using: Backups and Recovery</sub>

### Plan testing

The continuity plan is tested at least annually.

<sub>POL-13.04 · Controls: AV-02 · Tailor using: Availability responsibility</sub>

### Redundancy

Production runs across multiple availability zones with no single point of failure for critical components.

<sub>POL-13.05 · Controls: AV-03 · Tailor using: Hosting Platform</sub>

### Capacity

Capacity scales automatically, or is monitored and planned ahead of demand.

<sub>POL-13.06 · Controls: AV-04A, AV-04B · Tailor using: Auto-scaling</sub>

### Availability monitoring

Availability and performance are monitored, with alerts to {{on-call team}}.

<sub>POL-13.07 · Controls: AV-05A, AV-05B · Tailor using: Availability Monitoring</sub>

### Service levels and outage notices

Uptime is measured against commitments, and customers are told about outages and maintenance through {{status page or notice channel}}.

<sub>POL-13.08 · Controls: AV-06, AV-07A, AV-07B · Tailor using: Status Page, Service Commitments</sub>

### Regional failover

The service can fail over to another region within the recovery time target.

<sub>POL-13.09 · Controls: AV-09 · Tailor using: Hosting Platform</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
