# Terraform (Snowflake + backend)

This folder contains Terraform scaffolding for:
- Snowflake roles/warehouses/db/schema for ingestion + transformation
- Example Postgres backend for remote-ish state (local Postgres)

## Backend
See `backend/` for an example Postgres backend configuration.

## Snowflake
See `snowflake/` for starter RBAC resources.

> This is intentionally a scaffold. You will need to fill in your Snowflake account/org specifics.
