#!/usr/bin/python3
"""Module for stats function.
This script reads stdin line by line and computes metrics
"""

import sys


def print_metrics(total_file_size, status_code_dic):
    """Print the metrics."""
    print("File size: {}".format(total_file_size))
    for key in sorted(status_code_dic.keys()):
        print("{}: {}".format(key, status_code_dic[key]))
    return


def input_parser(line):
    """Parse input and return the <status code> and <file size>"""
    try:
        parsed_line = line.split()
        file_size = int(parsed_line[-1])
        status_code = int(parsed_line[-2])

        if (len(line) < 2):
            return (0, None)
        return (file_size, status_code)
    except Exception:
        return (0, None)


def stats():
    """Main funcion of the script"""
    total_file_size = 0
    status_code_dic = {}
    i = 0

    try:
        for line in sys.stdin:
            file_size, status_code = input_parser(line)
            i += 1
            total_file_size += file_size
            if status_code in status_code_dic:
                status_code_dic[status_code] += 1
            else:
                status_code_dic[status_code] = 1
            if i % 10 == 0:
                print_metrics(total_file_size, status_code_dic)

        if i % 10 != 0:
            print_metrics(total_file_size, status_code_dic)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_dic)

    if (total_file_size == 0):
        print_metrics(total_file_size, status_code_dic)


__name__ == "__main__" and stats()
