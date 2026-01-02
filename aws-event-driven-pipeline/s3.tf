resource "aws_s3_bucket" "raw_data" {
  bucket = "${var.project_name}-raw-data"
}

resource "aws_s3_bucket" "reports" {
  bucket = "${var.project_name}-reports"
}
