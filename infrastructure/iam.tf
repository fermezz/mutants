# ------- IAM Roles, Policies and Profile ------- #

# ECS instance role so that EC2 instances can belong to the ECS cluster

resource "aws_iam_role" "ecs_instance_role" {
  name               = "ecsInstanceRole"
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
  role       = aws_iam_role.ecs_instance_role.id
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_instance_profile" "ecs_instance_profile" {
  name = "ecs_instance_profile"
  role = aws_iam_role.ecs_instance_role.id
}



# Task execution role so that containers can manage secrets

resource "aws_iam_role" "ecs_task_execution_role" {
  name               = "ecsTaskExecutionRole"
  path               = "/"
  assume_role_policy = "${data.aws_iam_policy_document.ecs_task_execution_role_policy.json}"
}

data "aws_iam_policy_document" "ecs_task_execution_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy" "ecs_task_execution_role_inline_policy" {
    name = "ecsTaskExecutionRoleInlinePolicy"
    role = aws_iam_role.ecs_task_execution_role.id

    policy = <<-EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:secretsmanager:sa-east-1:642559655451:secret:mutants_api/honeycomb-Hzdad5",
        "arn:aws:secretsmanager:sa-east-1:642559655451:secret:mongodb/username-Se86Ur",
        "arn:aws:secretsmanager:sa-east-1:642559655451:secret:mongodb/password-ifibgF",
        "arn:aws:secretsmanager:sa-east-1:642559655451:secret:mongodb/hostname-b8Vn3B",
        "arn:aws:secretsmanager:sa-east-1:642559655451:secret:mongodb/database-QhdhIS",
        "arn:aws:kms:sa-east-1:642559655451:key/1cdb5f91-f0e2-4832-bf94-9129f7e8981f"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy_attachment" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}


