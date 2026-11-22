# Records

> [!NOTE]
> **🧭 Guide.** Records accumulate as the program runs, and they're what an auditor samples from. Add rows at the bottom. Record what actually happened, when and by whom; never back-date a record. Keep the fewest records that cover your in-scope controls, and combine where you can (AI Guidance 10.1).

| File | What goes in it | Key values |
| --- | --- | --- |
| [audit-trail.csv](audit-trail.csv) | Every meaningful change to the program, and who or what made it | Actor type: `Person`, `AI agent`, `AI drafted and person approved`. Action: `Created`, `Updated`, `Approved`, `Decision`, `Evidence added`, `Configuration change`, `Correction`, `Context review` |
| [activity-log.csv](activity-log.csv) | Each time a recurring control operates: access reviews, training, restore tests, management reviews | One row per occurrence, with its evidence link and next due date |
| [requests-and-tickets.csv](requests-and-tickets.csv) | Access requests and removals, changes, privacy requests, incidents and exceptions | Type: `Access request`, `Access removal`, `Change`, `Privacy request`, `Incident`, `Exception`, `Other`. Status: `Open`, `In progress`, `Done`, `Rejected` |
| [sign-off-log.csv](sign-off-log.csv) | Decisions by management | Decision type: `Policy approval`, `Risk acceptance`, `Vendor approval`, `Management review`, `Risk register review`, `Vendor register review`, `Context review` |
| [policy-acknowledgements.csv](policy-acknowledgements.csv) | Staff acknowledging policies | Reason: `Joining`, `Annual`, `Material change` |

## Audit trail and git history

The audit trail is the readable story of the program; git history is the tamper-evident record underneath it. Use both:

- One audit trail row and one commit per block of work, with matching wording.
- Work done by an AI agent gets a reviewer in "Reviewed by" once a person has checked it.
- Don't edit past audit trail or sign-off rows. If one is wrong, add a `Correction` row that names the original, such as "AUDT-3".
- Number entries in order: AUDT-1, AUDT-2 and so on. Tickets use TKT-1, TKT-2.

If your ticketing lives in another tool (Jira, Linear, GitHub Issues), link to it from the Link column rather than copying it here.
