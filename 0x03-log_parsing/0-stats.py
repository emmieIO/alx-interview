#!/usr/bin/python3
""" Stats"""
from collections import defaultdict


def parse_line(line):
    """
    Parses a line in the expected format and returns a dictionary with data.

    Args:
        line: The line to parse.

    Returns:
        A dictionary containing IP address, date (optional),
        path, status code, and file size (optional).
    """
    try:
        # Split the line based on spaces
        parts = line.split()

        # Extract data from specific parts
        ip = parts[0]
        status_code = int(parts[-2])
        file_size = None

        # Check for optional date
        if len(parts) > 4 and parts[1].startswith("[") and parts[1].endswith("]"):
            date = parts[1][1:-1]
            path = parts[3]
        else:
            date = None
            path = parts[2]

        # Check for optional file size
        if len(parts) > 5:
            try:
                file_size = int(parts[-1])
            except ValueError:
                pass  # Ignore invalid file size

        return {
            "ip": ip,
            "date": date,
            "path": path,
            "status_code": status_code,
            "file_size": file_size,
        }
    except (IndexError, ValueError):
        # Ignore lines that don't follow the expected format
        return None


def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in iter(input, ""):
            data = parse_line(line)

            if not data:
                continue  # Skip invalid lines

            line_count += 1
            total_size += data.get("file_size", 0)
            status_counts[data["status_code"]] += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code, count in sorted(status_counts.items()):
                    print(f"{code}: {count}")

                # Reset counters for next iteration
                line_count = 0
                status_counts = defaultdict(int)
    except KeyboardInterrupt:
        # Print statistics on KeyboardInterrupt
        print(f"Total file size: {total_size}")
        for code, count in sorted(status_counts.items()):
            print(f"{code}: {count}")


if __name__ == "__main__":
    main()
