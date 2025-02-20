from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # ✅ Correct way to load configuration
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    return app
