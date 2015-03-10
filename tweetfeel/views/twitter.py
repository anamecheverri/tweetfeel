from functools import wraps

from flask import session, Blueprint, url_for, redirect, flash

from ..extensions import oauth


twitter = oauth.remote_app(
    'twitter',
    app_key='TWITTER',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

twitter_bp = Blueprint("twitter", __name__, url_prefix="/twitter")


def require_twitter_login(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'twitter_oauth' in session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for("twitter.login"))

    return decorated_view


@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@twitter_bp.route("/")
def login():
    session.pop('twitter_oauth', None)
    return twitter.authorize(callback=url_for('.authorized', _external=True))


@twitter_bp.route("/authorized/")
def authorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
        return "BAD TIMES"
    session['twitter_oauth'] = resp
    return redirect(url_for("tweetfeel.index"))
