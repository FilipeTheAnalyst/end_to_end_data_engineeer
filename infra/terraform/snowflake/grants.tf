# Minimal, illustrative grants.
# Expand to include users, service accounts, and least-privilege patterns.

resource "snowflake_grant_privileges_to_role" "loader_on_wh" {
  privileges        = ["USAGE", "OPERATE"]
  role_name         = snowflake_role.loader.name
  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.ingest.name
  }
}

resource "snowflake_grant_privileges_to_role" "transformer_on_wh" {
  privileges        = ["USAGE", "OPERATE"]
  role_name         = snowflake_role.transformer.name
  on_account_object {
    object_type = "WAREHOUSE"
    object_name = snowflake_warehouse.transform.name
  }
}

resource "snowflake_grant_privileges_to_role" "transformer_on_schema" {
  privileges = ["USAGE", "CREATE TABLE", "CREATE VIEW"]
  role_name  = snowflake_role.transformer.name

  on_schema {
    schema_name = "${snowflake_database.analytics.name}.${snowflake_schema.lastfm.name}"
  }
}

resource "snowflake_grant_privileges_to_role" "reader_on_schema" {
  privileges = ["USAGE"]
  role_name  = snowflake_role.reader.name

  on_schema {
    schema_name = "${snowflake_database.analytics.name}.${snowflake_schema.lastfm.name}"
  }
}
