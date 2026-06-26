# Call of War Replay Website

Statische GitHub Pages-Seite zur Wiedergabe gespeicherter Screenshots als Videosequenz.

## Inhalte

- `index.html` — Hauptseite
- `style.css` — Styling
- `screenshots/` — Screenshot-Bilder
- `screenshots.json` — Metadaten für die Wiedergabe

## Deployment

1. Git initialisieren:
   ```bash
   git init
   git branch -M main
   git remote add origin https://github.com/RubenOesch/callofwar.git
   git add .
   git commit -m "Initial commit for Call of War playback site"
   git push -u origin main
   ```

2. GitHub Pages aktivieren im Repository unter `Settings > Pages`.
3. Branch `main` und Root `/` auswählen.
4. Seite aufrufen unter `https://ruben.oesch.github.io/callofwar/`.
