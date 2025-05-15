from dataclasses import dataclass

import mysql.connector


# Vytvořte dataclass 'Product', která odpovídá informací v tabulce 'products'.
@dataclass
class Product: ...


def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost", user="root", password="macSucks"
    )
    return connection


def add_product(product):
    cursor = conn.cursor()
    cursor.execute("use automat")

    # Níže doplňte (dovnitř závorek) SQL příkaz, který do tabulky 'products'
    # přidá produkt 'product'. Do sloupce 'id' nic nevpisujete, ten si databáze
    # řeší sama.

    cursor.execute()

    conn.commit()


def print_products():
    cursor = conn.cursor()
    cursor.execute("use automat")

    cursor.execute("select code, name, price, quantity from products")
    for code, name, price, quantity in cursor:
        print(f"{code}: {name} -- {price} Kč ({quantity} ks)")


def buy_product_by_code(code):
    cursor = conn.cursor()
    cursor.execute("use automat")

    cursor.execute(f"select quantity from products where code='{code}'")
    (quantity,) = list(cursor)[0]

    # Do závorek níže doplňte SQL příkaz, který sníží množství ('quantity')
    # produktu s kódem 'code' o 1.

    cursor.execute()

    conn.commit()


def print_menu():
    print("1. Seznam produktů.")
    print("2. Koupit produkt.")
    print("3. Přidat produkt.")
    print("4. Ukončit.")


def run():
    running = True
    while running:
        print_menu()
        choice = input("Zadejte volbu (1 až 4): ")
        if choice == "1":
            print("-------------------------")
            print_products()
            print("-------------------------")
        if choice == "2":
            ...
            # Zeptejte se uživatele na kód produktu, který chce zakoupit, a pak
            # produkt s tímto kódem kupte přes funkci 'buy_product_by_code'.
        if choice == "3":
            code = input("Kód produktu: ")
            name = input("Název produktu: ")
            price = input("Cena produktu: ")
            quantity = input("Množství: ")
            new_product = Product(
                code=code, name=name, price=float(price), quantity=int(quantity)
            )
            add_product(new_product)
        if choice == "4":
            running = False


conn = connect_to_db()

run()

conn.close()
