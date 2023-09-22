import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # Set your configuration options here
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('database_url')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
