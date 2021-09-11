#!/usr/bin/python3

from flask import Flask, abort
from flask.templating import render_template

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
    return "Python {}".format(text)


@app.route('/number/<string:n>', strict_slashes=False)
def number(n):
    """route for n"""
    if n.isnumeric():
        return "n is a number"
    abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Route for number template"""
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
