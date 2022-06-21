from flask import Flask, render_template
from flask_restful import Api
from controllers.default import GeniusConsume
from models.models import get_db_connection
import os

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

api.add_resource(GeniusConsume, '/artista/<string:artist>')


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM Artistas').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(host=os.environ.get('FLASK_HOST'), port=os.environ.get('FLASK_PORT'))