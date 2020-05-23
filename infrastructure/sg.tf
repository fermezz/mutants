# Create the Security Group
resource "aws_security_group" "mutants_vpc_security_group" {
  description  = "Security Group for mutants_vpc"
  name         = "mutants_vpc_security_group"
  vpc_id       = aws_vpc.mutants_vpc.id
  
  # allow ingress of all ports for now
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  } 
  
  # allow egress of all ports
  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  }
}
