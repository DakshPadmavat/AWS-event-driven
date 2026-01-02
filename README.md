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

Secrets Setup
Add these GitHub repository secrets under:
Settings → Secrets and variables → Actions
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION

Deployment
git add .
git commit -m "Deploy"
git push origin main
