resource "aws_acm_certificate" "cert" {
  domain_name       = "hugoleonor.com"
  validation_method = "DNS"
}

resource "aws_route53_record" "cert_validation" {
  name    = element(aws_acm_certificate.cert.domain_validation_options.*.resource_record_name, 0)
  type    = element(aws_acm_certificate.cert.domain_validation_options.*.resource_record_type, 0)
  zone_id = data.aws_route53_zone.primary.zone_id
  records = [element(aws_acm_certificate.cert.domain_validation_options.*.resource_record_value, 0)]
  ttl     = 60
}

resource "aws_acm_certificate_validation" "cert_validation" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [aws_route53_record.cert_validation.fqdn]
}
