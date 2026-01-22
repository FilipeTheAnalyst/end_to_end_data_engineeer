variable "snowflake_account" {
  type        = string
  description = "Snowflake account identifier"
}

variable "database" {
  type        = string
  description = "Analytics database"
  default     = "ANALYTICS"
}

variable "schema" {
  type        = string
  description = "Target schema"
  default     = "LASTFM"
}

variable "ingest_warehouse" {
  type        = string
  default     = "INGEST_WH"
}

variable "transform_warehouse" {
  type        = string
  default     = "TRANSFORM_WH"
}
