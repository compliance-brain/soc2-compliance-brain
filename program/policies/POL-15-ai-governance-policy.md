# AI Governance Policy

<!-- policy: POL-15 | status: Draft | version: V1 | owner: {{owner}} | approved-by: | approved-on: | staff-must-acknowledge: no -->

> [!NOTE]
> **🧭 Guide.** A first draft for the reference company, a 10-person SaaS ([profile](../context/profile.yaml)). `{{label: example}}` values are the reference company's answers: replace them with yours. The statements below are the library statements in scope for that company; **Add if your setup differs** lists the rest and when each applies. Keep each statement short (AI Guidance 4.2 and 6.2), and delete this box once adapted.

> [!WARNING]
> **✅ Confirm before approval.** Each default below is written into a statement. Keep it, change it to your real practice where that meets the requirement, or agree a fix (AI Guidance 5.6 and 9.4).
>
> - [ ] `{{Confirm: Provider terms (POL-15.03): No training on customer data}}`

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

### Agent authority and boundaries

AI agents act only within defined permissions and boundaries. Consequential actions need human approval or can be reversed, and the boundaries are re-approved when an agent's capabilities change. Each agent-run control has a named person accountable for it.

<sub>POL-15.06 · Controls: GV-13 · Tailor using: AI reliance, Control execution</sub>

### Agent-made changes

Changes written with AI assistance are reviewed, tested and deployed by a person through the change process. Where an agent deploys or remediates on its own, each change is authorised by risk, tested, reviewed afterwards, alerted to the owner and reversible by rollback.

<sub>POL-15.09 · Controls: AI-13 · Tailor using: Change management, Build and Deployment / CI/CD, AI reliance</sub>

## Add if your setup differs

<details>
<summary>6 more library statements, and when each applies</summary>

- **Evaluation before release** (POL-15.04; controls AI-04). *Applies when:* All stages, when AI reliance is Assistive, AI-native or Agentic.  
  AI features are evaluated for accuracy, safety and bias before release and after significant model changes.
- **Monitoring in production** (POL-15.05; controls AI-05). *Applies when:* All stages, when AI reliance is AI-native or Agentic.  
  AI features in production are monitored for errors, harmful output and drift, and customers can report issues.
- **Agent inventory, owner and risk** (POL-15.07; controls AI-07, AI-08, AI-09). *Applies when:* All stages, when AI reliance is Agentic.  
  Each AI agent operating in production is recorded with its purpose, scope, boundaries and the systems and data it can reach, has a named accountable owner who monitors it and can restrict or stop it, and is risk-assessed before go-live and when it changes.
- **Agent access** (POL-15.08; controls AI-10, AI-11, AI-12). *Applies when:* All stages, when AI reliance is Agentic.  
  Each agent has its own identity, with least-privilege permissions approved before they are granted and included in access reviews. Elevated or emergency access for an agent is approved, time-bound, logged and reviewed after use.
- **Agent monitoring and incident authority** (POL-15.10; controls AI-16, AI-17, AI-19). *Applies when:* All stages, when AI reliance is Agentic.  
  Agent actions are logged against the agent's identity, and actions outside its boundaries alert the owner. Where an agent monitors systems or triages incidents, its authority, escalation points and human review are defined, and customer notifications it drafts are approved before release.
- **Customer-directed agent changes** (POL-15.11; controls AI-15). *Applies when:* All stages, when AI reliance is Agentic.  
  Where customers direct or approve an agent's changes, the split of responsibilities is defined and communicated as customer responsibilities (CUECs), and the agent records who directed each change.

</details>

<details>
<summary>Questions to adapt this policy</summary>

Ask the owner: Which AI tools does the team use day to day? Does the product use AI, and who checks its output? Do any agents take actions on their own?

Profile fields to draw on: AI Models and Platforms, AI reliance, Responsibility for outcomes, Control execution, Data Handled.

</details>

## Exceptions

Exceptions to this policy are approved by {{approver: CTO}}, recorded in [requests-and-tickets.csv](../records/requests-and-tickets.csv) as an Exception, and reviewed at the next management review.

## Revision history

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| V1 | `{{date}}` | First version | `{{name}}` |
