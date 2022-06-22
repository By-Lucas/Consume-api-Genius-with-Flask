from controllers.genius import Genius
from flask import Flask, request
from flask_restful import Resource, Api
from models.dynamo_db import DynamoDB
import json
from controllers.rediscache import RedisCache

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

if __name__ == '__main__':
    app.run(debug=True)
