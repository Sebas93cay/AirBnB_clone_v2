#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Hello World"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def cRoute(text):
    """Route for c"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<string:text>', strict_slashes=False)
def pythonRoute(text):
    """route for python"""
    text = text.replace('_', ' ')
    print("super duper")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(debug=True)
