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

resource "aws_security_group" "mutants_red_cluster_security_group" {
  description  = "Security Group for the Mutants Redis cluster"
  name         = "mutants_red_cluster_security_group"
  vpc_id       = aws_vpc.mutants_vpc.id

  # We only allow communicating with the redis cluster thru the port 6379
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 6379
    protocol    = "tcp"
    to_port     = 6379
  }

  # allow egress of all ports
  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  }
}
