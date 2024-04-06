import os

SECRET_KEY = "pbsOohQZWz98Jwcxhum4aMKPl6kd1ebaQltT7haDsn8="

TEMPLATE_FOLDER = "../frontend/templates/"
STATIC_FOLDER = "../frontend/static/dest/"
TEMPLATES_AUTO_RELOAD = True

NEWS_MAX_CHAR = 100

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.path.dirname(__file__), "database.db"
)
