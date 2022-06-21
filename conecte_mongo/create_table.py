import boto3
import os


def create_dax_table(dyn_resource=None):
    """
    Creates a DynamoDB table.

    :param dyn_resource: Either a Boto3 or DAX resource.
    :return: The newly created table.
    """
    if dyn_resource is None:
        dyn_resource = boto3.resource('dynamodb',
            region_name='us-east-1',
            aws_access_key_id="AKIAUMCUSPZCS7FYFQP6",
            aws_secret_access_key="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")

    table_name = 'Artistas'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id_transaction', 'KeyType': 'HASH'},
            {'AttributeName': 'artist', 'KeyType': 'RANGE'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'id_transaction', 'AttributeType': 'S'},
            {'AttributeName': 'artist', 'AttributeType': 'S'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }
    table = dyn_resource.create_table(**params)
    print(f"Creating {table_name}...")
    table.wait_until_exists()
    return table


if __name__ == '__main__':
    dax_table = create_dax_table()
    print(f"Created table.")