terraform {
  required_version = ">= 1.5.0"
  required_providers {
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = ">= 0.80.0"
    }
  }
}

provider "snowflake" {
  # Configure via environment variables (recommended):
  # SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ROLE
}

resource "snowflake_database" "analytics" {
  name = var.database
}

resource "snowflake_schema" "lastfm" {
  database = snowflake_database.analytics.name
  name     = var.schema
}

resource "snowflake_warehouse" "ingest" {
  name           = var.ingest_warehouse
  warehouse_size = "XSMALL"
  auto_suspend   = 60
}

resource "snowflake_warehouse" "transform" {
  name           = var.transform_warehouse
  warehouse_size = "XSMALL"
  auto_suspend   = 60
}
