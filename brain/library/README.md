# Library method

How the library becomes a company's program. `tools/scope.py` applies these rules to `program/context/profile.yaml`.

## Control scoping rules

Each row of [controls.csv](controls.csv) carries the rule that brings it into scope. A control is in scope when all of these pass:

1. **Stages.** Blank means every stage. Otherwise Company Stage must be one of the listed stages. An unanswered stage counts as Startup.
2. **Criteria.** Security controls always apply. Availability, Confidentiality, Processing Integrity and Privacy controls apply when Framework Scope names that criterion (for example "SOC 2 Availability").
3. **If / And.** Up to two conditions on profile fields:
   - `in use`: the field has a real answer (not blank, TBC, Unsure or anything starting "None").
   - `not in use`: the field is blank, TBC, Unsure or "None…".
   - `any of`: the answer includes at least one of the values (values separated by `|`).
   - `not any of`: the answer includes none of the values. Unanswered passes.

Where a family has alternatives (for example AC-01A and AC-01B), the rules pick the one that matches how the company works. `{{TOOL}}` in the wording is replaced with the tools named for the field the rule tests.

Policies, policy statements and risks are in scope when at least one linked or treating control is in scope.

## Risk rating

| Score | Likelihood | Impact |
| --- | --- | --- |
| 1 | Rare: not expected in the next few years. | Minimal: little effect on customers or operations. |
| 2 | Unlikely: could happen in the next few years. | Minor: brief disruption, or a small exposure of internal data. |
| 3 | Possible: could happen in the next year. | Moderate: disruption customers notice, or exposure of limited confidential data. |
| 4 | Likely: expected in the next year. | Major: breach of customer data, a missed commitment or a regulator notice. |
| 5 | Almost certain: happening now or expected within months. | Severe: large breach, extended outage, or a threat to the business. |

Score = likelihood × impact, from 1 to 25. Inherent is the rating before controls; residual is what remains once controls operate. Scores are coloured by band: Low, Medium, High, Critical. Anything above the appetite needs a treatment plan, and management accepts the residual risk.

| Band | From score |
| --- | --- |
| Medium | 5 |
| High | 10 |
| Critical | 20 |

Below Medium is Low. Management sets the bands and the risk appetite; record changes in the Audit trail.

## Vendor tiers

See [vendor-tiers.csv](vendor-tiers.csv) for the checks before onboarding and at each review, and [vendor-categories.csv](vendor-categories.csv) for where vendors are usually found.

## Policy documents

Light depth builds the 15 policies from [policies.csv](policies.csv) and [policy-statements.csv](policy-statements.csv). Detailed depth uses [policy-documents.csv](policy-documents.csv). Both follow these conventions:

Every document, in this order. Title and purpose (one or two sentences; no background or definitions unless a statement calls for them) · Revision history (table: Version | Updated by | Summary | Revision date; first row V1, the owner, 'First version created', the date; one row per approved change, with approval recorded in the register above, not here) · Responsibilities (the Accountable role owns revision, updates, communication and compliance; the Responsible role monitors, enforces and handles breaches, security concerns and questions; all employees, and contractors with system access, read, acknowledge and follow it and report concerns; name roles, not people, and if one person holds both roles print the role once) · the document's sections, in the order on its row · Policy compliance (optional: compliance is mandatory and non-compliance may lead to disciplinary action, including termination; usually printed in the Access Control, Network Security and Asset Management policies, where elsewhere the Code of Conduct covers it) · Exemptions (approval from the owner or the responsible role; at Enterprise stage also risk-assessed, time-limited and tracked to closure, GV-09).



Writing. One short paragraph, list or table per statement, in plain language, using the client's real tool, role and product names. Name other policies by their exact title, and only when they are in scope too. Under 100 staff, keep each document to the in-scope statements, tightly worded. Where a section says 'Options', use the items that are true for the client and drop the rest. Tables named in Sections and tables are built, not described. Acknowledgement is at hire and annually (GV-06).



Roles. Accountable and Responsible resolve to the people in Team Details: Governance Lead, Technical Lead and Compliance Owner directly. Security lead is the Technical Lead until one is named in Key Parties (control GV-07 expects a named security lead from Scaleup stage). Operations lead is the document's owner. People lead is the Governance Lead. Engineering lead is the Technical Lead. Privacy officer is the Compliance Owner, after asking whether a Data Protection Officer is required. Emergency Response Team default: Governance Lead as decision maker, Technical Lead as technical lead, Operations lead as customer communication lead; ask for members and contact numbers and never invent a number. Board: ask whether there is one; if not, name who oversees leadership. Stop and ask if no one holds a role.

Defaults to confirm are in [settings-to-confirm.csv](settings-to-confirm.csv); law and standard summaries in [requirement-lines.csv](requirement-lines.csv) and [privacy-obligations.csv](privacy-obligations.csv). Laws change: check a requirement line before anyone relies on it (AI Guidance 6.7).
