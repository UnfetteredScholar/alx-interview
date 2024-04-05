#!/usr/bin/python3
"""
Defines the function validUTF8
"""


def validUTF8(data):
    """
    Determines if data is
    in valid UTF-8 Format
    """
    length = 0
    for b in data:
        b = b & 0b11111111
        if length == 0:
            if (b >> 7) == 0:
                continue
            elif (b >> 5) == 6:
                length = 1
            elif (b >> 4) == 14:
                length = 2
            elif (b >> 3) == 30:
                length = 3
            else:
                return False
        else:
            if (b >> 6) != 2:
                return False
            length -= 1

    return length == 0
