# ------ ECR ------- #
resource "aws_ecr_repository" "ecr_mutants_api" {
  name = "mutants_api"
}

resource "aws_ecr_repository" "ecr_nginx" {
  name = "nginx"
}
