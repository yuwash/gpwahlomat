#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: generic_api_handler.py
'''
An API handler that handles with the common REST functions.
# get
# put
# post
# delete
This is instanciated every time a request to one of the api routes is made.
'''
from flask import jsonify, request, render_template

from db.db_client import database_connection


db = database_connection()
cursor = db.cursor()


class GenericAPIHandler(object):
    def __init__(self):
        super(GenericAPIHandler).__init__()
        if not request.form:
            return render_template('index.html')
        self.path = request.path[1:]
        self.json = request.form
        self.id = self.json.get('id', None)
        self.data = self.json.get('data', None)

    def get(self):
        if self.id:
            cursor.execute(
                '''SELECT * FROM {table} WHERE id = ({id})'''.format(
                    table=self.path, id=self.id))
            return jsonify(cursor.fetchone())
        else:
            cursor.execute('''SELECT * FROM {table} '''.format(
                table=self.path))
            return jsonify(cursor.fetchall())

    def put(self):
        if self.id:
            cols = self.json.keys()
            vals = [self.json[x] for x in cols]
            vals_str_list = ["%s"] * len(vals)
            vals_str = ", ".join(vals_str_list)
            cursor.execute(
                ''' UPDATE {table} ({cols})
                    WHERE id = ({id})
                    VALUES ({vals_str})'''.format(
                    table=self.path, cols=cols, id=self.id,
                    vals_str=vals_str), vals)
            return 'OK'

    def post(self):
        cols = self.json.keys()
        cols_str = ", ".join([i for i in self.json.keys()])
        vals = [self.json[x] for x in cols]
        vals_str_list = ','.join(["%s"] * len(vals))
        insert_query = (
            ''' INSERT INTO {table} ({cols})
                VALUES ({vals_str})'''.format(
                table=self.path, cols=cols_str, vals_str=vals_str_list))
        cursor.execute(insert_query, tuple(vals))
        return 'OK'

    def delete(self):
        if self.id:
            cursor.execute(
                ''' DELETE * FROM {table}
                    WHERE id = ({id})'''.format(
                    table=self.path, id=self.id))
            return 'OK'
