import os
import subprocess
import smtplib
import ssl

from random import choice, shuffle
from copy import deepcopy
from dataclasses import dataclass
from collections import defaultdict
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unidecode import unidecode as ud

CLASS = "4a2"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASS_DIR = os.path.join(BASE_DIR, CLASS)

EMAIL = "adam.klepac@gevo.cz"
PASS = "Ad031169Kle9410"


@dataclass
class Question:
    author: str
    index: int
    percentage: int

    def __eq__(self, __o: object) -> bool:
        return (self.author == __o.author and
                self.index == __o.index)

    def __add__(self, __o: object) -> int:
        return self.percentage + __o.percentage

    def __repr__(self) -> str:
        return (f"Question {self.index} by "
                f"{self.author} for {self.percentage} %.")


@dataclass
class Student:
    name: str
    middle_name: str
    surname: str
    submitted: bool
    authored_questions: list[Question]
    exam_questions: list[Question]

    def __eq__(self, __o: object) -> bool:
        return (self.name == __o.name and
                self.middle_name == __o.middle_name and
                self.surname == __o.surname)

    def __repr__(self) -> str:
        return f"{self.full_name}"

    @property
    def full_name(self) -> str:
        if self.middle_name != "":
            return f"{self.name} {self.middle_name} {self.surname}"
        return f"{self.name} {self.surname}"

    @property
    def decoded_name(self) -> str:
        if self.middle_name != "":
            return (f"{ud(self.name).lower()}-{ud(self.middle_name).lower()}-"
                    f"{ud(self.surname).lower()}")
        return f"{ud(self.name).lower()}-{ud(self.surname).lower()}"

    @property
    def email(self) -> str:
        if self.middle_name != "":
            return (f"{ud(self.name).lower()}.{ud(self.middle_name).lower()}."
                    f"{ud(self.surname).lower()}@gevo.cz")
        return f"{ud(self.name).lower()}.{ud(self.surname).lower()}@gevo.cz"

    def add_exam_question(self, question: Question) -> bool:
        if len(self.exam_questions) == 0:
            if question.author == self.full_name:
                return False
            self.exam_questions.append(question)
            return True

        if len(self.exam_questions) == 1:
            if question.author != "Pan Rezerva":
                if question.author == self.full_name:
                    return False
                if question.author == self.exam_questions[0].author:
                    return False

            if question + self.exam_questions[0] != 100:
                return False

            self.exam_questions.append(question)
            return True

    def remove_exam_question(self, question: Question) -> None:
        if question in self.exam_questions:
            self.exam_questions.remove(question)


def read_questions_data() -> list[Student]:
    """ Read students from file. """

    students = []
    with open(
        os.path.join(CLASS_DIR, "studenti.txt"), "r", encoding="utf-8"
    ) as file:
        for line in file.readlines():
            name, questions = line.strip().split(":")
            name_list = name.split(" ")
            if len(name_list) == 2:
                name, surname = tuple(name_list)
                middle_name = ""
            elif len(name_list) == 3:
                name, middle_name, surname = tuple(name_list)

            student = Student(
                name=name,
                middle_name=middle_name,
                surname=surname,
                submitted=True,
                authored_questions=[],
                exam_questions=[]
            )
            if questions == "rezerva":
                student.submitted = False
                students.append(student)
                continue

            values = questions.split("|")

            for value in values:
                index, percentage = tuple(value.split(","))
                question = Question(
                    author=student.full_name,
                    index=int(index),
                    percentage=int(percentage)
                )
                student.authored_questions.append(question)
            students.append(student)

    return students


def good_distribution(students: list[Student], rezerva: Student) -> bool:
    for student in students:
        if student == rezerva:
            continue
        if len(student.exam_questions) != 2:
            return False
    return True


def distribute_questions(
    students: list[Student],
    rezerva: Student,
    used_questions: set[Question],
    num_of_questions_by: dict[str, int],
    possible_distributions: list[list[Student]]
):

    if len(possible_distributions) > 20:
        return

    if good_distribution(students, rezerva):
        possible_distributions.append(deepcopy(students))
        return

    for student in students:
        if student == rezerva:
            continue

        if len(student.exam_questions) == 2:
            continue

        if not student.submitted:
            for question in rezerva.authored_questions:
                if str(question) in used_questions:
                    continue

                if not student.add_exam_question(question):
                    continue

                used_questions.add(str(question))
                distribute_questions(
                    students, rezerva, used_questions,
                    num_of_questions_by, possible_distributions
                )
                used_questions.remove(str(question))

            continue

        for other_student in students:
            if other_student == rezerva:
                continue

            if num_of_questions_by[other_student.full_name] == 2:
                continue

            for question in other_student.authored_questions:
                if str(question) in used_questions:
                    continue

                if not student.add_exam_question(question):
                    continue

                used_questions.add(str(question))
                num_of_questions_by[other_student.full_name] += 1

                distribute_questions(
                    students, rezerva, used_questions, num_of_questions_by,
                    possible_distributions
                )

                used_questions.remove(str(question))
                num_of_questions_by[other_student.full_name] -= 1
                student.remove_exam_question(question)


def create_exam(student: Student) -> None:
    """ Create exam for student. """

    with open(
        os.path.join(BASE_DIR, "template.tex"), "r", encoding="utf-8"
    ) as file:
        template = file.readlines()

    template[7] = f"{template[7].strip()} {student}\n"
    for question in student.exam_questions:
        decoded_author_name = "-".join(ud(name).lower()
                                       for name in question.author.split(" "))
        file_path = f"{decoded_author_name}-{question.index}.tex"
        if question.author == "Pan Rezerva":
            file_path = f"../rezerva/rezerva-{question.index}.tex"

        template.insert(
            9,
            f"  \\input{{{file_path}}}\n"
        )

    with open(
        os.path.join(CLASS_DIR, f"{student.decoded_name}-exam.tex"),
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


def send_exams(students: list[Student]):
    """ Send exams to students. """

    for student in students:
        if student.surname == "Rezerva":
            continue

        sender_email = EMAIL
        receiver_email = student.email
        subject = f"IVT DÚ - do 18. 1. 2023"
        body = (
            "Čau,\n"
            "\n"
            "moc se omlouvám za zdržení. Protože jsme se dohodli, že test uděláme radši formou domácího úkolu,"
            " posílám náhodně vybrané otázky (pokud můj program funguje). Ti z vás, "
            "kdo mi odevzdali předchozí domácí úkol, mají "
            "přidělené otázky od ostatních, kdo taky odevzdali. Ti, kdo ne, mají přiřazené nějaké ode mě. "
            "Ještě pošlu některé úlohy vyřešené na Classroom.\n"
            "\n"
            "Máte právo na celkem dvě odevzdání. Když mi úkol poprvé pošlete a "
            "nebude dobře, vrátím vám ho s komentáři k předělání. Druhé odevzdání "
            "je definitivní. Úkoly odevzdávejte jako soubor s koncovkou .py; "
            "fotky a screenshoty nebo - Nedej, Bože! - textové dokumenty "
            "neberu. Na další hodině vás budu obcházet a ptát se na vaše řešení, abych "
            "si byl jistý, že jim rozumíte. S těmi, kdo nepřijdou, se domluvím individuálně.\n"
            "\n"
            "Adam"
        )

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        filename = os.path.join(
            CLASS_DIR,
            f"{student.decoded_name}-exam.pdf"
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
    students = read_questions_data()
    rezerva = students[-1]

    # shuffle students and their questions
    # shuffle(students)
    # for student in students:
    #     shuffle(student.authored_questions)

    # distribute questions among students randomly
    # possible_distributions = []
    # distribute_questions(students, rezerva, set(), defaultdict(int),
    #                      possible_distributions)

    # create exams for each student
    # for student in choice(possible_distributions):
    #     if student.surname == "Rezerva":
    #         continue
    #     create_exam(student)

    # build exams using pdflatex
    # build_exams()

    # send exams via Gmail
    send_exams(students)


if __name__ == '__main__':
    main()
