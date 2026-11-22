# Access request

> [!NOTE]
> **🧭 Guide.** Controls AC-01A and AC-13B. Use for every new account or permission change, and for any exception-only access to customer data. Log it in [requests-and-tickets.csv](../records/requests-and-tickets.csv) (Type: Access request) or in `{{ticketing: Linear}}`, approved *before* access is granted.

| Field | Answer |
| --- | --- |
| Person | `{{name}}` |
| System and access level | `{{system and role · e.g. AWS production read-only}}` |
| Why it's needed | |
| Customer data involved? | No / Yes (exception only: say which customer, why and for how long) |
| Expires | `{{date, or "role-based, no expiry"}}` |
| Approved by | `{{approver: CTO}}` on `{{date}}` |
| Granted by | `{{name}}` on `{{date}}` |

- [ ] Approval recorded before access was granted
- [ ] Access matches the role (least privilege, AC-04)
- [ ] Temporary access removed when it expired
