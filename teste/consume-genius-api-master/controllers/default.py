import boto3
import requests
import uuid
import os
from flask_restful import Resource, reqparse
from flask import request, jsonify
from dotenv import load_dotenv
from os.path import join, dirname

env_path = os.path.dirname(__file__).replace('/controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)


class GeniusConsume(Resource):


    def search_artist(self, artist):
        base_url = "http://api.genius.com"
        headers = {'Authorization': 'Bearer {}'.format(os.environ.get("GENIUS_TOKEN"))}
        search_url = "{}/search?q={}".format(base_url, artist)
        return requests.get(search_url, headers=headers).json()


    def top_hits(self, info_artist):
        list_songs = []
        for song in info_artist['response']['hits']:
            list_songs.append(song['result']['title'])
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
            region_name='us-east-2',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
            )

        table = dynamodb.Table('tb_searches')

        table.put_item(
            Item={
                'id_transaction': id_transaction,
                'artist': artist,
                'songs': hits
            }
        )

        return jsonify(about)