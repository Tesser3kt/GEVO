from functools import wraps
from flask import redirect, url_for, Blueprint, current_app, session
from .models import User, UserRole
from authlib.integrations.flask_client import OAuth

from .auxil import get_from_db, create_in_db

auth = Blueprint('auth', __name__)

# Create OAuth2 provider
oauth = OAuth()


@auth.route('/google')
def google():
    """ Google OAuth2 authentication. """
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

    oauth.register(
        name='google',
        client_id=current_app.config['GOOGLE_CLIENT_ID'],
        client_secret=current_app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    redirect_uri = url_for('auth.google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth.route('/google/auth')
def google_auth():
    """ Google OAuth2 authentication callback. """
    token = oauth.google.authorize_access_token()
    userinfo = token['userinfo']
    print(userinfo)
    if not userinfo:
        # TODO redirect to error page
        return redirect(url_for('pages.login'))

    if userinfo.get('hd') != 'gevo.cz':
        # TODO redirect to error page
        return redirect(url_for('pages.login'))

    # get user from db based on email
    user = get_from_db(User, email=userinfo.get('email'))
    if not user:
        # create new db entry
        user = create_in_db(
            User,
            name=userinfo.get('name'),
            email=userinfo.get('email'),
            role=UserRole.STUDENT
        )

    # save user info to session
    session['user_id'] = user.id
    session['user_name'] = user.name
    session['user_email'] = user.email
    session['user_role'] = user.role.value

    return redirect(url_for('pages.index'))


def login_required(redirect_url):
    def login_wrapper(f):
        """ Decorator for routes that require login. """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            session['url'] = redirect_url
            if 'user_id' not in session:
                print('User not logged in.')
                return redirect(url_for('pages.login'))
            return f(*args, **kwargs)
        return decorated_function
    return login_wrapper
