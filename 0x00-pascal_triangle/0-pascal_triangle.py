#!/usr/bin/python3
"""
Script responsible for generating Pascal's triangle
up to nth row
"""


def pascal_triangle(n):
    """Returns Pascal's Triangle up to the nth row

    Args:
        n (int): The number of rows to generate

    Returns:
        A list of lists, where each sublist represents
        a row in Pascal's Triangle
    """
    if n <= 0:
        return []

    p_triangle = [[1]]
    """Initialize the triangle with the first row"""

    for i in range(1, n):
        """Start row with 1"""
        row = [1]
        """middle vlues generation"""
        for j in range(1, i):
            row.append(p_triangle[i-1][j-1] + p_triangle[i-1][j])
        """row should end with 1"""
        row.append(1)
        p_triangle.append(row)

    return p_triangle
