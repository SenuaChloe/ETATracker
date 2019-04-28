#!/bin/python3

import sys
import file_reader
import tracking_request
import tools
from datetime import datetime
from datetime import timedelta

# Checking script parameters
if len(sys.argv) != 3:
    print("usage:    "+sys.argv[0]+" input_file [1|0]")
    sys.exit()

if sys.argv[2] == "0":
    DEBUG_MODE=False
else:
    DEBUG_MODE=True

# read input file
input_filename = sys.argv[1]
coord_list = file_reader.read_file(input_filename, DEBUG_MODE) # List of triplets (string, string, string)

# Computing times
eta_list = [] # list of pairs (string, string)
for (comment, string_from, string_to) in coord_list:
    string_duration, sec_duration = tracking_request.tracking_request(string_from, string_to, DEBUG_MODE)
    # Calculation of real ETA
    delta = timedelta(seconds=sec_duration)
    eta = datetime.now()+delta
    string_eta = eta.time().isoformat().split(".")[0] # Removing microseconds
    # Adding info to result list
    eta_list.append( (comment, string_duration, string_eta) )


# Printing results
for (comment, duration, eta) in eta_list:
    print(comment+", "+duration+", "+eta)

