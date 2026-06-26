import os
import time
import datetime
import pyautogui
from PIL import ImageChops
import config

try:
    import ctypes
    HAS_CTYPES = True
except ImportError:
    HAS_CTYPES = False


def ensure_screenshot_dir():
    os.makedirs(config.SCREENSHOTS_DIR, exist_ok=True)


def get_active_window_title() -> str:
    """Get active window title, with fallback for systems where getActiveWindow fails."""
    try:
        if HAS_CTYPES:
            import ctypes
            GetWindowText = ctypes.windll.user32.GetWindowTextW
            GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
            hwnd = GetForegroundWindow()
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buf = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buf, length + 1)
            return buf.value or ""
        else:
            window = pyautogui.getActiveWindow()
            if window is None:
                return ""
            return window.title or ""
    except Exception:
        return ""


def has_changed(img, last) -> bool:
    diff = ImageChops.difference(img, last)
    if not diff.getbbox():
        return False

    if config.SKIP_IDENTICAL:
        stat = diff.convert("L").histogram()
        squares = [(i ** 2) * count for i, count in enumerate(stat)]
        rms = (sum(squares) / float(img.size[0] * img.size[1])) ** 0.5
        return rms >= config.DIFF_THRESHOLD

    return True


def save_screenshot(img):
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S.png")
    path = os.path.join(config.SCREENSHOTS_DIR, filename)
    img.save(path)

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now.isoformat(sep=' ')} - screenshot saved: {filename}\n")

    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Screenshot gespeichert: {filename}")


def main():
    ensure_screenshot_dir()
    last = None

    print("Starte Call of War Recorder")
    print(f"Speichere Screenshots in: {config.SCREENSHOTS_DIR}")
    print(f"Intervall: {config.INTERVAL_SECONDS} Sekunden")

    while True:
        try:
            title = get_active_window_title()
            title_lower = title.lower()

            if config.REQUIRED_WINDOW_TITLE or config.REQUIRED_WINDOW_URL:
                title_matches = config.REQUIRED_WINDOW_TITLE and config.REQUIRED_WINDOW_TITLE.lower() in title_lower
                url_matches = config.REQUIRED_WINDOW_URL and config.REQUIRED_WINDOW_URL.lower() in title_lower
                if not title_matches and not url_matches:
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Call of War nicht aktiv. Warte {config.INTERVAL_SECONDS}s.")
                    time.sleep(config.INTERVAL_SECONDS)
                    continue

            img = pyautogui.screenshot()

            if last is not None and config.SKIP_IDENTICAL and not has_changed(img, last):
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Keine Änderung erkannt, Bild übersprungen.")
            else:
                save_screenshot(img)

            last = img
            time.sleep(config.INTERVAL_SECONDS)
        except Exception as e:
            error_msg = f"{datetime.datetime.now().isoformat(sep=' ')} - ERROR: {type(e).__name__}: {e}"
            print(f"[FEHLER] {error_msg}")
            try:
                with open("log.txt", "a", encoding="utf-8") as f:
                    f.write(error_msg + "\n")
            except Exception:
                pass
            time.sleep(config.INTERVAL_SECONDS)


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> origin/main
