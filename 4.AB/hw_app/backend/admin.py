"""HW app admin routes."""

from backend.auth import login_required, admin_required
from backend.auxil import get_user_from_session
from backend.models import User, Group, UserRole
from flask import render_template, redirect, url_for, Blueprint, session

admin = Blueprint('admin', __name__)


@admin.route('/admin/users/edit')
@login_required(redirect_url='/admin/users/')
@admin_required
def edit_user():
    ...
