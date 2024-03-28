#!/usr/bin/python3
"""Parses HTTP logs from the standard input"""
import re
from typing import Dict


def process_input(line: str):
    """Processes a line of an HTTP request log."""
    fp = (
        r"\s*(?P<ip>\S+)\s*",
        r"\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]",
        r'\s*"(?P<request>[^"]*)"\s*',
        r"\s*(?P<status_code>\S+)",
        r"\s*(?P<file_size>\d+)",
    )
    info = {
        "status_code": 0,
        "file_size": 0,
    }
    log_fmt = "{}\\-{}{}{}{}\\s*".format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, line)
    if resp_match is not None:
        status_code = resp_match.group("status_code")
        file_size = int(resp_match.group("file_size"))
        info["status_code"] = status_code
        info["file_size"] = file_size
    return info


def print_log_stats(file_size: int, code_count: Dict[int, int]):
    """Prints the log stats"""
    print(f"File size: {file_size}", flush=True)
    keys = sorted(code_count.keys())
    for k in keys:
        if code_count[k] > 0:
            print(f"{k}: {code_count[k]}")


def update_metrics(
    line: str, total_file_size: int, status_codes_stats: Dict[int, int]
) -> int:
    """Updates the metrics from a given HTTP request log."""
    line_info = process_input(line)
    status_code = line_info.get("status_code", "0")
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info["file_size"]


def run() -> None:
    """Starts the log parser."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_log_stats(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_log_stats(total_file_size, status_codes_stats)


if __name__ == "__main__":
    run()
