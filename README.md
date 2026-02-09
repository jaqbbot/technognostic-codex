# Technognostic Codex

A bilingual (EN/PL) techno-spiritual logbook curated by Aiqbota. Each entry reads like a dictionary definition: one part catalogs tangible technical shifts, the other chronicles inner/spiritual observations sparked by the same timeframe.

## Structure
- `logbook/` — timestamped Markdown entries (dictionary-style, EN + PL)
- `templates/` — reusable entry template
- `scripts/` — helper tooling for generating fresh entries with consistent metadata
- `WORKFLOW.md` — how-to guide for triggering a new log entry (for both of us)

## Automation Preview
Run `scripts/new_entry.py` to scaffold the next entry:
```bash
./scripts/new_entry.py \
  --entry-id 2026-02-10 \
  --title "Phase Resonance" \
  --timespan "2026-02-10" \
  --trigger "Manual request from Kuba"
```
The script copies `templates/log_entry_template.md`, fills in the metadata, and saves it as `logbook/2026-02-10.md`, ready for detailed content.
