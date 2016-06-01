#!venv/bin/python

from flask import Flask, jsonify, request, render_template
from db.db_client import database_connection


app = Flask(__name__, template_folder='oberflaeche_int/public')
db = database_connection()
cursor = db.cursor()


class GenericAPIHandler(object):
    def __init__(self):
        super(GenericAPIHandler).__init__()
        if not request.form:
            return render_template('index2.html')
        self.path = request.path
        self.json = request.form
        self.id = self.json.get('id', None)

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
        if self.id:
            cursor.execute(
                '''SELECT * FROM {table} WHERE id = (%s)'''.format(
                    table=self.path, id=self.id))
            return jsonify(cursor.fetchone())
        else:
            cursor.execute('''SELECT * FROM {table} '''.format(
                table=self.path))
            return jsonify(cursor.fetchall())

    def delete(self):
        if self.id:
            cursor.execute(
                ''' DELETE * FROM {table}
                    WHERE id = ({id})'''.format(
                    table=self.path, id=self.id))
            return 'OK'
