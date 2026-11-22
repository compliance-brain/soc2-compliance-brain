# Backup restore test record

> [!NOTE]
> **🧭 Guide.** At least annually. Controls BC-01A and BC-02 (and AV-01B if Availability is in scope). Backups run automatically in `{{backups: Amazon RDS automated backups}}`; this test proves you can restore them. Restore into a separate environment, never over production.

- [ ] Pick a recent backup and note its date
- [ ] Restore it to a separate environment and time it
- [ ] Check the data: expected tables or files, sensible counts, a test account works
- [ ] Delete the test environment afterwards
- [ ] If it failed or missed the recovery target, log an Exception ticket

| Backup date | Restored to | Time taken | Checks passed | Result |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

**Performed by:** `{{name}}` on `{{date}}`
