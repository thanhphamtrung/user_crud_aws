import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('lambda')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    # Logging data
    logger.info(event)
    
    #get user data by user id    
    try:
        response = table.get_item(
            Key= {
                'UserId': event.get('userid'),
            }
        )
    except ClientError as error:
        return {
            'statusCode': 400,
            'body': error.response['Error']['Message']
        }
    else:
        if(response.get('Item') is not None):
            return {
                'statusCode': 200,
                'body': response.get('Item')
            }
        else: 
            return {
                'statusCode': 404,
                'body': 'user does not exist'
            }
