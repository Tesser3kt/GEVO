import sqlite3
import hashlib
import re

from nastaveni import VYCHOZI_PRODUKTY


class SpravceDatabaze:
    """ Trida spravce databaze. Obsahuje metody pro vyber dat z databaze a
    jejich zapis. """

    def __init__(self, databaze_cesta):
        """ Konstruktor tridy SpravceDatabaze. """
        self.databaze_cesta = databaze_cesta
        self.kurzor = None
        self.pripojeni = None

    def __vytvor_tabulku_uzivatelu(self):
        """ Vytvori tabulku uzivatelu v databazi, pokud neexistuje. """
        try:
            # self.kurzor.execute("DROP TABLE uzivatele;")
            self.kurzor.execute(
                """CREATE TABLE IF NOT EXISTS uzivatele (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    jmeno TEXT NOT NULL,
                    heslo TEXT NOT NULL
                );"""
            )
            return None
        except sqlite3.Error as chyba:
            return chyba

    def __vytvor_tabulku_produktu(self):
        """
        Vytvori tabulku produktu v podle vychozich produktu v nastaveni.
        """
        try:
            self.kurzor.execute("DROP TABLE produkty;")
            self.kurzor.execute(
                """CREATE TABLE IF NOT EXISTS produkty (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nazev TEXT NOT NULL,
                    cena REAL NOT NULL,
                    popis TEXT NOT NULL,
                    na_sklade INTEGER NOT NULL
                );"""
            )
            for produkt in VYCHOZI_PRODUKTY:
                self.kurzor.execute(
                    ("INSERT INTO produkty (nazev, cena, popis, na_sklade) "
                     "VALUES (?, ?, ?, ?)"),
                    (produkt['nazev'], produkt['cena'],
                     produkt['popis'], produkt['na_sklade'])
                )
            self.pripojeni.commit()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def __vytvor_tabulku_kosiku(self):
        """ Vytvori tabulku kosiku v databazi, pokud neexistuje. """
        try:
            # self.kurzor.execute("DROP TABLE kosik;")
            self.kurzor.execute(
                """CREATE TABLE IF NOT EXISTS kosik (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uzivatel_id INTEGER NOT NULL,
                    produkt_id INTEGER NOT NULL,
                    pocet_kusu INTEGER NOT NULL,
                    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele (id),
                    FOREIGN KEY (produkt_id) REFERENCES produkty (id)
                );"""
            )
            return None
        except sqlite3.Error as chyba:
            return chyba

    def __prijatelne_jmeno(self, jmeno):
        """ Metoda pro overeni spravneho jmena uzivatele pri prihlaseni a
        registraci. """

        # jmeno musi mit nejmene 3 znaky
        if len(jmeno) < 3:
            return False

        # jmeno musi obsahovat pouze pismena a cislice
        if not re.match(r"^[a-zA-Z0-9]*$", jmeno):
            return False

        return True

    def __prijatelne_heslo(self, heslo):
        """ Metoda pro overeni spravneho hesla uzivatele pri prihlaseni a
        registraci. """

        # heslo musi mit nejmene 6 znaku
        if len(heslo) < 6:
            return False

        # heslo musi obsahovat nejmene jedno male pismeno, jedno velke pismeno
        # a jedno cislo
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$", heslo):
            return False

        return True

    def __najdi_uzivatele(self, jmeno):
        """ Metoda pro vyhledani uzivatele v databazi. """
        try:
            self.kurzor.execute(
                """SELECT * FROM uzivatele WHERE jmeno = ?;""", (jmeno,)
            )
            uzivatel = self.kurzor.fetchone()
            return uzivatel
        except sqlite3.Error:
            return None

    def __vloz_uzivatele(self, jmeno, heslo):
        """ Metoda pro vlozeni uzivatele do databaze. """
        try:
            heslo = hashlib.sha256(heslo.encode()).hexdigest()
            self.kurzor.execute(
                """INSERT INTO uzivatele (jmeno, heslo) VALUES (?, ?);""",
                (jmeno, heslo)
            )
            self.pripojeni.commit()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def pripoj_databazi(self):
        """ Metoda pro pripojeni k databazi. """
        try:
            self.pripojeni = sqlite3.connect(self.databaze_cesta)
            self.kurzor = self.pripojeni.cursor()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def inicializuj_databazi(self):
        """ Inicializuje tabulky v databazi, pokud neexistuji. """
        # vytvor tabulku uzivatelu
        chyba = self.__vytvor_tabulku_uzivatelu()
        if chyba:
            return chyba

        # vytvor tabulku produktu
        # chyba = self.__vytvor_tabulku_produktu()
        # if chyba:
        #     return chyba

        # vytvor tabulku kosiku
        chyba = self.__vytvor_tabulku_kosiku()
        if chyba:
            return chyba

        return None

    def zavri_databazi(self):
        """ Metoda pro zavreni databaze. """
        self.pripojeni.close()

    def odeber_uzivatele(self, jmeno):
        """ Metoda pro odebrani uzivatele z databaze. """
        if not self.__najdi_uzivatele(jmeno):
            return Exception(f"Uživatel {jmeno} neexistuje!")

        try:
            self.kurzor.execute(
                """DELETE FROM uzivatele WHERE jmeno = ?;""", (jmeno,)
            )
            self.pripojeni.commit()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def registruj_uzivatele(self, jmeno, heslo):
        """ Metoda pro vlozeni noveho uzivatele do databaze. """
        # overeni spravnosti jmena uzivatele
        if not self.__prijatelne_jmeno(jmeno):
            zprava = ("Uživatelské jméno musí obsahovat pouze písmena a "
                      "číslice a musí mít nejméně 3 znaky!")
            return Exception(zprava)

        if not self.__prijatelne_heslo(heslo):
            zprava = ("Heslo musí obsahovat nejméně jedno malé písmeno, "
                      "jedno velké písmeno a jedno číslo!")
            return Exception(zprava)

        if self.__najdi_uzivatele(jmeno):
            zprava = "Uživatel již existuje!"
            return Exception(zprava)

        chyba = self.__vloz_uzivatele(jmeno, heslo)
        if chyba:
            return chyba

        return None

    def najdi_id_uzivatele(self, jmeno):
        """ Metoda pro vyhledani uzivatele v databazi. """
        try:
            self.kurzor.execute(
                """SELECT id FROM uzivatele WHERE jmeno = ?;""", (jmeno,)
            )
            uzivatel = self.kurzor.fetchone()
            return uzivatel[0]
        except sqlite3.Error:
            return None

    def prihlas_uzivatele(self, jmeno, heslo):
        """ Metoda pro prihlaseni uzivatele. """

        # overeni spravnosti jmena uzivatele
        if not self.__prijatelne_jmeno(jmeno):
            zprava = ("Uživatelské jméno musí obsahovat pouze písmena a "
                      "číslice a musí mít nejméně 3 znaky!")
            return Exception(zprava)

        if not (uzivatel := self.__najdi_uzivatele(jmeno)):
            zprava = "Uživatel neexistuje!"
            return Exception(zprava)

        heslo = hashlib.sha256(heslo.encode()).hexdigest()
        if heslo != uzivatel[2]:
            zprava = "Chybné heslo!"
            return Exception(zprava)

        return None

    def vsechny_produkty(self):
        """ Metoda pro ziskani vsech produktu z databaze. """
        try:
            self.kurzor.execute("""SELECT * FROM produkty;""")
            produkty = self.kurzor.fetchall()
            return produkty
        except sqlite3.Error:
            return None

    def uloz_produkty_do_databaze(self, produkty):
        """ Metoda pro ulozeni produktu do databaze. """
        try:
            self.kurzor.execute("DROP TABLE produkty;")
            self.kurzor.execute(
                """CREATE TABLE IF NOT EXISTS produkty (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nazev TEXT NOT NULL,
                    cena REAL NOT NULL,
                    popis TEXT NOT NULL,
                    na_sklade INTEGER NOT NULL
                );"""
            )
            for produkt in produkty:
                self.kurzor.execute(
                    """INSERT INTO produkty (nazev, cena, popis, na_sklade)
                    VALUES (?, ?, ?, ?);""",
                    (produkt[1], produkt[2], produkt[3], produkt[4])
                )
            self.pripojeni.commit()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def uloz_kosik_do_databaze(self, id_uzivatele, kosik):
        """ Metoda pro ulozeni kosiku do databaze. """
        try:
            # uloz vsechny polozky kosiku
            for polozka in kosik.values():
                if polozka['pocet'] == 0:
                    # smaz vsechny polozky kosiku s poctem 0
                    self.kurzor.execute(
                        """DELETE FROM kosik WHERE uzivatel_id = ? AND
                        produkt_id = ?;""",
                        (id_uzivatele, polozka['id'])
                    )
                    continue

                self.kurzor.execute(
                    """INSERT INTO kosik (uzivatel_id, produkt_id, pocet_kusu)
                    VALUES (?, ?, ?);""",
                    (id_uzivatele, polozka['id'], polozka['pocet'])
                )
            self.pripojeni.commit()
            return None
        except sqlite3.Error as chyba:
            return chyba

    def nacti_kosik_z_databaze(self, id_uzivatele):
        """ Metoda pro nacteni kosiku z databaze. """
        try:
            self.kurzor.execute(
                """SELECT * FROM kosik WHERE uzivatel_id = ?;""",
                (id_uzivatele,)
            )
            kosik = self.kurzor.fetchall()
            return kosik
        except sqlite3.Error:
            return None
