# Step 3

# Purpose: detect possible brute-force attempts by counting authentication failures per rhost

# Usage: python3 count_attempts.py

import re
import os
from collections import defaultdict, deque
from datetime import datetime
import csv

LOG_FILE = "/home/stonney/Cybersecurity_projects/log-analysis/loghub/Linux/Linux_2k.log"
OUTPUT_DIR = "/home/stonney/Cybersecurity_projects/log-analysis/src/results"
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "alerts.csv")

# Detection parameters
THRESHOLD = 10           # number of failures
WINDOW_SECONDS = 120    # time window in seconds

# Regex to extract timestamp and rhost (and optional user)
pattern = re.compile(
    r"^(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*rhost=(?P<rhost>[\w\.\-\:]+).*user=(?P<user>[\w\-]+)?"
)

# Ensure results folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Keep per-IP deque of datetime objects
ip_windows = defaultdict(lambda: deque())

# Keep alerts to avoid duplicates (simple set of (ip, window_start, window_end, count))
alerts = []

# Current year for parsing (logs lack year)
CURRENT_YEAR = datetime.now().year

def parse_timestamp(ts_str):
    # ts_str example: "Jun 15 02:04:59"
    dt = datetime.strptime(f"{CURRENT_YEAR} {ts_str}", "%Y %b %d %H:%M:%S")
    return dt

with open(LOG_FILE, "r", errors="ignore") as fh:
    for line in fh:
        if "authentication failure" not in line:
            continue
        m = pattern.search(line)
        if not m:
            # Could be lines where 'user=' is missing — try to extract rhost only:
            rhost_match = re.search(r"rhost=([\w\.\-\:]+)", line)
            ts_match = re.match(r"^(?P<timestamp>\w{3}\s+\d+\s[\d:]+)", line)
            if not rhost_match or not ts_match:
                continue
            rhost = rhost_match.group(1)
            ts = parse_timestamp(ts_match.group("timestamp"))
            user = "-"
        else:
            ts = parse_timestamp(m.group("timestamp"))
            rhost = m.group("rhost")
            user = m.group("user") or "-"

        dq = ip_windows[rhost]
        dq.append(ts)

        # remove timestamps older than WINDOW_SECONDS from left
        cutoff = ts.timestamp() - WINDOW_SECONDS
        while dq and dq[0].timestamp() < cutoff:
            dq.popleft()

        # check threshold
        if len(dq) >= THRESHOLD:
            window_start = dq[0]
            window_end = dq[-1]
            alert = (rhost, window_start.isoformat(), window_end.isoformat(), len(dq), user)
            # simple dedupe: don't add if same ip and same window start already recorded
            if not any(a[0] == rhost and a[1] == alert[1] for a in alerts):
                alerts.append(alert)

# print brief summary
print(f"Total unique suspicious IPs: {len(alerts)}")
print("Sample alerts (first 10):")
for a in alerts[:10]:
    print(f"IP: {a[0]}  |  attempts: {a[3]}  |  window: {a[1]} -> {a[2]}  |  user: {a[4]}")

# Save to CSV
with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["rhost", "window_start", "window_end", "attempts", "user"])
    for a in alerts:
        writer.writerow(a)

print(f"\nAlerts saved to: {OUTPUT_CSV}")
