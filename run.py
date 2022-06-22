import re
from controllers.genius import Genius
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from models.dynamo_db import DynamoDB
import json, requests, os
from controllers.rediscache import RedisCache
from controllers.env_config import DEBUG, FLASK_HOST, FLASK_PORT, GENIUS_TOKEN

app = Flask(__name__)
api = Api(app)


class Artist(Resource):
    def __init__(self):
        """Iniciar class Genius, dynamoDB e RedisCache """
        self.songs_api = Genius()
        self.db = DynamoDB()
        self.cache = RedisCache()
        self.db.create_table_artists()

    def get(self, name):
        """Função para obter as 10 musicas mais populares do artista """
        #verificar query_string 
        if request.args.get('cache') is None:
            cache_query_string = True
        else:
            cache_query_string = eval(request.args.get('cache'))

        #Numero de musicas mais populares
        music_number = 10

        #se o registro já existir no cache selecione-os
        if self.cache.registry_exists(name):
            songs_list = self.cache.get_cache(name)
            print()
            response = {f'As 10 musicas mais populares de {name}': eval(songs_list),
                        'cache': cache_query_string}

        #se o registro ainda não existir no cache crie cache e salve no dynamodb
        else:
            popular_musics = self.songs_api.get_lyrics(name, music_number)
            self.db.insert_artists_songs(name, popular_musics)
            response = {f'As 10 musicas mais populares de {name}': popular_musics,
                        'cache': cache_query_string}
            self.cache.add_cache(name, str(popular_musics))

        #if cache param == False delete o registro e insira o artista no dynamoDB
        if not cache_query_string:
            self.cache.delete_registry(name)
            popular_musics = self.songs_api.get_lyrics(name, music_number)
            self.db.insert_artists_songs(name, popular_musics)

        else:
            print('cache=True, Utilizando os dados em cache')
            self.cache.get_cache(name)
        return response

api.add_resource(Artist, '/artista/<name>')


def search_artist():
    artista =  request.form.get('nome')
    base_url = "http://api.genius.com"
    headers = {'Authorization': 'Bearer {}'.format(os.environ.get("GENIUS_TOKEN"))}
    search_url = "{}/search?q={}".format(base_url, artista)
    return requests.get(search_url, headers=headers).json()


@app.route('/', methods=['GET', 'POST'])
def index():
    artista = request.form.get('nome')
    if artista != None:
        response =  search_artist()
        list_songs = []
        for artistas in response['response']['hits']:
            list_songs.append(artistas['result']['title'])
        print(list_songs)
        return render_template('index.html',artista=artista, list_songs=list_songs)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(FLASK_HOST, FLASK_PORT, DEBUG)
