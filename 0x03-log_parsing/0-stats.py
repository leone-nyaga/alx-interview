#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Dictionary to store status codes and their counts
status_count = defaultdict(int)
total_file_size = 0
lines_processed = 0

def print_stats():
    """Print the current statistics."""
    global total_file_size, status_count
    
    print(f"File size: {total_file_size}")
    
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")

def handle_interrupt(signum, frame):
    """Handle keyboard interruption."""
    print_stats()
    sys.exit(0)

# Set up signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        # Increment line counter
        lines_processed += 1
        
        # Process the line
        parts = line.split()
        if len(parts) != 7:
            continue
        
        try:
            status_code = int(parts[6])
            file_size = int(parts[5])
        except ValueError:
            continue
        
        if status_code not in {200, 301, 400, 401, 403, 404, 405, 500}:
            continue
        
        # Update statistics
        status_count[status_code] += 1
        total_file_size += file_size
        
        # Print stats after every 10 lines
        if lines_processed % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle manual interruption (CTRL + C)
    print_stats()
    sys.exit(0)

