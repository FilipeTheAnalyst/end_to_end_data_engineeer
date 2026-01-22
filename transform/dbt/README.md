# Transform (dbt)

This is the dbt Core project.

## Modeling conventions
- `models/staging/`: 1:1 with ingested raw tables (Airbyte landing).
- `models/intermediate/`: business logic building blocks.
- `models/marts/`: Kimball star schema (dims/facts) for Metabase.

## Setup
Copy `profiles.yml.example` to your local dbt profiles location:

```bash
mkdir -p ~/.dbt
cp transform/dbt/profiles.yml.example ~/.dbt/profiles.yml
```

Then:
```bash
cd transform/dbt
dbt deps
dbt compile
```
