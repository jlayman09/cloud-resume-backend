resource "aws_dynamodb_table" "visitor_counter" {
  name         = "MyResumeViewCount"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}
resource "aws_apigatewayv2_api" "visitor_counter_api" {
  name          = "MyResumeViewCount-API"
  protocol_type = "HTTP"
  description = "Created by AWS Lambda"

  cors_configuration {
    allow_credentials = false
    allow_headers     = []
    allow_methods     = ["GET", "OPTIONS"]
    allow_origins     = [
      "https://jonathanlayman.com",
      "https://www.jonathanlayman.com",
    ]
    expose_headers = []
    max_age        = 300
  }
}
resource "aws_lambda_function" "visitor_counter" {
  function_name = "MyResumeViewCount"
  role = data.aws_iam_role.visitor_counter_role.arn

  handler = "lambda_function.lambda_handler"
  runtime = "python3.13"

  filename = "placeholder.zip"

  memory_size   = 128
  timeout       = 3
  architectures = ["x86_64"]
  package_type  = "Zip"

  ephemeral_storage {
    size = 512
  }

  tracing_config {
    mode = "PassThrough"
  }

  lifecycle {
    ignore_changes = [
      filename,
      runtime
    ]
  }
}