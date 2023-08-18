from pathlib import Path
from dotenv import load_dotenv 
import os

load_dotenv()

# this is api key and you should grab your own using nasa api website
# https://api.nasa.gov/

API_KEY = os.environ.get("API_KEY")# enter your api key here
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

IMAGE_DIR = Path() / 'images'
