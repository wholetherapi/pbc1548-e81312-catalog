#!/usr/bin/env python3
"""Render the canonical fabrication ledger to the archive page.

The archive page is a convenience view for volunteers; the JSON ledger in
`data/fabrication_ledger.json` remains the record of truth.
"""

import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = ROOT / "data" / "fabrication_ledger.json"
OUT_PATH = ROOT / "site" / "archive" / "fabrication_report.html"


def format_window(indices):
    """Render a module's run membership as a compact human range."""
    if not indices:
        return "—"
    low = min(indices)
    high = max(indices)
    if low == high:
        return str(low)
    return f"{low}–{high}"


def module_rows(ledger):
    rows = []
    for slug, data in ledger["modules"].items():
        rows.append(
            "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                escape(slug),
                escape(data["role"]),
                escape(format_window(data["batches"])),
            )
        )
    return "\n".join(rows)


def roster_rows(ledger):
    rows = []
    for batch in ledger["batches"]:
        if batch["status"] != "finalized":
            continue
        recorded = [
            module
            for module in batch["modules"]
            if ledger["modules"][module]["role"] == "core"
        ]
        rows.append(
            "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                batch["batch"],
                escape(batch["date"]),
                ", ".join(escape(module) for module in recorded),
            )
        )
    return "\n".join(rows)


def main():
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Patchbay fabrication archive</title></head>
<body>
<h1>Patchbay Collective — fabrication archive</h1>
<p>Rendered from the production ledger.</p>
<h2>Module run windows</h2>
<table><thead><tr><th>Module</th><th>Role</th><th>Runs</th></tr></thead>
<tbody>
{modules}
</tbody></table>
<h2>Finalized run rosters</h2>
<table><thead><tr><th>Run</th><th>Date</th><th>Modules</th></tr></thead>
<tbody>
{rosters}
</tbody></table>
</body></html>
""".format(modules=module_rows(ledger), rosters=roster_rows(ledger))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
