#!/usr/bin/env python3
"""Check what's left to do before the program is ready for an auditor.

Usage:
    python3 tools/check.py           # report only
    python3 tools/check.py --strict  # exit with code 1 if anything blocks audit readiness

Reports:
  - profile answers still marked "# example" (the reference company's)
  - high-impact profile fields still TBC, Unsure or blank
  - profile answers that aren't in the allowed options
  - placeholders ({{...}}) and open Confirm items left in program/
  - example rows still in the CSV records
  - CSV records whose columns don't match the expected header
  - AI work in the audit trail with no reviewer
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scope import ROOT, LIB, load_profile, split_answers, unknown  # noqa: E402

PROGRAM = os.path.join(ROOT, 'program')
HEADERS = {
    'controls/control-list.csv': ['ID', 'Control', 'What we do', 'Owner', 'Frequency', 'Where it lives', 'Evidence',
                                  'Policy', 'Template', 'Status', 'Last operated', 'Next due', 'Evidence link', 'Notes'],
    'context/context-sources.csv': ['Source', 'Type', 'Impact', 'Status', 'Informs', 'Link', 'Owner',
                                    'Last reviewed', 'Notes'],
    'registers/risk-register.csv': ['ID', 'Risk', 'Owner', 'Likelihood', 'Impact', 'Rating', 'Treatment',
                                    'Linked controls', 'Last reviewed', 'Notes'],
    'registers/vendor-register.csv': ['Vendor', 'What they provide', 'Data held', 'Tier', 'Assurance',
                                      'Contract and DPA', 'Owner', 'Last review', 'Next review', 'Notes'],
    'registers/people.csv': ['Name', 'Role', 'Type', 'Start date', 'Background check', 'Confidentiality signed',
                             'Policies acknowledged', 'Training completed', 'End date', 'Access removed', 'Status'],
    'records/activity-log.csv': ['Date', 'Activity', 'Control IDs', 'Performed by', 'Result', 'Evidence link',
                                 'Next due'],
    'records/requests-and-tickets.csv': ['Ref', 'Date', 'Type', 'Summary', 'Requested by', 'Approved by',
                                         'Status', 'Closed on', 'Control IDs', 'Link'],
    'records/sign-off-log.csv': ['Date', 'Decision type', 'Record', 'Decision', 'Approved by',
                                 'Open Confirm items accepted', 'Notes'],
    'records/policy-acknowledgements.csv': ['Date', 'Person', 'Policies', 'Version', 'Reason'],
    'records/audit-trail.csv': ['Ref', 'Date', 'Actor type', 'Actor', 'Action', 'Record affected', 'Summary',
                                'Reviewed by'],
}
PLACEHOLDER = re.compile(r'\{\{(?!TOOL\}\})[^{}]+\}\}')
CONFIRM = re.compile(r'- \[ \] `?\{\{Confirm:')


def read_csv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.reader(f))


def main():
    strict = '--strict' in sys.argv
    blockers, notes = [], []

    # 1. Profile
    profile = load_profile()
    fields = {r['Field']: r for r in csv.DictReader(open(os.path.join(LIB, 'brain-fields.csv'), encoding='utf-8'))}
    options = {}
    for r in csv.DictReader(open(os.path.join(LIB, 'field-options.csv'), encoding='utf-8')):
        options.setdefault(r['Field'], []).append(r['Option'])
    high_open = [f for f, r in fields.items() if r['Impact'] == 'H' and unknown(profile.get(f, ''))]
    med_open = [f for f, r in fields.items() if r['Impact'] == 'M' and unknown(profile.get(f, ''))]
    bad = []
    for f, v in profile.items():
        if f in options and not unknown(v):
            for part in split_answers(v):
                if part not in options[f]:
                    bad.append(f'{f}: "{part}"')
    missing = [f for f in fields if f not in profile]
    raw = open(os.path.join(ROOT, 'program', 'context', 'profile.yaml'), encoding='utf-8').read()
    examples = [l.split(':')[0] for l in raw.splitlines() if l.rstrip().endswith('# example') and not l.startswith('#')]
    print('Profile (program/context/profile.yaml)')
    print(f'  High-impact fields still open: {len(high_open)} of {sum(1 for r in fields.values() if r["Impact"] == "H")}')
    for f in high_open:
        print(f'    - {f}')
    print(f'  Medium-impact fields still open: {len(med_open)}')
    if bad:
        print('  Answers not in the allowed options (add them to brain/library/field-options.csv if they are real):')
        for b in bad:
            print(f'    - {b}')
    if missing:
        print(f'  Fields missing from the profile: {", ".join(missing)}')
    if examples:
        print(f'  Still the reference company\'s answers ("# example"): {len(examples)} fields. Replace them with yours.')
        blockers.append(f'{len(examples)} profile answers still describe the reference company')
    if high_open:
        blockers.append(f'{len(high_open)} high-impact profile fields open')

    # 2. Placeholders and Confirm items
    ph_files, confirm_total = [], 0
    for dirpath, _, files in os.walk(PROGRAM):
        if os.path.relpath(dirpath, PROGRAM).startswith('templates'):
            continue  # templates keep their placeholders; copies made from them are checked
        for name in files:
            if not name.endswith(('.md', '.csv')) or name == 'scope.md':
                continue
            path = os.path.join(dirpath, name)
            if name == 'README.md' and os.path.relpath(path, PROGRAM) != os.path.join('context', 'README.md'):
                continue  # explanatory pages
            text = open(path, encoding='utf-8').read()
            n = len(PLACEHOLDER.findall(text))
            c = len(CONFIRM.findall(text))
            confirm_total += c
            if n:
                ph_files.append((os.path.relpath(path, ROOT), n, c))
    print('\nPlaceholders and Confirm items (program/)')
    if ph_files:
        for path, n, c in sorted(ph_files):
            print(f'  {path}: {n} placeholders' + (f', {c} open Confirm items' if c else ''))
        blockers.append(f'{sum(n for _, n, _ in ph_files)} placeholders in {len(ph_files)} files')
    else:
        print('  None left.')

    # 3. CSV records
    print('\nRecords (program/**/*.csv)')
    for rel, header in HEADERS.items():
        path = os.path.join(PROGRAM, rel)
        if not os.path.exists(path):
            print(f'  {rel}: missing')
            continue
        rows = read_csv(path)
        if not rows or rows[0] != header:
            print(f'  {rel}: header changed. Expected: {", ".join(header)}')
            blockers.append(f'{rel} header changed')
            continue
        body = [r for r in rows[1:] if any(c.strip() for c in r)]
        examples = [r for r in body if any(c.startswith('Example') for c in r)]
        wrong = [i + 2 for i, r in enumerate(rows[1:]) if any(c.strip() for c in r) and len(r) != len(header)]
        msg = f'  {rel}: {len(body)} rows'
        if examples:
            msg += f', {len(examples)} example rows to replace or delete'
            blockers.append(f'example rows in {rel}')
        if wrong:
            msg += f', wrong number of columns on lines {wrong}'
            blockers.append(f'malformed rows in {rel}')
        print(msg)

    # 4. Audit trail reviewers
    path = os.path.join(PROGRAM, 'records/audit-trail.csv')
    if os.path.exists(path):
        rows = list(csv.DictReader(open(path, encoding='utf-8')))
        unreviewed = [r['Ref'] for r in rows if r.get('Actor type') == 'AI agent'
                      and (not r.get('Reviewed by', '').strip() or '{{' in r.get('Reviewed by', ''))]
        print('\nAudit trail')
        print(f'  {len(rows)} entries; AI work awaiting a reviewer: {", ".join(unreviewed) or "none"}')
        if unreviewed:
            blockers.append(f'{len(unreviewed)} AI audit trail entries without a reviewer')

    print('\nSummary')
    if blockers:
        print('  Not ready for an auditor yet:')
        for b in blockers:
            print(f'    - {b}')
    else:
        print('  Nothing generic left. Have the Compliance Owner review before anything goes to an auditor (AI Guidance 0.7).')
    if strict and blockers:
        sys.exit(1)


if __name__ == '__main__':
    main()
