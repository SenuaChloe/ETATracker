#!/bin/python3

import googlemaps
from datetime import datetime
import tools

# Arguments must be strings
def tracking_request(string_from, string_to, DEBUG_MODE=False):
    gmaps = googlemaps.Client(key='API-ID-googlemaps')

    tools.dprint("from:"+string_from+" to:"+string_to, DEBUG_MODE)

    # Putting them into the calculator
    now = datetime.now()
    directions_result = gmaps.directions(string_from, string_to, mode="driving", departure_time=now)

    # dump
    tools.dump(directions_result, DEBUG_MODE)

    duration = directions_result[0]["legs"][0]["duration_in_traffic"]["text"]
    eta = directions_result[0]["legs"][0]["duration_in_traffic"]["value"]

    # debug trace
    tools.dprint(eta, DEBUG_MODE)

    # Outputting the result
    return (duration, eta)
