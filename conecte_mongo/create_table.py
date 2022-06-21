import boto3
import os
from dotenv import load_dotenv
from os.path import join, dirname

env_path = os.path.dirname(__file__).replace('../controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)


def create_dax_table(dyn_resource=None):
    """
    Creates a DynamoDB table.

    :param dyn_resource: Either a Boto3 or DAX resource.
    :return: The newly created table.
    """
    if dyn_resource is None:
        dyn_resource = boto3.resource('dynamodb',
            region_name='us-east-2',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
            
    table_name = 'artistas'

    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id_transaction', 'KeyType': 'HASH'},
            {'AttributeName': 'artist', 'KeyType': 'RANGE'},
            {'AttributeName': 'songs', 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'id_transaction', 'AttributeType': 'N'},
            {'AttributeName': 'artist', 'AttributeType': 'N'},
            {'AttributeName': 'songs', 'AttributeType': 'N'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }


    table = dyn_resource.create_table(**params)
    print(f"Cruiado tabela {table_name}...")
    table.wait_until_exists()
    return table

if __name__ == '__main__':
    dax_table = create_dax_table()
    print(f"Tabela criada.")