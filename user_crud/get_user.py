import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context):
    fetchType = event.get('type')
    if(fetchType == 'all'):
        return table.scan()
    elif (fetchType == 'single'):
        return table.get_item(
            Key={
                'UserId': event.get('userId')
            }
        )['Item']