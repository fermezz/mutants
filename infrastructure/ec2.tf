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
