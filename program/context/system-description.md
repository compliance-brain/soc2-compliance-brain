# System description

> [!NOTE]
> **🧭 Guide.** The narrative of your SOC 2 report: who you are, what the service does, the data it handles, what you commit to and where the system boundary sits. These fields flow straight into the report, so keep to plain, factual statements about what exists today. Draft each one with the matching prompt in [brain/prompts/system-description.md](../../brain/prompts/system-description.md), using your profile and public sources.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI drafts each section once Company Name and Domain are in the profile, adding the source after each fact, for example `[Source: https://example.com/terms]` or `[Source: profile.yaml]`. Where a fact needs a document that isn't public, leave a placeholder such as `{{requires SLA to complete}}`. 👤 The Compliance Owner reviews and approves before anything goes to the auditor.

## Company description

`{{2 to 4 sentences: legal and trading name, year founded, headquarters, what the company does, and the industries and customer types it serves.}}`

## Service description

`{{What the service does and how it is delivered.}}`

## Data collected

`{{The data handled, where it lives and how long it is kept.}}`

## Principal service commitments and system requirements

`{{What you commit to customers in contracts, terms and SLAs, and the system requirements that support those commitments.}}`

## Boundaries of the system

`{{What is in and out of scope: infrastructure, software, people, procedures and data, plus subservice organisations and whether they are carved out.}}`

## Complementary user entity controls (CUECs)

Tick the responsibilities your customers carry, then copy each one's report wording from [cuecs.csv](../../brain/library/cuecs.csv) into the list below the checklist. "Typically applies when" is a guide, not a rule.

| Applies | CUEC | Typically applies when |
| --- | --- | --- |
| [ ] | User access administration | Customers create and manage their own user accounts or roles in the product. |
| [ ] | User access reviews | Customer admins can grant roles or elevated permissions. |
| [ ] | Authentication settings | Customers can configure MFA, password rules or session settings. |
| [ ] | Single sign-on and provisioning | Customers connect their own identity provider (SAML/OIDC single sign-on or SCIM). |
| [ ] | Credential security | Most services with named user logins. |
| [ ] | API keys and endpoints | The service offers APIs, webhooks or access tokens that customers configure. |
| [ ] | Third-party integrations | Customers can connect third-party apps, plug-ins or marketplace integrations. |
| [ ] | Data accuracy and completeness | Customers upload, import or send data that the service processes or reports on. |
| [ ] | Appropriate data submitted | The service is not designed for certain sensitive data (e.g. card or health data). |
| [ ] | Sharing and permission settings | Customers can share content, create public links or invite external users. |
| [ ] | Data retention, export and deletion | Customers control retention settings or request data export or deletion. |
| [ ] | Customer-managed encryption keys | The service supports bring-your-own-key or customer-held encryption keys. |
| [ ] | Personal data and privacy obligations | Customers submit personal data about their own staff, customers or end users. |
| [ ] | Data held outside the service | Customers export, download or sync data to their own environments. |
| [ ] | Incident notification | Nearly all services. |
| [ ] | Activity and audit log review | Customers can view audit logs, login history or admin activity. |
| [ ] | User devices and networks | Users access the service from customer-managed devices and networks. |
| [ ] | Network connections and allowlists | Customers set up VPNs, private links, firewall rules or IP allowlists to connect. |
| [ ] | Customer-hosted components | Customers install agents, connectors, SDKs, desktop or mobile apps, or self-hosted components. |
| [ ] | On-site equipment | The company deploys devices or hardware at customer premises. |
| [ ] | Customer configuration changes | Customers build their own workflows, rules, automations or configurations in the product. |
| [ ] | Business continuity planning | Customers rely on the service for business-critical operations. |
| [ ] | Acceptable use | Most services. |
| [ ] | Contacts and service notices | Most services. |
| [ ] | AI output review | The product generates text, code, images, summaries or recommendations using AI. |
| [ ] | Human oversight of AI decisions | AI outputs inform decisions about people, money, safety or compliance. |
| [ ] | AI agent permissions | AI agents can take actions or access connected systems on a user's behalf. |
| [ ] | Data entered into AI features | Users can enter prompts, free text or files into AI features. |
| [ ] | AI settings and data use | Customers can enable or disable AI features, or opt in or out of data use for model improvement. |
| [ ] | Training and grounding data | Customers fine-tune models or connect their own documents or knowledge bases to ground AI responses. |
| [ ] | Appropriate AI use and compliance | Customers use AI features in regulated or higher-risk use cases. |
| [ ] | AI disclosure to end users | Customers expose AI chat, agents or AI-generated content to their own customers. |
| [ ] | AI-generated code and configuration | The product generates code, scripts, queries or infrastructure configuration. |
| [ ] | Customer-supplied AI provider accounts | Customers connect their own AI provider accounts or API keys (e.g. OpenAI, Azure OpenAI, Amazon Bedrock). |
| [ ] | Reporting AI issues | The product includes AI features. |

### CUECs that apply

`{{Report wording for each CUEC ticked above.}}`

## Significant incidents and changes

Significant incidents and system changes in the last 12 months. The report must disclose them.

| What happened | When | Impact and response | Type |
| --- | --- | --- | --- |
|  |  |  |  |

> [!WARNING]
> **✅ Confirm.** Reviewed and approved by `{{Compliance Owner}}` on `{{date}}`.
