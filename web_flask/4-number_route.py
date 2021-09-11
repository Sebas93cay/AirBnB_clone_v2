#!/usr/bin/python3

from flask import Flask, abort

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def pythonRoute(text='is cool'):
    """route for python"""
    text = text.replace('_', ' ')
    print("super duper")
    return "Python {}".format(text)


@app.route('/number/<string:n>', strict_slashes=False)
def number(n):
    """route for n"""
    if n.isnumeric():
        return "n is a number"
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
