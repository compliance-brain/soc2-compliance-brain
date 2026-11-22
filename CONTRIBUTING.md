# Contributing

Thanks for helping make compliance simpler. This repository is two things: a shared library (`brain/` and `tools/`) and a program skeleton (`program/`) that each company copies and fills in. Contributions go to the shared parts.

## Good contributions

- A control, policy statement, risk or CUEC that's missing, wrong or worded badly
- A scoping rule that brings a control in or out when it shouldn't
- A new option for a profile field, such as a tool that's missing from a list
- Guidance that would stop an AI agent making a mistake you've seen
- Fixes to the tools, with a note of how you tested them

## How

1. Open an issue first for anything bigger than a wording fix, so we can agree the approach.
2. Keep changes small and plain. The library's first principle is simple first: detail that doesn't serve a control, a customer commitment or a legal duty stays out.
3. Keep IDs stable. Don't renumber controls, statements or risks; add new IDs instead. Keep CSV column names unchanged.
4. If you change scoping rules, run `python3 tools/scope.py` with a blank profile and say how the counts changed. A blank profile should give 58 controls, 13 policies and 28 risks unless the change is intended to alter that.
5. Add a line to `CHANGELOG.md`.

## Never include

Your company's program, profile answers, evidence, names, customer details or anything confidential. If you're contributing from your company's copy, make the change in a fresh fork of this repository.

## Accuracy

Laws and standards change. When you add or change a requirement line, cite the source in the pull request. Nothing here is legal advice.
