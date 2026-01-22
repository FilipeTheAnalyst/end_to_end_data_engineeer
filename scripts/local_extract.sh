#!/usr/bin/env bash
set -euo pipefail

# Runs the extractor container and writes output to ./extract/output

if [ ! -f docker/.env ]; then
  echo "Missing docker/.env. Run: cp docker/env.example docker/.env"
  exit 1
fi

set -a
source docker/.env
set +a

docker build -t e2e-lastfm-extract ./extract

mkdir -p ./extract/output

docker run --rm \
  -e LASTFM_API_KEY="$LASTFM_API_KEY" \
  -e LASTFM_USER_AGENT="${LASTFM_USER_AGENT:-end-to-end-data-engineer}" \
  -v "$(pwd)/extract/output:/app/output" \
  e2e-lastfm-extract \
  --countries Portugal "United Kingdom" "United States" \
  --pages 1 \
  --limit 200 \
  --out /app/output
