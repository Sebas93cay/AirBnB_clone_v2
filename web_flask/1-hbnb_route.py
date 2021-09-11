#!/usr/bin/python3
"""This script starts a simple server"""

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


if __name__ == "__main__":
    app.run(debug=True)
