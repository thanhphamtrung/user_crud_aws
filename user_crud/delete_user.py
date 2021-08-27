import boto3
import logging
from botocore.exceptions import ClientError
import uuid 
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')
client = boto3.client('lambda')

def lambda_handler(event, context):
    # Logging data
    logger.info(event)
    
    userIdToDelete = {'userid': str(event.get('userid'))}
    
    client  = boto3.client('lambda')
    getUserResponse = client.invoke(
		FunctionName='arn:aws:lambda:us-east-2:315665109356:function:get_user_by_id',
		InvocationType='RequestResponse',
		Payload=json.dumps(userIdToDelete)
		)	
    getUserStatus = json.load(getUserResponse['Payload']).get('statusCode')
    
    if(getUserStatus is not 200):
        return {
            'statusCode': getUserStatus,
            'body': 'user id is not existed'
        }
    #delete user by id
    try:
        response = table.delete_item(
            Key={
                'UserId': event.get('userid')
            }
        )
    except ClientError as error:
            return {
                'statusCode': 400,
                'body': error.response['Error']['Message']
            }
    else:
        return {
            'statusCode': 200,
            'body': "user deleted succesfully"
        }