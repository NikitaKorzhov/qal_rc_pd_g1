import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Generator, Tuple, Dict, Optional


def setup_logger(log_path: Path) -> logging.Logger:
    """Configure and return a logger instance outputting strictly to the target log file."""
    logger = logging.getLogger("HeartbeatLogger")
    logger.setLevel(logging.WARNING)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def parse_log_line(line: str) -> Optional[Tuple[datetime, str]]:
    """
    Extract timestamp and process key from a raw log entry.
    
    Supports timestamp formats like:
      - 2024-01-01 12:00:00,123 Key TSTFEED0300 ...
      - 2024-01-01T12:00:00 Key TSTFEED0300 ...
    """
    line = line.strip()
    if not line:
        return None

    # Regex pattern to capture timestamp and process key following 'Key'
    pattern = r"(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:[.,]\d+)?).*?Key\s+([A-Za-z0-9_-]+)"
    match = re.search(pattern, line)

    if not match:
        return None

    raw_dt, key = match.groups()
    
    # Normalize delimiter for parsing
    raw_dt = raw_dt.replace(',', '.').replace('T', ' ')
    
    try:
        if '.' in raw_dt:
            dt = datetime.strptime(raw_dt, "%Y-%m-%d %H:%M:%S.%f")
        else:
            dt = datetime.strptime(raw_dt, "%Y-%m-%d %H:%M:%S")
        return dt, key
    except ValueError:
        return None


def stream_log_entries(file_path: Path) -> Generator[Tuple[datetime, str], None, None]:
    """Generator streaming parsed (timestamp, process_key) tuples line-by-line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = parse_log_line(line)
            if entry:
                yield entry


def analyze_heartbeat_log(input_path: Path, output_path: Path):
    """
    Analyze heartbeat signals for each process key:
    - 31s < delay <= 33s -> WARNING
    - delay > 33s        -> ERROR
    """
    logger = setup_logger(output_path)
    
    last_seen: Dict[str, datetime] = {}
    max_delays: Dict[str, float] = {}

    for timestamp, key in stream_log_entries(input_path):
        if key in last_seen:
            prev_time = last_seen[key]
            delta_sec = (timestamp - prev_time).total_seconds()

            # Track maximum delay per process for bonus challenge
            if key not in max_delays or delta_sec > max_delays[key]:
                max_delays[key] = delta_sec

            # Verification rules
            if 31 < delta_sec <= 33:
                msg = f"Heartbeat interval for Key {key} was {delta_sec:.2f} seconds (Threshold: > 31s and <= 33s)"
                logger.warning(msg)
            elif delta_sec > 33:
                msg = f"Heartbeat interval for Key {key} was {delta_sec:.2f} seconds (Threshold: > 33s)"
                logger.error(msg)

        last_seen[key] = timestamp

    # Print longest heartbeat delay summary (Bonus section)
    print("=" * 65)
    print("LONGEST HEARTBEAT DELAY SUMMARY PER PROCESS:")
    print("=" * 65)
    for key, max_delay in sorted(max_delays.items(), key=lambda x: x[1], reverse=True):
        print(f"Process Key: {key:<15} | Longest Delay: {max_delay:.2f} seconds")
    print("=" * 65)


if __name__ == "__main__":
    # Path construction via pathlib inside main
    base_dir = Path(__file__).resolve().parent

    # Target file paths - analyze the real heartbeat log provided for the task
    input_file_path = base_dir / "hblog"
    output_file_path = base_dir / "hb_test.log"

    if not input_file_path.exists():
        raise FileNotFoundError(f"Heartbeat log not found at '{input_file_path}'")

    print(f"[INFO] Analyzing log file at: {input_file_path}")
    analyze_heartbeat_log(input_file_path, output_file_path)
    print(f"[INFO] Analysis complete. Log file written to: {output_file_path}")