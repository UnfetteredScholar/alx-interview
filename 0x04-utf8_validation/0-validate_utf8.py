#!/usr/bin/python3
"""
Defines the function validUTF8
"""


# def validUTF8(data):
#     """
#     Determines if data is
#     in valid UTF-8 Format
#     """
#     length = 0
#     for b in data:
#         if length == 0:
#             if (b >> 7) == 0:
#                 continue
#             elif (b >> 5) == 6:
#                 length = 1
#             elif (b >> 4) == 14:
#                 length = 2
#             elif (b >> 3) == 30:
#                 length = 3
#             else:
#                 return False
#         else:
#             if (b >> 6) != 2:
#                 return False
#             length -= 1

#     return length == 0


def validUTF8(data):
    """
    data: input list
    """
    n_bytes = 0

    for num in data:
        bin_rep = format(num, "#010b")[-8:]

        if n_bytes == 0:
            for bit in bin_rep:
                if bit == "0":
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_rep[0] == "1" and bin_rep[1] == "0"):
                return False
        n_bytes -= 1

    return n_bytes == 0
