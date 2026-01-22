# Data model (Kimball draft)

## Grain
**fact_top_tracks_geo_daily**
- Grain: `date` x `country` x `track`

## Dimensions
- `dim_date` (standard calendar)
- `dim_country`
- `dim_artist`
- `dim_track`

## Facts
- `fact_top_tracks_geo_daily`
  - `rank`
  - `playcount`
  - `listeners`

## Notes
The exact schema depends on how Airbyte lands the raw payload (variant/JSON columns vs flattened). Start with minimal staging models mirroring raw payload, then normalize.
