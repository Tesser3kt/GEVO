import csv
import datetime as dt
from random import choice
from enum import Enum
from collections import defaultdict
import pandas as pd
from openai import OpenAI
from valentyn_troll_config import OPENAI_API_KEY


class Signs(Enum):
    CHINESE = "chinese_zodiac"
    ZODIAC = "zodiac"
    CELTIC = "celtic_zodiac"
    ANGEL = "angelic_number"
    STONE = "spiritual_stone"


COLUMNS = [
    "Příjmení",
    "Jméno",
    "Pohlaví",
    "Datum narození",
    "Andělské číslo",
    "Anděl strážný",
    "Popis anděla strážného",
    "Zvířecí znamení",
    "Kameny duše",
    "Živel",
    "Keltské znamení",
    "Čínské znamení",
]

CHINESE_ZODIAC = [
    "Krysa",
    "Bůvol",
    "Tygr",
    "Zajíc",
    "Drak",
    "Had",
    "Kůň",
    "Koza",
    "Opice",
    "Kohout",
    "Pes",
    "Vepř",
]

this_year = dt.date.today().year
celtic_zodiac_dates = {
    "Buk": pd.date_range(dt.date(this_year, 12, 21), periods=1).to_list(),
    "Jabloň": pd.date_range(dt.date(this_year, 6, 22), periods=11).tolist()
    + pd.date_range(dt.date(this_year, 12, 22), periods=11).to_list(),
    "Jedle": pd.date_range(dt.date(this_year, 1, 2), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 7, 3), periods=11).to_list(),
    "Jilm": pd.date_range(dt.date(this_year, 1, 12), periods=11).tolist()
    + pd.date_range(dt.date(this_year, 7, 14), periods=11).to_list(),
    "Cypřiš": pd.date_range(dt.date(this_year, 1, 23), periods=9).tolist()
    + pd.date_range(dt.date(this_year, 7, 25), periods=11).to_list(),
    "Topol": pd.date_range(dt.date(this_year, 11, 1), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 5, 1), periods=10).to_list()
    + pd.date_range(dt.date(this_year, 2, 1), periods=10).to_list()
    + pd.date_range(dt.date(this_year, 8, 5), periods=10).to_list(),
    "Borovice": pd.date_range(dt.date(this_year, 2, 21), periods=11).tolist()
    + pd.date_range(dt.date(this_year, 8, 25), periods=10).to_list(),
    "Modřín": pd.date_range(dt.date(this_year, 2, 11), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 8, 15), periods=10).to_list(),
    "Lípa": pd.date_range(dt.date(this_year, 3, 13), periods=8).tolist()
    + pd.date_range(dt.date(this_year, 9, 14), periods=9).to_list(),
    "Vrba": pd.date_range(dt.date(this_year, 3, 3), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 9, 4), periods=10).to_list(),
    "Dub": pd.date_range(dt.date(this_year, 3, 21), periods=1).tolist(),
    "Olše": pd.date_range(dt.date(this_year, 9, 23), periods=1).tolist(),
    "Jeřáb": pd.date_range(dt.date(this_year, 4, 1), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 10, 3), periods=9).to_list(),
    "Líska": pd.date_range(dt.date(this_year, 3, 22), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 9, 24), periods=9).to_list(),
    "Ořešák": pd.date_range(dt.date(this_year, 4, 21), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 10, 22), periods=10).to_list(),
    "Javor": pd.date_range(dt.date(this_year, 4, 11), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 10, 12), periods=10).to_list(),
    "Osika": pd.date_range(dt.date(this_year, 12, 11), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 6, 11), periods=10).tolist(),
    "Kaštan": pd.date_range(dt.date(this_year, 11, 11), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 5, 11), periods=10).tolist(),
    "Jasan": pd.date_range(dt.date(this_year, 11, 21), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 5, 21), periods=10).tolist(),
    "Habr": pd.date_range(dt.date(this_year, 12, 1), periods=10).tolist()
    + pd.date_range(dt.date(this_year, 5, 31), periods=11).tolist(),
}

CELTIC_ZODIAC = {
    key: set(map(lambda x: (x.day, x.month), value))
    for key, value in celtic_zodiac_dates.items()
}

zodiac_dates = {
    "Beran": pd.date_range(dt.date(this_year, 3, 21), periods=31).tolist(),
    "Býk": pd.date_range(dt.date(this_year, 4, 21), periods=31).tolist(),
    "Blíženci": pd.date_range(dt.date(this_year, 5, 22), periods=31).tolist(),
    "Rak": pd.date_range(dt.date(this_year, 6, 22), periods=31).tolist(),
    "Lev": pd.date_range(dt.date(this_year, 7, 23), periods=31).tolist(),
    "Panna": pd.date_range(dt.date(this_year, 8, 23), periods=31).tolist(),
    "Váhy": pd.date_range(dt.date(this_year, 9, 23), periods=31).tolist(),
    "Štír": pd.date_range(dt.date(this_year, 10, 24), periods=30).tolist(),
    "Střelec": pd.date_range(dt.date(this_year, 11, 23), periods=29).tolist(),
    "Kozoroh": pd.date_range(dt.date(this_year, 12, 22), periods=30).tolist(),
    "Vodnář": pd.date_range(dt.date(this_year, 1, 21), periods=31).tolist(),
    "Ryby": pd.date_range(dt.date(this_year, 2, 21), periods=29).tolist(),
}

ZODIAC = {
    key: set(map(lambda x: (x.day, x.month), value))
    for key, value in zodiac_dates.items()
}

SPIRITUAL_STONES = {
    "Vodnář": {"stones": ("jasmín", "opál"), "element": "vzduch"},
    "Ryby": {"stones": ("ametyst", "opál"), "element": "voda"},
    "Beran": {"stones": ("karneol", "jaspis"), "element": "oheň"},
    "Býk": {"stones": ("růženín", "achát"), "element": "země"},
    "Blíženci": {"stones": ("tygří oko",), "element": "vzduch"},
    "Rak": {"stones": ("karneol",), "element": "voda"},
    "Lev": {"stones": ("křišťál", "granát"), "element": "oheň"},
    "Panna": {"stones": ("citrín", "jaspis"), "element": "země"},
    "Váhy": {"stones": ("achát",), "element": "vzduch"},
    "Štír": {"stones": ("hematit", "jaspis"), "element": "voda"},
    "Střelec": {"stones": ("sodalit", "chalcedon"), "element": "oheň"},
    "Kozoroh": {"stones": ("obsidián", "ametyst", "onyx"), "element": "země"},
}

GUARDIAN_ANGELS = {
    1: {
        "name": "Raquel",
        "description": "Nad vámi bdí archanděl Raquel, která je známá tím, že dohlíží nad spravedlností a harmonií. Váš strážný anděl vám nejenom zaručuje, že se vám v životě nestane nějaká nespravedlivost, ale také vám dodá odvahu bojovat proti tomu, když se někomu děje příkoří. Učiní z vás ochránce slabších, využijte ve svém životě tuto výjimečnou moc.",
    },
    2: {
        "name": "Uriel",
        "description": "Archanděl Uriel ztělesňuje pravdu. Chrání vás před tím, aby s vámi ostatní manipulovali a lhali vám. Také vás podpoří v tom, abyste pravdu vyjevili i vy sami. S jeho pomocí budete schopni vnést světlo do situací, kdy není jasné, kdo mluví pravdu, a kdo lže. Také vám pomůže lépe se soustředit a mít jasnou mysl a dobrý úsudek.",
    },
    3: {
        "name": "Jophiel",
        "description": "Archanděl Jophiel je spjatý se vším krásným. Nebavíme se jen o tom, co je vidět očima, ale i o vnitřní kráse. Sesílá vám pozitivní myšlenky a nápady, kterými ze světa můžete udělat hezčí místo. Díky jeho vlivu oplýváte kreativitou a tvoříte úžasné věci. Také na vás „nemůžou“ negativní myšlenky, ty ve vaší mysli nemají místo.",
    },
    4: {
        "name": "Haniel",
        "description": "Archanděl Haniel vnáší do vašeho života radost. Snaží se vás v životě nasměřovat tak, abyste si nikdy nepřipadali ztracení. I když vás možná někdy potká zklamání, nebudete smutnit dlouho. Archanděl Haniel se postará o to, aby jste byli v životě spokojení a veselí. Svým smíchem a dobrou náladou jste schopni „nakazit“ i své okolí.",
    },
    5: {
        "name": "Jeremiel",
        "description": "Pokud je vaše životní číslo 5, pak nad vámi bdí archanděl Jeremiel, ochránce snů a vizí. Vaše síla myšlenky je neuvěřitelná, pokud si budete správně přát, máte šanci dosáhnout všeho, po čem v životě toužíte. Také k vám vysílá povzbuzující energii, snaží se vás motivovat, abyste naplnili svůj osud.",
    },
    6: {
        "name": "Michael",
        "description": "Pokud máte životní číslo 6, můžete si gratulovat. Pozor na vás dává výjimečně mocný archanděl Michael. Ten v sobě spojuje vlastnosti archandělů Raquel a Uriela, dopomůže vám k odhalení pravdy a nastolení spravedlnosti. Avšak co je ještě důležitější, dává vám sílu vyvést ostatní z nastalé krize. Lidé s vaším číslem jsou pro svět nesmírně důležití, právě oni mají sílu a moc postavit se všemu zlému.",
    },
    7: {
        "name": "Rafael",
        "description": "Archanděl Rafael je anděl léčitel. Drží nad vámi ochrannou ruku, pokud onemocníte a dává vám sílu uzdravit se. Také máte schopnost léčit druhé, zvažte kariéru ve zdravotnictví, v tomto oboru se vám bude dařit. Dobře snášíte bolest a rychle se vám od ní uleví, a to od té fyzické i psychické.",
    },
    8: {
        "name": "Raziel",
        "description": "Archanděl Raziel spravuje veškerá tajemství. Byl vám dán dar odhalit je, až nastane ten pravý čas. Umíte číst mezi řádky, snadno rozluštíte šifry a nikdo před vámi nic neutají. V životě vám pomáhá věci pochopit, dobře vyhodnotit a kriticky uvažovat. Některým lidem s životním číslem 8 byla do vínku dána i jasnozřivost.",
    },
    9: {
        "name": "Ariel",
        "description": "Archanděl Ariel je znám jako strážný anděl přírody. Zajímáte se o environmentální problémy a snažíte se chránit zvířata i rostliny. Archanděl Ariel vám v tom pomůže, potrestá ty, které identifikujete jako ničitele přírody. Dá vám sílu a odvahu bojovat za zachování krás přírody i talent učit tyto zásady druhé.",
    },
}

MAX_TRIES = 10


def split_name(name_to_split: str) -> tuple[str, str, str]:
    """Split the name into surname, first name and middle name."""
    if len(name_list := name_to_split.split(" ")) == 3:
        return tuple(name_list)
    return tuple(name_list + [""])


def birthdate_from_number(number: str) -> tuple[int, int, int]:
    """Return the birthdate from the number."""
    if len(number) != 6:
        return None

    birthdate = [
        int(number[4:6]),
        int(number[2:4]),
        int("20" + number[0:2]),
    ]
    if birthdate[1] > 12:
        birthdate[1] -= 50

    return tuple(birthdate)


def gender_from_number(number: str) -> str:
    """Converts personal number to gender."""
    if len(number) != 6:
        return

    return "muž" if int(number[2:4]) <= 12 else "žena"


def angelic_number(birthdate: tuple[int, int, int]) -> int:
    """Return the angelic number based on birthdate."""
    if not birthdate:
        return -1

    birthdate_string = "".join(map(str, birthdate))
    ang_number = sum(map(int, birthdate_string))
    while ang_number > 9:
        ang_number = sum(map(int, str(ang_number)))

    return ang_number


def chinese_zodiac(birthdate: tuple[int, int, int]) -> str:
    """Return the chinese zodiac based on birthdate."""
    if not birthdate:
        return -1

    birth_year = birthdate[2]
    return CHINESE_ZODIAC[(birth_year - 4) % 12]


def celtic_zodiac(birthdate: tuple[int, int, int]) -> str:
    """Return the celtic zodiac based on birthdate."""
    if not birthdate:
        return -1

    birth_day, birth_month, _ = birthdate
    for key, value in CELTIC_ZODIAC.items():
        if (birth_day, birth_month) in value:
            return key


def zodiac(birthdate: tuple[int, int, int]) -> str:
    """Return the zodiac based on birthdate."""
    if not birthdate:
        return -1

    birth_day, birth_month, _ = birthdate
    for key, value in ZODIAC.items():
        if (birth_day, birth_month) in value:
            return key


def spiritual_stone(zodiac_sign: str) -> str:
    """Return the spiritual stone based on zodiac."""
    if not zodiac_sign:
        return -1

    return SPIRITUAL_STONES[zodiac_sign]


def data_for_export(data: list) -> list:
    """Return the data for export."""
    return [
        {
            "Příjmení": student["surname"],
            "Jméno": (
                student["first_name"] + " " + student["middle_name"]
                if student["middle_name"]
                else student["first_name"]
            ),
            "Pohlaví": student["gender"],
            "Datum narození": dt.date(*reversed(student["birthdate"])).strftime(
                "%d.%m.%Y"
            ),
            "Andělské číslo": student["angelic_number"],
            "Anděl strážný": student["guardian_angel"],
            "Popis anděla strážného": student["guardian_angel_description"],
            "Zvířecí znamení": student["zodiac"],
            "Kameny duše": ", ".join(student["spiritual_stone"]["stones"]),
            "Živel": student["spiritual_stone"]["element"],
            "Keltské znamení": student["celtic_zodiac"],
            "Čínské znamení": student["chinese_zodiac"],
        }
        for student in data
    ]


def create_data() -> list:
    """Creates students' esoteric data and saves them in a csv."""
    students_data = []

    # Read the file
    with open("students.csv", "r", encoding="cp1250") as file:
        reader = csv.reader(file, delimiter=";")

        # Skip the header
        next(reader)

        # Read the data
        for row in reader:
            name, _ = tuple(row[0].split(sep="  ", maxsplit=1))
            surname, first_name, middle_name = split_name(name)

            personal_number = row[7][:6]
            student_data = {
                "surname": surname,
                "first_name": first_name,
                "middle_name": middle_name,
                "birthdate": birthdate_from_number(personal_number),
                "gender": gender_from_number(personal_number),
            }
            if student_data["birthdate"]:
                students_data.append(student_data)

    # Fill out esoteric stuff
    for student in students_data:
        student["angelic_number"] = angelic_number(student["birthdate"])
        student["guardian_angel"] = GUARDIAN_ANGELS[student["angelic_number"]]["name"]
        student["guardian_angel_description"] = GUARDIAN_ANGELS[
            student["angelic_number"]
        ]["description"]
        student["zodiac"] = zodiac(student["birthdate"])
        student["spiritual_stone"] = spiritual_stone(student["zodiac"])
        student["chinese_zodiac"] = chinese_zodiac(student["birthdate"])
        student["celtic_zodiac"] = celtic_zodiac(student["birthdate"])

    # Export data
    with open("valentyn_troll.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, delimiter="|")
        writer.writeheader()
        writer.writerows(data_for_export(students_data))

    return students_data


def find_random_connection(student, students_data: list) -> tuple:
    """Find a random connection between the students."""
    connection = choice(list(Signs))
    connected_students = [
        stud
        for stud in students_data
        if stud["surname"] != student["surname"]
        and stud["gender"] != student["gender"]
        and stud[connection.value] == student[connection.value]
    ]
    if not connected_students:
        return None, None
    return choice(connected_students), connection


def full_name(student: dict) -> str:
    """Return the full name of the student."""
    return (
        " ".join(
            [
                student["surname"],
                student["first_name"],
                student["middle_name"],
            ]
        )
        if student["middle_name"]
        else " ".join([student["surname"], student["first_name"]])
    )


def create_pairs(students_data: list) -> None:
    """Create pairs of students based on their esoteric data."""
    from_dict = defaultdict(int)
    pairs = []
    failed_students = []

    for student in students_data:
        connected_stud, connection = find_random_connection(student, students_data)
        if not connected_stud:
            failed_students.append(full_name(student))
            continue

        tries = 0
        while from_dict[full_name(student)] >= 2 and tries < MAX_TRIES:
            connected_stud, connection = find_random_connection(student, students_data)
            tries += 1

        if tries == MAX_TRIES:
            failed_students.append(full_name(student))
        else:
            from_dict[full_name(student)] += 1
            pairs.append(
                (full_name(student), full_name(connected_stud), connection.value)
            )

    print(failed_students)
    with open("valentyn_pary.csv", "w+", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow(["Od", "Komu", "Spojení"])
        writer.writerows(pairs)


def prepare_tokens() -> list[str]:
    client = OpenAI(api_key=OPENAI_API_KEY)


students_data = create_data()
create_pairs(students_data)
