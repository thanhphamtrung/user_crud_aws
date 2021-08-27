import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    # Logging data
    logger.info(event)
    
    #get data by user id    
    try:
        response = table.scan()
    except ClientError as error:
        return {
            'statusCode': 400,
            'body': error.response['Error']['Message']
        }
    else:
        return {
            'statusCode': 200,
            'body': response.get('Items', [])
        }
        