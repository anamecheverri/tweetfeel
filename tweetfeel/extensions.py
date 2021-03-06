# -*- coding: utf-8 -*-
"""Extensions module."""

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask_oauthlib.client import OAuth
oauth = OAuth()

# Change this to HerokuConfig if using Heroku.
from flask.ext.appconfig import AppConfig
config = AppConfig()
