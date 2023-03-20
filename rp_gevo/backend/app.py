import os
import csv
import subprocess
from subprocess import TimeoutExpired, SubprocessError, CalledProcessError
from datetime import datetime
from config import *

from flask import Flask, url_for, redirect, session, abort, request, send_file
from flask_sqlalchemy import SQLAlchemy

import openpyxl
import unidecode as ud

# allow insecure transport for development
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# create Flask app
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

# configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# create SQLAlchemy object
db = SQLAlchemy()
db.init_app(app)

# import models
from models import *


@app.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


@app.route('/api/current-user', methods=['GET'])
def current_user():
    """ Get current user. """
    if 'id' in session:
        return {
            'id': session['id'],
            'name': session['name'],
            'email': session['email'],
            'role': session['role']
        }
    else:
        return {
            'id': None,
            'name': None,
            'email': None,
            'role': None
        }


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    """ Log in user. """
    if request.method == 'POST':
        # get user info from request
        user_info = request.get_json()

        # get user from database
        teacher = Teacher.query.filter_by(email=user_info['email']).first()
        student = Student.query.filter_by(email=user_info['email']).first()

        # check if user exists
        if teacher is None and student is None:
            return {
                'id': None,
                'name': None,
                'email': None,
                'role': None
            }

        user = teacher if teacher is not None else student
        session['id'] = user.id
        session['name'] = user.name
        session['email'] = user.email
        session['role'] = user.role
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
    else:
        abort(405)


@app.route('/api/logout', methods=['GET'])
def logout():
    """ Log out user. """
    session.clear()
    return {
        'logout': 'success'
    }


@app.route('/api/theses', methods=['GET'])
def theses():
    """ Get theses table data. """
    if 'id' in session:
        if session['role'] == 'teacher':
            supervised_theses = Thesis.query.filter_by(
                supervisor_id=session['id']
            ).all()
            opposed_theses = Thesis.query.filter_by(
                opponent_id=session['id']
            ).all()

            return {
                'authored': None,
                'supervised': [thesis.basic_data()
                               for thesis in supervised_theses],
                'opposed': [thesis.basic_data()
                            for thesis in opposed_theses],
                'other': None
            }

        elif session['role'] == 'student':
            authored_theses = Thesis.query.filter_by(
                author_id=session['id']
            ).all()

            return {
                'authored': [thesis.basic_data()
                             for thesis in authored_theses],
                'supervised': None,
                'opposed': None,
                'other': None
            }

        elif session['role'] == 'admin':
            supervised_theses = Thesis.query.filter_by(
                supervisor_id=session['id']
            )
            opposed_theses = Thesis.query.filter_by(
                opponent_id=session['id']
            )
            all_theses = Thesis.query.all()
            return {
                'authored': [],
                'supervised': [thesis.basic_data()
                               for thesis in supervised_theses],
                'opposed': [thesis.basic_data()
                            for thesis in opposed_theses],
                'other': [thesis.basic_data()
                          for thesis in all_theses if
                          thesis not in supervised_theses and
                          thesis not in opposed_theses]
            }

    else:
        abort(401)


@app.route('/api/thesis-data', methods=['GET', 'POST'])
def thesis_data():
    """ Upload thesis data. """
    if request.method == 'POST':
        thesis_basic_data = request.get_json()
        thesis = Thesis.query.filter_by(id=thesis_basic_data['id']).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }

        thesis.title = thesis_basic_data['title']

        if thesis_basic_data['supervisor']:
            supervisor = Teacher.query.filter_by(
                name=thesis_basic_data['supervisor']
            ).first()
            if not supervisor:
                return {
                    'success': False,
                    'message': (f'Učitel jménem '
                                f'{thesis_basic_data["supervisor"]} '
                                f'nebyl nalezen v databázi.')
                }
            thesis.supervisor_id = supervisor.id
        else:
            return {
                'success': False,
                'message': 'Musíte vybrat vedoucího práce.'
            }

        if thesis_basic_data['opponent']:
            opponent = Teacher.query.filter_by(
                name=thesis_basic_data['opponent']
            ).first()
            if not opponent:
                return {
                    'success': False,
                    'message': (f'Učitel jménem '
                                f'{thesis_basic_data["opponent"]} '
                                f'nebyl nalezen v databázi.')
                }
            thesis.opponent_id = opponent.id
        else:
            thesis.opponent_id = None

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': 'Nastala chyba při ukládání dat do databáze.'
            }

        return {
            'success': True,
            'message': 'Údaje byly úspěšně uloženy.',
            'new_thesis_data': thesis.basic_data()
        }
    else:
        abort(405)


@app.route('/api/thesis-evaluation', methods=['GET', 'POST'])
def thesis_evaluation():
    """ Upload and get thesis evaluation. """
    if request.method == 'POST':
        thesis_evaluation_data = request.get_json()
        thesis = Thesis.query.filter_by(
            id=thesis_evaluation_data['id']).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }
        grades = thesis_evaluation_data['grades']
        if thesis_evaluation_data['from'] == 'supervisor':
            evaluation = Evaluation.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).first()
            if not evaluation:
                new_evaluation = Evaluation(
                    formulation=grades[0],
                    methodology=grades[1],
                    bibliography=grades[2],
                    structure=grades[3],
                    contribution=grades[4],
                    terminology=grades[5],
                    citations=grades[6],
                    language=grades[7],
                    formatting=grades[8],
                    results=grades[9],
                    supervisor_thesis_id=thesis.id
                )
                db.session.add(new_evaluation)
            else:
                evaluation.formulation = grades[0]
                evaluation.methodology = grades[1]
                evaluation.bibliography = grades[2]
                evaluation.structure = grades[3]
                evaluation.contribution = grades[4]
                evaluation.terminology = grades[5]
                evaluation.citations = grades[6]
                evaluation.language = grades[7]
                evaluation.formatting = grades[8]
                evaluation.results = grades[9]

        elif thesis_evaluation_data['from'] == 'opponent':
            evaluation = Evaluation.query.filter_by(
                opponent_thesis_id=thesis.id
            ).first()
            if not evaluation:
                new_evaluation = Evaluation(
                    formulation=grades[0],
                    methodology=grades[1],
                    bibliography=grades[2],
                    structure=grades[3],
                    contribution=grades[4],
                    terminology=grades[5],
                    results=grades[6],
                    opponent_thesis_id=thesis.id
                )
                db.session.add(new_evaluation)
            else:
                evaluation.formulation = grades[0]
                evaluation.methodology = grades[1]
                evaluation.bibliography = grades[2]
                evaluation.structure = grades[3]
                evaluation.contribution = grades[4]
                evaluation.terminology = grades[5]
                evaluation.results = grades[6]

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': 'Nastala chyba při ukládání dat do databáze.'
            }

        return {
            'success': True,
            'message': 'Údaje byly úspěšně uloženy.'
        }

    elif request.method == 'GET':
        thesis_id = request.args.get('id')
        user_for = request.args.get('for')
        if not thesis_id:
            return {
                'success': False,
                'message': 'Nebylo zadáno ID práce.'
            }
        thesis = Thesis.query.filter_by(id=thesis_id).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }
        if user_for == 'supervisor':
            evaluation = Evaluation.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).first()
            if evaluation:
                return {
                    'success': True,
                    'grades': [
                        evaluation.formulation,
                        evaluation.methodology,
                        evaluation.bibliography,
                        evaluation.structure,
                        evaluation.contribution,
                        evaluation.terminology,
                        evaluation.citations,
                        evaluation.language,
                        evaluation.formatting,
                        evaluation.results
                    ]
                }
            else:
                return {
                    'success': True,
                    'grades': [0] * 10
                }

        elif user_for == 'opponent':
            evaluation = Evaluation.query.filter_by(
                opponent_thesis_id=thesis.id
            ).first()
            if evaluation:
                return {
                    'success': True,
                    'grades': [
                        evaluation.formulation,
                        evaluation.methodology,
                        evaluation.bibliography,
                        evaluation.structure,
                        evaluation.contribution,
                        evaluation.terminology,
                        evaluation.results
                    ]
                }
            else:
                return {
                    'success': True,
                    'grades': [0] * 7
                }

        else:
            return {
                'success': False,
                'message': 'Nebyla zadána role uživatele.'
            }

    else:
        abort(405)


@app.route('/api/thesis-review', methods=['GET', 'POST'])
def thesis_review():
    """ Upload and get thesis reviews. """
    if request.method == 'POST':
        thesis_review_data = request.get_json()
        thesis = Thesis.query.filter_by(
            id=thesis_review_data['id']).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }
        review_text = thesis_review_data['review']
        if thesis_review_data['from'] == 'supervisor':
            review = Review.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).first()
            if not review:
                new_review = Review(
                    text=review_text,
                    supervisor_thesis_id=thesis.id
                )
                db.session.add(new_review)
            else:
                review.text = review_text

        elif thesis_review_data['from'] == 'opponent':
            review = Review.query.filter_by(
                opponent_thesis_id=thesis.id
            ).first()
            if not review:
                new_review = Review(
                    text=review_text,
                    opponent_thesis_id=thesis.id
                )
                db.session.add(new_review)
            else:
                review.text = review_text

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': 'Nastala chyba při ukládání dat do databáze.'
            }

        return {
            'success': True,
            'message': 'Údaje byly úspěšně uloženy.'
        }

    elif request.method == 'GET':
        thesis_id = request.args.get('id')
        user_for = request.args.get('for')
        if not thesis_id:
            return {
                'success': False,
                'message': 'Nebylo zadáno ID práce.'
            }
        thesis = Thesis.query.filter_by(id=thesis_id).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }

        if user_for == 'supervisor':
            review = Review.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).first()
            if review:
                return {
                    'success': True,
                    'review': review.text
                }
            else:
                return {
                    'success': True,
                    'review': ''
                }
        elif user_for == 'opponent':
            review = Review.query.filter_by(
                opponent_thesis_id=thesis.id
            ).first()
            if review:
                return {
                    'success': True,
                    'review': review.text
                }
            else:
                return {
                    'success': True,
                    'review': ''
                }
        else:
            return {
                'success': False,
                'message': 'Nebyla zadána role uživatele.'
            }

    else:
        abort(405)


@app.route('/api/thesis-questions', methods=['GET', 'POST'])
def thesis_questions():
    """ Upload and get thesis questions. """
    if request.method == 'POST':
        thesis_questions_data = request.get_json()
        thesis = Thesis.query.filter_by(
            id=thesis_questions_data['id']).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }
        questions = thesis_questions_data['questions']
        # update thesis questions by order

        if thesis_questions_data['from'] == 'supervisor':
            for i in range(len(questions)):
                question = Question.query.filter_by(
                    supervisor_thesis_id=thesis.id,
                    order=i
                ).first()
                if not question:
                    new_question = Question(
                        text=questions[i]['text'],
                        order=i,
                        supervisor_thesis_id=thesis.id
                    )
                    db.session.add(new_question)
                else:
                    question.text = questions[i]['text']
            # delete questions that are not in the list
            questions_to_delete = Question.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).filter(
                Question.order >= len(questions)
            ).all()
            for question in questions_to_delete:
                db.session.delete(question)

        elif thesis_questions_data['from'] == 'opponent':
            for i in range(len(questions)):
                question = Question.query.filter_by(
                    opponent_thesis_id=thesis.id,
                    order=i
                ).first()
                if not question:
                    new_question = Question(
                        text=questions[i]['text'],
                        order=i,
                        opponent_thesis_id=thesis.id
                    )
                    db.session.add(new_question)
                else:
                    question.text = questions[i]['text']
            # delete questions that are not in the list
            questions_to_delete = Question.query.filter_by(
                opponent_thesis_id=thesis.id
            ).filter(
                Question.order >= len(questions)
            ).all()
            for question in questions_to_delete:
                db.session.delete(question)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': 'Nastala chyba při ukládání dat do databáze.'
            }

        return {
            'success': True,
            'message': 'Údaje byly úspěšně uloženy.'
        }

    elif request.method == 'GET':
        thesis_id = request.args.get('id')
        user_for = request.args.get('for')
        if not thesis_id:
            return {
                'success': False,
                'message': 'Nebylo zadáno ID práce.'
            }
        thesis = Thesis.query.filter_by(id=thesis_id).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }

        if user_for == 'supervisor':
            questions = Question.query.filter_by(
                supervisor_thesis_id=thesis.id
            ).order_by(Question.order).all()
            if questions:
                return {
                    'success': True,
                    'questions': [
                        {
                            'text': question.text,
                            'order': question.order
                        }
                        for question in questions
                    ]
                }
            else:
                return {
                    'success': True,
                    'questions': []
                }
        elif user_for == 'opponent':
            questions = Question.query.filter_by(
                opponent_thesis_id=thesis.id
            ).order_by(Question.order).all()
            if questions:
                return {
                    'success': True,
                    'questions': [
                        {
                            'text': question.text,
                            'order': question.order
                        }
                        for question in questions
                    ]
                }
            else:
                return {
                    'success': True,
                    'questions': []
                }
        else:
            return {
                'success': False,
                'message': 'Nebyla zadána role uživatele.'
            }
    else:
        abort(405)


@app.route('/api/thesis-pdf', methods=['GET'])
def thesis_pdf():
    """ Generate thesis PDF. """
    if request.method == 'GET':
        thesis_id = request.args.get('id')
        user_from = request.args.get('from')
        if not thesis_id:
            return {
                'success': False,
                'message': 'Nebylo zadáno ID práce.'
            }
        thesis = Thesis.query.filter_by(id=thesis_id).first()
        if not thesis:
            return {
                'success': False,
                'message': 'Práce s tímto ID nebyla nalezena v databázi.'
            }
        filepath = __fill_template_file(user_from, thesis)
        if filepath != '':
            print(filepath)
            return send_file(filepath.replace('.tex', '.pdf'),
                             as_attachment=True)
        return {
            'success': False,
            'message': ('Nastala chyba při generování PDF. Ověřte, že jste '
                        'vyplnili a uložili všechny údaje.')
        }
    else:
        abort(405)


def __fill_template_file(user_job, thesis):
    template = open(f'template_{user_job}.tex', 'r', encoding='utf-8')
    final_name = (f"{str(thesis.author.class_)}_"
                  f"{thesis.author.name.replace(' ', '_')}_"
                  "RP_"
                  f"{'PV' if user_job == 'supervisor' else 'PO'}_"
                  f"{thesis.academic_year[:2] + thesis.academic_year[-2:]}"
                  ".tex")
    final_folder = os.path.join(os.path.dirname(__file__), 'final')
    final_path = os.path.join(final_folder, final_name)
    final = open(final_path, 'w+', encoding='utf-8')

    template_text = template.read()

    # basic data
    template_text = template_text.replace(r'%%TITLE%%', thesis.title)
    template_text = template_text.replace(
        r'%%AUTHOR%%', f'{thesis.author.name}, {str(thesis.author.class_)}'
    )
    if user_job == 'supervisor':
        template_text = template_text.replace(
            r'%%SUPERVISOR%%', thesis.supervisor.name
        )
    else:
        if not thesis.opponent_id:
            template.close()
            final.close()
            return ''
        template_text = template_text.replace(
            r'%%OPPONENT%%', thesis.opponent.name
        )

    # evaluation
    if user_job == 'supervisor':
        evaluation = Evaluation.query.filter_by(
            supervisor_thesis_id=thesis.id
        ).first()
    else:
        evaluation = Evaluation.query.filter_by(
            opponent_thesis_id=thesis.id
        ).first()

    if not evaluation:
        template.close()
        final.close()
        return ''

    template_text = template_text.replace(
        r'%%FORMULATION%%', f'{evaluation.formulation} \\%'
    )
    template_text = template_text.replace(
        r'%%METHODOLOGY%%', f'{evaluation.methodology} \\%'
    )
    template_text = template_text.replace(
        r'%%BIBLIOGRAPHY%%', f'{evaluation.bibliography} \\%'
    )
    template_text = template_text.replace(
        r'%%STRUCTURE%%', f'{evaluation.structure} \\%'
    )
    template_text = template_text.replace(
        r'%%CONTRIBUTION%%', f'{evaluation.contribution} \\%'
    )
    template_text = template_text.replace(
        r'%%TERMINOLOGY%%', f'{evaluation.terminology} \\%'
    )
    template_text = template_text.replace(
        r'%%RESULTS%%', f'{evaluation.results} \\%'
    )
    if user_job == 'supervisor':
        template_text = template_text.replace(
            r'%%CITATIONS%%', f'{evaluation.citations} \\%'
        )
        template_text = template_text.replace(
            r'%%LANGUAGE%%', f'{evaluation.language} \\%'
        )
        template_text = template_text.replace(
            r'%%FORMATTING%%', f'{evaluation.formatting} \\%'
        )
    template_text = template_text.replace(
        r'%%WEIGHTED MEAN%%', f'{evaluation.weighted_mean} \\%'
    )

    # review
    if user_job == 'supervisor':
        review = Review.query.filter_by(
            supervisor_thesis_id=thesis.id
        ).first()
    else:
        review = Review.query.filter_by(
            opponent_thesis_id=thesis.id
        ).first()

    if not review:
        template.close()
        final.close()
        return ''

    template_text = template_text.replace(
        r'%%REVIEW%%', review.text
    )

    # questions
    if user_job == 'supervisor':
        questions = Question.query.filter_by(
            supervisor_thesis_id=thesis.id
        ).order_by(Question.order).all()
    else:
        questions = Question.query.filter_by(
            opponent_thesis_id=thesis.id
        ).order_by(Question.order).all()

    if not questions:
        template.close()
        final.close()
        return ''

    questions_text = [
        f'\\item {question.text}'
        for question in questions
    ]
    template_text = template_text.replace(
        r'%%QUESTIONS%%', '\n'.join(questions_text)
    )

    # date
    template_text = template_text.replace(
        r'%%DATE%%', datetime.now().strftime('%d.%m.%Y')
    )

    final.write(template_text)
    final.close()
    template.close()

    try:
        os.chdir(final_folder)
        p = subprocess.Popen(['pdflatex', final_name])
        p.wait(timeout=10)
        os.chdir(os.path.dirname(__file__))
    except Exception as e:
        print(e)
        os.chdir(os.path.dirname(__file__))
        p.kill()
        return ''

    return final_path


def __register_name(name_list, class_, role):
    if not name_list:
        return None

    if len(name_list) == 2:
        name = f"{name_list[1]} {name_list[0]}"
    elif len(name_list) == 3:
        name = (f"{name_list[1]} {name_list[2]}"
                f" {name_list[0]}")

    if role == 'teacher':
        user = Teacher.query.filter_by(name=name).first()
    elif role == 'student':
        user = Student.query.filter_by(name=name).first()

    if user is None:
        if role == 'teacher':
            user = Teacher(
                    name=name,
                    email=(ud.unidecode(name).replace(' ', '.').lower()
                           + '@gevo.cz'),
                    role='teacher'
                )
        elif role == 'student':
            grade = class_.split('.')[0]
            letter = class_.split('.')[1]
            class_ = Class.query.filter_by(grade=grade,
                                           letter=letter).first()

            if class_ is None:
                class_ = Class(
                        grade=grade,
                        letter=letter
                    )
                db.session.add(class_)
                db.session.commit()

            user = Student(
                    name=name,
                    email=(ud.unidecode(name).replace(' ', '.').lower()
                           + '@gevo.cz'),
                    role='student',
                    class_id=class_.id
                )

        if user:
            db.session.add(user)
            db.session.commit()

    return user


def populate_from_excel_table():
    workbook = openpyxl.load_workbook('data_rocnikovky.xlsx')
    sheet = workbook.active

    rows = []
    for row in sheet.iter_rows(min_row=3, max_row=60):
        row_data = {
            'skolitel': row[0].value,
            'student': row[1].value,
            'prace': row[2].value,
            'oponent': row[3].value,
            'trida': row[4].value
        }
        rows.append(row_data)

    for row in rows:
        supervisor = __register_name(row['skolitel'].split(' '),
                                     '', 'teacher')
        student = __register_name(row['student'].split(' '),
                                  row['trida'], 'student')
        if row['oponent']:
            opponent = __register_name(row['oponent'].split(' '),
                                       '', 'teacher')

        if supervisor and student and row['prace']:
            thesis = Thesis(
                title=row['prace'],
                academic_year='2022/23',
                supervisor_id=supervisor.id,
                author_id=student.id,
                opponent_id=opponent.id if row['oponent'] else None,
                supervisor_finalized=False,
                opponent_finalized=False
            )
            db.session.add(thesis)
            db.session.commit()


def populate_from_teachers_csv():
    with open('teachers.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            teacher = Teacher.query.filter_by(email=row[1]).first()
            if teacher:
                continue

            teacher = Teacher(
                name=row[0],
                email=row[1],
                role='teacher'
            )
            db.session.add(teacher)
            db.session.commit()


if __name__ == '__main__':
    # run app
    app.run()
