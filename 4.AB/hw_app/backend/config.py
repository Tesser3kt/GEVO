""" HW app config file """

DEBUG = True
SECRET_KEY = 'dev'

DB_USER = 'testuser'
DB_PASS = 'testpass'
DB_NAME = 'hw_app'
SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}"

STATIC_FOLDER = "../frontend/dest/"
TEMPLATE_FOLDER = "../frontend/templates/"

GOOGLE_CLIENT_ID =\
    "236865910793-2k90h5jgaikar3jgnlbqeppou1kbotpu.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"

SESSION_TYPE = 'sqlalchemy'
SESSION_PERMANENT = True
SESSION_SQLALCHEMY_TABLE = 'sessions'
