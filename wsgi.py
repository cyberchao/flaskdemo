import os
from dotenv import load_dotenv
import click


from . import create_app
app = create_app('development')


dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)






