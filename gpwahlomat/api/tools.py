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
    alles['questions'] = get_questions()


def get_questions():
    cursor.execute(
        '''SELECT frage.id, frage.data, frage.kategorie_id,
            antwort.data, antwort.wahl FROM frage, antwort''')
    questions = cursor.fetchall()
    q_dict = {}
    q_list = []
    for question in questions:
        if question[1] in q_dict:
            q_dict[question[1]]['positions'].append({
                'orientation':question[4], 'argumentation': question[3]})
        else:
            q_dict[question[1]] = {
                'id': question[0],
                'cat_id': question[2],
                'positions': [
                    {'orientation': question[4], 'argumentation': question[3]}]
            }
    for key in q_dict:
        new_dict = q_dict[key]
        new_dict['text'] = key
        q_list.append(new_dict)
    return q_list

