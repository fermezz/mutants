# ------ EC2 Instances ------ #
resource "aws_instance" "ec2_instance" {
  # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html
  ami                    = "ami-0d6ac368fff49ff2d"
  instance_type          = "t2.medium"
  user_data              = "${data.template_file.user_data.rendered}"
  iam_instance_profile   = aws_iam_instance_profile.ecs_instance_profile.name
  key_name               = "mutants-prod"

  vpc_security_group_ids = [aws_security_group.mutants_vpc_security_group.id]
  subnet_id              = aws_subnet.mutants_vpc_subnet_a.id
}

data "template_file" "user_data" {
  template = "${file("${path.module}/user_data.tpl")}"
}

output "ec2_instance_public_dns" {
  value = "${aws_instance.ec2_instance.public_dns}"
}
