import boto3
import os

def create_users_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', 
            region_name='us-east-2',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"))
 
    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'occupation',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'occupation',
                'AttributeType': 'S'
            },
 
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table
 
if __name__ == '__main__':
    users_table = create_users_table()
    print("Table status:", users_table.table_status)