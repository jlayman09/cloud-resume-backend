# Cloud Resume Backend

This repository contains the serverless backend powering my personal website as part of the **AWS Cloud Resume Challenge**.

The backend is responsible for tracking website visitors using a serverless architecture built with **AWS Lambda, DynamoDB, and API Gateway**. This project demonstrates practical cloud engineering by implementing a real production-style serverless architecture.

---

## Architecture Overview

```
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
```

---

## Repository Structure

```
cloud-resume-backend
│
├── lambda
│   └── visitor_counter.py
│
├── terraform
│   └── main.tf
│
└── docs
    └── system-overview.md
```

---

## Backend Components

### AWS Lambda

The visitor counter is powered by a Python Lambda function that increments a value in DynamoDB each time the website loads.

### Amazon DynamoDB

DynamoDB stores the total visitor count using a simple key-value structure.

Example record:

```
{
  "id": "views",
  "count": 123
}
```

### Amazon API Gateway

API Gateway exposes a public HTTP endpoint used by the website’s JavaScript to retrieve and update the visitor count.

---

## Technologies Used

* AWS Lambda (Python)
* Amazon DynamoDB
* Amazon API Gateway
* Amazon S3
* Amazon CloudFront
* Route 53
* GitHub
* Terraform (Infrastructure as Code – in progress)

---

## Purpose of This Repository

This repository contains the **backend logic and infrastructure** for my Cloud Resume Challenge project. It demonstrates several real-world cloud engineering concepts:

* Serverless architecture
* API integration
* Infrastructure as Code
* Cloud security best practices
* CI/CD workflows

---

## Related Repository

The frontend website is located here:

Frontend Repository
https://github.com/jlayman09/Layman_CloudResumeWebsite

This repository contains the static website, frontend code, and CI/CD pipeline used to deploy the site to AWS.

---

## Future Improvements

* Import existing AWS infrastructure into Terraform
* Email contact form using AWS Lambda
* CloudWatch monitoring and alerts
* Security hardening for the API endpoint
