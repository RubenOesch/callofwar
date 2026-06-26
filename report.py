import os
import glob
import datetime
import config

log_path = os.path.join(config.BASE_DIR, "log.txt")
screenshot_pattern = os.path.join(config.SCREENSHOTS_DIR, "*.png")

screenshots = sorted(glob.glob(screenshot_pattern))
log_lines = []
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        log_lines = [line.strip() for line in f if line.strip()]

print("Nachtbericht")
print("----------------")
print(f"Screenshot-Ordner: {config.SCREENSHOTS_DIR}")
print(f"Gespeicherte Screenshots: {len(screenshots)}")

if screenshots:
    first = os.path.basename(screenshots[0])
    last = os.path.basename(screenshots[-1])
    try:
        first_dt = datetime.datetime.strptime(first[:-4], "%Y%m%d_%H%M%S")
        last_dt = datetime.datetime.strptime(last[:-4], "%Y%m%d_%H%M%S")
        duration = last_dt - first_dt
        print(f"Zeitraum: {first_dt.strftime('%Y-%m-%d %H:%M:%S')} bis {last_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Dauer: {duration}")
    except ValueError:
        pass

if log_lines:
    print("\nProtokoll:")
    for line in log_lines[-20:]:
        print(line)
