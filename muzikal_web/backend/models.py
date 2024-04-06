from app import db
from datetime import datetime


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)


class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    subtitle = db.Column(db.String(400), nullable=False)


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True)


class Footer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    copyright = db.Column(db.String(50), nullable=False)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=True)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    alt = db.Column(db.String, nullable=False)
    credit = db.Column(db.String, nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
