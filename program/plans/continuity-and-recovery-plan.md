# Continuity and recovery plan

> [!NOTE]
> **🧭 Guide.** Controls BC-02, AV-01B, AV-02, AV-05B and AV-07B. How you keep the service running and recover it. Keep it to what you'd actually use in an outage. Review it every year and after any real recovery or test.

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
| Recovery lead | `{{name}}` |
| Emergency backup | `{{name}}` |

## What you depend on

| Service | What it does | If it fails | First response |
| --- | --- | --- | --- |
| `{{hosting provider}}` | `{{hosts the app}}` | `{{service unavailable}}` | `{{check status page; roll back a bad deploy}}` |
| `{{database provider}}` | `{{stores customer data}}` | `{{users can't sign in}}` | `{{restore from backup}}` |
| `{{code host}}` | `{{source code}}` | `{{can't ship changes}}` | `{{local copies hold full history}}` |

## Recovery targets

| Target | Value | Basis |
| --- | --- | --- |
| Recovery time objective (longest acceptable outage) | `{{value}}` | `{{why}}` |
| Recovery point objective (most data that can be lost) | `{{value}}` | `{{backup frequency}}` |

## Scenarios

- **A deployment breaks production:** `{{how you roll back}}`
- **Data is lost or damaged:** `{{how you restore, and where to}}`
- **A provider has an outage:** confirm on its status page, notify affected customers, log it as an incident.
- **A device is lost or stolen:** report it, sign out sessions, wipe the device, issue new secrets.
- **The founder is unavailable:** `{{who acts and how}}`

## Testing

A backup restore test and a plan test every year, recorded in the [activity log](../records/activity-log.csv) using the [restore test template](../templates/backup-restore-test-record.md).
