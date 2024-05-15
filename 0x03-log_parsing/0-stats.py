#!/usr/bin/python3
""" Stats"""
import sys

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        # Check if format is valid
        if len(line.split()) != 9:
            continue
        ip, date, _, _, status_code, _, file_size = line.split()
        try:
            # Convert status code and file size to integers
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update metrics
        total_size += file_size
        if 200 <= status_code <= 500:
            status_counts[status_code] += 1

        # Print statistics every 10 lines or on keyboard interrupt
        if line_count % 10 == 0 or line_count == 1:
            print(f"Total file size: {total_size}")
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
