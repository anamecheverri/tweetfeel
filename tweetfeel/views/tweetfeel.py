"""Add your views here.

We have started you with an initial blueprint. Add more as needed.
"""

from flask import Blueprint, session, render_template
from .twitter import require_twitter_login, twitter
from textblob import TextBlob

tweetfeel = Blueprint("tweetfeel", __name__)


@tweetfeel.route("/")
@require_twitter_login
def index():
    resp = twitter.get("statuses/home_timeline.json")
    statuses = resp.data
    tweets = [TextBlob(status['text']) for status in statuses]
    return render_template("index.html", tweets=tweets)
