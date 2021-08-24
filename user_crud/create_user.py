import json
from random import random
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    response = table.put_item(
       Item= {
                'UserId': str(random()),
                'UserName': event.get('UserName')
            }
        )
    return response
    
   