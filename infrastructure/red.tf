resource "aws_elasticache_cluster" "mutants_red_cluster" {
  cluster_id           = "mutants-red-cluster"
  engine               = "redis"
  node_type            = "cache.t2.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis5.0"
  engine_version       = "5.0.6"
  port                 = 6379
  subnet_group_name    = aws_elasticache_subnet_group.mutants_red_cluster_subnet_group.name
  security_group_ids   = [aws_security_group.mutants_red_cluster_security_group.id]
}
