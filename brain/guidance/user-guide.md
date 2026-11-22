# User Guide

What each Compliance Brain field means, and how it shapes your compliance. The fields themselves live in [program/context/profile.yaml](../../program/context/profile.yaml).

> [!NOTE]
> This guide is shared with the Google Sheets edition, so it mentions tabs. The [table at the top of the AI Guidance](ai-guidance.md#reading-this-guidance-in-the-repository) shows where each one lives in this repository.

## Start here

*How the Compliance Brain works, and how to get the most from it.*

**What this is**

AI already knows compliance: the frameworks, the risks, the controls and how auditors test them. What it doesn't know is your context. This file gives your AI that context, along with the guardrails and structure to run compliance for you. Load it into your AI, then work in chat: your AI updates the sheet with what it knows and asks you for the rest.

**Your agent**

At the top of the Compliance Brain tab you'll find how to get started and a starter instruction to paste into your AI. You can also choose the agent's role (Compliance Manager, Analyst or Expert), where you'll work with it and the principles it follows. What it can reach and do is set with your AI provider, and it asks before anything irreversible or anything that leaves the company.

**Your workbook**

- Start here – an overview of the file, the two tabs you use, and live counts across your program.
- Compliance Brain – how to get started, where your program lives, your agent setup and your context. You use this tab.
- Audit Trail – a high-level record of the work your agent has completed. You review this tab.
- System Description – the narrative sections of your report, the controls your customers are responsible for (CUECs), and a log of significant incidents and changes. Drafted from your brain.
- Controls – your control framework, pulled directly from the Control Library and tailored to you.
- User Guide – this page: what each field means and how it shapes your compliance.
- Hidden reference library (View > Hidden sheets) – AI Guidance, Policies, Risks, Vendors, Control Library, AI Prompts and Brain Lists. Your agent reads these: the guardrails it follows, and the structure and blueprints it uses to build your policies, registers and controls. Finished policies are reviewed and approved where they're built, in your program home.

**How each answer is used**

Every field feeds one or more of five lenses:
- Scope – what's in and out of the report, and which criteria and frameworks apply.
- Risk – what could go wrong for you and your customers, and how much rigour is needed.
- Controls – which controls you need, and how they're worded to match your workflows.
- Evidence – where proof lives (source systems, tickets, logs) and how it's collected.
- Commitments – what you promise customers, and what they're responsible for in return.

**Compliance shapes**

Shapes describe how you actually operate, as a position on a spectrum: centralised or distributed access, standing or just-in-time production access, and so on. There's no right or wrong position. The agent designs controls to fit your shape instead of forcing a generic template, so pick the closest match for how things work today. Choose Unsure or TBC when you're not sure, and revisit them as you change.

**It evolves with you**

You don't need everything upfront. Once the H fields are in, your agent can get going. Every answer you add makes it more capable: controls that fit better, evidence pulled from the right places and fewer questions back to you. When something changes, tell your agent and it updates the file.

**Answering well**

- Describe how things work today, not how you'd like them to work. Plans and intentions go in notes.
- Choose 'None / not used' when something doesn't apply, and 'TBC' when you're not sure yet. Avoid blanks.
- Use real product names (Okta, GitHub, AWS). They appear in control wording and the report.
- Missing a tool? Add it to the bottom of its column on the Brain Lists tab (hidden: View > Hidden sheets) and it appears in the dropdown.
- Multi-select fields accept several answers. Choose everything genuinely in use.

**Impact key**

H – High impact: the agent relies on these most. Start here.
M – Medium impact: sharpens control wording and the evidence plan.
L – Low impact: useful detail. Fill in when it applies.

## Your compliance agent

*Set up at the top of the Compliance Brain tab. These choices set what your agent does for you and how it works with you.*

## Agent role     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

The job you want the agent to do for you.

**Options**

- Compliance Manager (executor) – runs the programme day to day: implements and operates controls, collects evidence, follows up with owners and keeps you audit-ready.
- Compliance Analyst (assessor, drafter and guide) – assesses your environment, drafts policies, controls and evidence requests, and tells you what to do next. Your team executes.
- Compliance Expert (educator and advisor) – explains requirements, answers questions and reviews your work. Your team does the work.

**Choosing a role**

Compliance Manager is recommended once you're comfortable with the agent acting for you, as it saves the most time. If you'd rather review everything first, start as Analyst and move up as trust builds. Expert suits teams that want to do the work themselves with expert guidance on hand.

**Who stays accountable**

Whatever the role, your management stays responsible for your controls, your system description and your decisions. The agent works for you, within the guardrails you set.

## Where you'll use it     Compliance Brain  ·  Multi-select  ·  High impact

**What it captures**

Where you'll work with the agent day to day.

**Options**

- Slack – the agent works in your channels: answering questions, nudging owners and sharing updates.
- Agentic platform – the agent runs multi-step work with connected tools, such as Claude Cowork or a similar agent workspace.
- Browser agent – the agent works inside web apps you're signed in to, to gather evidence or check settings.
- Chat interface – you bring questions and documents to the agent; it can't act on its own.

**Tips**

Choose all that apply. Many teams use an agent platform for the heavy lifting and Slack for updates and approvals.

## Design principles     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

How the agent should approach your compliance programme.

**Defaults**

Pre-selected to reflect a lean, engineering-led model: Minimise manual controls; prefer existing workflows; no new tools unless necessary; avoid standing production access; evidence from source systems; keep policies concise; no committees just for compliance; engineering owns technical controls; optimise for enterprise customer trust.

**Tips**

Remove any that don't fit. To add your own, type it at the bottom of the Design principles list on the Brain Lists tab (hidden: View > Hidden sheets), then select it.

## Point of contact     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

The person the agent reports to and asks for approvals.

**Tips**

Name, role and best channel, e.g. Jane Doe, CTO – Slack #compliance.

## Check-in rhythm     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

How often the agent updates you on progress, open questions and anything waiting on your approval.

## Company & team

*Who you are, the scope of your compliance program, and who leads it.*

## Company Name     Compliance Brain  ·  Text  ·  High impact

**What it captures**

Your company's legal entity name, as it will appear on the SOC 2 report.

**Why it matters**

The report is issued for a specific legal entity. Using a trading name instead can create confusion in customer contracts and reviews.

**Day to day**

Together with Domain, it unlocks the AI Draft Status so the system description can be drafted.

**Tips**

Check it against the company register and the entity named in your customer contracts.

## Domain     Compliance Brain  ·  Text  ·  High impact

**What it captures**

The main website for the company or product, e.g. acme.com.

**Why it matters**

The AI drafting fields research this domain (home, product, trust and legal pages) to produce a first draft of the company description, service description, commitments and boundaries.

**Customer commitments**

Published terms, privacy policy, SLA and trust pages are commitments to customers. The report needs to be consistent with them.

**Tips**

Use the domain customers sign up on. If the product runs on a separate domain (e.g. app.acme.io), mention it in Product/Service Scope.

## Framework Scope     Compliance Brain  ·  Multi-select  ·  High impact

**What it captures**

The frameworks in scope, such as SOC 2, ISO/IEC 27001 or HIPAA. For SOC 2, pick each Trust Services Criteria category covered: Security (always included), plus optionally Availability, Confidentiality, Processing Integrity and Privacy.

**Controls**

Each category adds criteria and controls. Availability adds capacity, backup and disaster recovery controls; Confidentiality adds classification, retention and disposal controls.

**Customer commitments**

Choose categories that match what customers rely on you for. Uptime commitments point to Availability; confidentiality clauses point to Confidentiality.

**How auditors test**

Every criterion in each selected category is tested, so each category added means more controls and more evidence.

**Tips**

Most first reports start with Security, adding Availability or Confidentiality when customers ask for them.

## Report Type     Compliance Brain  ·  Text  ·  Low impact

**What it captures**

Type 1 (control design at a point in time) or Type 2 (operating effectiveness over a period, usually 3–12 months).

**Evidence**

A Type 1 needs evidence that controls exist and are designed well on one date. A Type 2 needs evidence that each control operated throughout the period: every quarterly access review, every change approval.

**Customer commitments**

Enterprise buyers usually expect a Type 2. A Type 1 can bridge the gap while the Type 2 period runs.

**How auditors test**

For a Type 2, auditors sample from populations across the whole period, so a gap in any month can become an exception.

## Audit Period     Compliance Brain  ·  Text  ·  Low impact

**What it captures**

The period your report covers: a date range for a Type 2 (e.g. 1 Jan 2026 – 30 Jun 2026), or the as-of date for a Type 1.

**Evidence**

Evidence must come from within the period. The agent uses it to plan collection and check that evidence covers the whole window.

## Terms of Service     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

A link to your online terms of service, if you have them.

**Customer commitments**

Your terms set out what you promise customers: uptime, support, security, and data return and deletion. The agent reads them so your controls and system description match what you've committed to.

## Privacy Policy     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

A link to your online privacy policy, if you have one.

**Customer commitments**

Describes the data you handle, your sub-processors, and where and how long data is kept. The agent uses it for data handling, vendors and regulatory drivers.

## Governance Lead     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

The person who owns governance and business risk – often the CEO, CFO or COO. Name and title.

**Day to day**

Typically approves policies, risk decisions and vendor choices, and the management assertion for the report.

## Technical Lead     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

The person who owns systems and engineering – often the CTO, CISO, CPO or Head of Engineering. Name and title.

**Day to day**

Owns most technical controls – access, change management, infrastructure and monitoring – and the evidence that comes from those systems.

## Compliance Owner     Compliance Brain  ·  Text  ·  High impact

**What it captures**

The person accountable for the compliance program – often the governance or technical lead. Name and title.

**Day to day**

The agent's main contact: approves changes, answers open questions, reviews anything going to auditors and keeps the program on track.

## Key Parties     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

Other people involved in the program – material control owners and interested parties – with their role or title and how they are involved, at a high level.

**Tips**

One line each, e.g. Jane Doe, Head of People – onboarding, offboarding and training. The agent routes evidence requests and reminders to them.

## Company context

*The business context that sets scope, risk and how formal your controls need to be.*

## Service Type     Compliance Brain  ·  Multi-select  ·  High impact

**What it captures**

The kind of service in scope: SaaS, platform or API, managed service, devices or hardware, professional services.

**Scope**

Defines what the system is and where its boundaries sit.

**Controls**

Different services carry different controls. Hardware adds supply chain and device controls; managed services add controls over access to customer environments.

**Customer commitments**

Determines which complementary user entity controls (CUECs) apply to your customers.

**How auditors test**

Auditors confirm the service description matches what customers actually receive.

## Target Timeline     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

When you need the report, which sets the audit window and how long you have to get ready.

**Risks**

Compressed timelines are the most common cause of exceptions. Controls that start late don't build enough operating history for a Type 2.

**Controls**

Short runways favour automated controls you can switch on quickly, and often a Type 1 first.

**Evidence**

For a Type 2, evidence must exist from the first day of the period, so collection should start before the window opens.

**Customer commitments**

Often driven by a deal or renewal date. Align the report date with what customers have been told.

**Tips**

Work backwards: report date → period end → period start → controls live and evidenced.

## Headcount     Compliance Brain  ·  Number  ·  Medium impact

**What it captures**

Total employees and contractors with access to company systems.

**Risks**

People are the largest attack surface. More people means more joiners, leavers and access to manage.

**Controls**

Scales HR and access controls: background checks, onboarding, security training, access reviews and offboarding.

**Evidence**

HRIS and identity provider records become the populations auditors sample from.

**How auditors test**

Sample sizes depend on population size. Small teams may see every instance tested.

**Tips**

Include contractors with system access. They're in scope for people controls too.

## Company Stage     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

Where the company is on its journey, from early stage to established.

**Controls**

Calibrates formality. Early-stage companies can rely on lean, automated controls and direct leadership oversight; later stages need more defined ownership, cadence and segregation of duties.

**Risks**

The risk isn't being small. It's controls that don't match how the company actually works.

**Day to day**

The agent avoids introducing committees or heavy process that don't fit your stage.

## Country/Region(s)     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Where the company is registered, operates and employs staff or contractors.

**Risks**

Each jurisdiction brings its own privacy, employment and data-transfer laws.

**Controls**

Affects background check practices, privacy controls and where data may be stored or accessed from.

**Evidence**

Distributed teams often mean evidence from several HR, payroll or employer-of-record providers.

**Tips**

Include countries with contractors or offshore teams who can access production.

## Facilities     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Physical locations: offices, co-working spaces, data centres, or fully remote.

**Scope**

Sites that house systems or sensitive data are in scope for physical security.

**Controls**

Offices with infrastructure add badge access, visitor logs and CCTV controls. Cloud-only and remote teams rely on the cloud provider's SOC report for physical security.

**Evidence**

Badge system reports and visitor logs, or the provider's SOC 2 report.

**Tips**

A co-working desk with no servers adds little. An office with network equipment or stored records adds more.

## Customer Types     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Who you sell to: SMB, mid-market, enterprise, government, regulated industries, consumers.

**Risks**

Larger and regulated customers raise the impact of a breach or outage.

**Customer commitments**

Enterprise and regulated customers negotiate stronger terms (security addenda, right to audit, notification timeframes) that controls must support.

**Day to day**

Expect more security questionnaires. The report and your trust materials answer most of them.

**Tips**

Select the segments you sell to today and those this report is meant to unlock.

## Customer Geography     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Where your customers and their end users are located.

**Risks**

Serving EU, UK or Australian customers can bring GDPR, UK GDPR or Privacy Act obligations even if you're based elsewhere.

**Customer commitments**

Customers may require data residency, approved transfer mechanisms or local breach notification.

**Controls**

Can add privacy, data residency and cross-border transfer controls.

## Data Handled     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

The kinds of data your service holds or processes, at a high level: customer content, personal data, health data, payment card data, financial data, and credentials and secrets.

**Scope**

Confidential customer data points to the Confidentiality category; personal data points to Privacy. Health or payment card data brings obligations such as HIPAA or PCI DSS into view.

**Controls**

Sets how data is classified, encrypted, retained and deleted, and how tightly access to it is controlled.

**Tips**

Choose every category the service holds, even in small amounts. Choose Minimal / no customer data only if the service doesn't store customer data at all.

## Service Commitments     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

What you promise customers in contracts, SLAs and terms: uptime, support response, recovery times, breach notification, and data return and deletion.

**Customer commitments**

SOC 2 reports describe your principal service commitments, and auditors test controls against them. Your agent turns these into the commitments section of the system description.

**Controls**

Sets the targets controls are built to: recovery objectives, backup restore testing, incident notification windows and deletion timeframes.

**Tips**

Paste the relevant clauses from your standard contract, SLA or DPA, or add links. The AI drafting fields already research the published terms on your Domain, so focus on what's only in contracts. If terms are negotiated per customer, paste the strictest you've agreed.

## Regulatory Drivers     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Laws, regulations and standards beyond SOC 2 that apply to you or your customers, e.g. HIPAA, GDPR, APRA CPS 234.

**Scope**

Some drivers widen scope or suggest additional categories (such as Privacy) or frameworks.

**Controls**

Each driver maps to specific obligations. HIPAA requires business associate agreements and PHI safeguards; CPS 234 requires regulated customers to assess your controls.

**Customer commitments**

Regulated customers pass their obligations down to you through contracts.

**How auditors test**

SOC 2 doesn't certify compliance with these laws, but controls should be consistent with them.

## Subservice Providers     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

Third parties that perform part of your service: cloud hosting, payments, email delivery, AI model providers, support platforms.

**Scope**

Each is either carved out (excluded, relying on their own controls) or included (the inclusive method). Most reports carve out.

**Controls**

Vendor management controls: reviewing their SOC reports and performing the complementary controls they expect of you.

**Evidence**

Their SOC 2 reports, your documented review of each, contracts and DPAs.

**Customer commitments**

The report lists the controls you rely on each provider to perform (CSOCs), so customers see the full picture.

**How auditors test**

Auditors check you review each provider's report at least annually and address exceptions or coverage gaps.

**Tips**

Include AI model providers if customer data passes through them.

## Operating Cadence     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

The rhythm your leadership meets on to review the business and align the company: ad hoc, weekly, monthly or quarterly.

**Day to day**

Your agent builds management reviews, risk and access reviews, and policy approvals into this rhythm instead of creating new meetings.

**How auditors test**

Auditors look for evidence that leadership oversees security, such as minutes or recorded decisions. A regular rhythm makes that evidence routine.

**Tips**

If teams run different rhythms, pick the one leadership uses to review the business. If it's ad hoc today, monthly is a good rhythm to align around.

## Release Frequency     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

Roughly how often changes reach production. Pick the closest: multiple times per day, daily, weekly, bi-weekly, monthly, quarterly or annually.

**Controls**

Frequent releases lean on automated pipeline checks and pull request approvals. Infrequent releases suit planned release approvals.

**How auditors test**

Auditors sample changes from the period, so release frequency sets the size of the population they sample from.

**Tips**

Choose N/A if you don't develop or change the software yourselves, for example a professional service or a reseller of another provider's platform.

## Compliance Goals     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Why you're pursuing SOC 2: winning enterprise deals, meeting a customer mandate, entering new markets, improving security or operations.

**Controls**

Shapes priorities. Deal-driven goals favour speed and customer-facing assurance; security goals favour depth.

**Day to day**

Guides how the agent balances effort, rigour and timing, and what it puts first.

**Tips**

Be candid. The goal changes the plan, not the standard.

## Compliance Stage     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Where you are with compliance today: just starting, building, implemented but not yet audited, first audit underway, or audited before.

**Day to day**

Sets where the agent focuses: scoping and building early on, running the rhythm and gathering evidence later, and supporting auditors and renewals once you have been audited.

**Controls**

Early programs start lean with the controls that matter most; mature programs focus on keeping controls operating and evidenced.

**Tips**

Pick the closest option. If you are between stages, choose the earlier one and the agent will confirm as it goes.

## Existing Compliance     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Frameworks and certifications already in place, e.g. ISO 27001, PCI DSS, a HIPAA programme, a prior SOC 2.

**Controls**

Existing controls and policies are reused and mapped rather than rebuilt.

**Evidence**

Prior reports and evidence show what's already operating. Prior exceptions show where to focus.

**How auditors test**

For a returning SOC 2, auditors review prior-period exceptions and follow up on remediation.

## Target Compliance     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Frameworks you plan to add, e.g. ISO 27001, ISO 42001, HIPAA, PCI DSS.

**Controls**

Controls are designed once and mapped across frameworks, so one piece of evidence serves several audits.

**Tips**

Even rough plans help. They avoid redesigning controls later.

## Known Gaps     Compliance Brain  ·  Text  ·  Medium impact

**What it captures**

Weak spots you already know about: exceptions from past audits, findings from assessments or penetration tests, and fixes still open.

**Risks**

Known gaps are the first place auditors look. Each one becomes a risk with an owner and a plan.

**Day to day**

Your agent prioritises these, tracks them to closure and records compensating controls in the meantime.

**Tips**

Be candid. A gap you've found and are fixing is far better than one an auditor finds.

## Planned Changes     Compliance Brain  ·  Text  ·  Low impact

**What it captures**

Major changes expected in the next 12 months: new products or regions, tool migrations, hiring, funding, acquisitions or new frameworks.

**Scope**

New products or regions can widen scope, and significant changes during the audit period are disclosed in the system description.

**Day to day**

Your agent plans ahead: it avoids building controls on tools being retired and lines up evidence for new ones.

**Tips**

A line per change with a rough date is enough, e.g. Move from Heroku to AWS – Q2.

## Penetration Test Status     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

Whether an independent penetration test has been completed, is scheduled, or still needs to be arranged.

**Risks**

Without testing, exploitable weaknesses in the application or infrastructure can go unnoticed.

**Controls**

Supports vulnerability management and risk assessment controls. An annual test is the common expectation.

**Evidence**

The test report or executive summary, plus tickets showing findings were fixed.

**Customer commitments**

One of the most requested documents in customer security reviews.

**How auditors test**

Auditors check the test was done by a qualified independent party within the period, and that high-risk findings were tracked to closure.

## Penetration Test Approach     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How the test is or will be performed: black, grey or white box; AI-performed; human-led; or human-in-the-loop with AI.

**Risks**

Automated-only testing can miss business logic and authorisation flaws.

**Evidence**

The approach shapes how much weight customers and auditors place on the results. Human-led or hybrid testing generally carries more weight.

**Tips**

Match the approach to customer expectations. Enterprise buyers often ask for a human-led or hybrid application test.

## Product/Service Description     Compliance Brain  ·  Text (AI-drafted)  ·  Low impact

**What it captures**

The specific products and services the report covers, in one or two sentences.

**Scope**

Anything not named here is out of scope. Customers read this to check the report covers what they buy.

**How auditors test**

Auditors confirm the description matches reality and that controls cover everything named.

**Tips**

Use the product names customers know. Leave out betas or separate products unless they share the same infrastructure and controls.

## System context

*The tools and platforms in scope. Each one shapes control wording and where evidence lives. Choose 'None / not used' where a category doesn't apply.*

## Infrastructure     Compliance Brain  ·  Multi-select  ·  High impact

**What it captures**

The cloud and network layer the product runs on, e.g. AWS, Google Cloud, Azure or on-premises.

**Risks**

Misconfiguration and unpatched systems are leading causes of breaches.

**Controls**

Anchors hardening, network segmentation, patching, encryption at rest and infrastructure access controls.

**Evidence**

Comes straight from the cloud console, configuration tools and infrastructure-as-code repositories.

**How auditors test**

Auditors inspect configurations (security groups, encryption settings) and sample patching and access.

## Hosting Platform     Compliance Brain  ·  Multi-select  ·  High impact

**What it captures**

Where the application is deployed and served, e.g. Kubernetes, ECS, Vercel, Heroku.

**Scope**

Platform providers are usually subservice organisations. The shared responsibility model sets what you control and what they do.

**Controls**

Deployment access, runtime configuration and separation of environments.

**Evidence**

Platform settings, access lists and the provider's SOC report.

**How auditors test**

Auditors confirm the provider's SOC report covers the period and that you perform the user controls it lists.

## Databases     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Where customer and system data is stored, e.g. PostgreSQL on RDS, MongoDB Atlas, BigQuery.

**Risks**

Databases hold your most sensitive data. Exposure or loss directly affects customers.

**Controls**

Encryption at rest, restricted access, backups and monitoring of privileged activity.

**Evidence**

Encryption and backup settings, database user lists and access logs.

**Customer commitments**

Often tied to contractual commitments on encryption, residency and retention.

**How auditors test**

Auditors inspect encryption settings and test who can access production data.

## Workspace     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

Email, documents and collaboration tools, e.g. Google Workspace, Microsoft 365, Slack.

**Risks**

Sensitive data often lives in documents and chat, not just in production.

**Controls**

External sharing settings, MFA, data retention and admin access.

**Evidence**

Admin console settings and user lists.

**How auditors test**

Auditors inspect key settings such as external sharing and MFA enforcement.

## Compliance Automation     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

A platform that tracks controls and collects evidence, e.g. Vanta, Drata, Secureframe.

**Evidence**

Sets how much evidence is collected automatically and where auditors look first.

**Day to day**

Integrations monitor controls continuously and flag failing tests early.

**How auditors test**

Auditors may use platform reports but still validate the underlying data and the completeness of integrations.

**Tips**

'None / not used' is fine if you manage evidence in shared folders.

## AI Models and Platforms     Compliance Brain  ·  Multi-select  ·  Medium impact

**What it captures**

AI models and services used in the product or by staff, e.g. OpenAI, Anthropic, Amazon Bedrock, Vertex AI.

**Risks**

Customer data may be sent to model providers, outputs can be inaccurate, and agents can take actions in connected systems.

**Controls**

AI governance, vendor review, data-use settings (such as no training on customer data) and output monitoring.

**Evidence**

Provider agreements and data-use settings, a model inventory and your AI policy.

**Customer commitments**

Customers increasingly ask how AI uses their data, often addressed in DPAs and AI terms.

**Scope**

Providers that process customer data may be listed as subservice organisations, and the AI CUECs may apply to customers.

## Backups and Recovery     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How data and systems are backed up and restored: native snapshots, backup services, disaster recovery regions.

**Risks**

Without tested backups, ransomware, accidental deletion or a regional outage can mean permanent data loss.

**Controls**

Backup schedule, retention, encryption, restore testing and disaster recovery planning.

**Evidence**

Backup job logs, retention settings and restore test records.

**Customer commitments**

Supports recovery time and recovery point (RTO/RPO) and availability commitments.

**How auditors test**

Auditors inspect backup configuration and look for a restore test performed during the period.

## Edge and Web Protection     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

CDN, web application firewall, DDoS protection and DNS at the perimeter, e.g. Cloudflare, AWS WAF.

**Risks**

Web attacks and denial of service can expose the application or take it offline.

**Controls**

Network security, TLS enforcement and availability protections.

**Evidence**

WAF rules, TLS settings, and attack and alert logs.

**How auditors test**

Auditors inspect configuration and confirm protections are enabled for production endpoints.

## Identity and Authentication     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

The identity provider staff use to sign in, e.g. Google Workspace, Okta, Microsoft Entra ID.

**Risks**

Compromised credentials are the most common way attackers get in.

**Controls**

Central to single sign-on, MFA enforcement, password policy, provisioning and offboarding.

**Evidence**

User lists, MFA settings, sign-in logs and deprovisioning records. Often the single most-used evidence source.

**How auditors test**

Auditors check MFA is enforced, sample leavers for timely removal, and use user listings for access reviews.

## Password Manager     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How staff store and share credentials, e.g. 1Password, Bitwarden.

**Risks**

Shared or reused passwords spread a single compromise across systems.

**Controls**

Credential management, shared vault access and removal at offboarding.

**Evidence**

Vault policies, admin settings and user lists.

## Application Secrets and Encryption     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where keys, tokens and application secrets are held, e.g. AWS KMS, Secrets Manager, HashiCorp Vault, Doppler.

**Risks**

Secrets left in code or configuration files are a frequent cause of breaches.

**Controls**

Key management, rotation, restricted access and secret scanning.

**Evidence**

KMS and vault configuration, rotation settings and access policies.

**Customer commitments**

Underpins commitments on encryption in transit and at rest.

**How auditors test**

Auditors inspect key policies and check that secrets aren't stored in code repositories.

## Privileged Access Management     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How admin and production access is granted: standing access, just-in-time elevation, or bastion and session tools, e.g. Teleport, StrongDM, AWS IAM Identity Center.

**Risks**

Standing admin access magnifies the impact of a compromised account or a simple mistake.

**Controls**

Least privilege, approval, time-bound elevation and session logging for production access.

**Evidence**

Access requests and approvals, session logs and privileged user lists.

**How auditors test**

Auditors review who holds privileged access and sample elevation requests for approval.

**Tips**

Just-in-time access usually means fewer manual controls and stronger evidence than standing access.

## Device Management     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

The tool that enrols and configures laptops, e.g. Jamf, Kandji, Microsoft Intune.

**Controls**

Enforces disk encryption, screen lock, operating system updates and remote wipe.

**Evidence**

MDM compliance reports are the device control evidence.

**How auditors test**

Auditors sample devices, compare settings to policy and check coverage across all staff devices.

**Tips**

Read alongside Device Ownership. A BYOD-only team may select 'None / not used'.

## Endpoint Protection     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Malware and threat protection on staff devices, e.g. CrowdStrike, SentinelOne, Microsoft Defender.

**Risks**

Malware on one laptop can lead straight to production credentials.

**Controls**

Endpoint security, alerting and response.

**Evidence**

Console coverage reports and records of how alerts were handled.

**How auditors test**

Auditors compare coverage to the device inventory and review alert handling.

## Code Repository     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where source code lives and is reviewed, e.g. GitHub, GitLab, Bitbucket.

**Controls**

Anchors change management: branch protection, required reviews and restricted access.

**Evidence**

Pull request history, branch protection rules and repository access lists. The core change evidence.

**How auditors test**

Auditors sample merged changes for peer review and confirm protections can't be bypassed, including by admins.

## Build and Deployment / CI/CD     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How code is tested and released to production, e.g. GitHub Actions, CircleCI, Argo CD.

**Controls**

Automated tests and deployment gates can replace manual approvals, supporting a protected-pipeline change shape.

**Evidence**

Pipeline configuration and deployment logs link each production change to a reviewed pull request.

**How auditors test**

Auditors check that only the pipeline can deploy to production and that deployments trace back to reviewed code.

## Infrastructure Configuration     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

How infrastructure is defined and changed: infrastructure as code (Terraform, CloudFormation, Pulumi) or changes in the console.

**Controls**

Infrastructure as code brings infrastructure changes under the same review and version control as application code.

**Evidence**

Infrastructure-as-code repositories and plans. Console changes rely on cloud audit logs.

**How auditors test**

Auditors sample infrastructure changes for review and approval.

## Infrastructure Vulnerability Scanning     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Scanning of hosts, containers, images and cloud services for known vulnerabilities, e.g. Amazon Inspector, Wiz, Qualys.

**Risks**

Known, unpatched vulnerabilities are one of the most common paths to a breach.

**Controls**

Vulnerability management with a defined scan frequency and fix timeframes (SLAs) by severity.

**Evidence**

Scan reports and remediation tickets showing fixes within SLA.

**How auditors test**

Auditors sample scans across the period and check critical and high findings were fixed within your stated timeframes.

## Software Vulnerability Scanning     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Scanning of your code (SAST), dependencies (SCA) and running web applications (DAST), e.g. Snyk, Dependabot, Semgrep.

**Controls**

Secure development controls: issues found before release and tracked to a fix.

**Evidence**

Scan results, pull request checks and dependency update history.

**How auditors test**

Auditors check scanning ran throughout the period and high-severity findings were fixed or formally risk-accepted.

## Cloud Configuration Monitoring     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Continuous checks of cloud settings against good practice, e.g. AWS Security Hub, Wiz, Prowler.

**Controls**

Configuration monitoring that catches drift between periodic reviews.

**Evidence**

Dashboards, findings and remediation tickets.

**Day to day**

Turns periodic manual reviews into continuous, automated evidence.

## Audit Logging     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where system, infrastructure and user activity is recorded and retained, e.g. CloudTrail, Datadog, a SIEM.

**Risks**

Without logs, incidents can't be detected or investigated.

**Controls**

Logging coverage, retention, log protection and review.

**Evidence**

Logging configuration, retention settings and access restrictions.

**How auditors test**

Auditors check key systems are logged, logs are kept for the stated period, and access to logs is restricted.

## Security Threat Detection     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Tools that detect and alert on suspicious activity, e.g. GuardDuty, a SIEM, managed detection and response.

**Controls**

Monitoring and incident response: alerts are triaged, escalated and resolved.

**Evidence**

Alert configuration and triage records or tickets.

**How auditors test**

Auditors sample alerts for timely review and escalation.

## Availability Monitoring     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Uptime, performance and error monitoring, e.g. Datadog, Better Stack, Pingdom.

**Customer commitments**

Measures performance against uptime commitments and powers status pages.

**Controls**

Availability monitoring, capacity management and incident response.

**Evidence**

Alert configuration, uptime history and incident records.

**How auditors test**

Auditors check alerts reach on-call staff and incidents are tracked to resolution.

## Auto-scaling     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

Whether production capacity scales automatically with load, partly, manually or not at all.

**Controls**

With Availability in scope, configured auto-scaling brings in an automatic scaling control. Otherwise capacity is forecast and increased as required.

**Evidence**

Auto-scaling configuration and alerts, or capacity review records.

**Tips**

Choose Partly auto-scaled if some production services still scale by hand. The capacity planning control then covers them.

## Status Page     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

The tool used to tell customers about outages and planned maintenance.

**Customer commitments**

Shows how you meet the communication commitments in your terms and service levels.

**Evidence**

Status page history of incidents and maintenance notices.

## HR System     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where joiners, movers and leavers are recorded.

**Controls**

When named, HR events drive account set-up and removal, which strengthens access provisioning and removal.

**How auditors test**

Auditors sample joiners and leavers from HR records, so a reliable HR system makes testing cleaner.

**Tips**

Name the system of record, even if payroll runs elsewhere.

## Ticketing     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where access requests, changes, incidents and customer requests are tracked.

**Evidence**

Tickets become the evidence trail for approvals, changes and incident handling.

**Tips**

Name every tool used for tracking, for example one for engineering and one for support.

## Knowledge Management     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Where policies, procedures and runbooks live, e.g. Notion, Confluence, Google Drive.

**Controls**

The home for policies, procedures and their version history.

**Evidence**

Policy documents, approval history and staff acknowledgements.

**How auditors test**

Auditors check policies are approved, reviewed on schedule and available to staff.

**Tips**

Keep policies concise. They should describe how you actually work.

## Data Loss Prevention     Compliance Brain  ·  Multi-select  ·  Low impact

**What it captures**

Tools that detect or stop sensitive data leaving the organisation, e.g. Google DLP, Nightfall, Microsoft Purview.

**Controls**

Confidentiality and data protection controls.

**Evidence**

DLP policies and incident logs.

**Tips**

Most relevant when Confidentiality or Privacy is in scope, or regulated data is handled.

## Compliance shapes: service & customer

*How customers use and rely on the service. Shapes commitments, CUECs and the system boundary. Pick the closest match for how things work today.*

## Hosting responsibility     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Who operates the environment the service runs in.

**Options**

- Provider-hosted – you operate the service environment.
- Shared – responsibility is split.
- Customer-hosted – the customer operates the environment.
- Unsure / TBC – not known yet.

**Controls**

Provider-hosted puts infrastructure, change and monitoring controls on you. Shared or customer-hosted moves some of them to customers as CUECs and narrows your system boundary.

**Customer commitments**

The report must say clearly which parts customers operate, so they know what they must secure.

**How auditors test**

Auditors test the controls inside your boundary and check the CUECs match what customers actually run.

**Worth noting**

Your hosting model, any components customers install or host (agents, connectors, on-premises appliances), and how responsibilities are split.

## Tenancy & isolation     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How customers are separated from each other.

**Options**

- Multi-tenant – shared environment with logical separation.
- Isolated – stronger customer-specific isolation.
- Dedicated – a separate environment per customer.
- Unsure / TBC – not known yet.

**Risks**

Weak separation can expose one customer's data to another, a high-impact failure for any SaaS service.

**Controls**

Multi-tenant services need strong logical access controls and testing of tenant boundaries. Dedicated environments shift effort to consistent provisioning and configuration.

**Evidence**

Architecture and isolation design, plus penetration test coverage of cross-tenant access.

**Customer commitments**

Enterprise buyers often ask for isolation details or a dedicated option.

**Worth noting**

Your tenancy model, whether a dedicated environment is available, and how isolation is enforced (tenant IDs, separate schemas, separate accounts).

## Data minimisation     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How much sensitive data the service takes in.

**Options**

- Broad – the service can process a wide range of customer data.
- Purpose-limited – data types are deliberately constrained.
- Minimised – the architecture avoids receiving or storing sensitive data where possible.
- Unsure / TBC – not known yet.

**Risks**

The more sensitive data you hold, the greater the impact of a breach and the more regulations apply.

**Controls**

Minimised services can rely on fewer privacy, retention and encryption controls. Broad services need classification, retention and disposal controls.

**Customer commitments**

Restricted data types (e.g. no card or health data) often become CUECs telling customers what not to submit.

**Worth noting**

The data types the service accepts, the types it restricts or rejects, and whether data may be stored locally on devices.

## Data control boundary     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

Who decides where customer data is stored.

**Options**

- Provider-controlled – you determine the storage and processing environment.
- Shared – meaningful control on both sides.
- Customer-controlled – the customer keeps primary control over where data resides.
- Unsure / TBC – not known yet.

**Controls**

Provider-controlled storage puts residency, encryption and backup controls on you. Customer-controlled storage (e.g. their own cloud bucket or keys) moves those to customers.

**Customer commitments**

Shapes data residency and key management commitments, and the data CUECs.

**How auditors test**

Auditors check residency and storage claims against configuration.

**Worth noting**

Who owns the storage, where data is located, and whether customers can bring their own storage or keys.

## Availability responsibility     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

How much customers rely on the service being up.

**Options**

- Best efforts – limited formal reliance.
- Targeted availability – a defined internal or service target.
- Committed availability – customers contractually or operationally rely on stated availability.
- Unsure / TBC – not known yet.

**Scope**

Committed availability usually means the Availability criteria belong in scope.

**Controls**

Drives capacity planning, monitoring, backup, disaster recovery and incident response controls.

**Evidence**

Uptime history, status page records, and backup and DR test results.

**Customer commitments**

SLAs, RTOs and RPOs must be backed by controls and tested recovery.

**Worth noting**

Your availability target, SLA, RTO, RPO and how business-critical the service is for customers.

## Integration surface     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How customers connect to the service.

**Options**

- Closed – a mostly standalone service.
- Integrated – supported integrations with other systems.
- API-first / extensible – customers materially rely on APIs, webhooks or programmatic integration.
- Unsure / TBC – not known yet.

**Risks**

APIs, webhooks and stored customer credentials widen the attack surface.

**Controls**

Adds API authentication, rate limiting, key management, secure development and integration monitoring controls.

**Customer commitments**

Adds CUECs for customers to secure their API keys, endpoints and connected apps.

**Worth noting**

Whether there's a public API, the types of integrations, webhooks, and whether the service stores customer credentials for other systems.

## AI reliance     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

How central AI is to what customers receive.

**Options**

- Peripheral – AI is minor or supporting.
- Assistive – AI materially influences user workflows.
- AI-native – AI outputs are central to the service.
- Agentic – AI can independently take consequential actions.
- Unsure / TBC – not known yet.

**Risks**

Inaccurate outputs, customer data shared with model providers, and agents taking unintended actions.

**Controls**

Reliance scales the AI controls: model and vendor review, data-use settings, output evaluation and monitoring, and human approval for agent actions.

**Customer commitments**

Assistive and AI-native services typically add AI CUECs such as output review and human oversight. Agentic services need clear limits on what agents can do.

**Worth noting**

AI features, model providers, how much customers rely on AI outputs, and what actions AI is allowed to take.

## Customer administration     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Who administers customers' users and settings.

**Options**

- Customer-managed – the customer manages its users and configuration.
- Shared – administration is split.
- Provider-managed – you perform material administration for the customer.
- Unsure / TBC – not known yet.

**Controls**

Customer-managed administration puts user access CUECs on customers. Provider-managed administration needs your own approval, logging and review controls.

**Customer commitments**

Determines the access administration and access review CUECs.

**Worth noting**

Who administers users, what admin actions your team performs for customers, and how support access works.

## Responsibility for outcomes     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

Who owns the results the service produces.

**Options**

- Customer-directed – the software provides tools; the customer owns decisions and outcomes.
- Shared – you take on some responsibility for results.
- Provider-reliant – customers materially rely on outcomes you generate.
- Unsure / TBC – not known yet.

**Scope**

Where customers rely on your outputs (calculations, decisions, reports), Processing Integrity may belong in scope.

**Controls**

Provider-reliant services need input validation, processing accuracy and output review controls.

**Customer commitments**

Customer-directed services add CUECs for customers to validate outputs and decisions.

**Worth noting**

Any outcome commitments, whether customers must validate results, and any professional services element.

## Service standardisation     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

How much the service varies per customer.

**Options**

- Standardised – substantially the same service for everyone.
- Configurable – customers make meaningful configuration choices.
- Customised / managed – you change or operate material elements per customer.
- Unsure / TBC – not known yet.

**Controls**

Standardised services run one set of controls for everyone. Customised or managed services need per-customer change, configuration and access controls.

**Evidence**

Customised services may need evidence sampled per customer.

**Worth noting**

The level of customisation, any customer-specific controls, and elements you operate on a customer's behalf.

## Provider access to customer data     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

When your people can see customer data.

**Options**

- Routine – authorised staff may access customer data in normal operations.
- Exception-only – access happens only for defined support or incident cases.
- Technically restricted – the architecture prevents or heavily constrains your access.
- Unsure / TBC – not known yet.

**Risks**

Broad staff access to customer data is a leading confidentiality concern for customers.

**Controls**

Routine access needs least privilege, logging and periodic review. Exception-only access needs approval and a break-glass process. Technically restricted access is evidenced by design.

**Customer commitments**

Often written into confidentiality clauses and DPAs.

**How auditors test**

Auditors sample access events for approval and check logs are kept.

**Worth noting**

How support access works, who can reach production data, and your break-glass process.

## Compliance shapes: internal operations

*How the company runs day to day. Shapes how controls are designed, owned and evidenced. Pick the closest match for how things work today.*

## Access ownership     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Who grants and removes access to systems.

**Options**

- Distributed – system owners manage access.
- Federated – central rules with distributed execution.
- Centralised – identity and access are managed centrally.
- Unsure / TBC – not known yet.

**Controls**

Centralised models run access controls through one identity provider. Distributed models need consistent controls across every system owner.

**Evidence**

Centralised: one source for user lists and provisioning records. Distributed: evidence from each system.

**How auditors test**

Auditors sample joiners, movers and leavers and inspect access reviews.

**Worth noting**

Who approves access, your identity provider, and which system owners administer access themselves.

## Change management     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

How changes are approved and reach production.

**Options**

- Traditional approval – explicit change approval and gating.
- Agile – a lightweight workflow built into delivery.
- DevSecOps – automated security and testing gates.
- Empowered developers – developers deploy within defined guardrails.
- Unsure / TBC – not known yet.

**Controls**

Traditional approval relies on approvers. DevSecOps and empowered-developer models rely on peer review, automated tests and protected pipelines.

**Evidence**

Approval tickets, pull request reviews, pipeline gates and deployment logs.

**How auditors test**

Auditors sample changes and confirm each followed the designed path, including emergency changes.

**Worth noting**

Your deployment model, when approval is required, peer review rules and automated gates.

## Infrastructure operations     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How much of the stack you run yourselves.

**Options**

- Self-managed – you operate substantial infrastructure.
- Managed / PaaS – a provider manages much of the underlying stack.
- Serverless – operations are further abstracted to cloud services.
- Unsure / TBC – not known yet.

**Controls**

Self-managed infrastructure needs hardening, patching and capacity controls. Managed and serverless models rely more on provider SOC reports and configuration controls.

**Evidence**

Provider SOC reports and cloud configuration, rather than server-level evidence.

**Worth noting**

Your hosting stack, managed services, serverless usage, and who handles operations.

## Workforce model     Compliance Brain  ·  Single-select  ·  Low impact

**What it captures**

Where and how your people work.

**Options**

- Office-first – work happens mainly from controlled premises.
- Hybrid – meaningful office and remote work.
- Remote-first – designed primarily for distributed work.
- Unsure / TBC – not known yet.

**Controls**

Office-first adds physical security controls. Remote-first relies on device, identity and network controls.

**Evidence**

Badge and visitor records for offices; device and access evidence for remote teams.

**Worth noting**

Office locations, whether remote work is allowed, and the share of remote staff.

## Endpoint model     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Who owns and manages the devices staff use.

**Options**

- Corporate managed – the company owns and manages endpoints.
- Mixed – managed and personal devices coexist.
- BYOD – personal or unmanaged devices are an intentional part of the model.
- Unsure / TBC – not known yet.

**Risks**

Unmanaged devices can't be centrally secured or wiped if lost.

**Controls**

Corporate-managed devices enforce encryption, screen lock and updates through MDM. BYOD relies on browser-only access, conditional access and policy.

**Evidence**

MDM compliance reports, or access restriction settings and attestations for BYOD.

**How auditors test**

Auditors sample devices and compare their settings to policy.

**Worth noting**

Device ownership, your MDM tool, whether local data is allowed, and whether unmanaged devices can reach company systems.

## Privileged & production access     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

How admin and production access is held.

**Options**

- Standing – authorised users keep privileged access.
- Temporary / elevated – privilege is granted for defined needs.
- JIT – access is provisioned just in time and expires automatically.
- Unsure / TBC – not known yet.

**Risks**

Standing privileged access magnifies the impact of a compromised account.

**Controls**

Standing access needs periodic review and monitoring. Temporary and JIT models need request, approval and automatic expiry.

**Evidence**

Privileged user lists, access requests and approvals, and session logs.

**How auditors test**

Auditors review who holds privileged access and sample elevation requests.

**Worth noting**

Whether standing access exists, any JIT tooling, approval requirements and break-glass accounts.

## Risk management     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How risks are identified and kept current.

**Options**

- Periodic – formal scheduled assessments.
- Hybrid – periodic review plus event-driven updates.
- Continuous – risk is maintained through ongoing operating processes.
- Unsure / TBC – not known yet.

**Controls**

Periodic models rely on a scheduled assessment and register. Continuous models draw on ongoing inputs such as monitoring, incidents and changes.

**Evidence**

The risk register and assessment records, or the operating records that update risk.

**How auditors test**

Auditors check a risk assessment covers the period and drives control decisions.

**Worth noting**

How often risks are reviewed, which continuous inputs feed risk, and who owns risks.

## Vendor management     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

Who selects and oversees vendors.

**Options**

- Centralised – procurement or security centrally governs vendors.
- Federated – central standards with business owners.
- Distributed – teams largely own vendor selection and oversight.
- Unsure / TBC – not known yet.

**Controls**

Centralised models run vendor approval and review through one team. Distributed models need clear standards every owner follows.

**Evidence**

The vendor inventory, approvals, risk reviews and SOC report reviews.

**How auditors test**

Auditors sample new and critical vendors for approval and review.

**Worth noting**

Who owns procurement, who approves vendors, and what system owners are responsible for.

## Incident response     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

Who leads when something goes wrong.

**Options**

- Security-led – a dedicated security function coordinates response.
- Coordinated – security, operations and engineering share leadership.
- Engineering-led – system owners lead the technical response within escalation rules.
- Unsure / TBC – not known yet.

**Controls**

Sets incident roles, escalation paths and how the response plan is tested.

**Evidence**

Incident tickets, post-incident reviews and tabletop exercise records.

**How auditors test**

Auditors inspect incidents in the period (or a test) for detection, escalation and follow-up.

**Worth noting**

Who leads incidents, whether there's a security team, engineering's role, and when executives are involved.

## Governance     Compliance Brain  ·  Single-select  ·  Medium impact

**What it captures**

How leadership oversees security and compliance.

**Options**

- Formal committees – boards, committees and scheduled forums.
- Hybrid – formal oversight plus embedded accountability.
- Embedded ownership – accountable leaders govern through normal operating structures.
- Unsure / TBC – not known yet.

**Controls**

Formal committees evidence oversight through minutes. Embedded ownership uses existing leadership forums, without creating committees just for compliance.

**Evidence**

Meeting records, decisions and reporting to leadership or the board.

**How auditors test**

Auditors look for evidence that leadership reviewed security, risk and control performance during the period.

**Worth noting**

Your governance body, meeting cadence, executive owner and embedded owners.

## Control execution     Compliance Brain  ·  Single-select  ·  High impact

**What it captures**

Who or what performs routine controls.

**Options**

- Human / manual – people perform most control activities.
- Hybrid – people and automation share execution.
- Automated / agentic – systems or agents perform routine controls; people focus on exceptions and judgement.
- Unsure / TBC – not known yet.

**Controls**

Manual controls need checklists and sign-offs. Automated and agent-run controls need monitoring of the automation itself and clear thresholds for human review.

**Evidence**

Moves from screenshots and sign-offs to system logs and agent activity records.

**How auditors test**

Auditors test that the automation is configured correctly and that exceptions reach a person.

**Worth noting**

Which controls are manual, automated or agent-operated, and when a person must review.

## System description

*On the System Description tab. The narrative sections of the report, drafted by AI from your Domain and Compliance Brain answers, then reviewed by a person.*

## Company Description     System Description B6  ·  AI-drafted

**What it captures**

Who the company is: legal and trading name, year founded, headquarters, what it does and who it serves.

**Why it matters**

Opens the description of the system in the report and gives readers context.

**Day to day**

Drafted by AI from the Domain. Check every fact and remove the source tags once reviewed.

## Service Description     System Description B7  ·  AI-drafted

**What it captures**

The in-scope service, how customers use it and how it's delivered.

**Why it matters**

Sets the context auditors test controls against. Customers use it to check the report covers what they buy.

**Tips**

Plain, present tense and factual. No marketing language.

## Data Collected     System Description B8  ·  AI-drafted

**What it captures**

The types of customer and personal data processed, where they're stored and how long they're kept.

**Risks**

Data type drives impact. Personal, health or financial data raises the stakes.

**Controls**

Drives confidentiality, privacy, encryption, retention and disposal controls.

**Customer commitments**

Must align with your privacy policy and data processing agreement.

**Tips**

Anything not publicly stated is flagged [REQUIRES CLIENT CONFIRMATION].

## Principal Service Commitments and System Requirements     System Description E6  ·  AI-drafted

**What it captures**

What you promise customers (availability, security, confidentiality, breach notification, support) and the internal requirements that keep those promises.

**Controls**

Every commitment listed must be supported by controls. This is what the SOC 2 opinion is measured against.

**Customer commitments**

Drawn from your terms, MSA, SLA, DPA and trust pages.

**How auditors test**

Auditors assess whether controls are designed (and, for a Type 2, operating) to meet these commitments.

**Tips**

If the MSA or SLA isn't public, the draft shows [REQUIRES MSA TEMPLATE TO COMPLETE].

## Boundaries of the System     System Description E7  ·  AI-drafted

**What it captures**

What's in and out of scope: infrastructure, software, people, data and procedures, plus subservice organisations and how they're treated.

**Scope**

The line auditors test within. Everything inside needs controls and evidence; everything outside must be clearly excluded.

**Tips**

Tighter boundaries mean less to test, but they must still cover the service customers rely on.

## AI Draft Status     System Description E8  ·  Status

**What it captures**

Turns green once Client Name and Domain are set on the Compliance Brain tab. Then select B6:E8 and click Generate and fill.

**Tips**

Use Refresh to redraft after changing Compliance Brain answers. A person must review every draft before it's used.

## Complementary user entity controls

*On the System Description tab. Responsibilities your customers carry for the overall system to stay secure.*

## CUEC library     System Description A12:E46  ·  Tick boxes

**What it captures**

Controls your customers must operate, such as administering their own users, securing their API keys, or reviewing AI-generated outputs.

**Customer commitments**

Ticked CUECs are listed in the report so customers understand their side of the shared responsibility. They should match your contracts and documentation.

**Day to day**

Tick each CUEC that applies based on your product's features. Reflect the same responsibilities in onboarding and help content.

**How auditors test**

Auditors don't test CUECs, but check they're consistent with the service description and the controls that depend on them.

**Tips**

The AI CUECs apply when your product has AI features. Review them carefully as AI capabilities change.

## Incidents and changes

*On the System Description tab. Significant incidents and system changes the report must disclose.*

## Incidents & changes     System Description A50:E59  ·  Log

**What it captures**

Significant incidents and major system changes in the last 12 months: what happened, when, the impact on customers or commitments, and what was done.

**Why it matters**

The report must disclose significant incidents that affected your commitments and, for a Type 2, significant changes to the system during the period.

**Day to day**

Log each one as it happens. Your agent judges significance with you and drafts the disclosure for management to approve. Entries older than 12 months turn grey; keep them for history.

**How auditors test**

Auditors compare the log with incident tickets, postmortems and change records, and check that what the report discloses is complete.

## Your records

*On the Policies, Risks, Vendors, Controls and Audit Trail tabs. Where your records live, and the registers your agent keeps current.*

## Where your program lives     Compliance Brain B9 and E9  ·  Multi-select  ·  High impact

****

Where your agent builds and keeps your program: policies, evidence, and your risk and vendor registers. Set it once at the top of the Compliance Brain tab, and your agent uses it to decide where to build and store each one. Your controls and audit trail stay in this file.

****

Choose a cloud drive (Google Drive, OneDrive or SharePoint), a workspace wiki (Notion or Confluence), a compliance platform (such as Vanta or Drata), this file or other. Choose more than one if you split things up. TBC or Unsure means your agent will ask.

**Choosing a home**

Choose what your team already uses, and check your agent can reach it. If you have no preference, a cloud drive is the simplest place to start. Your program can't live only inside your AI. Later, your agent can migrate assets to other tools, which may mean working in a browser to build them there.

**What lives where**

If you use more than one tool, note what goes in each in E9: for example, policies, risk and vendor registers in Notion, and other audit evidence collated in Drive. Your agent adds links there once it has built them. The Policies, Risks, Vendors and Controls tabs show these details at the top.

## Policies     Policies A11:Q30, A34:I200 and A203:Q281  ·  Register and library

**What it captures**

The structure your agent follows to build your policies. The register holds one row per policy: purpose, scope, linked controls, the brain fields to draw on and the questions to ask, then owner, status, version, what changed, who approved it and when, the next review (12 months after approval) and a link to the finished policy. Policy statements hold the rules, one per row, each linked to the controls it supports, with a default to confirm where a timeframe or frequency applies.

**Starting point**

Fifteen policies and 139 statements, mapped to the Control Library. A policy or statement comes into scope when its linked controls do, so where there are alternatives (such as central or owner-led access reviews) only the one that fits your brain shows. Your agent tailors the in-scope statements and adds any your commitments need.

**Your choices**

At the top right of the Policies tab your agent records three choices it asks you before building: Depth (Light builds the 15 policies from the in-scope statements; Detailed builds the Throughline document set, 22 documents with full sections and tables, from the library at the bottom of the tab), Alignment (Defaults uses role names and library defaults confirmed by the owner; Tailored checks every setting against your systems and answers the Ask the client questions) and Document format (Google Docs or Word files, wiki pages or your compliance platform). Light with Defaults suits most teams under 100 staff and needs the fewest questions; you can step up later.

**Day to day**

Your agent generates finished policies from this structure, stores them where you've chosen, records what changed and moves the version on, then asks management to approve. Approval is recorded in the register.

**How auditors test**

Auditors check each policy is approved, reviewed at least annually and communicated to staff. They inspect the finished policy in your program home, with its version and approval recorded in the register.

## Risk register     Risks A16:V75  ·  Register

**What it captures**

Each risk: what could go wrong, its category, typical causes, the controls that treat it, the brain fields to draw on and a question to ask, then your tailored risk, owner, likelihood and impact, the inherent rating (calculated), treatment, residual rating, who accepted it and when, and the last review.

**Starting point**

Starts with 35 common SOC 2 risks, including fraud, key-person dependency and AI, each mapped to library controls. A risk comes into scope when its controls do. Your agent tailors them to your brain: your shapes, tools, data, customers and plans.

**Ratings**

Likelihood and impact are each scored 1 to 5 using the scales at the top of the Risks tab. Inherent rating is likelihood × impact before controls; residual rating is what's left once controls operate. Your management sets the rating bands and risk appetite there, and accepts residual risk.

**How auditors test**

Auditors expect a documented risk assessment at least annually that considers fraud, with each risk linked to the controls that treat it.

## Vendor register     Vendors A28:O127  ·  Register

**What it captures**

Each vendor: category, what they provide, the most sensitive data they access, tier, whether they're a subservice organisation, the assurance they hold and when it was reviewed, contract and DPA status, owner, approval and review dates. The next review is calculated from the tier.

**From your brain**

Tools named in your Compliance Brain that aren't in the register yet are listed on the right, so none are missed. Finding every vendor lists where else vendors are usually found, such as accounting bills and third-party app access, with a question to ask for each.

**Day to day**

Your agent collects assurance reports such as SOC 2 reports, flags gaps and tracks annual reviews. Your management signs off.

**How auditors test**

Auditors check vendors are assessed before onboarding and reviewed periodically, and that subservice organisations match the system description.

## Control framework     Controls A12:P183  ·  Register

**What it captures**

Your control framework, kept directly in this file. Left: every control in the Control Library, with In scope showing whether the rules apply it to you today. Right: whether it applies, your tailored wording, owner, the tool it lives in, where its evidence comes from, evidence type and status.

**How it's built**

The Control Library's rules read your brain and mark each control in scope, so the list updates as your brain fills in. Your agent tailors each in-scope control and you confirm. Add your own controls in the rows below the library.

**Your tools**

Lives in and Evidenced from list the tools you named in your Compliance Brain, plus This file and Manual process. Choose more than one where needed.

**How auditors test**

Auditors test each control as described, against the evidence you name. Accurate tool and evidence mapping makes testing faster and cleaner.

## Audit trail     Audit Trail A6:B  ·  Log

**What it captures**

A very high-level record of the work your agent has completed: the date and the key actions, such as policies drafted, risks added or vendors added.

**Day to day**

Your agent adds a row after each block of work. If it can't edit this file, it gives you the entry to add. Use it to keep track of what's been done. It doesn't replace approvals or version history.

## Questions about a field? Ask your Throughline Delivery Lead, or your compliance agent once it's connected.
