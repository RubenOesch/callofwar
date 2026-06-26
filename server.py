import http.server
import socketserver
import json
import os
import re
import datetime
import config

FRAME_NAME_PATTERN = re.compile(rf"^{re.escape(config.SCREENSHOT_PREFIX)}\((\d+)\)\.(png|jpg|jpeg)$", re.IGNORECASE)


def parse_screenshot_entry(filename):
    name, ext = os.path.splitext(filename)
    timestamp = ""
    label = filename
    filepath = os.path.join(config.SCREENSHOTS_DIR, filename)

    # Timestamp from date-based filenames
    try:
        timestamp = datetime.datetime.strptime(name, "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        match = FRAME_NAME_PATTERN.match(filename)
        if match:
            timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "filename": filename,
        "timestamp": timestamp,
        "label": label,
    }


def screenshot_sort_key(filename):
    match = FRAME_NAME_PATTERN.match(filename)
    if match:
        return (0, int(match.group(1)), filename.lower())
    try:
        dt = datetime.datetime.strptime(os.path.splitext(filename)[0], "%Y%m%d_%H%M%S")
        return (1, dt, filename.lower())
    except ValueError:
        return (2, filename.lower())


class PlaybackHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/screenshots":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            files = []
            try:
                entries = [f for f in os.listdir(config.SCREENSHOTS_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
                for filename in sorted(entries, key=screenshot_sort_key):
                    files.append(parse_screenshot_entry(filename))
            except FileNotFoundError:
                files = []

            self.wfile.write(json.dumps(files).encode("utf-8"))
            return

        return super().do_GET()

if __name__ == "__main__":
    os.chdir(config.BASE_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", config.PORT), PlaybackHandler) as httpd:
        print(f"Playback-Server gestartet auf http://localhost:{config.PORT}")
        print(f"Screenshots werden aus {config.SCREENSHOTS_DIR} bereitgestellt")
        httpd.serve_forever()
