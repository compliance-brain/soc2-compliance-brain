# Incident response plan

> [!NOTE]
> **🧭 Guide.** Controls IR-01, IR-02B, IR-03 and IR-04 (plus PR-07 when Privacy is in scope). The steps to follow when something goes wrong. Log every incident in [requests-and-tickets.csv](../records/requests-and-tickets.csv) with Type set to Incident, and use the [incident record](../templates/incident-record.md).

> [!WARNING]
> **✅ Confirm before approval.**
>
> - [ ] `{{Confirm: notification duties and deadlines under the laws and contracts that apply to you, with counsel}}`

## First hour

- [ ] **Log it.** Note when you found out: notification deadlines run from then.
- [ ] **Put people first.** If anyone may be at risk of harm, deal with that first.
- [ ] **Contain it.** Remove access, issue new secrets, roll back or switch off a feature.
- [ ] **Keep the evidence.** Don't delete anything; export logs before they expire.
- [ ] **Set the severity** and decide who to involve, such as counsel or the provider's support.

## Severity

| Severity | Examples | Response |
| --- | --- | --- |
| Critical | Confirmed exposure of customer data; production down for everyone | Work on it until contained |
| High | Suspected exposure; a leaked production secret; a major feature down | Start immediately; contain the same day |
| Medium | A limited outage; a phishing link clicked with no details entered | Within 1 business day |
| Low | Spam, blocked attacks, minor faults | Log and close |

## Contacts

| Who | For | How |
| --- | --- | --- |
| `{{incident lead: CTO}}` | Leads the response | `{{contact: phone and Slack}}` |
| `{{backup lead: Lead Engineer}}` | Leads if the incident lead is unavailable | `{{contact}}` |
| `{{legal counsel: external privacy lawyer}}` | Breach assessment and notices | `{{contact}}` |
| `{{cloud provider: Amazon Web Services}}` support | Provider-side incidents | `{{support plan and link}}` |

## Who has to be told

`{{List each law and contract that applies, who must be told and by when. Typical examples: GDPR (supervisory authority within 72 hours), HIPAA (a business associate tells the healthcare customer within 60 days), Australia's Notifiable Data Breaches scheme, US state breach laws, and customer contracts. Confirm with counsel.}}`

## Closing an incident

Record the root cause and actions with owners, update the risk register if needed, and have the incident lead review it before closing.

## Testing

A tabletop exercise every year (IR-04), recorded in the activity log.
