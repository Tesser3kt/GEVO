from config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)

# configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# create SQLAlchemy object
db = SQLAlchemy(app)


@app.route('/data')
def data():
    """ Returns a list of users. """
    users = User.query.all()
    return {'users': [user.name for user in users]}


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
    app.run(debug=DEBUG)
