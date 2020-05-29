# ------ EC2 Instances ------ #

data "template_file" "user_data" {
  template = "${file("${path.module}/user_data.tpl")}"
}

resource "aws_launch_configuration" "mutants_ecs_cluster_launch_configuration" {
  name                        = "mutants_ecs_cluster_launch_configuration"
  # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html
  image_id                    = "ami-0d6ac368fff49ff2d"
  instance_type               = "t2.small"
  user_data                   = "${data.template_file.user_data.rendered}"
  iam_instance_profile        = aws_iam_instance_profile.ecs_instance_profile.name
  key_name                    = "mutants-prod"

  security_groups             = [aws_security_group.mutants_vpc_security_group.id]

  root_block_device {
    volume_type = "standard"
    volume_size = 100
    delete_on_termination = true
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "mutants_ecs_cluster_autoscaling_group" {
  name                        = "mutants_ecs_cluster_autoscaling_group"
  max_size                    = 2
  min_size                    = 1
  vpc_zone_identifier         = [
    aws_subnet.mutants_vpc_subnet_a.id,
    aws_subnet.mutants_vpc_subnet_c.id
  ]
  target_group_arns           = [
    aws_alb_target_group.mutants_alb_target_group.arn
  ]
  launch_configuration        = aws_launch_configuration.mutants_ecs_cluster_launch_configuration.name
  health_check_type           = "EC2"
}

resource "aws_autoscaling_policy" "mutants_ecs_cluster_autoscaling_up_policy" {
  name                   = "mutants_ecs_cluster_autoscaling_up_policy"
  scaling_adjustment     = 1
  adjustment_type        = "ChangeInCapacity"
  cooldown               = 300
  autoscaling_group_name = aws_autoscaling_group.mutants_ecs_cluster_autoscaling_group.name
}

resource "aws_autoscaling_policy" "mutants_ecs_cluster_autoscaling_down_policy" {
  name                   = "mutants_ecs_cluster_autoscaling_down_policy"
  scaling_adjustment     = -1
  adjustment_type        = "ChangeInCapacity"
  cooldown               = 300
  autoscaling_group_name = aws_autoscaling_group.mutants_ecs_cluster_autoscaling_group.name
}
