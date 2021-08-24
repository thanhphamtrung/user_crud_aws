import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'UserId': event.get('UserId'),
        },
        UpdateExpression="set UserName=:name",
        ExpressionAttributeValues={
            ':name': event.get('UserName')
        },
        ReturnValues="UPDATED_NEW"
    )
    return response