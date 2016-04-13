import hug

from gpwahlomat.db.db_client import database_connection


db = database_connection()
cursor = db.cursor()


@hug.get('/kategorie')
def kategorie(id: hug.types.number):
    cursor.execute(
        '''SELECT * FROM kategorie WHERE id = (%s)''', (id, ))
    return cursor.fetchone()


@hug.put('/kategorie')
def kategorie(data: hug.types.text):
    cursor.execute(
        '''INSERT INTO kategorie (data) VALUES (%s)''', (data, ))


@hug.get('/kategorien')
def kategorien():
    cursor.execute('''SELECT * FROM kategorie ''')
    return cursor.fetchall()


@hug.get('/partei')
def partei(id: hug.types.number):
    cursor.execute(
        '''SELECT * FROM partei WHERE id = (%s)''', (id, ))
    return cursor.fetchone()


@hug.put('/partei')
def partei(data: hug.types.text):
    cursor.execute(
        '''INSERT INTO partei (data) VALUES (%s)''', (data, ))


@hug.get('/parteien')
def parteien():
    cursor.execute('''SELECT * FROM partei ''')
    return cursor.fetchall()


@hug.get('/antwort')
def antwort(id: hug.types.number):
    cursor.execute(
        '''SELECT * FROM antwort WHERE id = (%s)''', (id, ))
    return res.fetchone()


@hug.put('/antwort')
def antwort(
        data: hug.types.text, frage_id: hug.types.number,
        partei_id: hug.types.number):
    cursor.execute(
        '''INSERT INTO antwort (data, frage_id, partei_id) VALUES (%s, %s, %s)
        ''', (data, frage_id, partei_id, ))


@hug.get('/antworten')
def antworten():
    cursor.execute('''SELECT * FROM antwort ''')
    return cursor.fetchall()


@hug.get('/frage')
def frage(id: hug.types.number):
    cursor.execute('''SELECT * FROM frage WHERE id = (%s)''', (id, ))
    return cursor.fetchone()


@hug.put('/frage')
def frage(data: hug.types.text, kategorie_id: hug.types.number):
    cursor.execute(
        '''INSERT INTO frage (data, kategorie_id) VALUES (%s, %d)''', (
            data, kategorie_id, ))


@hug.get('/fragen')
def fragen():
    cursor.execute('''SELECT * FROM frage ''')
    return cursor.fetchall()


@hug.get('/auswahl')
def auswahl(id: hug.types.number):
    cursor.execute('''SELECT * FROM auswahl WHERE id = (%s)''', (id, ))
    return cursor.fetchone()


@hug.put('/auswahl')
def auswahl(data: hug.types.text, kategorie_id: hug.types.number):
    cursor.execute(
        '''INSERT INTO auswahl (data, kategorie_id) VALUES (%s, %d)
        ''', (data, kategorie_id, ))


@hug.get('/auswahlen')
def auswahlen():
    cursor.execute('''SELECT * FROM auswahl ''')
    return cursor.fetchall()
