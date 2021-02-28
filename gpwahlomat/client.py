#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: run.py
'''
Main file that gets run and handles the routing to index and api calls
'''
from flask import Flask, render_template, jsonify
from api.tools import get_everything, FileQuestionsData

# TODO remove static_url_path
app = Flask(__name__, template_folder='static/', static_url_path='')

DATA_FILE_PATH = "data.json"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/alles', methods=['GET'])
def alles():
    with open(DATA_FILE_PATH) as data_file:
        questions_data = FileQuestionsData(data_file)
    return jsonify(get_everything(questions_data))


if __name__ == '__main__':
    app.run(debug=True)
