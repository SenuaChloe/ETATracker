#!/bin/python3

import sys

def eprint(string_message):
    sys.stderr.write("[ERROR] "+__file__+": "+string_message)


def dprint(string_message, DEBUG_MODE):
    if DEBUG_MODE:
        print("[DEBUG] "+__file__+": "+string_message)
