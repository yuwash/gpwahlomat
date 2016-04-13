import hug
from passlib.apps import custom_app_context as pwd_context

from gpwahlomat.db.db_client import database_connection


db = database_connection()
cursor = db.cursor()


@hug.put('/benutzer')
def benutzer(
        username: hug.types.text, email: hug.types.text,
        password: hug.types.text):
    pwdhash = pwd_context.encrypt(password)
    cursor.execute(
        '''INSERT INTO benutzer (username, email, pwdhash) VALUES (%s, %s, %s)''', (
            username, email, pwdhash))


@hug.delete('/benutzer')
def benutzer(id: hug.types.number):
    cursor.execute(
        '''SELECT * FROM benutzer WHERE id = (%s)''', (id, ))
    return cursor.fetchone()


@hug.get('/alle_benutzer')
def alle_benutzer():
    cursor.execute('''SELECT * FROM benutzer ''')
    return cursor.fetchall()
