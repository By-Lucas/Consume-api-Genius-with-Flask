import boto3
import os
from dotenv import load_dotenv
from os.path import join, dirname

env_path = os.path.dirname(__file__).replace('/controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)

dynamodb = boto3.resource('dynamodb',
            region_name='us-east-2',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
table = dynamodb.Table('musica')

table.put_item(
    Item={
        'id_transaction': 'ruanb',
        'artist': 'ruan',
        'songs': 'bekker',
    }
)