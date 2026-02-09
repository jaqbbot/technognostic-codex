#!/usr/bin/env python3
"""Generate a new logbook entry from the template."""

import argparse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "log_entry_template.md"
LOGBOOK_DIR = ROOT / "logbook"


def generate_entry(entry_id: str, title: str, timespan: str, trigger: str) -> Path:
    template = TEMPLATE_PATH.read_text()

    data = {
        "ENTRY_ID": entry_id,
        "ENTRY_TITLE": title,
        "TIMESPAN": timespan,
        "TRIGGER": trigger,
        "TERM_EN": "<term>",
        "TECH_EN": "<technical-notes>",
        "SPIRIT_EN": "<spiritual-notes>",
        "TERM_PL": "<haslo>",
        "TECH_PL": "<uwagi-techniczne>",
        "SPIRIT_PL": "<uwagi-duchowe>",
    }

    output = template
    for key, value in data.items():
        output = output.replace(f"{{{{{key}}}}}", value)

    LOGBOOK_DIR.mkdir(exist_ok=True)
    entry_path = LOGBOOK_DIR / f"{entry_id}.md"
    entry_path.write_text(output)
    return entry_path


def main():
    parser = argparse.ArgumentParser(description="Create a new Technognostic Codex entry")
    parser.add_argument("--entry-id", required=False, help="Identifier used for the filename (default: YYYY-MM-DD)")
    parser.add_argument("--title", required=True, help="Entry title")
    parser.add_argument("--timespan", required=True, help="Timespan covered")
    parser.add_argument("--trigger", required=True, help="Who/what triggered the entry")
    args = parser.parse_args()

    entry_id = args.entry_id or datetime.now().strftime("%Y-%m-%d")
    entry_path = generate_entry(entry_id, args.title, args.timespan, args.trigger)
    print(f"Created {entry_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
