output "ecr_mutants_repository_url" {
  value = "${aws_ecr_repository.ecr_mutants_api.repository_url}"
}

output "mutants_alb_dns_name" {
  value = "${aws_alb.mutants_alb.dns_name}"
}
