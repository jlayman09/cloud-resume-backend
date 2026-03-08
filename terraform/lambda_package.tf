data "archive_file" "visitor_counter_zip" {
  type        = "zip"
  source_file = "../lambda/lambda_function.py"
  output_path = "${path.module}/build/visitor_counter.zip"
}