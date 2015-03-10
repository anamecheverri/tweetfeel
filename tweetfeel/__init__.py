from flask import Flask, render_template

from . import models
from .extensions import db, migrate, config
from .views import tweetfeel, twitter_blueprint

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/tweetfeel.db"
DEBUG = True
SECRET_KEY = 'development-key'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(tweetfeel)
    app.register_blueprint(twitter_blueprint)

    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app