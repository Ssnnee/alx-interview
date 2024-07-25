#!/usr/bin/python3
"""This module implements a function that determines if a given data set"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0
    for byte in data:
        byte = byte & 255
        if num_bytes == 0:
            if (byte >> 5) == 6:
                return False
            elif (byte >> 4) == 14:
                num_bytes = 1
            elif (byte >> 3) == 30:
                num_bytes = 2
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 2:
                return False
            num_bytes -= 1
    return num_bytes == 0
