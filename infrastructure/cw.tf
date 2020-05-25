resource "aws_cloudwatch_metric_alarm" "ecs_cluster_memory_reservation_upper_threshold_metric_alarm" {
  alarm_name          = "ecs_cluster_memory_reservation_upper_threshold_metric_alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "MemoryReservation"
  namespace           = "AWS/ECS"
  period              = "120"
  statistic           = "Maximum"
  threshold           = "80"

  dimensions = {
    ClusterName          = aws_ecs_cluster.mutants_ecs_cluster.name
  }

  alarm_description = "Triggers when ECS Cluster MemoryReservation is at 80% or higher."
  alarm_actions     = [
    aws_autoscaling_policy.mutants_ecs_cluster_autoscaling_up_policy.arn
  ]
}

resource "aws_cloudwatch_metric_alarm" "ecs_cluster_memory_reservation_lower_metric_alarm" {
  alarm_name          = "ecs_cluster_memory_reservation_lower_metric_alarm"
  comparison_operator = "LessThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "MemoryReservation"
  namespace           = "AWS/ECS"
  period              = "120"
  statistic           = "Maximum"
  threshold           = "40"

  dimensions          = {
    ClusterName       = aws_ecs_cluster.mutants_ecs_cluster.name
  }

  alarm_description   = "Triggers when ECS Cluster MemoryReservation is at 40% or lower."
  alarm_actions       = [
    aws_autoscaling_policy.mutants_ecs_cluster_autoscaling_down_policy.arn
  ]
}
