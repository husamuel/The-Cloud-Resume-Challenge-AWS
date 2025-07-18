output "website_url" {
  value = "http://${aws_s3_bucket.resume_bucket.bucket}.s3-website-${var.region}.amazonaws.com"
}

output "lambda_function_name" {
  value = aws_lambda_function.visitor_counter.function_name
}
