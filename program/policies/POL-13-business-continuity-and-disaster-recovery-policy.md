# Business Continuity and Disaster Recovery Policy

<!-- policy: POL-13 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Backups (POL-13.01): Daily, kept 30 days}}`
> - [ ] `{{Confirm: Continuity plan (POL-13.02): Targets that match customer commitments}}`

## Purpose

Sets out how the company keeps the service running and recovers data and systems after a disruption.

## Scope

The in-scope service, its data, and the people and vendors it depends on.

## Policy statements

### Backups

Customer data and critical systems are backed up automatically, encrypted and kept in a separate location.

<sub>POL-13.01 · Controls: BC-01A · Tailor using: Backups and Recovery</sub>

### Continuity plan

A continuity and recovery plan sets recovery time and data loss targets and the steps to restore service.

<sub>POL-13.02 · Controls: BC-02 · Tailor using: Service Commitments, Availability responsibility</sub>

## Add if your setup differs

<details>
<summary>7 more library statements, and when each applies</summary>

- **Restore testing** (POL-13.03; controls AV-01A, AV-01B). *Applies when:* All stages, when Availability is in scope, and Availability responsibility is Committed availability.  
  Backups are test-restored at least annually and the results recorded.
- **Plan testing** (POL-13.04; controls AV-02). *Applies when:* All stages, when Availability is in scope.  
  The continuity plan is tested at least annually.
- **Redundancy** (POL-13.05; controls AV-03). *Applies when:* All stages, when Availability is in scope, and Availability responsibility isn't Best efforts (or isn't answered yet).  
  Production runs across multiple availability zones with no single point of failure for critical components.
- **Capacity** (POL-13.06; controls AV-04A, AV-04B). *Applies when:* All stages, when Availability is in scope, and Auto-scaling is Auto-scaling configured.  
  Capacity scales automatically, or is monitored and planned ahead of demand.
- **Availability monitoring** (POL-13.07; controls AV-05A, AV-05B). *Applies when:* All stages, when Availability is in scope, and a Availability Monitoring tool is named.  
  Availability and performance are monitored, with alerts to {{on-call team: TBC}}.
- **Service levels and outage notices** (POL-13.08; controls AV-06, AV-07A, AV-07B). *Applies when:* All stages, when Availability is in scope, and Availability responsibility is Committed availability or Targeted availability.  
  Uptime is measured against commitments, and customers are told about outages and maintenance through {{status page or notice channel: TBC}}.
- **Regional failover** (POL-13.09; controls AV-09). *Applies when:* Enterprise only, when Availability is in scope.  
  The service can fail over to another region within the recovery time target.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: If your main cloud region went down, what would you do? How much data could you afford to lose? Have you ever restored from a backup?

Profile fields to draw on: Backups and Recovery, Availability responsibility, Service Commitments, Hosting Platform, Auto-scaling, Availability Monitoring, Status Page.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
