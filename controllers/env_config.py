import os
from dotenv import load_dotenv
from os.path import join

env_path = os.path.dirname(__file__).replace('controllers', '')
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)

GENIUS_TOKEN=os.environ.get("GENIUS_TOKEN")
AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION=os.environ.get("AWS_REGION")