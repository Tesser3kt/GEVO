""" HW app pages routes. """

from backend.auth import login_required, admin_required
from backend.auxil import get_user_from_session
from backend.models import User, Group, UserRole
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
    user = get_user_from_session()
    return render_template(
        'page.html',
        title="Testpage",
        user=user
    )


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


@pages.route('/admin/users')
@login_required(redirect_url='/admin/users')
@admin_required
def admin_users():
    user = get_user_from_session()
    all_users = User.query.all()
    all_groups = Group.query.all()

    users_data = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role.value,
            'group': user.group.name if user.group else None
        }
        for user in all_users
    ]
    group_names = [group.name for group in all_groups]
    students = [user for user in users_data if user['role']
                == UserRole.STUDENT.value]
    teachers = [user for user in users_data if user['role']
                == UserRole.TEACHER.value]
    admins = [user for user in users_data if user['role']
              == UserRole.ADMIN.value]
    return render_template(
        'admin_users.html',
        title="Uživatelé",
        user=user,
        students=students,
        teachers=teachers,
        admins=admins,
        groups=group_names
    )


@pages.route('/admin/users/<int:user_id>')
@login_required(redirect_url='/admin/users')
@admin_required
def admin_user(user_id):
    user = get_user_from_session()
    edited_user = User.query.get(user_id)
    if not edited_user:
        return redirect(url_for('pages.admin_users'))

    groups = Group.query.all()

    return render_template(
        'admin_users_form.html',
        title="Uživatel",
        user=user,
        edited_user=edited_user,
        groups=groups,
        form_title="Úprava uživatele"
    )


@pages.route('/admin/users/add')
@login_required(redirect_url='/admin/users')
@admin_required
def admin_user_add():
    user = get_user_from_session()
    groups = Group.query.all()

    return render_template(
        'admin_users_form.html',
        title="Uživatel",
        user=user,
        edited_user=None,
        groups=groups,
        form_title="Nový uživatel"
    )


@pages.route('/admin/groups')
@login_required(redirect_url='/admin/groups')
@admin_required
def admin_groups():
    user = get_user_from_session()
    return render_template(
        'admin_groups.html',
        title="Skupiny",
        user=user
    )


@pages.route('/admin/homeworks')
@login_required(redirect_url='/admin/homeworks')
@admin_required
def admin_homeworks():
    user = get_user_from_session()
    return render_template(
        'admin_homeworks.html',
        title="Úkoly",
        user=user
    )


@pages.route('/admin/assignments')
@login_required(redirect_url='/admin/assignments')
@admin_required
def admin_assignments():
    user = get_user_from_session()
    return render_template(
        'admin_assignments.html',
        title="Zadání",
        user=user
    )


@pages.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('pages.login'))
