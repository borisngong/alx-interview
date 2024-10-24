#!/usr/bin/python3
"""
Log Processor Script that reads HTTP request logs from stdin
and computes:
1. Total file size.
2. Counts of specific HTTP status codes.
"""

import sys


def print_statistics(status_code_counts, total_file_size):
    """
    Method to print the statistics of the log file.
    Prints total file size and counts of status codes.
    """
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))


# Initialize the total file size and status code counts
total_file_size = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

line_count = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line into components

        if len(parsed_line) > 2:
            try:
                # Extract file size and status code from the line
                file_size = int(parsed_line[-1])  # File size is the last component
                status_code = parsed_line[-2]  # Status code is the second-to-last component

                # Increment the total file size
                total_file_size += file_size

                # Update status code count if the status code is valid
                if status_code in status_code_count:
                    status_code_count[status_code] += 1

            except (ValueError, IndexError):
                # Skip line if there's an issue with parsing the file size or status code
                continue

            # Increment the line counter
            line_count += 1

            # Every 10 lines, print the statistics
            if line_count == 10:
                print_statistics(status_code_count, total_file_size)
                line_count = 0  # Reset the line counter

finally:
    # Print remaining statistics after the loop ends (or on interruption)
    print_statistics(status_code_count, total_file_size)
