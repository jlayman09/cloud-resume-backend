# Cloud Resume Backend

This repository contains the serverless backend powering my personal website as part of the **AWS Cloud Resume Challenge**.

The backend is responsible for tracking website visitors using a serverless architecture built with AWS Lambda, DynamoDB, and API Gateway. This project is part of my effort to move beyond theoretical certifications and build a working cloud architecture from the ground up.

---

# Architecture Overview

User Browser  
↓  
CloudFront CDN  
↓  
S3 Static Website  
↓  
JavaScript API Call  
↓  
API Gateway (HTTP API)  
↓  
AWS Lambda (Python)  
↓  
DynamoDB

---

# Repository Structure
cloud-resume-backend
│
├── lambda
│ └── visitor_counter.py
│
├── terraform
│ └── main.tf
│
└── docs
└── system-overview.md


---

# Backend Components

### AWS Lambda

The visitor counter is powered by a Python AWS Lambda function that increments a DynamoDB value each time the website is loaded.

### Amazon DynamoDB

DynamoDB stores the total visitor count using a simple key-value structure.

Example record:
id: "views"
count: <number>


### Amazon API Gateway

API Gateway exposes a public HTTP endpoint that allows the frontend JavaScript code to retrieve the updated visitor count.

---

# Technologies Used

- AWS Lambda (Python)
- Amazon DynamoDB
- Amazon API Gateway
- Amazon S3
- Amazon CloudFront
- Route 53
- GitHub
- Terraform (Infrastructure as Code – in progress)

---

# Purpose of This Repository

This repository contains the **backend logic and infrastructure** for my Cloud Resume Challenge project. It is designed to demonstrate real-world cloud engineering concepts including:

- Serverless architecture
- API integration
- Infrastructure as Code
- Cloud security best practices
- CI/CD workflows

---

# Related Repository

The frontend website is located here:

**Frontend Repository**
https://github.com/jlayman09/Layman_CloudResumeWebsite


This repository contains the static website, frontend code, and CI/CD pipeline used to deploy the site to AWS.

---

# Future Improvements

- Full Terraform infrastructure deployment
- Email contact form using AWS Lambda
- Additional monitoring and logging with CloudWatch