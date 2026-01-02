resource "aws_lambda_function" "ingest"{
  function_name = "event-driven-ingest"
  runtime       = "python3.10"
  handler       = "initialisor.handler"

  role = "arn:aws:iam::677276092681:role/lambda_role"

  filename         = "../lambdas/ingest/ingest.zip"
  source_code_hash = filebase64sha256("../lambdas/ingest/initialisor.py")
}

