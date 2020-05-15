#!/bin/bash

# Update all packages
# We need to install and initialize the ECS agent manually
# because we can't afford an ECS-optimized image :D

sudo yum update -y
sudo yum install -y ecs-init
sudo service docker start
sudo start ecs

echo ECS_CLUSTER=mutants_ecs_production >> /etc/ecs/ecs.config
cat /etc/ecs/ecs.config | grep "ECS_CLUSTER"
