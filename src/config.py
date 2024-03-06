from os import environ

from dotenv import load_dotenv

load_dotenv()

# Django
DEBUG = environ.get("DEBUG")
SECRET_KEY = environ.get("SECRET_KEY")

# Google drive
FOLDER_ID = environ.get("FOLDER_ID")
