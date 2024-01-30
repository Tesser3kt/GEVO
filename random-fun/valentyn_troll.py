import csv

COLUMNS = [
    "Příjmení",
    "Jméno",
    "Datum narození",
    "Andělské číslo",
    "Anděl strážný",
    "Popis anděla strážného",
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
        students_data.append(student_data)

# Fill out esoteric stuff
for student in students_data:
    student["angelic_number"] = angelic_number(student["birthdate"])
    student["guardian_angel"] = GUARDIAN_ANGELS[student["angelic_number"]]["name"]
    student["guardian_angel_description"] = GUARDIAN_ANGELS[student["angelic_number"]][
        "description"
    ]
    student["chinese_zodiac"] = chinese_zodiac(student["birthdate"])
