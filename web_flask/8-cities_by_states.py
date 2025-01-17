#!/usr/bin/python3
"""
This scripts tarts a Flask web application that shows a list of states
"""

from flask import Flask
from flask.templating import render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Close db"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
