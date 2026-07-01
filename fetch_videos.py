#!/usr/bin/env python3
"""
Pick 2 random Africa-related videos from a curated pool and write videos.json.

The list is a curated collection of publicly available YouTube videos about
Africa (travel, wildlife, culture, music, history, food). The script runs
without any API key and refreshes the selection every day via GitHub Actions.
"""
import json
import random
from datetime import datetime, timezone

OUT_FILE = "videos.json"

VIDEO_POOL = [
    {
        "id": "X2LCr7qZNgM",
        "title": "Africa: The Serengeti – Wildlife Documentary",
        "description": "A breathtaking journey through the Serengeti and its Great Migration."
    },
    {
        "id": "Y6aYx_KKM7A",
        "title": "South Africa in 4K",
        "description": "Cinematic aerial views of South Africa's diverse landscapes."
    },
    {
        "id": "p5rQHoaBzFo",
        "title": "The Hidden Cultures of Ethiopia",
        "description": "Exploring ancient tribes, traditions and landscapes of Ethiopia."
    },
    {
        "id": "f24JRU4LJ5Y",
        "title": "Morocco Travel Guide – Marrakech to Sahara",
        "description": "From bustling medinas to the dunes of the Sahara Desert."
    },
    {
        "id": "7k4GkDavc1E",
        "title": "African Street Food in Lagos, Nigeria",
        "description": "A taste of vibrant street-food culture in West Africa's biggest city."
    },
    {
        "id": "u9Dg-g7T2lE",
        "title": "Victoria Falls: The Smoke That Thunders",
        "description": "The world's largest curtain of falling water between Zambia and Zimbabwe."
    },
    {
        "id": "hQaKYlNK7Fw",
        "title": "African Safari: Big Five in Kenya",
        "description": "Lions, elephants, buffalo, leopards and rhinos in the Kenyan savannah."
    },
    {
        "id": "m3c6vJ7lQ-8",
        "title": "Ghana: History, Culture and Coast",
        "description": "From Cape Coast castles to the rhythms of Accra."
    },
    {
        "id": "kJQP7kiw5Fk",
        "title": "Desiigner – Panda",
        "description": "A globally successful track shaped by African-American culture and sound."
    },
    {
        "id": "RgKAFK5djSk",
        "title": "WizKid – Come Closer ft. Drake",
        "description": "A milestone for Afrobeats reaching a worldwide audience."
    },
    {
        "id": "9XaS93WMRQQ",
        "title": "Burna Boy – Ye",
        "description": "One of the anthems that brought Nigerian Afrobeats to the world stage."
    },
    {
        "id": "LXXQLa-5n5w",
        "title": "Madagascar: Island of Marvels",
        "description": "Unique wildlife and landscapes found nowhere else on Earth."
    },
    {
        "id": "rBxcF-r9Ibs",
        "title": "Tanzania: Kilimanjaro and Beyond",
        "description": "From Africa's highest peak to the plains below."
    },
    {
        "id": "_a7wB-4y3rM",
        "title": "Ancient Egypt: Beyond the Pyramids",
        "description": "A deeper look into one of history's greatest civilizations."
    },
    {
        "id": "Yg6U8X4_r8E",
        "title": "Namibia's Skeleton Coast",
        "description": "Dramatic desert meeting the Atlantic Ocean along Namibia's shores."
    },
    {
        "id": "dQw4w9WgXcQ",
        "title": "Rick Astley – Never Gonna Give You Up",
        "description": "A classic global hit – just for fun."
    }
]


def main() -> None:
    selected = random.sample(VIDEO_POOL, min(2, len(VIDEO_POOL)))

    payload = {
        "updated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "videos": selected,
    }

    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT_FILE} with {len(selected)} videos.")
    for v in selected:
        print(f" - {v['id']}: {v['title'][:70]}")


if __name__ == "__main__":
    main()
