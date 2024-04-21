#!/usr/bin/python3
"""doc"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def data():
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
