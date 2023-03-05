import os
import pathlib
import requests
from config import *
from flask import Flask, redirect, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

# create Flask app
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

# configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# create SQLAlchemy object
db = SQLAlchemy(app)

# development only
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secrets.json"
)

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid"
    ],
    redirect_uri="http://localhost:5000/callback"
)


# a function to check if the user is authorized or not
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:  # authorization required
            return abort(401)
        else:
            return function()

    return wrapper


@app.route('/data')
def data():
    """ Returns a list of users. """
    users = User.query.all()
    return {'users': [user.name for user in users]}


@app.route('/login')
def login():
    """ Login page for google. """
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route('/callback')
def callback():
    """ Callback page for google login. """
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # state does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    # defining the results to show on the page
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/home")


@app.route("/logout")
def logout():
    """ Logout page. """
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    """ Index page. Redirects to either login or home page. """
    if "google_id" in session:
        return redirect("/home")
    else:
        return redirect("/login")


@app.route("/home")
@login_is_required
def home():
    """ Home page. Only shows to logged in users. """
    # the logout button
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"


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
