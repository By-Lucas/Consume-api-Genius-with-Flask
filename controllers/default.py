import boto3
import requests
import uuid
import os
from flask_restful import Resource
from flask import jsonify, request
from dotenv import load_dotenv
from os.path import join, dirname
from models.models import add_data
from botocore.exceptions import ClientError

from controllers import cash_redis
from rediscache import RedisCache


env_path = os.path.dirname(__file__).replace('controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)


class GeniusConsume(Resource):
    def __init__(self):
        self.cache = RedisCache()

    def search_artist(self, artist):
        base_url = "http://api.genius.com"
        headers = {'Authorization': 'Bearer {}'.format(os.environ.get("GENIUS_TOKEN"))}
        search_url = "{}/search?q={}".format(base_url, artist)
        return requests.get(search_url, headers=headers).json()

    def top_hits(self, info_artist):
        search_term = request.args.get("artist")
        print(search_term)
        CACHE = request.args.get("cache")
        if CACHE == 'false':
            cash_redis.deletar_item(search_term)
            res_item = self.search_artist(cash_redis)

        list_songs = []
        for song in info_artist['response']['hits']:
            list_songs.append(song['result']['title'])
        print('Songs',list_songs)
        return list_songs

    def get(self, artist):
        
        res = self.search_artist(artist)

        id_transaction = ''
        if len(res['response']['hits']) != 0:
            id_transaction = str(uuid.uuid4())

        hits = self.top_hits(res)

        about = {
            'id_transaction': id_transaction,
            'artist': artist,
            'songs': hits
        }

        if about['id_transaction'] == '':
            return jsonify(about)


        dynamodb = boto3.resource(
            'dynamodb',
            region_name='us-east-1',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
            )

        table = dynamodb.Table('Artistas')

        #data_base = add_data(id_transaction, artist, hits)

        try:
            table.put_item(
                Item={
                    'id_transaction': id_transaction,
                    'artist': artist,
                    'songs': hits
                }
            )
            print('Dados inseridos')
        except ClientError as e:
            print('Error', e)

        return jsonify(about)

def artista_esta_no_cache(artist):
    return cash_redis.carregar_item(artist)

def artista_esta_no_cache(artist_name):
    return cash_redis.get_item(artist_name)


def artista_esta_no_banco(artist_name):
    item = bd_controller.get_item(artist_name)
    return item.get('Item')