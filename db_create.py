#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
script to create and set up the database
'''

from psycopg2 import connect
import ConfigParser


config = ConfigParser.ConfigParser()
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
        id integer PRIMARY KEY,
        data varchar
    )'''
)
cur.execute(
    '''CREATE TABLE partei(
        id integer PRIMARY KEY,
        data varchar
    )'''
)
cur.execute(
    '''CREATE TABLE frage(
        id integer PRIMARY KEY,
        data varchar,
        kategorie_id integer references kategorie(id)
    )'''
)
cur.execute(
    '''CREATE TABLE antwort(
        id integer PRIMARY KEY,
        data varchar,
        frage_id integer references frage(id),
        partei_id integer references partei(id)
    )'''
)
cur.execute(
    '''CREATE TABLE auswahl(
        id integer PRIMARY KEY,
        wahl integer,
        frage_id integer references frage(id)
    )'''
)
cur.execute(
    '''CREATE TABLE statisch(
        titel varchar,
        impressum varchar
    )'''
)
con.commit()
cur.close()
