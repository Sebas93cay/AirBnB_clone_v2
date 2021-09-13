#!/usr/bin/python3
"""
This scripts starts a web application that shows the filters
from web-statics
"""

from flask import Flask
from flask.templating import render_template

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exeption):
    """Close database"""
    storage.close()


@app.route('/hbnb')
def hbnb():
    """show hbnb web page"""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    states = storage.all(State).values()
    amenities = storage.all(Amenity)
    places = storage.all(Place).values()
    users = storage.all(User)
    place_users = []
    place_amenities = []
    place_reviews = []
    for place in places:
        place_users.append(users['User.'+place.user_id])
        place_amenities.append([])
        for amenity in place.amenities:
            place_amenities[-1].append(amenity)
        place_reviews.append([])
        for review in place.reviews:
            review.user = users['User.'+review.user_id]
            place_reviews[-1].append(review)

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities.values(),
                           places=zip(places,
                                      place_users,
                                      place_amenities,
                                      place_reviews),
                           months=months)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
