import os
from config import *

from flask import Flask, url_for, redirect, session, abort, request
from flask_sqlalchemy import SQLAlchemy

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


@app.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    """ Log user in. """
    if request.method == 'POST':
        # get user data from request
        user_data = request.get_json()
        # check if user exists
        user = User.query.filter_by(email=user_data['email']).first()
        if user is None:
            # create new user
            user = User(
                name=user_data['name'],
                email=user_data['email'],
                role='teacher'
            )
            db.session.add(user)
            db.session.commit()
        # log user in
        session['user_email'] = user.email
        session['user_name'] = user.name
        return {
            'user_name': user.name,
            'user_email': user.email
        }
    elif request.method == 'GET':
        # check if user is logged in
        if 'user_name' in session:
            return {
                'user_name': session['user_name'],
                'user_email': session['user_email']
            }
        else:
            return None


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
