#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: tools.py
'''
A collection of tools used in other modules
'''
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
    cursor.execute('''SELECT * FROM frage ''')
    alles['questions'] = cursor.fetchall()
    return alles
