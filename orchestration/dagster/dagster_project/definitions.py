from __future__ import annotations

import os
import subprocess
from pathlib import Path

from dagster import asset, define_asset_job, Definitions


@asset
def lastfm_raw_extract() -> str:
    """Runs the extractor and writes raw JSONL to ./extract/output.

    This is intentionally simple scaffolding.
    """
    api_key = os.getenv("LASTFM_API_KEY")
    if not api_key:
        raise ValueError("Missing LASTFM_API_KEY")

    repo_root = Path(__file__).resolve().parents[2]
    extract_dir = repo_root / "extract"

    cmd = [
        "python",
        "-m",
        "lastfm_extract.extract_geo_top_tracks",
        "--countries",
        "Portugal",
        "United Kingdom",
        "United States",
        "--pages",
        "1",
        "--limit",
        "200",
        "--out",
        str(extract_dir / "output"),
    ]

    env = {**os.environ, "PYTHONPATH": str(extract_dir / "src")}
    subprocess.check_call(cmd, cwd=str(extract_dir), env=env)

    return str(extract_dir / "output")


@asset(deps=[lastfm_raw_extract])
def airbyte_sync_lastfm_to_snowflake() -> str:
    """Placeholder for triggering an Airbyte connection sync.

    In a real setup, call the Airbyte API (/api/v1/connections/sync) with a connection_id.
    """
    return "TODO: configure Airbyte connection + trigger via API"


@asset(deps=[airbyte_sync_lastfm_to_snowflake])
def dbt_build_lastfm() -> str:
    """Placeholder for running dbt build.

    In a real setup, run `dbt build` against Snowflake using configured profiles/secrets.
    """
    return "TODO: run dbt build"


e2e_job = define_asset_job(name="e2e_job")


definitions = Definitions(assets=[lastfm_raw_extract, airbyte_sync_lastfm_to_snowflake, dbt_build_lastfm], jobs=[e2e_job])
