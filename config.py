import os

# Verzeichnisse definieren
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
WEB_DIR = BASE_DIR
SCREENSHOT_PREFIX = "callofwar"
SCREENSHOT_FILENAME_TEMPLATE = f"{SCREENSHOT_PREFIX}({{}}).png"
# Sicherstellen, dass die Ordner existieren
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Aufnahme-Einstellungen
INTERVAL_SECONDS = 10             # Jede Minute ein Screenshot
REQUIRED_WINDOW_TITLE = "call of war"  # Nur aufnehmen, wenn dieser Begriff im aktiven Fenstertitel vorkommt (z.B. Browsertab)
REQUIRED_WINDOW_URL = ""          # Optional: z.B. "callofwar.com" für Browser-Tab/Titelerkennung


# Speicherfilter
SKIP_IDENTICAL = False            # Jede Minute speichern, auch wenn sich wenig ändert
DIFF_THRESHOLD = 0.5              # RMS-Schwellenwert. < 0.5 gilt als unverändert

# Server-Einstellungen
PORT = 8000                       # Port für das Playback-Dashboard
