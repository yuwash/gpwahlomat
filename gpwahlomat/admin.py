#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: admin.py
'''
Main file that gets run and handles the routing to index and api calls
'''
from flask import Flask, request, render_template
from flask_login import login_required
from api.generic_api_handler import GenericAPIHandler, DBAPIData

# TODO remove static_url_path
app = Flask(__name__, template_folder='static/', static_url_path='')


def _create_api_handler():
    api_data = DBAPIData()
    return GenericAPIHandler(api_data)


@login_required
@app.route('/')
@app.route('/index')
def index():
    return render_template('admin.html')


@login_required
@app.route('/kategorie', methods=['GET', 'PUT', 'POST', 'DELETE'])
def kategorie():
    _handler = _create_api_handler()
    return _handler.__getattribute__(request.method.lower())()


@login_required
@app.route('/partei', methods=['GET', 'PUT', 'POST', 'DELETE'])
def partei():
    _handler = _create_api_handler()
    return _handler.__getattribute__(request.method.lower())()


@login_required
@app.route('/antwort', methods=['GET', 'PUT', 'POST', 'DELETE'])
def antwort():
    _handler = _create_api_handler()
    return _handler.__getattribute__(request.method.lower())()


@login_required
@app.route('/frage', methods=['GET', 'PUT', 'POST', 'DELETE'])
def frage():
    _handler = _create_api_handler()
    return _handler.__getattribute__(request.method.lower())()


@login_required
@app.route('/auswahl', methods=['GET', 'PUT', 'POST', 'DELETE'])
def auswahl():
    _handler = _create_api_handler()
    return _handler.__getattribute__(request.method.lower())()


if __name__ == '__main__':
    app.run(debug=True, port=5001)
