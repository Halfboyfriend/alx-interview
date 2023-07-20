#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""

from collections import defaultdict
import signal
import sys

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
total_file_size = 0
lines_by_status_code = defaultdict(int)
line_count = 0

def print_statistics():
    print(f"Total file size: File size: {total_file_size}")
    for status_code in sorted(status_codes):
        if lines_by_status_code[status_code]:
            print(f"{status_code}: {lines_by_status_code[status_code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue

        _, _, _, _, status_code, file_size, _ = parts

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_codes:
            total_file_size += file_size
            lines_by_status_code[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
