# End-to-End Data Engineer

Last.fm API  Airbyte  Snowflake  dbt (Kimball)  Metabase  Dagster  OpenMetadata

## Architecture (high level)
1. **Extract**: Pull raw, messy JSON from the Last.fm public API.
2. **Ingestion**: Load raw data into **Snowflake** (recommended via **Airbyte**).
3. **Transformation**: Build a Kimball-style star schema using **dbt Core**.
4. **Dashboard**: Explore curated marts in **Metabase**.
5. **Orchestration**: Run end-to-end workflows with **Dagster**.
6. **Observability**: Catalog/lineage with **OpenMetadata**.

## Quickstart (local)
1. Copy environment file:

```bash
cp docker/env.example docker/.env
```

2. Start the local stack:

```bash
docker compose -f docker/docker-compose.yml up -d
```

3. Run a sample Last.fm extraction (writes raw JSONL locally):

```bash
./scripts/local_extract.sh
```

## UIs
- Dagster: http://localhost:3000
- Airbyte: http://localhost:8000
- Metabase: http://localhost:3001
- OpenMetadata: http://localhost:8585

## Repository layout
- `extract/`: Last.fm extractor (Python)
- `ingestion/airbyte/`: Airbyte templates + notes
- `transform/dbt/`: dbt project skeleton (staging/intermediate/marts)
- `orchestration/dagster/`: Dagster assets/jobs
- `observability/openmetadata/`: OpenMetadata configs/templates
- `infra/terraform/`: Snowflake RBAC + Postgres backend example
- `docker/`: Docker Compose stack

## Notes
- This repo is scaffolded to be runnable locally via Docker Compose.
- Snowflake and Last.fm credentials are provided via environment variables (see `docker/env.example`).
