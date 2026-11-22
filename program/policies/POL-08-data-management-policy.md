# Data Management Policy

<!-- policy: POL-08 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Classification (POL-08.01): Four levels}}`
> - [ ] `{{Confirm: Encryption in transit (POL-08.02): TLS 1.2 or higher}}`
> - [ ] `{{Confirm: Encryption at rest (POL-08.03): AES-256}}`

## Purpose

Sets out how information is classified, handled, encrypted, retained and deleted.

## Scope

All company and customer data in the system boundary, in any format.

## Policy statements

### Classification

Information is classified as Public, Internal, Confidential or Restricted, and handled according to its class. Customer data is Confidential at minimum.

<sub>POL-08.01 · Controls: DM-01 · Tailor using: Data Handled</sub>

### Encryption in transit

Data is encrypted in transit over public networks using current TLS.

<sub>POL-08.02 · Controls: NS-03 · Tailor using: Edge and Web Protection, Hosting Platform</sub>

### Encryption at rest

Customer data is encrypted at rest using provider-managed or customer-managed keys.

<sub>POL-08.03 · Controls: NS-04 · Tailor using: Databases, Application Secrets and Encryption</sub>

### Keys and secrets

Keys and secrets are kept in {{secrets manager: AWS Secrets Manager}}, never in code, and rotated when exposed or when people with access leave.

<sub>POL-08.04 · Controls: NS-05A · Tailor using: Application Secrets and Encryption</sub>

### Tenant separation

Each customer's data is kept separate from other customers' data, and the separation is tested.

<sub>POL-08.05 · Controls: DM-02A · Tailor using: Tenancy & isolation</sub>

## Add if your setup differs

<details>
<summary>6 more library statements, and when each applies</summary>

- **Data location** (POL-08.06; controls NS-08). *Applies when:* All stages, when Data control boundary is Customer-controlled or Shared.  
  Customer data is stored in the regions committed to in contracts, and moved only with the customer's agreement.
- **Retention** (POL-08.07; controls CF-02). *Applies when:* All stages, when Confidentiality is in scope.  
  Data is kept only as long as its purpose and contracts require, as set out in the retention schedule.
- **Deletion** (POL-08.08; controls CF-03). *Applies when:* All stages, when Confidentiality is in scope.  
  Data is securely deleted at the end of its retention period or on a valid customer request, and the deletion is recorded.
- **Test data** (POL-08.09; controls CF-04). *Applies when:* All stages, when Confidentiality is in scope.  
  Production customer data isn't used in development or test environments unless it has been anonymised.
- **Data minimisation** (POL-08.10; controls CF-05). *Applies when:* All stages, when Confidentiality is in scope, and Data minimisation is Minimised or Purpose-limited.  
  The service collects only the customer data it needs for its purpose.
- **Data loss prevention** (POL-08.11; controls NS-09). *Applies when:* All stages, when a Data Loss Prevention tool is named.  
  Data loss prevention rules monitor and limit sensitive data leaving approved systems.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: What customer data do you hold, and where? How long do you keep it after a customer leaves? Do you ever copy production data into test?

Profile fields to draw on: Data Handled, Data minimisation, Data control boundary, Tenancy & isolation, Databases, Application Secrets and Encryption, Service Commitments.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
