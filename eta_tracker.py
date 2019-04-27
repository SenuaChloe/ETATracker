#!/bin/python3

import sys
import file_reader
import tracking_request
import tools

DEBUG_MODE=True

# Checking script parameters
if len(sys.argv) != 2:
    print("usage:    "+sys.argv[0]+" input_file")
    sys.exit()

# read input file
input_filename = sys.argv[1]
coord_list = file_reader.read_file(input_filename, DEBUG_MODE) # List of triplets (string, string, string)

# Computing times
eta_list = [] # list of pairs (string, string)
for (comment, string_from, string_to) in coord_list:
    tools.dprint(string_from+" :: "+string_to, DEBUG_MODE)
    request_result = tracking_request.tracking_request(string_from, string_to, DEBUG_MODE)
    eta_list.append( (comment, request_result) )


# Printing results
for (comment, eta) in eta_list:
    print("comment+": "+eta)

