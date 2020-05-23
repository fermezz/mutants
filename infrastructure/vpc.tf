resource "aws_vpc" "mutants_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
}

resource "aws_subnet" "mutants_vpc_subnet_a" {
  vpc_id                  = aws_vpc.mutants_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "sa-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "mutants_vpc_subnet_b" {
  vpc_id                  = aws_vpc.mutants_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "sa-east-1b"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "mutants_vpc_internet_gateway" {
  vpc_id = aws_vpc.mutants_vpc.id
}

resource "aws_route_table" "mutants_vpc_route_table" {
  vpc_id = aws_vpc.mutants_vpc.id
}

resource "aws_route" "mutants_vpc_internet_access_route" {
  route_table_id         = aws_route_table.mutants_vpc_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.mutants_vpc_internet_gateway.id
}

resource "aws_main_route_table_association" "a" {
  vpc_id         = aws_vpc.mutants_vpc.id
  route_table_id = aws_route_table.mutants_vpc_route_table.id
}

resource "aws_route_table_association" "mutants_vpc_subnet_a_association" {
  subnet_id      = aws_subnet.mutants_vpc_subnet_a.id
  route_table_id = aws_route_table.mutants_vpc_route_table.id
}

resource "aws_route_table_association" "mutants_vpc_subnet_b_association" {
  subnet_id      = aws_subnet.mutants_vpc_subnet_b.id
  route_table_id = aws_route_table.mutants_vpc_route_table.id
}
