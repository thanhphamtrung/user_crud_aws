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
 
    #create user    
    try:
        response = table.put_item(
            Item= {
                    'UserId': str(uuid.uuid1()),
                    'UserName': event.get('username'),
                    'Height': event.get('height')
                }
        )
    except ClientError as error:
        return {
            'statusCode': 400,
            'body': error.response['Error']['Message']
        }
    else:
        return {
            'statusCode': 201,
            'body': "user created succesfully"
        }
            