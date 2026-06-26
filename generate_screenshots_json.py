<<<<<<< HEAD
import os
import re
import json
import datetime

SCREENSHOTS_DIR = "screenshots"
OUTPUT_FILE = "screenshots.json"
SCREENSHOT_PREFIX = "callofwar"

FRAME_NAME_PATTERN = re.compile(
    rf'^{re.escape(SCREENSHOT_PREFIX)}\((\d+)\)\.(png|jpg|jpeg)$',
    re.IGNORECASE,
)


def sort_key(filename):
    match = FRAME_NAME_PATTERN.match(filename)
    if match:
        return (0, int(match.group(1)), filename.lower())
    try:
        date = datetime.datetime.strptime(os.path.splitext(filename)[0], "%Y%m%d_%H%M%S")
        return (1, date, filename.lower())
    except ValueError:
        return (2, filename.lower())


def build_entries():
    if not os.path.isdir(SCREENSHOTS_DIR):
        return []

    files = [
        f for f in os.listdir(SCREENSHOTS_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    files = sorted(files, key=sort_key)

    entries = []
    for filename in files:
        label = filename
        timestamp = ""
        file_path = os.path.join(SCREENSHOTS_DIR, filename)

        match = FRAME_NAME_PATTERN.match(filename)
        if match:
            label = f"{SCREENSHOT_PREFIX}({int(match.group(1))})"
            timestamp = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            ).strftime("%Y-%m-%d %H:%M:%S")
        else:
            try:
                timestamp = datetime.datetime.strptime(
                    os.path.splitext(filename)[0], "%Y%m%d_%H%M%S"
                ).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                timestamp = ""

        entries.append({
            "filename": filename,
            "label": label,
            "timestamp": timestamp,
        })

    return entries


def write_output(entries):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    entries = build_entries()
    write_output(entries)
    print(f"{OUTPUT_FILE} created with {len(entries)} entries")
=======
import os
import re
import json
import datetime

SCREENSHOTS_DIR = "screenshots"
OUTPUT_FILE = "screenshots.json"
SCREENSHOT_PREFIX = "callofwar"

FRAME_NAME_PATTERN = re.compile(
    rf'^{re.escape(SCREENSHOT_PREFIX)}\((\d+)\)\.(png|jpg|jpeg)$',
    re.IGNORECASE,
)


def sort_key(filename):
    match = FRAME_NAME_PATTERN.match(filename)
    if match:
        return (0, int(match.group(1)), filename.lower())
    try:
        date = datetime.datetime.strptime(os.path.splitext(filename)[0], "%Y%m%d_%H%M%S")
        return (1, date, filename.lower())
    except ValueError:
        return (2, filename.lower())


def build_entries():
    if not os.path.isdir(SCREENSHOTS_DIR):
        return []

    files = [
        f for f in os.listdir(SCREENSHOTS_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    files = sorted(files, key=sort_key)

    entries = []
    for filename in files:
        label = filename
        timestamp = ""
        file_path = os.path.join(SCREENSHOTS_DIR, filename)

        match = FRAME_NAME_PATTERN.match(filename)
        if match:
            label = f"{SCREENSHOT_PREFIX}({int(match.group(1))})"
            timestamp = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            ).strftime("%Y-%m-%d %H:%M:%S")
        else:
            try:
                timestamp = datetime.datetime.strptime(
                    os.path.splitext(filename)[0], "%Y%m%d_%H%M%S"
                ).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                timestamp = ""

        entries.append({
            "filename": filename,
            "label": label,
            "timestamp": timestamp,
        })

    return entries


def write_output(entries):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    entries = build_entries()
    write_output(entries)
    print(f"{OUTPUT_FILE} created with {len(entries)} entries")
>>>>>>> origin/main
