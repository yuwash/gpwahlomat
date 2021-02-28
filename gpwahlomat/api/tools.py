#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: tools.py
'''
A collection of tools used in other modules
'''


class FileQuestionsData(object):
    def __init__(self, data_file):
        import json

        self.jsonData = json.load(data_file)

    # TODO-ish: implement those methods from DBQuestionsData;
    #  Might not be necessary anyway


class DBQuestionsData(object):
    def __init__(self):
        from db.db_client import database_connection

        db = database_connection()
        self.cursor = db.cursor()

    def get_response(self):
        self.cursor.execute('''SELECT * FROM statisch ''')
        return self.cursor.fetchall()

    def get_kategories(self):
        self.cursor.execute('''SELECT id, data FROM kategorie ''')
        return self.cursor.fetchall()

    def get_parties(self):
        self.cursor.execute('''SELECT id, data FROM partei ''')
        return self.cursor.fetchall()

    def get_questions(self):
        self.cursor.execute(
            "SELECT frage.id, frage.kategorie_id, frage.data FROM frage")
        return self.cursor.fetchall()

    def get_positions(self):
        self.cursor.execute(
                "SELECT antwort.data, antwort.partei_id, antwort.wahl FROM antwort WHERE antwort.frage_id = %s",[question[0]])
        return self.cursor.fetchall()


def flatten(_list):
    return [item for sublist in _list for item in sublist]


def get_everything(questions_data):
    alles = {}

    response = questions_data.get_response()
    content = response[0]
    static = {
        'thema': content[0],
        'welcome': content[1],
        'welcometxt': content[2],
        'accenttitle': content[3],
        'resultArticle': content[4],
        'favoriteArticle': content[5],
        'neutralWarning': content[6],
        'noteResultArticle': content[7]
    }
    alles['content_'] = static

    kategories = questions_data.get_kategories()
    k_list = []

    for kategorie in kategories:
        k_dict = {}
        k_dict[kategorie[0]] = {
            'id': kategorie[0],
            'name': kategorie[1]
        }

        k_list.append(k_dict[kategorie[0]])

    alles['categories'] = k_list

    parties = questions_data.get_parties()
    p_list = []

    for partie in parties:
        p_dict = {}
        p_dict[partie[0]] = {
            'id': partie[0],
            'name': partie[1]
        }

        p_list.append(p_dict[partie[0]])

    alles['parties'] = p_list

    alles['questions'] = get_questions(questions_data)
    return alles


def get_questions(questions_data):
    q_list = []

    questions = questions_data.get_questions(questions_data)

    for question in questions:
        q_dict = {}

        # save question in q_dict
        q_dict = {
            'cat_id': question[1],
            'text' : question[2],
            'positions': []
        }

        # add positions to question
        positions = questions_data.get_positions()
        for position in positions:
            q_dict['positions'].append({
                'orientation':position[1],
                'vote': position[2],
                'argumentation':position[0]})

        # save question to q_list
        q_list.append(q_dict)
    return q_list
