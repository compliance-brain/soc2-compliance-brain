# Secure Development and Change Management Policy

<!-- policy: POL-11 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how changes to code, infrastructure and configuration are designed, reviewed, tested and released. Linked controls: CM-01, CM-02A, CM-02B, CM-03A, CM-03B, CM-04A, CM-04B, CM-05, CM-06A, CM-06B, CM-06C, CM-07, CM-08A, CM-08B, CM-09, CM-10, CM-11, CM-12. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (Change management, Release Frequency, Code Repository, Build and Deployment / CI/CD, Infrastructure Configuration, Ticketing, Service standardisation). 👤 The owner answers: Walk me through how a change gets to production. Can anyone deploy on their own? What happens when something urgent needs fixing at night?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Peer review (default: One reviewer)}}`
> - [ ] `{{Confirm: Emergency changes (default: Reviewed within 2 business days)}}`

## Purpose

Sets out how changes to code, infrastructure and configuration are designed, reviewed, tested and released.

## Scope

Application code, infrastructure, configuration and data changes to the in-scope system.

## Policy statements

### Change types

Change types (standard, normal and emergency) are defined, along with who can approve each.

<sub>POL-11.01 · Controls: CM-01 · Tailor using: Change management</sub>

### Version control

All code and infrastructure definitions are kept in {{code repository}}.

<sub>POL-11.02 · Controls: CM-02A, CM-02B · Tailor using: Code Repository</sub>

### Branch protection

The main branch is protected: changes go through pull requests and can't be pushed directly.

<sub>POL-11.03 · Controls: CM-02A · Tailor using: Code Repository</sub>

### Peer review

Every change is reviewed and approved by someone other than its author before release.

<sub>POL-11.04 · Controls: CM-03B · Tailor using: Change management</sub>

### Formal approval

Changes are approved by a change authority before release, with risk and rollback recorded.

<sub>POL-11.05 · Controls: CM-03A · Tailor using: Change management, Ticketing</sub>

### Testing

Changes pass automated tests and checks in {{CI/CD}} before they can be released.

<sub>POL-11.06 · Controls: CM-04A, CM-04B · Tailor using: Build and Deployment / CI/CD</sub>

### Separate environments

Development, test and production are kept separate.

<sub>POL-11.07 · Controls: CM-05 · Tailor using: Hosting Platform</sub>

### Deployment

Production deployments run through {{CI/CD}}, and only authorised people can deploy.

<sub>POL-11.08 · Controls: CM-06A, CM-06B, CM-06C · Tailor using: Change management, Build and Deployment / CI/CD</sub>

### Emergency changes

Emergency changes may skip normal approval to restore service, and are reviewed and approved afterwards.

<sub>POL-11.09 · Controls: CM-07 · Tailor using: Incident response</sub>

### Infrastructure changes

Infrastructure changes are made through {{infrastructure as code}} and reviewed like application changes.

<sub>POL-11.10 · Controls: CM-08A, CM-08B · Tailor using: Infrastructure Configuration</sub>

### Security gates

Security checks such as code scanning, dependency checks and secret detection run in the pipeline and block high-risk issues.

<sub>POL-11.11 · Controls: CM-09 · Tailor using: Software Vulnerability Scanning</sub>

### Customer-specific changes

Customer-specific configurations and changes are requested, approved by the customer and tracked.

<sub>POL-11.12 · Controls: CM-10 · Tailor using: Service standardisation</sub>

### Security design review

Significant new features and architecture changes get a security design review.

<sub>POL-11.13 · Controls: CM-11 · Tailor using: Company Stage</sub>

### Ticketed work

Changes and requests are tracked in {{ticketing}} and linked to the code change.

<sub>POL-11.14 · Controls: CM-12 · Tailor using: Ticketing</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
