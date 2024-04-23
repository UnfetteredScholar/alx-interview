#!/usr/bin/python3
"""Defines rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """Rotates an NxN matrix by 90 degrees"""
    N = len(matrix)
    new_matrix = [[] for i in range(N)]

    for row in matrix:
        i = 0
        for i in range(N):
            new_matrix[i].insert(0, row[i])

    for r in range(N):
        for c in range(N):
            matrix[r][c] = new_matrix[r][c]
