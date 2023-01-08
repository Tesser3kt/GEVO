import os
import subprocess
import smtplib
import ssl

from datetime import datetime
from random import randint, choice
from unidecode import unidecode
from collections import defaultdict
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLASS = "4b2"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASS_DIR = os.path.join(BASE_DIR, CLASS)

EMAIL = "adam.klepac@gevo.cz"
PASS = "*************"


def read_questions_data() -> dict[str, list[tuple[int, int]]]:
    """ Read students from file. """

    question_data = defaultdict(list)
    with open(
        os.path.join(CLASS_DIR, "studenti.txt"), "r", encoding="utf-8"
    ) as file:
        for line in file.readlines():
            name, questions = line.strip().split(":")
            values = questions.split("|")

            for value in values:
                index, percentage = tuple(value.split(","))
                question_data[name].append((int(index), int(percentage)))

    return question_data


def create_exam(student: str, questions: list[tuple[str, int]]) -> None:
    """ Create exam for student. """

    decoded_student_name = "-".join(unidecode(name).lower()
                                    for name in student.split(" "))

    with open(
        os.path.join(BASE_DIR, "template.tex"), "r", encoding="utf-8"
    ) as file:
        template = file.readlines()

    template[7] = f"{template[7].strip()} {student}\n"
    for author, number in questions:
        decoded_author_name = "-".join(unidecode(name).lower()
                                       for name in author.split(" "))
        template.insert(
            10,
            f"  \\input{{{decoded_author_name}-{number[0]}.tex}}\n"
        )

    with open(
        os.path.join(CLASS_DIR, f"{decoded_student_name}-exam.tex"),
        "w",
        encoding="utf-8"
    ) as file:
        file.writelines(template)


def build_exams() -> None:
    """ Build exams. """

    for file in os.listdir(CLASS_DIR):
        if file.endswith("-exam.tex"):
            subprocess.run(
                [
                    "pdflatex",
                    "-output-directory",
                    CLASS_DIR,
                    os.path.join(CLASS_DIR, file)
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )


def send_exams(students: list[str]) -> None:
    """ Send exams to students. """

    decoded_names = []
    for student in students:
        decoded_name = [unidecode(name).lower() for name in student.split(" ")]
        decoded_names.append(decoded_name)

    for decoded_name in decoded_names:
        sender_email = EMAIL
        receiver_email = f"{'.'.join(decoded_name)}@gevo.cz"
        subject = f"IVT Test - {datetime.today().strftime('%d.%m.%Y')}"
        body = "Posílám náhodně přiřazený test z IVT."

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        filename = os.path.join(
            CLASS_DIR,
            f"{'-'.join(decoded_name)}-exam.pdf"
        )
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(filename)}",
        )

        message.attach(part)
        text = message.as_string()

        port = 465
        smtp_server = "smtp.gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            smtp_server, port, context=context
        ) as server:
            server.login(EMAIL, PASS)
            server.sendmail(sender_email, receiver_email, text)


def good_questions(student: str, chosen_questions: list) -> True:
    """ Determines if the chosen questions sum up to 100% and are from a
    different student. """

    total = 0
    if len(chosen_questions) != 2:
        return False

    if chosen_questions[0][0] == chosen_questions[1][0]:
        return False

    for author, question in chosen_questions:
        if author == student:
            return False

        total += question[1]

    return total == 100


def questions_distributed(questions_data: dict, chosen_questions: dict) -> bool:
    """ Determines if all questions are distributed. """

    if len(chosen_questions.keys()) != len(questions_data.keys()):
        return False

    for student in chosen_questions:
        if not good_questions(student, chosen_questions[student]):
            return False

    return True


def copy_dict(dictionary: dict) -> dict:
    """ Copy dictionary. """

    new_dict = {}
    for key in dictionary:
        new_dict[key] = dictionary[key].copy()

    return new_dict


def distribute_questions(questions_data: dict, chosen_questions: dict,
                         used_questions: set, distributions: list) -> None:
    """ Distribute questions among students. """

    if questions_distributed(questions_data, chosen_questions):
        distributions.append(copy_dict(chosen_questions))
        return

    if len(distributions) > 0:
        return

    for student_name in questions_data:
        if len(chosen_questions[student_name]) == 2:
            continue

        for author_name in questions_data:
            if len(questions_data[author_name]) == 0:
                continue

            if author_name == student_name:
                continue

            if len(questions_data[author_name]) == 1:
                question = questions_data[author_name].pop()
            else:
                question = questions_data[author_name].pop(randint(0, 1))
            chosen_questions[student_name].append((author_name, question))

            distribute_questions(
                questions_data, chosen_questions,
                used_questions, distributions
            )

            chosen_questions[student_name].pop()
            questions_data[author_name].append(question)


def main():
    """ Main function. """

    # read students
    questions_data = read_questions_data()

    # eliminate one question of each student
    for student_name in questions_data:
        questions_data[student_name].pop(randint(0, 2))

    # distribute questions among students randomly
    possible_distributions = []
    distribute_questions(questions_data, defaultdict(
        list), set(), possible_distributions)

    chosen_questions = choice(possible_distributions)

    # create exams for each student
    for student_name, questions in chosen_questions.items():
        create_exam(student_name, questions)

    # build exams using pdflatex
    build_exams()

    # send exams via Gmail
    # send_exams(list(students.keys()))


if __name__ == '__main__':
    main()
