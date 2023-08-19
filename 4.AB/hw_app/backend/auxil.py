""" Module for auxiliary functions """

from .app import db


def get_from_db(model, **kwargs):
    """ Get or create model object. """
    return model.query.filter_by(**kwargs).first()


def create_in_db(model, **kwargs):
    """ Create model object. """
    obj = model(**kwargs)
    db.session.add(obj)
    db.session.commit()
    return obj
