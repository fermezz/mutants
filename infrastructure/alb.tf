resource "aws_alb" "mutants_alb" {
  name            = "mutants-alb"
  subnets         = [aws_subnet.mutants_vpc_subnet_a.id, aws_subnet.mutants_vpc_subnet_b.id]
  security_groups = [aws_security_group.mutants_vpc_security_group.id]
  internal        = false
}

resource "aws_alb_listener" "mutants_alb_listener" {
  load_balancer_arn = aws_alb.mutants_alb.arn
  port              = "80"
  protocol          = "HTTP"
  
  default_action {
    target_group_arn = aws_alb_target_group.mutants_alb_target_group.arn
    type             = "forward"
  }
}

resource "aws_alb_target_group" "mutants_alb_target_group" {
  name     = "mutants-alb-target-group"
  port     = "80"
  protocol = "HTTP"
  vpc_id   = aws_vpc.mutants_vpc.id

  health_check {
    healthy_threshold   = 3
    unhealthy_threshold = 10
    timeout             = 5
    interval            = 10
    path                = "/api/stats/"
  }
}

output "mutants_alb_dns_name" {
  value = "${aws_alb.mutants_alb.dns_name}"
}
