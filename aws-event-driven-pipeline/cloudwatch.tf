resource "aws_cloudwatch_log_group" "ingest_logs" {
  name              = "/aws/lambda/${var.project_name}-ingest"
  retention_in_days = 7
}

resource "aws_cloudwatch_log_group" "report_logs" {
  name              = "/aws/lambda/${var.project_name}-report"
  retention_in_days = 7
}
