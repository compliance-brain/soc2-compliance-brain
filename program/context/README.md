# Your context

> [!NOTE]
> **🧭 Guide.** Your compliance context is the set of facts about your company that shapes large parts of your program: which controls apply, how strict each policy needs to be, which risks matter and which vendors are in scope. When it's set up well, AI can build and run a program that fits how you actually work. When it's thin or wrong, everything built on it drifts. Spend your first hour here.

> [!IMPORTANT]
> **✏️ Adapt.** 🤖 AI: draft each answer in [profile.yaml](profile.yaml) from the sources in [context-sources.csv](context-sources.csv), cite the source in the source's Notes, and add anything you inferred to the Confirm box below. 👤 Person: check each answer, resolve the Confirm items and record who reviewed it and when. Come back here when something changes: a new product, market, data type, vendor or regulation.

## The reference company

The profile ships with the answers for a reference company, each marked `# example`: a simple, fully remote 10-person B2B SaaS on AWS (RDS, Cloudflare), Google Workspace sign-in, Slack, GitHub with Actions and Terraform, 1Password, Kandji-managed laptops, Linear and Rippling, live with early customers and going for a SOC 2 Security Type 1 then Type 2. The whole program is drafted for it. Replace each answer with yours and delete the marker; `tools/check.py` lists any left, and `tools/scope.py` shows how your scope differs.

## What's here

| File | What it holds |
| --- | --- |
| [profile.yaml](profile.yaml) | The 93 profile fields that shape your program, grouped as in the Compliance Brain. High-impact fields are marked `[H]`. `tools/scope.py` reads it. |
| [context-sources.csv](context-sources.csv) | The documents and systems the profile draws on, with what each informs and when it was last reviewed. |
| [system-description.md](system-description.md) | The narrative of your SOC 2 report, the customer responsibilities (CUECs) that apply, and significant incidents and changes. |

What each field means, and how it's used, is in the [User Guide](../../brain/guidance/user-guide.md).

## Start with what you already have

You probably hold documents that already describe your context. Linking them first saves a long questionnaire and gives AI evidence to work from rather than guesses. In rough order of impact:

1. **Completed security questionnaires** (from customers or prospects): usually the fastest map of your data, hosting, access and practices.
2. **Terms of service, privacy policy and any DPA**: what you've already promised customers about data, retention, subprocessors and breach notice.
3. **Trust or security page**: public claims your controls must back up.
4. **Operating manuals, runbooks and onboarding docs**: how work actually gets done day to day.
5. **Architecture or system diagrams**: what's in scope and where data flows.
6. **Tool and billing list** (or card statements): the fastest route to a complete vendor register.
7. **Org chart or team list**: owners, approvers and who needs access.
8. **Customer contracts and enterprise requirements**: commitments such as audit rights, notice periods and where data must stay.
9. **Investor or board updates and pitch deck**: stage, plans and product direction.

Link private documents rather than copying them into this repository.

## The fields that matter most

These high-impact fields set scope and structure, so answer them first. Some trigger a question your agent must ask before building (AI Guidance 9.3), such as a product that isn't live yet, health or payment card data, or AI that takes actions for users.

Program home · Agent role · Where you'll use it · Company Name · Domain · Framework Scope · Service Type · Compliance Stage · Product Status · Compliance Owner · Infrastructure · Hosting Platform · Hosting responsibility · Availability responsibility · AI reliance · Customer administration · Provider access to customer data · Access ownership · Change management · Endpoint model · Privileged & production access · Control execution

> [!WARNING]
> **✅ Confirm.** Profile reviewed by `{{name}}` on `{{date}}`. Open Confirm items: `{{list or none}}`. Log each review in the [audit trail](../records/audit-trail.csv).

## Keeping oversight

- **One source of truth:** if a policy or register disagrees with the profile, fix whichever one is wrong and log the change in the audit trail.
- **Review triggers:** check the profile each quarter, and whenever you launch a product, enter a market, take on a new data type, add a critical vendor or face a new regulation.
- **AI reads this first:** your agent reads the profile at the start of each session so its work stays aligned with your context.
