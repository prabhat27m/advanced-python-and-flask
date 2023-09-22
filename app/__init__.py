from flask import Flask
# from .config import Config
from .routes import init_routes
from dotenv import load_dotenv
from .database import db
import os

load_dotenv()

# Access the database URL from the .env file
def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('database_url')
    with app.app_context():
        db.init_app(app)
    init_routes(app)
    return app

