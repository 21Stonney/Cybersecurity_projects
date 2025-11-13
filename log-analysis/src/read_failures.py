#Step 1

# Path to your dataset (adjust if needed)
log_file = "/home/stonney/Cybersecurity_projects/log-analysis/loghub/Linux/Linux_2k.log"

# Open the log file
with open(log_file, "r") as f:
    for line in f:
        if "authentication failure" in line:
            print(line.strip())
