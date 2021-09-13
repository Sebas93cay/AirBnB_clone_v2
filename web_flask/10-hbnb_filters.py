#!/usr/bin/python3
"""
This scripts starts a web application that shows the filters
from web-statics
"""

from flask import Flask, g, abort
from flask.templating import render_template

from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exeption):
    storage.close()
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    print('las amenities: ', amenities)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
