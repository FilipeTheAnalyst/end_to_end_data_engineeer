# Runbook

## Local development
1. Start stack: `./scripts/bootstrap.sh`
2. Run extract: `./scripts/local_extract.sh`
3. Configure Airbyte connections (see `ingestion/airbyte/README.md`)
4. Configure dbt profile (see `transform/dbt/README.md`)
5. Run dbt: `cd transform/dbt && dbt build`

## Troubleshooting
- Airbyte uses significant resources; if it fails to start, increase Docker Desktop memory/CPU.
- Last.fm API failures: check API key + reduce pages/limit.
