#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
script to create and set up the database
'''

import configparser
from psycopg2 import connect


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
cur.execute('DROP DATABASE ' + dbname)
cur.execute('CREATE DATABASE ' + dbname)
cur.close()

# connect to wahlomat db and create the necessary tables
con = connect(
    dbname=dbname, user=user, host=host, password=password)
cur = con.cursor()
cur.execute(
    '''CREATE TABLE kategorie(
        id SERIAL PRIMARY KEY,
        data VARCHAR
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
con.commit()
cur.close()
