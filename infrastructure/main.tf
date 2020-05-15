provider "aws" {
  profile = "default"
  region  = "sa-east-1"
}

# ------ ECS Cluster ------- #
resource "aws_ecs_cluster" "mutants_ecs_cluster" {
  name = "mutants_ecs_production"
}


# ------ EC2 Instances ------ #
resource "aws_instance" "ec2_instance" {
  # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html
  ami                  = "ami-03e1e4abf50e14ded"
  instance_type        = "t2.micro"
  user_data            = "${data.template_file.user_data.rendered}"
  iam_instance_profile = aws_iam_instance_profile.ecs_instance_profile.name
  key_name             = "mutants-prod"
}

data "template_file" "user_data" {
  template = "${file("${path.module}/user_data.tpl")}"
}


output "ec2_instance_public_dns" {
  value = "${aws_instance.ec2_instance.public_dns}"
}


# ------- IAM Roles, Policies and Profile ------- #
resource "aws_iam_role" "ecs_instance_role" {
  name               = "ecs_instance_role"
  path               = "/"
  assume_role_policy = "${data.aws_iam_policy_document.ecs_instance_policy.json}"
}

data "aws_iam_policy_document" "ecs_instance_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecs_instance_role_attachment" {
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_instance_profile" "ecs_instance_profile" {
  name = "ecs_instance_profile"
  role = aws_iam_role.ecs_instance_role.name
}


# ------ ECS Service and Task Definitions ------ #
resource "aws_ecs_service" "mutants_service" {
  name            = "mutants"
  cluster         = aws_ecs_cluster.mutants_ecs_cluster.id
  launch_type     = "EC2"
  task_definition = aws_ecs_task_definition.mutants_api.arn
  desired_count   = 1
}

resource "aws_ecs_task_definition" "mutants_api" {
  family                = "mutants_stack"
  container_definitions = file("container_definitions.json")
  network_mode          = "bridge"
}


# ------ ECR ------- #
resource "aws_ecr_repository" "ecr_mutants_api" {
  name = "mutants_api"
}

resource "aws_ecr_repository" "ecr_nginx" {
  name = "nginx"
}

output "ecr_mutants_repository_url" {
  value = "${aws_ecr_repository.ecr_mutants_api.repository_url}"
}
