#!/usr/bin/python3
"""doc"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    new_text = text.replace('_', ' ')
    return f"C {escape(new_text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
