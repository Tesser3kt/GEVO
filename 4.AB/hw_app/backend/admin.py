"""HW app admin routes."""

from backend.app import db
from backend.auth import login_required, admin_required
from backend.auxil import get_user_from_session
from backend.models import User, Group, UserRole
from flask import render_template, redirect, url_for, Blueprint, session
from flask import request

admin = Blueprint('admin', __name__)


@admin.route('/admin/users/edit/<int:user_id>', methods=['POST'])
@login_required(redirect_url='/admin/users/')
@admin_required
def edit_user(user_id):
    """ Edit user. """
    user = get_user_from_session()
    if user['role'] != UserRole.ADMIN.value:
        return redirect(url_for('pages.dashboard'))

    edited_user = User.query.filter_by(id=user_id).first()
    if not edited_user:
        return redirect(url_for('pages.admin_users'))

    edited_user.name = request.form.get('name')
    edited_user.email = request.form.get('email')
    edited_user.role = UserRole(request.form.get('role'))
    if request.form.get('group'):
        edited_user.group_id = int(request.form.get('group'))

    db.session.commit()
    return redirect(url_for('pages.admin_users'))


@admin.route('/admin/users/new_user', methods=['POST'])
@login_required(redirect_url='/admin/users/')
@admin_required
def new_user():
    """ Add user. """
    user = get_user_from_session()
    if user['role'] != UserRole.ADMIN.value:
        return redirect(url_for('pages.dashboard'))

    new_user = User(
        name=request.form.get('name'),
        email=request.form.get('email'),
        role=UserRole(request.form.get('role'))
    )
    if request.form.get('group'):
        new_user.group_id = int(request.form.get('group'))

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('pages.admin_users'))


@admin.route('/admin/users/delete/<int:user_id>', methods=['GET', 'POST'])
@login_required(redirect_url='/admin/users/')
@admin_required
def delete_user(user_id):
    """ Delete user. """
    user = get_user_from_session()
    if user['role'] != UserRole.ADMIN.value:
        return redirect(url_for('pages.dashboard'))

    deleted_user = User.query.filter_by(id=user_id).first()
    if not deleted_user:
        return redirect(url_for('pages.admin_users'))

    db.session.delete(deleted_user)
    db.session.commit()
    return redirect(url_for('pages.admin_users'))
