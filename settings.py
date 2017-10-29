# settings.py
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)

USERNAME = os.environ.get("JOYFUN_USERNAME")
PASSWORD = os.environ.get("JOYFUN_PASSWORD")