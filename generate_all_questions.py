"""
Comprehensive Question Generator for Multi-Cloud Certification Platform
Generates 300+ professional questions for each certification path:
- AWS Developer Associate (DVA-C02)
- AWS AI Practitioner (AIF-C01)
- Azure Developer Associate (AZ-204)
- Azure AI Engineer Associate (AI-102)
"""

import json
import random
from pathlib import Path

def load_existing_questions(filepath):
    """Load existing questions to avoid duplication"""
    if Path(filepath).exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_questions(questions, filepath):
    """Save questions to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(questions)} questions to {filepath}")

# ==================== AWS DEVELOPER QUESTIONS ====================

AWS_DEVELOPER_QUESTIONS = [
    # Lambda & Serverless
    {
        "question": "You need to increase the memory allocation for a Lambda function. What else will be affected?",
        "options": [
            "CPU allocation increases proportionally",
            "Execution timeout increases",
            "Nothing else changes",
            "Network bandwidth decreases"
        ],
        "answer": "CPU allocation increases proportionally",
        "explanation": "AWS Lambda allocates CPU power linearly in proportion to the amount of memory configured. More memory means more CPU power."
    },
    {
        "question": "What is the maximum execution duration for an AWS Lambda function?",
        "options": [
            "5 minutes",
            "10 minutes",
            "15 minutes",
            "30 minutes"
        ],
        "answer": "15 minutes",
        "explanation": "The maximum execution duration for a Lambda function is 15 minutes (900 seconds)."
    },
    {
        "question": "How can you provide AWS credentials to a Lambda function securely?",
        "options": [
            "Hard-code them in the function code",
            "Store them in environment variables",
            "Use an IAM execution role",
            "Pass them as function parameters"
        ],
        "answer": "Use an IAM execution role",
        "explanation": "The best practice is to use an IAM execution role attached to the Lambda function. This provides temporary credentials automatically."
    },
    {
        "question": "Which Lambda invocation type is asynchronous?",
        "options": [
            "RequestResponse",
            "Event",
            "DryRun",
            "Synchronous"
        ],
        "answer": "Event",
        "explanation": "The 'Event' invocation type is asynchronous. Lambda queues the event and returns immediately with a 202 status."
    },
    {
        "question": "What service can you use to orchestrate multiple Lambda functions into a workflow?",
        "options": [
            "AWS Batch",
            "AWS Step Functions",
            "AWS Glue",
            "AWS Data Pipeline"
        ],
        "answer": "AWS Step Functions",
        "explanation": "AWS Step Functions lets you coordinate multiple AWS services including Lambda into serverless workflows."
    },
    
    # DynamoDB
    {
        "question": "What is the default consistency model for DynamoDB read operations?",
        "options": [
            "Strong consistency",
            "Eventual consistency",
            "Immediate consistency",
            "Transactional consistency"
        ],
        "answer": "Eventual consistency",
        "explanation": "By default, DynamoDB uses eventually consistent reads. You can request strongly consistent reads explicitly."
    },
    {
        "question": "Which DynamoDB operation allows you to retrieve multiple items efficiently?",
        "options": [
            "Scan",
            "Query",
            "BatchGetItem",
            "GetItem"
        ],
        "answer": "BatchGetItem",
        "explanation": "BatchGetItem allows you to retrieve up to 100 items or 16 MB of data from one or more tables in a single operation."
    },
    {
        "question": "What is a DynamoDB Global Secondary Index (GSI)?",
        "options": [
            "An index with the same partition key as the table",
            "An index with a different partition key and optional sort key",
            "An index that spans multiple regions",
            "A read-only replica of the table"
        ],
        "answer": "An index with a different partition key and optional sort key",
        "explanation": "A GSI allows you to query using a different partition key and sort key than the base table."
    },
    {
        "question": "How can you handle a ProvisionedThroughputExceededException in DynamoDB?",
        "options": [
            "Increase the table's provisioned capacity",
            "Implement exponential backoff retry logic",
            "Switch to on-demand billing mode",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "You can handle throughput exceptions by increasing capacity, implementing retries with exponential backoff, or using on-demand mode."
    },
    {
        "question": "What is DynamoDB Streams used for?",
        "options": [
            "Backing up tables",
            "Capturing item-level changes in a table",
            "Monitoring table performance",
            "Encrypting data at rest"
        ],
        "answer": "Capturing item-level changes in a table",
        "explanation": "DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table."
    },
    
    # API Gateway
    {
        "question": "Which API Gateway integration type forwards the request to an AWS Lambda function?",
        "options": [
            "HTTP",
            "AWS",
            "AWS_PROXY",
            "MOCK"
        ],
        "answer": "AWS_PROXY",
        "explanation": "AWS_PROXY (Lambda Proxy Integration) forwards the entire request to Lambda and returns the response directly to the client."
    },
    {
        "question": "How can you protect your API from being overwhelmed by too many requests?",
        "options": [
            "Implement caching",
            "Use throttling settings",
            "Enable CORS",
            "Use API keys"
        ],
        "answer": "Use throttling settings",
        "explanation": "API Gateway throttling allows you to set rate limits and burst limits to protect your backend from being overwhelmed."
    },
    {
        "question": "What is the purpose of API Gateway stages?",
        "options": [
            "To manage different versions of your API",
            "To cache responses",
            "To authenticate users",
            "To transform requests"
        ],
        "answer": "To manage different versions of your API",
        "explanation": "Stages allow you to manage multiple versions (dev, test, prod) of your API simultaneously."
    },
    {
        "question": "Which authentication mechanism integrates with API Gateway for securing APIs?",
        "options": [
            "IAM roles and policies",
            "Amazon Cognito User Pools",
            "Lambda authorizers",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "API Gateway supports IAM authentication, Cognito User Pools, and custom Lambda authorizers."
    },
    
    # S3
    {
        "question": "Which S3 storage class is most cost-effective for infrequently accessed data?",
        "options": [
            "S3 Standard",
            "S3 Intelligent-Tiering",
            "S3 Standard-IA",
            "S3 Glacier"
        ],
        "answer": "S3 Standard-IA",
        "explanation": "S3 Standard-Infrequent Access (IA) is designed for data that is accessed less frequently but requires rapid access when needed."
    },
    {
        "question": "How can you enable versioning on an existing S3 bucket?",
        "options": [
            "You must create a new bucket with versioning enabled",
            "Update the bucket configuration in the S3 console or via API",
            "It's enabled by default",
            "Contact AWS Support"
        ],
        "answer": "Update the bucket configuration in the S3 console or via API",
        "explanation": "You can enable versioning on an existing bucket through the console, CLI, or API at any time."
    },
    {
        "question": "What happens when you delete an object in a versioning-enabled S3 bucket?",
        "options": [
            "The object is permanently deleted",
            "A delete marker is placed",
            "The bucket is locked",
            "An error is returned"
        ],
        "answer": "A delete marker is placed",
        "explanation": "In a versioning-enabled bucket, deleting an object creates a delete marker, but the object versions remain."
    },
    {
        "question": "Which S3 feature automatically moves objects between storage classes?",
        "options": [
            "S3 Replication",
            "S3 Lifecycle Policies",
            "S3 Inventory",
            "S3 Analytics"
        ],
        "answer": "S3 Lifecycle Policies",
        "explanation": "S3 Lifecycle policies allow you to automatically transition objects to different storage classes or delete them based on rules."
    },
    {
        "question": "How can you secure S3 objects from public access?",
        "options": [
            "Enable S3 Block Public Access",
            "Use bucket policies",
            "Use IAM policies",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "You can secure S3 objects using Block Public Access, bucket policies, IAM policies, and ACLs."
    },
    
    # IAM & Security
    {
        "question": "What is the principle of least privilege in IAM?",
        "options": [
            "Grant maximum permissions by default",
            "Grant only the permissions required to perform a task",
            "Use root account for all operations",
            "Share credentials across users"
        ],
        "answer": "Grant only the permissions required to perform a task",
        "explanation": "The principle of least privilege means granting only the minimum permissions necessary to perform required tasks."
    },
    {
        "question": "Which IAM entity should you use for applications running on EC2?",
        "options": [
            "IAM User with access keys",
            "IAM Role",
            "Root account",
            "IAM Group"
        ],
        "answer": "IAM Role",
        "explanation": "Use IAM roles for EC2 instances. This provides temporary credentials and follows security best practices."
    },
    {
        "question": "What service should you use to store database credentials securely?",
        "options": [
            "S3",
            "DynamoDB",
            "AWS Secrets Manager",
            "CloudWatch Logs"
        ],
        "answer": "AWS Secrets Manager",
        "explanation": "AWS Secrets Manager helps you protect secrets needed to access applications, services, and IT resources."
    },
    {
        "question": "How can you rotate secrets automatically in AWS?",
        "options": [
            "Manually update them monthly",
            "Use AWS Secrets Manager rotation",
            "Store them in environment variables",
            "Hard-code them in application"
        ],
        "answer": "Use AWS Secrets Manager rotation",
        "explanation": "Secrets Manager can automatically rotate secrets for supported AWS services using Lambda functions."
    },
    
    # CloudFormation
    {
        "question": "What format can CloudFormation templates be written in?",
        "options": [
            "JSON only",
            "YAML only",
            "JSON or YAML",
            "XML only"
        ],
        "answer": "JSON or YAML",
        "explanation": "CloudFormation templates can be written in either JSON or YAML format."
    },
    {
        "question": "What happens when you delete a CloudFormation stack?",
        "options": [
            "Only the template is deleted",
            "All resources in the stack are deleted",
            "Resources are archived",
            "Nothing happens"
        ],
        "answer": "All resources in the stack are deleted",
        "explanation": "Deleting a stack deletes all resources that were created by that stack (unless protected by DeletionPolicy)."
    },
    {
        "question": "How can you prevent a resource from being deleted when the stack is deleted?",
        "options": [
            "Use DeletionPolicy: Retain",
            "Use UpdatePolicy",
            "Use CreationPolicy",
            "Use Condition"
        ],
        "answer": "Use DeletionPolicy: Retain",
        "explanation": "The DeletionPolicy: Retain attribute preserves a resource when its stack is deleted."
    },
    
    # CI/CD
    {
        "question": "Which AWS service provides managed CI/CD pipelines?",
        "options": [
            "AWS CodePipeline",
            "AWS CodeCommit",
            "AWS CodeBuild",
            "AWS CodeDeploy"
        ],
        "answer": "AWS CodePipeline",
        "explanation": "CodePipeline is a continuous delivery service that orchestrates build, test, and deployment processes."
    },
    {
        "question": "What file defines the build specifications for AWS CodeBuild?",
        "options": [
            "build.yaml",
            "buildspec.yml",
            "codebuild.json",
            "config.yml"
        ],
        "answer": "buildspec.yml",
        "explanation": "CodeBuild uses a buildspec.yml file to define build commands and settings."
    },
    {
        "question": "Which CodeDeploy deployment configuration deploys to half of instances at a time?",
        "options": [
            "AllAtOnce",
            "HalfAtATime",
            "OneAtATime",
            "CodeDeployDefault.HalfAtATime"
        ],
        "answer": "CodeDeployDefault.HalfAtATime",
        "explanation": "CodeDeployDefault.HalfAtATime deploys to up to half of the instances at a time."
    },
]

# Generate more AWS Developer questions programmatically
def generate_more_aws_developer_questions():
    """Generate additional AWS Developer questions to reach 300+"""
    additional_questions = []
    
    # Add more questions for each major service
    services = {
        "ECS": [
            ("What launch type runs containers on your managed infrastructure?", 
             ["Fargate", "EC2", "Lambda", "EKS"], "EC2",
             "EC2 launch type runs containers on EC2 instances that you manage."),
            ("What is AWS Fargate?",
             ["A container orchestrator", "A serverless compute engine for containers", "A Docker registry", "A load balancer"],
             "A serverless compute engine for containers",
             "Fargate is a serverless compute engine that lets you run containers without managing servers."),
        ],
        "RDS": [
            ("What is the maximum retention period for automated RDS backups?",
             ["7 days", "30 days", "35 days", "90 days"], "35 days",
             "Automated backups can be retained for up to 35 days."),
            ("Which RDS feature provides read scaling?",
             ["Multi-AZ", "Read Replicas", "Backup retention", "Parameter groups"],
             "Read Replicas",
             "Read replicas allow you to scale read operations by routing read traffic to replica instances."),
        ],
        "ElastiCache": [
            ("Which ElastiCache engine supports pub/sub messaging?",
             ["Memcached", "Redis", "Both", "Neither"], "Redis",
             "Redis supports pub/sub messaging patterns, while Memcached does not."),
            ("What is the benefit of using ElastiCache?",
             ["Reduced database load", "Faster data retrieval", "Improved application performance", "All of the above"],
             "All of the above",
             "ElastiCache reduces database load, provides faster data access, and improves overall application performance."),
        ],
        "SQS": [
            ("What is the maximum message retention period in SQS?",
             ["1 day", "7 days", "14 days", "30 days"], "14 days",
             "SQS can retain messages for up to 14 days."),
            ("What type of SQS queue guarantees message order?",
             ["Standard queue", "FIFO queue", "Priority queue", "Dead-letter queue"],
             "FIFO queue",
             "FIFO (First-In-First-Out) queues preserve the exact order in which messages are sent and received."),
        ],
        "SNS": [
            ("What protocol does SNS NOT support for notifications?",
             ["HTTP/HTTPS", "Email", "FTP", "SMS"], "FTP",
             "SNS supports HTTP/HTTPS, Email, SMS, SQS, Lambda, and mobile push, but not FTP."),
        ],
        "CloudWatch": [
            ("What is the default metric interval for EC2 instances?",
             ["1 minute", "5 minutes", "10 minutes", "15 minutes"], "5 minutes",
             "By default, EC2 sends metric data to CloudWatch in 5-minute intervals."),
            ("How can you create custom metrics in CloudWatch?",
             ["Using PutMetricData API", "Through the console only", "Automatically", "It's not possible"],
             "Using PutMetricData API",
             "You can publish your own custom metrics to CloudWatch using the PutMetricData API."),
        ],
        "X-Ray": [
            ("What does AWS X-Ray help you do?",
             ["Monitor application performance", "Debug distributed applications", "Trace requests", "All of the above"],
             "All of the above",
             "X-Ray helps you analyze and debug distributed applications, trace requests, and monitor performance."),
        ],
        "Cognito": [
            ("Which Cognito service provides user authentication?",
             ["User Pools", "Identity Pools", "Both", "Neither"], "User Pools",
             "Cognito User Pools provide authentication (sign-up, sign-in) for your app users."),
            ("What does Cognito Identity Pools provide?",
             ["Authentication", "Authorization and AWS credentials", "User management", "MFA"],
             "Authorization and AWS credentials",
             "Identity Pools provide AWS credentials for accessing other AWS services."),
        ],
    }
    
    for service, questions in services.items():
        for q in questions:
            additional_questions.append({
                "question": q[0],
                "options": q[1],
                "answer": q[2],
                "explanation": q[3]
            })
    
    return additional_questions

# ==================== AWS AI QUESTIONS ====================

AWS_AI_QUESTIONS = [
    {
        "question": "What is Amazon SageMaker primarily used for?",
        "options": [
            "Database management",
            "Building, training, and deploying machine learning models",
            "Content delivery",
            "Identity management"
        ],
        "answer": "Building, training, and deploying machine learning models",
        "explanation": "SageMaker is a fully managed service that provides tools to build, train, and deploy ML models at scale."
    },
    {
        "question": "Which Amazon service can analyze images and detect objects?",
        "options": [
            "Amazon Comprehend",
            "Amazon Rekognition",
            "Amazon Transcribe",
            "Amazon Translate"
        ],
        "answer": "Amazon Rekognition",
        "explanation": "Amazon Rekognition provides computer vision capabilities to analyze images and videos."
    },
    {
        "question": "What service would you use to extract text from scanned documents?",
        "options": [
            "Amazon Textract",
            "Amazon Polly",
            "Amazon Lex",
            "Amazon Comprehend"
        ],
        "answer": "Amazon Textract",
        "explanation": "Amazon Textract automatically extracts text, handwriting, and data from scanned documents."
    },
    {
        "question": "Which service converts text to lifelike speech?",
        "options": [
            "Amazon Transcribe",
            "Amazon Polly",
            "Amazon Lex",
            "Amazon Translate"
        ],
        "answer": "Amazon Polly",
        "explanation": "Amazon Polly is a text-to-speech service that uses advanced deep learning to synthesize natural-sounding speech."
    },
    {
        "question": "What is Amazon Comprehend used for?",
        "options": [
            "Speech recognition",
            "Natural language processing and text analysis",
            "Image recognition",
            "Video analysis"
        ],
        "answer": "Natural language processing and text analysis",
        "explanation": "Amazon Comprehend uses NLP to extract insights from text, including sentiment, entities, and key phrases."
    },
    {
        "question": "Which service helps you build conversational interfaces?",
        "options": [
            "Amazon Lex",
            "Amazon Polly",
            "Amazon Rekognition",
            "Amazon Textract"
        ],
        "answer": "Amazon Lex",
        "explanation": "Amazon Lex is a service for building conversational interfaces using voice and text."
    },
    {
        "question": "What is Amazon Forecast used for?",
        "options": [
            "Weather prediction",
            "Time-series forecasting using machine learning",
            "Cost estimation",
            "Resource planning"
        ],
        "answer": "Time-series forecasting using machine learning",
        "explanation": "Amazon Forecast uses machine learning to deliver highly accurate forecasts based on time-series data."
    },
    {
        "question": "Which principle is part of responsible AI?",
        "options": [
            "Maximize profit only",
            "Fairness and bias mitigation",
            "Collect maximum data",
            "Deploy without testing"
        ],
        "answer": "Fairness and bias mitigation",
        "explanation": "Responsible AI includes principles like fairness, transparency, privacy, and accountability."
    },
]

def generate_more_aws_ai_questions():
    """Generate additional AWS AI questions"""
    topics = {
        "SageMaker": [
            ("What is a SageMaker notebook instance?", 
             ["A virtual machine", "A managed Jupyter notebook", "A database", "A storage service"],
             "A managed Jupyter notebook",
             "SageMaker notebook instances are managed Jupyter notebooks for data exploration and model development."),
            ("What is SageMaker Autopilot?",
             ["Manual model training", "Automated machine learning (AutoML)", "Data labeling service", "Model monitoring"],
             "Automated machine learning (AutoML)",
             "SageMaker Autopilot automatically builds, trains, and tunes ML models."),
        ],
        "AI Services": [
            ("What does Amazon Personalize do?",
             ["Customizes EC2 instances", "Provides personalized recommendations", "Configures IAM policies", "Manages user accounts"],
             "Provides personalized recommendations",
             "Amazon Personalize creates individualized recommendations for customers using machine learning."),
            ("Which service detects inappropriate content in images?",
             ["Amazon Comprehend", "Amazon Rekognition Content Moderation", "Amazon Textract", "Amazon Polly"],
             "Amazon Rekognition Content Moderation",
             "Rekognition can detect inappropriate, unwanted, or offensive content in images and videos."),
        ],
    }
    
    additional_questions = []
    for topic, questions in topics.items():
        for q in questions:
            additional_questions.append({
                "question": q[0],
                "options": q[1],
                "answer": q[2],
                "explanation": q[3]
            })
    
    return additional_questions

print("=" * 70)
print("MULTI-CLOUD CERTIFICATION QUESTION GENERATOR")
print("Generating 300+ questions per certification path")
print("=" * 70)

# Load existing questions
print("\n📊 Loading existing questions...")
aws_dev_existing = load_existing_questions('questions_aws_developer.json')
aws_ai_existing = load_existing_questions('questions_aws_ai.json')
azure_dev_existing = load_existing_questions('questions_azure_developer.json')
azure_ai_existing = load_existing_questions('questions_azure_ai.json')

print(f"  AWS Developer: {len(aws_dev_existing)} existing")
print(f"  AWS AI: {len(aws_ai_existing)} existing")
print(f"  Azure Developer: {len(azure_dev_existing)} existing")
print(f"  Azure AI: {len(azure_ai_existing)} existing")

# This script provides the framework
# For production, you'd want to generate all 300+ questions
# For now, showing the structure and some samples

print("\n⚠️  Note: This is a framework script.")
print("For full 300+ questions per path, you'll need to:")
print("1. Expand the question templates")
print("2. Add more service-specific questions")
print("3. Validate all questions for accuracy")
print("\nCurrently showing structure with sample questions.")

