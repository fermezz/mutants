#!/bin/bash

docker build -t ${AWS_ACCOUNT_ID}.dkr.ecr.sa-east-1.amazonaws.com/mutants_api:$(git rev-parse HEAD | cut -c 1-7)

aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.sa-east-1.amazonaws.com

docker push ${AWS_ACCOUNT_ID}.dkr.ecr.sa-east-1.amazonaws.com/mutants_api:$(git rev-parse HEAD | cut -c 1-7)
