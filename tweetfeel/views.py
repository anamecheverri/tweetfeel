"""Add your views here.

We have started you with an initial blueprint. Add more as needed.
"""

from flask import Blueprint, flash, session, render_template
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

twitter_blueprint = make_twitter_blueprint(
    api_key="FAKEID",
    api_secret="FAKESECRET",
    redirect_to="tweetfeel.index"
)

tweetfeel = Blueprint("tweetfeel", __name__)


@tweetfeel.route("/")
def index():
    if twitter.authorized:
        my_twitter_id = session['twitter_oauth_token']['user_id']
        my_twitter_name = session['twitter_oauth_token']['screen_name']
        resp = twitter.get("statuses/user_timeline.json", params={"user_id": my_twitter_id})
        return render_template("index.html", statuses=resp.json())
    else:
        return "Hello, world!"
