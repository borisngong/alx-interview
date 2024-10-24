#!/usr/bin/python3
"""
Log Processor Script that tracks reads HTTP request logs from
standard input and tracks Total file size, Counts of specific
HTTP status codes 
"""
import sys

# Initialize variables
total_file_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


# Read input line by line from stdin
for line in sys.stdin:
    line_count += 1
    try:
        # Split the line into parts
        parts = line.split()

        # Parse the important values from the log line
        ip = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update the total file size
        total_file_size += file_size

        # Update the status code count if it's valid
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    except (IndexError, ValueError):
        continue

    if line_count % 10 == 0:
        print_stats()
