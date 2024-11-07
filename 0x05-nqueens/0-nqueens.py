#!/usr/bin/python3
"""
Module for working with N Queens problem solver
"""
import sys

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

size = int(sys.argv[1])

if size < 4:
    print("N must be at least 4")
    sys.exit(1)


def place_queens(size, row=0, queens_positions=[], pos_diags=[], neg_diags=[]):
    """Recursively generate valid queen positions"""
    if row == size:
        yield queens_positions
    else:
        for col in range(size):
            if (col not in queens_positions and
                    (row + col) not in pos_diags and
                    (row - col) not in neg_diags):
                yield from place_queens(
                    size,
                    row + 1,
                    queens_positions + [col],
                    pos_diags + [row + col],
                    neg_diags + [row - col]
                )


def display_solutions(size):
    """Print each solution for the N Queens problem."""
    for solution in place_queens(size):
        print([[r, c] for r, c in enumerate(solution)])


# Execute the solution display
display_solutions(size)
