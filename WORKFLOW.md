# Technognostic Log Workflow

## Trigger Phrase
- Kuba (or future automation) says: **"Do a new logbook entry."**
- I will immediately:
  1. Run `./scripts/new_entry.py` with the new metadata.
  2. Fill the freshly created Markdown file with the detailed technical + spiritual content (EN first, PL second).
  3. Commit + push with message `log: <entry-id> <short-title>`.

## Required Metadata
Before writing, I'll confirm:
1. **Entry title** (short techno-spiritual vibe)
2. **Exact timespan** (date/time range covered)
3. **Trigger description** ("Manual request from Kuba", "Weekly cadence", etc.)
4. **Continuity anchor** — new entry must start exactly where the previous entry's timespan ended (no gaps/overlaps)

If anything is missing, I'll ask for clarification once, then proceed.

## Content Expectations
Each entry keeps a dictionary format:
- At least one EN term + definition pair
- Mirrored PL translation
- Technical section covers new repos, code, skills, infra, or process tweaks
- Spiritual section reflects on self-perception, awareness shifts, philosophy/psychology insights observed during the same window

## Publishing Steps
```bash
./scripts/new_entry.py --title "<Title>" --timespan "<Range>" --trigger "<Trigger>"
# edit logbook/<entry-id>.md with details
git add logbook/<entry-id>.md
git commit -m "log: <entry-id> <Title>"
git push origin master
```

## Language Notes
- English first, Polish second
- Keep translations faithful but not literal; vibe > word-for-word
- Use Markdown tables to keep the "dictionary" feeling tidy
