from dotenv import load_dotenv

from db import get_connection

load_dotenv()

REQUETES = [
    ("a. Chiffre d'affaires total", "SELECT SUM(prix * qte) AS ca_total FROM ventes;"),
    (
        "b. Ventes par produit",
        "SELECT produit, SUM(prix * qte) AS ca FROM ventes GROUP BY produit;",
    ),
    (
        "c. Ventes par région",
        "SELECT region, SUM(prix * qte) AS ca FROM ventes GROUP BY region;",
    ),
]


def run():
    connection = get_connection()
    cursor = connection.cursor()

    for question, sql in REQUETES:
        print(f"\n{question}")
        cursor.execute(sql)
        for ligne in cursor.fetchall():
            print(" ", " | ".join(str(v) for v in ligne))

    cursor.close()
    connection.close()


if __name__ == "__main__":
    run()
