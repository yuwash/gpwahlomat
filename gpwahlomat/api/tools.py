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
    response = cursor.fetchall()
    content = response[0]
    static = {
        'thema': content[0],
        'welcome': content[1],
        'welcometxt': content[2],
        'accenttitle': content[3],
        'resultArticle': content[4],
        'favoriteArticle': content[5],
        'neutralWarning': content[6]
    }
    alles['content_'] = static


    cursor.execute('''SELECT id, data FROM kategorie ''')
    kategories = cursor.fetchall()
    k_list = []

    for kategorie in kategories:
        k_dict = {}
        k_dict[kategorie[0]] = {
            'id': kategorie[0],
            'name': kategorie[1]
        }

        k_list.append(k_dict[kategorie[0]])

    alles['categories'] = k_list

    cursor.execute('''SELECT id, data FROM partei ''')
    parties = cursor.fetchall()
    p_list = []

    for partie in parties:
        p_dict = {}
        p_dict[partie[0]] = {
            'id': partie[0],
            'name': partie[1]
        }

        p_list.append(p_dict[partie[0]])

    alles['parties'] = p_list

    alles['questions'] = get_questions()
    return alles


def get_questions():
    q_list = []

    cursor.execute(
        "SELECT frage.id, frage.kategorie_id, frage.data FROM frage")
    questions = cursor.fetchall()


    for question in questions:
        q_dict = {}

        # save question in q_dict
        q_dict[question[0]] = {
            'cat_id': question[1],
            'text' : question[2],
            'positions': []
        }

        # add positions to question
        cursor.execute(
                "SELECT antwort.data, antwort.partei_id, antwort.wahl FROM antwort WHERE antwort.frage_id = %s",[question[0]])
        positions = cursor.fetchall()
        for position in positions:
            q_dict[question[0]]['positions'].append({
                'orientation':position[1],
                'vote': position[2],
                'argumentation':position[0]})

        # save question to q_list
        q_list.append(q_dict)
    return q_list
