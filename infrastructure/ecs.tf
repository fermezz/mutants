# ------ ECS Cluster ------- #
resource "aws_ecs_cluster" "mutants_ecs_cluster" {
  name = "mutants_ecs_production"
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
  execution_role_arn    = aws_iam_role.ecs_task_execution_role.arn
}
