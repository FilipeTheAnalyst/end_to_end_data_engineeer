# Architecture

## Building blocks
- Extract: Last.fm API -> raw JSONL files
- Ingestion: Airbyte -> Snowflake (raw landing)
- Transform: dbt Core -> Kimball star schema
- Dashboard: Metabase
- Orchestration: Dagster
- Observability: OpenMetadata
- Infra: Terraform (Snowflake RBAC) + Postgres backend

## Data flow (proposed)
1. Dagster runs `extract` container daily
2. Airbyte ingests new raw files into Snowflake landing tables
3. dbt builds staging -> intermediate -> marts
4. Metabase reads marts
5. OpenMetadata ingests metadata from Snowflake, dbt, Metabase
