# Extract (Last.fm)

This package pulls **raw/messy** data from the Last.fm public API.

## Endpoint used
- `geo.getTopTracks`

## Run locally
```bash
export LASTFM_API_KEY=...  # required
python -m lastfm_extract.extract_geo_top_tracks --countries Portugal "United Kingdom" --pages 1 --limit 200 --out output
```

## Output
Writes JSONL files partitioned by date/country, e.g.:

`output/run_date=2026-01-22/country=portugal/top_tracks.jsonl`
