import os
from flask import Flask
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from routes import blueprint
from controller import db

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_URI_dbperpustakaan')
    db.init_app(app)

    app.register_blueprint(blueprint)

    return app