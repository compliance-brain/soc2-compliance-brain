# Throughline Compliance Brain

**An open, AI-ready SOC 2 program for early-stage companies.** Give it to your AI agent and it builds a lean compliance program that fits how your company actually works: control list, policies, risk and vendor registers, records and evidence plan, all as plain files you own.

AI already knows compliance: the frameworks, the risks, the controls and how auditors test them. What it doesn't know is your company. This repository gives it your context, the guardrails it works within, and a library to work from.

- **185 controls** mapped to the SOC 2 Trust Services Criteria, each with the rule that brings it into scope
- **15 policy blueprints** with 144 statements, plus a detailed document library
- **35 common SOC 2 risks**, vendor tiers and review checks, and **35 customer responsibilities (CUECs)**
- **Guardrails** for how an AI agent works: accuracy first, people approve, simple before detailed
- **Two small tools**: one works out what's in scope for you, one checks what's left before an audit

> [!IMPORTANT]
> This is a starting point, not legal advice or a certification. Your auditor tests your controls independently, and anything here is generic until it's adapted to your company and approved by your people.

## Quick start

1. **Make your own private copy.** Select **Use this template** → **Create a new repository**, and set it to **Private**. Your program will hold internal details.
2. **Open it with an AI agent that can read and write files**, such as Claude Code, Codex, Cursor or GitHub Copilot.
3. **Say:** *"Read AGENTS.md and help me set up our compliance program."*

The agent reads its brief, asks where your program should live, gathers your existing documents (security questionnaires, terms of service, privacy policy, operating manuals), drafts your profile and generates your control list. You answer questions, make decisions and approve.

No git? Download the ZIP, unzip it, and give the folder to any AI assistant that can read and write files.

## How it works

```
Your context            The library               Your agent                 Your program
profile.yaml      +     brain/library/      →     scopes and tailors   →     program/
context-sources         controls, policies,       (tools/scope.py,          control list, policies,
                        risks, vendors, CUECs     AI Guidance)              registers, records
```

1. **Your context** lives in [program/context/](program/context/): the company profile (what you sell, who relies on it, your data, tools and how your teams work) and the documents it's drawn from.
2. **The library** in [brain/](brain/) holds the controls, blueprints and guardrails. It's the same for everyone.
3. **Your agent** keeps what applies to you and rewrites it with your people, tools, timeframes and commitments. It asks when a detail matters and never guesses.
4. **Your program** in [program/](program/) is lean, audit-ready and describes how you actually work. Git history plus the [audit trail](program/records/audit-trail.csv) show who changed what, whether a person or an AI.

## What's in the repo

| Folder | What it holds |
| --- | --- |
| [AGENTS.md](AGENTS.md) | The AI agent's brief. Start here if you're an AI. |
| [brain/guidance/](brain/guidance/) | AI Guidance (guardrails) and the User Guide (what each field means) |
| [brain/library/](brain/library/) | Controls with scoping rules, policy blueprints and statements, risks, vendor tiers, CUECs, field options |
| [program/context/](program/context/) | Your company profile, context sources and system description |
| [program/controls/](program/controls/) | What's in scope (generated) and your working control list |
| [program/policies/](program/policies/) | 15 policy skeletons to adapt |
| [program/registers/](program/registers/) | Risk register, vendor register, people |
| [program/records/](program/records/) | Activity log, requests and tickets, sign-offs, acknowledgements, audit trail |
| [program/templates/](program/templates/) | Access review, management review, restore test, vendor review, onboarding, leaving, incident |
| [program/plans/](program/plans/) | Continuity and recovery, incident response, organisation and roles, evidence guide |
| [tools/](tools/) | `scope.py` and `check.py` (Python 3, no dependencies) |

## The tools

```bash
python3 tools/scope.py    # what's in scope for your profile → program/controls/scope.md
python3 tools/check.py    # open profile fields, placeholders, Confirm items, example rows, unreviewed AI work
python3 tools/check.py --strict   # exits with an error if anything blocks audit readiness
```

With a blank profile you start at 58 controls (Startup, Security only). Naming your stage, criteria, tools and how you operate brings the right alternatives in and the rest out.

## Markers

| Marker | Means | Who acts |
| --- | --- | --- |
| `{{like this}}` | Something to replace with your own value | 🤖 AI fills it from your profile; 👤 a person confirms |
| 🧭 **Guide** (note box) | How this part works and what auditors look for | Read, then delete |
| ✏️ **Adapt** (important box) | What to customise before relying on it | 🤖 AI drafts; 👤 owner checks |
| ✅ **Confirm** (warning box) | A decision the owner makes before approval, with the default and why | 👤 Owner decides |
| `Example:` rows | Sample data showing the format | Replace or delete |

## Principles

- **Simple first.** Detail that doesn't serve a control, a customer commitment or a legal duty stays out.
- **Ask now, confirm, or check at the end.** Only questions that change scope get asked up front. Everything else is drafted with a Confirm item and resolved before approval.
- **Be honest about complexity.** Regulated data, outside AI models, several countries or a product not yet live all mean more decisions. A lean first cut is never presented as complete.
- **Size to your stage.** Add fields and records when a control, auditor or customer needs them. Anything a law or contract requires is there from day one.
- **Stay true.** Never invent tools, people, numbers or evidence. Never alter or back-date evidence.
- **People approve.** AI agents draft, prepare and collect evidence. Your team changes security settings, with the agent guiding and recording.

## Other editions

The same brain is also available as a Google Sheets template and a Notion template. Use whichever fits how your team works; the library and guardrails are the same.

## Contributing

Improvements to the library and guidance are welcome: a control that's missing, a rule that scopes wrongly, a policy statement that reads badly. See [CONTRIBUTING.md](CONTRIBUTING.md). Please don't open issues or pull requests that contain your company's own program details.

## License

[MIT](LICENSE). Use it, adapt it and share it, commercially or not, keeping the copyright notice.
