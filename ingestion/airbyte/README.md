# Ingestion (Airbyte)

Goal: ingest raw Last.fm extract output into **Snowflake**.

## Recommended approach (template)
Because Last.fm is a rate-limited HTTP API, a pragmatic approach is:
1. **Extract** raw JSONL locally (or in a scheduled container).
2. Use Airbyte **File** source (mounted volume, S3, or S3-compatible) to ingest into Snowflake.

If you prefer a pure Airbyte approach:
- Evaluate the Airbyte **HTTP API** source to call Last.fm directly (may require custom config or connector).

## Notes
- Keep credentials out of git.
- Store your connection JSON in `templates/` as examples only.
