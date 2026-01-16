import boto3
from app.config.config import AWS_REGION

def get_bedrock_client():
    return boto3.client(
        "bedrock-agent-runtime",
        region_name=AWS_REGION
    )
