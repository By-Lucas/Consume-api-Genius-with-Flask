from redis import Redis
import datetime


class RedisCache:
    def __init__(self):
        """Iniciar a Classe Cache Redis"""

        self.redis = Redis(
            host='localhost',
            port='6379',
            db=0)

    def add_cache(self, artist, list_songs):
        """ Função adicionar dados de registro no Redis e
            definir o tempo de expiração para chave """
        days = datetime.timedelta(days=7)
        seconds = days.total_seconds()
        self.redis.set(artist, list_songs)
        self.redis.expire(artist, time=int(seconds))
        print('Registro adicionado a cache redis')

    def get_cache(self, artist):
        """ Função obter dados de registro no Redis."""
        value = self.redis.get(artist)
        return value

    def registry_exists(self, artist):
        """ Função para verificar se existem dados de registro no Redis."""
        exists = self.redis.exists(artist)
        return exists

    def delete_registry(self, artist):
        """ Função para excluir dados do registro no Redis."""
        self.redis.delete(artist)
        print('Registro em cache deletado')
