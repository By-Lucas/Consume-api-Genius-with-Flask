import os
from dotenv import load_dotenv
from os.path import join

env_path = os.path.dirname(__file__).replace('controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)

#CONEXOES GENIUS E AWS
GENIUS_TOKEN=os.environ.get("GENIUS_TOKEN")
AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION=os.environ.get("AWS_REGION")

#CONEXOES FLASK
DEBUG=os.environ.get("DEBUG")
FLASK_HOST=os.environ.get("FLASK_HOST")
FLASK_PORT=os.environ.get("FLASK_PORT")
