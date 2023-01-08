import os
import subprocess
import smtplib
import ssl

from datetime import datetime
from random import randint, choice
from unidecode import unidecode
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLASS = "demo"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASS_DIR = os.path.join(BASE_DIR, CLASS)

EMAIL = "adam.klepac@gevo.cz"
PASS = "*************"


def read_students() -> dict[str, list[int]]:
    """ Read students from file. """

    with open(
        os.path.join(CLASS_DIR, "studenti.txt"), "r", encoding="utf-8"
    ) as file:
        students = {line.strip(): [1, 2, 3] for line in file.readlines()}

    return students


def create_exam(student: str, questions: list[tuple[str, int]]) -> None:
    """ Create exam for student. """

    decoded_student_name = "-".join(unidecode(name).lower()
                                    for name in student.split(" "))

    with open(
        os.path.join(BASE_DIR, "template.tex"), "r", encoding="utf-8"
    ) as file:
        template = file.readlines()

    template[3] = f"{template[3].strip()} {student}\n"
    for author, number in questions:
        decoded_author_name = "-".join(unidecode(name).lower()
                                       for name in author.split(" "))
        template.insert(
            6,
            f"  \\input{{{decoded_author_name}-{number}.tex}}\n"
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


def main():
    """ Main function. """

    # read students
    students = read_students()

    # eliminate one question of each student
    for student in students:
        students[student].pop(randint(0, 2))

    # distribute questions among students randomly
    chosen_questions = {}
    for student in students:
        chosen_questions[student] = []
        for _ in range(2):
            author = choice(list(students.keys()))
            while len(students[author]) == 0 or author == student:
                author = choice(list(students.keys()))

            question = choice(students[author])
            students[author].remove(question)
            chosen_questions[student].append((author, question))

    # create exams for each student
    for student, questions in chosen_questions.items():
        create_exam(student, questions)

    # build exams using pdflatex
    build_exams()

    # send exams via Gmail
    send_exams(list(students.keys()))


if __name__ == '__main__':
    main()
