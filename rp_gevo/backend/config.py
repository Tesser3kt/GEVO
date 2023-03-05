from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')
DB_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
