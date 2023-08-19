""" HW app main file. """

from .config import STATIC_FOLDER, TEMPLATE_FOLDER
from .models import db
from .pages import pages
from .auth import auth, oauth
from flask import Flask
from flask_session import Session
import datetime

# init app and load config
app = Flask(__name__, static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
app.config.from_pyfile('config.py')
app.config['SESSION_SQLALCHEMY'] = db

# register auth and pages blueprints
app.register_blueprint(pages)
app.register_blueprint(auth)

# init db
db.init_app(app)

# init oauth
oauth.init_app(app)

# init session
Session(app)

# run app
if __name__ == '__main__':
    app.run()
