#!/usr/bin/python3
"""
This scripts tarts a Flask web application that shows a list of states
"""

from flask import Flask, g, abort
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


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def states(id=None):
    states = storage.all(State)
    if id is None:
        return render_template('9-states.html', title='States',
                               items=states.values())
    elif ('State.'+id in states.keys()):
        state = states['State.'+id]
        return render_template('9-states.html',
                               title='State: {}'.format(state.name),
                               items=state.cities)
    else:
        return render_template('9-states.html', title='Not found!',
                               items=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
