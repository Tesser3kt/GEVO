""" HW app database models """

from enum import Enum
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


class AssignmentStatus(Enum):
    """ Enum for assignment status. """
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'


class UserRole(Enum):
    """ Enum for user role. """
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'


class User(db.Model):
    """
    User database model. Contains:
        - name
        - email address
        - assignments
        - authored comments
    """

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)

    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    assignments = db.relationship('Assignment', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name} | {self.role.value}>'


class Group(db.Model):
    """ Group database model. Contains:
        - name
        - users
        - assignments
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='group', lazy=True)
    assignments = db.relationship('Assignment', backref='group', lazy=True)

    def __repr__(self):
        return f'<Group {self.name}>'


class Homework(db.Model):
    """
    Homework database model. Contains:
        - title
        - description
        - maximum points
        - maximum tries
        - assignments
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    max_points = db.Column(db.Integer, nullable=False)
    max_tries = db.Column(db.Integer, nullable=False)
    assignments = db.relationship('Assignment', backref='homework', lazy=True)

    def __repr__(self):
        return f'<Homework {self.title}>'


class Assignment(db.Model):
    """
    Assignment database model. Contains:
        - user id
        - homework id
        - points
        - tries
        - deadline
        - status (see AssignmentStatus enum)
        - comments
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)
    homework_id = db.Column(db.Integer, db.ForeignKey('homework.id'),
                            nullable=False)
    points = db.Column(db.Integer, nullable=False)
    tries = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(AssignmentStatus), nullable=False)
    comments = db.relationship('Comment', backref='assignment', lazy=True)

    def __repr__(self):
        return (f'<Assignment of {self.homework} to {self.user}. Deadline: '
                f'{self.deadline}>')


class Comment(db.Model):
    """
    Comment database model. Contains:
        - user id
        - assignment id
        - comment
        - creation date
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'),
                              nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f'<Comment by {self.user} on {self.assignment}. Created on: '
                f'{self.date_created}>')
