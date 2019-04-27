#!/bin/python3

import googlemaps
from datetime import datetime
import tools

# Arguments must be strings
def tracking_request(string_from, string_to, DEBUG_MODE=False):
    gmaps = googlemaps.Client(key='AIzaSyDUxIxbbDx9ZMv9SzuVYfenr12APcJ9xg4')

    # Getting the coordinates
    #geocode_from = gmaps.geocode(string_from)
    #geocode_to = gmaps.geocode(string_to)

    # Putting them into the calculator
    now = datetime.now()
    #directions_result = gmaps.directions(geocode_from, geocode_to, mode="transit", departure_time=now)
    directions_result = gmaps.directions(string_from, string_to)

    # debug trace
    tools.dprint(directions_result, DEBUG_MODE);

    # Outputting the result
    return
