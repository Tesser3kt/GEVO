""" Module for auxiliary functions """

from backend.app import db
from flask import session


def get_from_db(model, **kwargs):
    """ Get or create model object. """
    return model.query.filter_by(**kwargs).first()


def create_in_db(model, **kwargs):
    """ Create model object. """
    obj = model(**kwargs)
    db.session.add(obj)
    db.session.commit()
    return obj


def get_user_from_session():
    return {
        'name': session.get('user_name'),
        'email': session.get('user_email'),
        'role': session.get('user_role')
    }
