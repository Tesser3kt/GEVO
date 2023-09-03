""" HW app main file. """

from backend.config import STATIC_FOLDER, TEMPLATE_FOLDER
from backend.models import db
from backend.pages import pages
from backend.auth import auth, oauth
from flask import Flask, send_from_directory
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

# special route for preline UI


@app.route('/preline.js')
def serve_preline_js():
    return send_from_directory('../frontend/node_modules/preline/dist',
                               'preline.js')


# run app
if __name__ == '__main__':
    app.run()
