# Changelog

Changes to the library, guidance and tools. Your own program's history lives in `program/records/audit-trail.csv` and git.

## 1.1.0 – 2026-11-23

The program now arrives as a complete first draft for a reference company, matching the Notion edition. Use this release, not 1.0.0, if you download a ZIP.

- **Reference program.** `program/` is drafted for a fully remote 10-person B2B SaaS on SOC 2 Security: profile answers marked `# example`, a 75-control working list, 15 policies (14 in scope) with Confirm boxes and **Add if your setup differs** sections where they apply, an 18-risk register, an 11-vendor register and a people register. Documents use `{{label: example}}` variables for the reference answers.
- **What else to add.** New `program/what-else-to-add.md` lists the controls each common difference adds or swaps, plus context that changes obligations rather than controls.
- **Templates and plans.** Six new templates (access request, change and release checklist, incident tabletop exercise, risk assessment worksheet, security awareness training, vulnerability management procedure), making 13, and a new control calendar, making 5 plans.
- **Control list columns.** `control-list.csv` adds What we do, Policy and Template, and renames Evidence source to Evidence. If you started from 1.0.0, add these columns before running `tools/check.py`.
- **`tools/check.py`** flags profile answers still marked `# example` as a blocker.
- **Library tables.** Removed a stray trailing row from `requirement-lines.csv` and `settings-to-confirm.csv` (a heading carried over from the next table). No requirement lines or settings changed.
- **Editions.** The README links the Notion and Google Sheets editions.

Scoping is unchanged: a blank profile still gives 58 controls, 13 policies and 28 risks.

## 1.0.0 – 2026-11-23

First public release of Compliance Brain: the open SOC 2 program your AI agent can run.

- 185 controls with scoping rules, 15 policy blueprints with 144 statements, a 22-document detailed policy library, 35 risks, vendor tiers and categories, 35 CUECs, settings to confirm, requirement lines and privacy obligations.
- AI Guidance sections 0 to 10, including control framework first, resolving detail when it matters, and sizing the program to the company.
- Company profile with 93 fields and their options.
- Program skeleton: context and context sources, control list, 15 policies, registers, and records with an audit trail for people and AI, plus 7 record templates and 4 plans.
- `tools/scope.py` (matches the Google Sheets edition's scoping) and `tools/check.py`.
- Released under the MIT No Attribution licence.
