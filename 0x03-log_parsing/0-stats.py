#!/usr/bin/python3
import sys
import signal

# Dictionary to count each status code
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0


def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.strip().split()
            if len(parts) < 7:
                continue

            # Extract status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

        except Exception:
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Ensure final stats are printed after EOF
print_stats()

