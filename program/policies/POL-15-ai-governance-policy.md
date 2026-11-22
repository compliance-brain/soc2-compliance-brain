# AI Governance Policy

<!-- policy: POL-15 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** Sets out how AI tools, AI features and AI agents are approved, used, tested and monitored. Linked controls: AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, AI-08, AI-09, AI-10, AI-11, AI-12, AI-13, AI-14, AI-15, AI-16, AI-17, AI-18, AI-19, GV-13. Keep only the statements whose controls are in scope (run `python3 tools/scope.py`), one short paragraph each (AI Guidance 4.2 and 6.2). Delete this box once adapted.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each statement from the profile fields named under it (AI Models and Platforms, AI reliance, Responsibility for outcomes, Control execution, Data Handled). 👤 The owner answers: Which AI tools does the team use day to day? Does the product use AI, and who checks its output? Do any agents take actions on their own?

> [!WARNING]
> **✅ Confirm before approval.** Check each default with its owner and use your real practice where it meets the requirement (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Provider terms (default: No training on customer data)}}`
> - [ ] `{{Confirm: Agent inventory, owner and risk (default: Reviewed when agents change and at least annually)}}`
> - [ ] `{{Confirm: Agent access (default: Reviewed quarterly with user access)}}`

## Purpose

Sets out how AI tools, AI features and AI agents are approved, used, tested and monitored.

## Scope

AI tools used by staff, AI features in the product, and AI agents acting for the company.

## Policy statements

### Inventory and approval

AI tools, models and agents are approved before use and recorded with their owner and the data they can access.

<sub>POL-15.01 · Controls: AI-01 · Tailor using: AI Models and Platforms</sub>

### Acceptable use

Staff follow the AI rules in the acceptable use policy and enter data into each AI tool only as far as that tool is approved.

<sub>POL-15.02 · Controls: AI-02 · Tailor using: Data Handled</sub>

### Provider terms

AI providers' terms are checked for training on customer data, retention and data location before customer data is sent to them.

<sub>POL-15.03 · Controls: AI-03 · Tailor using: AI Models and Platforms</sub>

### Evaluation before release

AI features are evaluated for accuracy, safety and bias before release and after significant model changes.

<sub>POL-15.04 · Controls: AI-04 · Tailor using: AI reliance, Responsibility for outcomes</sub>

### Monitoring in production

AI features in production are monitored for errors, harmful output and drift, and customers can report issues.

<sub>POL-15.05 · Controls: AI-05 · Tailor using: AI reliance</sub>

### Agent authority and boundaries

AI agents act only within defined permissions and boundaries. Consequential actions need human approval or can be reversed, and the boundaries are re-approved when an agent's capabilities change. Each agent-run control has a named person accountable for it.

<sub>POL-15.06 · Controls: AI-06, GV-13 · Tailor using: AI reliance, Control execution</sub>

### Agent inventory, owner and risk

Each AI agent operating in production is recorded with its purpose, scope, boundaries and the systems and data it can reach, has a named accountable owner who monitors it and can restrict or stop it, and is risk-assessed before go-live and when it changes.

<sub>POL-15.07 · Controls: AI-07, AI-08, AI-09 · Tailor using: AI reliance, AI Models and Platforms, Key Parties</sub>

### Agent access

Each agent has its own identity, with least-privilege permissions approved before they are granted and included in access reviews. Elevated or emergency access for an agent is approved, time-bound, logged and reviewed after use.

<sub>POL-15.08 · Controls: AI-10, AI-11, AI-12 · Tailor using: Identity and Authentication, Privileged Access Management, Access ownership</sub>

### Agent-made changes

Changes written with AI assistance are reviewed, tested and deployed by a person through the change process. Where an agent deploys or remediates on its own, each change is authorised by risk, tested, reviewed afterwards, alerted to the owner and reversible by rollback.

<sub>POL-15.09 · Controls: AI-13, AI-14, AI-18 · Tailor using: Change management, Build and Deployment / CI/CD, AI reliance</sub>

### Agent monitoring and incident authority

Agent actions are logged against the agent's identity, and actions outside its boundaries alert the owner. Where an agent monitors systems or triages incidents, its authority, escalation points and human review are defined, and customer notifications it drafts are approved before release.

<sub>POL-15.10 · Controls: AI-16, AI-17, AI-19 · Tailor using: Audit Logging, Incident response, Status Page</sub>

### Customer-directed agent changes

Where customers direct or approve an agent's changes, the split of responsibilities is defined and communicated as customer responsibilities (CUECs), and the agent records who directed each change.

<sub>POL-15.11 · Controls: AI-15 · Tailor using: Customer administration, Service standardisation</sub>

## Exceptions

Exceptions to this policy are approved by `{{approver}}`, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
