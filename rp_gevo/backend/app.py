import os
import requests
from config import *

from flask import Flask, url_for, redirect, session, abort, request
from flask_sqlalchemy import SQLAlchemy

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.transport import requests as google_requests

from pip._vendor import cachecontrol

# allow insecure transport for development
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# create Flask app
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

# configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# create SQLAlchemy object
db = SQLAlchemy()
db.init_app(app)

# load client secrets from JSON file
client_secrets_file = os.path.join(
    os.path.dirname(__file__), 'client_secrets.json'
)

# create google auth flow
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=['openid', 'email', 'profile'],
    redirect_uri=url_for('oauth2callback', _external=True)
)


@app.route('/login')
def login():
    """ Redirect to Google login page and return user info. """
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    """ Handle Google OAuth2 callback. """
    # fetch token from Google
    flow.fetch_token(authorization_response=request.url)

    if session['state'] != request.args['state']:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google_requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session['google_id'] = id_info.get('sub')
    session['name'] = id_info.get('name')

    return f"Hello {session['name']}! You are logged in."


class User(db.Model):
    """ Basic user database model. """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"<User {self.name} | Role {self.role}>"


if __name__ == '__main__':
    # run app
    app.run()
