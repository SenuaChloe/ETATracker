#!/bin/python3

import googlemaps
from datetime import datetime
import tools

# Arguments must be strings
def tracking_request(string_from, string_to, DEBUG_MODE=False):
    gmaps = googlemaps.Client(key='AIzaSyDUxIxbbDx9ZMv9SzuVYfenr12APcJ9xg4')

    # Putting them into the calculator
    directions_result = gmaps.directions(string_from, string_to)

    eta = directions_result[0]["legs"][0]["duration"]["text"]

    # debug trace
    tools.dprint(eta, DEBUG_MODE)

    # Outputting the result
    return eta
