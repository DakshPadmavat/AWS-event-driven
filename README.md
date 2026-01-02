# AWS Event-Driven Pipeline — CI/CD with GitHub Actions

## Project Overview

This project implements an AWS event-driven pipeline using:
- **API Gateway** (event ingestion)
- **AWS Lambda** (data processing)
- **Amazon S3** (raw + reports)
- **DynamoDB** (fast lookups)
- **EventBridge** (scheduled triggers)

## Continuous Integration & Delivery (CI/CD)

Used **GitHub Actions** to automate deployment:

CI/CD Workflow

- Triggered on push to `main`
- Runs Terraform to:
  - Validate
  - Plan
  - Apply infrastructure changes

Security Notice:
This repository does not contain any credentials, secrets, or Terraform state files.
AWS access is managed via IAM roles and GitHub Actions secrets following least-privilege principles.

Deployment
git add .
git commit -m "Deploy"
git push origin main(or master)
