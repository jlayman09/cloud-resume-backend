# Cloud Resume Backend Overview

This repository contains the serverless backend for my AWS Cloud Resume Challenge project.

Current components:

- AWS Lambda (Python) for the visitor counter
- Amazon DynamoDB table storing the visitor count
- Amazon API Gateway used to trigger the Lambda function
- Terraform configuration (in progress) to migrate the infrastructure to Infrastructure as Code

The backend works with the frontend static website hosted in Amazon S3 and distributed through CloudFront.