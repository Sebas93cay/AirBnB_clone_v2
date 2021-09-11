#!/usr/bin/python3
"""
This scripts tarts a Flask web application that shows a list of states
"""

from flask import Flask, g
from flask.templating import render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exeption):
    storage.close()
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
