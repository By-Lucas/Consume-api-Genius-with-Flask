import redis
import os
from datetime import timedelta


conextion_redis = redis.Redis(host=os.environ.get('FLASK_HOST'), 
                                port=os.environ.get('FLASK_PORT'), db=0)

def definir_item(artist, items):
    dias = 7 # dias para expirar o cache
    time = timedelta(days=dias)
    return conextion_redis.set(artist, items, ex=time)
    
def carregar_item(artist):
    return conextion_redis.get(artist)

def deletar_item(artist):
    return conextion_redis.delete(artist)

