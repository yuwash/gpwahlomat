#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: tools.py
'''
A collection of tools used in other modules
'''
from db.db_client import database_connection


db = database_connection()
cursor = db.cursor()


def flatten(_list):
    return [item for sublist in _list for item in sublist]


def get_everything():
    alles = {}
    cursor.execute('''SELECT * FROM statisch ''')
    alles['tenor'] = cursor.fetchall()
    cursor.execute('''SELECT data FROM kategorie ''')
    alles['categories'] = flatten(cursor.fetchall())
    cursor.execute('''SELECT data FROM partei ''')
    alles['parties'] = flatten(cursor.fetchall())
    cursor.execute(
        '''SELECT frage.id, frage.data, frage.kategorie_id,
            antwort.data, antwort.wahl FROM frage, antwort''')
    alles['questions'] = flatten(cursor.fetchall())
    print(alles)
    return alles
