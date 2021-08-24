import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-profile')

def lambda_handler(event, context)
    try
        response = table.delete_item(
            Key={
                'UserId' event.get('UserId')
            }
        )
    except ClientError as e
        if e.response['Error']['Code'] == ConditionalCheckFailedException
            print(e.response['Error']['Message'])
        else
            raise
    else
        return response