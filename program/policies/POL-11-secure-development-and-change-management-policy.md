# Secure Development and Change Management Policy

<!-- policy: POL-11 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Peer review (POL-11.04): One reviewer}}`

## Purpose

Sets out how changes to code, infrastructure and configuration are designed, reviewed, tested and released.

## Scope

Application code, infrastructure, configuration and data changes to the in-scope system.

## Policy statements

### Change types

Change types (standard, normal and emergency) are defined, along with who can approve each.

<sub>POL-11.01 · Controls: CM-01 · Tailor using: Change management</sub>

### Version control

All code and infrastructure definitions are kept in {{code repository: GitHub}}.

<sub>POL-11.02 · Controls: CM-02A · Tailor using: Code Repository</sub>

### Branch protection

The main branch is protected: changes go through pull requests and can't be pushed directly.

<sub>POL-11.03 · Controls: CM-02A · Tailor using: Code Repository</sub>

### Peer review

Every change is reviewed and approved by someone other than its author before release.

<sub>POL-11.04 · Controls: CM-03B · Tailor using: Change management</sub>

### Testing

Changes pass automated tests and checks in {{CI/CD: GitHub Actions}} before they can be released.

<sub>POL-11.06 · Controls: CM-04A · Tailor using: Build and Deployment / CI/CD</sub>

### Separate environments

Development, test and production are kept separate.

<sub>POL-11.07 · Controls: CM-05 · Tailor using: Hosting Platform</sub>

### Deployment

Production deployments run through {{CI/CD: GitHub Actions}}, and only authorised people can deploy.

<sub>POL-11.08 · Controls: CM-06A · Tailor using: Change management, Build and Deployment / CI/CD</sub>

### Infrastructure changes

Infrastructure changes are made through {{infrastructure as code: Terraform}} and reviewed like application changes.

<sub>POL-11.10 · Controls: CM-08A · Tailor using: Infrastructure Configuration</sub>

### Security gates

Security checks such as code scanning, dependency checks and secret detection run in the pipeline and block high-risk issues.

<sub>POL-11.11 · Controls: CM-09 · Tailor using: Software Vulnerability Scanning</sub>

### Ticketed work

Changes and requests are tracked in {{ticketing: Linear}} and linked to the code change.

<sub>POL-11.14 · Controls: CM-12 · Tailor using: Ticketing</sub>

## Add if your setup differs

<details>
<summary>4 more library statements, and when each applies</summary>

- **Formal approval** (POL-11.05; controls CM-03A). *Applies when:* All stages, when Change management is Traditional approval.  
  Changes are approved by a change authority before release, with risk and rollback recorded.
- **Emergency changes** (POL-11.09; controls CM-07). *Applies when:* Scaleup and Enterprise. Always included.  
  Emergency changes may skip normal approval to restore service, and are reviewed and approved afterwards.
- **Customer-specific changes** (POL-11.12; controls CM-10). *Applies when:* All stages, when Service standardisation is Customised / managed.  
  Customer-specific configurations and changes are requested, approved by the customer and tracked.
- **Security design review** (POL-11.13; controls CM-11). *Applies when:* Enterprise only. Always included.  
  Significant new features and architecture changes get a security design review.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Walk me through how a change gets to production. Can anyone deploy on their own? What happens when something urgent needs fixing at night?

Profile fields to draw on: Change management, Release Frequency, Code Repository, Build and Deployment / CI/CD, Infrastructure Configuration, Ticketing, Service standardisation.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
