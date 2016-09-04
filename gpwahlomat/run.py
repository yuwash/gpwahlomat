#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: run.py
'''
Main file that gets run and handles the routing to index and api calls
'''
from flask import Flask, request, render_template, jsonify

from api.generic_api_handler import GenericAPIHandler
from api.tools import get_everything


app = Flask(__name__, template_folder='static/')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/kategorie', methods=['GET', 'PUT', 'POST', 'DELETE'])
def kategorie():
    _handler = GenericAPIHandler()
    return _handler.__getattribute__(request.method.lower())()


@app.route('/partei', methods=['GET', 'PUT', 'POST', 'DELETE'])
def partei():
    _handler = GenericAPIHandler()
    return _handler.__getattribute__(request.method.lower())()


@app.route('/antwort', methods=['GET', 'PUT', 'POST', 'DELETE'])
def antwort():
    _handler = GenericAPIHandler()
    return _handler.__getattribute__(request.method.lower())()


@app.route('/frage', methods=['GET', 'PUT', 'POST', 'DELETE'])
def frage():
    _handler = GenericAPIHandler()
    return _handler.__getattribute__(request.method.lower())()


@app.route('/auswahl', methods=['GET', 'PUT', 'POST', 'DELETE'])
def auswahl():
    _handler = GenericAPIHandler()
    return _handler.__getattribute__(request.method.lower())()


@app.route('/alles', methods=['GET'])
def alles():
    print(get_everything())
    return jsonify(get_everything())

if __name__ == '__main__':
    app.run(debug=True)
