# Continuity and recovery plan

> [!NOTE]
> **🧭 Guide.** Controls BC-01A and BC-02 (plus AV-01B, AV-02, AV-05 and AV-07 when Availability is in scope). How you keep the service running and recover it. Keep it to what you'd actually use in an outage. Review it every year and after any real recovery or test.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI fills the dependencies from the System Context fields in [profile.yaml](../context/profile.yaml). 👤 Set the recovery targets and the emergency backup person.

> [!WARNING]
> **✅ Confirm before approval.**
>
> - [ ] `{{Confirm: recovery time objective, e.g. 24 hours}}`
> - [ ] `{{Confirm: recovery point objective, which follows from how often backups run}}`
> - [ ] `{{Confirm: who can act if the founder is unavailable, and how they get access}}`

## Who does what

| Role | Who |
| --- | --- |
| Recovery lead | `{{recovery lead: CTO}}` |
| Emergency backup | `{{emergency backup: Lead Engineer, with break-glass access to the cloud account}}` |

## What you depend on

| Service | What it does | If it fails | First response |
| --- | --- | --- | --- |
| `{{cloud provider: Amazon Web Services}}` | Hosts the application | Service unavailable | Check the provider status page; roll back a bad deploy; tell customers through `{{status page: Better Stack}}` |
| `{{database: Amazon RDS}}` | Stores customer data | Users can't sign in or load data | Fail over or restore from `{{backups: Amazon RDS automated backups}}` |
| `{{code repository: GitHub}}` | Source code and deploys | Can't ship changes | Local clones hold full history; hold releases until restored |
| `{{identity provider: Google Workspace}}` | Staff sign-in | Staff can't reach tools | Use break-glass accounts kept in `{{password manager: 1Password}}` |

## Recovery targets

| Target | Value | Basis |
| --- | --- | --- |
| Recovery time objective (longest acceptable outage) | `{{RTO: 8 hours}}` | `{{basis: customer expectations and the uptime target in your terms}}` |
| Recovery point objective (most data that can be lost) | `{{RPO: 5 minutes}}` | `{{basis: point-in-time recovery on the database}}` |

## Scenarios

- **A deployment breaks production:** `{{rollback: redeploy the previous release from the pipeline}}`
- **Data is lost or damaged:** `{{restore: point-in-time restore to a new database, check it, then switch over}}`
- **A provider has an outage:** confirm on its status page, notify affected customers, log it as an incident.
- **A device is lost or stolen:** report it, sign out sessions, wipe the device, issue new secrets.
- **The founder is unavailable:** `{{succession: the Lead Engineer acts, using break-glass access}}`

## Testing

A backup restore test and a plan test every year, recorded in the [activity log](../records/activity-log.csv) using the [restore test template](../templates/backup-restore-test-record.md).
