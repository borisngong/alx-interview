#!/usr/bin/python3
"""
Log Processor Script that tracks reads HTTP request logs from
standard input and tracks Total file size, Counts of specific
HTTP status codes
"""
import sys


def print_statistics(status_code_counts, total_file_size):
    """
    Method to print the statistics of the log file
    """
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))


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
        parsed_line = line.split()  # Splitting the line into components
        parsed_line = parsed_line[::-1]  # Reversing the order of components

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                file_size = int(parsed_line[0])  # File size is now clearer
                status_code = parsed_line[1]  # Status code is now clearer

                if status_code in status_code_count.keys():
                    status_code_count[status_code] += 1

            if line_count == 10:
                print_statistics(status_code_count, total_file_size)
                line_count = 0

finally:
    print_statistics(status_code_count, total_file_size)
