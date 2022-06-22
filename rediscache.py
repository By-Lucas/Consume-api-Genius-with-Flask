from redis import Redis
import datetime


class RedisCache:
    def __init__(self):
        """Inicialize class Redis to put data on cache"""

        self.redis = Redis(
            host='localhost',
            port='6379')

    def add_cache(self, artist, list_songs):
        """ Function add registry data  on Redis and
            set the expiration time to key
               Args
               ----
                   name(str): artists name

               Returns
               -------
                  """
        days = datetime.timedelta(days=7)
        seconds = days.total_seconds()
        self.redis.set(artist, list_songs)
        self.redis.expire(artist, time=int(seconds))
        print('Registro adicionado a cache')

    def get_cache(self, artist):
        """ Function get registry data  on Redis.
               Args
               ----
                   name(str): artists name

               Returns
               -------
                  """
        value = self.redis.get(artist)
        return value

    def registry_exists(self, artist):
        """ Function to verify if registry data exists on Redis.
                Args
                ----
                    name(str): artists name

                Returns
                -------
                   """
        exists = self.redis.exists(artist)
        return exists

    def delete_registry(self, artist):
        """ Function to delete registry data on Redis.

                Args
                ----
                    name(str): artists name

                Returns
                -------
            """
        self.redis.delete(artist)
        print('Registro em cache deletado')
