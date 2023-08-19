""" HW app pages routes. """

from .auth import login_required
from flask import render_template, redirect, url_for, Blueprint, session

pages = Blueprint('pages', __name__)


@pages.route('/')
def index():
    """ Redirects to the last page. Defaults to dashboard. """
    if 'url' not in session:
        session['url'] = url_for('pages.testpage')
    return redirect(session['url'])


@pages.route('/login')
def login():
    return render_template('login.html', title="Login")


@pages.route('/testpage')
@login_required(redirect_url='/testpage')
def testpage():
    return render_template('page.html', title="Testpage",
                           user_name=session['user_name'])


@pages.route('/dashboard')
@login_required(redirect_url='/dashboard')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")


@pages.route('/finished')
@login_required(redirect_url='/finished')
def finished():
    return render_template('finished.html', title="Finished")


@pages.route('/not_finished')
@login_required(redirect_url='/not_finished')
def not_finished():
    return render_template('not_finished.html', title="Not Finished")


@pages.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('pages.login'))
