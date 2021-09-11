#!/usr/bin/python3
"""This script starts a simple server"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Hello World"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>')
def cRoute(text):
    """Route for c"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(debug=True)
