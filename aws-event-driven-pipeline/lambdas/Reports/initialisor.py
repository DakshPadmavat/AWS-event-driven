import json
import logging
import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = os.environ.get("TABLE_NAME")
REPORT_BUCKET = os.environ.get("REPORT_BUCKET")

def lambda_handler(event, context):
    logger.info("Daily Report Lambda triggered")

    try:
        table = dynamodb.Table(TABLE_NAME)
        response = table.scan()
        items = response.get("Items", [])

        report = {
            "date": datetime.utcnow().isoformat(),
            "total_events": len(items)
        }

        report_key = f"reports/daily-report-{datetime.utcnow().date()}.json"

        s3.put_object(
            Bucket=REPORT_BUCKET,
            Key=report_key,
            Body=json.dumps(report)
        )

        logger.info(f"Report generated: {report_key}")

        return {
            "statusCode": 200,
            "body": json.dumps(report)
        }

    except ClientError as aws_error:
        logger.error(f"AWS ClientError: {aws_error}", exc_info=True)

    except Exception as e:
        logger.error(f"Unhandled exception: {e}", exc_info=True)

    return {
        "statusCode": 500,
        "body": "Failed to generate report"
    }
