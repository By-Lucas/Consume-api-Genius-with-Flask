try:
    import requests
    from run import app, api
    from controllers.genius import Genius
    from controllers.rediscache import RedisCache
    from models.dynamo_db import DynamoDB
    import unittest
except Exception as e:
    print('Erro ao importar modulo {}'.format(e))


class FlaskTest(unittest.TestCase):

    def setUp(self):
        app = app.test_client()
        
        self.api_genius = Genius.get_lyrics()

        self.cache_test_add = RedisCache.add_cache()
        self.cache_test_get = RedisCache.get_cache()
        self.cache_test_register = RedisCache.registry_exists()
        self.cache_test_delete = RedisCache.delete_registry()

        self.test_dynamodb_create = DynamoDB.create_table_artists()
        self.test_dynamodb_insert = DynamoDB.insert_artists_songs()

        self.response = app

    def test_api(self):
        self.assertEqual(200, self.api_test.status_code)
