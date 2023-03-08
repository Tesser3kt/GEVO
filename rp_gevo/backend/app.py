import requests
from config import *
from flask import Flask, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_oauth import OAuth

# create Flask app
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

# create OAuth object
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_method='GET',
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_params={
        'scope': ['email', 'profile'],
        'response_type': 'code'
    }
)

# configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# create SQLAlchemy object
db = SQLAlchemy(app)


@app.route('/login')
def login():


@app.route('/authorize')
def authorize():
    ...


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
