# Africa Only – Daily Random Videos

Eine statische Webanwendung, die täglich 2 zufällige Afrika-Videos anzeigt.

- **HTML/CSS/JS**-Frontend (kein Build-Schritt nötig)
- Tägliche Aktualisierung per **GitHub Actions**-Cronjob
- Automatisches Deployment auf **Vercel**

## Struktur

- `index.html` – Die Webseite
- `videos.json` – Täglich aktualisierte Videoauswahl
- `fetch_videos.py` — Python-Skript zur Auswahl der Videos
- `.github/workflows/daily-update.yml` – GitHub Actions Workflow

## Lokale Entwicklung

```bash
python3 fetch_videos.py
# Dann index.html über einen lokalen Server öffnen
python3 -m http.server 8000
```
