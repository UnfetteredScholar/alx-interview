#!/usr/bin/python3
"""Parses logs from the standard input"""
import re
import signal
import sys
from typing import Dict

if __name__ == "__main__":
    line_pattern = (
        r'\d+\.\d+\.\d+\.\d+\s-\s\[.+\]\s"'
        + r'GET\s\/projects\/260\sHTTP\/1.1"\s\d{3}\s\d+'
    )
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0
    file_size = 0
    code_count = {}

    def print_log_stats(file_size: int, code_count: Dict[int, int]):
        """Prints the log stats"""
        print(f"File size: {file_size}")
        keys = sorted(code_count.keys())
        for k in keys:
            print(f"{k}: {code_count[k]}")

    def signal_handler(sig, frame):
        """Handles the keyboard interrupt (CTRL + C)"""
        print_log_stats(file_size, code_count)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        if re.match(line_pattern, line):
            parts = line.split(" ")
            file_size += int(parts[-1])
            code = parts[-2]
            if code.isdigit() and int(code) in status_codes:
                code = int(code)
                if code in code_count:
                    code_count[code] += 1
                else:
                    code_count[code] = 1

            count += 1

        if count % 10 == 0:
            print_log_stats(file_size, code_count)
            file_size = 0
            code_count = {}
