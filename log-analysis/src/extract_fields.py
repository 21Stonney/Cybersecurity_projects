# Step 2

# Purpose: Extract timestamp, rhost, and username from authentication failure logs

import re

log_file = "/home/stonney/Cybersecurity_projects/log-analysis/loghub/Linux/Linux_2k.log"

# Regex pattern for fields
pattern = re.compile(
    r"^(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*rhost=(?P<rhost>[\w\.\-]+).*user=(?P<user>\w+)?"
)

with open(log_file, "r") as f:
    for line in f:
        if "authentication failure" in line:
            match = pattern.search(line)
            if match:
                timestamp = match.group("timestamp")
                rhost = match.group("rhost")
                user = match.group("user") if match.group("user") else "-"
                print(f"{timestamp} | {rhost} | {user}")
