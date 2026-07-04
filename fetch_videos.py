#!/usr/bin/env python3
"""
Fetch approved videos from africaonly.tv and pick 2 random ones for the day.

The public catalog endpoint returns YouTube videos grouped by African country.
This script flattens that catalog, randomly selects 2 videos, and writes the
result to videos.json. GitHub Actions runs it daily.
"""
import json
import random
import urllib.request
from datetime import datetime, timezone

CATALOG_URL = "https://africaonly.tv/api/catalog/approved-videos"
OUT_FILE = "videos.json"


def fetch_catalog() -> dict:
    req = urllib.request.Request(
        CATALOG_URL,
        headers={
            "Accept": "application/json",
            "User-Agent": "AfricaOnly-Daily-Videos/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize_video(video: dict) -> dict:
    youtube_id = video.get("youtubeId") or ""
    title = video.get("title") or "Untitled"
    artist = (video.get("artist") or "Unknown Artist").strip()
    genre = (video.get("genre") or "").strip()
    year = video.get("year")
    country = video.get("country", "").upper()

    # Avoid redundant or placeholder artist information
    parts = []
    is_placeholder = artist.lower() in {"unknown", "unknown artist", ""}
    if artist and artist.lower() != title.lower() and not is_placeholder:
        parts.append(artist)
    if genre:
        parts.append(genre)
    if year:
        parts.append(str(year))
    if country:
        parts.append(country)

    description = " · ".join(parts) or "Africa Only TV"

    return {
        "id": youtube_id,
        "title": title,
        "description": description,
        "country": country,
    }


def main() -> None:
    catalog = fetch_catalog()
    approved = catalog.get("approvedVideos", {})

    all_videos = []
    for country_code, videos in approved.items():
        for video in videos:
            video["country"] = country_code.upper()
            all_videos.append(video)

    # Filter out entries without a usable YouTube id
    all_videos = [v for v in all_videos if v.get("youtubeId")]

    if len(all_videos) < 2:
        raise RuntimeError(f"Only {len(all_videos)} usable video(s) found in catalog.")

    selected = random.sample(all_videos, 2)

    payload = {
        "updated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source": "https://africaonly.tv",
        "videos": [normalize_video(v) for v in selected],
    }

    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT_FILE} with {len(selected)} videos from {len(all_videos)} available.")
    for v in payload["videos"]:
        print(f" - {v['id']}: {v['title'][:70]}")


if __name__ == "__main__":
    main()
