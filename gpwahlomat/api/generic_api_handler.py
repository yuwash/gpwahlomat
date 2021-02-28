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
from flask import jsonify, request


class FileAPIData(object):
    def __init__(self, data_file):
        import json

        self.jsonData = json.load(data_file)

    # TODO-ish: implement those methods from DBAPIData;
    #  Might not be necessary anyway


class DBAPIData(object):
    def __init__(self):
        from db.db_client import database_connection

        db = database_connection()
        self.cursor = db.cursor()

    def get_item(self, path, item_id):
        self.cursor.execute(
            '''SELECT * FROM {table} WHERE id = ({id})'''.format(
                table=path, id=item_id))
        return self.cursor.fetchone()

    def get_all(self, path):
        self.cursor.execute('''SELECT * FROM {table} '''.format(
            table=path))
        return self.cursor.fetchall()

    def update_item(self, path, item_id, cols, vals):
        vals_str_list = ["%s"] * len(vals)
        vals_str = ", ".join(vals_str_list)
        return self.cursor.execute(
            ''' UPDATE {table} ({cols})
                WHERE id = ({id})
                VALUES ({vals_str})'''.format(
                table=path, cols=cols, id=item_id,
                vals_str=vals_str), vals)

    def create_item(self, path, cols, vals):
        cols_str = ", ".join([i for i in self.json.keys()])
        vals_str_list = ','.join(["%s"] * len(vals))
        insert_query = (
            ''' INSERT INTO {table} ({cols})
                VALUES ({vals_str})'''.format(
                table=path, cols=cols_str, vals_str=vals_str_list))
        return self.cursor.execute(insert_query, tuple(vals))

    def delete_item(self, path, item_id):
        return self.cursor.execute(
            ''' DELETE * FROM {table}
                WHERE id = ({id})'''.format(
                table=path, id=item_id))


class GenericAPIHandler(object):
    def __init__(self, api_data):
        super(GenericAPIHandler).__init__()
        self.api_data = api_data
        self.path = request.path[1:]
        self.json = request.form
        self.id = self.json.get('id', None)
        self.data = self.json.get('data', None)

    def get(self):
        if self.id:
            item = self.api_data.get_item(self.path, self.id)
            return jsonify(item)
        else:
            all_ = self.api_data.get_all(self.path)
            return jsonify(all_)

    def put(self):
        if self.id:
            cols = self.json.keys()
            vals = [self.json[x] for x in cols]
            self.api_data.update_item(
                self.path,
                self.id,
                cols=cols,
                vals=vals,
            )
            return 'OK'

    def post(self):
        cols = self.json.keys()
        vals = [self.json[x] for x in cols]
        self.api_data.create_item(
            self.path,
            cols=cols,
            vals=vals,
        )
        return 'OK'

    def delete(self):
        if self.id:
            self.api_data.delete_item(self.path, self.id)
            return 'OK'
