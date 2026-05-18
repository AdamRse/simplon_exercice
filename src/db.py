import os

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection


def get_connection() -> MySQLConnection:
    """Crée et retourne une connexion MySQL à partir des variables d'environnement."""
    try:
        connection = mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            port=int(os.environ.get("MYSQL_PORT", 3306)),
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"],
        )
        print(f"✅ Connecté à MySQL sur {os.environ['MYSQL_HOST']}")
        return connection  # type: ignore[return-value]
    except Error as e:
        raise RuntimeError(f"❌ Erreur de connexion MySQL : {e}") from e
