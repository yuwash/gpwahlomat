#!venv/bin/python

from db.db_client import database_connection


db = database_connection()
cursor = db.cursor()


def get_everything():
    alles = {}
    cursor.execute('''SELECT * FROM statisch ''')
    alles['tenor'] = cursor.fetchall()
    cursor.execute('''SELECT * FROM kategorie ''')
    alles['categories'] = cursor.fetchall()
    cursor.execute('''SELECT * FROM partei ''')
    alles['parties'] = cursor.fetchall()
    cursor.execute('''SELECT * FROM antwort ''')
    alles['questions'] = cursor.fetchall()
    return alles
