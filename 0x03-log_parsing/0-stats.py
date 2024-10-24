#!/usr/bin/env python3
"""
Log parsing script that reads from stdin and computes metrics.
"""

import sys
import re
from collections import defaultdict

def main():
    total_file_size = 0
    status_codes_count = defaultdict(int)
    line_count = 0

    # Regular expression to match the log line format
    log_line_pattern = re.compile(
        r'^(?P<ip>(?:\d{1,3}\.){3}\d{1,3}) - \[(?P<date>[^\]]+)\] '
        r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_line_pattern.match(line)

            if match:
                status_code = int(match.group('status_code'))
                file_size = int(match.group('file_size'))

                # Update metrics
                total_file_size += file_size
                status_codes_count[status_code] += 1
                line_count += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics(total_file_size, status_codes_count)

        # Print final metrics if the loop ends naturally
        print_metrics(total_file_size, status_codes_count)

    except KeyboardInterrupt:
        # Print metrics on keyboard interruption
        print_metrics(total_file_size, status_codes_count)
        sys.exit(0)

def print_metrics(total_file_size, status_codes_count):
    """Print the metrics in the required format."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        print(f"{status_code}: {status_codes_count[status_code]}")

if __name__ == "__main__":
    main()