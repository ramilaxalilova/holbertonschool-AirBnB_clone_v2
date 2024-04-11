#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """lists states from database"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
