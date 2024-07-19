#!/usr/bin/python3
"""Module for stats function."""

"""Struture my thinking

The function have to reads stdin line by line and computes metrics.

1. Have to validate the input format wich is "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>"
2. The script have to print the following metrics after every 10 lines read from stdin and/or or a keyboard interruption:
    - Total file size: File size of all the logs
    - Number of lines by status code in ascending order

To solve this problem I will use the following steps:
1. Read the input from stdin
2. Validate the input format
3. Compute the metrics
4. Print the metrics
5. Handle the keyboard interruption
6. Print the metrics after every 10 lines read from stdin and/or or a keyboard interruption
"""


import sys


def print_metrics(total_file_size, status_codes):
    """Print the metrics."""
    print("File size: {}".format(total_file_size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(status_codes[key], key))
    return

def input_validator(line):
    """Validate the input format."""
    try:
        parsed_line = line.split()
        file_size = int(parsed_line[-1])
        status_code = parsed_line[-2]
        if len(parsed_line) < 2:
            return (0, None)
        return (file_size, status_code)
    except Exception:
        return (0, None)

def stats():
    """Reads stdin line by line and computes metrics."""
    total_file_size = 0
    status_codes = {}
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            file_size, status_code = input_validator(line)
            if file_size == 0:
                continue
            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if lines_read % 10 == 0:
                print_metrics(total_file_size, status_codes)
        print_metrics(total_file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes)
        raise


__name__ == "__main__" and stats()
