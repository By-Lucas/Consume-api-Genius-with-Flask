import boto3
import uuid
import os
from controllers.env_config import (
    AWS_ACCESS_KEY_ID,
    AWS_REGION, 
    AWS_SECRET_ACCESS_KEY
    )


class DynamoDB:

    def __init__(self):
        """Iniciar classe DynamoDB """

        self.ACCESS_KEY = AWS_SECRET_ACCESS_KEY
        self.KEY_ID = AWS_ACCESS_KEY_ID
        self.REGION = AWS_REGION
        self.dynamodb = boto3.resource(service_name='dynamodb',
                                        region_name=self.REGION,
                                        aws_access_key_id=self.KEY_ID,
                                        aws_secret_access_key=self.ACCESS_KEY)
        self.key = str(uuid.uuid4())

    def create_table_artists(self):
        """ Verifique se as tabelas existem, caso contrário a tabela é criada."""
        tables = list(self.dynamodb.tables.all())
        tables_name = [table.name for table in tables]

        if 'Artists' not in tables_name:
            table = self.dynamodb.create_table(
                TableName='Artistas',
                KeySchema=[
                    {
                        'AttributeName': 'id_transaction',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'artist',
                        'KeyType': 'RANGE'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id_transaction',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'artist',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
        else:
            print('Tabela existente')

    # insert item
    def insert_artists_songs(self, artist_name, songs):
        """ insirir o nome e as músicas dos artistas no DynamoDB"""
        table = self.dynamodb.Table('Artists')

        try:
            table.put_item(Item={'id_transaction': self.key, 'artist': artist_name, 'songs': songs})
            print('Registro inserido no DynamoDB com sucesso')
            # return self.key
        except:
            print('Erro ao inserir registro na tabela')


if __name__ == '__main__':
    db = DynamoDB()
    db.create_table_artists()
