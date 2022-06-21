import boto3
import os
from pprint import pprint


def put_user(name, occupation, hobby, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', 
            region_name='us-east-2',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
            )


    table = dynamodb.Table('artistas')
    response = table.put_item(
        Item={
            'id_transaction': name,
            'artist': occupation,
            'songs': hobby
        }
    )
    return response
 
if __name__ == '__main__':
    user_resp = put_user("Thamires", "Student", "games")
    print("Put user succeeded:")
    pprint(user_resp, sort_dicts=False)