# AWS Lambda Golden Boot Winners API

## Key Features
- **Serverless Infrastructure**: Built using **AWS Lambda** and **API Gateway** for scalable, serverless architecture.
- **Real-Time Data Processing**: Retrieves **Premier League Golden Boot winners** from 1992 to the current season.
- **Infrastructure as Code (IaC)**: Deployed entirely on AWS services, showcasing expertise in serverless computing.
- **Minimal Infrastructure Management**: Leveraging AWS API Gateway and Lambda means no traditional server management.

## Tech Stack
- **AWS Lambda**: Executes code in response to API requests, ensuring a serverless environment.
- **AWS API Gateway**: Handles REST API integration with Lambda.
- **Python**: Used for processing the data and generating responses.
- **JSON**: Outputs Premier League Golden Boot winners data in JSON format for easy consumption by front-end or other services.

## How It Works
1. **API Gateway** receives a GET request.
2. **AWS Lambda** is triggered to fetch the Premier League Golden Boot winners' data.
3. The data is returned in JSON format, structured by season, player, club, and goals.

## Key AWS Services
- **AWS Lambda**: Serverless computing for efficient, scalable, and low-cost back-end processing.
- **API Gateway**: Secure and scalable API routing.
- **IAM Roles & Policies**: Used for securely managing access control between AWS services.
- **CloudWatch**: Integrated for monitoring and logging Lambda invocations.

## API Endpoint
**Base URL**: 
https://5qn31isv88.execute-api.eu-west-2.amazonaws.com/GoldenBootWinnersAPI




