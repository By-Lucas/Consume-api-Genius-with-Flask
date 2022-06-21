import boto3
import os
from dotenv import load_dotenv
from os.path import join, dirname

env_path = os.path.dirname(__file__).replace('controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)
class Artistas:
    """Encapsulates an Amazon DynamoDB table of movie data."""
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        self.table = None

    def create_dax_table(dyn_resource=None):
        if dyn_resource is None:
            dyn_resource = boto3.resource('dynamodb',
                region_name='us-east-2',
                aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"))
                
        try:
            table = dyn_resource.create_table(
                TableName='artistas',
                KeySchema=[
                    {'AttributeName': 'id_transaction', 'KeyType': 'HASH'},
                    {'AttributeName': 'artist', 'KeyType': 'HASH'},
                    {'AttributeName': 'songs','KeyType': 'RANGE'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'id_transaction','AttributeType': 'S'},
                    {'AttributeName': 'artist','AttributeType': 'S'},
                    {'AttributeName': 'songs','AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
            return table
        except:
            print('Erro ao criar banco de dados')

    if __name__ == '__main__':
        users_table = create_dax_table()
        print("Status da tabela:", users_table.table_status)