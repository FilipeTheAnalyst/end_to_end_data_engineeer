#!/usr/bin/env bash
set -euo pipefail

if [ ! -f docker/.env ]; then
  cp docker/env.example docker/.env
  echo "Created docker/.env from docker/env.example"
fi

docker compose -f docker/docker-compose.yml up -d

echo "Stack started."
echo "Dagster:   http://localhost:3000"
echo "Airbyte:   http://localhost:8000"
echo "Metabase:  http://localhost:3001"
