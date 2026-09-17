#!/usr/bin/env python3
"""Read/update the Atrily outreach tracker (Google Sheets).

Setup, column reference, and follow-up schedule: references/google-sheets-api.md

Usage:
    python3 scripts/sheets_client.py read [--status STATUS]
    python3 scripts/sheets_client.py update "Full Name" --status STATUS [--notes "text"]
    python3 scripts/sheets_client.py needs-draft
    python3 scripts/sheets_client.py write-draft "Full Name" "draft text"
    python3 scripts/sheets_client.py mark-sent "Full Name"
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

REPO_ROOT = Path(__file__).resolve().parent.parent
KEY_PATH = REPO_ROOT / "credentials" / "aios-sheets-key.json"
SHEET_ID = "1q8e6SnYRsyl_1iolDQ77ANj50zuNgXj0hlNwvAO0Gt8"
TAB_NAME = "outreach"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

COLUMNS = [
    "NAME", "DATE", "STATUS", "LINKEDIN", "NOTES",
    "RAW_NOTES", "DRAFT", "LAST_SENT", "TOUCH",
]

# Touch = number of messages already sent (0 = none yet). Value = day offset
# from DATE (the initial DM date, day 0) at which the NEXT message is due.
FOLLOWUP_SCHEDULE = {0: 0, 1: 4, 2: 11, 3: 21, 4: 35}
TOUCH_LABELS = {0: "Initial DM", 1: "Follow-up 1", 2: "Follow-up 2", 3: "Follow-up 3", 4: "Follow-up 4"}
SEQUENCE_LENGTH = 5  # touches 0-4; touch 5 = sequence complete


def get_service():
    creds = service_account.Credentials.from_service_account_file(
        str(KEY_PATH), scopes=SCOPES
    )
    return build("sheets", "v4", credentials=creds)


def read_rows(service, status_filter=None):
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SHEET_ID, range=TAB_NAME)
        .execute()
    )
    values = result.get("values", [])
    if not values:
        return []
    header, rows = values[0], values[1:]
    records = []
    for i, row in enumerate(rows, start=2):  # sheet row number, header is row 1
        record = {header[j]: (row[j] if j < len(row) else "") for j in range(len(header))}
        record["_row"] = i
        if status_filter and record.get("STATUS", "").lower() != status_filter.lower():
            continue
        records.append(record)
    return records


def find_row(records, name):
    matches = [r for r in records if r.get("NAME", "").strip().lower() == name.strip().lower()]
    if not matches:
        return None, None
    if len(matches) > 1:
        print(f"Warning: {len(matches)} rows match '{name}', using the first", file=sys.stderr)
    return matches[0], matches[0]["_row"]


def col_letter(name):
    return chr(ord("A") + COLUMNS.index(name))


def write_cells(service, updates):
    """updates: list of (row_num, COLUMN_NAME, value)"""
    data = [
        {"range": f"{TAB_NAME}!{col_letter(col)}{row_num}", "values": [[value]]}
        for row_num, col, value in updates
    ]
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={"valueInputOption": "USER_ENTERED", "data": data},
    ).execute()


def parse_date(date_str):
    """Sheet dates are 'DD-Mon' with no year (e.g. '18-Jul'). Assumes the
    current year — this breaks if an outreach thread spans a year boundary.
    Returns None if unparseable."""
    date_str = (date_str or "").strip()
    if not date_str:
        return None
    try:
        return datetime.strptime(f"{date_str}-{datetime.now().year}", "%d-%b-%Y")
    except ValueError:
        return None


def update_row(service, name, status=None, notes=None):
    records = read_rows(service)
    record, row_num = find_row(records, name)
    if record is None:
        print(f"No row found for '{name}'", file=sys.stderr)
        return False

    updates = []
    if status is not None:
        updates.append((row_num, "STATUS", status))
    if notes is not None:
        updates.append((row_num, "NOTES", notes))

    if not updates:
        print("Nothing to update — pass --status and/or --notes", file=sys.stderr)
        return False

    write_cells(service, updates)
    return True


def needs_draft(service):
    """List rows that need a drafted message written now: brand-new leads
    with raw signal notes but no draft yet, and 'waiting' leads whose next
    follow-up in the day-0/4/11/21/35 sequence is due. Skips anything with
    a draft already queued (waiting on you to send + run mark-sent) and
    anything no longer 'waiting' (replied/booked — sequence stops)."""
    records = read_rows(service)
    today = datetime.now()
    due, sequence_complete, unparseable = [], [], []

    for r in records:
        status = r.get("STATUS", "").strip().lower()
        if status not in ("", "waiting"):
            continue
        if r.get("DRAFT", "").strip():
            continue  # already queued, waiting on you to send + mark-sent

        touch = int(r.get("TOUCH") or 0)

        if touch == 0:
            raw = r.get("RAW_NOTES", "").strip()
            if not raw:
                continue  # nothing to draft from yet
            due.append({
                "row": r["_row"], "name": r["NAME"], "reason": TOUCH_LABELS[0],
                "raw_notes": raw, "last_sent": "",
            })
        elif touch >= SEQUENCE_LENGTH:
            sequence_complete.append({"row": r["_row"], "name": r["NAME"]})
        else:
            date_val = parse_date(r.get("DATE", ""))
            if date_val is None:
                unparseable.append({"row": r["_row"], "name": r["NAME"], "date": r.get("DATE", "")})
                continue
            days_since = (today - date_val).days
            if days_since >= FOLLOWUP_SCHEDULE[touch]:
                due.append({
                    "row": r["_row"], "name": r["NAME"], "reason": TOUCH_LABELS[touch],
                    "raw_notes": r.get("RAW_NOTES", ""), "last_sent": r.get("LAST_SENT", ""),
                })

    return due, sequence_complete, unparseable


def write_draft(service, name, text):
    records = read_rows(service)
    record, row_num = find_row(records, name)
    if record is None:
        print(f"No row found for '{name}'", file=sys.stderr)
        return False
    write_cells(service, [(row_num, "DRAFT", text)])
    return True


def mark_sent(service, name):
    records = read_rows(service)
    record, row_num = find_row(records, name)
    if record is None:
        print(f"No row found for '{name}'", file=sys.stderr)
        return False
    draft = record.get("DRAFT", "").strip()
    if not draft:
        print(f"No pending draft for '{name}' — nothing to mark as sent", file=sys.stderr)
        return False

    touch = int(record.get("TOUCH") or 0)
    updates = [
        (row_num, "LAST_SENT", draft),
        (row_num, "DRAFT", ""),
        (row_num, "TOUCH", touch + 1),
    ]
    if touch == 0:
        # First message going out now — this is day 0, the anchor for the whole schedule.
        updates.append((row_num, "DATE", datetime.now().strftime("%d-%b")))
        if not record.get("STATUS", "").strip():
            updates.append((row_num, "STATUS", "waiting"))
    write_cells(service, updates)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    read_p = sub.add_parser("read", help="List prospects, optionally filtered by status")
    read_p.add_argument("--status", help="Filter by STATUS column (e.g. waiting, replied, booked)")

    update_p = sub.add_parser("update", help="Update a prospect's status and/or notes")
    update_p.add_argument("name", help="Exact NAME as it appears in the sheet")
    update_p.add_argument("--status")
    update_p.add_argument("--notes")

    sub.add_parser("needs-draft", help="List leads needing an initial or follow-up draft right now")

    write_p = sub.add_parser("write-draft", help="Write a drafted message into a lead's DRAFT cell")
    write_p.add_argument("name")
    write_p.add_argument("text")

    mark_p = sub.add_parser("mark-sent", help="Confirm the queued DRAFT was sent; advances the follow-up sequence")
    mark_p.add_argument("name")

    args = parser.parse_args()
    service = get_service()

    if args.command == "read":
        records = read_rows(service, status_filter=args.status)
        print(f"{len(records)} row(s)")
        for r in records:
            print(f"  [{r['_row']}] {r['NAME']} | {r['DATE']} | {r['STATUS']} | {r['LINKEDIN']}")

    elif args.command == "update":
        ok = update_row(service, args.name, status=args.status, notes=args.notes)
        if ok:
            print(f"Updated '{args.name}'")
        else:
            sys.exit(1)

    elif args.command == "needs-draft":
        due, sequence_complete, unparseable = needs_draft(service)
        print(f"{len(due)} lead(s) need a draft:")
        for d in due:
            print(f"  [{d['row']}] {d['name']} — {d['reason']}")
            if d["raw_notes"]:
                print(f"      RAW_NOTES: {d['raw_notes']}")
            if d["last_sent"]:
                print(f"      LAST_SENT: {d['last_sent']}")
        if sequence_complete:
            print(f"\n{len(sequence_complete)} lead(s) finished all 4 follow-ups with no reply — decide manually:")
            for s in sequence_complete:
                print(f"  [{s['row']}] {s['name']}")
        if unparseable:
            print(f"\n{len(unparseable)} lead(s) have an unparseable DATE — check manually:")
            for u in unparseable:
                print(f"  [{u['row']}] {u['name']} — DATE='{u['date']}'")

    elif args.command == "write-draft":
        ok = write_draft(service, args.name, args.text)
        if ok:
            print(f"Draft written for '{args.name}'")
        else:
            sys.exit(1)

    elif args.command == "mark-sent":
        ok = mark_sent(service, args.name)
        if ok:
            print(f"Marked sent for '{args.name}' — sequence advanced")
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
