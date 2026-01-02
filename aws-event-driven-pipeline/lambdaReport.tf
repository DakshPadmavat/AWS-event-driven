resource "aws_lambda_function" "report" {
  function_name = "event-driven-report"
  runtime       = "python3.10"
  handler       = "initialisor.handler"

  role = "arn:aws:iam::677276092681:role/lambda_role"

  filename         = "../lambdas/Reports/report.zip"
  source_code_hash = filebase64sha256("../lambdas/Reports/initialisor.py")
}
