from flask import Flask
from flask_restful import Api
from controllers.default import GeniusConsume
import os

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

api.add_resource(GeniusConsume, '/artista/<string:artist>')


if __name__ == "__main__":
    app.run(host=os.environ.get('FLASK_HOST'), port=os.environ.get('FLASK_PORT'))