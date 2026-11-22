# Data Management Policy

<!-- policy: POL-08 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how information is classified, handled, encrypted, retained and deleted. Linked controls: DM-01, DM-02A, DM-02B, DM-02C, NS-03, NS-04, NS-05A, NS-05B, NS-08, NS-09, CF-01, CF-02, CF-03, CF-04, CF-05. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Data Handled, Data minimisation, Data control boundary, Tenancy & isolation, Databases, Application Secrets and Encryption, Service Commitments). 👤 The owner answers: What customer data do you hold, and where? How long do you keep it after a customer leaves? Do you ever copy production data into test?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Classification (default: Four levels)}}`
> - [ ] `{{Confirm: Encryption in transit (default: TLS 1.2 or higher)}}`
> - [ ] `{{Confirm: Encryption at rest (default: AES-256)}}`
> - [ ] `{{Confirm: Retention (default: Customer data deleted within 30 to 90 days of contract end)}}`

## Purpose

Sets out how information is classified, handled, encrypted, retained and deleted.

## Scope

All company and customer data in the system boundary, in any format.

## Policy statements

### Classification

Information is classified as Public, Internal, Confidential or Restricted, and handled according to its class. Customer data is Confidential at minimum.

<sub>POL-08.01 · Controls: DM-01, CF-01 · Tailor using: Data Handled</sub>

### Encryption in transit

Data is encrypted in transit over public networks using current TLS.

<sub>POL-08.02 · Controls: NS-03 · Tailor using: Edge and Web Protection, Hosting Platform</sub>

### Encryption at rest

Customer data is encrypted at rest using provider-managed or customer-managed keys.

<sub>POL-08.03 · Controls: NS-04 · Tailor using: Databases, Application Secrets and Encryption</sub>

### Keys and secrets

Keys and secrets are kept in {{secrets manager}}, never in code, and rotated when exposed or when people with access leave.

<sub>POL-08.04 · Controls: NS-05A, NS-05B · Tailor using: Application Secrets and Encryption</sub>

### Tenant separation

Each customer's data is kept separate from other customers' data, and the separation is tested.

<sub>POL-08.05 · Controls: DM-02A, DM-02B, DM-02C · Tailor using: Tenancy & isolation</sub>

### Data location

Customer data is stored in the regions committed to in contracts, and moved only with the customer's agreement.

<sub>POL-08.06 · Controls: NS-08 · Tailor using: Data control boundary, Customer Geography</sub>

### Retention

Data is kept only as long as its purpose and contracts require, as set out in the retention schedule.

<sub>POL-08.07 · Controls: CF-02 · Tailor using: Service Commitments, Regulatory Drivers</sub>

### Deletion

Data is securely deleted at the end of its retention period or on a valid customer request, and the deletion is recorded.

<sub>POL-08.08 · Controls: CF-03 · Tailor using: Service Commitments</sub>

### Test data

Production customer data isn't used in development or test environments unless it has been anonymised.

<sub>POL-08.09 · Controls: CF-04 · Tailor using: Databases</sub>

### Data minimisation

The service collects only the customer data it needs for its purpose.

<sub>POL-08.10 · Controls: CF-05 · Tailor using: Data minimisation</sub>

### Data loss prevention

Data loss prevention rules monitor and limit sensitive data leaving approved systems.

<sub>POL-08.11 · Controls: NS-09 · Tailor using: Data Loss Prevention</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
