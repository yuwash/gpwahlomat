#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: db_create.py
'''
Script to create and set up the database
'''
import configparser
from psycopg2 import connect, ProgrammingError
import json


config = configparser.ConfigParser()
config.readfp(open('config.cfg'))
dbname = config.get('db', 'name')
user = config.get('db', 'user')
host = config.get('db', 'host')
password = config.get('db', 'password')

# create wahlomat db (deletes if already existed and creates anew)
con = connect(
    dbname='postgres', user=user, host=host, password=password)
con.autocommit = True
cur = con.cursor()
try:
    cur.execute('DROP DATABASE ' + dbname)
except ProgrammingError:
    pass
cur.execute('CREATE DATABASE ' + dbname)
cur.close()

# connect to wahlomat db and create the necessary tables
con = connect(
    dbname=dbname, user=user, host=host, password=password)
cur = con.cursor()


def create_schema():
    cur.execute(
        '''CREATE TABLE kategorie(
            id SERIAL PRIMARY KEY,
            data VARCHAR UNIQUE
        )'''
    )
    cur.execute(
        '''CREATE TABLE partei(
            id SERIAL PRIMARY KEY,
            data VARCHAR
        )'''
    )
    cur.execute(
        '''CREATE TABLE frage(
            id SERIAL PRIMARY KEY,
            data VARCHAR,
            kategorie_id INTEGER REFERENCES kategorie(id)
        )'''
    )
    cur.execute(
        '''CREATE TABLE antwort(
            id SERIAL PRIMARY KEY,
            data VARCHAR,
            wahl INTEGER,
            frage_id INTEGER REFERENCES frage(id),
            partei_id INTEGER REFERENCES partei(id)
        )'''
    )
    cur.execute(
        '''CREATE TABLE auswahl(
            id SERIAL PRIMARY KEY,
            wahl INTEGER,
            frage_id INTEGER REFERENCES frage(id)
        )'''
    )
    cur.execute(
        '''CREATE TABLE statisch(
            titel VARCHAR,
            impressum VARCHAR
        )'''
    )
    cur.execute(
        '''CREATE TABLE benutzer(
            id SERIAL PRIMARY KEY,
            username VARCHAR UNIQUE,
            email VARCHAR UNIQUE,
            pwdhash VARCHAR,
            ctime TIMESTAMP default current_timestamp
        )'''
    )
    con.commit()


def fill_data(json_file):
    with open(json_file) as data_file:
        questions = json.load(data_file)
        for question in questions:
            for q_text in question:
                cur.execute(
                    '''SELECT id FROM kategorie
                        WHERE data = (%s)
                    ''', (question[q_text]['kategorie'], )
                )
                cat = cur.fetchone()
                if not cat:
                    cur.execute(
                        '''INSERT INTO kategorie (data)
                            VALUES (%s) RETURNING id
                        ''', (question[q_text]['kategorie'], )
                    )
                    cat = cur.fetchone()
                cat_id = cat[0]
                cur.execute(
                    '''INSERT INTO frage (data, kategorie_id)
                        VALUES (%s, %s) RETURNING id
                    ''', (q_text, cat_id, )
                )
                q_id = cur.fetchone()[0]
                for partei in question[q_text]['parteien']:
                    cur.execute(
                        '''SELECT id FROM partei
                            WHERE data = (%s)
                        ''', (partei['name'], ))
                    party = cur.fetchone()
                    if not party:
                        cur.execute(
                            '''INSERT INTO partei (data)
                                VALUES (%s) RETURNING id
                            ''', (partei['name'], )
                        )
                        party = cur.fetchone()
                    party_id = party[0]
                    cur.execute(
                        '''INSERT INTO antwort (data, wahl, frage_id, partei_id)
                            VALUES (%s, %s, %s, %s)
                        ''', (partei['antwort'],
                        partei['wahl'], q_id, party_id, ))


create_schema()
fill_data('data.json')
cur.close()

