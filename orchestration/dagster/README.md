# Orchestration (Dagster)

This is a minimal Dagster scaffold that will evolve into:
- Extract (Last.fm) asset
- Airbyte sync asset
- dbt build asset

## Run locally
From repo root:

```bash
docker compose -f docker/docker-compose.yml up -d dagster
```

Then open Dagster at http://localhost:3000
