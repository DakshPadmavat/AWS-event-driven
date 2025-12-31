import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = os.environ.get("TABLE_NAME")
BUCKET = os.environ.get("BUCKET")

def lambda_handler(event, context):
    logger.info("Ingest Lambda triggered")
    logger.info(f"Incoming event: {json.dumps(event)}")

    try:
        body = event.get("body", "{}")
        data = json.loads(body)

        event_id = data.get("event_id", context.aws_request_id)

        # Store in DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={"event_id": event_id, "payload": data})

        # Store raw event in S3
        s3.put_object(
            Bucket=BUCKET,
            Key=f"events/{event_id}.json",
            Body=json.dumps(data)
        )

        logger.info("Event stored successfully")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Event ingested successfully"})
        }

    except ClientError as aws_error:
        logger.error(f"AWS ClientError: {aws_error}", exc_info=True)
        return {
            "statusCode": 500,
            "body": "AWS service error occurred"
        }

    except Exception as e:
        logger.error(f"Unhandled exception: {e}", exc_info=True)
        return {
            "statusCode": 500,
            "body": "Internal server error"
        }

