import docx2txt
from unidecode import unidecode as ud

doc = docx2txt.process('seznam_ucitelu.docx')
names = doc.split('\n')

written_names = set()
with open('teachers.csv', 'w+', encoding='utf-8') as file:
    for name in names:
        if len(name) > 6:
            name_list = name.split(' ')
            if len(name_list) == 2:
                surname, name = tuple(name_list)
                email = f"{ud(name).lower()}.{ud(surname).lower()}@gevo.cz"
                if email not in written_names:
                    file.write(f"{name} {surname},{email}\n")
                    written_names.add(email)
            if len(name_list) == 3:
                surname, name1, name2 = tuple(name_list)
                email = f"{ud(name1).lower()}.{ud(surname).lower()}@gevo.cz"
                if email not in written_names:
                    file.write(f"{name1} {name2} {surname},{email}\n")
                    written_names.add(email)

