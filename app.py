from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import json_util, ObjectId
import json, os, requests

app = Flask(__name__, static_folder='static')

class Config:
    # adicione após as outras chaves
    MONGODB_HOST = os.getenv('MONGODB_URI')
        

@app.route("/")
def index():

    return render_template('index.html')



if __name__ == "__main__":
    app.run(host=os.getenv('FLASK_HOST'), port=os.getenv('FLASK_PORT'), debug=os.getenv('DEBUG'))