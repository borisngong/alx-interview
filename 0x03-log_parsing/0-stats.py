#!/usr/bin/env python3
"""
This module contains log statistics for HTTP request logs
It parses logs, counts status codes, and sums file sizes and displayed
at regular intervals until termination
"""
import sys
import re


def initialize_logs():
    """
    Initialize the logs dictionary with file size and status codes
    """
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    logs = {
        'file_size': 0,
        'code_list': {str(code): 0 for code in status_codes}
    }
    return logs


def parse_line(line, regex, logs):
    """
    Parse a single line of the log file, updating logs with file size
    and status codes
    """
    match = regex.fullmatch(line)
    if match:
        status_code, file_size = match.group(3), match.group(4)
        logs['file_size'] += int(file_size)
        if status_code.isdecimal() and status_code in logs['code_list']:
            logs['code_list'][status_code] += 1
    return logs


def display_logs(logs):
    """
    Display the current logs with file size and status code counts
    """
    print(f"File size: {logs['file_size']}")
    for code, count in sorted(logs['code_list'].items()):
        if count > 0:
            print(f"{code}: {count}")


def main():
    """
    Main function to read lines from stdin, parse them, and display logs.

    It will display logs every 10 lines and catch KeyboardInterrupt to
    gracefully exit, showing the final logs before termination.
    """
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET '
        r'/projects/\d+ HTTP/1\.1" (\d{3}) (\d+)'
    )
    line_count = 0
    logs = initialize_logs()

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                logs = parse_line(line, regex, logs)
                line_count += 1
                if line_count % 10 == 0:
                    display_logs(logs)
    except BrokenPipeError:
        sys.stderr.write("Broken pipe error occurred.\n")
    finally:
        display_logs(logs)


if __name__ == '__main__':
    main()
