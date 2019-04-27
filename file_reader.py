#!/bin/python3

import sys
import tools

def read_file(string_filepath, DEBUG_MODE=False):

    input_file = open(string_filepath)
    result = []

    for row in input_file:
        tools.dprint(row[:-1], DEBUG_MODE)
        row_sequence = row.split("|")
        if len(row_sequence) != 3:
            tools.eprint("Following line is ignored due to wrong format:")
            tools.eprint(row[:-1])
        else:
            description,string_from,string_to = row_sequence
            row_result = (description.strip(), string_from.strip(), string_to.strip())
            result.append(row_result)

    input_file.close()

    return result

