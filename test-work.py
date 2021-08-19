import json

def lambda_hello_world(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, AWC!')
    }
