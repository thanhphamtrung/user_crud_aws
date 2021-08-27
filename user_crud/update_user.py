import boto3
import logging
from botocore.exceptions import ClientError
import uuid 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    # Logging data
    logger.info(event)
    
    #update user
    try:
        response = table.update_item(
            Key={
                'UserId': event.get('userid'),
            },
            UpdateExpression="set UserName=:username, Height=:height",
            ExpressionAttributeValues={
                ':username': event.get('username'),
                ':height': event.get('height')
            },
            ReturnValues="UPDATED_NEW",
            ReturnValuesOnConditionCheckFailure="NONE"
        )
    except ClientError as error:
        return {
            'statusCode': 400,
            'body': error.response['Error']['Message']
        }
    else:
        return {
            'statusCode': 201,
            'body': "user updated succesfully"
        }
