from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')
DB_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GOOGLE_BASE_URI = config('GOOGLE_BASE_URI')
GOOGLE_AUTH_URI = config('GOOGLE_AUTH_URI')
GOOGLE_TOKEN_URI = config('GOOGLE_TOKEN_URI')
GOOGLE_REQUEST_SCOPE = "https://www.googleapis.com/auth/userinfo.email"

REDIRECT_URI = config('REDIRECT_URI')
