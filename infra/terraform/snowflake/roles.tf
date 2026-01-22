resource "snowflake_role" "loader" {
  name = "LOADER"
}

resource "snowflake_role" "transformer" {
  name = "TRANSFORMER"
}

resource "snowflake_role" "reader" {
  name = "READER"
}
