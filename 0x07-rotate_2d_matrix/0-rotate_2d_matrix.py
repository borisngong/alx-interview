#!/usr/bin/python3
"""
Module for working with and rotating 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Responsible for rotating a  n x n 2D matrix 90 degrees
    clockwise in place

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate
    """
    n = len(matrix)

    # Perform layer-by-layer rotation
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Offset to track the current index within the layer
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top
