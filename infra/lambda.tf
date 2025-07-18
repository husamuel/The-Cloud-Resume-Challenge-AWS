resource "aws_lambda_function" "visitor_counter" {
  function_name = "visitorCounter"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_exec_role.arn

  filename         = "${path.module}/../backend/lambda_function.zip"
  source_code_hash = filebase64sha256("${path.module}/../backend/lambda_function.zip")
}
