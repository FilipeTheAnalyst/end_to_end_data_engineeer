from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Iterable, List

from .client import LastFmClient
from .utils import env


def write_jsonl(path: Path, records: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def extract_country(client: LastFmClient, country: str, pages: int, limit: int) -> List[dict]:
    out: List[dict] = []
    for page in range(1, pages + 1):
        payload = client.geo_get_top_tracks(country=country, page=page, limit=limit)
        out.append(
            {
                "extracted_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "country": country,
                "page": page,
                "payload": payload,
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Last.fm geo.getTopTracks (raw JSONL)")
    parser.add_argument("--countries", nargs="+", default=["Portugal", "United Kingdom", "United States"])
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--out", default="output")
    args = parser.parse_args()

    api_key = env("LASTFM_API_KEY")
    user_agent = os.getenv("LASTFM_USER_AGENT", "end-to-end-data-engineer")
    client = LastFmClient(api_key=api_key, user_agent=user_agent)

    run_date = dt.date.today().isoformat()
    base = Path(args.out)

    for country in args.countries:
        safe_country = country.lower().replace(" ", "_")
        path = base / f"run_date={run_date}" / f"country={safe_country}" / "top_tracks.jsonl"
        records = extract_country(client, country=country, pages=args.pages, limit=args.limit)
        write_jsonl(path, records)
        print(f"Wrote {len(records)} records to {path}")


if __name__ == "__main__":
    main()
