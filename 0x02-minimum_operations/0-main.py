#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__("0-minoperations").minOperations

for n in range(-2, 1000, 1):
    m1 = minOperations(n)
    print("Min # of operations to reach {} char: {}".format(n, m1))
    print("======================")
