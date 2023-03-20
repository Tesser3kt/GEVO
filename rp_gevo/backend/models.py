from app import db


class Class(db.Model):
    """ Class database model. """
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(80), unique=False, nullable=False)
    letter = db.Column(db.String(80), unique=False, nullable=False)

    students = db.relationship('Student', uselist=True,
                               backref='class_', lazy=True)

    def __str__(self):
        return f"{self.grade}.{self.letter}"

    def __repr__(self):
        return f"<Class {self.grade}.{self.letter}>"


class Student(db.Model):
    """ Student database model. """
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

    class_id = db.Column(
        db.Integer, db.ForeignKey('classes.id'), nullable=False)
    thesis = db.relationship('Thesis', uselist=False,
                             backref='author', lazy=True)

    def __repr__(self):
        return f"<Student {self.name} | Class: {self.class_}>"


class Teacher(db.Model):
    """ Teacher database model. """
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

    supervised_theses = db.relationship(
        'Thesis', uselist=True,
        backref='supervisor', lazy=True,
        foreign_keys='Thesis.supervisor_id')
    opposed_theses = db.relationship(
        'Thesis', uselist=True,
        backref='opponent', lazy=True,
        foreign_keys='Thesis.opponent_id')

    def __repr__(self):
        return f"<Teacher {self.name} | Role: {self.role}>"


class Thesis(db.Model):
    """ Thesis database model. """
    __tablename__ = 'theses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    academic_year = db.Column(db.String(80), unique=False, nullable=False)

    author_id = db.Column(
        db.Integer, db.ForeignKey('students.id'), nullable=False)
    supervisor_id = db.Column(
        db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    opponent_id = db.Column(
        db.Integer, db.ForeignKey('teachers.id'), nullable=True)

    supervisor_evaluation = db.relationship(
        'Evaluation', uselist=False,
        backref="supervisor_thesis", lazy=True,
        foreign_keys='Evaluation.supervisor_thesis_id')
    opponent_evaluation = db.relationship(
        'Evaluation', uselist=False,
        backref="opponent_thesis", lazy=True,
        foreign_keys='Evaluation.opponent_thesis_id')

    supervisor_review = db.relationship(
        'Review', uselist=False,
        backref="supervisor_thesis", lazy=True,
        foreign_keys='Review.supervisor_thesis_id')
    opponent_review = db.relationship(
        'Review', uselist=False,
        backref="opponent_thesis", lazy=True,
        foreign_keys='Review.opponent_thesis_id')

    supervisor_questions = db.relationship(
        'Question', uselist=True,
        backref="supervisor_thesis", lazy=True,
        foreign_keys='Question.supervisor_thesis_id')
    opponent_questions = db.relationship(
        'Question', uselist=True,
        backref="opponent_thesis", lazy=True,
        foreign_keys='Question.opponent_thesis_id')

    supervisor_finalized = db.Column(db.Boolean, unique=False, nullable=False)
    opponent_finalized = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return (f"<Thesis {self.title} | Author: {self.author} |"
                f" Supervisor: {self.supervisor} | Opponent: {self.opponent}>")

    def basic_data(self):
        """ Returns basic data (id, title, author, supervisor, opponent,
        academic_year) about the thesis. """

        return {
            'id': self.id,
            'title': self.title,
            'author': self.author.name,
            'author_id': self.author_id,
            'author_class': str(self.author.class_),
            'supervisor': self.supervisor.name,
            'supervisor_id': self.supervisor_id,
            'opponent': self.opponent.name if self.opponent else '',
            'opponent_id': self.opponent_id if self.opponent_id else '',
            'academic_year': self.academic_year,
            'supervisor_finalized': self.supervisor_finalized,
            'opponent_finalized': self.opponent_finalized
        }


class Evaluation(db.Model):
    """ Evaluation database model. """
    WEIGHTS = {
        'formulation': 1,
        'methodology': 3,
        'bibliography': 2,
        'structure': 4,
        'contribution': 4,
        'terminology': 1,
        'citations': 3,
        'language': 2,
        'formatting': 2,
        'results': 4
    }
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key=True)
    formulation = db.Column(db.Integer, unique=False, nullable=False)
    methodology = db.Column(db.Integer, unique=False, nullable=False)
    bibliography = db.Column(db.Integer, unique=False, nullable=False)
    structure = db.Column(db.Integer, unique=False, nullable=False)
    contribution = db.Column(db.Integer, unique=False, nullable=False)
    terminology = db.Column(db.Integer, unique=False, nullable=False)
    citations = db.Column(db.Integer, unique=False, nullable=True)
    language = db.Column(db.Integer, unique=False, nullable=True)
    formatting = db.Column(db.Integer, unique=False, nullable=True)
    results = db.Column(db.Integer, unique=False, nullable=False)

    supervisor_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)
    opponent_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)

    def __repr__(self):
        thesis = (self.supervised_thesis if self.supervised_thesis else
                  self.opponent_thesis)
        return f"<Evaluation of {thesis}>"

    @property
    def weighted_mean(self):
        """ Returns the weighted mean of the evaluation. """
        total = 0
        for key, value in self.WEIGHTS.items():
            if getattr(self, key):
                total += getattr(self, key) * value
        return round(total / sum(self.WEIGHTS.values()))


class Review(db.Model):
    """ Review database model. """
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, unique=False, nullable=False)

    supervisor_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)
    opponent_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)

    def __repr__(self):
        thesis = (self.supervised_thesis if self.supervised_thesis else
                  self.opponent_thesis)
        return f"<Review of {thesis}>"


class Question(db.Model):
    """ Question database model. """
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, unique=False, nullable=False)
    order = db.Column(db.Integer, unique=False, nullable=False)

    supervisor_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)
    opponent_thesis_id = db.Column(
        db.Integer, db.ForeignKey('theses.id'), nullable=True)

    def __repr__(self):
        return f"<Question {self.text}>"
