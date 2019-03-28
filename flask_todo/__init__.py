# importing request, make_response, and render_template from flask.
from flask import Flask, request, make_response, render_template

import psycopg2

from . import db

# Defining create_app with test_config equal to none.
def create_app(test_config=None):
# Creating an object from the Flask class.
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods=['GET', 'POST', 'PUT'])
    def index():
        Homework = {'name': 'Homework', 'complete': False, 'date_set': '5/21/05'}
        Wash_Dishes = {'name': 'Wash Dishes', 'complete': False, 'date_set': '9/21/09'}
        Laundry = {'name': 'Laundry', 'complete': False, 'date_set': '1/13/15'}
        items = [Homework, Wash_Dishes, Laundry]
        return render_template('index.html', items=items)

    @app.route("/create", methods=['GET', 'POST'])
    def create_todo():
        return render_template('create_todo.html')

    @app.route("/update", methods=['GET', 'PUT'])
    def update_todo():
        return render_template('update_todo.html')

    return app
