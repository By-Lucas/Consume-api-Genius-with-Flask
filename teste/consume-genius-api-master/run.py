from flask import Flask
from flask_restful import Api
from controllers.default import GeniusConsume

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

api.add_resource(GeniusConsume, '/artista/<string:artist>')


if __name__ == "__main__":
    app.run()