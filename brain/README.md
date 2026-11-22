# The brain

The shared part of the Compliance Brain: the same for every company. Your own program lives in [program/](../program/).

| Folder | What it holds |
| --- | --- |
| [guidance/ai-guidance.md](guidance/ai-guidance.md) | Standing guardrails for AI agents, sections 0 to 10 |
| [guidance/user-guide.md](guidance/user-guide.md) | What each profile field means and how it shapes your compliance |
| [library/](library/) | Controls and scoping rules, policy blueprints, statements and document library, risks, vendor tiers and categories, CUECs, profile fields and options, settings to confirm, requirement lines, privacy obligations. [library/README.md](library/README.md) explains the method. |
| [prompts/system-description.md](prompts/system-description.md) | Prompts for drafting the system description |

Don't edit these files in your company's copy. When the library improves, you can pull the changes in without touching your program. If something here is wrong or missing, raise it upstream (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Updating from upstream

If you created your copy with **Use this template**, add the original as a remote once, then bring in new versions of `brain/` and `tools/`:

```bash
git remote add upstream https://github.com/{{owner}}/throughline-compliance-brain.git
git fetch upstream
git checkout upstream/main -- brain tools AGENTS.md
python3 tools/scope.py   # see whether scope changed
```

Review the changes, log the update in your audit trail, and commit.
